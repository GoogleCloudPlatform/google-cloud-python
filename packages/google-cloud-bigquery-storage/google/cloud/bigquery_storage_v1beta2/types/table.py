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
    package="google.cloud.bigquery.storage.v1beta2",
    manifest={
        "TableSchema",
        "TableFieldSchema",
    },
)


class TableSchema(proto.Message):
    r"""Schema of a table

    Attributes:
        fields (MutableSequence[google.cloud.bigquery_storage_v1beta2.types.TableFieldSchema]):
            Describes the fields in a table.
    """

    fields: MutableSequence["TableFieldSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TableFieldSchema",
    )


class TableFieldSchema(proto.Message):
    r"""A field in TableSchema

    Attributes:
        name (str):
            Required. The field name. The name must contain only letters
            (a-z, A-Z), numbers (0-9), or underscores (\_), and must
            start with a letter or underscore. The maximum length is 128
            characters.
        type_ (google.cloud.bigquery_storage_v1beta2.types.TableFieldSchema.Type):
            Required. The field data type.
        mode (google.cloud.bigquery_storage_v1beta2.types.TableFieldSchema.Mode):
            Optional. The field mode. The default value
            is NULLABLE.
        fields (MutableSequence[google.cloud.bigquery_storage_v1beta2.types.TableFieldSchema]):
            Optional. Describes the nested schema fields
            if the type property is set to STRUCT.
        description (str):
            Optional. The field description. The maximum
            length is 1,024 characters.
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


__all__ = tuple(sorted(__protobuf__.manifest))
