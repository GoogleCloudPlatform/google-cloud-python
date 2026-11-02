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
    package="google.cloud.datacatalog.v1",
    manifest={
        "Tag",
        "TagField",
        "TagTemplate",
        "TagTemplateField",
        "FieldType",
    },
)


class Tag(proto.Message):
    r"""Tags contain custom metadata and are attached to Data Catalog
    resources. Tags conform with the specification of their tag
    template.

    See `Data Catalog
    IAM <https://cloud.google.com/data-catalog/docs/concepts/iam>`__ for
    information on the permissions needed to create or view tags.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the tag in
            URL format where tag ID is a system-generated
            identifier.

            Note: The tag itself might not be stored in the
            location specified in its name.
        template (str):
            Required. The resource name of the tag template this tag
            uses. Example:

            ``projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE_ID}``

            This field cannot be modified after creation.
        template_display_name (str):
            Output only. The display name of the tag
            template.
        column (str):
            Resources like entry can have schemas associated with them.
            This scope allows you to attach tags to an individual column
            based on that schema.

            To attach a tag to a nested column, separate column names
            with a dot (``.``). Example: ``column.nested_column``.

            This field is a member of `oneof`_ ``scope``.
        fields (MutableMapping[str, google.cloud.datacatalog_v1.types.TagField]):
            Required. Maps the ID of a tag field to its
            value and additional information about that
            field.

            Tag template defines valid field IDs. A tag
            must have at least 1 field and at most 500
            fields.
        dataplex_transfer_status (google.cloud.datacatalog_v1.types.TagTemplate.DataplexTransferStatus):
            Output only. Denotes the transfer status of
            the Tag Template.
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
    dataplex_transfer_status: "TagTemplate.DataplexTransferStatus" = proto.Field(
        proto.ENUM,
        number=7,
        enum="TagTemplate.DataplexTransferStatus",
    )


class TagField(proto.Message):
    r"""Contains the value and additional information on a field within a
    [Tag][google.cloud.datacatalog.v1.Tag].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            Output only. The display name of this field.
        double_value (float):
            The value of a tag field with a double type.

            This field is a member of `oneof`_ ``kind``.
        string_value (str):
            The value of a tag field with a string type.

            The maximum length is 2000 UTF-8 characters.

            This field is a member of `oneof`_ ``kind``.
        bool_value (bool):
            The value of a tag field with a boolean type.

            This field is a member of `oneof`_ ``kind``.
        timestamp_value (google.protobuf.timestamp_pb2.Timestamp):
            The value of a tag field with a timestamp
            type.

            This field is a member of `oneof`_ ``kind``.
        enum_value (google.cloud.datacatalog_v1.types.TagField.EnumValue):
            The value of a tag field with an enum type.

            This value must be one of the allowed values
            listed in this enum.

            This field is a member of `oneof`_ ``kind``.
        richtext_value (str):
            The value of a tag field with a rich text
            type.
            The maximum length is 10 MiB as this value holds
            HTML descriptions including encoded images. The
            maximum length of the text without images is 100
            KiB.

            This field is a member of `oneof`_ ``kind``.
        order (int):
            Output only. The order of this field with respect to other
            fields in this tag. Can be set by
            [Tag][google.cloud.datacatalog.v1.TagTemplateField.order].

            For example, a higher value can indicate a more important
            field. The value can be negative. Multiple fields can have
            the same order, and field orders within a tag don't have to
            be sequential.
    """

    class EnumValue(proto.Message):
        r"""An enum value.

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
    richtext_value: str = proto.Field(
        proto.STRING,
        number=8,
        oneof="kind",
    )
    order: int = proto.Field(
        proto.INT32,
        number=7,
    )


