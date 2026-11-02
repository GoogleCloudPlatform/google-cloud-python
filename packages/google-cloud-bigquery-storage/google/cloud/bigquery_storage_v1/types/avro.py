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
    package="google.cloud.bigquery.storage.v1",
    manifest={
        "AvroSchema",
        "AvroRows",
        "AvroSerializationOptions",
    },
)


class AvroSchema(proto.Message):
    r"""Avro schema.

    Attributes:
        schema (str):
            Json serialized schema, as described at
            https://avro.apache.org/docs/1.8.1/spec.html.
    """

    schema: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AvroRows(proto.Message):
    r"""Avro rows.

    Attributes:
        serialized_binary_rows (bytes):
            Binary serialized rows in a block.
        row_count (int):
            [Deprecated] The count of rows in the returning block.
            Please use the format-independent ReadRowsResponse.row_count
            instead.
    """

    serialized_binary_rows: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class AvroSerializationOptions(proto.Message):
    r"""Contains options specific to Avro Serialization.

    Attributes:
        enable_display_name_attribute (bool):
            Enable displayName attribute in Avro schema.

            The Avro specification requires field names to
            be alphanumeric.  By default, in cases when
            column names do not conform to these
            requirements (e.g. non-ascii unicode codepoints)
            and Avro is requested as an output format, the
            CreateReadSession call will fail.

            Setting this field to true, populates avro field
            names with a placeholder value and populates a
            "displayName" attribute for every avro field
            with the original column name.
        picos_timestamp_precision (google.cloud.bigquery_storage_v1.types.AvroSerializationOptions.PicosTimestampPrecision):
            Optional. Set timestamp precision option. If
            not set, the default precision is microseconds.
    """

    class PicosTimestampPrecision(proto.Enum):
        r"""The precision of the timestamp value in the Avro message. This
        precision will **only** be applied to the column(s) with the
        ``TIMESTAMP_PICOS`` type.

        Values:
            PICOS_TIMESTAMP_PRECISION_UNSPECIFIED (0):
                Unspecified timestamp precision. The default
                precision is microseconds.
            TIMESTAMP_PRECISION_MICROS (1):
                Timestamp values returned by Read API will be
                truncated to microsecond level precision. The
                value will be encoded as Avro TIMESTAMP type in
                a 64 bit integer.
            TIMESTAMP_PRECISION_NANOS (2):
                Timestamp values returned by Read API will be
                truncated to nanosecond level precision. The
                value will be encoded as Avro TIMESTAMP type in
                a 64 bit integer.
            TIMESTAMP_PRECISION_PICOS (3):
                Read API will return full precision
                picosecond value. The value will be encoded as a
                string which conforms to ISO 8601 format.
        """

        PICOS_TIMESTAMP_PRECISION_UNSPECIFIED = 0
        TIMESTAMP_PRECISION_MICROS = 1
        TIMESTAMP_PRECISION_NANOS = 2
        TIMESTAMP_PRECISION_PICOS = 3

    enable_display_name_attribute: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    picos_timestamp_precision: PicosTimestampPrecision = proto.Field(
        proto.ENUM,
        number=2,
        enum=PicosTimestampPrecision,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
