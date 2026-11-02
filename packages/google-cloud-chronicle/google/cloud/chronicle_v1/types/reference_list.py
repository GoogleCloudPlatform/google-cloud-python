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
    package="google.cloud.chronicle.v1",
    manifest={
        "ReferenceListSyntaxType",
        "ReferenceListView",
        "ScopeInfo",
        "ReferenceListScope",
        "GetReferenceListRequest",
        "ListReferenceListsRequest",
        "ListReferenceListsResponse",
        "CreateReferenceListRequest",
        "UpdateReferenceListRequest",
        "VerifyReferenceListRequest",
        "VerifyReferenceListResponse",
        "ReferenceList",
        "ReferenceListEntry",
        "ReferenceListError",
    },
)


class ReferenceListSyntaxType(proto.Enum):
    r"""The syntax type indicating how list entries should be
    validated.

    Values:
        REFERENCE_LIST_SYNTAX_TYPE_UNSPECIFIED (0):
            Defaults to REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING.
        REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING (1):
            List contains plain text patterns.
        REFERENCE_LIST_SYNTAX_TYPE_REGEX (2):
            List contains only Regular Expression
            patterns.
        REFERENCE_LIST_SYNTAX_TYPE_CIDR (3):
            List contains only CIDR patterns.
    """

    REFERENCE_LIST_SYNTAX_TYPE_UNSPECIFIED = 0
    REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING = 1
    REFERENCE_LIST_SYNTAX_TYPE_REGEX = 2
    REFERENCE_LIST_SYNTAX_TYPE_CIDR = 3


class ReferenceListView(proto.Enum):
    r"""ReferenceListView is a mechanism for viewing partial
    responses of the ReferenceList resource.

    Values:
        REFERENCE_LIST_VIEW_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the BASIC view for
            ListReferenceLists. The API will default to the
            FULL view for methods that return a single
            ReferenceList resource.
        REFERENCE_LIST_VIEW_BASIC (1):
            Include metadata about the ReferenceList.
            This is the default view for ListReferenceLists.
        REFERENCE_LIST_VIEW_FULL (2):
            Include all details about the ReferenceList:
            metadata, content lines, associated rule counts.
            This is the default view for GetReferenceList.
    """

    REFERENCE_LIST_VIEW_UNSPECIFIED = 0
    REFERENCE_LIST_VIEW_BASIC = 1
    REFERENCE_LIST_VIEW_FULL = 2


class ScopeInfo(proto.Message):
    r"""ScopeInfo specifies the scope info of the reference list.

    Attributes:
        reference_list_scope (google.cloud.chronicle_v1.types.ReferenceListScope):
            Required. The list of scope names of the
            reference list, if the list is empty the
            reference list is treated as unscoped.
    """

    reference_list_scope: "ReferenceListScope" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReferenceListScope",
    )


