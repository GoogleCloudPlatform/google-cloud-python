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

from google.cloud.vectorsearch_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.vectorsearch_v1.services.data_object_search_service",
    "google.cloud.vectorsearch_v1.services.data_object_service",
    "google.cloud.vectorsearch_v1.services.vector_search_service",
    "google.cloud.vectorsearch_v1.types.common",
    "google.cloud.vectorsearch_v1.types.data_object",
    "google.cloud.vectorsearch_v1.types.data_object_search_service",
    "google.cloud.vectorsearch_v1.types.data_object_service",
    "google.cloud.vectorsearch_v1.types.embedding_config",
    "google.cloud.vectorsearch_v1.types.encryption_spec",
    "google.cloud.vectorsearch_v1.types.vectorsearch_service",
}


from .services.data_object_search_service import (
    DataObjectSearchServiceAsyncClient,
    DataObjectSearchServiceClient,
)
from .services.data_object_service import (
    DataObjectServiceAsyncClient,
    DataObjectServiceClient,
)
from .services.vector_search_service import (
    VectorSearchServiceAsyncClient,
    VectorSearchServiceClient,
)
from .types.common import DistanceMetric
from .types.data_object import DataObject, DenseVector, SparseVector, Vector
from .types.data_object_search_service import (
    AggregateDataObjectsRequest,
    AggregateDataObjectsResponse,
    AggregationMethod,
    BatchSearchDataObjectsRequest,
    BatchSearchDataObjectsResponse,
    OutputFields,
    QueryDataObjectsRequest,
    QueryDataObjectsResponse,
    Ranker,
    ReciprocalRankFusion,
    Search,
    SearchDataObjectsRequest,
    SearchDataObjectsResponse,
    SearchHint,
    SearchResult,
    SemanticSearch,
    TextSearch,
    VectorSearch,
    VertexRanker,
)
from .types.data_object_service import (
    BatchCreateDataObjectsRequest,
    BatchCreateDataObjectsResponse,
    BatchDeleteDataObjectsRequest,
    BatchUpdateDataObjectsRequest,
    BatchUpdateDataObjectsResponse,
    CreateDataObjectRequest,
    DeleteDataObjectRequest,
    GetDataObjectRequest,
    UpdateDataObjectRequest,
)
from .types.embedding_config import EmbeddingTaskType, VertexEmbeddingConfig
from .types.encryption_spec import EncryptionSpec
from .types.vectorsearch_service import (
    Collection,
    CreateCollectionRequest,
    CreateIndexRequest,
    DedicatedInfrastructure,
    DeleteCollectionRequest,
    DeleteIndexRequest,
    DenseScannIndex,
    DenseVectorField,
    ExportDataObjectsMetadata,
    ExportDataObjectsRequest,
    ExportDataObjectsResponse,
    GetCollectionRequest,
    GetIndexRequest,
    ImportDataObjectsMetadata,
    ImportDataObjectsRequest,
    ImportDataObjectsResponse,
    Index,
    ListCollectionsRequest,
    ListCollectionsResponse,
    ListIndexesRequest,
    ListIndexesResponse,
    OperationMetadata,
    SparseVectorField,
    UpdateCollectionRequest,
    UpdateIndexRequest,
    VectorField,
)

__all__ = (
    "DataObjectSearchServiceAsyncClient",
    "DataObjectServiceAsyncClient",
    "VectorSearchServiceAsyncClient",
    "AggregateDataObjectsRequest",
    "AggregateDataObjectsResponse",
    "AggregationMethod",
    "BatchCreateDataObjectsRequest",
    "BatchCreateDataObjectsResponse",
    "BatchDeleteDataObjectsRequest",
    "BatchSearchDataObjectsRequest",
    "BatchSearchDataObjectsResponse",
    "BatchUpdateDataObjectsRequest",
    "BatchUpdateDataObjectsResponse",
    "Collection",
    "CreateCollectionRequest",
    "CreateDataObjectRequest",
    "CreateIndexRequest",
    "DataObject",
    "DataObjectSearchServiceClient",
    "DataObjectServiceClient",
    "DedicatedInfrastructure",
    "DeleteCollectionRequest",
    "DeleteDataObjectRequest",
    "DeleteIndexRequest",
    "DenseScannIndex",
    "DenseVector",
    "DenseVectorField",
    "DistanceMetric",
    "EmbeddingTaskType",
    "EncryptionSpec",
    "ExportDataObjectsMetadata",
    "ExportDataObjectsRequest",
    "ExportDataObjectsResponse",
    "GetCollectionRequest",
    "GetDataObjectRequest",
    "GetIndexRequest",
    "ImportDataObjectsMetadata",
    "ImportDataObjectsRequest",
    "ImportDataObjectsResponse",
    "Index",
    "ListCollectionsRequest",
    "ListCollectionsResponse",
    "ListIndexesRequest",
    "ListIndexesResponse",
    "OperationMetadata",
    "OutputFields",
    "QueryDataObjectsRequest",
    "QueryDataObjectsResponse",
    "Ranker",
    "ReciprocalRankFusion",
    "Search",
    "SearchDataObjectsRequest",
    "SearchDataObjectsResponse",
    "SearchHint",
    "SearchResult",
    "SemanticSearch",
    "SparseVector",
    "SparseVectorField",
    "TextSearch",
    "UpdateCollectionRequest",
    "UpdateDataObjectRequest",
    "UpdateIndexRequest",
    "Vector",
    "VectorField",
    "VectorSearch",
    "VectorSearchServiceClient",
    "VertexEmbeddingConfig",
    "VertexRanker",
)

api_core.check_python_version("google.cloud.vectorsearch_v1")
api_core.check_dependency_versions("google.cloud.vectorsearch_v1")
