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

from google.cloud.apihub_v1.types import common_fields

__protobuf__ = proto.module(
    package="google.cloud.apihub.v1",
    manifest={
        "CreateApiRequest",
        "GetApiRequest",
        "UpdateApiRequest",
        "DeleteApiRequest",
        "ListApisRequest",
        "ListApisResponse",
        "CreateVersionRequest",
        "GetVersionRequest",
        "UpdateVersionRequest",
        "DeleteVersionRequest",
        "ListVersionsRequest",
        "ListVersionsResponse",
        "CreateSpecRequest",
        "GetSpecRequest",
        "UpdateSpecRequest",
        "DeleteSpecRequest",
        "ListSpecsRequest",
        "ListSpecsResponse",
        "GetSpecContentsRequest",
        "CreateApiOperationRequest",
        "GetApiOperationRequest",
        "UpdateApiOperationRequest",
        "DeleteApiOperationRequest",
        "ListApiOperationsRequest",
        "ListApiOperationsResponse",
        "GetDefinitionRequest",
        "CreateDeploymentRequest",
        "GetDeploymentRequest",
        "UpdateDeploymentRequest",
        "DeleteDeploymentRequest",
        "ListDeploymentsRequest",
        "ListDeploymentsResponse",
        "CreateAttributeRequest",
        "GetAttributeRequest",
        "UpdateAttributeRequest",
        "DeleteAttributeRequest",
        "ListAttributesRequest",
        "ListAttributesResponse",
        "SearchResourcesRequest",
        "ApiHubResource",
        "SearchResult",
        "SearchResourcesResponse",
        "CreateDependencyRequest",
        "GetDependencyRequest",
        "UpdateDependencyRequest",
        "DeleteDependencyRequest",
        "ListDependenciesRequest",
        "ListDependenciesResponse",
        "CreateExternalApiRequest",
        "GetExternalApiRequest",
        "UpdateExternalApiRequest",
        "DeleteExternalApiRequest",
        "ListExternalApisRequest",
        "ListExternalApisResponse",
    },
)


