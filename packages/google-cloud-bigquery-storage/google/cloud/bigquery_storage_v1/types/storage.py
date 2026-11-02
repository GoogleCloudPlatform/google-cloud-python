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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.bigquery_storage_v1.types import arrow, avro, protobuf, stream, table

__protobuf__ = proto.module(
    package="google.cloud.bigquery.storage.v1",
    manifest={
        "CreateReadSessionRequest",
        "ReadRowsRequest",
        "ThrottleState",
        "StreamStats",
        "ReadRowsResponse",
        "SplitReadStreamRequest",
        "SplitReadStreamResponse",
        "CreateWriteStreamRequest",
        "AppendRowsRequest",
        "AppendRowsResponse",
        "GetWriteStreamRequest",
        "BatchCommitWriteStreamsRequest",
        "BatchCommitWriteStreamsResponse",
        "FinalizeWriteStreamRequest",
        "FinalizeWriteStreamResponse",
        "FlushRowsRequest",
        "FlushRowsResponse",
        "StorageError",
        "RowError",
        "ClientStats",
    },
)


class CreateReadSessionRequest(proto.Message):
    r"""Request message for ``CreateReadSession``.

    Attributes:
        parent (str):
            Required. The request project that owns the session, in the
            form of ``projects/{project_id}``.
        read_session (google.cloud.bigquery_storage_v1.types.ReadSession):
            Required. Session to be created.
        max_stream_count (int):
            Max initial number of streams. If unset or zero, the server
            will provide a value of streams so as to produce reasonable
            throughput. Must be non-negative. The number of streams may
            be lower than the requested number, depending on the amount
            parallelism that is reasonable for the table. There is a
            default system max limit of 1,000.

            This must be greater than or equal to
            preferred_min_stream_count. Typically, clients should either
            leave this unset to let the system to determine an upper
            bound OR set this a size for the maximum "units of work" it
            can gracefully handle.
        preferred_min_stream_count (int):
            The minimum preferred stream count. This
            parameter can be used to inform the service that
            there is a desired lower bound on the number of
            streams. This is typically a target parallelism
            of the client (e.g. a Spark cluster with
            N-workers would set this to a low multiple of N
            to ensure good cluster utilization).

            The system will make a best effort to provide at
            least this number of streams, but in some cases
            might provide less.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_session: stream.ReadSession = proto.Field(
        proto.MESSAGE,
        number=2,
        message=stream.ReadSession,
    )
    max_stream_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    preferred_min_stream_count: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ReadRowsRequest(proto.Message):
    r"""Request message for ``ReadRows``.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        read_stream (str):
            Required. Stream to read rows from.
        offset (int):
            The offset requested must be less than the
            last row read from Read. Requesting a larger
            offset is undefined. If not specified, start
            reading from offset zero.
        arrow_serialization_options (google.cloud.bigquery_storage_v1.types.ArrowSerializationOptions):
            Optional. Options specific to the Apache
            Arrow output format.
            This feature is not yet available.

            This field is a member of `oneof`_ ``output_format_serialization_options``.
    """

    read_stream: str = proto.Field(
        proto.STRING,
        number=1,
    )
    offset: int = proto.Field(
        proto.INT64,
        number=2,
    )
    arrow_serialization_options: arrow.ArrowSerializationOptions = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="output_format_serialization_options",
        message=arrow.ArrowSerializationOptions,
    )


class ThrottleState(proto.Message):
    r"""Information on if the current connection is being throttled.

    Attributes:
        throttle_percent (int):
            How much this connection is being throttled.
            Zero means no throttling, 100 means fully
            throttled.
    """

    throttle_percent: int = proto.Field(
        proto.INT32,
        number=1,
    )


class StreamStats(proto.Message):
    r"""Estimated stream statistics for a given read Stream.

    Attributes:
        progress (google.cloud.bigquery_storage_v1.types.StreamStats.Progress):
            Represents the progress of the current
            stream.
    """

    class Progress(proto.Message):
        r"""

        Attributes:
            at_response_start (float):
                The fraction of rows assigned to the stream that have been
                processed by the server so far, not including the rows in
                the current response message.

                This value, along with ``at_response_end``, can be used to
                interpolate the progress made as the rows in the message are
                being processed using the following formula:
                ``at_response_start + (at_response_end - at_response_start) * rows_processed_from_response / rows_in_response``.

                Note that if a filter is provided, the ``at_response_end``
                value of the previous response may not necessarily be equal
                to the ``at_response_start`` value of the current response.
            at_response_end (float):
                Similar to ``at_response_start``, except that this value
                includes the rows in the current response.
        """

        at_response_start: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        at_response_end: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )

    progress: Progress = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Progress,
    )


class ReadRowsResponse(proto.Message):
    r"""Response from calling ``ReadRows`` may include row data, progress
    and throttling information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        avro_rows (google.cloud.bigquery_storage_v1.types.AvroRows):
            Serialized row data in AVRO format.

            This field is a member of `oneof`_ ``rows``.
        arrow_record_batch (google.cloud.bigquery_storage_v1.types.ArrowRecordBatch):
            Serialized row data in Arrow RecordBatch
            format.

            This field is a member of `oneof`_ ``rows``.
        row_count (int):
            Number of serialized rows in the rows block.
        stats (google.cloud.bigquery_storage_v1.types.StreamStats):
            Statistics for the stream.
        throttle_state (google.cloud.bigquery_storage_v1.types.ThrottleState):
            Throttling state. If unset, the latest
            response still describes the current throttling
            status.
        avro_schema (google.cloud.bigquery_storage_v1.types.AvroSchema):
            Output only. Avro schema.

            This field is a member of `oneof`_ ``schema``.
        arrow_schema (google.cloud.bigquery_storage_v1.types.ArrowSchema):
            Output only. Arrow schema.

            This field is a member of `oneof`_ ``schema``.
        uncompressed_byte_size (int):
            Optional. If the row data in this ReadRowsResponse is
            compressed, then uncompressed byte size is the original size
            of the uncompressed row data. If it is set to a value
            greater than 0, then decompress into a buffer of size
            uncompressed_byte_size using the compression codec that was
            requested during session creation time and which is
            specified in TableReadOptions.response_compression_codec in
            ReadSession. This value is not set if no
            response_compression_codec was not requested and it is -1 if
            the requested compression would not have reduced the size of
            this ReadRowsResponse's row data. This attempts to match
            Apache Arrow's behavior described here
            https://github.com/apache/arrow/issues/15102 where the
            uncompressed length may be set to -1 to indicate that the
            data that follows is not compressed, which can be useful for
            cases where compression does not yield appreciable savings.
            When uncompressed_byte_size is not greater than 0, the
            client should skip decompression.

            This field is a member of `oneof`_ ``_uncompressed_byte_size``.
        total_estimated_row_count (int):
            Output only. The total estimated number of
            rows in the query results. Only populated when
            reading data from a BigQuery job.

            This feature is not yet available.

            This field is a member of `oneof`_ ``_total_estimated_row_count``.
    """

    avro_rows: avro.AvroRows = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="rows",
        message=avro.AvroRows,
    )
    arrow_record_batch: arrow.ArrowRecordBatch = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="rows",
        message=arrow.ArrowRecordBatch,
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=6,
    )
    stats: "StreamStats" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StreamStats",
    )
    throttle_state: "ThrottleState" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ThrottleState",
    )
    avro_schema: avro.AvroSchema = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="schema",
        message=avro.AvroSchema,
    )
    arrow_schema: arrow.ArrowSchema = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="schema",
        message=arrow.ArrowSchema,
    )
    uncompressed_byte_size: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    total_estimated_row_count: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )


class SplitReadStreamRequest(proto.Message):
    r"""Request message for ``SplitReadStream``.

    Attributes:
        name (str):
            Required. Name of the stream to split.
        fraction (float):
            A value in the range (0.0, 1.0) that
            specifies the fractional point at which the
            original stream should be split. The actual
            split point is evaluated on pre-filtered rows,
            so if a filter is provided, then there is no
            guarantee that the division of the rows between
            the new child streams will be proportional to
            this fractional value. Additionally, because the
            server-side unit for assigning data is
            collections of rows, this fraction will always
            map to a data storage boundary on the server
            side.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fraction: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class SplitReadStreamResponse(proto.Message):
    r"""Response message for ``SplitReadStream``.

    Attributes:
        primary_stream (google.cloud.bigquery_storage_v1.types.ReadStream):
            Primary stream, which contains the beginning portion of
            \|original_stream\|. An empty value indicates that the
            original stream can no longer be split.
        remainder_stream (google.cloud.bigquery_storage_v1.types.ReadStream):
            Remainder stream, which contains the tail of
            \|original_stream\|. An empty value indicates that the
            original stream can no longer be split.
    """

    primary_stream: stream.ReadStream = proto.Field(
        proto.MESSAGE,
        number=1,
        message=stream.ReadStream,
    )
    remainder_stream: stream.ReadStream = proto.Field(
        proto.MESSAGE,
        number=2,
        message=stream.ReadStream,
    )


