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

from google.cloud.designcenter_v1.types import best_practices, catalog_management, iac

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "ListSpacesRequest",
        "ListSpacesResponse",
        "GetSpaceRequest",
        "CreateSpaceRequest",
        "UpdateSpaceRequest",
        "DeleteSpaceRequest",
        "GetCatalogRequest",
        "ListCatalogsRequest",
        "ListCatalogsResponse",
        "CreateCatalogRequest",
        "UpdateCatalogRequest",
        "DeleteCatalogRequest",
        "CreateCatalogTemplateRequest",
        "GetCatalogTemplateRequest",
        "ListCatalogTemplatesRequest",
        "ListCatalogTemplatesResponse",
        "UpdateCatalogTemplateRequest",
        "DeleteCatalogTemplateRequest",
        "CreateCatalogTemplateRevisionRequest",
        "GetCatalogTemplateRevisionRequest",
        "ListCatalogTemplateRevisionsRequest",
        "ListCatalogTemplateRevisionsResponse",
        "DeleteCatalogTemplateRevisionRequest",
        "FetchCatalogTemplateRevisionTFSourceRequest",
        "FetchCatalogTemplateRevisionTFSourceResponse",
        "FetchCatalogTemplateRevisionAssessmentReportRequest",
        "FetchCatalogTemplateRevisionAssessmentReportResponse",
    },
)


class ListSpacesRequest(proto.Message):
    r"""Message for requesting a list of spaces.

    Attributes:
        parent (str):
            Required. The name of the parent resource,
            for which spaces are listed.
        page_size (int):
            Optional. The maximum number of pages to
            return from this request. If unspecified, the
            value automatically reflects the number of
            results returned.
        page_token (str):
            Optional. If present, retrieve the next batch
            of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter that chooses which spaces
            to return.
        order_by (str):
            Optional. How the results are sorted.
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


class ListSpacesResponse(proto.Message):
    r"""Results returned from projects.locations.spaces.list.

    Attributes:
        spaces (MutableSequence[google.cloud.designcenter_v1.types.Space]):
            A list of spaces.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, nextPageToken is
            included. To get the next set of results, call
            this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    spaces: MutableSequence[catalog_management.Space] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=catalog_management.Space,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSpaceRequest(proto.Message):
    r"""Results returned from projects.locations.spaces.get.

    Attributes:
        name (str):
            Required. The space name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSpaceRequest(proto.Message):
    r"""Message for creating a space.

    Attributes:
        parent (str):
            Required. The parent in which to create a
            space.
        space_id (str):
            Required. The ID of the space to create.
        space (google.cloud.designcenter_v1.types.Space):
            Required. The space to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    space_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    space: catalog_management.Space = proto.Field(
        proto.MESSAGE,
        number=3,
        message=catalog_management.Space,
    )


class UpdateSpaceRequest(proto.Message):
    r"""Message for updating a space.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The fields to overwrite in the
            space update. If you don't provide a mask, all
            fields are overwritten.
        space (google.cloud.designcenter_v1.types.Space):
            Required. The space to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    space: catalog_management.Space = proto.Field(
        proto.MESSAGE,
        number=2,
        message=catalog_management.Space,
    )


class DeleteSpaceRequest(proto.Message):
    r"""Message for deleting a space.

    Attributes:
        name (str):
            Required. The space name.
        force (bool):
            Optional. If set to true, the space's
            children are also deleted. If false, the space
            is only deleted if it has no children.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class GetCatalogRequest(proto.Message):
    r"""Message for getting a catalog.

    Attributes:
        name (str):
            Required. The catalog name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCatalogsRequest(proto.Message):
    r"""Message for requesting a list of catalogs.

    Attributes:
        parent (str):
            Required. The parent space from which catalogs are listed.
            Format:
            ``projects/$project/locations/$location/spaces/$space``
        page_size (int):
            Optional. The maximum number of results to
            return from this request. Non-positive values
            are ignored. The presence of nextPageToken in
            the response indicates that more results might
            be available.
        page_token (str):
            Optional. If present, retrieve the next batch
            of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter that chooses which
            catalogs to return.
        order_by (str):
            Optional. How the results should be sorted.
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


