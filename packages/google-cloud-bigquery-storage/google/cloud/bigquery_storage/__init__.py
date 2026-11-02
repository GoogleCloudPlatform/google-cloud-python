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
from google.cloud.bigquery_storage import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.bigquery_storage_v1 import BigQueryReadClient
from google.cloud.bigquery_storage_v1 import gapic_types as types
from google.cloud.bigquery_storage_v1.reader import ReadRowsStream
from google.cloud.bigquery_storage_v1.services.big_query_write.async_client import (
    BigQueryWriteAsyncClient,
)
from google.cloud.bigquery_storage_v1.services.big_query_write.client import (
    BigQueryWriteClient,
)
from google.cloud.bigquery_storage_v1.types.arrow import (
    ArrowRecordBatch,
    ArrowSchema,
    ArrowSerializationOptions,
)
from google.cloud.bigquery_storage_v1.types.avro import (
    AvroRows,
    AvroSchema,
    AvroSerializationOptions,
)
from google.cloud.bigquery_storage_v1.types.protobuf import ProtoRows, ProtoSchema
from google.cloud.bigquery_storage_v1.types.storage import (
    AppendRowsRequest,
    AppendRowsResponse,
    BatchCommitWriteStreamsRequest,
    BatchCommitWriteStreamsResponse,
    ClientStats,
    CreateReadSessionRequest,
    CreateWriteStreamRequest,
    FinalizeWriteStreamRequest,
    FinalizeWriteStreamResponse,
    FlushRowsRequest,
    FlushRowsResponse,
    GetWriteStreamRequest,
    ReadRowsRequest,
    ReadRowsResponse,
    RowError,
    SplitReadStreamRequest,
    SplitReadStreamResponse,
    StorageError,
    StreamStats,
    ThrottleState,
)
from google.cloud.bigquery_storage_v1.types.stream import (
    DataFormat,
    ReadSession,
    ReadStream,
    WriteStream,
    WriteStreamView,
)
from google.cloud.bigquery_storage_v1.types.table import TableFieldSchema, TableSchema
from google.cloud.bigquery_storage_v1.writer import AppendRowsStream

__all__ = (
    "BigQueryReadClient",
    "BigQueryWriteClient",
    "BigQueryWriteAsyncClient",
    "__version__",
    "types",
    "ArrowRecordBatch",
    "ArrowSchema",
    "ArrowSerializationOptions",
    "AvroRows",
    "AvroSchema",
    "AvroSerializationOptions",
    "ProtoRows",
    "ProtoSchema",
    "AppendRowsRequest",
    "AppendRowsResponse",
    "BatchCommitWriteStreamsRequest",
    "BatchCommitWriteStreamsResponse",
    "ClientStats",
    "CreateReadSessionRequest",
    "CreateWriteStreamRequest",
    "FinalizeWriteStreamRequest",
    "FinalizeWriteStreamResponse",
    "FlushRowsRequest",
    "FlushRowsResponse",
    "GetWriteStreamRequest",
    "ReadRowsRequest",
    "ReadRowsResponse",
    "RowError",
    "SplitReadStreamRequest",
    "SplitReadStreamResponse",
    "StorageError",
    "StreamStats",
    "ThrottleState",
    "AppendRowsStream",
    "ReadRowsStream",
    "ReadSession",
    "ReadStream",
    "WriteStream",
    "DataFormat",
    "WriteStreamView",
    "TableFieldSchema",
    "TableSchema",
)