class CreateApiRequest(proto.Message):
    r"""The [CreateApi][google.cloud.apihub.v1.ApiHub.CreateApi] method's
    request.

    Attributes:
        parent (str):
            Required. The parent resource for the API resource. Format:
            ``projects/{project}/locations/{location}``
        api_id (str):
            Optional. The ID to use for the API resource, which will
            become the final component of the API's resource name. This
            field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              API resource in the API hub.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, and valid characters
            are /[a-z][A-Z][0-9]-\_/.
        api (google.cloud.apihub_v1.types.Api):
            Required. The API resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    api: common_fields.Api = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.Api,
    )


class GetApiRequest(proto.Message):
    r"""The [GetApi][google.cloud.apihub.v1.ApiHub.GetApi] method's request.

    Attributes:
        name (str):
            Required. The name of the API resource to retrieve. Format:
            ``projects/{project}/locations/{location}/apis/{api}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateApiRequest(proto.Message):
    r"""The [UpdateApi][google.cloud.apihub.v1.ApiHub.UpdateApi] method's
    request.

    Attributes:
        api (google.cloud.apihub_v1.types.Api):
            Required. The API resource to update.

            The API resource's ``name`` field is used to identify the
            API resource to update. Format:
            ``projects/{project}/locations/{location}/apis/{api}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    api: common_fields.Api = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.Api,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteApiRequest(proto.Message):
    r"""The [DeleteApi][google.cloud.apihub.v1.ApiHub.DeleteApi] method's
    request.

    Attributes:
        name (str):
            Required. The name of the API resource to delete. Format:
            ``projects/{project}/locations/{location}/apis/{api}``
        force (bool):
            Optional. If set to true, any versions from
            this API will also be deleted. Otherwise, the
            request will only work if the API has no
            versions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListApisRequest(proto.Message):
    r"""The [ListApis][google.cloud.apihub.v1.ApiHub.ListApis] method's
    request.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of API
            resources. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            Optional. An expression that filters the list of
            ApiResources.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. The comparison operator must be one of: ``<``,
            ``>``, ``:`` or ``=``. Filters are not case sensitive.

            The following fields in the ``ApiResource`` are eligible for
            filtering:

            - ``owner.email`` - The email of the team which owns the
              ApiResource. Allowed comparison operators: ``=``.
            - ``create_time`` - The time at which the ApiResource was
              created. The value should be in the
              (RFC3339)[https://tools.ietf.org/html/rfc3339] format.
              Allowed comparison operators: ``>`` and ``<``.
            - ``display_name`` - The display name of the ApiResource.
              Allowed comparison operators: ``=``.
            - ``target_user.enum_values.values.id`` - The allowed value
              id of the target users attribute associated with the
              ApiResource. Allowed comparison operator is ``:``.
            - ``target_user.enum_values.values.display_name`` - The
              allowed value display name of the target users attribute
              associated with the ApiResource. Allowed comparison
              operator is ``:``.
            - ``team.enum_values.values.id`` - The allowed value id of
              the team attribute associated with the ApiResource.
              Allowed comparison operator is ``:``.
            - ``team.enum_values.values.display_name`` - The allowed
              value display name of the team attribute associated with
              the ApiResource. Allowed comparison operator is ``:``.
            - ``business_unit.enum_values.values.id`` - The allowed
              value id of the business unit attribute associated with
              the ApiResource. Allowed comparison operator is ``:``.
            - ``business_unit.enum_values.values.display_name`` - The
              allowed value display name of the business unit attribute
              associated with the ApiResource. Allowed comparison
              operator is ``:``.
            - ``maturity_level.enum_values.values.id`` - The allowed
              value id of the maturity level attribute associated with
              the ApiResource. Allowed comparison operator is ``:``.
            - ``maturity_level.enum_values.values.display_name`` - The
              allowed value display name of the maturity level attribute
              associated with the ApiResource. Allowed comparison
              operator is ``:``.
            - ``api_style.enum_values.values.id`` - The allowed value id
              of the api style attribute associated with the
              ApiResource. Allowed comparison operator is ``:``.
            - ``api_style.enum_values.values.display_name`` - The
              allowed value display name of the api style attribute
              associated with the ApiResource. Allowed comparison
              operator is ``:``.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id``
              - The allowed value id of the user defined enum attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-enum-id is a
              placeholder that can be replaced with any user defined
              enum attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name``

            - The allowed value display name of the user defined enum
              attribute associated with the Resource. Allowed comparison
              operator is ``:``. Here
              user-defined-attribute-enum-display-name is a placeholder
              that can be replaced with any user defined enum attribute
              enum name.

            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values``
              - The allowed value of the user defined string attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-string is a
              placeholder that can be replaced with any user defined
              string attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values``
              - The allowed value of the user defined JSON attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-json is a
              placeholder that can be replaced with any user defined
              JSON attribute name.

            A filter function is also supported in the filter string.
            The filter function is ``id(name)``. The ``id(name)``
            function returns the id of the resource name. For example,
            ``id(name) = \"api-1\"`` is equivalent to
            ``name = \"projects/test-project-id/locations/test-location-id/apis/api-1\"``
            provided the parent is
            ``projects/test-project-id/locations/test-location-id``.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            Here are a few examples:

            - ``owner.email = \"apihub@google.com\"`` - - The owner team
              email is *apihub@google.com*.
            - ``owner.email = \"apihub@google.com\" AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\"``
              - The owner team email is *apihub@google.com* and the api
              was created before *2021-08-15 14:50:00 UTC* and after
              *2021-08-10 12:00:00 UTC*.
            - ``owner.email = \"apihub@google.com\" OR team.enum_values.values.id: apihub-team-id``
              - The filter string specifies the APIs where the owner
              team email is *apihub@google.com* or the id of the allowed
              value associated with the team attribute is
              *apihub-team-id*.
            - ``owner.email = \"apihub@google.com\" OR team.enum_values.values.display_name: ApiHub Team``
              - The filter string specifies the APIs where the owner
              team email is *apihub@google.com* or the display name of
              the allowed value associated with the team attribute is
              ``ApiHub Team``.
            - ``owner.email = \"apihub@google.com\" AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.enum_values.values.id: test_enum_id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/1765\0f90-4a29-5431-b3d0-d5532da3764c.string_values.values: test_string_value``
              - The filter string specifies the APIs where the owner
              team email is *apihub@google.com* and the id of the
              allowed value associated with the user defined attribute
              of type enum is *test_enum_id* and the value of the user
              defined attribute of type string is *test*..
        page_size (int):
            Optional. The maximum number of API resources
            to return. The service may return fewer than
            this value. If unspecified, at most 50 Apis will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListApis`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters (except page_size)
            provided to ``ListApis`` must match the call that provided
            the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListApisResponse(proto.Message):
    r"""The [ListApis][google.cloud.apihub.v1.ApiHub.ListApis] method's
    response.

    Attributes:
        apis (MutableSequence[google.cloud.apihub_v1.types.Api]):
            The API resources present in the API hub.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    apis: MutableSequence[common_fields.Api] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.Api,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateVersionRequest(proto.Message):
    r"""The [CreateVersion][google.cloud.apihub.v1.ApiHub.CreateVersion]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for API version. Format:
            ``projects/{project}/locations/{location}/apis/{api}``
        version_id (str):
            Optional. The ID to use for the API version, which will
            become the final component of the version's resource name.
            This field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              version in the API resource.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, overall resource name
            which will be of format
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``,
            its length is limited to 700 characters and valid characters
            are /[a-z][A-Z][0-9]-\_/.
        version (google.cloud.apihub_v1.types.Version):
            Required. The version to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: common_fields.Version = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.Version,
    )


class GetVersionRequest(proto.Message):
    r"""The [GetVersion][google.cloud.apihub.v1.ApiHub.GetVersion] method's
    request.

    Attributes:
        name (str):
            Required. The name of the API version to retrieve. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateVersionRequest(proto.Message):
    r"""The [UpdateVersion][google.cloud.apihub.v1.ApiHub.UpdateVersion]
    method's request.

    Attributes:
        version (google.cloud.apihub_v1.types.Version):
            Required. The API version to update.

            The version's ``name`` field is used to identify the API
            version to update. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    version: common_fields.Version = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.Version,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteVersionRequest(proto.Message):
    r"""The [DeleteVersion][google.cloud.apihub.v1.ApiHub.DeleteVersion]
    method's request.

    Attributes:
        name (str):
            Required. The name of the version to delete. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``
        force (bool):
            Optional. If set to true, any specs from this
            version will also be deleted. Otherwise, the
            request will only work if the version has no
            specs.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListVersionsRequest(proto.Message):
    r"""The [ListVersions][google.cloud.apihub.v1.ApiHub.ListVersions]
    method's request.

    Attributes:
        parent (str):
            Required. The parent which owns this collection of API
            versions i.e., the API resource Format:
            ``projects/{project}/locations/{location}/apis/{api}``
        filter (str):
            Optional. An expression that filters the list of Versions.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string, a number, or a boolean. The comparison operator must
            be one of: ``<``, ``>`` or ``=``. Filters are not case
            sensitive.

            The following fields in the ``Version`` are eligible for
            filtering:

            - ``display_name`` - The display name of the Version.
              Allowed comparison operators: ``=``.
            - ``create_time`` - The time at which the Version was
              created. The value should be in the
              (RFC3339)[https://tools.ietf.org/html/rfc3339] format.
              Allowed comparison operators: ``>`` and ``<``.
            - ``lifecycle.enum_values.values.id`` - The allowed value id
              of the lifecycle attribute associated with the Version.
              Allowed comparison operators: ``:``.
            - ``lifecycle.enum_values.values.display_name`` - The
              allowed value display name of the lifecycle attribute
              associated with the Version. Allowed comparison operators:
              ``:``.
            - ``compliance.enum_values.values.id`` - The allowed value
              id of the compliances attribute associated with the
              Version. Allowed comparison operators: ``:``.
            - ``compliance.enum_values.values.display_name`` - The
              allowed value display name of the compliances attribute
              associated with the Version. Allowed comparison operators:
              ``:``.
            - ``accreditation.enum_values.values.id`` - The allowed
              value id of the accreditations attribute associated with
              the Version. Allowed comparison operators: ``:``.
            - ``accreditation.enum_values.values.display_name`` - The
              allowed value display name of the accreditations attribute
              associated with the Version. Allowed comparison operators:
              ``:``.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id``
              - The allowed value id of the user defined enum attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-enum-id is a
              placeholder that can be replaced with any user defined
              enum attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name``

            - The allowed value display name of the user defined enum
              attribute associated with the Resource. Allowed comparison
              operator is ``:``. Here
              user-defined-attribute-enum-display-name is a placeholder
              that can be replaced with any user defined enum attribute
              enum name.

            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values``
              - The allowed value of the user defined string attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-string is a
              placeholder that can be replaced with any user defined
              string attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values``
              - The allowed value of the user defined JSON attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-json is a
              placeholder that can be replaced with any user defined
              JSON attribute name.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            Here are a few examples:

            - ``lifecycle.enum_values.values.id: preview-id`` - The
              filter string specifies that the id of the allowed value
              associated with the lifecycle attribute of the Version is
              *preview-id*.
            - ``lifecycle.enum_values.values.display_name: \"Preview Display Name\"``
              - The filter string specifies that the display name of the
              allowed value associated with the lifecycle attribute of
              the Version is ``Preview Display Name``.
            - ``lifecycle.enum_values.values.id: preview-id AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\"``
              - The id of the allowed value associated with the
              lifecycle attribute of the Version is *preview-id* and it
              was created before *2021-08-15 14:50:00 UTC* and after
              *2021-08-10 12:00:00 UTC*.
            - ``compliance.enum_values.values.id: gdpr-id OR compliance.enum_values.values.id: pci-dss-id``

            - The id of the allowed value associated with the compliance
              attribute is *gdpr-id* or *pci-dss-id*.

            - ``lifecycle.enum_values.values.id: preview-id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.string_values.values: test``
              - The filter string specifies that the id of the allowed
              value associated with the lifecycle attribute of the
              Version is *preview-id* and the value of the user defined
              attribute of type string is *test*.
        page_size (int):
            Optional. The maximum number of versions to
            return. The service may return fewer than this
            value. If unspecified, at most 50 versions will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListVersions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListVersions`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListVersionsResponse(proto.Message):
    r"""The [ListVersions][google.cloud.apihub.v1.ApiHub.ListVersions]
    method's response.

    Attributes:
        versions (MutableSequence[google.cloud.apihub_v1.types.Version]):
            The versions corresponding to an API.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    versions: MutableSequence[common_fields.Version] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.Version,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateSpecRequest(proto.Message):
    r"""The [CreateSpec][google.cloud.apihub.v1.ApiHub.CreateSpec] method's
    request.

    Attributes:
        parent (str):
            Required. The parent resource for Spec. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``
        spec_id (str):
            Optional. The ID to use for the spec, which will become the
            final component of the spec's resource name. This field is
            optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              spec in the API resource.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, overall resource name
            which will be of format
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``,
            its length is limited to 1000 characters and valid
            characters are /[a-z][A-Z][0-9]-\_/.
        spec (google.cloud.apihub_v1.types.Spec):
            Required. The spec to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    spec_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    spec: common_fields.Spec = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.Spec,
    )


class GetSpecRequest(proto.Message):
    r"""The [GetSpec][google.cloud.apihub.v1.ApiHub.GetSpec] method's
    request.

    Attributes:
        name (str):
            Required. The name of the spec to retrieve. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSpecRequest(proto.Message):
    r"""The [UpdateSpec][google.cloud.apihub.v1.ApiHub.UpdateSpec] method's
    request.

    Attributes:
        spec (google.cloud.apihub_v1.types.Spec):
            Required. The spec to update.

            The spec's ``name`` field is used to identify the spec to
            update. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    spec: common_fields.Spec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.Spec,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSpecRequest(proto.Message):
    r"""The [DeleteSpec][google.cloud.apihub.v1.ApiHub.DeleteSpec] method's
    request.

    Attributes:
        name (str):
            Required. The name of the spec to delete. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSpecsRequest(proto.Message):
    r"""The [ListSpecs][ListSpecs] method's request.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of specs.
            Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``
        filter (str):
            Optional. An expression that filters the list of Specs.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. The comparison operator must be one of: ``<``,
            ``>``, ``:`` or ``=``. Filters are not case sensitive.

            The following fields in the ``Spec`` are eligible for
            filtering:

            - ``display_name`` - The display name of the Spec. Allowed
              comparison operators: ``=``.
            - ``create_time`` - The time at which the Spec was created.
              The value should be in the
              (RFC3339)[https://tools.ietf.org/html/rfc3339] format.
              Allowed comparison operators: ``>`` and ``<``.
            - ``spec_type.enum_values.values.id`` - The allowed value id
              of the spec_type attribute associated with the Spec.
              Allowed comparison operators: ``:``.
            - ``spec_type.enum_values.values.display_name`` - The
              allowed value display name of the spec_type attribute
              associated with the Spec. Allowed comparison operators:
              ``:``.
            - ``lint_response.json_values.values`` - The json value of
              the lint_response attribute associated with the Spec.
              Allowed comparison operators: ``:``.
            - ``mime_type`` - The MIME type of the Spec. Allowed
              comparison operators: ``=``.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id``
              - The allowed value id of the user defined enum attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-enum-id is a
              placeholder that can be replaced with any user defined
              enum attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name``

            - The allowed value display name of the user defined enum
              attribute associated with the Resource. Allowed comparison
              operator is ``:``. Here
              user-defined-attribute-enum-display-name is a placeholder
              that can be replaced with any user defined enum attribute
              enum name.

            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values``
              - The allowed value of the user defined string attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-string is a
              placeholder that can be replaced with any user defined
              string attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values``
              - The allowed value of the user defined JSON attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-json is a
              placeholder that can be replaced with any user defined
              JSON attribute name.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            Here are a few examples:

            - ``spec_type.enum_values.values.id: rest-id`` - The filter
              string specifies that the id of the allowed value
              associated with the spec_type attribute is *rest-id*.
            - ``spec_type.enum_values.values.display_name: \"Rest Display Name\"``
              - The filter string specifies that the display name of the
              allowed value associated with the spec_type attribute is
              ``Rest Display Name``.
            - ``spec_type.enum_values.values.id: grpc-id AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\"``
              - The id of the allowed value associated with the
              spec_type attribute is *grpc-id* and the spec was created
              before *2021-08-15 14:50:00 UTC* and after *2021-08-10
              12:00:00 UTC*.
            - ``spec_type.enum_values.values.id: rest-id OR spec_type.enum_values.values.id: grpc-id``

            - The id of the allowed value associated with the spec_type
              attribute is *rest-id* or *grpc-id*.

            - ``spec_type.enum_values.values.id: rest-id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.enum_values.values.id: test``
              - The filter string specifies that the id of the allowed
              value associated with the spec_type attribute is *rest-id*
              and the id of the allowed value associated with the user
              defined attribute of type enum is *test*.
        page_size (int):
            Optional. The maximum number of specs to
            return. The service may return fewer than this
            value. If unspecified, at most 50 specs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSpecs`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListSpecs`` must match the call that provided the page
            token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListSpecsResponse(proto.Message):
    r"""The [ListSpecs][google.cloud.apihub.v1.ApiHub.ListSpecs] method's
    response.

    Attributes:
        specs (MutableSequence[google.cloud.apihub_v1.types.Spec]):
            The specs corresponding to an API Version.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    specs: MutableSequence[common_fields.Spec] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.Spec,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSpecContentsRequest(proto.Message):
    r"""The [GetSpecContents][google.cloud.apihub.v1.ApiHub.GetSpecContents]
    method's request.

    Attributes:
        name (str):
            Required. The name of the spec whose contents need to be
            retrieved. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateApiOperationRequest(proto.Message):
    r"""The
    [CreateApiOperation][google.cloud.apihub.v1.ApiHub.CreateApiOperation]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the operation resource.
            Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``
        api_operation_id (str):
            Optional. The ID to use for the operation resource, which
            will become the final component of the operation's resource
            name. This field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              operation resource in the API hub.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, overall resource name
            which will be of format
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``,
            its length is limited to 700 characters, and valid
            characters are /[a-z][A-Z][0-9]-\_/.
        api_operation (google.cloud.apihub_v1.types.ApiOperation):
            Required. The operation resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_operation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    api_operation: common_fields.ApiOperation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.ApiOperation,
    )