class CreateWriteStreamRequest(proto.Message):
    r"""Request message for ``CreateWriteStream``.

    Attributes:
        parent (str):
            Required. Reference to the table to which the stream
            belongs, in the format of
            ``projects/{project}/datasets/{dataset}/tables/{table}``.
        write_stream (google.cloud.bigquery_storage_v1.types.WriteStream):
            Required. Stream to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    write_stream: stream.WriteStream = proto.Field(
        proto.MESSAGE,
        number=2,
        message=stream.WriteStream,
    )


class AppendRowsRequest(proto.Message):
    r"""Request message for ``AppendRows``.

    Because AppendRows is a bidirectional streaming RPC, certain parts
    of the AppendRowsRequest need only be specified for the first
    request before switching table destinations. You can also switch
    table destinations within the same connection for the default
    stream.

    The size of a single AppendRowsRequest must be less than 20 MB in
    size. Requests larger than this return an error, typically
    ``INVALID_ARGUMENT``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        write_stream (str):
            Required. The write_stream identifies the append operation.
            It must be provided in the following scenarios:

            - In the first request to an AppendRows connection.

            - In all subsequent requests to an AppendRows connection, if
              you use the same connection to write to multiple tables or
              change the input schema for default streams.

            For explicitly created write streams, the format is:

            - ``projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}``

            For the special default stream, the format is:

            - ``projects/{project}/datasets/{dataset}/tables/{table}/streams/_default``.

            An example of a possible sequence of requests with
            write_stream fields within a single connection:

            - r1: {write_stream: stream_name_1}

            - r2: {write_stream: /*omit*/}

            - r3: {write_stream: /*omit*/}

            - r4: {write_stream: stream_name_2}

            - r5: {write_stream: stream_name_2}

            The destination changed in request_4, so the write_stream
            field must be populated in all subsequent requests in this
            stream.
        offset (google.protobuf.wrappers_pb2.Int64Value):
            If present, the write is only performed if the next append
            offset is same as the provided value. If not present, the
            write is performed at the current end of stream. Specifying
            a value for this field is not allowed when calling
            AppendRows for the '\_default' stream.
        proto_rows (google.cloud.bigquery_storage_v1.types.AppendRowsRequest.ProtoData):
            Rows in proto format.

            This field is a member of `oneof`_ ``rows``.
        arrow_rows (google.cloud.bigquery_storage_v1.types.AppendRowsRequest.ArrowData):
            Rows in arrow format.

            This field is a member of `oneof`_ ``rows``.
        trace_id (str):
            Id set by client to annotate its identity.
            Only initial request setting is respected.
        missing_value_interpretations (MutableMapping[str, google.cloud.bigquery_storage_v1.types.AppendRowsRequest.MissingValueInterpretation]):
            A map to indicate how to interpret missing value for some
            fields. Missing values are fields present in user schema but
            missing in rows. The key is the field name. The value is the
            interpretation of missing values for the field.

            For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE}
            means all missing values in field foo are interpreted as
            NULL, all missing values in field bar are interpreted as the
            default value of field bar in table schema.

            If a field is not in this map and has missing values, the
            missing values in this field are interpreted as NULL.

            This field only applies to the current request, it won't
            affect other requests on the connection.

            Currently, field name can only be top-level column name,
            can't be a struct field path like 'foo.bar'.
        default_missing_value_interpretation (google.cloud.bigquery_storage_v1.types.AppendRowsRequest.MissingValueInterpretation):
            Optional. Default missing value interpretation for all
            columns in the table. When a value is specified on an
            ``AppendRowsRequest``, it is applied to all requests from
            that point forward, until a subsequent ``AppendRowsRequest``
            sets it to a different value.
            ``missing_value_interpretation`` can override
            ``default_missing_value_interpretation``. For example, if
            you want to write ``NULL`` instead of using default values
            for some columns, you can set
            ``default_missing_value_interpretation`` to
            ``DEFAULT_VALUE`` and at the same time, set
            ``missing_value_interpretations`` to ``NULL_VALUE`` on those
            columns.
        client_stats (google.cloud.bigquery_storage_v1.types.ClientStats):
            Optional. Stats and telemetry data gathered
            on the client side.
    """

    class MissingValueInterpretation(proto.Enum):
        r"""An enum to indicate how to interpret missing values of fields
        that are present in user schema but missing in rows. A missing
        value can represent a NULL or a column default value defined in
        BigQuery table schema.

        Values:
            MISSING_VALUE_INTERPRETATION_UNSPECIFIED (0):
                Invalid missing value interpretation.
                Requests with this value will be rejected.
            NULL_VALUE (1):
                Missing value is interpreted as NULL.
            DEFAULT_VALUE (2):
                Missing value is interpreted as column
                default value if declared in the table schema,
                NULL otherwise.
        """

        MISSING_VALUE_INTERPRETATION_UNSPECIFIED = 0
        NULL_VALUE = 1
        DEFAULT_VALUE = 2

    class ArrowData(proto.Message):
        r"""Arrow schema and data.

        Attributes:
            writer_schema (google.cloud.bigquery_storage_v1.types.ArrowSchema):
                Optional. Arrow Schema used to serialize the
                data.
            rows (google.cloud.bigquery_storage_v1.types.ArrowRecordBatch):
                Required. Serialized row data in Arrow
                format.
        """

        writer_schema: arrow.ArrowSchema = proto.Field(
            proto.MESSAGE,
            number=1,
            message=arrow.ArrowSchema,
        )
        rows: arrow.ArrowRecordBatch = proto.Field(
            proto.MESSAGE,
            number=2,
            message=arrow.ArrowRecordBatch,
        )

    class ProtoData(proto.Message):
        r"""ProtoData contains the data rows and schema when constructing
        append requests.

        Attributes:
            writer_schema (google.cloud.bigquery_storage_v1.types.ProtoSchema):
                Optional. The protocol buffer schema used to serialize the
                data. Provide this value whenever:

                - You send the first request of an RPC connection.

                - You change the input schema.

                - You specify a new destination table.
            rows (google.cloud.bigquery_storage_v1.types.ProtoRows):
                Required. Serialized row data in protobuf
                message format. Currently, the backend expects
                the serialized rows to adhere to proto2
                semantics when appending rows, particularly with
                respect to how default values are encoded.
        """

        writer_schema: protobuf.ProtoSchema = proto.Field(
            proto.MESSAGE,
            number=1,
            message=protobuf.ProtoSchema,
        )
        rows: protobuf.ProtoRows = proto.Field(
            proto.MESSAGE,
            number=2,
            message=protobuf.ProtoRows,
        )

    write_stream: str = proto.Field(
        proto.STRING,
        number=1,
    )
    offset: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int64Value,
    )
    proto_rows: ProtoData = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="rows",
        message=ProtoData,
    )
    arrow_rows: ArrowData = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="rows",
        message=ArrowData,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    missing_value_interpretations: MutableMapping[str, MissingValueInterpretation] = (
        proto.MapField(
            proto.STRING,
            proto.ENUM,
            number=7,
            enum=MissingValueInterpretation,
        )
    )
    default_missing_value_interpretation: MissingValueInterpretation = proto.Field(
        proto.ENUM,
        number=8,
        enum=MissingValueInterpretation,
    )
    client_stats: "ClientStats" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ClientStats",
    )


class AppendRowsResponse(proto.Message):
    r"""Response message for ``AppendRows``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        append_result (google.cloud.bigquery_storage_v1.types.AppendRowsResponse.AppendResult):
            Result if the append is successful.

            This field is a member of `oneof`_ ``response``.
        error (google.rpc.status_pb2.Status):
            Error returned when problems were encountered. If present,
            it indicates rows were not accepted into the system. Users
            can retry or continue with other append requests within the
            same connection.

            Additional information about error signalling:

            ALREADY_EXISTS: Happens when an append specified an offset,
            and the backend already has received data at this offset.
            Typically encountered in retry scenarios, and can be
            ignored.

            OUT_OF_RANGE: Returned when the specified offset in the
            stream is beyond the current end of the stream.

            INVALID_ARGUMENT: Indicates a malformed request or data.

            ABORTED: Request processing is aborted because of prior
            failures. The request can be retried if previous failure is
            addressed.

            INTERNAL: Indicates server side error(s) that can be
            retried.

            This field is a member of `oneof`_ ``response``.
        updated_schema (google.cloud.bigquery_storage_v1.types.TableSchema):
            If backend detects a schema update, pass it
            to user so that user can use it to input new
            type of message. It will be empty when no schema
            updates have occurred.
        row_errors (MutableSequence[google.cloud.bigquery_storage_v1.types.RowError]):
            If a request failed due to corrupted rows, no
            rows in the batch will be appended. The API will
            return row level error info, so that the caller
            can remove the bad rows and retry the request.
        write_stream (str):
            The target of the append operation. Matches the write_stream
            in the corresponding request.
    """

    class AppendResult(proto.Message):
        r"""AppendResult is returned for successful append requests.

        Attributes:
            offset (google.protobuf.wrappers_pb2.Int64Value):
                The row offset at which the last append
                occurred. The offset will not be set if
                appending using default streams.
        """

        offset: wrappers_pb2.Int64Value = proto.Field(
            proto.MESSAGE,
            number=1,
            message=wrappers_pb2.Int64Value,
        )

    append_result: AppendResult = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="response",
        message=AppendResult,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="response",
        message=status_pb2.Status,
    )
    updated_schema: table.TableSchema = proto.Field(
        proto.MESSAGE,
        number=3,
        message=table.TableSchema,
    )
    row_errors: MutableSequence["RowError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="RowError",
    )
    write_stream: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetWriteStreamRequest(proto.Message):
    r"""Request message for ``GetWriteStreamRequest``.

    Attributes:
        name (str):
            Required. Name of the stream to get, in the form of
            ``projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}``.
        view (google.cloud.bigquery_storage_v1.types.WriteStreamView):
            Indicates whether to get full or partial view
            of the WriteStream. If not set, view returned
            will be basic.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: stream.WriteStreamView = proto.Field(
        proto.ENUM,
        number=3,
        enum=stream.WriteStreamView,
    )


