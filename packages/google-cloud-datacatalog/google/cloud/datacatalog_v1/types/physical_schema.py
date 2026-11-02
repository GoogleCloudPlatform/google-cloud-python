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
        "PhysicalSchema",
    },
)


class PhysicalSchema(proto.Message):
    r"""Native schema used by a resource represented as an entry.
    Used by query engines for deserializing and parsing source data.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        avro (google.cloud.datacatalog_v1.types.PhysicalSchema.AvroSchema):
            Schema in Avro JSON format.

            This field is a member of `oneof`_ ``schema``.
        thrift (google.cloud.datacatalog_v1.types.PhysicalSchema.ThriftSchema):
            Schema in Thrift format.

            This field is a member of `oneof`_ ``schema``.
        protobuf (google.cloud.datacatalog_v1.types.PhysicalSchema.ProtobufSchema):
            Schema in protocol buffer format.

            This field is a member of `oneof`_ ``schema``.
        parquet (google.cloud.datacatalog_v1.types.PhysicalSchema.ParquetSchema):
            Marks a Parquet-encoded data source.

            This field is a member of `oneof`_ ``schema``.
        orc (google.cloud.datacatalog_v1.types.PhysicalSchema.OrcSchema):
            Marks an ORC-encoded data source.

            This field is a member of `oneof`_ ``schema``.
        csv (google.cloud.datacatalog_v1.types.PhysicalSchema.CsvSchema):
            Marks a CSV-encoded data source.

            This field is a member of `oneof`_ ``schema``.
    """

    class AvroSchema(proto.Message):
        r"""Schema in Avro JSON format.

        Attributes:
            text (str):
                JSON source of the Avro schema.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ThriftSchema(proto.Message):
        r"""Schema in Thrift format.

        Attributes:
            text (str):
                Thrift IDL source of the schema.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ProtobufSchema(proto.Message):
        r"""Schema in protocol buffer format.

        Attributes:
            text (str):
                Protocol buffer source of the schema.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ParquetSchema(proto.Message):
        r"""Marks a Parquet-encoded data source."""

    class OrcSchema(proto.Message):
        r"""Marks an ORC-encoded data source."""

    class CsvSchema(proto.Message):
        r"""Marks a CSV-encoded data source."""

    avro: AvroSchema = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="schema",
        message=AvroSchema,
    )
    thrift: ThriftSchema = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="schema",
        message=ThriftSchema,
    )
    protobuf: ProtobufSchema = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="schema",
        message=ProtobufSchema,
    )
    parquet: ParquetSchema = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="schema",
        message=ParquetSchema,
    )
    orc: OrcSchema = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="schema",
        message=OrcSchema,
    )
    csv: CsvSchema = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="schema",
        message=CsvSchema,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
