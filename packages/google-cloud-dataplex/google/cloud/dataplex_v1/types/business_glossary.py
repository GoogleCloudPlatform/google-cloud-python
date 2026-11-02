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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "Glossary",
        "GlossaryCategory",
        "GlossaryTerm",
        "CreateGlossaryRequest",
        "UpdateGlossaryRequest",
        "DeleteGlossaryRequest",
        "GetGlossaryRequest",
        "ListGlossariesRequest",
        "ListGlossariesResponse",
        "CreateGlossaryCategoryRequest",
        "UpdateGlossaryCategoryRequest",
        "DeleteGlossaryCategoryRequest",
        "GetGlossaryCategoryRequest",
        "ListGlossaryCategoriesRequest",
        "ListGlossaryCategoriesResponse",
        "CreateGlossaryTermRequest",
        "UpdateGlossaryTermRequest",
        "DeleteGlossaryTermRequest",
        "GetGlossaryTermRequest",
        "ListGlossaryTermsRequest",
        "ListGlossaryTermsResponse",
    },
)


class Glossary(proto.Message):
    r"""A Glossary represents a collection of GlossaryCategories and
    GlossaryTerms defined by the user. Glossary is a top level
    resource and is the Google Cloud parent resource of all the
    GlossaryCategories and GlossaryTerms within it.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the Glossary.
            Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
        uid (str):
            Output only. System generated unique id for
            the Glossary. This ID will be different if the
            Glossary is deleted and re-created with the same
            name.
        display_name (str):
            Optional. User friendly display name of the
            Glossary. This is user-mutable. This will be
            same as the GlossaryId, if not specified.
        description (str):
            Optional. The user-mutable description of the
            Glossary.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the Glossary
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the Glossary
            was last updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            Glossary.
        term_count (int):
            Output only. The number of GlossaryTerms in
            the Glossary.
        category_count (int):
            Output only. The number of GlossaryCategories
            in the Glossary.
        etag (str):
            Optional. Needed for resource freshness
            validation. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    term_count: int = proto.Field(
        proto.INT32,
        number=8,
    )
    category_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )


class GlossaryCategory(proto.Message):
    r"""A GlossaryCategory represents a collection of
    GlossaryCategories and GlossaryTerms within a Glossary that are
    related to each other.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the
            GlossaryCategory. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}
        uid (str):
            Output only. System generated unique id for
            the GlossaryCategory. This ID will be different
            if the GlossaryCategory is deleted and
            re-created with the same name.
        display_name (str):
            Optional. User friendly display name of the
            GlossaryCategory. This is user-mutable. This
            will be same as the GlossaryCategoryId, if not
            specified.
        description (str):
            Optional. The user-mutable description of the
            GlossaryCategory.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            GlossaryCategory was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            GlossaryCategory was last updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            GlossaryCategory.
        parent (str):
            Required. The immediate parent of the GlossaryCategory in
            the resource-hierarchy. It can either be a Glossary or a
            GlossaryCategory. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
            OR
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GlossaryTerm(proto.Message):
    r"""GlossaryTerms are the core of Glossary.
    A GlossaryTerm holds a rich text description that can be
    attached to Entries or specific columns to enrich them.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the
            GlossaryTerm. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}
        uid (str):
            Output only. System generated unique id for
            the GlossaryTerm. This ID will be different if
            the GlossaryTerm is deleted and re-created with
            the same name.
        display_name (str):
            Optional. User friendly display name of the
            GlossaryTerm. This is user-mutable. This will be
            same as the GlossaryTermId, if not specified.
        description (str):
            Optional. The user-mutable description of the
            GlossaryTerm.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            GlossaryTerm was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            GlossaryTerm was last updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            GlossaryTerm.
        parent (str):
            Required. The immediate parent of the GlossaryTerm in the
            resource-hierarchy. It can either be a Glossary or a
            GlossaryCategory. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
            OR
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=8,
    )


class CreateGlossaryRequest(proto.Message):
    r"""Create Glossary Request

    Attributes:
        parent (str):
            Required. The parent resource where this Glossary will be
            created. Format:
            projects/{project_id_or_number}/locations/{location_id}
            where ``location_id`` refers to a Google Cloud region.
        glossary_id (str):
            Required. Glossary ID: Glossary identifier.
        glossary (google.cloud.dataplex_v1.types.Glossary):
            Required. The Glossary to create.
        validate_only (bool):
            Optional. Validates the request without
            actually creating the Glossary. Default: false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    glossary_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    glossary: "Glossary" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Glossary",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateGlossaryRequest(proto.Message):
    r"""Update Glossary Request

    Attributes:
        glossary (google.cloud.dataplex_v1.types.Glossary):
            Required. The Glossary to update. The Glossary's ``name``
            field is used to identify the Glossary to update. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
        validate_only (bool):
            Optional. Validates the request without
            actually updating the Glossary. Default: false.
    """

    glossary: "Glossary" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Glossary",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteGlossaryRequest(proto.Message):
    r"""Delete Glossary Request

    Attributes:
        name (str):
            Required. The name of the Glossary to delete. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
        etag (str):
            Optional. The etag of the Glossary.
            If this is provided, it must match the server's
            etag. If the etag is provided and does not match
            the server-computed etag, the request must fail
            with a ABORTED error code.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetGlossaryRequest(proto.Message):
    r"""Get Glossary Request

    Attributes:
        name (str):
            Required. The name of the Glossary to retrieve. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGlossariesRequest(proto.Message):
    r"""List Glossaries Request

    Attributes:
        parent (str):
            Required. The parent, which has this collection of
            Glossaries. Format:
            projects/{project_id_or_number}/locations/{location_id}
            where ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. The maximum number of Glossaries to
            return. The service may return fewer than this
            value. If unspecified, at most 50 Glossaries
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListGlossaries`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListGlossaries`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter expression that filters Glossaries listed
            in the response. Filters on proto fields of Glossary are
            supported. Examples of using a filter are:

            - ``display_name="my-glossary"``
            - ``categoryCount=1``
            - ``termCount=0``
        order_by (str):
            Optional. Order by expression that orders Glossaries listed
            in the response. Order by fields are: ``name`` or
            ``create_time`` for the result. If not specified, the
            ordering is undefined.
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


class ListGlossariesResponse(proto.Message):
    r"""List Glossaries Response

    Attributes:
        glossaries (MutableSequence[google.cloud.dataplex_v1.types.Glossary]):
            Lists the Glossaries in the specified parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable_locations (MutableSequence[str]):
            Locations that the service couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    glossaries: MutableSequence["Glossary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Glossary",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateGlossaryCategoryRequest(proto.Message):
    r"""Creates a new GlossaryCategory under the specified Glossary.

    Attributes:
        parent (str):
            Required. The parent resource where this GlossaryCategory
            will be created. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
            where ``locationId`` refers to a Google Cloud region.
        category_id (str):
            Required. GlossaryCategory identifier.
        category (google.cloud.dataplex_v1.types.GlossaryCategory):
            Required. The GlossaryCategory to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    category_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    category: "GlossaryCategory" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GlossaryCategory",
    )


class UpdateGlossaryCategoryRequest(proto.Message):
    r"""Update GlossaryCategory Request

    Attributes:
        category (google.cloud.dataplex_v1.types.GlossaryCategory):
            Required. The GlossaryCategory to update. The
            GlossaryCategory's ``name`` field is used to identify the
            GlossaryCategory to update. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    category: "GlossaryCategory" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GlossaryCategory",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteGlossaryCategoryRequest(proto.Message):
    r"""Delete GlossaryCategory Request

    Attributes:
        name (str):
            Required. The name of the GlossaryCategory to delete.
            Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetGlossaryCategoryRequest(proto.Message):
    r"""Get GlossaryCategory Request

    Attributes:
        name (str):
            Required. The name of the GlossaryCategory to retrieve.
            Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGlossaryCategoriesRequest(proto.Message):
    r"""List GlossaryCategories Request

    Attributes:
        parent (str):
            Required. The parent, which has this collection of
            GlossaryCategories. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
            Location is the Google Cloud region.
        page_size (int):
            Optional. The maximum number of
            GlossaryCategories to return. The service may
            return fewer than this value. If unspecified, at
            most 50 GlossaryCategories will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListGlossaryCategories`` call. Provide this to retrieve
            the subsequent page. When paginating, all other parameters
            provided to ``ListGlossaryCategories`` must match the call
            that provided the page token.
        filter (str):
            Optional. Filter expression that filters GlossaryCategories
            listed in the response. Filters are supported on the
            following fields:

            - immediate_parent

            Examples of using a filter are:
            -------------------------------

            ``immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}"``
            -------------------------------------------------------------------------------------------------------

            ``immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}"``

            This will only return the GlossaryCategories that are
            directly nested under the specified parent.
        order_by (str):
            Optional. Order by expression that orders GlossaryCategories
            listed in the response. Order by fields are: ``name`` or
            ``create_time`` for the result. If not specified, the
            ordering is undefined.
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


class ListGlossaryCategoriesResponse(proto.Message):
    r"""List GlossaryCategories Response

    Attributes:
        categories (MutableSequence[google.cloud.dataplex_v1.types.GlossaryCategory]):
            Lists the GlossaryCategories in the specified
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable_locations (MutableSequence[str]):
            Locations that the service couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    categories: MutableSequence["GlossaryCategory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GlossaryCategory",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateGlossaryTermRequest(proto.Message):
    r"""Creates a new GlossaryTerm under the specified Glossary.

    Attributes:
        parent (str):
            Required. The parent resource where the GlossaryTerm will be
            created. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
            where ``location_id`` refers to a Google Cloud region.
        term_id (str):
            Required. GlossaryTerm identifier.
        term (google.cloud.dataplex_v1.types.GlossaryTerm):
            Required. The GlossaryTerm to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    term_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    term: "GlossaryTerm" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GlossaryTerm",
    )


class UpdateGlossaryTermRequest(proto.Message):
    r"""Update GlossaryTerm Request

    Attributes:
        term (google.cloud.dataplex_v1.types.GlossaryTerm):
            Required. The GlossaryTerm to update. The GlossaryTerm's
            ``name`` field is used to identify the GlossaryTerm to
            update. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    term: "GlossaryTerm" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GlossaryTerm",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteGlossaryTermRequest(proto.Message):
    r"""Delete GlossaryTerm Request

    Attributes:
        name (str):
            Required. The name of the GlossaryTerm to delete. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetGlossaryTermRequest(proto.Message):
    r"""Get GlossaryTerm Request

    Attributes:
        name (str):
            Required. The name of the GlossaryTerm to retrieve. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGlossaryTermsRequest(proto.Message):
    r"""List GlossaryTerms Request

    Attributes:
        parent (str):
            Required. The parent, which has this collection of
            GlossaryTerms. Format:
            projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}
            where ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. The maximum number of GlossaryTerms
            to return. The service may return fewer than
            this value. If unspecified, at most 50
            GlossaryTerms will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListGlossaryTerms`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListGlossaryTerms`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter expression that filters GlossaryTerms
            listed in the response. Filters are supported on the
            following fields:

            - immediate_parent

            Examples of using a filter are:
            -------------------------------

            ``immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}"``
            -------------------------------------------------------------------------------------------------------

            ``immediate_parent="projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}"``

            This will only return the GlossaryTerms that are directly
            nested under the specified parent.
        order_by (str):
            Optional. Order by expression that orders GlossaryTerms
            listed in the response. Order by fields are: ``name`` or
            ``create_time`` for the result. If not specified, the
            ordering is undefined.
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


class ListGlossaryTermsResponse(proto.Message):
    r"""List GlossaryTerms Response

    Attributes:
        terms (MutableSequence[google.cloud.dataplex_v1.types.GlossaryTerm]):
            Lists the GlossaryTerms in the specified
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable_locations (MutableSequence[str]):
            Locations that the service couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    terms: MutableSequence["GlossaryTerm"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GlossaryTerm",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
