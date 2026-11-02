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
        "ArrowSchema",
        "ArrowRecordBatch",
        "ArrowSerializationOptions",
    },
)


class ArrowSchema(proto.Message):
    r"""Arrow schema as specified in
    https://arrow.apache.org/docs/python/api/datatypes.html and
    serialized to bytes using IPC:

    https://arrow.apache.org/docs/format/Columnar.html#serialization-and-interprocess-communication-ipc

    See code samples on how this message can be deserialized.

    Attributes:
        serialized_schema (bytes):
            IPC serialized Arrow schema.
    """

    serialized_schema: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class ArrowRecordBatch(proto.Message):
    r"""Arrow RecordBatch.

    Attributes:
        serialized_record_batch (bytes):
            IPC-serialized Arrow RecordBatch.
        row_count (int):
            [Deprecated] The count of rows in
            ``serialized_record_batch``. Please use the
            format-independent ReadRowsResponse.row_count instead.
    """

    serialized_record_batch: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class ArrowSerializationOptions(proto.Message):
    r"""Contains options specific to Arrow Serialization.

    Attributes:
        buffer_compression (google.cloud.bigquery_storage_v1.types.ArrowSerializationOptions.CompressionCodec):
            The compression codec to use for Arrow
            buffers in serialized record batches.
        picos_timestamp_precision (google.cloud.bigquery_storage_v1.types.ArrowSerializationOptions.PicosTimestampPrecision):
            Optional. Set timestamp precision option. If
            not set, the default precision is microseconds.
    """

    class CompressionCodec(proto.Enum):
        r"""Compression codec's supported by Arrow.

        Values:
            COMPRESSION_UNSPECIFIED (0):
                If unspecified no compression will be used.
            LZ4_FRAME (1):
                LZ4 Frame
                (https://github.com/lz4/lz4/blob/dev/doc/lz4_Frame_format.md)
            ZSTD (2):
                Zstandard compression.
        """

        COMPRESSION_UNSPECIFIED = 0
        LZ4_FRAME = 1
        ZSTD = 2

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
                value will be encoded as Arrow TIMESTAMP type in
                a 64 bit integer.
            TIMESTAMP_PRECISION_NANOS (2):
                Timestamp values returned by Read API will be
                truncated to nanosecond level precision. The
                value will be encoded as Arrow TIMESTAMP type in
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

    buffer_compression: CompressionCodec = proto.Field(
        proto.ENUM,
        number=2,
        enum=CompressionCodec,
    )
    picos_timestamp_precision: PicosTimestampPrecision = proto.Field(
        proto.ENUM,
        number=3,
        enum=PicosTimestampPrecision,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
