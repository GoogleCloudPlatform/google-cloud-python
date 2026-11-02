# Copyright 2022 Google LLC
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

import mock
import pytest

from google.cloud.datastore.aggregation import (
    AggregationQuery,
    AvgAggregation,
    CountAggregation,
    SumAggregation,
)
from google.cloud.datastore.helpers import set_database_id_to_request
from tests.unit.test_query import _make_client, _make_query

_PROJECT = "PROJECT"


def test_count_aggregation_to_pb():
    from google.cloud.datastore_v1.types import query as query_pb2

    count_aggregation = CountAggregation(alias="total")

    expected_aggregation_query_pb = query_pb2.AggregationQuery.Aggregation()
    expected_aggregation_query_pb.count = query_pb2.AggregationQuery.Aggregation.Count()
    expected_aggregation_query_pb.alias = count_aggregation.alias
    assert count_aggregation._to_pb() == expected_aggregation_query_pb


def test_sum_aggregation_to_pb():
    from google.cloud.datastore_v1.types import query as query_pb2

    sum_aggregation = SumAggregation("appearances", alias="total")

    expected_aggregation_query_pb = query_pb2.AggregationQuery.Aggregation()
    expected_aggregation_query_pb.sum = query_pb2.AggregationQuery.Aggregation.Sum()
    expected_aggregation_query_pb.sum.property.name = sum_aggregation.property_ref
    expected_aggregation_query_pb.alias = sum_aggregation.alias
    assert sum_aggregation._to_pb() == expected_aggregation_query_pb


def test_avg_aggregation_to_pb():
    from google.cloud.datastore_v1.types import query as query_pb2

    avg_aggregation = AvgAggregation("appearances", alias="total")

    expected_aggregation_query_pb = query_pb2.AggregationQuery.Aggregation()
    expected_aggregation_query_pb.avg = query_pb2.AggregationQuery.Aggregation.Avg()
    expected_aggregation_query_pb.avg.property.name = avg_aggregation.property_ref
    expected_aggregation_query_pb.alias = avg_aggregation.alias
    assert avg_aggregation._to_pb() == expected_aggregation_query_pb


@pytest.fixture
def database_id(request):
    return request.param


