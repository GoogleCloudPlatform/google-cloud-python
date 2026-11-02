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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1beta1",
    manifest={
        "Tag",
        "TagField",
        "TagTemplate",
        "TagTemplateField",
        "FieldType",
    },
)


class Tag(proto.Message):
    r"""Tags are used to attach custom metadata to Data Catalog resources.
    Tags conform to the specifications within their tag template.

    See `Data Catalog
    IAM <https://cloud.google.com/data-catalog/docs/concepts/iam>`__ for
    information on the permissions needed to create or view tags.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the tag in URL format.
            Example:

            - projects/{project_id}/locations/{location}/entrygroups/{entry_group_id}/entries/{entry_id}/tags/{tag_id}

            where ``tag_id`` is a system-generated identifier. Note that
            this Tag may not actually be stored in the location in this
            name.
        template (str):
            Required. The resource name of the tag template that this
            tag uses. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

            This field cannot be modified after creation.
        template_display_name (str):
            Output only. The display name of the tag
            template.
        column (str):
            Resources like Entry can have schemas associated with them.
            This scope allows users to attach tags to an individual
            column based on that schema.

            For attaching a tag to a nested column, use ``.`` to
            separate the column names. Example:

            - ``outer_column.inner_column``

            This field is a member of `oneof`_ ``scope``.
        fields (MutableMapping[str, google.cloud.datacatalog_v1beta1.types.TagField]):
            Required. This maps the ID of a tag field to
            the value of and additional information about
            that field. Valid field IDs are defined by the
            tag's template. A tag must have at least 1 field
            and at most 500 fields.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    template: str = proto.Field(
        proto.STRING,
        number=2,
    )
    template_display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    column: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="scope",
    )
    fields: MutableMapping[str, "TagField"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message="TagField",
    )


class TagField(proto.Message):
    r"""Contains the value and supporting information for a field within a
    [Tag][google.cloud.datacatalog.v1beta1.Tag].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            Output only. The display name of this field.
        double_value (float):
            Holds the value for a tag field with double
            type.

            This field is a member of `oneof`_ ``kind``.
        string_value (str):
            Holds the value for a tag field with string
            type.

            This field is a member of `oneof`_ ``kind``.
        bool_value (bool):
            Holds the value for a tag field with boolean
            type.

            This field is a member of `oneof`_ ``kind``.
        timestamp_value (google.protobuf.timestamp_pb2.Timestamp):
            Holds the value for a tag field with
            timestamp type.

            This field is a member of `oneof`_ ``kind``.
        enum_value (google.cloud.datacatalog_v1beta1.types.TagField.EnumValue):
            Holds the value for a tag field with enum
            type. This value must be one of the allowed
            values in the definition of this enum.

            This field is a member of `oneof`_ ``kind``.
        order (int):
            Output only. The order of this field with respect to other
            fields in this tag. It can be set in
            [Tag][google.cloud.datacatalog.v1beta1.TagTemplateField.order].
            For example, a higher value can indicate a more important
            field. The value can be negative. Multiple fields can have
            the same order, and field orders within a tag do not have to
            be sequential.
    """

    class EnumValue(proto.Message):
        r"""Holds an enum value.

        Attributes:
            display_name (str):
                The display name of the enum value.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=2,
        oneof="kind",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="kind",
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="kind",
    )
    timestamp_value: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="kind",
        message=timestamp_pb2.Timestamp,
    )
    enum_value: EnumValue = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="kind",
        message=EnumValue,
    )
    order: int = proto.Field(
        proto.INT32,
        number=7,
    )


