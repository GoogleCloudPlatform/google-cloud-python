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

from google.cloud.bigquery_storage_v1.types import arrow, avro
from google.cloud.bigquery_storage_v1.types import table as gcbs_table

__protobuf__ = proto.module(
    package="google.cloud.bigquery.storage.v1",
    manifest={
        "DataFormat",
        "WriteStreamView",
        "ReadSession",
        "ReadStream",
        "WriteStream",
    },
)


class DataFormat(proto.Enum):
    r"""Data format for input or output data.

    Values:
        DATA_FORMAT_UNSPECIFIED (0):
            Data format is unspecified.
        AVRO (1):
            Avro is a standard open source row based file
            format. See https://avro.apache.org/ for more
            details.
        ARROW (2):
            Arrow is a standard open source column-based
            message format. See https://arrow.apache.org/
            for more details.
    """

    DATA_FORMAT_UNSPECIFIED = 0
    AVRO = 1
    ARROW = 2


class WriteStreamView(proto.Enum):
    r"""WriteStreamView is a view enum that controls what details
    about a write stream should be returned.

    Values:
        WRITE_STREAM_VIEW_UNSPECIFIED (0):
            The default / unset value.
        BASIC (1):
            The BASIC projection returns basic metadata
            about a write stream.  The basic view does not
            include schema information.  This is the default
            view returned by GetWriteStream.
        FULL (2):
            The FULL projection returns all available
            write stream metadata, including the schema.
            CreateWriteStream returns the full projection of
            write stream metadata.
    """

    WRITE_STREAM_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class ReadSession(proto.Message):
    r"""Information about the ReadSession.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Unique identifier for the session, in the form
            ``projects/{project_id}/locations/{location}/sessions/{session_id}``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the session becomes invalid.
            After this time, subsequent requests to read this Session
            will return errors. The expire_time is automatically
            assigned and currently cannot be specified or updated.
        data_format (google.cloud.bigquery_storage_v1.types.DataFormat):
            Immutable. Data format of the output data.
            DATA_FORMAT_UNSPECIFIED not supported.
        avro_schema (google.cloud.bigquery_storage_v1.types.AvroSchema):
            Output only. Avro schema.

            This field is a member of `oneof`_ ``schema``.
        arrow_schema (google.cloud.bigquery_storage_v1.types.ArrowSchema):
            Output only. Arrow schema.

            This field is a member of `oneof`_ ``schema``.
        table (str):
            Immutable. Table that this ReadSession is reading from, in
            the form
            ``projects/{project_id}/datasets/{dataset_id}/tables/{table_id}``
        table_modifiers (google.cloud.bigquery_storage_v1.types.ReadSession.TableModifiers):
            Optional. Any modifiers which are applied
            when reading from the specified table.
        read_options (google.cloud.bigquery_storage_v1.types.ReadSession.TableReadOptions):
            Optional. Read options for this session (e.g.
            column selection, filters).
        streams (MutableSequence[google.cloud.bigquery_storage_v1.types.ReadStream]):
            Output only. A list of streams created with the session.

            At least one stream is created with the session. In the
            future, larger request_stream_count values *may* result in
            this list being unpopulated, in that case, the user will
            need to use a List method to get the streams instead, which
            is not yet available.
        estimated_total_bytes_scanned (int):
            Output only. An estimate on the number of
            bytes this session will scan when all streams
            are completely consumed. This estimate is based
            on metadata from the table which might be
            incomplete or stale.
        estimated_total_physical_file_size (int):
            Output only. A pre-projected estimate of the
            total physical size of files (in bytes) that
            this session will scan when all streams are
            consumed. This estimate is independent of the
            selected columns and can be based on incomplete
            or stale metadata from the table.  This field is
            only set for BigLake tables.
        estimated_row_count (int):
            Output only. An estimate on the number of
            rows present in this session's streams. This
            estimate is based on metadata from the table
            which might be incomplete or stale.
        trace_id (str):
            Optional. ID set by client to annotate a
            session identity.  This does not need to be
            strictly unique, but instead the same ID should
            be used to group logically connected sessions
            (e.g. All using the same ID for all sessions
            needed to complete a Spark SQL query is
            reasonable).

            Maximum length is 256 bytes.
    """

    class TableModifiers(proto.Message):
        r"""Additional attributes when reading a table.

        Attributes:
            snapshot_time (google.protobuf.timestamp_pb2.Timestamp):
                The snapshot time of the table. If not set,
                interpreted as now.
        """

        snapshot_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    class TableReadOptions(proto.Message):
        r"""Options dictating how we read a table.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            selected_fields (MutableSequence[str]):
                Optional. The names of the fields in the table to be
                returned. If no field names are specified, then all fields
                in the table are returned.

                Nested fields -- the child elements of a STRUCT field -- can
                be selected individually using their fully-qualified names,
                and will be returned as record fields containing only the
                selected nested fields. If a STRUCT field is specified in
                the selected fields list, all of the child elements will be
                returned.

                As an example, consider a table with the following schema:

                { "name": "struct_field", "type": "RECORD", "mode":
                "NULLABLE", "fields": [ { "name": "string_field1", "type":
                "STRING", . "mode": "NULLABLE" }, { "name": "string_field2",
                "type": "STRING", "mode": "NULLABLE" } ] }

                Specifying "struct_field" in the selected fields list will
                result in a read session schema with the following logical
                structure:

                struct_field { string_field1 string_field2 }

                Specifying "struct_field.string_field1" in the selected
                fields list will result in a read session schema with the
                following logical structure:

                struct_field { string_field1 }

                The order of the fields in the read session schema is
                derived from the table schema and does not correspond to the
                order in which the fields are specified in this list.
            row_restriction (str):
                SQL text filtering statement, similar to a WHERE clause in a
                query. Aggregates are not supported.

                Examples: "int_field > 5" "date_field = CAST('2014-9-27' as
                DATE)" "nullable_field is not NULL" "st_equals(geo_field,
                st_geofromtext("POINT(2, 2)"))" "numeric_field BETWEEN 1.0
                AND 5.0"

                Restricted to a maximum length for 1 MB.
            arrow_serialization_options (google.cloud.bigquery_storage_v1.types.ArrowSerializationOptions):
                Optional. Options specific to the Apache
                Arrow output format.

                This field is a member of `oneof`_ ``output_format_serialization_options``.
            avro_serialization_options (google.cloud.bigquery_storage_v1.types.AvroSerializationOptions):
                Optional. Options specific to the Apache Avro
                output format

                This field is a member of `oneof`_ ``output_format_serialization_options``.
            sample_percentage (float):
                Optional. Specifies a table sampling percentage.
                Specifically, the query planner will use TABLESAMPLE SYSTEM
                (sample_percentage PERCENT). The sampling percentage is
                applied at the data block granularity. It will randomly
                choose for each data block whether to read the rows in that
                data block. For more details, see
                https://cloud.google.com/bigquery/docs/table-sampling)

                This field is a member of `oneof`_ ``_sample_percentage``.
            response_compression_codec (google.cloud.bigquery_storage_v1.types.ReadSession.TableReadOptions.ResponseCompressionCodec):
                Optional. Set response_compression_codec when creating a
                read session to enable application-level compression of
                ReadRows responses.

                This field is a member of `oneof`_ ``_response_compression_codec``.
        """

        class ResponseCompressionCodec(proto.Enum):
            r"""Specifies which compression codec to attempt on the entire
            serialized response payload (either Arrow record batch or Avro
            rows). This is not to be confused with the Apache Arrow native
            compression codecs specified in ArrowSerializationOptions. For
            performance reasons, when creating a read session requesting
            Arrow responses, setting both native Arrow compression and
            application-level response compression will not be allowed -
            choose, at most, one kind of compression.

            Values:
                RESPONSE_COMPRESSION_CODEC_UNSPECIFIED (0):
                    Default is no compression.
                RESPONSE_COMPRESSION_CODEC_LZ4 (2):
                    Use raw LZ4 compression.
            """

            RESPONSE_COMPRESSION_CODEC_UNSPECIFIED = 0
            RESPONSE_COMPRESSION_CODEC_LZ4 = 2

        selected_fields: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        row_restriction: str = proto.Field(
            proto.STRING,
            number=2,
        )
        arrow_serialization_options: arrow.ArrowSerializationOptions = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="output_format_serialization_options",
            message=arrow.ArrowSerializationOptions,
        )
        avro_serialization_options: avro.AvroSerializationOptions = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="output_format_serialization_options",
            message=avro.AvroSerializationOptions,
        )
        sample_percentage: float = proto.Field(
            proto.DOUBLE,
            number=5,
            optional=True,
        )
        response_compression_codec: "ReadSession.TableReadOptions.ResponseCompressionCodec" = proto.Field(
            proto.ENUM,
            number=6,
            optional=True,
            enum="ReadSession.TableReadOptions.ResponseCompressionCodec",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    data_format: "DataFormat" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DataFormat",
    )
    avro_schema: avro.AvroSchema = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="schema",
        message=avro.AvroSchema,
    )
    arrow_schema: arrow.ArrowSchema = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="schema",
        message=arrow.ArrowSchema,
    )
    table: str = proto.Field(
        proto.STRING,
        number=6,
    )
    table_modifiers: TableModifiers = proto.Field(
        proto.MESSAGE,
        number=7,
        message=TableModifiers,
    )
    read_options: TableReadOptions = proto.Field(
        proto.MESSAGE,
        number=8,
        message=TableReadOptions,
    )
    streams: MutableSequence["ReadStream"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="ReadStream",
    )
    estimated_total_bytes_scanned: int = proto.Field(
        proto.INT64,
        number=12,
    )
    estimated_total_physical_file_size: int = proto.Field(
        proto.INT64,
        number=15,
    )
    estimated_row_count: int = proto.Field(
        proto.INT64,
        number=14,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=13,
    )