class BatchCommitWriteStreamsRequest(proto.Message):
    r"""Request message for ``BatchCommitWriteStreams``.

    Attributes:
        parent (str):
            Required. Parent table that all the streams should belong
            to, in the form of
            ``projects/{project}/datasets/{dataset}/tables/{table}``.
        write_streams (MutableSequence[str]):
            Required. The group of streams that will be
            committed atomically.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    write_streams: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchCommitWriteStreamsResponse(proto.Message):
    r"""Response message for ``BatchCommitWriteStreams``.

    Attributes:
        commit_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which streams were committed in microseconds
            granularity. This field will only exist when there are no
            stream errors. **Note** if this field is not set, it means
            the commit was not successful.
        stream_errors (MutableSequence[google.cloud.bigquery_storage_v1.types.StorageError]):
            Stream level error if commit failed. Only
            streams with error will be in the list.
            If empty, there is no error and all streams are
            committed successfully. If non empty, certain
            streams have errors and ZERO stream is committed
            due to atomicity guarantee.
    """

    commit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    stream_errors: MutableSequence["StorageError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="StorageError",
    )


class FinalizeWriteStreamRequest(proto.Message):
    r"""Request message for invoking ``FinalizeWriteStream``.

    Attributes:
        name (str):
            Required. Name of the stream to finalize, in the form of
            ``projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FinalizeWriteStreamResponse(proto.Message):
    r"""Response message for ``FinalizeWriteStream``.

    Attributes:
        row_count (int):
            Number of rows in the finalized stream.
    """

    row_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class FlushRowsRequest(proto.Message):
    r"""Request message for ``FlushRows``.

    Attributes:
        write_stream (str):
            Required. The stream that is the target of
            the flush operation.
        offset (google.protobuf.wrappers_pb2.Int64Value):
            Ending offset of the flush operation. Rows
            before this offset(including this offset) will
            be flushed.
    """

    write_stream: str = proto.Field(
        proto.STRING,
        number=1,
    )
    offset: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int64Value,
    )


