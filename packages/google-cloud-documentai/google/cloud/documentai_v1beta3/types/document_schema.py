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

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1beta3",
    manifest={
        "SummaryOptions",
        "FieldExtractionMetadata",
        "PropertyMetadata",
        "EntityTypeMetadata",
        "DocumentSchema",
    },
)


class SummaryOptions(proto.Message):
    r"""Metadata for document summarization.

    Attributes:
        length (google.cloud.documentai_v1beta3.types.SummaryOptions.Length):
            How long the summary should be.
        format_ (google.cloud.documentai_v1beta3.types.SummaryOptions.Format):
            The format the summary should be in.
    """

    class Length(proto.Enum):
        r"""The Length enum.

        Values:
            LENGTH_UNSPECIFIED (0):
                Default.
            BRIEF (1):
                A brief summary of one or two sentences.
            MODERATE (2):
                A paragraph-length summary.
            COMPREHENSIVE (3):
                The longest option available.
        """

        LENGTH_UNSPECIFIED = 0
        BRIEF = 1
        MODERATE = 2
        COMPREHENSIVE = 3

    class Format(proto.Enum):
        r"""The Format enum.

        Values:
            FORMAT_UNSPECIFIED (0):
                Default.
            PARAGRAPH (1):
                Format the output in paragraphs.
            BULLETS (2):
                Format the output in bullets.
        """

        FORMAT_UNSPECIFIED = 0
        PARAGRAPH = 1
        BULLETS = 2

    length: Length = proto.Field(
        proto.ENUM,
        number=1,
        enum=Length,
    )
    format_: Format = proto.Field(
        proto.ENUM,
        number=2,
        enum=Format,
    )


class FieldExtractionMetadata(proto.Message):
    r"""Metadata for how this field value is extracted.

    Attributes:
        summary_options (google.cloud.documentai_v1beta3.types.SummaryOptions):
            Summary options config.
    """

    summary_options: "SummaryOptions" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SummaryOptions",
    )


class PropertyMetadata(proto.Message):
    r"""Metadata about a property.

    Attributes:
        inactive (bool):
            Whether the property should be considered as
            "inactive".
        field_extraction_metadata (google.cloud.documentai_v1beta3.types.FieldExtractionMetadata):
            Field extraction metadata on the property.
    """

    inactive: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    field_extraction_metadata: "FieldExtractionMetadata" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="FieldExtractionMetadata",
    )


