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

import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.storage.v1",
    manifest={
        "TableSchema",
        "TableFieldSchema",
    },
)


class TableSchema(proto.Message):
    r"""Schema of a table. This schema is a subset of
    google.cloud.bigquery.v2.TableSchema containing information
    necessary to generate valid message to write to BigQuery.

    Attributes:
        fields (MutableSequence[google.cloud.bigquery_storage_v1.types.TableFieldSchema]):
            Describes the fields in a table.
    """

    fields: MutableSequence["TableFieldSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TableFieldSchema",
    )


class TableFieldSchema(proto.Message):
    r"""TableFieldSchema defines a single field/column within a table
    schema.

    Attributes:
        name (str):
            Required. The field name. The name must contain only letters
            (a-z, A-Z), numbers (0-9), or underscores (\_), and must
            start with a letter or underscore. The maximum length is 128
            characters.
        type_ (google.cloud.bigquery_storage_v1.types.TableFieldSchema.Type):
            Required. The field data type.
        mode (google.cloud.bigquery_storage_v1.types.TableFieldSchema.Mode):
            Optional. The field mode. The default value
            is NULLABLE.
        fields (MutableSequence[google.cloud.bigquery_storage_v1.types.TableFieldSchema]):
            Optional. Describes the nested schema fields
            if the type property is set to STRUCT.
        description (str):
            Optional. The field description. The maximum
            length is 1,024 characters.
        max_length (int):
            Optional. Maximum length of values of this field for STRINGS
            or BYTES.

            If max_length is not specified, no maximum length constraint
            is imposed on this field.

            If type = "STRING", then max_length represents the maximum
            UTF-8 length of strings in this field.

            If type = "BYTES", then max_length represents the maximum
            number of bytes in this field.

            It is invalid to set this field if type is not "STRING" or
            "BYTES".
        precision (int):
            Optional. Precision (maximum number of total digits in base
            10) and scale (maximum number of digits in the fractional
            part in base 10) constraints for values of this field for
            NUMERIC or BIGNUMERIC.

            It is invalid to set precision or scale if type is not
            "NUMERIC" or "BIGNUMERIC".

            If precision and scale are not specified, no value range
            constraint is imposed on this field insofar as values are
            permitted by the type.

            Values of this NUMERIC or BIGNUMERIC field must be in this
            range when:

            - Precision (P) and scale (S) are specified: [-10^(P-S) +
              10^(-S), 10^(P-S) - 10^(-S)]
            - Precision (P) is specified but not scale (and thus scale
              is interpreted to be equal to zero): [-10^P + 1, 10^P -
              1].

            Acceptable values for precision and scale if both are
            specified:

            - If type = "NUMERIC": 1 <= precision - scale <= 29 and 0 <=
              scale <= 9.
            - If type = "BIGNUMERIC": 1 <= precision - scale <= 38 and 0
              <= scale <= 38.

            Acceptable values for precision if only precision is
            specified but not scale (and thus scale is interpreted to be
            equal to zero):

            - If type = "NUMERIC": 1 <= precision <= 29.
            - If type = "BIGNUMERIC": 1 <= precision <= 38.

            If scale is specified but not precision, then it is invalid.
        scale (int):
            Optional. See documentation for precision.
        default_value_expression (str):
            Optional. A SQL expression to specify the [default value]
            (https://cloud.google.com/bigquery/docs/default-values) for
            this field.
        timestamp_precision (google.protobuf.wrappers_pb2.Int64Value):
            Optional. Precision (maximum number of total digits in base
            10) for seconds of TIMESTAMP type.

            Possible values include:

            - 6 (Default, for TIMESTAMP type with microsecond precision)
            - 12 (For TIMESTAMP type with picosecond precision)
        range_element_type (google.cloud.bigquery_storage_v1.types.TableFieldSchema.FieldElementType):
            Optional. The subtype of the RANGE, if the type of this
            field is RANGE. If the type is RANGE, this field is
            required. Possible values for the field element type of a
            RANGE include:

            - DATE
            - DATETIME
            - TIMESTAMP
    """

    class Type(proto.Enum):
        r"""

        Values:
            TYPE_UNSPECIFIED (0):
                Illegal value
            STRING (1):
                64K, UTF8
            INT64 (2):
                64-bit signed
            DOUBLE (3):
                64-bit IEEE floating point
            STRUCT (4):
                Aggregate type
            BYTES (5):
                64K, Binary
            BOOL (6):
                2-valued
            TIMESTAMP (7):
                64-bit signed usec since UTC epoch
            DATE (8):
                Civil date - Year, Month, Day
            TIME (9):
                Civil time - Hour, Minute, Second,
                Microseconds
            DATETIME (10):
                Combination of civil date and civil time
            GEOGRAPHY (11):
                Geography object
            NUMERIC (12):
                Numeric value
            BIGNUMERIC (13):
                BigNumeric value
            INTERVAL (14):
                Interval
            JSON (15):
                JSON, String
            RANGE (16):
                RANGE
        """

        TYPE_UNSPECIFIED = 0
        STRING = 1
        INT64 = 2
        DOUBLE = 3
        STRUCT = 4
        BYTES = 5
        BOOL = 6
        TIMESTAMP = 7
        DATE = 8
        TIME = 9
        DATETIME = 10
        GEOGRAPHY = 11
        NUMERIC = 12
        BIGNUMERIC = 13
        INTERVAL = 14
        JSON = 15
        RANGE = 16

    class Mode(proto.Enum):
        r"""

        Values:
            MODE_UNSPECIFIED (0):
                Illegal value
            NULLABLE (1):
                No description available.
            REQUIRED (2):
                No description available.
            REPEATED (3):
                No description available.
        """

        MODE_UNSPECIFIED = 0
        NULLABLE = 1
        REQUIRED = 2
        REPEATED = 3

    class FieldElementType(proto.Message):
        r"""Represents the type of a field element.

        Attributes:
            type_ (google.cloud.bigquery_storage_v1.types.TableFieldSchema.Type):
                Required. The type of a field element.
        """

        type_: "TableFieldSchema.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="TableFieldSchema.Type",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    mode: Mode = proto.Field(
        proto.ENUM,
        number=3,
        enum=Mode,
    )
    fields: MutableSequence["TableFieldSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="TableFieldSchema",
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    max_length: int = proto.Field(
        proto.INT64,
        number=7,
    )
    precision: int = proto.Field(
        proto.INT64,
        number=8,
    )
    scale: int = proto.Field(
        proto.INT64,
        number=9,
    )
    default_value_expression: str = proto.Field(
        proto.STRING,
        number=10,
    )
    timestamp_precision: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=27,
        message=wrappers_pb2.Int64Value,
    )
    range_element_type: FieldElementType = proto.Field(
        proto.MESSAGE,
        number=11,
        message=FieldElementType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
