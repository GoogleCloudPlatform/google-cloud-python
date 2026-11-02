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
from __future__ import absolute_import

from google.cloud.spanner_v1 import gapic_version as package_version

__version__: str = package_version.__version__

from google.cloud.spanner_v1 import param_types
from google.cloud.spanner_v1._async.client import Client as AsyncClient
from google.cloud.spanner_v1._async.pool import (
    AbstractSessionPool as AsyncAbstractSessionPool,
)
from google.cloud.spanner_v1._async.pool import BurstyPool as AsyncBurstyPool
from google.cloud.spanner_v1._async.pool import FixedSizePool as AsyncFixedSizePool
from google.cloud.spanner_v1._async.pool import PingingPool as AsyncPingingPool
from google.cloud.spanner_v1._async.pool import (
    TransactionPingingPool as AsyncTransactionPingingPool,
)
from google.cloud.spanner_v1.client import Client
from google.cloud.spanner_v1.keyset import KeyRange, KeySet
from google.cloud.spanner_v1.pool import (
    AbstractSessionPool,
    BurstyPool,
    FixedSizePool,
    PingingPool,
    TransactionPingingPool,
)

from .data_types import Interval, JsonObject
from .exceptions import wrap_with_request_id
from .services.spanner import SpannerAsyncClient, SpannerClient
from .transaction import BatchTransactionId, DefaultTransactionOptions
from .types import RequestOptions
from .types.commit_response import CommitResponse
from .types.keys import KeyRange as KeyRangePB
from .types.keys import KeySet as KeySetPB
from .types.mutation import Mutation
from .types.query_plan import PlanNode, QueryPlan
from .types.result_set import (
    PartialResultSet,
    ResultSet,
    ResultSetMetadata,
    ResultSetStats,
)
from .types.spanner import (
    BatchCreateSessionsRequest,
    BatchCreateSessionsResponse,
    BatchWriteRequest,
    BatchWriteResponse,
    BeginTransactionRequest,
    CommitRequest,
    CreateSessionRequest,
    DeleteSessionRequest,
    DirectedReadOptions,
    ExecuteBatchDmlRequest,
    ExecuteBatchDmlResponse,
    ExecuteSqlRequest,
    GetSessionRequest,
    ListSessionsRequest,
    ListSessionsResponse,
    Partition,
    PartitionOptions,
    PartitionQueryRequest,
    PartitionReadRequest,
    PartitionResponse,
    ReadRequest,
    RollbackRequest,
    Session,
)
from .types.transaction import Transaction, TransactionOptions, TransactionSelector
from .types.type import StructType, Type, TypeAnnotationCode, TypeCode

COMMIT_TIMESTAMP = "spanner.commit_timestamp()"
"""Placeholder be used to store commit timestamp of a transaction in a column.
This value can only be used for timestamp columns that have set the option
``(allow_commit_timestamp=true)`` in the schema.
"""

__all__ = (
    # google.cloud.spanner_v1
    "__version__",
    "param_types",
    # google.cloud.spanner_v1.exceptions
    "wrap_with_request_id",
    # google.cloud.spanner_v1.client
    "Client",
    "AsyncClient",
    # google.cloud.spanner_v1.keyset
    "KeyRange",
    "KeySet",
    # google.cloud.spanner_v1.pool
    "AbstractSessionPool",
    "BurstyPool",
    "FixedSizePool",
    "PingingPool",
    "TransactionPingingPool",
    "AsyncAbstractSessionPool",
    "AsyncBurstyPool",
    "AsyncFixedSizePool",
    "AsyncPingingPool",
    "AsyncTransactionPingingPool",
    # local
    "COMMIT_TIMESTAMP",
    # google.cloud.spanner_v1.types
    "BatchCreateSessionsRequest",
    "BatchCreateSessionsResponse",
    "BatchWriteRequest",
    "BatchWriteResponse",
    "BeginTransactionRequest",
    "CommitRequest",
    "CommitResponse",
    "CreateSessionRequest",
    "DeleteSessionRequest",
    "DirectedReadOptions",
    "ExecuteBatchDmlRequest",
    "ExecuteBatchDmlResponse",
    "ExecuteSqlRequest",
    "GetSessionRequest",
    "KeyRangePB",
    "KeySetPB",
    "ListSessionsRequest",
    "ListSessionsResponse",
    "Mutation",
    "PartialResultSet",
    "Partition",
    "PartitionOptions",
    "PartitionQueryRequest",
    "PartitionReadRequest",
    "PartitionResponse",
    "PlanNode",
    "QueryPlan",
    "ReadRequest",
    "RequestOptions",
    "ResultSet",
    "ResultSetMetadata",
    "ResultSetStats",
    "RollbackRequest",
    "Session",
    "StructType",
    "Transaction",
    "TransactionOptions",
    "TransactionSelector",
    "Type",
    "TypeAnnotationCode",
    "TypeCode",
    # Custom spanner related data types
    "JsonObject",
    "Interval",
    # google.cloud.spanner_v1.services
    "SpannerClient",
    "SpannerAsyncClient",
    "BatchTransactionId",
    "DefaultTransactionOptions",
)