class GetApiOperationRequest(proto.Message):
    r"""The [GetApiOperation][google.cloud.apihub.v1.ApiHub.GetApiOperation]
    method's request.

    Attributes:
        name (str):
            Required. The name of the operation to retrieve. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateApiOperationRequest(proto.Message):
    r"""The
    [UpdateApiOperation][google.cloud.apihub.v1.ApiHub.UpdateApiOperation]
    method's request.

    Attributes:
        api_operation (google.cloud.apihub_v1.types.ApiOperation):
            Required. The apiOperation resource to update.

            The operation resource's ``name`` field is used to identify
            the operation resource to update. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    api_operation: common_fields.ApiOperation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.ApiOperation,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteApiOperationRequest(proto.Message):
    r"""The
    [DeleteApiOperation][google.cloud.apihub.v1.ApiHub.DeleteApiOperation]
    method's request.

    Attributes:
        name (str):
            Required. The name of the operation resource to delete.
            Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListApiOperationsRequest(proto.Message):
    r"""The
    [ListApiOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
    method's request.

    Attributes:
        parent (str):
            Required. The parent which owns this collection of
            operations i.e., the API version. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}``
        filter (str):
            Optional. An expression that filters the list of
            ApiOperations.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string or a boolean. The comparison operator must be one of:
            ``<``, ``>`` or ``=``. Filters are not case sensitive.

            The following fields in the ``ApiOperation`` are eligible
            for filtering:

            - ``name`` - The ApiOperation resource name. Allowed
              comparison operators: ``=``.
            - ``details.http_operation.path.path`` - The http
              operation's complete path relative to server endpoint.
              Allowed comparison operators: ``=``.
            - ``details.http_operation.method`` - The http operation
              method type. Allowed comparison operators: ``=``.
            - ``details.deprecated`` - Indicates if the ApiOperation is
              deprecated. Allowed values are True / False indicating the
              deprycation status of the ApiOperation. Allowed comparison
              operators: ``=``.
            - ``create_time`` - The time at which the ApiOperation was
              created. The value should be in the
              (RFC3339)[https://tools.ietf.org/html/rfc3339] format.
              Allowed comparison operators: ``>`` and ``<``.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id``
              - The allowed value id of the user defined enum attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-enum-id is a
              placeholder that can be replaced with any user defined
              enum attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name``

            - The allowed value display name of the user defined enum
              attribute associated with the Resource. Allowed comparison
              operator is ``:``. Here
              user-defined-attribute-enum-display-name is a placeholder
              that can be replaced with any user defined enum attribute
              enum name.

            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values``
              - The allowed value of the user defined string attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-string is a
              placeholder that can be replaced with any user defined
              string attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values``
              - The allowed value of the user defined JSON attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-json is a
              placeholder that can be replaced with any user defined
              JSON attribute name.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            Here are a few examples:

            - ``details.deprecated = True`` - The ApiOperation is
              deprecated.
            - ``details.http_operation.method = GET AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\"``
              - The method of the http operation of the ApiOperation is
              *GET* and the spec was created before *2021-08-15 14:50:00
              UTC* and after *2021-08-10 12:00:00 UTC*.
            - ``details.http_operation.method = GET OR details.http_operation.method = POST``.
              - The http operation of the method of ApiOperation is
              *GET* or *POST*.
            - ``details.deprecated = True AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.string_values.values: test``
              - The filter string specifies that the ApiOperation is
              deprecated and the value of the user defined attribute of
              type string is *test*.
        page_size (int):
            Optional. The maximum number of operations to
            return. The service may return fewer than this
            value. If unspecified, at most 50 operations
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListApiOperations`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListApiOperations`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListApiOperationsResponse(proto.Message):
    r"""The
    [ListApiOperations][google.cloud.apihub.v1.ApiHub.ListApiOperations]
    method's response.

    Attributes:
        api_operations (MutableSequence[google.cloud.apihub_v1.types.ApiOperation]):
            The operations corresponding to an API
            version.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    api_operations: MutableSequence[common_fields.ApiOperation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.ApiOperation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDefinitionRequest(proto.Message):
    r"""The [GetDefinition][google.cloud.apihub.v1.ApiHub.GetDefinition]
    method's request.

    Attributes:
        name (str):
            Required. The name of the definition to retrieve. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/definitions/{definition}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDeploymentRequest(proto.Message):
    r"""The
    [CreateDeployment][google.cloud.apihub.v1.ApiHub.CreateDeployment]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the deployment resource.
            Format: ``projects/{project}/locations/{location}``
        deployment_id (str):
            Optional. The ID to use for the deployment resource, which
            will become the final component of the deployment's resource
            name. This field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              deployment resource in the API hub.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, and valid characters
            are /[a-z][A-Z][0-9]-\_/.
        deployment (google.cloud.apihub_v1.types.Deployment):
            Required. The deployment resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    deployment: common_fields.Deployment = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.Deployment,
    )


class GetDeploymentRequest(proto.Message):
    r"""The [GetDeployment][google.cloud.apihub.v1.ApiHub.GetDeployment]
    method's request.

    Attributes:
        name (str):
            Required. The name of the deployment resource to retrieve.
            Format:
            ``projects/{project}/locations/{location}/deployments/{deployment}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDeploymentRequest(proto.Message):
    r"""The
    [UpdateDeployment][google.cloud.apihub.v1.ApiHub.UpdateDeployment]
    method's request.

    Attributes:
        deployment (google.cloud.apihub_v1.types.Deployment):
            Required. The deployment resource to update.

            The deployment resource's ``name`` field is used to identify
            the deployment resource to update. Format:
            ``projects/{project}/locations/{location}/deployments/{deployment}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    deployment: common_fields.Deployment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.Deployment,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteDeploymentRequest(proto.Message):
    r"""The
    [DeleteDeployment][google.cloud.apihub.v1.ApiHub.DeleteDeployment]
    method's request.

    Attributes:
        name (str):
            Required. The name of the deployment resource to delete.
            Format:
            ``projects/{project}/locations/{location}/deployments/{deployment}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDeploymentsRequest(proto.Message):
    r"""The [ListDeployments][google.cloud.apihub.v1.ApiHub.ListDeployments]
    method's request.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            deployment resources. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            Optional. An expression that filters the list of
            Deployments.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. The comparison operator must be one of: ``<``, ``>``
            or ``=``. Filters are not case sensitive.

            The following fields in the ``Deployments`` are eligible for
            filtering:

            - ``display_name`` - The display name of the Deployment.
              Allowed comparison operators: ``=``.
            - ``create_time`` - The time at which the Deployment was
              created. The value should be in the
              (RFC3339)[https://tools.ietf.org/html/rfc3339] format.
              Allowed comparison operators: ``>`` and ``<``.
            - ``resource_uri`` - A URI to the deployment resource.
              Allowed comparison operators: ``=``.
            - ``api_versions`` - The API versions linked to this
              deployment. Allowed comparison operators: ``:``.
            - ``source_project`` - The project/organization at source
              for the deployment. Allowed comparison operators: ``=``.
            - ``source_environment`` - The environment at source for the
              deployment. Allowed comparison operators: ``=``.
            - ``deployment_type.enum_values.values.id`` - The allowed
              value id of the deployment_type attribute associated with
              the Deployment. Allowed comparison operators: ``:``.
            - ``deployment_type.enum_values.values.display_name`` - The
              allowed value display name of the deployment_type
              attribute associated with the Deployment. Allowed
              comparison operators: ``:``.
            - ``slo.string_values.values`` -The allowed string value of
              the slo attribute associated with the deployment. Allowed
              comparison operators: ``:``.
            - ``environment.enum_values.values.id`` - The allowed value
              id of the environment attribute associated with the
              deployment. Allowed comparison operators: ``:``.
            - ``environment.enum_values.values.display_name`` - The
              allowed value display name of the environment attribute
              associated with the deployment. Allowed comparison
              operators: ``:``.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id``
              - The allowed value id of the user defined enum attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-enum-id is a
              placeholder that can be replaced with any user defined
              enum attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name``

            - The allowed value display name of the user defined enum
              attribute associated with the Resource. Allowed comparison
              operator is ``:``. Here
              user-defined-attribute-enum-display-name is a placeholder
              that can be replaced with any user defined enum attribute
              enum name.

            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values``
              - The allowed value of the user defined string attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-string is a
              placeholder that can be replaced with any user defined
              string attribute name.
            - ``attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values``
              - The allowed value of the user defined JSON attribute
              associated with the Resource. Allowed comparison operator
              is ``:``. Here user-defined-attribute-json is a
              placeholder that can be replaced with any user defined
              JSON attribute name.

            A filter function is also supported in the filter string.
            The filter function is ``id(name)``. The ``id(name)``
            function returns the id of the resource name. For example,
            ``id(name) = \"deployment-1\"`` is equivalent to
            ``name = \"projects/test-project-id/locations/test-location-id/deployments/deployment-1\"``
            provided the parent is
            ``projects/test-project-id/locations/test-location-id``.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            Here are a few examples:

            - ``environment.enum_values.values.id: staging-id`` - The
              allowed value id of the environment attribute associated
              with the Deployment is *staging-id*.
            - ``environment.enum_values.values.display_name: \"Staging Deployment\"``
              - The allowed value display name of the environment
              attribute associated with the Deployment is
              ``Staging Deployment``.
            - ``environment.enum_values.values.id: production-id AND create_time < \"2021-08-15T14:50:00Z\" AND create_time > \"2021-08-10T12:00:00Z\"``
              - The allowed value id of the environment attribute
              associated with the Deployment is *production-id* and
              Deployment was created before *2021-08-15 14:50:00 UTC*
              and after *2021-08-10 12:00:00 UTC*.
            - ``environment.enum_values.values.id: production-id OR slo.string_values.values: \"99.99%\"``

            - The allowed value id of the environment attribute
              Deployment is *production-id* or string value of the slo
              attribute is *99.99%*.

            - ``environment.enum_values.values.id: staging-id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.string_values.values: test``
              - The filter string specifies that the allowed value id of
              the environment attribute associated with the Deployment
              is *staging-id* and the value of the user defined
              attribute of type string is *test*.
        page_size (int):
            Optional. The maximum number of deployment
            resources to return. The service may return
            fewer than this value. If unspecified, at most
            50 deployments will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDeployments`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListDeployments`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDeploymentsResponse(proto.Message):
    r"""The [ListDeployments][google.cloud.apihub.v1.ApiHub.ListDeployments]
    method's response.

    Attributes:
        deployments (MutableSequence[google.cloud.apihub_v1.types.Deployment]):
            The deployment resources present in the API
            hub.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    deployments: MutableSequence[common_fields.Deployment] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.Deployment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAttributeRequest(proto.Message):
    r"""The [CreateAttribute][google.cloud.apihub.v1.ApiHub.CreateAttribute]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for Attribute. Format:
            ``projects/{project}/locations/{location}``
        attribute_id (str):
            Optional. The ID to use for the attribute, which will become
            the final component of the attribute's resource name. This
            field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              attribute resource in the API hub.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, and valid characters
            are /[a-z][A-Z][0-9]-\_/.
        attribute (google.cloud.apihub_v1.types.Attribute):
            Required. The attribute to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attribute_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attribute: common_fields.Attribute = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.Attribute,
    )


class GetAttributeRequest(proto.Message):
    r"""The [GetAttribute][google.cloud.apihub.v1.ApiHub.GetAttribute]
    method's request.

    Attributes:
        name (str):
            Required. The name of the attribute to retrieve. Format:
            ``projects/{project}/locations/{location}/attributes/{attribute}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAttributeRequest(proto.Message):
    r"""The [UpdateAttribute][google.cloud.apihub.v1.ApiHub.UpdateAttribute]
    method's request.

    Attributes:
        attribute (google.cloud.apihub_v1.types.Attribute):
            Required. The attribute to update.

            The attribute's ``name`` field is used to identify the
            attribute to update. Format:
            ``projects/{project}/locations/{location}/attributes/{attribute}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    attribute: common_fields.Attribute = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.Attribute,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAttributeRequest(proto.Message):
    r"""The [DeleteAttribute][google.cloud.apihub.v1.ApiHub.DeleteAttribute]
    method's request.

    Attributes:
        name (str):
            Required. The name of the attribute to delete. Format:
            ``projects/{project}/locations/{location}/attributes/{attribute}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAttributesRequest(proto.Message):
    r"""The [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for Attribute. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            Optional. An expression that filters the list of Attributes.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string or a boolean. The comparison operator must be one of:
            ``<``, ``>`` or ``=``. Filters are not case sensitive.

            The following fields in the ``Attribute`` are eligible for
            filtering:

            - ``display_name`` - The display name of the Attribute.
              Allowed comparison operators: ``=``.
            - ``definition_type`` - The definition type of the
              attribute. Allowed comparison operators: ``=``.
            - ``scope`` - The scope of the attribute. Allowed comparison
              operators: ``=``.
            - ``data_type`` - The type of the data of the attribute.
              Allowed comparison operators: ``=``.
            - ``mandatory`` - Denotes whether the attribute is mandatory
              or not. Allowed comparison operators: ``=``.
            - ``create_time`` - The time at which the Attribute was
              created. The value should be in the
              (RFC3339)[https://tools.ietf.org/html/rfc3339] format.
              Allowed comparison operators: ``>`` and ``<``.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            Here are a few examples:

            - ``display_name = production`` - - The display name of the
              attribute is *production*.
            - ``(display_name = production) AND (create_time < \"2021-08-15T14:50:00Z\") AND (create_time > \"2021-08-10T12:00:00Z\")``
              - The display name of the attribute is *production* and
              the attribute was created before *2021-08-15 14:50:00 UTC*
              and after *2021-08-10 12:00:00 UTC*.
            - ``display_name = production OR scope = api`` - The
              attribute where the display name is *production* or the
              scope is *api*.
        page_size (int):
            Optional. The maximum number of attribute
            resources to return. The service may return
            fewer than this value. If unspecified, at most
            50 attributes will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAttributes`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAttributes`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAttributesResponse(proto.Message):
    r"""The [ListAttributes][google.cloud.apihub.v1.ApiHub.ListAttributes]
    method's response.

    Attributes:
        attributes (MutableSequence[google.cloud.apihub_v1.types.Attribute]):
            The list of all attributes.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    attributes: MutableSequence[common_fields.Attribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.Attribute,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchResourcesRequest(proto.Message):
    r"""The [SearchResources][google.cloud.apihub.v1.ApiHub.SearchResources]
    method's request.

    Attributes:
        location (str):
            Required. The resource name of the location which will be of
            the type ``projects/{project_id}/locations/{location_id}``.
            This field is used to identify the instance of API-Hub in
            which resources should be searched.
        query (str):
            Required. The free text search query. This
            query can contain keywords which could be
            related to any detail of the API-Hub resources
            such display names, descriptions, attributes
            etc.
        filter (str):
            Optional. An expression that filters the list of search
            results.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string, a number, or a boolean. The comparison operator must
            be ``=``. Filters are not case sensitive.

            The following field names are eligible for filtering: \*
            ``resource_type`` - The type of resource in the search
            results. Must be one of the following: ``Api``,
            ``ApiOperation``, ``Deployment``, ``Definition``, ``Spec``
            or ``Version``. This field can only be specified once in the
            filter.

            Here are is an example:

            - ``resource_type = Api`` - The resource_type is *Api*.
        page_size (int):
            Optional. The maximum number of search results to return.
            The service may return fewer than this value. If unspecified
            at most 10 search results will be returned. If value is
            negative then ``INVALID_ARGUMENT`` error is returned. The
            maximum value is 25; values above 25 will be coerced to 25.
            While paginating, you can specify a new page size parameter
            for each page of search results to be listed.
        page_token (str):
            Optional. A page token, received from a previous
            [SearchResources][SearchResources] call. Specify this
            parameter to retrieve the next page of transactions.

            When paginating, you must specify the ``page_token``
            parameter and all the other parameters except
            [page_size][google.cloud.apihub.v1.SearchResourcesRequest.page_size]
            should be specified with the same value which was used in
            the previous call. If the other fields are set with a
            different value than the previous call then
            ``INVALID_ARGUMENT`` error is returned.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ApiHubResource(proto.Message):
    r"""ApiHubResource is one of the resources such as Api,
    Operation, Deployment, Definition, Spec and Version resources
    stored in API-Hub.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        api (google.cloud.apihub_v1.types.Api):
            This represents Api resource in search results. Only name,
            display_name, description and owner fields are populated in
            search results.

            This field is a member of `oneof`_ ``resource``.
        operation (google.cloud.apihub_v1.types.ApiOperation):
            This represents ApiOperation resource in
            search results. Only name, description, spec and
            details fields are populated in search results.

            This field is a member of `oneof`_ ``resource``.
        deployment (google.cloud.apihub_v1.types.Deployment):
            This represents Deployment resource in search results. Only
            name, display_name, description, deployment_type and
            api_versions fields are populated in search results.

            This field is a member of `oneof`_ ``resource``.
        spec (google.cloud.apihub_v1.types.Spec):
            This represents Spec resource in search results. Only name,
            display_name, description, spec_type and documentation
            fields are populated in search results.

            This field is a member of `oneof`_ ``resource``.
        definition (google.cloud.apihub_v1.types.Definition):
            This represents Definition resource in search
            results. Only name field is populated in search
            results.

            This field is a member of `oneof`_ ``resource``.
        version (google.cloud.apihub_v1.types.Version):
            This represents Version resource in search results. Only
            name, display_name, description, lifecycle, compliance and
            accreditation fields are populated in search results.

            This field is a member of `oneof`_ ``resource``.
    """

    api: common_fields.Api = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="resource",
        message=common_fields.Api,
    )
    operation: common_fields.ApiOperation = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="resource",
        message=common_fields.ApiOperation,
    )
    deployment: common_fields.Deployment = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="resource",
        message=common_fields.Deployment,
    )
    spec: common_fields.Spec = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="resource",
        message=common_fields.Spec,
    )
    definition: common_fields.Definition = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="resource",
        message=common_fields.Definition,
    )
    version: common_fields.Version = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="resource",
        message=common_fields.Version,
    )


class SearchResult(proto.Message):
    r"""Represents the search results.

    Attributes:
        resource (google.cloud.apihub_v1.types.ApiHubResource):
            This represents the ApiHubResource.
            Note: Only selected fields of the resources are
            populated in response.
    """

    resource: "ApiHubResource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ApiHubResource",
    )


class SearchResourcesResponse(proto.Message):
    r"""Response for the
    [SearchResources][google.cloud.apihub.v1.ApiHub.SearchResources]
    method.

    Attributes:
        search_results (MutableSequence[google.cloud.apihub_v1.types.SearchResult]):
            List of search results according to the
            filter and search query specified. The order of
            search results represents the ranking.
        next_page_token (str):
            Pass this token in the
            [SearchResourcesRequest][google.cloud.apihub.v1.SearchResourcesRequest]
            to continue to list results. If all results have been
            returned, this field is an empty string or not present in
            the response.
    """

    @property
    def raw_page(self):
        return self

    search_results: MutableSequence["SearchResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDependencyRequest(proto.Message):
    r"""The
    [CreateDependency][google.cloud.apihub.v1.ApiHubDependencies.CreateDependency]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the dependency resource.
            Format: ``projects/{project}/locations/{location}``
        dependency_id (str):
            Optional. The ID to use for the dependency resource, which
            will become the final component of the dependency's resource
            name. This field is optional.

            - If provided, the same will be used. The service will throw
              an error if duplicate id is provided by the client.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, and valid characters
            are ``[a-z][A-Z][0-9]-_``.
        dependency (google.cloud.apihub_v1.types.Dependency):
            Required. The dependency resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dependency_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dependency: common_fields.Dependency = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.Dependency,
    )


class GetDependencyRequest(proto.Message):
    r"""The [GetDependency][.ApiHubDependencies.GetDependency] method's
    request.

    Attributes:
        name (str):
            Required. The name of the dependency resource to retrieve.
            Format:
            ``projects/{project}/locations/{location}/dependencies/{dependency}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDependencyRequest(proto.Message):
    r"""The
    [UpdateDependency][google.cloud.apihub.v1.ApiHubDependencies.UpdateDependency]
    method's request.

    Attributes:
        dependency (google.cloud.apihub_v1.types.Dependency):
            Required. The dependency resource to update.

            The dependency's ``name`` field is used to identify the
            dependency to update. Format:
            ``projects/{project}/locations/{location}/dependencies/{dependency}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    dependency: common_fields.Dependency = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.Dependency,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteDependencyRequest(proto.Message):
    r"""The
    [DeleteDependency][google.cloud.apihub.v1.ApiHubDependencies.DeleteDependency]
    method's request.

    Attributes:
        name (str):
            Required. The name of the dependency resource to delete.
            Format:
            ``projects/{project}/locations/{location}/dependencies/{dependency}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDependenciesRequest(proto.Message):
    r"""The
    [ListDependencies][google.cloud.apihub.v1.ApiHubDependencies.ListDependencies]
    method's request.

    Attributes:
        parent (str):
            Required. The parent which owns this collection of
            dependency resources. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            Optional. An expression that filters the list of
            Dependencies.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. Allowed comparison operator is ``=``. Filters are
            not case sensitive.

            The following fields in the ``Dependency`` are eligible for
            filtering:

            - ``consumer.operation_resource_name`` - The operation
              resource name for the consumer entity involved in a
              dependency. Allowed comparison operators: ``=``.
            - ``consumer.external_api_resource_name`` - The external api
              resource name for the consumer entity involved in a
              dependency. Allowed comparison operators: ``=``.
            - ``supplier.operation_resource_name`` - The operation
              resource name for the supplier entity involved in a
              dependency. Allowed comparison operators: ``=``.
            - ``supplier.external_api_resource_name`` - The external api
              resource name for the supplier entity involved in a
              dependency. Allowed comparison operators: ``=``.

            Expressions are combined with either ``AND`` logic operator
            or ``OR`` logical operator but not both of them together
            i.e. only one of the ``AND`` or ``OR`` operator can be used
            throughout the filter string and both the operators cannot
            be used together. No other logical operators are supported.
            At most three filter fields are allowed in the filter string
            and if provided more than that then ``INVALID_ARGUMENT``
            error is returned by the API.

            For example,
            ``consumer.operation_resource_name = \"projects/p1/locations/global/apis/a1/versions/v1/operations/o1\" OR supplier.operation_resource_name = \"projects/p1/locations/global/apis/a1/versions/v1/operations/o1\"``
            - The dependencies with either consumer or supplier
            operation resource name as
            *projects/p1/locations/global/apis/a1/versions/v1/operations/o1*.
        page_size (int):
            Optional. The maximum number of dependency
            resources to return. The service may return
            fewer than this value. If unspecified, at most
            50 dependencies will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDependencies`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDependencies`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDependenciesResponse(proto.Message):
    r"""The
    [ListDependencies][google.cloud.apihub.v1.ApiHubDependencies.ListDependencies]
    method's response.

    Attributes:
        dependencies (MutableSequence[google.cloud.apihub_v1.types.Dependency]):
            The dependency resources present in the API
            hub.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    dependencies: MutableSequence[common_fields.Dependency] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.Dependency,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateExternalApiRequest(proto.Message):
    r"""The
    [CreateExternalApi][google.cloud.apihub.v1.ApiHub.CreateExternalApi]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the External API resource.
            Format: ``projects/{project}/locations/{location}``
        external_api_id (str):
            Optional. The ID to use for the External API resource, which
            will become the final component of the External API's
            resource name. This field is optional.

            - If provided, the same will be used. The service will throw
              an error if the specified id is already used by another
              External API resource in the API hub.
            - If not provided, a system generated id will be used.

            This value should be 4-500 characters, and valid characters
            are /[a-z][A-Z][0-9]-\_/.
        external_api (google.cloud.apihub_v1.types.ExternalApi):
            Required. The External API resource to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    external_api_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    external_api: common_fields.ExternalApi = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common_fields.ExternalApi,
    )