class TagTemplate(proto.Message):
    r"""A tag template defines a tag, which can have one or more typed
    fields. The template is used to create and attach the tag to Google
    Cloud resources. `Tag template
    roles <https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles>`__
    provide permissions to create, edit, and use the template. See, for
    example, the `TagTemplate
    User <https://cloud.google.com/data-catalog/docs/how-to/template-user>`__
    role, which includes permission to use the tag template to tag
    resources.

    Attributes:
        name (str):
            Identifier. The resource name of the tag template in URL
            format. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

            Note that this TagTemplate and its child resources may not
            actually be stored in the location in this name.
        display_name (str):
            The display name for this template. Defaults
            to an empty string.
        fields (MutableMapping[str, google.cloud.datacatalog_v1beta1.types.TagTemplateField]):
            Required. Map of tag template field IDs to the settings for
            the field. This map is an exhaustive list of the allowed
            fields. This map must contain at least one field and at most
            500 fields.

            The keys to this map are tag template field IDs. Field IDs
            can contain letters (both uppercase and lowercase), numbers
            (0-9) and underscores (\_). Field IDs must be at least 1
            character long and at most 64 characters long. Field IDs
            must start with a letter or underscore.
        dataplex_transfer_status (google.cloud.datacatalog_v1beta1.types.TagTemplate.DataplexTransferStatus):
            Output only. Transfer status of the
            TagTemplate
    """

    class DataplexTransferStatus(proto.Enum):
        r"""This enum describes TagTemplate transfer status to Dataplex
        service.

        Values:
            DATAPLEX_TRANSFER_STATUS_UNSPECIFIED (0):
                Default value. TagTemplate and its tags are
                only visible and editable in DataCatalog.
            MIGRATED (1):
                TagTemplate and its tags are auto-copied to
                Dataplex service. Visible in both services.
                Editable in DataCatalog, read-only in Dataplex.
                Deprecated: Individual TagTemplate migration is
                deprecated in favor of organization or project
                wide TagTemplate migration opt-in.
        """

        DATAPLEX_TRANSFER_STATUS_UNSPECIFIED = 0
        MIGRATED = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    fields: MutableMapping[str, "TagTemplateField"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message="TagTemplateField",
    )
    dataplex_transfer_status: DataplexTransferStatus = proto.Field(
        proto.ENUM,
        number=7,
        enum=DataplexTransferStatus,
    )


class TagTemplateField(proto.Message):
    r"""The template for an individual field within a tag template.

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the tag
            template field in URL format. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template}/fields/{field}

            Note that this TagTemplateField may not actually be stored
            in the location in this name.
        display_name (str):
            The display name for this field. Defaults to
            an empty string.
        type_ (google.cloud.datacatalog_v1beta1.types.FieldType):
            Required. The type of value this tag field
            can contain.
        is_required (bool):
            Whether this is a required field. Defaults to
            false.
        description (str):
            The description for this field. Defaults to
            an empty string.
        order (int):
            The order of this field with respect to other
            fields in this tag template.  A higher value
            indicates a more important field. The value can
            be negative. Multiple fields can have the same
            order, and field orders within a tag do not have
            to be sequential.
    """

    name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "FieldType" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FieldType",
    )
    is_required: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order: int = proto.Field(
        proto.INT32,
        number=5,
    )


class FieldType(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        primitive_type (google.cloud.datacatalog_v1beta1.types.FieldType.PrimitiveType):
            Represents primitive types - string, bool
            etc.

            This field is a member of `oneof`_ ``type_decl``.
        enum_type (google.cloud.datacatalog_v1beta1.types.FieldType.EnumType):
            Represents an enum type.

            This field is a member of `oneof`_ ``type_decl``.
    """

    class PrimitiveType(proto.Enum):
        r"""

        Values:
            PRIMITIVE_TYPE_UNSPECIFIED (0):
                This is the default invalid value for a type.
            DOUBLE (1):
                A double precision number.
            STRING (2):
                An UTF-8 string.
            BOOL (3):
                A boolean value.
            TIMESTAMP (4):
                A timestamp.
        """

        PRIMITIVE_TYPE_UNSPECIFIED = 0
        DOUBLE = 1
        STRING = 2
        BOOL = 3
        TIMESTAMP = 4

    class EnumType(proto.Message):
        r"""

        Attributes:
            allowed_values (MutableSequence[google.cloud.datacatalog_v1beta1.types.FieldType.EnumType.EnumValue]):

        """

        class EnumValue(proto.Message):
            r"""

            Attributes:
                display_name (str):
                    Required. The display name of the enum value.
                    Must not be an empty string.
            """

            display_name: str = proto.Field(
                proto.STRING,
                number=1,
            )

        allowed_values: MutableSequence["FieldType.EnumType.EnumValue"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="FieldType.EnumType.EnumValue",
            )
        )

    primitive_type: PrimitiveType = proto.Field(
        proto.ENUM,
        number=1,
        oneof="type_decl",
        enum=PrimitiveType,
    )
    enum_type: EnumType = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type_decl",
        message=EnumType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