@pytest.fixture
def client(database_id):
    return _make_client(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_project(client, database_id):
    # Fallback to client
    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)
    assert aggregation_query.project == _PROJECT

    # Fallback to query
    query = _make_query(client, project="other-project")
    aggregation_query = _make_aggregation_query(client=client, query=query)
    assert aggregation_query.project == "other-project"


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_namespace(client, database_id):
    # Fallback to client
    client.namespace = "other-namespace"
    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)
    assert aggregation_query.namespace == "other-namespace"

    # Fallback to query
    query = _make_query(client, namespace="third-namespace")
    aggregation_query = _make_aggregation_query(client=client, query=query)
    assert aggregation_query.namespace == "third-namespace"


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert pb.aggregations == []


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query_with_count(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    aggregation_query.count(alias="total")
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert len(pb.aggregations) == 1
    assert pb.aggregations[0] == CountAggregation(alias="total")._to_pb()


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query_with_add_aggregation(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    aggregation_query.add_aggregation(CountAggregation(alias="total"))
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert len(pb.aggregations) == 1
    assert pb.aggregations[0] == CountAggregation(alias="total")._to_pb()


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query_with_add_aggregations(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    aggregations = [
        CountAggregation(alias="total"),
        CountAggregation(alias="all"),
        SumAggregation("appearances", alias="sum_appearances"),
        AvgAggregation("appearances", alias="avg_appearances"),
    ]

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    aggregation_query.add_aggregations(aggregations)
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert len(pb.aggregations) == 4
    assert pb.aggregations[0] == CountAggregation(alias="total")._to_pb()
    assert pb.aggregations[1] == CountAggregation(alias="all")._to_pb()
    assert (
        pb.aggregations[2]
        == SumAggregation("appearances", alias="sum_appearances")._to_pb()
    )
    assert (
        pb.aggregations[3]
        == AvgAggregation("appearances", alias="avg_appearances")._to_pb()
    )


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query_with_sum(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    aggregation_query.sum("appearances", alias="total")
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert len(pb.aggregations) == 1
    assert pb.aggregations[0] == SumAggregation("appearances", alias="total")._to_pb()


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query_sum_with_add_aggregation(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    aggregation_query.add_aggregation(SumAggregation("appearances", alias="total"))
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert len(pb.aggregations) == 1
    assert pb.aggregations[0] == SumAggregation("appearances", alias="total")._to_pb()


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query_with_avg(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    aggregation_query.avg("appearances", alias="avg")
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert len(pb.aggregations) == 1
    assert pb.aggregations[0] == AvgAggregation("appearances", alias="avg")._to_pb()


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_pb_over_query_avg_with_add_aggregation(client, database_id):
    from google.cloud.datastore.query import _pb_from_query

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    aggregation_query.add_aggregation(AvgAggregation("appearances", alias="avg"))
    pb = aggregation_query._to_pb()
    assert pb.nested_query == _pb_from_query(query)
    assert len(pb.aggregations) == 1
    assert pb.aggregations[0] == AvgAggregation("appearances", alias="avg")._to_pb()


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_query_fetch_defaults_w_client_attr(client, database_id):
    from google.cloud.datastore.aggregation import AggregationResultIterator

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)
    iterator = aggregation_query.fetch()

    assert isinstance(iterator, AggregationResultIterator)
    assert iterator._aggregation_query is aggregation_query
    assert iterator.client is client
    assert iterator._retry is None
    assert iterator._timeout is None


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_query_fetch_w_explicit_client_w_retry_w_timeout(client, database_id):
    from google.cloud.datastore.aggregation import AggregationResultIterator

    other_client = _make_client(database=database_id)
    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)
    retry = mock.Mock()
    timeout = 100000

    iterator = aggregation_query.fetch(
        client=other_client, retry=retry, timeout=timeout
    )

    assert isinstance(iterator, AggregationResultIterator)
    assert iterator._aggregation_query is aggregation_query
    assert iterator.client is other_client
    assert iterator._retry == retry
    assert iterator._timeout == timeout


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_query_fetch_w_explicit_client_w_limit(client, database_id):
    from google.cloud.datastore.aggregation import AggregationResultIterator

    other_client = _make_client(database=database_id)
    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)
    limit = 2

    iterator = aggregation_query.fetch(client=other_client, limit=limit)

    assert isinstance(iterator, AggregationResultIterator)
    assert iterator._aggregation_query is aggregation_query
    assert iterator.client is other_client
    assert iterator._limit == limit


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
def test_aggregation_uses_nested_query_explain_options(client, database_id):
    """
    If explain_options is set on the nested query but not the aggregation,
    use the nested query's explain_options.
    """
    expected_explain_options = mock.Mock()
    query = _make_query(client, explain_options=expected_explain_options)
    aggregation_query = _make_aggregation_query(
        client=client, query=query, explain_options=None
    )
    assert aggregation_query._explain_options is expected_explain_options


def test_iterator_constructor_defaults():
    query = mock.Mock()
    client = object()
    aggregation_query = AggregationQuery(client=client, query=query)
    assert aggregation_query._explain_options == query._explain_options
    iterator = _make_aggregation_iterator(aggregation_query, client)

    assert not iterator._started
    assert iterator.client is client
    assert iterator.page_number == 0
    assert iterator.num_results == 0
    assert iterator._aggregation_query is aggregation_query
    assert iterator._more_results
    assert iterator._retry is None
    assert iterator._timeout is None
    assert iterator._explain_metrics is None


def test_iterator_constructor_explicit():
    query = object()
    client = object()
    explain_options = object()
    aggregation_query = AggregationQuery(
        client=client, query=query, explain_options=explain_options
    )
    assert aggregation_query._explain_options is explain_options
    retry = mock.Mock()
    timeout = 100000
    limit = 2

    iterator = _make_aggregation_iterator(
        aggregation_query, client, retry=retry, timeout=timeout, limit=limit
    )

    assert not iterator._started
    assert iterator.client is client
    assert iterator.page_number == 0
    assert iterator.num_results == 0
    assert iterator._aggregation_query is aggregation_query
    assert iterator._more_results
    assert iterator._retry == retry
    assert iterator._timeout == timeout
    assert iterator._limit == limit
    assert iterator._explain_metrics is None


def test_iterator__build_protobuf_empty():
    from google.cloud.datastore_v1.types import query as query_pb2

    client = _Client(None)
    query = _make_query(client)
    aggregation_query = AggregationQuery(client=client, query=query)
    iterator = _make_aggregation_iterator(aggregation_query, client)

    pb = iterator._build_protobuf()
    expected_pb = query_pb2.AggregationQuery()
    expected_pb.nested_query = query_pb2.Query()
    assert pb == expected_pb


def test_iterator__build_protobuf_all_values():
    from google.cloud.datastore_v1.types import query as query_pb2

    client = _Client(None)
    query = _make_query(client)
    alias = "total"
    limit = 2
    property_ref = "appearances"
    aggregation_query = AggregationQuery(client=client, query=query)
    aggregation_query.count(alias)
    aggregation_query.sum(property_ref)
    aggregation_query.avg(property_ref)

    iterator = _make_aggregation_iterator(aggregation_query, client, limit=limit)
    iterator.num_results = 4

    pb = iterator._build_protobuf()
    expected_pb = query_pb2.AggregationQuery()
    expected_pb.nested_query = query_pb2.Query()
    expected_pb.nested_query.limit = limit

    expected_count_pb = query_pb2.AggregationQuery.Aggregation(alias=alias)
    expected_count_pb.count = query_pb2.AggregationQuery.Aggregation.Count()
    expected_pb.aggregations.append(expected_count_pb)

    expected_sum_pb = query_pb2.AggregationQuery.Aggregation()
    expected_sum_pb.sum = query_pb2.AggregationQuery.Aggregation.Sum()
    expected_sum_pb.sum.property.name = property_ref
    expected_pb.aggregations.append(expected_sum_pb)

    expected_avg_pb = query_pb2.AggregationQuery.Aggregation()
    expected_avg_pb.avg = query_pb2.AggregationQuery.Aggregation.Avg()
    expected_avg_pb.avg.property.name = property_ref
    expected_pb.aggregations.append(expected_avg_pb)

    assert pb == expected_pb


def test_iterator__process_query_results():
    from google.cloud.datastore.aggregation import AggregationResult
    from google.cloud.datastore_v1.types import query as query_pb2

    iterator = _make_aggregation_iterator(None, None)

    aggregation_pbs = [AggregationResult(alias="total", value=1)]

    more_results_enum = query_pb2.QueryResultBatch.MoreResultsType.NOT_FINISHED
    response_pb = _make_aggregation_query_response(aggregation_pbs, more_results_enum)
    result = iterator._process_query_results(response_pb)
    assert result == [
        r.aggregate_properties for r in response_pb.batch.aggregation_results
    ]
    assert iterator._more_results


def test_iterator__process_query_results_finished_result():
    from google.cloud.datastore.aggregation import AggregationResult
    from google.cloud.datastore_v1.types import query as query_pb2

    iterator = _make_aggregation_iterator(None, None)

    aggregation_pbs = [AggregationResult(alias="total", value=1)]

    more_results_enum = query_pb2.QueryResultBatch.MoreResultsType.NO_MORE_RESULTS
    response_pb = _make_aggregation_query_response(aggregation_pbs, more_results_enum)
    result = iterator._process_query_results(response_pb)
    assert result == [
        r.aggregate_properties for r in response_pb.batch.aggregation_results
    ]
    assert iterator._more_results is False


def test_iterator__process_query_results_unexpected_result():
    from google.cloud.datastore.aggregation import AggregationResult

    iterator = _make_aggregation_iterator(None, None)

    aggregation_pbs = [AggregationResult(alias="total", value=1)]

    more_results_enum = 999
    response_pb = _make_aggregation_query_response(aggregation_pbs, more_results_enum)
    with pytest.raises(ValueError):
        iterator._process_query_results(response_pb)


def test_aggregation_iterator__next_page():
    _next_page_helper()


def test_iterator__next_page_w_retry():
    retry = mock.Mock()
    _next_page_helper(retry=retry)


def test_iterator__next_page_w_timeout():
    _next_page_helper(timeout=100000)


def test_iterator__next_page_in_transaction():
    txn_id = b"1xo1md\xe2\x98\x83"
    _next_page_helper(txn_id=txn_id)


def test_iterator__next_page_no_more():
    from google.cloud.datastore.query import Query

    ds_api = _make_datastore_api_for_aggregation()
    client = _Client(None, datastore_api=ds_api)
    query = Query(client)

    iterator = _make_aggregation_iterator(query, client)
    iterator._more_results = False
    page = iterator._next_page()
    assert page is None
    ds_api.run_aggregation_query.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
@pytest.mark.parametrize("analyze", [True, False])
def test_iterator_sends_explain_options_w_request(database_id, analyze):
    """
    When query has explain_options set, all requests should include
    the explain_options field.
    """
    from google.cloud.datastore.query_profile import ExplainOptions

    response_pb = _make_aggregation_query_response([], 0)
    ds_api = _make_datastore_api_for_aggregation(response_pb)
    client = _Client(None, datastore_api=ds_api)
    explain_options = ExplainOptions(analyze=analyze)
    query = _make_aggregation_query(
        client, _make_query(client), explain_options=explain_options
    )
    iterator = _make_aggregation_iterator(query, client)
    iterator._next_page()
    # ensure explain_options is set in request
    assert ds_api.run_aggregation_query.call_count == 1
    found_explain_options = ds_api.run_aggregation_query.call_args[1]["request"][
        "explain_options"
    ]
    assert found_explain_options == explain_options._to_dict()
    assert found_explain_options["analyze"] == analyze


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics(database_id):
    """
    If explain_metrics is recieved from backend, it should be set on the iterator
    """
    from google.protobuf import duration_pb2

    from google.cloud.datastore.query_profile import ExplainMetrics
    from google.cloud.datastore_v1.types import query_profile as query_profile_pb2

    expected_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=query_profile_pb2.PlanSummary(),
        execution_stats=query_profile_pb2.ExecutionStats(
            results_returned=100,
            execution_duration=duration_pb2.Duration(seconds=1),
            read_operations=10,
            debug_stats={},
        ),
    )
    response_pb = _make_aggregation_query_response([], 0)
    response_pb.explain_metrics = expected_metrics
    ds_api = _make_datastore_api_for_aggregation(response_pb)
    client = _Client(None, datastore_api=ds_api)
    query = _make_aggregation_query(client=client, query=_make_query(client))
    iterator = _make_aggregation_iterator(query, client)
    assert iterator._explain_metrics is None
    iterator._next_page()
    assert isinstance(iterator._explain_metrics, ExplainMetrics)
    assert iterator._explain_metrics == ExplainMetrics._from_pb(expected_metrics)
    assert iterator.explain_metrics == ExplainMetrics._from_pb(expected_metrics)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics_no_explain(database_id):
    """
    If query has no explain_options set, iterator.explain_metrics should raise
    an exception.
    """
    from google.cloud.datastore.query_profile import QueryExplainError

    ds_api = _make_datastore_api_for_aggregation()
    client = _Client(None, datastore_api=ds_api)
    query = _make_aggregation_query(client, _make_query(client), explain_options=None)
    iterator = _make_aggregation_iterator(query, client)
    assert iterator._explain_metrics is None
    with pytest.raises(QueryExplainError) as exc:
        iterator.explain_metrics
    assert "explain_options not set on query" in str(exc.value)
    # should not raise error if field is set
    iterator._explain_metrics = object()
    assert iterator.explain_metrics is iterator._explain_metrics


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics_no_analyze_make_call(database_id):
    """
    If query.explain_options(analyze=False), accessing iterator.explain_metrics
    should make a network call to get the data.
    """
    from google.protobuf import duration_pb2

    from google.cloud.datastore.query_profile import ExplainMetrics, ExplainOptions
    from google.cloud.datastore_v1.types import query_profile as query_profile_pb2

    response_pb = _make_aggregation_query_response([], 0)
    expected_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=query_profile_pb2.PlanSummary(),
        execution_stats=query_profile_pb2.ExecutionStats(
            results_returned=100,
            execution_duration=duration_pb2.Duration(seconds=1),
            read_operations=10,
            debug_stats={},
        ),
    )
    response_pb.explain_metrics = expected_metrics
    ds_api = _make_datastore_api_for_aggregation(response_pb)
    client = _Client(None, datastore_api=ds_api)
    explain_options = ExplainOptions(analyze=False)
    query = _make_aggregation_query(
        client, _make_query(client), explain_options=explain_options
    )
    iterator = _make_aggregation_iterator(query, client)
    assert ds_api.run_aggregation_query.call_count == 0
    metrics = iterator.explain_metrics
    # ensure explain_options is set in request
    assert ds_api.run_aggregation_query.call_count == 1
    assert isinstance(metrics, ExplainMetrics)
    assert metrics == ExplainMetrics._from_pb(expected_metrics)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics_no_analyze_make_call_failed(database_id):
    """
    If query.explain_options(analyze=False), accessing iterator.explain_metrics
    should make a network call to get the data.
    If the call does not result in explain_metrics data, it should raise a QueryExplainError.
    """
    from google.cloud.datastore.query_profile import ExplainOptions, QueryExplainError

    # mocked response does not return explain_metrics
    response_pb = _make_aggregation_query_response([], 0)
    ds_api = _make_datastore_api_for_aggregation(response_pb)
    client = _Client(None, datastore_api=ds_api)
    explain_options = ExplainOptions(analyze=False)
    query = _make_aggregation_query(
        client, _make_query(client), explain_options=explain_options
    )
    iterator = _make_aggregation_iterator(query, client)
    assert ds_api.run_aggregation_query.call_count == 0
    with pytest.raises(QueryExplainError):
        iterator.explain_metrics
    assert ds_api.run_aggregation_query.call_count == 1


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_analyze_access_before_complete(database_id):
    """
    If query.explain_options(analyze=True), accessing iterator.explain_metrics
    before the query is complete should raise an exception.
    """
    from google.cloud.datastore.query_profile import ExplainOptions, QueryExplainError

    ds_api = _make_datastore_api_for_aggregation()
    client = _Client(None, datastore_api=ds_api)
    explain_options = ExplainOptions(analyze=True)
    query = _make_aggregation_query(
        client, _make_query(client), explain_options=explain_options
    )
    iterator = _make_aggregation_iterator(query, client)
    expected_error = "explain_metrics not available until query is complete"
    with pytest.raises(QueryExplainError) as exc:
        iterator.explain_metrics
    assert expected_error in str(exc.value)


def _next_page_helper(txn_id=None, retry=None, timeout=None, database_id=None):
    from google.api_core import page_iterator

    from google.cloud.datastore.aggregation import AggregationResult
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2
    from google.cloud.datastore_v1.types import query as query_pb2

    more_enum = query_pb2.QueryResultBatch.MoreResultsType.NOT_FINISHED
    aggregation_pbs = [AggregationResult(alias="total", value=1)]

    result_1 = _make_aggregation_query_response([], more_enum)
    result_2 = _make_aggregation_query_response(
        aggregation_pbs, query_pb2.QueryResultBatch.MoreResultsType.NO_MORE_RESULTS
    )

    project = "prujekt"
    ds_api = _make_datastore_api_for_aggregation(result_1, result_2)
    if txn_id is None:
        client = _Client(project, datastore_api=ds_api, database=database_id)
    else:
        transaction = mock.Mock(
            id=txn_id, _begin_later=False, spec=["id", "_begin_later"]
        )
        client = _Client(
            project, datastore_api=ds_api, transaction=transaction, database=database_id
        )

    query = _make_query(client)
    kwargs = {}

    if retry is not None:
        kwargs["retry"] = retry

    if timeout is not None:
        kwargs["timeout"] = timeout

    it_kwargs = kwargs.copy()  # so it doesn't get overwritten later

    aggregation_query = AggregationQuery(client=client, query=query)

    iterator = _make_aggregation_iterator(aggregation_query, client, **it_kwargs)
    page = iterator._next_page()

    assert isinstance(page, page_iterator.Page)
    assert page._parent is iterator

    partition_id = entity_pb2.PartitionId(project_id=project)
    if txn_id is not None:
        read_options = datastore_pb2.ReadOptions(transaction=txn_id)
    else:
        read_options = datastore_pb2.ReadOptions()

    aggregation_query = AggregationQuery(client=client, query=query)
    assert ds_api.run_aggregation_query.call_count == 2
    expected_request = {
        "project_id": project,
        "partition_id": partition_id,
        "read_options": read_options,
        "aggregation_query": aggregation_query._to_pb(),
    }
    set_database_id_to_request(expected_request, database_id)
    expected_call = mock.call(
        request=expected_request,
        **kwargs,
    )
    assert ds_api.run_aggregation_query.call_args_list == (
        [expected_call, expected_call]
    )


def test__item_to_aggregation_result():
    from google.cloud.datastore.aggregation import (
        AggregationResult,
        _item_to_aggregation_result,
    )

    with mock.patch(
        "proto.marshal.collections.maps.MapComposite"
    ) as map_composite_mock:
        map_composite_mock.keys.return_value = {"total": {"integer_value": 1}}

        result = _item_to_aggregation_result(None, map_composite_mock)

        assert len(result) == 1
        assert isinstance(result[0], AggregationResult)

        assert result[0].alias == "total"
        assert result[0].value == map_composite_mock.__getitem__().integer_value


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
@pytest.mark.parametrize(
    "aggregation_type,aggregation_args",
    [
        ("count", ()),
        (
            "sum",
            ("appearances",),
        ),
        ("avg", ("appearances",)),
    ],
)
def test_eventual_transaction_fails(database_id, aggregation_type, aggregation_args):
    """
    Queries with eventual consistency cannot be used in a transaction.
    """
    import mock

    transaction = mock.Mock()
    transaction.id = b"expected_id"
    client = _Client(None, database=database_id, transaction=transaction)

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)
    # initiate requested aggregation (ex count, sum, avg)
    getattr(aggregation_query, aggregation_type)(*aggregation_args)
    with pytest.raises(ValueError):
        list(aggregation_query.fetch(eventual=True))


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
@pytest.mark.parametrize(
    "aggregation_type,aggregation_args",
    [
        ("count", ()),
        (
            "sum",
            ("appearances",),
        ),
        ("avg", ("appearances",)),
    ],
)
def test_transaction_id_populated(database_id, aggregation_type, aggregation_args):
    """
    When an aggregation is run in the context of a transaction, the transaction
    ID should be populated in the request.
    """
    import mock

    transaction = mock.Mock()
    transaction.id = b"expected_id"
    mock_datastore_api = mock.Mock()
    mock_gapic = mock_datastore_api.run_aggregation_query
    mock_gapic.return_value = _make_aggregation_query_response([])
    client = _Client(
        None,
        datastore_api=mock_datastore_api,
        database=database_id,
        transaction=transaction,
    )

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    # initiate requested aggregation (ex count, sum, avg)
    getattr(aggregation_query, aggregation_type)(*aggregation_args)
    # run mock query
    list(aggregation_query.fetch())
    assert mock_gapic.call_count == 1
    request = mock_gapic.call_args[1]["request"]
    read_options = request["read_options"]
    # ensure transaction ID is populated
    assert read_options.transaction == client.current_transaction.id


