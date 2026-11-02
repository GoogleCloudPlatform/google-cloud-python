# Copyright 2024 Google LLC
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

from datetime import datetime, timedelta
from typing import List

import google_crc32c  # type: ignore
from google.protobuf import timestamp_pb2

from google.cloud.bigtable_v2.types.bigtable import (
    ExecuteQueryResponse,
    PrepareQueryResponse,
)
from google.cloud.bigtable_v2.types.data import (
    ColumnMetadata,
    ProtoRows,
    ProtoRowsBatch,
    ResultSetMetadata,
    Value,
)
from google.cloud.bigtable_v2.types.types import Type


def checksum(data: bytearray) -> int:
    return google_crc32c.value(bytes(memoryview(data)))


def split_bytes_into_chunks(bytes_to_split, num_chunks) -> List[bytes]:
    from google.cloud.bigtable.helpers import batched

    assert num_chunks <= len(bytes_to_split)
    bytes_per_part = (len(bytes_to_split) - 1) // num_chunks + 1
    result = list(map(bytes, batched(bytes_to_split, bytes_per_part)))
    assert len(result) == num_chunks
    return result


def column(name: str, type: Type) -> ColumnMetadata:
    c = ColumnMetadata()
    c.name = name
    c.type_ = type
    return c


def metadata(*args: ColumnMetadata) -> ResultSetMetadata:
    metadata = ResultSetMetadata()
    metadata.proto_schema.columns = args
    return metadata


def prepare_response(
    prepared_query: bytes,
    metadata: ResultSetMetadata,
    valid_until=datetime.now() + timedelta(seconds=10),
) -> PrepareQueryResponse:
    res = PrepareQueryResponse()
    res.prepared_query = prepared_query
    res.metadata = metadata
    ts = timestamp_pb2.Timestamp()
    ts.FromDatetime(valid_until)
    res.valid_until = ts
    return res


def batch_response(
    b: bytes, reset=False, token=None, checksum=None
) -> ExecuteQueryResponse:
    res = ExecuteQueryResponse()
    res.results.proto_rows_batch.batch_data = b
    res.results.reset = reset
    res.results.resume_token = token
    if checksum:
        res.results.batch_checksum = checksum
    return res


def execute_query_response(
    *args: Value, reset=False, token=None, checksum=None
) -> ExecuteQueryResponse:
    data = proto_rows_batch(args)
    return batch_response(data, reset, token, checksum=checksum)


def chunked_responses(
    num_chunks: int,
    *args: Value,
    reset=True,
    token=None,
) -> List[ExecuteQueryResponse]:
    """
    Creates one ExecuteQuery response per chunk, with the data in args split between chunks.
    """
    data_bytes = proto_rows_bytes(*args)
    chunks = split_bytes_into_chunks(data_bytes, num_chunks)
    responses = []
    for i, chunk in enumerate(chunks):
        response = ExecuteQueryResponse()
        if i == 0:
            response.results.reset = reset
        if i == len(chunks) - 1:
            response.results.resume_token = token
            response.results.batch_checksum = checksum(data_bytes)
        response.results.proto_rows_batch.batch_data = chunk
        responses.append(response)
    return responses


def proto_rows_bytes(*args: Value) -> bytes:
    rows = ProtoRows()
    rows.values = args
    return ProtoRows.serialize(rows)


def token_only_response(token: bytes) -> ExecuteQueryResponse:
    r = ExecuteQueryResponse()
    r.results.resume_token = token
    return r


def proto_rows_batch(*args: Value) -> ProtoRowsBatch:
    batch = ProtoRowsBatch()
    batch.batch_data = proto_rows_bytes(args)
    return batch


def str_val(s: str) -> Value:
    v = Value()
    v.string_value = s
    return v


def bytes_val(b: bytes) -> Value:
    v = Value()
    v.bytes_value = b
    return v


def int_val(i: int) -> Value:
    v = Value()
    v.int_value = i
    return v


def null_val() -> Value:
    return Value()


def str_type() -> Type:
    t = Type()
    t.string_type = {}
    return t


def bytes_type() -> Type:
    t = Type()
    t.bytes_type = {}
    return t


def int64_type() -> Type:
    t = Type()
    t.int64_type = {}
    return t


def float64_type() -> Type:
    t = Type()
    t.float64_type = {}
    return t


def float32_type() -> Type:
    t = Type()
    t.float32_type = {}
    return t


def bool_type() -> Type:
    t = Type()
    t.bool_type = {}
    return t


def ts_type() -> Type:
    t = Type()
    t.timestamp_type = {}
    return t


def date_type() -> Type:
    t = Type()
    t.date_type = {}
    return t


def proto_type() -> Type:
    t = Type()
    t.proto_type = {}
    return t


def enum_type() -> Type:
    t = Type()
    t.enum_type = {}
    return t


def array_type(elem_type: Type) -> Type:
    t = Type()
    arr_type = Type.Array()
    arr_type.element_type = elem_type
    t.array_type = arr_type
    return t
