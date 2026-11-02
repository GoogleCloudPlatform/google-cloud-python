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

from typing import TYPE_CHECKING

from google.cloud.firestore_v1 import pipeline_stages as stages
from google.cloud.firestore_v1.base_pipeline import _BasePipeline
from google.cloud.firestore_v1.pipeline_result import (
    AsyncPipelineStream,
    PipelineResult,
    PipelineSnapshot,
)

if TYPE_CHECKING:  # pragma: NO COVER
    import datetime

    from google.cloud.firestore_v1.async_client import AsyncClient
    from google.cloud.firestore_v1.async_transaction import AsyncTransaction
    from google.cloud.firestore_v1.pipeline_expressions import Constant
    from google.cloud.firestore_v1.query_profile import PipelineExplainOptions
    from google.cloud.firestore_v1.types.document import Value


class AsyncPipeline(_BasePipeline):
    """
    Pipelines allow for complex data transformations and queries involving
    multiple stages like filtering, projection, aggregation, and vector search.

    This class extends `_BasePipeline` and provides methods to execute the
    defined pipeline stages using an asynchronous `AsyncClient`.

    Usage Example:
        >>> from google.cloud.firestore_v1.pipeline_expressions import Field
        >>>
        >>> async def run_pipeline():
        ...     client = AsyncClient(...)
        ...     pipeline = client.pipeline()
        ...                      .collection("books")
        ...                      .where(Field.of("published").gt(1980))
        ...                      .select("title", "author")
        ...     async for result in pipeline.stream():
        ...         print(result)

    Use `client.pipeline()` to create instances of this class.


    """

    _client: AsyncClient

    def __init__(self, client: AsyncClient, *stages: stages.Stage):
        """
        Initializes an asynchronous Pipeline.

        Args:
            client: The asynchronous `AsyncClient` instance to use for execution.
            *stages: Initial stages for the pipeline.
        """
        super().__init__(client, *stages)

    async def execute(
        self,
        *,
        transaction: "AsyncTransaction" | None = None,
        read_time: datetime.datetime | None = None,
        explain_options: PipelineExplainOptions | None = None,
        additional_options: dict[str, Value | Constant] = {},
    ) -> PipelineSnapshot[PipelineResult]:
        """
        Executes this pipeline and returns results as a list

        Args:
            transaction (Optional[:class:`~google.cloud.firestore_v1.transaction.Transaction`]):
                An existing transaction that this query will run in.
                If a ``transaction`` is used and it already has write operations
                added, this method cannot be used (i.e. read-after-write is not
                allowed).
            read_time (Optional[datetime.datetime]): If set, reads documents as they were at the given
                time. This must be a microsecond precision timestamp within the past one hour, or
                if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp
                within the past 7 days. For the most accurate results, use UTC timezone.
            explain_options (Optional[:class:`~google.cloud.firestore_v1.query_profile.PipelineExplainOptions`]):
                Options to enable query profiling for this query. When set,
                explain_metrics will be available on the returned list.
            additional_options (Optional[dict[str, Value | Constant]]): Additional options to pass to the query.
                These options will take precedence over method argument if there is a conflict (e.g. explain_options)

        Raises:
            google.api_core.exceptions.GoogleAPIError: If there is a backend error.
        """
        kwargs = {k: v for k, v in locals().items() if k != "self"}
        stream = AsyncPipelineStream(PipelineResult, self, **kwargs)
        results = [result async for result in stream]
        return PipelineSnapshot(results, stream)

    def stream(
        self,
        *,
        read_time: datetime.datetime | None = None,
        transaction: "AsyncTransaction" | None = None,
        explain_options: PipelineExplainOptions | None = None,
        additional_options: dict[str, Value | Constant] = {},
    ) -> AsyncPipelineStream[PipelineResult]:
        """
        Process this pipeline as a stream, providing results through an AsyncIterable

        Args:
            transaction (Optional[:class:`~google.cloud.firestore_v1.transaction.Transaction`]):
                An existing transaction that this query will run in.
                If a ``transaction`` is used and it already has write operations
                added, this method cannot be used (i.e. read-after-write is not
                allowed).
            read_time (Optional[datetime.datetime]): If set, reads documents as they were at the given
                time. This must be a microsecond precision timestamp within the past one hour, or
                if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp
                within the past 7 days. For the most accurate results, use UTC timezone.
            explain_options (Optional[:class:`~google.cloud.firestore_v1.query_profile.PipelineExplainOptions`]):
                Options to enable query profiling for this query. When set,
                explain_metrics will be available on the returned generator.
            additional_options (Optional[dict[str, Value | Constant]]): Additional options to pass to the query.
                These options will take precedence over method argument if there is a conflict (e.g. explain_options)

        Raises:
            google.api_core.exceptions.GoogleAPIError: If there is a backend error.
        """
        kwargs = {k: v for k, v in locals().items() if k != "self"}
        return AsyncPipelineStream(PipelineResult, self, **kwargs)
