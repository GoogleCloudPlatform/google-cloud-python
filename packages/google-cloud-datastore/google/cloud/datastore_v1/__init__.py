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
import google.api_core as api_core

from google.cloud.datastore_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.datastore_v1.services.datastore",
    "google.cloud.datastore_v1.types.aggregation_result",
    "google.cloud.datastore_v1.types.datastore",
    "google.cloud.datastore_v1.types.entity",
    "google.cloud.datastore_v1.types.query",
    "google.cloud.datastore_v1.types.query_profile",
}


from .services.datastore import DatastoreAsyncClient, DatastoreClient
from .types.aggregation_result import AggregationResult, AggregationResultBatch
from .types.datastore import (
    AllocateIdsRequest,
    AllocateIdsResponse,
    BeginTransactionRequest,
    BeginTransactionResponse,
    CommitRequest,
    CommitResponse,
    LookupRequest,
    LookupResponse,
    Mutation,
    MutationResult,
    PropertyMask,
    PropertyTransform,
    ReadOptions,
    RequestOptions,
    ReserveIdsRequest,
    ReserveIdsResponse,
    RollbackRequest,
    RollbackResponse,
    RunAggregationQueryRequest,
    RunAggregationQueryResponse,
    RunQueryRequest,
    RunQueryResponse,
    TransactionOptions,
)
from .types.entity import ArrayValue, Entity, Key, PartitionId, Value
from .types.query import (
    AggregationQuery,
    CompositeFilter,
    EntityResult,
    Filter,
    FindNearest,
    GqlQuery,
    GqlQueryParameter,
    KindExpression,
    Projection,
    PropertyFilter,
    PropertyOrder,
    PropertyReference,
    Query,
    QueryResultBatch,
)
from .types.query_profile import (
    ExecutionStats,
    ExplainMetrics,
    ExplainOptions,
    PlanSummary,
)

__all__ = (
    "DatastoreAsyncClient",
    "AggregationQuery",
    "AggregationResult",
    "AggregationResultBatch",
    "AllocateIdsRequest",
    "AllocateIdsResponse",
    "ArrayValue",
    "BeginTransactionRequest",
    "BeginTransactionResponse",
    "CommitRequest",
    "CommitResponse",
    "CompositeFilter",
    "DatastoreClient",
    "Entity",
    "EntityResult",
    "ExecutionStats",
    "ExplainMetrics",
    "ExplainOptions",
    "Filter",
    "FindNearest",
    "GqlQuery",
    "GqlQueryParameter",
    "Key",
    "KindExpression",
    "LookupRequest",
    "LookupResponse",
    "Mutation",
    "MutationResult",
    "PartitionId",
    "PlanSummary",
    "Projection",
    "PropertyFilter",
    "PropertyMask",
    "PropertyOrder",
    "PropertyReference",
    "PropertyTransform",
    "Query",
    "QueryResultBatch",
    "ReadOptions",
    "RequestOptions",
    "ReserveIdsRequest",
    "ReserveIdsResponse",
    "RollbackRequest",
    "RollbackResponse",
    "RunAggregationQueryRequest",
    "RunAggregationQueryResponse",
    "RunQueryRequest",
    "RunQueryResponse",
    "TransactionOptions",
    "Value",
)

api_core.check_python_version("google.cloud.datastore_v1")
api_core.check_dependency_versions("google.cloud.datastore_v1")
