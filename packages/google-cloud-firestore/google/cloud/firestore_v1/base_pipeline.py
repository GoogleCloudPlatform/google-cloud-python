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

from typing import TYPE_CHECKING, Sequence, Type, TypeVar

from google.cloud.firestore_v1 import pipeline_stages as stages
from google.cloud.firestore_v1 import pipeline_types as types
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
from google.cloud.firestore_v1.pipeline_expressions import (
    AggregateFunction,
    AliasedExpression,
    BooleanExpression,
    Expression,
    Field,
    FunctionExpression,
    Selectable,
    _PipelineValueExpression,
)
from google.cloud.firestore_v1.types.pipeline import (
    StructuredPipeline as StructuredPipeline_pb,
)
from google.cloud.firestore_v1.vector import Vector

if TYPE_CHECKING:  # pragma: NO COVER
    from google.cloud.firestore_v1.async_client import AsyncClient
    from google.cloud.firestore_v1.client import Client
    from google.cloud.firestore_v1.types.document import Value

_T = TypeVar("_T", bound="_BasePipeline")


class _BasePipeline:
    """
    Base class for building Firestore data transformation and query pipelines.

    This class is not intended to be instantiated directly.
    Use `client.pipeline()` to create pipeline instances.
    """

    def __init__(self, client: Client | AsyncClient | None):
        """
        Initializes a new pipeline.

        Pipelines should not be instantiated directly. Instead,
        call client.pipeline() to create an instance

        Args:
            client: The client associated with the pipeline
        """
        self._client = client
        self.stages: Sequence[stages.Stage] = tuple()

    @classmethod
    def _create_with_stages(
        cls: Type[_T], client: Client | AsyncClient | None, *stages
    ) -> _T:
        """
        Initializes a new pipeline with the given stages.

        Pipeline classes should not be instantiated directly.

        Args:
            client: The client associated with the pipeline
            *stages: Initial stages for the pipeline.
        """
        new_instance = cls(client)
        new_instance.stages = tuple(stages)
        return new_instance

    def __repr__(self):
        cls_str = type(self).__name__
        if not self.stages:
            return f"{cls_str}()"
        elif len(self.stages) == 1:
            return f"{cls_str}({self.stages[0]!r})"
        else:
            stages_str = ",\n  ".join([repr(s) for s in self.stages])
            return f"{cls_str}(\n  {stages_str}\n)"

    def _to_pb(self, **options) -> StructuredPipeline_pb:
        return StructuredPipeline_pb(
            pipeline={"stages": [s._to_pb() for s in self.stages]},
            options=options,
        )

    def to_array_expression(self) -> Expression:
        """
        Converts this Pipeline into an expression that evaluates to an array of results.
        Used for embedding 1:N subqueries into stages like `addFields`.

        Example:
            >>> # Get a list of all reviewer names for each book
            >>> db.pipeline().collection("books").define(Field.of("id").as_("book_id")).add_fields(
            ...     db.pipeline().collection("reviews")
            ...         .where(Field.of("book_id").equal(Variable("book_id")))
            ...         .select(Field.of("reviewer").as_("name"))
            ...         .to_array_expression().as_("reviewers")
            ... )

        Returns:
            An :class:`Expression` representing the execution of this pipeline.
        """
        return FunctionExpression("array", [_PipelineValueExpression(self)])

    def to_scalar_expression(self) -> Expression:
        """
        Converts this Pipeline into an expression that evaluates to a single scalar result.
        Used for 1:1 lookups or Aggregations when the subquery is expected to return a single value or object.

        **Result Unwrapping:**
        For simpler access, scalar subqueries producing a single field automatically unwrap that value to the
        top level, ignoring the inner alias. If the subquery returns multiple fields, they are preserved as a map.

        Example:
            >>> # Calculate average rating for each restaurant using a subquery
            >>> db.pipeline().collection("restaurants").define(Field.of("id").as_("rid")).add_fields(
            ...     db.pipeline().collection("reviews")
            ...         .where(Field.of("restaurant_id").equal(Variable("rid")))
            ...         .aggregate(AggregateFunction.average("rating").as_("value"))
            ...         .to_scalar_expression().as_("average_rating")
            ... )

        **Runtime Validation:**
        The runtime will validate that the result set contains exactly one item. It returns an error if the result has more than one item, and evaluates to `null` if the pipeline has zero results.

        Returns:
            An :class:`Expression` representing the execution of this pipeline.
        """
        return FunctionExpression("scalar", [_PipelineValueExpression(self)])

    def _append(self, new_stage):
        """
        Create a new Pipeline object with a new stage appended
        """
        return self.__class__._create_with_stages(self._client, *self.stages, new_stage)

    def add_fields(self, *fields: Selectable) -> "_BasePipeline":
        """
        Adds new fields to outputs from previous stages.

        This stage allows you to compute values on-the-fly based on existing data
        from previous stages or constants. You can use this to create new fields
        or overwrite existing ones (if there is name overlap).

        The added fields are defined using `Selectable` expressions, which can be:
            - `Field`: References an existing document field.
            - `Function`: Performs a calculation using functions like `add`,
              `multiply` with assigned aliases using `Expression.as_()`.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field, add
            >>> pipeline = client.pipeline().collection("books")
            >>> pipeline = pipeline.add_fields(
            ...     Field.of("rating").as_("bookRating"), # Rename 'rating' to 'bookRating'
            ...     add(5, Field.of("quantity")).as_("totalCost")  # Calculate 'totalCost'
            ... )

        Args:
            *fields: The fields to add to the documents, specified as `Selectable`
                     expressions.
        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.AddFields(*fields))

    def remove_fields(self, *fields: Field | str) -> "_BasePipeline":
        """
        Removes fields from outputs of previous stages.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field
            >>> pipeline = client.pipeline().collection("books")
            >>> # Remove by name
            >>> pipeline = pipeline.remove_fields("rating", "cost")
            >>> # Remove by Field object
            >>> pipeline = pipeline.remove_fields(Field.of("rating"), Field.of("cost"))


        Args:
            *fields: The fields to remove, specified as field names (str) or
                     `Field` objects.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.RemoveFields(*fields))

    def select(self, *selections: str | Selectable) -> "_BasePipeline":
        """
        Selects or creates a set of fields from the outputs of previous stages.

        The selected fields are defined using `Selectable` expressions or field names:
            - `Field`: References an existing document field.
            - `Function`: Represents the result of a function with an assigned alias
              name using `Expression.as_()`.
            - `str`: The name of an existing field.

        If no selections are provided, the output of this stage is empty. Use
        `add_fields()` instead if only additions are desired.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field, to_upper
            >>> pipeline = client.pipeline().collection("books")
            >>> # Select by name
            >>> pipeline = pipeline.select("name", "address")
            >>> # Select using Field and Function expressions
            >>> pipeline = pipeline.select(
            ...     Field.of("name"),
            ...     Field.of("address").to_upper().as_("upperAddress"),
            ... )

        Args:
            *selections: The fields to include in the output documents, specified as
                         field names (str) or `Selectable` expressions.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Select(*selections))

    def where(self, condition: BooleanExpression) -> "_BasePipeline":
        """
        Filters the documents from previous stages to only include those matching
        the specified `BooleanExpression`.

        This stage allows you to apply conditions to the data, similar to a "WHERE"
        clause in SQL. You can filter documents based on their field values, using
        implementations of `BooleanExpression`, typically including but not limited to:
            - field comparators: `eq`, `lt` (less than), `gt` (greater than), etc.
            - logical operators: `And`, `Or`, `Not`, etc.
            - advanced functions: `regex_matches`, `array_contains`, etc.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field, And,
            >>> pipeline = client.pipeline().collection("books")
            >>> # Using static functions
            >>> pipeline = pipeline.where(
            ...     And(
            ...         Field.of("rating").gt(4.0),   # Filter for ratings > 4.0
            ...         Field.of("genre").eq("Science Fiction") # Filter for genre
            ...     )
            ... )
            >>> # Using methods on expressions
            >>> pipeline = pipeline.where(
            ...     And(
            ...         Field.of("rating").gt(4.0),
            ...         Field.of("genre").eq("Science Fiction")
            ...     )
            ... )


        Args:
            condition: The `BooleanExpression` to apply.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Where(condition))

    def find_nearest(
        self,
        field: str | Expression,
        vector: Sequence[float] | "Vector",
        distance_measure: "DistanceMeasure",
        options: types.FindNearestOptions | None = None,
    ) -> "_BasePipeline":
        """
        Performs vector distance (similarity) search with given parameters on the
        stage inputs.

        This stage adds a "nearest neighbor search" capability to your pipelines.
        Given a field or expression that evaluates to a vector and a target vector,
        this stage will identify and return the inputs whose vector is closest to
        the target vector, using the specified distance measure and options.

        Example:
            >>> from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
            >>> from google.cloud.firestore_v1.pipeline_stages import FindNearestOptions
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field
            >>>
            >>> target_vector = [0.1, 0.2, 0.3]
            >>> pipeline = client.pipeline().collection("books")
            >>> # Find using field name
            >>> pipeline = pipeline.find_nearest(
            ...     "topicVectors",
            ...     target_vector,
            ...     DistanceMeasure.COSINE,
            ...     options=FindNearestOptions(limit=10, distance_field="distance")
            ... )
            >>> # Find using Field expression
            >>> pipeline = pipeline.find_nearest(
            ...     Field.of("topicVectors"),
            ...     target_vector,
            ...     DistanceMeasure.COSINE,
            ...     options=FindNearestOptions(limit=10, distance_field="distance")
            ... )

        Args:
            field: The name of the field (str) or an expression (`Expression`) that
                   evaluates to the vector data. This field should store vector values.
            vector: The target vector (sequence of floats or `Vector` object) to
                    compare against.
            distance_measure: The distance measure (`DistanceMeasure`) to use
                              (e.g., `DistanceMeasure.COSINE`, `DistanceMeasure.EUCLIDEAN`).
            limit: The maximum number of nearest neighbors to return.
            options: Configuration options (`FindNearestOptions`) for the search,
                     such as limit and output distance field name.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(
            stages.FindNearest(field, vector, distance_measure, options)
        )

    def replace_with(
        self,
        field: Selectable,
    ) -> "_BasePipeline":
        """
        Fully overwrites all fields in a document with those coming from a nested map.

        This stage allows you to emit a map value as a document. Each key of the map becomes a field
        on the document that contains the corresponding value.

        Example:
            Input document:
            ```json
            {
              "name": "John Doe Jr.",
              "parents": {
                "father": "John Doe Sr.",
                "mother": "Jane Doe"
              }
            }
            ```

            >>> # Emit the 'parents' map as the document
            >>> pipeline = client.pipeline().collection("people").replace_with(Field.of("parents"))

            Output document:
            ```json
            {
              "father": "John Doe Sr.",
              "mother": "Jane Doe"
            }
            ```

        Args:
            field: The `Selectable` field containing the map whose content will
                   replace the document.
        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.ReplaceWith(field))

    def sort(self, *orders: stages.Ordering) -> "_BasePipeline":
        """
        Sorts the documents from previous stages based on one or more `Ordering` criteria.

        This stage allows you to order the results of your pipeline. You can specify
        multiple `Ordering` instances to sort by multiple fields or expressions in
        ascending or descending order. If documents have the same value for a sorting
        criterion, the next specified ordering will be used. If all orderings result
        in equal comparison, the documents are considered equal and the relative order
        is unspecified.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field
            >>> pipeline = client.pipeline().collection("books")
            >>> # Sort books by rating descending, then title ascending
            >>> pipeline = pipeline.sort(
            ...     Field.of("rating").descending(),
            ...     Field.of("title").ascending()
            ... )

        Args:
            *orders: One or more `Ordering` instances specifying the sorting criteria.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Sort(*orders))

    def search(
        self, query_or_options: str | BooleanExpression | types.SearchOptions
    ) -> "_BasePipeline":
        """
        Adds a search stage to the pipeline.

        .. note::
            This feature is currently in beta and is subject to change.

        This stage filters documents based on the provided query expression.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_stages import SearchOptions
            >>> from google.cloud.firestore_v1.pipeline_expressions import And, DocumentMatches, Field, GeoPoint
            >>> # Search for restaurants matching either "waffles" or "pancakes" near a location
            >>> pipeline = client.pipeline().collection("restaurants").search(
            ...     SearchOptions(
            ...         query=And(
            ...             DocumentMatches("waffles OR pancakes"),
            ...             Field.of("location").geo_distance(GeoPoint(38.9, -107.0)).less_than(1000)
            ...         ),
            ...         sort=Score().descending()
            ...     )
            ... )

        Args:
            options: Either a string or expression representing the search query, or
                A `SearchOptions` instance configuring the search.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Search(query_or_options))

    def sample(self, limit_or_options: int | types.SampleOptions) -> "_BasePipeline":
        """
        Performs a pseudo-random sampling of the documents from the previous stage.

        This stage filters documents pseudo-randomly.
        - If an `int` limit is provided, it specifies the maximum number of documents
          to emit. If fewer documents are available, all are passed through.
        - If `SampleOptions` are provided, they specify how sampling is performed
          (e.g., by document count or percentage).

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import SampleOptions
            >>> pipeline = client.pipeline().collection("books")
            >>> # Sample 10 books, if available.
            >>> pipeline = pipeline.sample(10)
            >>> pipeline = pipeline.sample(SampleOptions.doc_limit(10))
            >>> # Sample 50% of books.
            >>> pipeline = pipeline.sample(SampleOptions.percentage(0.5))


        Args:
            limit_or_options: Either an integer specifying the maximum number of
                              documents to sample, or a `SampleOptions` object.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Sample(limit_or_options))

    def union(self, other: "_BasePipeline") -> "_BasePipeline":
        """
        Performs a union of all documents from this pipeline and another pipeline,
        including duplicates.

        This stage passes through documents from the previous stage of this pipeline,
        and also passes through documents from the previous stage of the `other`
        pipeline provided. The order of documents emitted from this stage is undefined.

        Example:
            >>> books_pipeline = client.pipeline().collection("books")
            >>> magazines_pipeline = client.pipeline().collection("magazines")
            >>> # Emit documents from both collections
            >>> combined_pipeline = books_pipeline.union(magazines_pipeline)

        Args:
            other: The other `Pipeline` whose results will be unioned with this one.

        Raises:
            ValueError: If the `other` pipeline is a relative pipeline (e.g. created without a client).

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        if other._client is None:
            raise ValueError(
                "Union only supports combining root pipelines, doesn't support relative scope Pipeline "
                "like relative subcollection pipeline"
            )
        return self._append(stages.Union(other))

    def unnest(
        self,
        field: str | Selectable,
        alias: str | Field | None = None,
        options: types.UnnestOptions | None = None,
    ) -> "_BasePipeline":
        """
        Produces a document for each element in an array field from the previous stage document.

        For each previous stage document, this stage will emit zero or more augmented documents. The
        input array found in the previous stage document field specified by the `fieldName` parameter,
        will emit an augmented document for each input array element. The input array element will
        augment the previous stage document by setting the `alias` field  with the array element value.
        If `alias` is unset, the data in `field` will be overwritten.

        Example:
            Input document:
            ```json
            { "title": "The Hitchhiker's Guide", "tags": [ "comedy", "sci-fi" ], ... }
            ```

            >>> from google.cloud.firestore_v1.pipeline_stages import UnnestOptions
            >>> pipeline = client.pipeline().collection("books")
            >>> # Emit a document for each tag
            >>> pipeline = pipeline.unnest("tags", alias="tag")

            Output documents (without options):
            ```json
            { "title": "The Hitchhiker's Guide", "tag": "comedy", ... }
            { "title": "The Hitchhiker's Guide", "tag": "sci-fi", ... }
            ```

        Optionally, `UnnestOptions` can specify a field to store the original index
        of the element within the array

        Example:
            Input document:
            ```json
            { "title": "The Hitchhiker's Guide", "tags": [ "comedy", "sci-fi" ], ... }
            ```

            >>> from google.cloud.firestore_v1.pipeline_stages import UnnestOptions
            >>> pipeline = client.pipeline().collection("books")
            >>> # Emit a document for each tag, including the index
            >>> pipeline = pipeline.unnest("tags", options=UnnestOptions(index_field="tagIndex"))

            Output documents (with index_field="tagIndex"):
            ```json
            { "title": "The Hitchhiker's Guide", "tags": "comedy", "tagIndex": 0, ... }
            { "title": "The Hitchhiker's Guide", "tags": "sci-fi", "tagIndex": 1, ... }
            ```

        Args:
            field: The name of the field containing the array to unnest.
            alias The alias field is used as the field name for each element within the output array.
                If unset, or if `alias` matches the `field`, the output data will overwrite the original field.
            options: Optional `UnnestOptions` to configure additional behavior, like adding an index field.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Unnest(field, alias, options))

    def raw_stage(
        self,
        name: str,
        *params: Expression,
        options: dict[str, Expression | Value] | None = None,
    ) -> "_BasePipeline":
        """
        Adds a stage to the pipeline by specifying the stage name as an argument. This does not offer any
        type safety on the stage params and requires the caller to know the order (and optionally names)
        of parameters accepted by the stage.

        This class provides a way to call stages that are supported by the Firestore backend but that
        are not implemented in the SDK version being used.

        Example:
            >>> # Assume we don't have a built-in "where" stage
            >>> pipeline = client.pipeline().collection("books")
            >>> pipeline = pipeline.raw_stage("where", Field.of("published").lt(900))
            >>> pipeline = pipeline.select("title", "author")

        Args:
            name: The name of the stage.
            *params: A sequence of `Expression` objects representing the parameters for the stage.
            options: An optional dictionary of stage options.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.RawStage(name, *params, options=options or {}))

    def offset(self, offset: int) -> "_BasePipeline":
        """
        Skips the first `offset` number of documents from the results of previous stages.

        This stage is useful for implementing pagination, allowing you to retrieve
        results in chunks. It is typically used in conjunction with `limit()` to
        control the size of each page.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field
            >>> pipeline = client.pipeline().collection("books")
            >>> # Retrieve the second page of 20 results (assuming sorted)
            >>> pipeline = pipeline.sort(Field.of("published").descending())
            >>> pipeline = pipeline.offset(20)  # Skip the first 20 results
            >>> pipeline = pipeline.limit(20)   # Take the next 20 results

        Args:
            offset: The non-negative number of documents to skip.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Offset(offset))

    def limit(self, limit: int) -> "_BasePipeline":
        """
        Limits the maximum number of documents returned by previous stages to `limit`.

        This stage is useful for controlling the size of the result set, often used for:
            - **Pagination:** In combination with `offset()` to retrieve specific pages.
            - **Top-N queries:** To get a limited number of results after sorting.
            - **Performance:** To prevent excessive data transfer.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field
            >>> pipeline = client.pipeline().collection("books")
            >>> # Limit the results to the top 10 highest-rated books
            >>> pipeline = pipeline.sort(Field.of("rating").descending())
            >>> pipeline = pipeline.limit(10)

        Args:
            limit: The non-negative maximum number of documents to return.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Limit(limit))

    def aggregate(
        self,
        *accumulators: AliasedExpression[AggregateFunction],
        groups: Sequence[str | Selectable] = (),
    ) -> "_BasePipeline":
        """
        Performs aggregation operations on the documents from previous stages,
        optionally grouped by specified fields or expressions.

        This stage allows you to calculate aggregate values (like sum, average, count,
        min, max) over a set of documents.

        - **Accumulators:** Define the aggregation calculations using `AggregateFunction`
          expressions (e.g., `sum()`, `avg()`, `count()`, `min()`, `max()`) combined
          with `as_()` to name the result field.
        - **Groups:** Optionally specify fields (by name or `Selectable`) to group
          the documents by. Aggregations are then performed within each distinct group.
          If no groups are provided, the aggregation is performed over the entire input.
        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field
            >>> pipeline = client.pipeline().collection("books")
            >>> # Calculate the average rating and total count for all books
            >>> pipeline = pipeline.aggregate(
            ...     Field.of("rating").avg().as_("averageRating"),
            ...     Field.of("rating").count().as_("totalBooks")
            ... )
            >>> # Calculate the average rating for each genre
            >>> pipeline = pipeline.aggregate(
            ...     Field.of("rating").avg().as_("avg_rating"),
            ...     groups=["genre"] # Group by the 'genre' field
            ... )
            >>> # Calculate the count for each author, grouping by Field object
            >>> pipeline = pipeline.aggregate(
            ...     Count().as_("bookCount"),
            ...     groups=[Field.of("author")]
            ... )


        Args:
            *accumulators: One or more expressions defining the aggregations to perform and their
                           corresponding output names.
            groups: An optional sequence of field names (str) or `Selectable`
                    expressions to group by before aggregating.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Aggregate(*accumulators, groups=groups))

    def distinct(self, *fields: str | Selectable) -> "_BasePipeline":
        """
        Returns documents with distinct combinations of values for the specified
        fields or expressions.

        This stage filters the results from previous stages to include only one
        document for each unique combination of values in the specified `fields`.
        The output documents contain only the fields specified in the `distinct` call.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field, to_upper
            >>> pipeline = client.pipeline().collection("books")
            >>> # Get a list of unique genres (output has only 'genre' field)
            >>> pipeline = pipeline.distinct("genre")
            >>> # Get unique combinations of author (uppercase) and genre
            >>> pipeline = pipeline.distinct(
            ...     Field.of("author").to_upper().as_("authorUpper"),
            ...     Field.of("genre")
            ... )


        Args:
            *fields: Field names (str) or `Selectable` expressions to consider when
                     determining distinct value combinations. The output will only
                     contain these fields/expressions.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Distinct(*fields))

    def delete(self) -> "_BasePipeline":
        """
        Deletes the documents from the current pipeline stage.

        .. note::
            This feature is currently in beta and is subject to change.

        Example:
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field
            >>> pipeline = client.pipeline().collection("logs")
            >>> # Delete all documents in the "logs" collection where "status" is "archived"
            >>> pipeline = pipeline.where(Field.of("status").equal("archived")).delete()
            >>> pipeline.execute()

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Delete())

    def update(self, *transformed_fields: "Selectable") -> "_BasePipeline":
        """
        Performs an update operation using documents from previous stages.

        .. note::
            This feature is currently in beta and is subject to change.

        If called without `transformed_fields`, this method updates the documents in
        place based on the data flowing through the pipeline.

        To update specific fields with new values, provide `Selectable` expressions that define the
        transformations to apply.

        Example 1: Update a collection's schema by adding a new field and removing an old one.
            >>> from google.cloud.firestore_v1.pipeline_expressions import Constant
            >>> pipeline = client.pipeline().collection("books")
            >>> pipeline = pipeline.add_fields(Constant.of("Fiction").as_("genre"))
            >>> pipeline = pipeline.remove_fields("old_genre").update()
            >>> pipeline.execute()

        Example 2: Update documents in place with data from literals.
            >>> pipeline = client.pipeline().literals(
            ...     {"__name__": client.collection("books").document("book1"), "status": "Updated"}
            ... ).update()
            >>> pipeline.execute()

        Example 3: Update documents from previous stages with specified transformations.
            >>> from google.cloud.firestore_v1.pipeline_expressions import Field, Constant
            >>> pipeline = client.pipeline().collection("books")
            >>> # Update the "status" field to "Discounted" for all books where price > 50
            >>> pipeline = pipeline.where(Field.of("price").greater_than(50))
            >>> pipeline = pipeline.update(Constant.of("Discounted").as_("status"))
            >>> pipeline.execute()

        Args:
            *transformed_fields: Optional. The transformations to apply. If not provided,
                the update is performed in place based on the data flowing through the pipeline.

        Returns:
            A new Pipeline object with this stage appended to the stage list
        """
        return self._append(stages.Update(*transformed_fields))

    def define(self, *aliased_expressions: AliasedExpression) -> "_BasePipeline":
        """
        Binds one or more expressions to Variables that can be accessed in subsequent stages
        or inner subqueries using `Variable`.

        Each Variable is defined using an :class:`AliasedExpression`, which pairs an expression with
        a name (alias).

        Example:
            >>> db.pipeline().collection("products").define(
            ...     Field.of("price").multiply(0.9).as_("discountedPrice"),
            ...     Field.of("stock").add(10).as_("newStock")
            ... ).where(
            ...     Variable("discountedPrice").less_than(100)
            ... ).select(Field.of("name"), Variable("newStock"))

        Args:
            *aliased_expressions: One or more :class:`AliasedExpression` defining the Variable names and values.

        Returns:
            A new Pipeline object with this stage appended to the stage list.
        """
        return self._append(stages.Define(*aliased_expressions))


class SubPipeline(_BasePipeline):
    """
    A pipeline scoped to a subcollection, created without a database client.
    Cannot be executed directly; it must be used as a subquery within another pipeline.
    """

    _EXECUTE_ERROR_MSG = (
        "This pipeline was created without a database (e.g., as a subcollection pipeline) and "
        "cannot be executed directly. It can only be used as part of another pipeline."
    )

    def execute(self, *args, **kwargs):
        """
        Raises:
            RuntimeError: Always, as a subcollection pipeline cannot be executed directly.
        """
        raise RuntimeError(self._EXECUTE_ERROR_MSG)

    def stream(self, *args, **kwargs):
        """
        Raises:
            RuntimeError: Always, as a subcollection pipeline cannot be streamed directly.
        """
        raise RuntimeError(self._EXECUTE_ERROR_MSG)