class ReferenceListScope(proto.Message):
    r"""ReferenceListScope specifies the list of scope names of the
    reference list.

    Attributes:
        scope_names (MutableSequence[str]):
            Optional. The list of scope names of the reference list. The
            scope names should be full resource names and should be of
            the format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{scope_name}``.
    """

    scope_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class GetReferenceListRequest(proto.Message):
    r"""A request to get details about a reference list.

    Attributes:
        name (str):
            Required. The resource name of the reference list to
            retrieve. Format:
            ``projects/{project}/locations/{locations}/instances/{instance}/referenceLists/{reference_list}``
        view (google.cloud.chronicle_v1.types.ReferenceListView):
            How much of the ReferenceList to view. Defaults to
            REFERENCE_LIST_VIEW_FULL.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ReferenceListView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ReferenceListView",
    )


class ListReferenceListsRequest(proto.Message):
    r"""A request for a list of reference lists.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            reference lists. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        page_size (int):
            The maximum number of reference lists to
            return. The service may return fewer than this
            value. If unspecified, at most 100 reference
            lists will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListReferenceLists`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListReferenceLists`` must match the call that
            provided the page token.
        view (google.cloud.chronicle_v1.types.ReferenceListView):
            How much of each ReferenceList to view. Defaults to
            REFERENCE_LIST_VIEW_BASIC.
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
    view: "ReferenceListView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ReferenceListView",
    )


class ListReferenceListsResponse(proto.Message):
    r"""A response to a request for a list of reference lists.

    Attributes:
        reference_lists (MutableSequence[google.cloud.chronicle_v1.types.ReferenceList]):
            The reference lists.
            Ordered in ascending alphabetical order by name.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    reference_lists: MutableSequence["ReferenceList"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReferenceList",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateReferenceListRequest(proto.Message):
    r"""A request to create a reference list.

    Attributes:
        parent (str):
            Required. The parent resource where this reference list will
            be created. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        reference_list (google.cloud.chronicle_v1.types.ReferenceList):
            Required. The reference list to create.
        reference_list_id (str):
            Required. The ID to use for the reference
            list. This is also the display name for the
            reference list. It must satisfy the following
            requirements:

            - Starts with letter.
            - Contains only letters, numbers and underscore.
            - Has length less than 256.
            - Must be unique.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reference_list: "ReferenceList" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReferenceList",
    )
    reference_list_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateReferenceListRequest(proto.Message):
    r"""A request to update a reference list.

    Attributes:
        reference_list (google.cloud.chronicle_v1.types.ReferenceList):
            Required. The reference list to update.

            The reference list's ``name`` field is used to identify the
            reference list to update. Format:
            ``projects/{project}/locations/{locations}/instances/{instance}/referenceLists/{reference_list}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. When no field mask is
            supplied, all non-empty fields will be updated. A field mask
            of "\*" will update all fields, whether empty or not.
    """

    reference_list: "ReferenceList" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ReferenceList",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class VerifyReferenceListRequest(proto.Message):
    r"""VerifyReferenceList request message.

    Attributes:
        instance (str):
            Required. The name of the parent resource, which is the
            SecOps instance associated with the request. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        syntax_type (google.cloud.chronicle_v1.types.ReferenceListSyntaxType):
            Required. Type (format) of list lines.
        entries (MutableSequence[google.cloud.chronicle_v1.types.ReferenceListEntry]):
            Required. The entries of the reference list.
            Each line may be either an item in the list or a
            comment.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    syntax_type: "ReferenceListSyntaxType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ReferenceListSyntaxType",
    )
    entries: MutableSequence["ReferenceListEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ReferenceListEntry",
    )


class VerifyReferenceListResponse(proto.Message):
    r"""VerifyListResponse response message.

    Attributes:
        success (bool):
            Validity of list - true if no errors found.
        errors (MutableSequence[google.cloud.chronicle_v1.types.ReferenceListError]):
            Line-level errors causing the list to be
            invalid.
    """

    success: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    errors: MutableSequence["ReferenceListError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ReferenceListError",
    )


class ReferenceList(proto.Message):
    r"""A reference list.
    Reference lists are user-defined lists of values which users can
    use in multiple Rules.

    Attributes:
        name (str):
            Identifier. The resource name of the reference list. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/referenceLists/{reference_list}``
        display_name (str):
            Output only. The unique display name of the
            reference list.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the reference
            list was last updated.
        description (str):
            Required. A user-provided description of the
            reference list.
        entries (MutableSequence[google.cloud.chronicle_v1.types.ReferenceListEntry]):
            Required. The entries of the reference list. When listed,
            they are returned in the order that was specified at
            creation or update. The combined size of the values of the
            reference list may not exceed 6MB. This is returned only
            when the view is REFERENCE_LIST_VIEW_FULL.
        rules (MutableSequence[str]):
            Output only. The resource names for the associated
            self-authored Rules that use this reference list. This is
            returned only when the view is REFERENCE_LIST_VIEW_FULL.
        syntax_type (google.cloud.chronicle_v1.types.ReferenceListSyntaxType):
            Required. The syntax type indicating how list
            entries should be validated.
        rule_associations_count (int):
            Output only. The count of self-authored rules
            using the reference list.
        scope_info (google.cloud.chronicle_v1.types.ScopeInfo):
            The scope info of the reference list. During reference list
            creation, if this field is not set, the reference list
            without scopes (an unscoped list) will be created for an
            unscoped user. For a scoped user, this field must be set.
            During reference list update, if scope_info is requested to
            be updated, this field must be set.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    entries: MutableSequence["ReferenceListEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ReferenceListEntry",
    )
    rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    syntax_type: "ReferenceListSyntaxType" = proto.Field(
        proto.ENUM,
        number=8,
        enum="ReferenceListSyntaxType",
    )
    rule_associations_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    scope_info: "ScopeInfo" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ScopeInfo",
    )


class ReferenceListEntry(proto.Message):
    r"""An entry in a reference list.

    Attributes:
        value (str):
            Required. The value of the entry. Maximum
            length is 512 characters.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReferenceListError(proto.Message):
    r"""The error generated when verifying the reference list.

    Attributes:
        line_number (int):
            1-indexed line number where the error occurs.
            General list errors are indexed at -1.
        error_message (str):
            Message explaining why the line is invalid.
    """

    line_number: int = proto.Field(
        proto.INT32,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