class TagTemplate(proto.Message):
    r"""A tag template defines a tag that can have one or more typed fields.

    The template is used to create tags that are attached to Google
    Cloud resources. [Tag template roles]
    (https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
    provide permissions to create, edit, and use the template. For
    example, see the [TagTemplate User]
    (https://cloud.google.com/data-catalog/docs/how-to/template-user)
    role that includes a permission to use the tag template to tag
    resources.

    Attributes:
        name (str):
            Identifier. The resource name of the tag
            template in URL format.
            Note: The tag template itself and its child
            resources might not be stored in the location
            specified in its name.
        display_name (str):
            Display name for this template. Defaults to an empty string.

            The name must contain only Unicode letters, numbers (0-9),
            underscores (\_), dashes (-), spaces ( ), and can't start or
            end with spaces. The maximum length is 200 characters.
        is_publicly_readable (bool):
            Indicates whether tags created with this template are
            public. Public tags do not require tag template access to
            appear in
            [ListTags][google.cloud.datacatalog.v1.DataCatalog.ListTags]
            API response.

            Additionally, you can search for a public tag by value with
            a simple search query in addition to using a ``tag:``
            predicate.
        fields (MutableMapping[str, google.cloud.datacatalog_v1.types.TagTemplateField]):
            Required. Map of tag template field IDs to the settings for
            the field. This map is an exhaustive list of the allowed
            fields. The map must contain at least one field and at most
            500 fields.

            The keys to this map are tag template field IDs. The IDs
            have the following limitations:

            - Can contain uppercase and lowercase letters, numbers (0-9)
              and underscores (\_).
            - Must be at least 1 character and at most 64 characters
              long.
            - Must start with a letter or underscore.
        dataplex_transfer_status (google.cloud.datacatalog_v1.types.TagTemplate.DataplexTransferStatus):
            Optional. Transfer status of the TagTemplate
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
            TRANSFERRED (2):
                TagTemplate and its tags are auto-copied to
                Dataplex service. Visible in both services.
                Editable in Dataplex, read-only in DataCatalog.
        """

        DATAPLEX_TRANSFER_STATUS_UNSPECIFIED = 0
        MIGRATED = 1
        TRANSFERRED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    is_publicly_readable: bool = proto.Field(
        proto.BOOL,
        number=5,
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
            Identifier. The resource name of the tag template field in
            URL format. Example:

            ``projects/{PROJECT_ID}/locations/{LOCATION}/tagTemplates/{TAG_TEMPLATE}/fields/{FIELD}``

            Note: The tag template field itself might not be stored in
            the location specified in its name.

            The name must contain only letters (a-z, A-Z), numbers
            (0-9), or underscores (\_), and must start with a letter or
            underscore. The maximum length is 64 characters.
        display_name (str):
            The display name for this field. Defaults to an empty
            string.

            The name must contain only Unicode letters, numbers (0-9),
            underscores (\_), dashes (-), spaces ( ), and can't start or
            end with spaces. The maximum length is 200 characters.
        type_ (google.cloud.datacatalog_v1.types.FieldType):
            Required. The type of value this tag field
            can contain.
        is_required (bool):
            If true, this field is required. Defaults to
            false.
        description (str):
            The description for this field. Defaults to
            an empty string.
        order (int):
            The order of this field with respect to other
            fields in this tag template.

            For example, a higher value can indicate a more
            important field. The value can be negative.
            Multiple fields can have the same order and
            field orders within a tag don't have to be
            sequential.
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
        primitive_type (google.cloud.datacatalog_v1.types.FieldType.PrimitiveType):
            Primitive types, such as string, boolean,
            etc.

            This field is a member of `oneof`_ ``type_decl``.
        enum_type (google.cloud.datacatalog_v1.types.FieldType.EnumType):
            An enum type.

            This field is a member of `oneof`_ ``type_decl``.
    """

    class PrimitiveType(proto.Enum):
        r"""

        Values:
            PRIMITIVE_TYPE_UNSPECIFIED (0):
                The default invalid value for a type.
            DOUBLE (1):
                A double precision number.
            STRING (2):
                An UTF-8 string.
            BOOL (3):
                A boolean value.
            TIMESTAMP (4):
                A timestamp.
            RICHTEXT (5):
                A Richtext description.
        """

        PRIMITIVE_TYPE_UNSPECIFIED = 0
        DOUBLE = 1
        STRING = 2
        BOOL = 3
        TIMESTAMP = 4
        RICHTEXT = 5

    class EnumType(proto.Message):
        r"""

        Attributes:
            allowed_values (MutableSequence[google.cloud.datacatalog_v1.types.FieldType.EnumType.EnumValue]):
                The set of allowed values for this enum.

                This set must not be empty and can include up to 100 allowed
                values. The display names of the values in this set must not
                be empty and must be case-insensitively unique within this
                set.

                The order of items in this set is preserved. This field can
                be used to create, remove, and reorder enum values. To
                rename enum values, use the
                ``RenameTagTemplateFieldEnumValue`` method.
        """

        class EnumValue(proto.Message):
            r"""

            Attributes:
                display_name (str):
                    Required. The display name of the enum value. Must not be an
                    empty string.

                    The name must contain only Unicode letters, numbers (0-9),
                    underscores (\_), dashes (-), spaces ( ), and can't start or
                    end with spaces. The maximum length is 200 characters.
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