class ListCatalogsResponse(proto.Message):
    r"""Results returned from catalogs.list.

    Attributes:
        catalogs (MutableSequence[google.cloud.designcenter_v1.types.Catalog]):
            A list of catalogs
        next_page_token (str):
            If there might be more results than those
            appearing in this response, nextPageToken is
            included. To get the next set of results, call
            this method again using the value of
            nextPageToken as pageToken.
    """

    @property
    def raw_page(self):
        return self

    catalogs: MutableSequence[catalog_management.Catalog] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=catalog_management.Catalog,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateCatalogRequest(proto.Message):
    r"""Message for creating a catalog.

    Attributes:
        parent (str):
            Required. The parent space in which a catalog is created in
            the following format:
            ``projects/$project/locations/$location/spaces/$space``
        catalog_id (str):
            Required. The ID of the catalog to create.
        catalog (google.cloud.designcenter_v1.types.Catalog):
            Required. The catalog to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    catalog_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    catalog: catalog_management.Catalog = proto.Field(
        proto.MESSAGE,
        number=3,
        message=catalog_management.Catalog,
    )


class UpdateCatalogRequest(proto.Message):
    r"""Message for updating a catalog.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The fields to overwrite in the
            catalog update. If you don't provide a mask, all
            fields are overwritten.
        catalog (google.cloud.designcenter_v1.types.Catalog):
            Required. The catalog to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    catalog: catalog_management.Catalog = proto.Field(
        proto.MESSAGE,
        number=2,
        message=catalog_management.Catalog,
    )


class DeleteCatalogRequest(proto.Message):
    r"""Message for deleting a catalog.

    Attributes:
        name (str):
            Required. The catalog name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog``
        force (bool):
            Optional. If set to true, the catalog's
            children are also deleted. If false, the catalog
            is only deleted if it has no children.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateCatalogTemplateRequest(proto.Message):
    r"""Message for creating a catalog template.

    Attributes:
        parent (str):
            Required. The parent resource in which the
            catalog template is created.
        catalog_template_id (str):
            Required. The ID of the catalog template to
            create. The ID is appended to the catalog
            template's name.
        catalog_template (google.cloud.designcenter_v1.types.CatalogTemplate):
            Required. The catalog template to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    catalog_template_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    catalog_template: catalog_management.CatalogTemplate = proto.Field(
        proto.MESSAGE,
        number=3,
        message=catalog_management.CatalogTemplate,
    )


class GetCatalogTemplateRequest(proto.Message):
    r"""Message for getting a catalog template resource.

    Attributes:
        name (str):
            Required. The catalog template name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCatalogTemplatesRequest(proto.Message):
    r"""Message for requesting a list of catalog templates.

    Attributes:
        parent (str):
            Required. The parent from which the catalog templates are
            listed in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog``
        page_size (int):
            Optional. The maximum number of results to
            return from this request. Non-positive
             values are ignored. The presence of
            nextPageToken in the response  indicates that
            more results might be available.
        page_token (str):
            Optional. If present, then retrieve the next
            batch of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter that chooses the catalog
            templates to return.
        order_by (str):
            Optional. How the results should be sorted.
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