class ReadStream(proto.Message):
    r"""Information about a single stream that gets data out of the storage
    system. Most of the information about ``ReadStream`` instances is
    aggregated, making ``ReadStream`` lightweight.

    Attributes:
        name (str):
            Output only. Name of the stream, in the form
            ``projects/{project_id}/locations/{location}/sessions/{session_id}/streams/{stream_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class WriteStream(proto.Message):
    r"""Information about a single stream that gets data inside the
    storage system.

    Attributes:
        name (str):
            Output only. Name of the stream, in the form
            ``projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}``.
        type_ (google.cloud.bigquery_storage_v1.types.WriteStream.Type):
            Immutable. Type of the stream.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the stream. For the \_default
            stream, this is the creation_time of the table.
        commit_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Commit time of the stream. If a stream is of
            ``COMMITTED`` type, then it will have a commit_time same as
            ``create_time``. If the stream is of ``PENDING`` type, empty
            commit_time means it is not committed.
        table_schema (google.cloud.bigquery_storage_v1.types.TableSchema):
            Output only. The schema of the destination table. It is only
            returned in ``CreateWriteStream`` response. Caller should
            generate data that's compatible with this schema to send in
            initial ``AppendRowsRequest``. The table schema could go out
            of date during the life time of the stream.
        write_mode (google.cloud.bigquery_storage_v1.types.WriteStream.WriteMode):
            Immutable. Mode of the stream.
        location (str):
            Output only. The geographic location where
            the stream's dataset resides. See
            https://cloud.google.com/bigquery/docs/locations
            for supported locations.
    """

    class Type(proto.Enum):
        r"""Type enum of the stream.

        Values:
            TYPE_UNSPECIFIED (0):
                Unknown type.
            COMMITTED (1):
                Data will commit automatically and appear as
                soon as the write is acknowledged.
            PENDING (2):
                Data is invisible until the stream is
                committed.
            BUFFERED (3):
                Data is only visible up to the offset to
                which it was flushed.
        """

        TYPE_UNSPECIFIED = 0
        COMMITTED = 1
        PENDING = 2
        BUFFERED = 3

    class WriteMode(proto.Enum):
        r"""Mode enum of the stream.

        Values:
            WRITE_MODE_UNSPECIFIED (0):
                Unknown type.
            INSERT (1):
                Insert new records into the table.
                It is the default value if customers do not
                specify it.
        """

        WRITE_MODE_UNSPECIFIED = 0
        INSERT = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    commit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    table_schema: gcbs_table.TableSchema = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gcbs_table.TableSchema,
    )
    write_mode: WriteMode = proto.Field(
        proto.ENUM,
        number=7,
        enum=WriteMode,
    )
    location: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
