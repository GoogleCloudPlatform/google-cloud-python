# Copyright 2023 Google LLC All rights reserved.
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

from datetime import datetime, timedelta, timezone

import pytest

from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator
from google.cloud.firestore_v1.base_aggregation import (
    AggregationResult,
    AvgAggregation,
    CountAggregation,
    SumAggregation,
)
from google.cloud.firestore_v1.field_path import FieldPath
from google.cloud.firestore_v1.query_profile import ExplainMetrics, QueryExplainError
from google.cloud.firestore_v1.query_results import QueryResultsList
from tests.unit.v1._test_helpers import (
    make_aggregation_query_response,
    make_async_aggregation_query,
    make_async_client,
    make_async_query,
)
from tests.unit.v1.test__helpers import AsyncIter, AsyncMock

_PROJECT = "PROJECT"


def test_async_aggregation_query_constructor():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    assert aggregation_query._collection_ref == parent
    assert aggregation_query._nested_query == parent._query()
    assert len(aggregation_query._aggregations) == 0
    assert aggregation_query._client == client


def test_async_aggregation_query_add_aggregation():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.add_aggregation(CountAggregation(alias="all"))
    aggregation_query.add_aggregation(SumAggregation("someref", alias="sum_all"))
    aggregation_query.add_aggregation(AvgAggregation("otherref", alias="avg_all"))

    assert len(aggregation_query._aggregations) == 3

    assert aggregation_query._aggregations[0].alias == "all"
    assert isinstance(aggregation_query._aggregations[0], CountAggregation)

    assert aggregation_query._aggregations[1].field_ref == "someref"
    assert aggregation_query._aggregations[1].alias == "sum_all"
    assert isinstance(aggregation_query._aggregations[1], SumAggregation)

    assert aggregation_query._aggregations[2].field_ref == "otherref"
    assert aggregation_query._aggregations[2].alias == "avg_all"
    assert isinstance(aggregation_query._aggregations[2], AvgAggregation)


def test_async_aggregation_query_add_aggregations():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.add_aggregations(
        [
            CountAggregation(alias="all"),
            CountAggregation(alias="total"),
            SumAggregation("someref", alias="sum_all"),
            AvgAggregation("otherref", alias="avg_all"),
        ]
    )

    assert len(aggregation_query._aggregations) == 4
    assert aggregation_query._aggregations[0].alias == "all"
    assert aggregation_query._aggregations[1].alias == "total"

    assert aggregation_query._aggregations[2].field_ref == "someref"
    assert aggregation_query._aggregations[2].alias == "sum_all"

    assert aggregation_query._aggregations[3].field_ref == "otherref"
    assert aggregation_query._aggregations[3].alias == "avg_all"

    assert isinstance(aggregation_query._aggregations[0], CountAggregation)
    assert isinstance(aggregation_query._aggregations[1], CountAggregation)
    assert isinstance(aggregation_query._aggregations[2], SumAggregation)
    assert isinstance(aggregation_query._aggregations[3], AvgAggregation)


def test_async_aggregation_query_count():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.count(alias="all")

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias == "all"

    assert isinstance(aggregation_query._aggregations[0], CountAggregation)


def test_async_aggregation_query_count_twice():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.count(alias="all").count(alias="total")

    assert len(aggregation_query._aggregations) == 2
    assert aggregation_query._aggregations[0].alias == "all"
    assert aggregation_query._aggregations[1].alias == "total"

    assert isinstance(aggregation_query._aggregations[0], CountAggregation)
    assert isinstance(aggregation_query._aggregations[1], CountAggregation)


def test_async_aggregation_sum():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.sum("someref", alias="sum_all")

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias == "sum_all"
    assert aggregation_query._aggregations[0].field_ref == "someref"

    assert isinstance(aggregation_query._aggregations[0], SumAggregation)


def test_async_aggregation_query_sum_twice():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.sum("someref", alias="sum_all").sum(
        "another_ref", alias="sum_total"
    )

    assert len(aggregation_query._aggregations) == 2
    assert aggregation_query._aggregations[0].alias == "sum_all"
    assert aggregation_query._aggregations[0].field_ref == "someref"
    assert aggregation_query._aggregations[1].alias == "sum_total"
    assert aggregation_query._aggregations[1].field_ref == "another_ref"

    assert isinstance(aggregation_query._aggregations[0], SumAggregation)
    assert isinstance(aggregation_query._aggregations[1], SumAggregation)