class FlushRowsResponse(proto.Message):
    r"""Respond message for ``FlushRows``.

    Attributes:
        offset (int):
            The rows before this offset (including this
            offset) are flushed.
    """

    offset: int = proto.Field(
        proto.INT64,
        number=1,
    )


class StorageError(proto.Message):
    r"""Structured custom BigQuery Storage error message. The error
    can be attached as error details in the returned rpc Status. In
    particular, the use of error codes allows more structured error
    handling, and reduces the need to evaluate unstructured error
    text strings.

    Attributes:
        code (google.cloud.bigquery_storage_v1.types.StorageError.StorageErrorCode):
            BigQuery Storage specific error code.
        entity (str):
            Name of the failed entity.
        error_message (str):
            Message that describes the error.
    """

    class StorageErrorCode(proto.Enum):
        r"""Error code for ``StorageError``.

        Values:
            STORAGE_ERROR_CODE_UNSPECIFIED (0):
                Default error.
            TABLE_NOT_FOUND (1):
                Table is not found in the system.
            STREAM_ALREADY_COMMITTED (2):
                Stream is already committed.
            STREAM_NOT_FOUND (3):
                Stream is not found.
            INVALID_STREAM_TYPE (4):
                Invalid Stream type.
                For example, you try to commit a stream that is
                not pending.
            INVALID_STREAM_STATE (5):
                Invalid Stream state.
                For example, you try to commit a stream that is
                not finalized or is garbaged.
            STREAM_FINALIZED (6):
                Stream is finalized.
            SCHEMA_MISMATCH_EXTRA_FIELDS (7):
                There is a schema mismatch and it is caused
                by user schema has extra field than bigquery
                schema.
            OFFSET_ALREADY_EXISTS (8):
                Offset already exists.
            OFFSET_OUT_OF_RANGE (9):
                Offset out of range.
            CMEK_NOT_PROVIDED (10):
                Customer-managed encryption key (CMEK) not
                provided for CMEK-enabled data.
            INVALID_CMEK_PROVIDED (11):
                Customer-managed encryption key (CMEK) was
                incorrectly provided.
            CMEK_ENCRYPTION_ERROR (12):
                There is an encryption error while using
                customer-managed encryption key.
            KMS_SERVICE_ERROR (13):
                Key Management Service (KMS) service returned
                an error, which can be retried.
            KMS_PERMISSION_DENIED (14):
                Permission denied while using
                customer-managed encryption key.
        """

        STORAGE_ERROR_CODE_UNSPECIFIED = 0
        TABLE_NOT_FOUND = 1
        STREAM_ALREADY_COMMITTED = 2
        STREAM_NOT_FOUND = 3
        INVALID_STREAM_TYPE = 4
        INVALID_STREAM_STATE = 5
        STREAM_FINALIZED = 6
        SCHEMA_MISMATCH_EXTRA_FIELDS = 7
        OFFSET_ALREADY_EXISTS = 8
        OFFSET_OUT_OF_RANGE = 9
        CMEK_NOT_PROVIDED = 10
        INVALID_CMEK_PROVIDED = 11
        CMEK_ENCRYPTION_ERROR = 12
        KMS_SERVICE_ERROR = 13
        KMS_PERMISSION_DENIED = 14

    code: StorageErrorCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=StorageErrorCode,
    )
    entity: str = proto.Field(
        proto.STRING,
        number=2,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RowError(proto.Message):
    r"""The message that presents row level error info in a request.

    Attributes:
        index (int):
            Index of the malformed row in the request.
        code (google.cloud.bigquery_storage_v1.types.RowError.RowErrorCode):
            Structured error reason for a row error.
        message (str):
            Description of the issue encountered when
            processing the row.
    """

    class RowErrorCode(proto.Enum):
        r"""Error code for ``RowError``.

        Values:
            ROW_ERROR_CODE_UNSPECIFIED (0):
                Default error.
            FIELDS_ERROR (1):
                One or more fields in the row has errors.
        """

        ROW_ERROR_CODE_UNSPECIFIED = 0
        FIELDS_ERROR = 1

    index: int = proto.Field(
        proto.INT64,
        number=1,
    )
    code: RowErrorCode = proto.Field(
        proto.ENUM,
        number=2,
        enum=RowErrorCode,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ClientStats(proto.Message):
    r"""Stats and telemetry data gathered on the client side about
    requests being sent to the BigQuery Storage service, for
    internal use only.

    Attributes:
        request_stats (google.cloud.bigquery_storage_v1.types.ClientStats.RequestStats):
            Optional. Per-request stats.
        window_stats (google.cloud.bigquery_storage_v1.types.ClientStats.WindowStats):
            Optional. Windowed stats.
    """

    class RequestStats(proto.Message):
        r"""Stats and telemetry data gathered on the client side about a
        single request.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            send_time_millis (int):
                Optional. Timestamp indicating when the
                request was sent over the network, expressed in
                epoch milliseconds.

                This field is a member of `oneof`_ ``_send_time_millis``.
            queued_requests_count (int):
                Optional. Number of pending requests at the
                moment this request was sent. This includes
                requests waiting to be sent, and those that are
                inflight.

                This field is a member of `oneof`_ ``_queued_requests_count``.
        """

        send_time_millis: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        queued_requests_count: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )

    class WindowStats(proto.Message):
        r"""Aggregate connection metrics over a window interval.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            max_response_latency_millis (int):
                Optional. The maximum response latency
                observed in the window, expressed in
                milliseconds.

                This field is a member of `oneof`_ ``_max_response_latency_millis``.
            avg_response_latency_millis (int):
                Optional. The average response latency
                observed in the window, expressed in
                milliseconds.

                This field is a member of `oneof`_ ``_avg_response_latency_millis``.
            longest_wait_no_response_millis (int):
                Optional. The longest time spent waiting without receiving a
                response in the window. This could exceed
                max_response_latency_millis because the latter is evaluated
                only when a response is received. Expressed in milliseconds.

                This field is a member of `oneof`_ ``_longest_wait_no_response_millis``.
            requests_sent_count (int):
                Optional. How many requests were sent in the
                window.

                This field is a member of `oneof`_ ``_requests_sent_count``.
            responses_received_count (int):
                Optional. How many responses were received in
                the window.

                This field is a member of `oneof`_ ``_responses_received_count``.
            bytes_sent_count (int):
                Optional. How many bytes were sent in the
                window.

                This field is a member of `oneof`_ ``_bytes_sent_count``.
            window_start_time_epoch_millis (int):
                Optional. Start time of the window interval
                for which these stats are aggregated, expressed
                in epoch milliseconds.

                This field is a member of `oneof`_ ``_window_start_time_epoch_millis``.
            window_millis (int):
                Optional. Duration of the window interval for
                which these stats are aggregated, expressed in
                milliseconds.

                This field is a member of `oneof`_ ``_window_millis``.
        """

        max_response_latency_millis: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        avg_response_latency_millis: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        longest_wait_no_response_millis: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )
        requests_sent_count: int = proto.Field(
            proto.INT64,
            number=4,
            optional=True,
        )
        responses_received_count: int = proto.Field(
            proto.INT64,
            number=5,
            optional=True,
        )
        bytes_sent_count: int = proto.Field(
            proto.INT64,
            number=6,
            optional=True,
        )
        window_start_time_epoch_millis: int = proto.Field(
            proto.INT64,
            number=7,
            optional=True,
        )
        window_millis: int = proto.Field(
            proto.INT64,
            number=8,
            optional=True,
        )

    request_stats: RequestStats = proto.Field(
        proto.MESSAGE,
        number=1,
        message=RequestStats,
    )
    window_stats: WindowStats = proto.Field(
        proto.MESSAGE,
        number=2,
        message=WindowStats,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
