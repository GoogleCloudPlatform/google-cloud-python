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
from .aggregation_result import (
    AggregationResult,
)
from .bloom_filter import (
    BitSequence,
    BloomFilter,
)
from .common import (
    DocumentMask,
    Precondition,
    RequestOptions,
    TransactionOptions,
)
from .document import (
    ArrayValue,
    Document,
    Function,
    MapValue,
    Pipeline,
    Value,
)
from .explain_stats import (
    ExplainStats,
)
from .firestore import (
    BatchGetDocumentsRequest,
    BatchGetDocumentsResponse,
    BatchWriteRequest,
    BatchWriteResponse,
    BeginTransactionRequest,
    BeginTransactionResponse,
    CommitRequest,
    CommitResponse,
    CreateDocumentRequest,
    DeleteDocumentRequest,
    ExecutePipelineRequest,
    ExecutePipelineResponse,
    GetDocumentRequest,
    ListCollectionIdsRequest,
    ListCollectionIdsResponse,
    ListDocumentsRequest,
    ListDocumentsResponse,
    ListenRequest,
    ListenResponse,
    PartitionQueryRequest,
    PartitionQueryResponse,
    RollbackRequest,
    RunAggregationQueryRequest,
    RunAggregationQueryResponse,
    RunQueryRequest,
    RunQueryResponse,
    Target,
    TargetChange,
    UpdateDocumentRequest,
    WriteRequest,
    WriteResponse,
)
from .pipeline import (
    StructuredPipeline,
)
from .query import (
    Cursor,
    StructuredAggregationQuery,
    StructuredQuery,
)
from .query_profile import (
    ExecutionStats,
    ExplainMetrics,
    ExplainOptions,
    PlanSummary,
)
from .write import (
    DocumentChange,
    DocumentDelete,
    DocumentRemove,
    DocumentTransform,
    ExistenceFilter,
    Write,
    WriteResult,
)

__all__ = (
    "AggregationResult",
    "BitSequence",
    "BloomFilter",
    "DocumentMask",
    "Precondition",
    "RequestOptions",
    "TransactionOptions",
    "ArrayValue",
    "Document",
    "Function",
    "MapValue",
    "Pipeline",
    "Value",
    "ExplainStats",
    "BatchGetDocumentsRequest",
    "BatchGetDocumentsResponse",
    "BatchWriteRequest",
    "BatchWriteResponse",
    "BeginTransactionRequest",
    "BeginTransactionResponse",
    "CommitRequest",
    "CommitResponse",
    "CreateDocumentRequest",
    "DeleteDocumentRequest",
    "ExecutePipelineRequest",
    "ExecutePipelineResponse",
    "GetDocumentRequest",
    "ListCollectionIdsRequest",
    "ListCollectionIdsResponse",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ListenRequest",
    "ListenResponse",
    "PartitionQueryRequest",
    "PartitionQueryResponse",
    "RollbackRequest",
    "RunAggregationQueryRequest",
    "RunAggregationQueryResponse",
    "RunQueryRequest",
    "RunQueryResponse",
    "Target",
    "TargetChange",
    "UpdateDocumentRequest",
    "WriteRequest",
    "WriteResponse",
    "StructuredPipeline",
    "Cursor",
    "StructuredAggregationQuery",
    "StructuredQuery",
    "ExecutionStats",
    "ExplainMetrics",
    "ExplainOptions",
    "PlanSummary",
    "DocumentChange",
    "DocumentDelete",
    "DocumentRemove",
    "DocumentTransform",
    "ExistenceFilter",
    "Write",
    "WriteResult",
)