def test_async_aggregation_sum_no_alias():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.sum("someref")

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias is None
    assert aggregation_query._aggregations[0].field_ref == "someref"

    assert isinstance(aggregation_query._aggregations[0], SumAggregation)


def test_aggregation_query_avg():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.avg("someref", alias="all")

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias == "all"
    assert aggregation_query._aggregations[0].field_ref == "someref"

    assert isinstance(aggregation_query._aggregations[0], AvgAggregation)


def test_aggregation_query_avg_twice():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.avg("someref", alias="all").avg("another_ref", alias="total")

    assert len(aggregation_query._aggregations) == 2
    assert aggregation_query._aggregations[0].alias == "all"
    assert aggregation_query._aggregations[0].field_ref == "someref"
    assert aggregation_query._aggregations[1].alias == "total"
    assert aggregation_query._aggregations[1].field_ref == "another_ref"

    assert isinstance(aggregation_query._aggregations[0], AvgAggregation)
    assert isinstance(aggregation_query._aggregations[1], AvgAggregation)


def test_aggregation_query_avg_no_alias():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.avg("someref")

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias is None
    assert aggregation_query._aggregations[0].field_ref == "someref"

    assert isinstance(aggregation_query._aggregations[0], AvgAggregation)


def test_async_aggregation_query_to_protobuf():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.count(alias="all")
    aggregation_query.sum("someref", alias="sum_all")
    aggregation_query.avg("someref", alias="avg_all")
    pb = aggregation_query._to_protobuf()

    assert pb.structured_query == parent._query()._to_protobuf()
    assert len(pb.aggregations) == 3
    assert pb.aggregations[0] == aggregation_query._aggregations[0]._to_protobuf()
    assert pb.aggregations[1] == aggregation_query._aggregations[1]._to_protobuf()
    assert pb.aggregations[2] == aggregation_query._aggregations[2]._to_protobuf()


def test_async_aggregation_query_prep_stream():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.count(alias="all")
    aggregation_query.sum("someref", alias="sum_all")
    aggregation_query.avg("someref", alias="avg_all")
    request, kwargs = aggregation_query._prep_stream()

    parent_path, _ = parent._parent_info()
    expected_request = {
        "parent": parent_path,
        "structured_aggregation_query": aggregation_query._to_protobuf(),
        "transaction": None,
    }
    assert request == expected_request
    assert kwargs == {"retry": None}


def test_async_aggregation_query_prep_stream_with_transaction():
    client = make_async_client()
    transaction = client.transaction()
    txn_id = b"\x00\x00\x01-work-\xf2"
    transaction._id = txn_id

    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.count(alias="all")
    aggregation_query.sum("someref", alias="sum_all")
    aggregation_query.avg("someref", alias="avg_all")

    request, kwargs = aggregation_query._prep_stream(transaction=transaction)

    parent_path, _ = parent._parent_info()
    expected_request = {
        "parent": parent_path,
        "structured_aggregation_query": aggregation_query._to_protobuf(),
        "transaction": txn_id,
    }
    assert request == expected_request
    assert kwargs == {"retry": None}


def test_async_aggregation_query_prep_stream_with_explain_options():
    from google.cloud.firestore_v1 import query_profile

    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.count(alias="all")
    aggregation_query.sum("someref", alias="sumall")
    aggregation_query.avg("anotherref", alias="avgall")

    explain_options = query_profile.ExplainOptions(analyze=True)
    request, kwargs = aggregation_query._prep_stream(explain_options=explain_options)

    parent_path, _ = parent._parent_info()
    expected_request = {
        "parent": parent_path,
        "structured_aggregation_query": aggregation_query._to_protobuf(),
        "transaction": None,
        "explain_options": explain_options._to_dict(),
    }
    assert request == expected_request
    assert kwargs == {"retry": None}


def test_async_aggregation_query_prep_stream_with_read_time():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)

    aggregation_query.count(alias="all")
    aggregation_query.sum("someref", alias="sumall")
    aggregation_query.avg("anotherref", alias="avgall")

    # 1800 seconds after epoch
    read_time = datetime.now()

    request, kwargs = aggregation_query._prep_stream(read_time=read_time)

    parent_path, _ = parent._parent_info()
    expected_request = {
        "parent": parent_path,
        "structured_aggregation_query": aggregation_query._to_protobuf(),
        "transaction": None,
        "read_time": read_time,
    }
    assert request == expected_request
    assert kwargs == {"retry": None}


