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

from typing import (
    TYPE_CHECKING,
    Any,
    AsyncIterable,
    AsyncIterator,
    Generic,
    Iterable,
    Iterator,
    List,
    MutableMapping,
    Type,
    TypeVar,
)

from google.cloud.firestore_v1 import _helpers
from google.cloud.firestore_v1.field_path import FieldPath, get_nested_value
from google.cloud.firestore_v1.query_profile import ExplainStats, QueryExplainError
from google.cloud.firestore_v1.types.document import Value
from google.cloud.firestore_v1.types.firestore import ExecutePipelineRequest

if TYPE_CHECKING:  # pragma: NO COVER
    import datetime

    from google.protobuf.timestamp_pb2 import Timestamp

    from google.cloud.firestore_v1.async_client import AsyncClient
    from google.cloud.firestore_v1.async_pipeline import AsyncPipeline
    from google.cloud.firestore_v1.async_transaction import AsyncTransaction
    from google.cloud.firestore_v1.base_client import BaseClient
    from google.cloud.firestore_v1.base_document import BaseDocumentReference
    from google.cloud.firestore_v1.bson import BSONType
    from google.cloud.firestore_v1.client import Client
    from google.cloud.firestore_v1.pipeline import Pipeline
    from google.cloud.firestore_v1.pipeline_expressions import Constant
    from google.cloud.firestore_v1.query_profile import PipelineExplainOptions
    from google.cloud.firestore_v1.transaction import Transaction
    from google.cloud.firestore_v1.types.document import Value as ValueProto
    from google.cloud.firestore_v1.types.firestore import ExecutePipelineResponse
    from google.cloud.firestore_v1.vector import Vector


class PipelineResult:
    """
    Contains data read from a Firestore Pipeline. The data can be extracted with
    the `data()` or `get()` methods.

    If the PipelineResult represents a non-document result `ref` may be `None`.
    """

    def __init__(
        self,
        client: BaseClient,
        fields_pb: MutableMapping[str, ValueProto],
        ref: BaseDocumentReference | None = None,
        execution_time: Timestamp | None = None,
        create_time: Timestamp | None = None,
        update_time: Timestamp | None = None,
    ):
        """
        PipelineResult should be returned from `pipeline.execute()`, not constructed manually.

        Args:
            client: The Firestore client instance.
            fields_pb: A map of field names to their protobuf Value representations.
            ref: The DocumentReference or AsyncDocumentReference if this result corresponds to a document.
            execution_time: The time at which the pipeline execution producing this result occurred.
            create_time: The creation time of the document, if applicable.
            update_time: The last update time of the document, if applicable.
        """
        self._client = client
        self._fields_pb = fields_pb
        self._ref = ref
        self._execution_time = execution_time
        self._create_time = create_time
        self._update_time = update_time

    def __repr__(self):
        return f"{type(self).__name__}(data={self.data()!r})"

    @property
    def ref(self) -> BaseDocumentReference | None:
        """
        The `BaseDocumentReference` if this result represents a document, else `None`.
        """
        return self._ref

    @property
    def id(self) -> str | None:
        """The ID of the document if this result represents a document, else `None`."""
        return self._ref.id if self._ref else None

    @property
    def create_time(self) -> Timestamp | None:
        """The creation time of the document. `None` if not applicable."""
        return self._create_time

    @property
    def update_time(self) -> Timestamp | None:
        """The last update time of the document. `None` if not applicable."""
        return self._update_time

    @property
    def execution_time(self) -> Timestamp:
        """
        The time at which the pipeline producing this result was executed.

        Raise:
            ValueError: if not set
        """
        if self._execution_time is None:
            raise ValueError("'execution_time' is expected to exist, but it is None.")
        return self._execution_time

    def __eq__(self, other: object) -> bool:
        """
        Compares this `PipelineResult` to another object for equality.

        Two `PipelineResult` instances are considered equal if their document
        references (if any) are equal and their underlying field data
        (protobuf representation) is identical.
        """
        if not isinstance(other, PipelineResult):
            return NotImplemented
        return (self._ref == other._ref) and (self._fields_pb == other._fields_pb)

    def data(self) -> dict | "Vector" | "BSONType" | bytes | None:
        """
        Retrieves all fields in the result.

        Returns:
            The data in dictionary format, or `None` if the document doesn't exist.
        """
        if self._fields_pb is None:
            return None

        return _helpers.decode_dict(self._fields_pb, self._client)

    def get(self, field_path: str | FieldPath) -> Any:
        """
        Retrieves the field specified by `field_path`.

        Args:
            field_path: The field path (e.g. 'foo' or 'foo.bar') to a specific field.

        Returns:
            The data at the specified field location, decoded to Python types.
        """
        str_path = (
            field_path if isinstance(field_path, str) else field_path.to_api_repr()
        )
        value = get_nested_value(str_path, self._fields_pb)
        return _helpers.decode_value(value, self._client)