class EntityTypeMetadata(proto.Message):
    r"""Metadata about an entity type.

    Attributes:
        inactive (bool):
            Whether the entity type should be considered
            inactive.
    """

    inactive: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DocumentSchema(proto.Message):
    r"""The schema defines the output of the processed document by a
    processor.

    Attributes:
        display_name (str):
            Display name to show users.
        description (str):
            Description of the schema.
        entity_types (MutableSequence[google.cloud.documentai_v1beta3.types.DocumentSchema.EntityType]):
            Entity types of the schema.
        metadata (google.cloud.documentai_v1beta3.types.DocumentSchema.Metadata):
            Metadata of the schema.
        document_prompt (str):
            Optional. Document level prompt provided by
            the user. This custom text is injected into the
            AI model's prompt to provide extra,
            document-wide guidance for processing.
    """

    class EntityType(proto.Message):
        r"""EntityType is the wrapper of a label of the corresponding
        model with detailed attributes and limitations for entity-based
        processors. Multiple types can also compose a dependency tree to
        represent nested types.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            enum_values (google.cloud.documentai_v1beta3.types.DocumentSchema.EntityType.EnumValues):
                If specified, lists all the possible values for this entity.
                This should not be more than a handful of values. If the
                number of values is >10 or could change frequently, use the
                ``EntityType.value_ontology`` field and specify a list of
                all possible values in a value ontology file.

                This field is a member of `oneof`_ ``value_source``.
            display_name (str):
                User defined name for the type.
            name (str):
                Name of the type. It must be unique within the schema file
                and cannot be a "Common Type". The following naming
                conventions are used:

                - Use ``snake_casing``.
                - Name matching is case-sensitive.
                - Maximum 64 characters.
                - Must start with a letter.
                - Allowed characters: ASCII letters ``[a-z0-9_-]``. (For
                  backward compatibility, internal infrastructure and
                  tooling can handle any ASCII character.)
                - The ``/`` is sometimes used to denote a property of a
                  type. For example ``line_item/amount``. This convention is
                  deprecated, but will still be honored for backward
                  compatibility.
            description (str):
                The description of the entity type. Could be
                used to provide more information about the
                entity type for model calls.
            base_types (MutableSequence[str]):
                The entity type that this type is derived
                from.  For now, one and only one should be set.
            properties (MutableSequence[google.cloud.documentai_v1beta3.types.DocumentSchema.EntityType.Property]):
                Description the nested structure, or
                composition of an entity.
            entity_type_metadata (google.cloud.documentai_v1beta3.types.EntityTypeMetadata):
                Metadata for the entity type.
        """

        class EnumValues(proto.Message):
            r"""Defines the a list of enum values.

            Attributes:
                values (MutableSequence[str]):
                    The individual values that this enum values
                    type can include.
            """

            values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class Property(proto.Message):
            r"""Defines properties that can be part of the entity type.

            Attributes:
                name (str):
                    The name of the property.  Follows the same
                    guidelines as the EntityType name.
                description (str):
                    The description of the property. Could be
                    used to provide more information about the
                    property for model calls.
                display_name (str):
                    User defined name for the property.
                value_type (str):
                    A reference to the value type of the property. This type is
                    subject to the same conventions as the ``Entity.base_types``
                    field.
                occurrence_type (google.cloud.documentai_v1beta3.types.DocumentSchema.EntityType.Property.OccurrenceType):
                    Occurrence type limits the number of
                    instances an entity type appears in the
                    document.
                method (google.cloud.documentai_v1beta3.types.DocumentSchema.EntityType.Property.Method):
                    Specifies how the entity's value is obtained.
                property_metadata (google.cloud.documentai_v1beta3.types.PropertyMetadata):
                    Any additional metadata about the property
                    can be added here.
            """

            class OccurrenceType(proto.Enum):
                r"""Types of occurrences of the entity type in the document. This
                represents the number of instances, not mentions, of an entity. For
                example, a bank statement might only have one ``account_number``,
                but this account number can be mentioned in several places on the
                document. In this case, the ``account_number`` is considered a
                ``REQUIRED_ONCE`` entity type. If, on the other hand, it's expected
                that a bank statement contains the status of multiple different
                accounts for the customers, the occurrence type is set to
                ``REQUIRED_MULTIPLE``.

                Values:
                    OCCURRENCE_TYPE_UNSPECIFIED (0):
                        Unspecified occurrence type.
                    OPTIONAL_ONCE (1):
                        There will be zero or one instance of this
                        entity type.  The same entity instance may be
                        mentioned multiple times.
                    OPTIONAL_MULTIPLE (2):
                        The entity type will appear zero or multiple
                        times.
                    REQUIRED_ONCE (3):
                        The entity type will only appear exactly
                        once.  The same entity instance may be mentioned
                        multiple times.
                    REQUIRED_MULTIPLE (4):
                        The entity type will appear once or more
                        times.
                """

                OCCURRENCE_TYPE_UNSPECIFIED = 0
                OPTIONAL_ONCE = 1
                OPTIONAL_MULTIPLE = 2
                REQUIRED_ONCE = 3
                REQUIRED_MULTIPLE = 4

            class Method(proto.Enum):
                r"""Specifies how the entity's value is obtained from the
                document.

                Values:
                    METHOD_UNSPECIFIED (0):
                        Unspecified method. It defaults to ``EXTRACT``.
                    EXTRACT (1):
                        The entity's value is directly extracted
                        as-is from the document text.
                    DERIVE (2):
                        The entity's value is derived through
                        inference and is not necessarily an exact text
                        extraction from the document.
                """

                METHOD_UNSPECIFIED = 0
                EXTRACT = 1
                DERIVE = 2

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            description: str = proto.Field(
                proto.STRING,
                number=7,
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=6,
            )
            value_type: str = proto.Field(
                proto.STRING,
                number=2,
            )
            occurrence_type: "DocumentSchema.EntityType.Property.OccurrenceType" = (
                proto.Field(
                    proto.ENUM,
                    number=3,
                    enum="DocumentSchema.EntityType.Property.OccurrenceType",
                )
            )
            method: "DocumentSchema.EntityType.Property.Method" = proto.Field(
                proto.ENUM,
                number=8,
                enum="DocumentSchema.EntityType.Property.Method",
            )
            property_metadata: "PropertyMetadata" = proto.Field(
                proto.MESSAGE,
                number=5,
                message="PropertyMetadata",
            )

        enum_values: "DocumentSchema.EntityType.EnumValues" = proto.Field(
            proto.MESSAGE,
            number=14,
            oneof="value_source",
            message="DocumentSchema.EntityType.EnumValues",
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=13,
        )
        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=15,
        )
        base_types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        properties: MutableSequence["DocumentSchema.EntityType.Property"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="DocumentSchema.EntityType.Property",
            )
        )
        entity_type_metadata: "EntityTypeMetadata" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="EntityTypeMetadata",
        )

    class Metadata(proto.Message):
        r"""Metadata for global schema behavior.

        Attributes:
            document_splitter (bool):
                If true, a ``document`` entity type can be applied to
                subdocument (splitting). Otherwise, it can only be applied
                to the entire document (classification).
            document_allow_multiple_labels (bool):
                If true, on a given page, there can be multiple ``document``
                annotations covering it.
            prefixed_naming_on_properties (bool):
                If set, all the nested entities must be
                prefixed with the parents.
            skip_naming_validation (bool):
                If set, this will skip the naming format validation in the
                schema. So the string values in
                ``DocumentSchema.EntityType.name`` and
                ``DocumentSchema.EntityType.Property.name`` will not be
                checked.
        """

        document_splitter: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        document_allow_multiple_labels: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        prefixed_naming_on_properties: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        skip_naming_validation: bool = proto.Field(
            proto.BOOL,
            number=7,
        )

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entity_types: MutableSequence[EntityType] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=EntityType,
    )
    metadata: Metadata = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Metadata,
    )
    document_prompt: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
