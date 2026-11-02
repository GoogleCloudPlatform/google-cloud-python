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
from google.cloud.vectorsearch import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.vectorsearch_v1.services.data_object_search_service.async_client import (
    DataObjectSearchServiceAsyncClient,
)
from google.cloud.vectorsearch_v1.services.data_object_search_service.client import (
    DataObjectSearchServiceClient,
)
from google.cloud.vectorsearch_v1.services.data_object_service.async_client import (
    DataObjectServiceAsyncClient,
)
from google.cloud.vectorsearch_v1.services.data_object_service.client import (
    DataObjectServiceClient,
)
from google.cloud.vectorsearch_v1.services.vector_search_service.async_client import (
    VectorSearchServiceAsyncClient,
)
from google.cloud.vectorsearch_v1.services.vector_search_service.client import (
    VectorSearchServiceClient,
)
from google.cloud.vectorsearch_v1.types.common import DistanceMetric
from google.cloud.vectorsearch_v1.types.data_object import (
    DataObject,
    DenseVector,
    SparseVector,
    Vector,
)
from google.cloud.vectorsearch_v1.types.data_object_search_service import (
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
from google.cloud.vectorsearch_v1.types.data_object_service import (
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
from google.cloud.vectorsearch_v1.types.embedding_config import (
    EmbeddingTaskType,
    VertexEmbeddingConfig,
)
from google.cloud.vectorsearch_v1.types.encryption_spec import EncryptionSpec
from google.cloud.vectorsearch_v1.types.vectorsearch_service import (
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
    "DataObjectSearchServiceClient",
    "DataObjectSearchServiceAsyncClient",
    "DataObjectServiceClient",
    "DataObjectServiceAsyncClient",
    "VectorSearchServiceClient",
    "VectorSearchServiceAsyncClient",
    "DistanceMetric",
    "DataObject",
    "DenseVector",
    "SparseVector",
    "Vector",
    "AggregateDataObjectsRequest",
    "AggregateDataObjectsResponse",
    "BatchSearchDataObjectsRequest",
    "BatchSearchDataObjectsResponse",
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
    "TextSearch",
    "VectorSearch",
    "VertexRanker",
    "AggregationMethod",
    "BatchCreateDataObjectsRequest",
    "BatchCreateDataObjectsResponse",
    "BatchDeleteDataObjectsRequest",
    "BatchUpdateDataObjectsRequest",
    "BatchUpdateDataObjectsResponse",
    "CreateDataObjectRequest",
    "DeleteDataObjectRequest",
    "GetDataObjectRequest",
    "UpdateDataObjectRequest",
    "VertexEmbeddingConfig",
    "EmbeddingTaskType",
    "EncryptionSpec",
    "Collection",
    "CreateCollectionRequest",
    "CreateIndexRequest",
    "DedicatedInfrastructure",
    "DeleteCollectionRequest",
    "DeleteIndexRequest",
    "DenseScannIndex",
    "DenseVectorField",
    "ExportDataObjectsMetadata",
    "ExportDataObjectsRequest",
    "ExportDataObjectsResponse",
    "GetCollectionRequest",
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
    "SparseVectorField",
    "UpdateCollectionRequest",
    "UpdateIndexRequest",
    "VectorField",
)