class ListCatalogTemplatesResponse(proto.Message):
    r"""Message for response to listing catalog templates.

    Attributes:
        catalog_templates (MutableSequence[google.cloud.designcenter_v1.types.CatalogTemplate]):
            The list of catalog templates.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
    """

    @property
    def raw_page(self):
        return self

    catalog_templates: MutableSequence[catalog_management.CatalogTemplate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=catalog_management.CatalogTemplate,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateCatalogTemplateRequest(proto.Message):
    r"""Message for updating a catalog template.

    Attributes:
        catalog_template (google.cloud.designcenter_v1.types.CatalogTemplate):
            Required. The catalog template to update. Format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The fields to overwrite in the catalog template
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If you don't provide a
            mask, all fields are overwritten.
    """

    catalog_template: catalog_management.CatalogTemplate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=catalog_management.CatalogTemplate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCatalogTemplateRequest(proto.Message):
    r"""Message for deleting a catalog template.

    Attributes:
        name (str):
            Required. The catalog template name. Format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``
        force (bool):
            Optional. If set to true, the catalog
            template's children are also deleted. If false,
            the catalog template is only deleted if it has
            no children.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateCatalogTemplateRevisionRequest(proto.Message):
    r"""Message for creating a template revisions request.

    Attributes:
        parent (str):
            Required. The parent in which the catalog template revisions
            request is created in following format:
            ``projects/$project/locations/$location/spaces/$space/templates/$template``
        catalog_template_revision_id (str):
            Required. The ID of the template revision to
            create.
        catalog_template_revision (google.cloud.designcenter_v1.types.CatalogTemplateRevision):
            Required. The template revision to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    catalog_template_revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    catalog_template_revision: catalog_management.CatalogTemplateRevision = proto.Field(
        proto.MESSAGE,
        number=3,
        message=catalog_management.CatalogTemplateRevision,
    )


class GetCatalogTemplateRevisionRequest(proto.Message):
    r"""Message for GetTemplateRevision Request

    Attributes:
        name (str):
            Required. The catalog template revisions
            name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCatalogTemplateRevisionsRequest(proto.Message):
    r"""Message for requesting list of template revisions.

    Attributes:
        parent (str):
            Required. The parent resource from which a
            list of catalog template revisions is requested.
        page_size (int):
            Optional. The maximum number of results to
            return from this request. Non-positive
             values are ignored. The presence of
            nextPageToken in the response  indicates that
            more results might be available.
        page_token (str):
            Optional. If present, then retrieve the next
            batch of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter that chooses which catalog
            template revisions to return.
        order_by (str):
            Optional. How the results should be sorted.
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


class ListCatalogTemplateRevisionsResponse(proto.Message):
    r"""Message for response to listing template revisions.

    Attributes:
        catalog_template_revisions (MutableSequence[google.cloud.designcenter_v1.types.CatalogTemplateRevision]):
            The list of template revisions.
        next_page_token (str):
            If there might be more results than those
            appearing in this response, then nextPageToken
            is included. To get the next set of results,
            call this method again using the value of
            nextPageToken as pageToken.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    catalog_template_revisions: MutableSequence[
        catalog_management.CatalogTemplateRevision
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=catalog_management.CatalogTemplateRevision,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteCatalogTemplateRevisionRequest(proto.Message):
    r"""Message for deleting a template revision.

    Attributes:
        name (str):
            Required. The template revision name.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchCatalogTemplateRevisionTFSourceRequest(proto.Message):
    r"""Request message for fetching the Terraform source of a
    catalog template revision.

    Attributes:
        name (str):
            Required. Name of the resource Eg:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template/revisions/$revision``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchCatalogTemplateRevisionTFSourceResponse(proto.Message):
    r"""Response message for getting the Terraform source of a
    catalog template revision.

    Attributes:
        root_module (google.cloud.designcenter_v1.types.TerraformModule):
            The root Terraform module of the catalog
            template revision.
        modules (MutableSequence[google.cloud.designcenter_v1.types.TerraformModule]):
            The dependent Terraform modules used by the
            root module.
    """

    root_module: iac.TerraformModule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=iac.TerraformModule,
    )
    modules: MutableSequence[iac.TerraformModule] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=iac.TerraformModule,
    )


class FetchCatalogTemplateRevisionAssessmentReportRequest(proto.Message):
    r"""Request message for
    FetchCatalogTemplateRevisionAssessmentReport.

    Attributes:
        name (str):
            Required. The catalog template revision name in the
            following format:
            ``projects/{project}/locations/{location}/spaces/{space}/catalogs/{catalog}/templates/{template}/revisions/{revision}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchCatalogTemplateRevisionAssessmentReportResponse(proto.Message):
    r"""Response message for
    FetchCatalogTemplateRevisionAssessmentReport.

    Attributes:
        assessment_report (google.cloud.designcenter_v1.types.AssessmentReport):
            Assessment report for the catalog template
            revision.
    """

    assessment_report: best_practices.AssessmentReport = proto.Field(
        proto.MESSAGE,
        number=1,
        message=best_practices.AssessmentReport,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