@pytest.mark.parametrize("database_id", [None, "somedb"], indirect=True)
@pytest.mark.parametrize(
    "aggregation_type,aggregation_args",
    [
        ("count", ()),
        (
            "sum",
            ("appearances",),
        ),
        ("avg", ("appearances",)),
    ],
)
def test_transaction_begin_later(database_id, aggregation_type, aggregation_args):
    """
    When an aggregation is run in the context of a transaction with begin_later=True,
    the new_transaction field should be populated in the request read_options.
    """
    import mock

    from google.cloud.datastore_v1.types import TransactionOptions

    # make a fake begin_later transaction
    transaction = mock.Mock()
    transaction.id = None
    transaction._begin_later = True
    transaction._status = transaction._INITIAL
    transaction._options = TransactionOptions(read_only=TransactionOptions.ReadOnly())
    mock_datastore_api = mock.Mock()
    mock_gapic = mock_datastore_api.run_aggregation_query
    mock_gapic.return_value = _make_aggregation_query_response([])
    client = _Client(
        None,
        datastore_api=mock_datastore_api,
        database=database_id,
        transaction=transaction,
    )

    query = _make_query(client)
    aggregation_query = _make_aggregation_query(client=client, query=query)

    # initiate requested aggregation (ex count, sum, avg)
    getattr(aggregation_query, aggregation_type)(*aggregation_args)
    # run mock query
    list(aggregation_query.fetch())
    assert mock_gapic.call_count == 1
    request = mock_gapic.call_args[1]["request"]
    read_options = request["read_options"]
    # ensure new_transaction is populated
    assert not read_options.transaction
    assert read_options.new_transaction == transaction._options


