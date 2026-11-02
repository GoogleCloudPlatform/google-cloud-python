# Copyright 2025 Google LLC
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

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from google.cloud.firestore_v1 import pipeline_stages as stages
from google.cloud.firestore_v1._helpers import DOCUMENT_PATH_DELIMITER
from google.cloud.firestore_v1.base_pipeline import SubPipeline, _BasePipeline

if TYPE_CHECKING:  # pragma: NO COVER
    from google.cloud.firestore_v1.async_client import AsyncClient
    from google.cloud.firestore_v1.base_aggregation import BaseAggregationQuery
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference
    from google.cloud.firestore_v1.base_document import BaseDocumentReference
    from google.cloud.firestore_v1.base_query import BaseQuery
    from google.cloud.firestore_v1.client import Client
    from google.cloud.firestore_v1.pipeline_expressions import CONSTANT_TYPE, Expression


PipelineType = TypeVar("PipelineType", bound=_BasePipeline)


class PipelineSource(Generic[PipelineType]):
    """
    A factory for creating Pipeline instances, which provide a framework for building data
    transformation and query pipelines for Firestore.

    Not meant to be instantiated directly. Instead, start by calling client.pipeline()
    to obtain an instance of PipelineSource. From there, you can use the provided
    methods to specify the data source for your pipeline.
    """

    def __init__(self, client: Client | AsyncClient):
        self.client = client

    def _create_pipeline(self, source_stage):
        return self.client._pipeline_cls._create_with_stages(self.client, source_stage)

    def create_from(
        self, query: "BaseQuery" | "BaseAggregationQuery" | "BaseCollectionReference"
    ) -> PipelineType:
        """
        Create a pipeline from an existing query

        Args:
            query: the query to build the pipeline off of
        Returns:
            a new pipeline instance representing the query
        """
        return query._build_pipeline(self)

    def collection(self, path: str | tuple[str]) -> PipelineType:
        """
        Creates a new Pipeline that operates on a specified Firestore collection.

        Args:
            path: The path to the Firestore collection (e.g., "users"). Can either be:
                * A single ``/``-delimited path to a collection
                * A tuple of collection path segment
        Returns:
            a new pipeline instance targeting the specified collection
        """
        if isinstance(path, tuple):
            path = DOCUMENT_PATH_DELIMITER.join(path)
        return self._create_pipeline(stages.Collection(path))

    def collection_group(self, collection_id: str) -> PipelineType:
        """
        Creates a new Pipeline that that operates on all documents in a collection group.
        Args:
            collection_id: The ID of the collection group
        Returns:
            a new pipeline instance targeting the specified collection group
        """
        return self._create_pipeline(stages.CollectionGroup(collection_id))

    def database(self) -> PipelineType:
        """
        Creates a new Pipeline that operates on all documents in the Firestore database.
        Returns:
            a new pipeline instance targeting the specified collection
        """
        return self._create_pipeline(stages.Database())

    def documents(self, *docs: "BaseDocumentReference") -> PipelineType:
        """
        Creates a new Pipeline that operates on a specific set of Firestore documents.
        Args:
            docs: The DocumentReference instances representing the documents to include in the pipeline.
        Returns:
            a new pipeline instance targeting the specified documents
        """
        return self._create_pipeline(stages.Documents.of(*docs))

    def literals(
        self, *documents: dict[str, Expression | CONSTANT_TYPE]
    ) -> PipelineType:
        """
        Returns documents from a fixed set of predefined document objects.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Constant
            >>> documents = [
            ...     {"name": "joe", "age": 10},
            ...     {"name": "bob", "age": 30},
            ...     {"name": "alice", "age": 40}
            ... ]
            >>> pipeline = client.pipeline()
            ...     .literals(*documents)
            ...     .where(field("age").lessThan(35))

            Output documents:
            ```json
            [
                {"name": "joe", "age": 10},
                {"name": "bob", "age": 30}
            ]
            ```

        Behavior:
            The `literals(...)` stage can only be used as the first stage in a pipeline (or
            sub-pipeline). The order of documents returned from the `literals` matches the
            order in which they are defined.

            While literal values are the most common, it is also possible to pass in
            expressions, which will be evaluated and returned, making it possible to test
            out different query / expression behavior without first needing to create some
            test data.

            For example, the following shows how to quickly test out the `length(...)`
            function on some constant test sets:

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Constant
            >>> documents = [
            ...     {"x": Constant.of("foo-bar-baz").char_length()},
            ...     {"x": Constant.of("bar").char_length()}
            ... ]
            >>> pipeline = client.pipeline().literals(*documents)

            Output documents:
            ```json
            [
                {"x": 11},
                {"x": 3}
            ]
            ```

        Args:
            *documents: One or more documents to be returned by this stage. Each can be a `dict`
                       of values of `Expression` or `CONSTANT_TYPE` types.
        Returns:
            A new pipeline instance targeting the specified literal documents
        """
        return self._create_pipeline(stages.Literals(*documents))

    @staticmethod
    def subcollection(path: str) -> SubPipeline:
        """
        Initializes a pipeline scoped to a subcollection.

        This method allows you to start a new pipeline that operates on a subcollection of the
        current document. It is intended to be used as a subquery.

        **Note:** A pipeline created with `subcollection` cannot be executed directly using
        `execute()`. It must be used within a parent pipeline.

        Example:
            >>> db.pipeline().collection("books").add_fields(
            ...     PipelineSource.subcollection("reviews")
            ...         .aggregate(AggregateFunction.average("rating").as_("avg_rating"))
            ...         .to_scalar_expression().as_("average_rating")
            ... )

        Args:
            path: The path of the subcollection.

        Returns:
            A new pipeline instance targeting the specified subcollection
        """
        return SubPipeline._create_with_stages(None, stages.Subcollection(path))