@pytest.mark.asyncio
async def _async_aggregation_query_get_helper(
    retry=None,
    timeout=None,
    explain_options=None,
    response_read_time=None,
    query_read_time=None,
):
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_aggregation_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.count(alias="all")

    aggregation_result = AggregationResult(
        alias="total",
        value=5,
        read_time=response_read_time,
    )

    if explain_options is not None:
        explain_metrics = {"execution_stats": {"results_returned": 1}}
    else:
        explain_metrics = None

    response_pb = make_aggregation_query_response(
        [aggregation_result],
        read_time=response_read_time,
        explain_metrics=explain_metrics,
    )
    firestore_api.run_aggregation_query.return_value = AsyncIter([response_pb])
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Execute the query and check the response.
    returned = await aggregation_query.get(
        **kwargs,
        explain_options=explain_options,
        read_time=query_read_time,
    )
    assert isinstance(returned, QueryResultsList)
    assert len(returned) == 1

    for result in returned:
        for r in result:
            assert r.alias == aggregation_result.alias
            assert r.value == aggregation_result.value
            if response_read_time is not None:
                result_datetime = _datetime_to_pb_timestamp(r.read_time)
                assert result_datetime == response_read_time

    if explain_options is None:
        with pytest.raises(QueryExplainError, match="explain_options not set"):
            returned.get_explain_metrics()
    else:
        explain_metrics = returned.get_explain_metrics()
        assert isinstance(explain_metrics, ExplainMetrics)
        assert explain_metrics.execution_stats.results_returned == 1

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    expected_request = {
        "parent": parent_path,
        "structured_aggregation_query": aggregation_query._to_protobuf(),
        "transaction": None,
    }
    if explain_options is not None:
        expected_request["explain_options"] = explain_options._to_dict()
    if query_read_time is not None:
        expected_request["read_time"] = query_read_time
    firestore_api.run_aggregation_query.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.asyncio
async def test_async_aggregation_query_get():
    await _async_aggregation_query_get_helper()


@pytest.mark.asyncio
async def test_async_aggregation_query_get_with_readtime():
    from google.cloud._helpers import _datetime_to_pb_timestamp

    one_hour_ago = datetime.now(tz=timezone.utc) - timedelta(hours=1)
    read_time = _datetime_to_pb_timestamp(one_hour_ago)
    await _async_aggregation_query_get_helper(
        query_read_time=one_hour_ago, response_read_time=read_time
    )


@pytest.mark.asyncio
async def test_async_aggregation_query_get_with_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    await _async_aggregation_query_get_helper(explain_options=explain_options)


@pytest.mark.asyncio
async def test_async_aggregation_query_get_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    await _async_aggregation_query_get_helper(retry=retry, timeout=timeout)


@pytest.mark.asyncio
async def test_async_aggregation_query_get_transaction():
    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_aggregation_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")

    transaction = client.transaction()

    txn_id = b"\x00\x00\x01-work-\xf2"
    transaction._id = txn_id
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.count(alias="all")

    aggregation_result = AggregationResult(alias="total", value=5)
    response_pb = make_aggregation_query_response(
        [aggregation_result], transaction=txn_id
    )
    firestore_api.run_aggregation_query.return_value = AsyncIter([response_pb])
    retry = None
    timeout = None
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Execute the query and check the response.
    returned = await aggregation_query.get(transaction=transaction, **kwargs)
    assert isinstance(returned, list)
    assert len(returned) == 1

    for result in returned:
        for r in result:
            assert r.alias == aggregation_result.alias
            assert r.value == aggregation_result.value

    # Verify the mock call.
    parent_path, _ = parent._parent_info()

    firestore_api.run_aggregation_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_aggregation_query": aggregation_query._to_protobuf(),
            "transaction": txn_id,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.asyncio
async def test_async_aggregation_from_query():
    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_aggregation_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    query = make_async_query(parent)

    transaction = client.transaction()

    txn_id = b"\x00\x00\x01-work-\xf2"
    transaction._id = txn_id

    aggregation_result = AggregationResult(alias="total", value=5)
    response_pb = make_aggregation_query_response(
        [aggregation_result], transaction=txn_id
    )
    retry = None
    timeout = None
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Execute each aggregation query type and check the response.
    for aggregation_query in [
        query.count(alias="total"),
        query.sum("foo", alias="total"),
        query.avg("foo", alias="total"),
    ]:
        # reset api mock
        firestore_api.run_aggregation_query.reset_mock()
        firestore_api.run_aggregation_query.return_value = AsyncIter([response_pb])
        # run query
        returned = await aggregation_query.get(transaction=transaction, **kwargs)
        assert isinstance(returned, list)
        assert len(returned) == 1

        for result in returned:
            for r in result:
                assert r.alias == aggregation_result.alias
                assert r.value == aggregation_result.value

        # Verify the mock call.
        parent_path, _ = parent._parent_info()

        firestore_api.run_aggregation_query.assert_called_once_with(
            request={
                "parent": parent_path,
                "structured_aggregation_query": aggregation_query._to_protobuf(),
                "transaction": txn_id,
            },
            metadata=client._rpc_metadata,
            **kwargs,
        )