class _Client(object):
    def __init__(
        self,
        project,
        datastore_api=None,
        namespace=None,
        transaction=None,
        *,
        database=None,
    ):
        self.project = project
        self.database = database
        self._datastore_api = datastore_api
        self.namespace = namespace
        self._transaction = transaction

    @property
    def current_transaction(self):
        return self._transaction


def _make_aggregation_query(*args, **kw):
    from google.cloud.datastore.aggregation import AggregationQuery

    return AggregationQuery(*args, **kw)


def _make_aggregation_iterator(*args, **kw):
    from google.cloud.datastore.aggregation import AggregationResultIterator

    return AggregationResultIterator(*args, **kw)


def _make_aggregation_query_response(
    aggregation_pbs, more_results_enum=3
):  # 3 = NO_MORE_RESULTS
    from google.cloud.datastore_v1.types import aggregation_result
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    aggregation_results = []
    for aggr in aggregation_pbs:
        result = aggregation_result.AggregationResult()
        result.aggregate_properties.alias = aggr.alias
        result.aggregate_properties.value = aggr.value
        aggregation_results.append(result)

    return datastore_pb2.RunAggregationQueryResponse(
        batch=aggregation_result.AggregationResultBatch(
            aggregation_results=aggregation_results,
            more_results=more_results_enum,
        )
    )


def _make_datastore_api_for_aggregation(*results):
    if len(results) == 0:
        run_aggregation_query = mock.Mock(return_value=None, spec=[])
    else:
        run_aggregation_query = mock.Mock(side_effect=results, spec=[])

    return mock.Mock(
        run_aggregation_query=run_aggregation_query, spec=["run_aggregation_query"]
    )
