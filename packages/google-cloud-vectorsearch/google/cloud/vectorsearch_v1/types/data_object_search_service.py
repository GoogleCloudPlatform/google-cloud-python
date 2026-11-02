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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.vectorsearch_v1.types import common, embedding_config
from google.cloud.vectorsearch_v1.types import data_object as gcv_data_object

__protobuf__ = proto.module(
    package="google.cloud.vectorsearch.v1",
    manifest={
        "AggregationMethod",
        "OutputFields",
        "SearchHint",
        "Search",
        "VectorSearch",
        "SemanticSearch",
        "TextSearch",
        "SearchDataObjectsRequest",
        "SearchResult",
        "SearchDataObjectsResponse",
        "AggregateDataObjectsRequest",
        "AggregateDataObjectsResponse",
        "QueryDataObjectsRequest",
        "QueryDataObjectsResponse",
        "BatchSearchDataObjectsRequest",
        "Ranker",
        "ReciprocalRankFusion",
        "VertexRanker",
        "BatchSearchDataObjectsResponse",
    },
)


class AggregationMethod(proto.Enum):
    r"""Aggregation methods.

    Values:
        AGGREGATION_METHOD_UNSPECIFIED (0):
            Should not be used.
        COUNT (1):
            Count the number of data objects that match
            the filter.
    """

    AGGREGATION_METHOD_UNSPECIFIED = 0
    COUNT = 1


class OutputFields(proto.Message):
    r"""Defines a output fields struct for data in DataObject.

    Attributes:
        data_fields (MutableSequence[str]):
            Optional. The fields from the data fields to
            include in the output.
        vector_fields (MutableSequence[str]):
            Optional. The fields from the vector fields
            to include in the output.
        metadata_fields (MutableSequence[str]):
            Optional. The fields from the DataObject
            metadata to include in the output.
    """

    data_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    vector_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    metadata_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class SearchHint(proto.Message):
    r"""Represents a hint to the search index engine.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        knn_hint (google.cloud.vectorsearch_v1.types.SearchHint.KnnHint):
            Optional. If set, the search will use the
            system's default K-Nearest Neighbor (KNN) index
            engine.

            This field is a member of `oneof`_ ``index_type``.
        index_hint (google.cloud.vectorsearch_v1.types.SearchHint.IndexHint):
            Optional. Specifies that the search should
            use a particular index.

            This field is a member of `oneof`_ ``index_type``.
    """

    class IndexHint(proto.Message):
        r"""Message to specify the index to use for the search.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            dense_scann_params (google.cloud.vectorsearch_v1.types.SearchHint.IndexHint.DenseScannParams):
                Optional. Dense ScaNN parameters.

                This field is a member of `oneof`_ ``params``.
            name (str):
                Required. The resource name of the index to use for the
                search. The index must be in the same project, location, and
                collection. Format:
                ``projects/{project}/locations/{location}/collections/{collection}/indexes/{index}``
        """

        class DenseScannParams(proto.Message):
            r"""Parameters for dense ScaNN.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                target_recall (float):
                    Optional. The target recall for the search. Must be a double
                    in the range [0, 1]. While the search aims to achieve this
                    level of recall, it is not guaranteed.

                    This field is a member of `oneof`_ ``_target_recall``.
            """

            target_recall: float = proto.Field(
                proto.DOUBLE,
                number=3,
                optional=True,
            )

        dense_scann_params: "SearchHint.IndexHint.DenseScannParams" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="params",
            message="SearchHint.IndexHint.DenseScannParams",
        )
        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class KnnHint(proto.Message):
        r"""KnnHint will be used if search should be explicitly done on
        system's default K-Nearest Neighbor (KNN) index engine.

        """

    knn_hint: KnnHint = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="index_type",
        message=KnnHint,
    )
    index_hint: IndexHint = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="index_type",
        message=IndexHint,
    )


class Search(proto.Message):
    r"""A single search request within a batch operation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vector_search (google.cloud.vectorsearch_v1.types.VectorSearch):
            A vector-based search.

            This field is a member of `oneof`_ ``search_type``.
        semantic_search (google.cloud.vectorsearch_v1.types.SemanticSearch):
            A semantic search.

            This field is a member of `oneof`_ ``search_type``.
        text_search (google.cloud.vectorsearch_v1.types.TextSearch):
            A text search operation.

            This field is a member of `oneof`_ ``search_type``.
    """

    vector_search: "VectorSearch" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="search_type",
        message="VectorSearch",
    )
    semantic_search: "SemanticSearch" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="search_type",
        message="SemanticSearch",
    )
    text_search: "TextSearch" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="search_type",
        message="TextSearch",
    )