async def _async_aggregation_query_stream_helper(
    retry=None,
    timeout=None,
    read_time=None,
    explain_options=None,
):
    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_aggregation_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.count(alias="all")

    if explain_options and explain_options.analyze is True:
        aggregation_result = AggregationResult(
            alias="total", value=5, read_time=read_time
        )
        results_list = [aggregation_result]
    else:
        results_list = []

    if explain_options is not None:
        explain_metrics = {"execution_stats": {"results_returned": 1}}
    else:
        explain_metrics = None
    response_pb = make_aggregation_query_response(
        results_list,
        read_time=read_time,
        explain_metrics=explain_metrics,
    )
    firestore_api.run_aggregation_query.return_value = AsyncIter([response_pb])
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Execute the query and check the response.
    returned = aggregation_query.stream(
        **kwargs,
        explain_options=explain_options,
        read_time=read_time,
    )
    assert isinstance(returned, AsyncStreamGenerator)

    results = []
    async for result in returned:
        for r in result:
            assert r.alias == aggregation_result.alias
            assert r.value == aggregation_result.value
        results.append(result)
    await returned.aclose()
    assert len(results) == len(results_list)

    if explain_options is None:
        with pytest.raises(QueryExplainError, match="explain_options not set"):
            await returned.get_explain_metrics()
    else:
        explain_metrics = await returned.get_explain_metrics()
        assert isinstance(explain_metrics, ExplainMetrics)
        assert explain_metrics.execution_stats.results_returned == 1

    parent_path, _ = parent._parent_info()
    expected_request = {
        "parent": parent_path,
        "structured_aggregation_query": aggregation_query._to_protobuf(),
        "transaction": None,
    }
    if explain_options is not None:
        expected_request["explain_options"] = explain_options._to_dict()
    if read_time is not None:
        expected_request["read_time"] = read_time

    # Verify the mock call.
    firestore_api.run_aggregation_query.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.asyncio
async def test_aggregation_query_stream():
    await _async_aggregation_query_stream_helper()


@pytest.mark.asyncio
async def test_async_aggregation_query_stream_with_read_time():
    from google.cloud._helpers import _datetime_to_pb_timestamp

    one_hour_ago = datetime.now(tz=timezone.utc) - timedelta(hours=1)
    read_time = _datetime_to_pb_timestamp(one_hour_ago)
    await _async_aggregation_query_stream_helper(read_time=read_time)


@pytest.mark.asyncio
async def test_aggregation_query_stream_w_explain_options_analyze_true():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    await _async_aggregation_query_stream_helper(explain_options=explain_options)


@pytest.mark.asyncio
async def test_aggregation_query_stream_w_explain_options_analyze_false():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=False)
    await _async_aggregation_query_stream_helper(explain_options=explain_options)


@pytest.mark.parametrize(
    "field,in_alias,out_alias",
    [
        ("field", None, "field_1"),
        (FieldPath("test"), None, "field_1"),
        ("field", "overwrite", "overwrite"),
    ],
)
def test_async_aggreation_to_pipeline_sum(field, in_alias, out_alias):
    from google.cloud.firestore_v1.async_pipeline import AsyncPipeline
    from google.cloud.firestore_v1.pipeline_stages import Aggregate, Collection

    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.sum(field, alias=in_alias)
    pipeline = aggregation_query._build_pipeline(client.pipeline())
    assert isinstance(pipeline, AsyncPipeline)
    assert len(pipeline.stages) == 2
    assert isinstance(pipeline.stages[0], Collection)
    assert pipeline.stages[0].path == "/dee"
    aggregate_stage = pipeline.stages[1]
    assert isinstance(aggregate_stage, Aggregate)
    assert len(aggregate_stage.accumulators) == 1
    assert aggregate_stage.accumulators[0].expr.name == "sum"
    expected_field = field if isinstance(field, str) else field.to_api_repr()
    assert aggregate_stage.accumulators[0].expr.params[0].path == expected_field
    assert aggregate_stage.accumulators[0].alias == out_alias