class GetExternalApiRequest(proto.Message):
    r"""The [GetExternalApi][google.cloud.apihub.v1.ApiHub.GetExternalApi]
    method's request.

    Attributes:
        name (str):
            Required. The name of the External API resource to retrieve.
            Format:
            ``projects/{project}/locations/{location}/externalApis/{externalApi}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateExternalApiRequest(proto.Message):
    r"""The
    [UpdateExternalApi][google.cloud.apihub.v1.ApiHub.UpdateExternalApi]
    method's request.

    Attributes:
        external_api (google.cloud.apihub_v1.types.ExternalApi):
            Required. The External API resource to update.

            The External API resource's ``name`` field is used to
            identify the External API resource to update. Format:
            ``projects/{project}/locations/{location}/externalApis/{externalApi}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    external_api: common_fields.ExternalApi = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common_fields.ExternalApi,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteExternalApiRequest(proto.Message):
    r"""The
    [DeleteExternalApi][google.cloud.apihub.v1.ApiHub.DeleteExternalApi]
    method's request.

    Attributes:
        name (str):
            Required. The name of the External API resource to delete.
            Format:
            ``projects/{project}/locations/{location}/externalApis/{externalApi}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExternalApisRequest(proto.Message):
    r"""The
    [ListExternalApis][google.cloud.apihub.v1.ApiHub.ListExternalApis]
    method's request.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of External
            API resources. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            Optional. The maximum number of External API
            resources to return. The service may return
            fewer than this value. If unspecified, at most
            50 ExternalApis will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListExternalApis`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListExternalApis`` must match the call that
            provided the page token.
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


class ListExternalApisResponse(proto.Message):
    r"""The
    [ListExternalApis][google.cloud.apihub.v1.ApiHub.ListExternalApis]
    method's response.

    Attributes:
        external_apis (MutableSequence[google.cloud.apihub_v1.types.ExternalApi]):
            The External API resources present in the API
            hub.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    external_apis: MutableSequence[common_fields.ExternalApi] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.ExternalApi,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