class VectorSearch(proto.Message):
    r"""Defines a search operation using a query vector.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vector (google.cloud.vectorsearch_v1.types.DenseVector):
            A dense vector for the query.

            This field is a member of `oneof`_ ``vector_type``.
        sparse_vector (google.cloud.vectorsearch_v1.types.SparseVector):
            A sparse vector for the query.

            This field is a member of `oneof`_ ``vector_type``.
        search_field (str):
            Required. The vector field to search.
        filter (google.protobuf.struct_pb2.Struct):
            Optional. A JSON filter expression, e.g.
            {"genre": {"$eq": "sci-fi"}}, represented as a
            google.protobuf.Struct.
        top_k (int):
            Optional. The number of nearest neighbors to
            return.

            This field is a member of `oneof`_ ``_top_k``.
        output_fields (google.cloud.vectorsearch_v1.types.OutputFields):
            Optional. Mask specifying which fields to
            return.
        search_hint (google.cloud.vectorsearch_v1.types.SearchHint):
            Optional. Sets the search hint. If no
            strategy is specified, the service will use an
            index if one is available, and fall back to the
            default KNN search otherwise.
        distance_metric (google.cloud.vectorsearch_v1.types.DistanceMetric):
            Optional. The distance metric to use for the KNN search. If
            not specified, DOT_PRODUCT will be used as the default.
    """

    vector: gcv_data_object.DenseVector = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="vector_type",
        message=gcv_data_object.DenseVector,
    )
    sparse_vector: gcv_data_object.SparseVector = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="vector_type",
        message=gcv_data_object.SparseVector,
    )
    search_field: str = proto.Field(
        proto.STRING,
        number=8,
    )
    filter: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    top_k: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    output_fields: "OutputFields" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OutputFields",
    )
    search_hint: "SearchHint" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="SearchHint",
    )
    distance_metric: common.DistanceMetric = proto.Field(
        proto.ENUM,
        number=11,
        enum=common.DistanceMetric,
    )


class SemanticSearch(proto.Message):
    r"""Defines a semantic search operation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        search_text (str):
            Optional. The query text, which is used to
            generate an embedding according to the embedding
            model specified in the collection config.

            Required when using the text search mode.
        search_field (str):
            Required. The vector field to search.
        task_type (google.cloud.vectorsearch_v1.types.EmbeddingTaskType):
            Optional. The task type of the query
            embedding. Must be specified for text-only
            embedding models, see
            <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/task-types>
            Not needed for multi modal embedding models, see
            <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings#specify-task-instructions>
        output_fields (google.cloud.vectorsearch_v1.types.OutputFields):
            Optional. The fields to return in the search
            results.
        filter (google.protobuf.struct_pb2.Struct):
            Optional. A JSON filter expression, e.g.
            {"genre": {"$eq": "sci-fi"}}, represented as a
            google.protobuf.Struct.
        top_k (int):
            Optional. The number of data objects to
            return.

            This field is a member of `oneof`_ ``_top_k``.
        search_hint (google.cloud.vectorsearch_v1.types.SearchHint):
            Optional. Sets the search hint. If no
            strategy is specified, the service will use an
            index if one is available, and fall back to KNN
            search otherwise.
    """

    search_text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_field: str = proto.Field(
        proto.STRING,
        number=2,
    )
    task_type: embedding_config.EmbeddingTaskType = proto.Field(
        proto.ENUM,
        number=5,
        enum=embedding_config.EmbeddingTaskType,
    )
    output_fields: "OutputFields" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputFields",
    )
    filter: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    top_k: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    search_hint: "SearchHint" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="SearchHint",
    )


class TextSearch(proto.Message):
    r"""Defines a text search operation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        search_text (str):
            Optional. The query text. Required when using
            the default text search mode.
        data_field_names (MutableSequence[str]):
            Optional. The data field names to search.
            Required when using the default text search
            mode.
        output_fields (google.cloud.vectorsearch_v1.types.OutputFields):
            Optional. The fields to return in the search
            results.
        top_k (int):
            Optional. The number of results to return.

            This field is a member of `oneof`_ ``_top_k``.
        filter (google.protobuf.struct_pb2.Struct):
            Optional. A JSON filter expression, e.g.
            ``{"genre": {"$eq": "sci-fi"}}``, represented as a
            ``google.protobuf.Struct``.
    """

    search_text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_field_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    output_fields: "OutputFields" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputFields",
    )
    top_k: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    filter: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )


class SearchDataObjectsRequest(proto.Message):
    r"""Request for performing a single search.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vector_search (google.cloud.vectorsearch_v1.types.VectorSearch):
            A vector search operation.

            This field is a member of `oneof`_ ``search_type``.
        semantic_search (google.cloud.vectorsearch_v1.types.SemanticSearch):
            A semantic search operation.

            This field is a member of `oneof`_ ``search_type``.
        text_search (google.cloud.vectorsearch_v1.types.TextSearch):
            Optional. A text search operation.

            This field is a member of `oneof`_ ``search_type``.
        parent (str):
            Required. The resource name of the Collection for which to
            search. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``
        page_size (int):
            Optional. The standard list page size. Only supported for
            KNN. If not set, up to search_type.top_k results will be
            returned. The maximum value is 1000; values above 1000 will
            be coerced to 1000.
        page_token (str):
            Optional. The standard list page token. Typically obtained
            via
            [SearchDataObjectsResponse.next_page_token][google.cloud.vectorsearch.v1.SearchDataObjectsResponse.next_page_token]
            of the previous
            [DataObjectSearchService.SearchDataObjects][google.cloud.vectorsearch.v1.DataObjectSearchService.SearchDataObjects]
            call.
    """

    vector_search: "VectorSearch" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="search_type",
        message="VectorSearch",
    )
    semantic_search: "SemanticSearch" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="search_type",
        message="SemanticSearch",
    )
    text_search: "TextSearch" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="search_type",
        message="TextSearch",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SearchResult(proto.Message):
    r"""A single search result.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_object (google.cloud.vectorsearch_v1.types.DataObject):
            Output only. The matching data object.
        distance (float):
            Output only. Similarity distance or ranker
            score returned by BatchSearchDataObjects.

            This field is a member of `oneof`_ ``_distance``.
    """

    data_object: gcv_data_object.DataObject = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcv_data_object.DataObject,
    )
    distance: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


class SearchDataObjectsResponse(proto.Message):
    r"""Response for a search request.

    Attributes:
        results (MutableSequence[google.cloud.vectorsearch_v1.types.SearchResult]):
            Output only. The list of dataObjects that
            match the search criteria.
        next_page_token (str):
            Output only. A token to retrieve next page of results. Pass
            to
            [DataObjectSearchService.SearchDataObjectsRequest.page_token][]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence["SearchResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AggregateDataObjectsRequest(proto.Message):
    r"""Request message for
    [DataObjectSearchService.AggregateDataObjects][google.cloud.vectorsearch.v1.DataObjectSearchService.AggregateDataObjects].

    Attributes:
        parent (str):
            Required. The resource name of the Collection for which to
            query. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``
        filter (google.protobuf.struct_pb2.Struct):
            Optional. A JSON filter expression, e.g.
            {"genre": {"$eq": "sci-fi"}}, represented as a
            google.protobuf.Struct.
        aggregate (google.cloud.vectorsearch_v1.types.AggregationMethod):
            Required. The aggregation method to apply to
            the query.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    aggregate: "AggregationMethod" = proto.Field(
        proto.ENUM,
        number=3,
        enum="AggregationMethod",
    )


