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
    package="google.cloud.datacatalog.v1",
    manifest={
        "Schema",
        "ColumnSchema",
    },
)


class Schema(proto.Message):
    r"""Represents a schema, for example, a BigQuery, GoogleSQL, or
    Avro schema.

    Attributes:
        columns (MutableSequence[google.cloud.datacatalog_v1.types.ColumnSchema]):
            The unified GoogleSQL-like schema of columns.

            The overall maximum number of columns and nested
            columns is 10,000. The maximum nested depth is
            15 levels.
    """

    columns: MutableSequence["ColumnSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ColumnSchema",
    )


class ColumnSchema(proto.Message):
    r"""A column within a schema. Columns can be nested inside
    other columns.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        column (str):
            Required. Name of the column.

            Must be a UTF-8 string without dots (.).
            The maximum size is 64 bytes.
        type_ (str):
            Required. Type of the column.

            Must be a UTF-8 string with the maximum size of
            128 bytes.
        description (str):
            Optional. Description of the column. Default
            value is an empty string.
            The description must be a UTF-8 string with the
            maximum size of 2000 bytes.
        mode (str):
            Optional. A column's mode indicates whether values in this
            column are required, nullable, or repeated.

            Only ``NULLABLE``, ``REQUIRED``, and ``REPEATED`` values are
            supported. Default mode is ``NULLABLE``.
        default_value (str):
            Optional. Default value for the column.
        ordinal_position (int):
            Optional. Ordinal position
        highest_indexing_type (google.cloud.datacatalog_v1.types.ColumnSchema.IndexingType):
            Optional. Most important inclusion of this
            column.
        subcolumns (MutableSequence[google.cloud.datacatalog_v1.types.ColumnSchema]):
            Optional. Schema of sub-columns. A column can
            have zero or more sub-columns.
        looker_column_spec (google.cloud.datacatalog_v1.types.ColumnSchema.LookerColumnSpec):
            Looker specific column info of this column.

            This field is a member of `oneof`_ ``system_spec``.
        range_element_type (google.cloud.datacatalog_v1.types.ColumnSchema.FieldElementType):
            Optional. The subtype of the RANGE, if the type of this
            field is RANGE. If the type is RANGE, this field is
            required. Possible values for the field element type of a
            RANGE include:

            - DATE
            - DATETIME
            - TIMESTAMP
        gc_rule (str):
            Optional. Garbage collection policy for the
            column or column family. Applies to systems like
            Cloud Bigtable.
    """

    class IndexingType(proto.Enum):
        r"""Specifies inclusion of the column in an index

        Values:
            INDEXING_TYPE_UNSPECIFIED (0):
                Unspecified.
            INDEXING_TYPE_NONE (1):
                Column not a part of an index.
            INDEXING_TYPE_NON_UNIQUE (2):
                Column Part of non unique index.
            INDEXING_TYPE_UNIQUE (3):
                Column part of unique index.
            INDEXING_TYPE_PRIMARY_KEY (4):
                Column part of the primary key.
        """

        INDEXING_TYPE_UNSPECIFIED = 0
        INDEXING_TYPE_NONE = 1
        INDEXING_TYPE_NON_UNIQUE = 2
        INDEXING_TYPE_UNIQUE = 3
        INDEXING_TYPE_PRIMARY_KEY = 4

    class LookerColumnSpec(proto.Message):
        r"""Column info specific to Looker System.

        Attributes:
            type_ (google.cloud.datacatalog_v1.types.ColumnSchema.LookerColumnSpec.LookerColumnType):
                Looker specific column type of this column.
        """

        class LookerColumnType(proto.Enum):
            r"""Column type in Looker.

            Values:
                LOOKER_COLUMN_TYPE_UNSPECIFIED (0):
                    Unspecified.
                DIMENSION (1):
                    Dimension.
                DIMENSION_GROUP (2):
                    Dimension group - parent for Dimension.
                FILTER (3):
                    Filter.
                MEASURE (4):
                    Measure.
                PARAMETER (5):
                    Parameter.
            """

            LOOKER_COLUMN_TYPE_UNSPECIFIED = 0
            DIMENSION = 1
            DIMENSION_GROUP = 2
            FILTER = 3
            MEASURE = 4
            PARAMETER = 5

        type_: "ColumnSchema.LookerColumnSpec.LookerColumnType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ColumnSchema.LookerColumnSpec.LookerColumnType",
        )

    class FieldElementType(proto.Message):
        r"""Represents the type of a field element.

        Attributes:
            type_ (str):
                Required. The type of a field element. See
                [ColumnSchema.type][google.cloud.datacatalog.v1.ColumnSchema.type].
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )

    column: str = proto.Field(
        proto.STRING,
        number=6,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mode: str = proto.Field(
        proto.STRING,
        number=3,
    )
    default_value: str = proto.Field(
        proto.STRING,
        number=8,
    )
    ordinal_position: int = proto.Field(
        proto.INT32,
        number=9,
    )
    highest_indexing_type: IndexingType = proto.Field(
        proto.ENUM,
        number=10,
        enum=IndexingType,
    )
    subcolumns: MutableSequence["ColumnSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ColumnSchema",
    )
    looker_column_spec: LookerColumnSpec = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="system_spec",
        message=LookerColumnSpec,
    )
    range_element_type: FieldElementType = proto.Field(
        proto.MESSAGE,
        number=19,
        message=FieldElementType,
    )
    gc_rule: str = proto.Field(
        proto.STRING,
        number=11,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
