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
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "DocumentSchema",
        "PropertyDefinition",
        "IntegerTypeOptions",
        "FloatTypeOptions",
        "TextTypeOptions",
        "DateTimeTypeOptions",
        "MapTypeOptions",
        "TimestampTypeOptions",
        "PropertyTypeOptions",
        "EnumTypeOptions",
    },
)


class DocumentSchema(proto.Message):
    r"""A document schema used to define document structure.

    Attributes:
        name (str):
            The resource name of the document schema. Format:
            projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.

            The name is ignored when creating a document schema.
        display_name (str):
            Required. Name of the schema given by the
            user. Must be unique per project.
        property_definitions (MutableSequence[google.cloud.contentwarehouse_v1.types.PropertyDefinition]):
            Document details.
        document_is_folder (bool):
            Document Type, true refers the document is a
            folder, otherwise it is a typical document.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the document
            schema is last updated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the document
            schema is created.
        description (str):
            Schema description.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    property_definitions: MutableSequence["PropertyDefinition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="PropertyDefinition",
    )
    document_is_folder: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )


class PropertyDefinition(proto.Message):
    r"""Defines the metadata for a schema property.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the metadata property. Must be unique
            within a document schema and is case insensitive. Names must
            be non-blank, start with a letter, and can contain
            alphanumeric characters and: /, :, -, \_, and .
        display_name (str):
            The display-name for the property, used for
            front-end.
        is_repeatable (bool):
            Whether the property can have multiple
            values.
        is_filterable (bool):
            Whether the property can be filtered. If this
            is a sub-property, all the parent properties
            must be marked filterable.
        is_searchable (bool):
            Indicates that the property should be
            included in a global search.
        is_metadata (bool):
            Whether the property is user supplied
            metadata. This out-of-the box placeholder
            setting can be used to tag derived properties.
            Its value and interpretation logic should be
            implemented by API user.
        is_required (bool):
            Whether the property is mandatory.
            Default is 'false', i.e. populating property
            value can be skipped. If 'true' then user must
            populate the value for this property.
        retrieval_importance (google.cloud.contentwarehouse_v1.types.PropertyDefinition.RetrievalImportance):
            The retrieval importance of the property
            during search.
        integer_type_options (google.cloud.contentwarehouse_v1.types.IntegerTypeOptions):
            Integer property.

            This field is a member of `oneof`_ ``value_type_options``.
        float_type_options (google.cloud.contentwarehouse_v1.types.FloatTypeOptions):
            Float property.

            This field is a member of `oneof`_ ``value_type_options``.
        text_type_options (google.cloud.contentwarehouse_v1.types.TextTypeOptions):
            Text/string property.

            This field is a member of `oneof`_ ``value_type_options``.
        property_type_options (google.cloud.contentwarehouse_v1.types.PropertyTypeOptions):
            Nested structured data property.

            This field is a member of `oneof`_ ``value_type_options``.
        enum_type_options (google.cloud.contentwarehouse_v1.types.EnumTypeOptions):
            Enum/categorical property.

            This field is a member of `oneof`_ ``value_type_options``.
        date_time_type_options (google.cloud.contentwarehouse_v1.types.DateTimeTypeOptions):
            Date time property.
            It is not supported by CMEK compliant
            deployment.

            This field is a member of `oneof`_ ``value_type_options``.
        map_type_options (google.cloud.contentwarehouse_v1.types.MapTypeOptions):
            Map property.

            This field is a member of `oneof`_ ``value_type_options``.
        timestamp_type_options (google.cloud.contentwarehouse_v1.types.TimestampTypeOptions):
            Timestamp property.
            It is not supported by CMEK compliant
            deployment.

            This field is a member of `oneof`_ ``value_type_options``.
        schema_sources (MutableSequence[google.cloud.contentwarehouse_v1.types.PropertyDefinition.SchemaSource]):
            The mapping information between this property
            to another schema source.
    """

    class RetrievalImportance(proto.Enum):
        r"""Stores the retrieval importance.

        Values:
            RETRIEVAL_IMPORTANCE_UNSPECIFIED (0):
                No importance specified. Default medium
                importance.
            HIGHEST (1):
                Highest importance.
            HIGHER (2):
                Higher importance.
            HIGH (3):
                High importance.
            MEDIUM (4):
                Medium importance.
            LOW (5):
                Low importance (negative).
            LOWEST (6):
                Lowest importance (negative).
        """

        RETRIEVAL_IMPORTANCE_UNSPECIFIED = 0
        HIGHEST = 1
        HIGHER = 2
        HIGH = 3
        MEDIUM = 4
        LOW = 5
        LOWEST = 6

    class SchemaSource(proto.Message):
        r"""The schema source information.

        Attributes:
            name (str):
                The schema name in the source.
            processor_type (str):
                The Doc AI processor type name.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        processor_type: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    is_repeatable: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    is_filterable: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    is_searchable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    is_metadata: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    is_required: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    retrieval_importance: RetrievalImportance = proto.Field(
        proto.ENUM,
        number=18,
        enum=RetrievalImportance,
    )
    integer_type_options: "IntegerTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="value_type_options",
        message="IntegerTypeOptions",
    )
    float_type_options: "FloatTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="value_type_options",
        message="FloatTypeOptions",
    )
    text_type_options: "TextTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="value_type_options",
        message="TextTypeOptions",
    )
    property_type_options: "PropertyTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="value_type_options",
        message="PropertyTypeOptions",
    )
    enum_type_options: "EnumTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="value_type_options",
        message="EnumTypeOptions",
    )
    date_time_type_options: "DateTimeTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="value_type_options",
        message="DateTimeTypeOptions",
    )
    map_type_options: "MapTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="value_type_options",
        message="MapTypeOptions",
    )
    timestamp_type_options: "TimestampTypeOptions" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="value_type_options",
        message="TimestampTypeOptions",
    )
    schema_sources: MutableSequence[SchemaSource] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=SchemaSource,
    )


class IntegerTypeOptions(proto.Message):
    r"""Configurations for an integer property."""


class FloatTypeOptions(proto.Message):
    r"""Configurations for a float property."""


class TextTypeOptions(proto.Message):
    r"""Configurations for a text property."""


class DateTimeTypeOptions(proto.Message):
    r"""Configurations for a date time property."""


class MapTypeOptions(proto.Message):
    r"""Configurations for a Map property."""


class TimestampTypeOptions(proto.Message):
    r"""Configurations for a timestamp property."""


class PropertyTypeOptions(proto.Message):
    r"""Configurations for a nested structured data property.

    Attributes:
        property_definitions (MutableSequence[google.cloud.contentwarehouse_v1.types.PropertyDefinition]):
            Required. List of property definitions.
    """

    property_definitions: MutableSequence["PropertyDefinition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PropertyDefinition",
    )


class EnumTypeOptions(proto.Message):
    r"""Configurations for an enum/categorical property.

    Attributes:
        possible_values (MutableSequence[str]):
            Required. List of possible enum values.
        validation_check_disabled (bool):
            Make sure the Enum property value provided in
            the document is in the possile value list during
            document creation. The validation check runs by
            default.
    """

    possible_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    validation_check_disabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