@pytest.mark.parametrize(
    "field,in_alias,out_alias",
    [
        ("field", None, "field_1"),
        (FieldPath("test"), None, "field_1"),
        ("field", "overwrite", "overwrite"),
    ],
)
def test_async_aggreation_to_pipeline_avg(field, in_alias, out_alias):
    from google.cloud.firestore_v1.async_pipeline import AsyncPipeline
    from google.cloud.firestore_v1.pipeline_stages import Aggregate, Collection

    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.avg(field, alias=in_alias)
    pipeline = aggregation_query._build_pipeline(client.pipeline())
    assert isinstance(pipeline, AsyncPipeline)
    assert len(pipeline.stages) == 2
    assert isinstance(pipeline.stages[0], Collection)
    assert pipeline.stages[0].path == "/dee"
    aggregate_stage = pipeline.stages[1]
    assert isinstance(aggregate_stage, Aggregate)
    assert len(aggregate_stage.accumulators) == 1
    assert aggregate_stage.accumulators[0].expr.name == "average"
    expected_field = field if isinstance(field, str) else field.to_api_repr()
    assert aggregate_stage.accumulators[0].expr.params[0].path == expected_field
    assert aggregate_stage.accumulators[0].alias == out_alias


@pytest.mark.parametrize(
    "in_alias,out_alias",
    [
        (None, "field_1"),
        ("overwrite", "overwrite"),
    ],
)
def test_async_aggreation_to_pipeline_count(in_alias, out_alias):
    from google.cloud.firestore_v1.async_pipeline import AsyncPipeline
    from google.cloud.firestore_v1.pipeline_expressions import Count
    from google.cloud.firestore_v1.pipeline_stages import Aggregate, Collection

    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.count(alias=in_alias)
    pipeline = aggregation_query._build_pipeline(client.pipeline())
    assert isinstance(pipeline, AsyncPipeline)
    assert len(pipeline.stages) == 2
    assert isinstance(pipeline.stages[0], Collection)
    assert pipeline.stages[0].path == "/dee"
    aggregate_stage = pipeline.stages[1]
    assert isinstance(aggregate_stage, Aggregate)
    assert len(aggregate_stage.accumulators) == 1
    assert isinstance(aggregate_stage.accumulators[0].expr, Count)
    assert aggregate_stage.accumulators[0].alias == out_alias


def test_aggreation_to_pipeline_count_increment():
    """
    When aliases aren't given, should assign incrementing field_n values
    """
    from google.cloud.firestore_v1.pipeline_expressions import Count

    n = 100
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    aggregation_query = make_async_aggregation_query(query)
    for _ in range(n):
        aggregation_query.count()
    pipeline = aggregation_query._build_pipeline(client.pipeline())
    aggregate_stage = pipeline.stages[1]
    assert len(aggregate_stage.accumulators) == n
    for i in range(n):
        assert isinstance(aggregate_stage.accumulators[i].expr, Count)
        assert aggregate_stage.accumulators[i].alias == f"field_{i + 1}"


def test_async_aggreation_to_pipeline_complex():
    from google.cloud.firestore_v1.async_pipeline import AsyncPipeline
    from google.cloud.firestore_v1.pipeline_stages import Aggregate, Collection, Select

    client = make_async_client()
    query = client.collection("my_col").select(["field_a", "field_b.c"])
    aggregation_query = make_async_aggregation_query(query)
    aggregation_query.sum("field", alias="alias")
    aggregation_query.count()
    aggregation_query.avg("other")
    aggregation_query.sum("final")
    pipeline = aggregation_query._build_pipeline(client.pipeline())
    assert isinstance(pipeline, AsyncPipeline)
    assert len(pipeline.stages) == 3
    assert isinstance(pipeline.stages[0], Collection)
    assert isinstance(pipeline.stages[1], Select)
    assert isinstance(pipeline.stages[2], Aggregate)
    aggregate_stage = pipeline.stages[2]
    assert len(aggregate_stage.accumulators) == 4
    assert aggregate_stage.accumulators[0].expr.name == "sum"
    assert aggregate_stage.accumulators[0].alias == "alias"
    assert aggregate_stage.accumulators[1].expr.name == "count"
    assert aggregate_stage.accumulators[1].alias == "field_1"
    assert aggregate_stage.accumulators[2].expr.name == "average"
    assert aggregate_stage.accumulators[2].alias == "field_2"
    assert aggregate_stage.accumulators[3].expr.name == "sum"
    assert aggregate_stage.accumulators[3].alias == "field_3"
