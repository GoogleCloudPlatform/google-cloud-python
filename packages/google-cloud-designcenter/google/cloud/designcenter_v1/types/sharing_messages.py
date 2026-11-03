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

import proto  # type: ignore

from google.cloud.designcenter_v1.types import best_practices, iac, sharing

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "CreateShareRequest",
        "ListSharesRequest",
        "ListSharesResponse",
        "GetShareRequest",
        "DeleteShareRequest",
        "SyncShareRequest",
        "GetSharedTemplateRequest",
        "ListSharedTemplatesRequest",
        "ListSharedTemplatesResponse",
        "GetSharedTemplateRevisionRequest",
        "ListSharedTemplateRevisionsRequest",
        "ListSharedTemplateRevisionsResponse",
        "FetchSharedTemplateRevisionTFSourceRequest",
        "FetchSharedTemplateRevisionTFSourceResponse",
        "FetchSharedTemplateRevisionAssessmentReportRequest",
        "FetchSharedTemplateRevisionAssessmentReportResponse",
    },
)


class CreateShareRequest(proto.Message):
    r"""Message for creating a share of a catalog.

    Attributes:
        parent (str):
            Required. The parent resource in which shares
            are created.
        share_id (str):
            Required. The ID of the share to create.
        share (google.cloud.designcenter_v1.types.Share):
            Required. The share to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    share_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    share: sharing.Share = proto.Field(
        proto.MESSAGE,
        number=3,
        message=sharing.Share,
    )


class ListSharesRequest(proto.Message):
    r"""Message for listing shares of a catalog.

    Attributes:
        parent (str):
            Required. The parent resource from which a
            list of shares is requested.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListSharesResponse(proto.Message):
    r"""Message for response to listing shares of a catalog.

    Attributes:
        shares (MutableSequence[google.cloud.designcenter_v1.types.Share]):
            The list of shares.
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

    shares: MutableSequence[sharing.Share] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=sharing.Share,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetShareRequest(proto.Message):
    r"""Message for getting a share of a catalog.

    Attributes:
        name (str):
            Required. The share name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteShareRequest(proto.Message):
    r"""Message for deleting a share of a catalog.

    Attributes:
        name (str):
            Required. The share name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SyncShareRequest(proto.Message):
    r"""Message for syncing a share of a catalog.

    Attributes:
        name (str):
            Required. The share name in the following format:
            ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSharedTemplateRequest(proto.Message):
    r"""Message for getting a shared template.

    Attributes:
        name (str):
            Required. The shared template name. Format:
            ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSharedTemplatesRequest(proto.Message):
    r"""Message for requesting list of shared templates.

    Attributes:
        parent (str):
            Required. The parent space for which shared templates are
            listed in the following format:
            ``projects/$project/locations/$location/spaces/$space``
        page_size (int):
            Optional. The maximum number of results to
            return from this request. Non-positive values
            are ignored. The presence of nextPageToken in
            the response indicates that more results might
            be available.
        page_token (str):
            Optional. If present, then retrieve the next
            batch of results from the preceding call to this
            method. pageToken must be the value of
            nextPageToken from the previous response. The
            values of other method parameters should be
            identical to those in the previous call.
        filter (str):
            Optional. A filter that chooses which shared
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


class ListSharedTemplatesResponse(proto.Message):
    r"""Message for response to listing shared templates.

    Attributes:
        shared_templates (MutableSequence[google.cloud.designcenter_v1.types.SharedTemplate]):
            The list of shared templates.
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

    shared_templates: MutableSequence[sharing.SharedTemplate] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=sharing.SharedTemplate,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSharedTemplateRevisionRequest(proto.Message):
    r"""Message for getting a shared template revisions.

    Attributes:
        name (str):
            Required. The shared template revision name, in the
            following format:
            ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate/revisions/$revision``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSharedTemplateRevisionsRequest(proto.Message):
    r"""Message for requesting a list of shared template revisions.

    Attributes:
        parent (str):
            Required. The parent resource from which to list shared
            template revisions, in the following format:
            ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate``
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
            Optional. A filter that chooses which shared
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


class ListSharedTemplateRevisionsResponse(proto.Message):
    r"""Message for response to listing shared templates.

    Attributes:
        shared_template_revisions (MutableSequence[google.cloud.designcenter_v1.types.SharedTemplateRevision]):
            The list of shared templates.
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

    shared_template_revisions: MutableSequence[sharing.SharedTemplateRevision] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=sharing.SharedTemplateRevision,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchSharedTemplateRevisionTFSourceRequest(proto.Message):
    r"""Request message for fetching the Terraform source of a shared
    template revision.

    Attributes:
        name (str):
            Required. Name of the resource Eg:
            ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$template/revisions/$revision``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchSharedTemplateRevisionTFSourceResponse(proto.Message):
    r"""Response message for getting the Terraform source of a shared
    template revision.

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


class FetchSharedTemplateRevisionAssessmentReportRequest(proto.Message):
    r"""Request message for
    FetchSharedTemplateRevisionAssessmentReport.

    Attributes:
        name (str):
            Required. The shared template revision name in the following
            format:
            ``projects/{project}/locations/{location}/spaces/{space}/sharedTemplates/{shared_template}/revisions/{revision}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchSharedTemplateRevisionAssessmentReportResponse(proto.Message):
    r"""Response message for
    FetchSharedTemplateRevisionAssessmentReport.

    Attributes:
        assessment_report (google.cloud.designcenter_v1.types.AssessmentReport):
            Assessment report for the shared template
            revision.
    """

    assessment_report: best_practices.AssessmentReport = proto.Field(
        proto.MESSAGE,
        number=1,
        message=best_practices.AssessmentReport,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
