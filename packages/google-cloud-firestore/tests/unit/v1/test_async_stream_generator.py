# Copyright 2024 Google LLC All rights reserved.
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

import pytest
from google.protobuf import struct_pb2


def _make_async_stream_generator(iterable, explain_options=None):
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    async def _inner_generator():
        for i in iterable:
            X = yield i
            if X:
                yield X
        # return explain_metrics

    return AsyncStreamGenerator(_inner_generator(), explain_options)


@pytest.mark.asyncio
async def test_async_stream_generator_aiter():
    expected_results = [0, 1, 2]
    inst = _make_async_stream_generator(expected_results)

    actual_results = []
    async for result in inst:
        actual_results.append(result)

    assert expected_results == actual_results


@pytest.mark.asyncio
async def test_async_stream_generator_anext():
    expected_results = [0, 1]
    inst = _make_async_stream_generator(expected_results)

    actual_results = []

    # Use inst.__anext__() instead of anext(inst), because built-in anext()
    # was introduced in Python 3.10.
    actual_results.append(await inst.__anext__())
    actual_results.append(await inst.__anext__())

    with pytest.raises(StopAsyncIteration):
        await inst.__anext__()

    assert expected_results == actual_results


@pytest.mark.asyncio
async def test_async_stream_generator_asend():
    expected_results = [0, 1]
    inst = _make_async_stream_generator(expected_results)

    actual_results = []

    # Use inst.__anext__() instead of anext(inst), because built-in anext()
    # was introduced in Python 3.10.
    actual_results.append(await inst.__anext__())
    assert await inst.asend(2) == 2
    actual_results.append(await inst.__anext__())

    with pytest.raises(StopAsyncIteration):
        await inst.__anext__()

    assert expected_results == actual_results


@pytest.mark.asyncio
async def test_async_stream_generator_athrow():
    inst = _make_async_stream_generator([])
    with pytest.raises(ValueError):
        await inst.athrow(ValueError)


@pytest.mark.asyncio
async def test_async_stream_generator_aclose():
    expected_results = [0, 1]
    inst = _make_async_stream_generator(expected_results)

    await inst.aclose()

    # Verifies that generator is closed.
    with pytest.raises(StopAsyncIteration):
        await inst.__anext__()


def test_async_stream_generator_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    inst = _make_async_stream_generator([], explain_options)
    assert inst.explain_options == explain_options


@pytest.mark.asyncio
async def test_async_stream_generator_explain_metrics_explain_options_analyze_true():
    from google.protobuf import duration_pb2, struct_pb2

    import google.cloud.firestore_v1.query_profile as query_profile
    import google.cloud.firestore_v1.types.query_profile as query_profile_pb2

    indexes_used_dict = {
        "indexes_used": struct_pb2.Value(
            struct_value=struct_pb2.Struct(
                fields={
                    "query_scope": struct_pb2.Value(string_value="Collection"),
                    "properties": struct_pb2.Value(
                        string_value="(foo ASC, **name** ASC)"
                    ),
                }
            )
        )
    }
    plan_summary = query_profile_pb2.PlanSummary()
    plan_summary.indexes_used.append(indexes_used_dict)
    execution_stats = query_profile_pb2.ExecutionStats(
        {
            "results_returned": 1,
            "execution_duration": duration_pb2.Duration(seconds=2),
            "read_operations": 3,
            "debug_stats": struct_pb2.Struct(
                fields={
                    "billing_details": struct_pb2.Value(
                        string_value="billing_details_results"
                    ),
                    "documents_scanned": struct_pb2.Value(
                        string_value="documents_scanned_results"
                    ),
                    "index_entries_scanned": struct_pb2.Value(
                        string_value="index_entries_scanned"
                    ),
                }
            ),
        }
    )

    explain_options = query_profile.ExplainOptions(analyze=True)
    expected_explain_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=plan_summary,
        execution_stats=execution_stats,
    )
    iterator = [1, 2, expected_explain_metrics]

    inst = _make_async_stream_generator(iterator, explain_options)

    # Raise an exception if query isn't complete when explain_metrics is called.
    with pytest.raises(
        query_profile.QueryExplainError,
        match="explain_metrics not available until query is complete.",
    ):
        await inst.get_explain_metrics()

    results = [doc async for doc in inst]
    assert len(results) == 2

    actual_explain_metrics = await inst.get_explain_metrics()
    assert isinstance(actual_explain_metrics, query_profile._ExplainAnalyzeMetrics)
    assert actual_explain_metrics == query_profile.ExplainMetrics._from_pb(
        expected_explain_metrics
    )
    assert actual_explain_metrics.plan_summary.indexes_used == [
        {
            "indexes_used": {
                "query_scope": "Collection",
                "properties": "(foo ASC, **name** ASC)",
            }
        }
    ]
    assert actual_explain_metrics.execution_stats.results_returned == 1
    duration = actual_explain_metrics.execution_stats.execution_duration.total_seconds()
    assert duration == 2
    assert actual_explain_metrics.execution_stats.read_operations == 3

    expected_debug_stats = {
        "billing_details": "billing_details_results",
        "documents_scanned": "documents_scanned_results",
        "index_entries_scanned": "index_entries_scanned",
    }
    assert actual_explain_metrics.execution_stats.debug_stats == expected_debug_stats
    await inst.aclose()


@pytest.mark.asyncio
async def test_async_stream_generator_explain_metrics_explain_options_analyze_false():
    import google.cloud.firestore_v1.query_profile as query_profile
    import google.cloud.firestore_v1.types.query_profile as query_profile_pb2

    explain_options = query_profile.ExplainOptions(analyze=False)
    indexes_used_dict = {
        "indexes_used": struct_pb2.Value(
            struct_value=struct_pb2.Struct(
                fields={
                    "query_scope": struct_pb2.Value(string_value="Collection"),
                    "properties": struct_pb2.Value(
                        string_value="(foo ASC, **name** ASC)"
                    ),
                }
            )
        )
    }
    plan_summary = query_profile_pb2.PlanSummary()
    plan_summary.indexes_used.append(indexes_used_dict)
    expected_explain_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=plan_summary
    )
    iterator = [expected_explain_metrics]

    inst = _make_async_stream_generator(iterator, explain_options)
    actual_explain_metrics = await inst.get_explain_metrics()
    assert isinstance(actual_explain_metrics, query_profile.ExplainMetrics)
    assert actual_explain_metrics.plan_summary.indexes_used == [
        {
            "indexes_used": {
                "query_scope": "Collection",
                "properties": "(foo ASC, **name** ASC)",
            }
        }
    ]
    await inst.aclose()


@pytest.mark.asyncio
async def test_async_stream_generator_explain_metrics_missing_explain_options_analyze_false():
    import google.cloud.firestore_v1.query_profile as query_profile

    explain_options = query_profile.ExplainOptions(analyze=False)
    inst = _make_async_stream_generator([("1", None)], explain_options)
    with pytest.raises(
        query_profile.QueryExplainError, match="Did not receive explain_metrics"
    ):
        await inst.get_explain_metrics()
    await inst.aclose()


@pytest.mark.asyncio
async def test_stream_generator_explain_metrics_no_explain_options():
    from google.cloud.firestore_v1.query_profile import QueryExplainError

    inst = _make_async_stream_generator([])

    with pytest.raises(
        QueryExplainError,
        match="explain_options not set on query.",
    ):
        await inst.get_explain_metrics()