T = TypeVar("T", bound=PipelineResult)


class _PipelineResultContainer(Generic[T]):
    """Base class to hold shared attributes for PipelineSnapshot and PipelineStream"""

    def __init__(
        self,
        return_type: Type[T],
        pipeline: Pipeline | AsyncPipeline,
        transaction: Transaction | AsyncTransaction | None,
        read_time: datetime.datetime | None,
        explain_options: PipelineExplainOptions | None,
        additional_options: dict[str, Constant | Value],
    ):
        # public
        self.transaction = transaction
        self.pipeline: Pipeline | AsyncPipeline = pipeline
        self.execution_time: Timestamp | None = None
        # private
        self._client: Client | AsyncClient = pipeline._client
        self._started: bool = False
        self._read_time = read_time
        self._explain_stats: ExplainStats | None = None
        self._explain_options: PipelineExplainOptions | None = explain_options
        self._return_type = return_type
        self._additonal_options = {
            k: v if isinstance(v, Value) else v._to_pb()
            for k, v in additional_options.items()
        }

    @property
    def explain_stats(self) -> ExplainStats:
        if self._explain_stats is not None:
            return self._explain_stats
        elif self._explain_options is None:
            raise QueryExplainError("explain_options not set on query.")
        elif not self._started:
            raise QueryExplainError(
                "explain_stats not available until query is complete"
            )
        else:
            raise QueryExplainError("explain_stats not found")

    def _build_request(self) -> ExecutePipelineRequest:
        """
        shared logic for creating an ExecutePipelineRequest
        """
        database_name = (
            f"projects/{self._client.project}/databases/{self._client._database}"
        )
        transaction_id = (
            _helpers.get_transaction_id(self.transaction, read_operation=False)
            if self.transaction is not None
            else None
        )
        options = {}
        if self._explain_options:
            options["explain_options"] = self._explain_options._to_value()
        if self._additonal_options:
            options.update(self._additonal_options)
        request = ExecutePipelineRequest(
            database=database_name,
            transaction=transaction_id,
            structured_pipeline=self.pipeline._to_pb(**options),
            read_time=self._read_time,
        )
        return request

    def _process_response(self, response: ExecutePipelineResponse) -> Iterable[T]:
        """Shared logic for processing an individual response from a stream"""
        if response.explain_stats:
            self._explain_stats = ExplainStats(response.explain_stats)
        execution_time = response._pb.execution_time
        if execution_time and not self.execution_time:
            self.execution_time = execution_time
        for doc in response.results:
            ref = self._client.document(doc.name) if doc.name else None
            yield self._return_type(
                self._client,
                doc.fields,
                ref,
                execution_time,
                doc._pb.create_time if doc.create_time else None,
                doc._pb.update_time if doc.update_time else None,
            )


class PipelineSnapshot(_PipelineResultContainer[T], List[T]):
    """
    A list type that holds the result of a pipeline.execute() operation, along with related metadata
    """

    def __init__(self, results_list: List[T], source: _PipelineResultContainer[T]):
        self.__dict__.update(source.__dict__.copy())
        list.__init__(self, results_list)
        # snapshots are always complete
        self._started = True


class PipelineStream(_PipelineResultContainer[T], Iterable[T]):
    """
    An iterable stream representing the result of a pipeline.stream() operation, along with related metadata
    """

    def __iter__(self) -> Iterator[T]:
        if self._started:
            raise RuntimeError(f"{self.__class__.__name__} can only be iterated once")
        self._started = True
        request = self._build_request()
        stream = self._client._firestore_api.execute_pipeline(request)
        for response in stream:
            yield from self._process_response(response)


class AsyncPipelineStream(_PipelineResultContainer[T], AsyncIterable[T]):
    """
    An iterable stream representing the result of an async pipeline.stream() operation, along with related metadata
    """

    async def __aiter__(self) -> AsyncIterator[T]:
        if self._started:
            raise RuntimeError(f"{self.__class__.__name__} can only be iterated once")
        self._started = True
        request = self._build_request()
        stream = await self._client._firestore_api.execute_pipeline(request)
        async for response in stream:
            for result in self._process_response(response):
                yield result