class AggregateDataObjectsResponse(proto.Message):
    r"""Response message for
    [DataObjectSearchService.AggregateDataObjects][google.cloud.vectorsearch.v1.DataObjectSearchService.AggregateDataObjects].

    Attributes:
        aggregate_results (MutableSequence[google.protobuf.struct_pb2.Struct]):
            Output only. The aggregated results of the
            query.
    """

    aggregate_results: MutableSequence[struct_pb2.Struct] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class QueryDataObjectsRequest(proto.Message):
    r"""Request message for
    [DataObjectSearchService.QueryDataObjects][google.cloud.vectorsearch.v1.DataObjectSearchService.QueryDataObjects].

    Attributes:
        parent (str):
            Required. The resource name of the Collection for which to
            query. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``
        filter (google.protobuf.struct_pb2.Struct):
            Optional. A JSON filter expression, e.g.
            {"genre": {"$eq": "sci-fi"}}, represented as a
            google.protobuf.Struct.
        output_fields (google.cloud.vectorsearch_v1.types.OutputFields):
            Optional. Mask specifying which fields to
            return.
        page_size (int):
            Optional. The standard list page size.
            Default is 100. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. The standard list page token. Typically obtained
            via
            [QueryDataObjectsResponse.next_page_token][google.cloud.vectorsearch.v1.QueryDataObjectsResponse.next_page_token]
            of the previous
            [DataObjectSearchService.QueryDataObjects][google.cloud.vectorsearch.v1.DataObjectSearchService.QueryDataObjects]
            call.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    output_fields: "OutputFields" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OutputFields",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class QueryDataObjectsResponse(proto.Message):
    r"""Response message for
    [DataObjectSearchService.QueryDataObjects][google.cloud.vectorsearch.v1.DataObjectSearchService.QueryDataObjects].

    Attributes:
        data_objects (MutableSequence[google.cloud.vectorsearch_v1.types.DataObject]):
            Output only. The list of dataObjects that
            match the query.
        next_page_token (str):
            Output only. A token to retrieve next page of results. Pass
            to
            [DataObjectSearchService.QueryDataObjectsRequest.page_token][]
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    data_objects: MutableSequence[gcv_data_object.DataObject] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=gcv_data_object.DataObject,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchSearchDataObjectsRequest(proto.Message):
    r"""A request to perform a batch of search operations.

    Attributes:
        parent (str):
            Required. The resource name of the Collection for which to
            search. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``
        searches (MutableSequence[google.cloud.vectorsearch_v1.types.Search]):
            Required. A list of search requests to
            execute in parallel.
        combine (google.cloud.vectorsearch_v1.types.BatchSearchDataObjectsRequest.CombineResultsOptions):
            Optional. Options for combining the results
            of the batch search operations.
    """

    class CombineResultsOptions(proto.Message):
        r"""Options for combining the results of the batch search
        operations.

        Attributes:
            ranker (google.cloud.vectorsearch_v1.types.Ranker):
                Required. The ranker to use for combining the
                results.
            output_fields (google.cloud.vectorsearch_v1.types.OutputFields):
                Optional. Mask specifying which fields to
                return.
            top_k (int):
                Optional. The number of results to return. If
                not set, a default value will be used.
        """

        ranker: "Ranker" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Ranker",
        )
        output_fields: "OutputFields" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="OutputFields",
        )
        top_k: int = proto.Field(
            proto.INT32,
            number=3,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    searches: MutableSequence["Search"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Search",
    )
    combine: CombineResultsOptions = proto.Field(
        proto.MESSAGE,
        number=3,
        message=CombineResultsOptions,
    )


class Ranker(proto.Message):
    r"""Defines a ranker to combine results from multiple searches.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rrf (google.cloud.vectorsearch_v1.types.ReciprocalRankFusion):
            Reciprocal Rank Fusion ranking.

            This field is a member of `oneof`_ ``ranker``.
        vertex_ranker (google.cloud.vectorsearch_v1.types.VertexRanker):
            Optional. Vertex AI ranking.

            This field is a member of `oneof`_ ``reranker``.
    """

    rrf: "ReciprocalRankFusion" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="ranker",
        message="ReciprocalRankFusion",
    )
    vertex_ranker: "VertexRanker" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="reranker",
        message="VertexRanker",
    )


class ReciprocalRankFusion(proto.Message):
    r"""Defines the Reciprocal Rank Fusion (RRF) algorithm for result
    ranking.

    Attributes:
        weights (MutableSequence[float]):
            Required. The weights to apply to each search
            result set during fusion.
    """

    weights: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=1,
    )


class VertexRanker(proto.Message):
    r"""Defines a ranker using the Vertex AI ranking service.
    See
    <https://cloud.google.com/generative-ai-app-builder/docs/ranking>
    for details.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_record_spec (google.cloud.vectorsearch_v1.types.VertexRanker.TextRecordSpec):
            The record spec for text search.

            This field is a member of `oneof`_ ``record_spec``.
        model (str):
            Required. The model used for ranking documents. The list of
            available models is described in
            https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#models.
            Currently, only ``semantic-ranker-fast@latest`` is
            supported.
        top_n (int):
            Required. The number of documents to be
            processed for ranking.
    """

    class TextRecordSpec(proto.Message):
        r"""The record spec for text search.

        Attributes:
            query (str):
                Required. The query against which the records
                are ranked and scored.
            title_template (str):
                Optional. The template used to generate the
                record's title.
            content_template (str):
                Optional. The template used to generate the
                record's content.
        """

        query: str = proto.Field(
            proto.STRING,
            number=1,
        )
        title_template: str = proto.Field(
            proto.STRING,
            number=2,
        )
        content_template: str = proto.Field(
            proto.STRING,
            number=3,
        )

    text_record_spec: TextRecordSpec = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="record_spec",
        message=TextRecordSpec,
    )
    model: str = proto.Field(
        proto.STRING,
        number=4,
    )
    top_n: int = proto.Field(
        proto.INT32,
        number=5,
    )


class BatchSearchDataObjectsResponse(proto.Message):
    r"""A response from a batch search operation.

    Attributes:
        results (MutableSequence[google.cloud.vectorsearch_v1.types.SearchDataObjectsResponse]):
            Output only. A list of search responses, one
            for each request in the batch. If a ranker is
            used, a single ranked list of results is
            returned.
    """

    results: MutableSequence["SearchDataObjectsResponse"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchDataObjectsResponse",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
