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

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "UpdateType",
        "DatabaseType",
        "AccessControlMode",
        "DocumentCreatorDefaultRole",
        "RequestMetadata",
        "ResponseMetadata",
        "UserInfo",
        "UpdateOptions",
        "MergeFieldsOptions",
    },
)


class UpdateType(proto.Enum):
    r"""Update type of the requests.

    Values:
        UPDATE_TYPE_UNSPECIFIED (0):
            Defaults to full replace behavior, ie. FULL_REPLACE.
        UPDATE_TYPE_REPLACE (1):
            Fully replace all the fields (including
            previously linked raw document). Any field masks
            will be ignored.
        UPDATE_TYPE_MERGE (2):
            Merge the fields into the existing entities.
        UPDATE_TYPE_INSERT_PROPERTIES_BY_NAMES (3):
            Inserts the properties by names.
        UPDATE_TYPE_REPLACE_PROPERTIES_BY_NAMES (4):
            Replace the properties by names.
        UPDATE_TYPE_DELETE_PROPERTIES_BY_NAMES (5):
            Delete the properties by names.
        UPDATE_TYPE_MERGE_AND_REPLACE_OR_INSERT_PROPERTIES_BY_NAMES (6):
            For each of the property, replaces the
            property if the it exists, otherwise inserts a
            new property. And for the rest of the fields,
            merge them based on update mask and merge fields
            options.
    """

    UPDATE_TYPE_UNSPECIFIED = 0
    UPDATE_TYPE_REPLACE = 1
    UPDATE_TYPE_MERGE = 2
    UPDATE_TYPE_INSERT_PROPERTIES_BY_NAMES = 3
    UPDATE_TYPE_REPLACE_PROPERTIES_BY_NAMES = 4
    UPDATE_TYPE_DELETE_PROPERTIES_BY_NAMES = 5
    UPDATE_TYPE_MERGE_AND_REPLACE_OR_INSERT_PROPERTIES_BY_NAMES = 6


class DatabaseType(proto.Enum):
    r"""Type of database used by the customer

    Values:
        DB_UNKNOWN (0):
            This value is required by protobuf best
            practices
        DB_INFRA_SPANNER (1):
            Internal Spanner
        DB_CLOUD_SQL_POSTGRES (2):
            Cloud Sql with a Postgres Sql instance
    """

    DB_UNKNOWN = 0
    DB_INFRA_SPANNER = 1
    DB_CLOUD_SQL_POSTGRES = 2


class AccessControlMode(proto.Enum):
    r"""Access Control Mode.

    Values:
        ACL_MODE_UNKNOWN (0):
            This value is required by protobuf best
            practices
        ACL_MODE_UNIVERSAL_ACCESS (1):
            Universal Access: No document level access
            control.
        ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_BYOID (2):
            Document level access control with customer
            own Identity Service.
        ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_GCI (3):
            Document level access control using Google
            Cloud Identity.
    """

    ACL_MODE_UNKNOWN = 0
    ACL_MODE_UNIVERSAL_ACCESS = 1
    ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_BYOID = 2
    ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_GCI = 3


class DocumentCreatorDefaultRole(proto.Enum):
    r"""The default role of the document creator.

    Values:
        DOCUMENT_CREATOR_DEFAULT_ROLE_UNSPECIFIED (0):
            Unspecified, will be default to document
            admin role.
        DOCUMENT_ADMIN (1):
            Document Admin, same as
            contentwarehouse.googleapis.com/documentAdmin.
        DOCUMENT_EDITOR (2):
            Document Editor, same as
            contentwarehouse.googleapis.com/documentEditor.
        DOCUMENT_VIEWER (3):
            Document Viewer, same as
            contentwarehouse.googleapis.com/documentViewer.
    """

    DOCUMENT_CREATOR_DEFAULT_ROLE_UNSPECIFIED = 0
    DOCUMENT_ADMIN = 1
    DOCUMENT_EDITOR = 2
    DOCUMENT_VIEWER = 3


class RequestMetadata(proto.Message):
    r"""Meta information is used to improve the performance of the
    service.

    Attributes:
        user_info (google.cloud.contentwarehouse_v1.types.UserInfo):
            Provides user unique identification and
            groups information.
    """

    user_info: "UserInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UserInfo",
    )


class ResponseMetadata(proto.Message):
    r"""Additional information returned to client, such as debugging
    information.

    Attributes:
        request_id (str):
            A unique id associated with this call. This
            id is logged for tracking purpose.
    """

    request_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UserInfo(proto.Message):
    r"""The user information.

    Attributes:
        id (str):
            A unique user identification string, as determined by the
            client. The maximum number of allowed characters is 255.
            Allowed characters include numbers 0 to 9, uppercase and
            lowercase letters, and restricted special symbols (:, @, +,
            -, \_, ~) The format is "user:xxxx@example.com";
        group_ids (MutableSequence[str]):
            The unique group identifications which the
            user is belong to. The format is
            "group:yyyy@example.com";
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    group_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class UpdateOptions(proto.Message):
    r"""Options for Update operations.

    Attributes:
        update_type (google.cloud.contentwarehouse_v1.types.UpdateType):
            Type for update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask for merging Document fields. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
        merge_fields_options (google.cloud.contentwarehouse_v1.types.MergeFieldsOptions):
            Options for merging.
    """

    update_type: "UpdateType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="UpdateType",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    merge_fields_options: "MergeFieldsOptions" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MergeFieldsOptions",
    )


class MergeFieldsOptions(proto.Message):
    r"""Options for merging updated fields.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        replace_message_fields (bool):
            When merging message fields, the default
            behavior is to merge the content of two message
            fields together. If you instead want to use the
            field from the source message to replace the
            corresponding field in the destination message,
            set this flag to true. When this flag is set,
            specified submessage fields that are missing in
            source will be cleared in destination.

            This field is a member of `oneof`_ ``_replace_message_fields``.
        replace_repeated_fields (bool):
            When merging repeated fields, the default behavior is to
            append entries from the source repeated field to the
            destination repeated field. If you instead want to keep only
            the entries from the source repeated field, set this flag to
            true.

            If you want to replace a repeated field within a message
            field on the destination message, you must set both
            replace_repeated_fields and replace_message_fields to true,
            otherwise the repeated fields will be appended.

            This field is a member of `oneof`_ ``_replace_repeated_fields``.
    """

    replace_message_fields: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    replace_repeated_fields: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
