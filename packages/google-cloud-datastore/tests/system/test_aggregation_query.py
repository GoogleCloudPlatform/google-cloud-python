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

import pytest
from google.api_core import exceptions
from test_utils.retry import RetryErrors

from . import _helpers
from .utils import clear_datastore, populate_datastore

retry_503 = RetryErrors(exceptions.ServiceUnavailable)


def _make_iterator(aggregation_query, **kw):
    # Do retry for errors raised during initial API call
    return retry_503(aggregation_query.fetch)(**kw)


def _pull_iterator(aggregation_query, **kw):
    return list(_make_iterator(aggregation_query, **kw))


def _do_fetch(aggregation_query, **kw):
    # Do retry for errors raised during iteration
    return retry_503(_pull_iterator)(aggregation_query, **kw)


@pytest.fixture(scope="session")
def aggregation_query_client(datastore_client, database_id=None):
    return _helpers.clone_client(datastore_client, namespace=None, database=database_id)


@pytest.fixture(scope="session")
def ancestor_key(aggregation_query_client, in_emulator):
    # In the emulator, re-populating the datastore is cheap.
    if in_emulator:
        populate_datastore.add_characters(client=aggregation_query_client)

    ancestor_key = aggregation_query_client.key(*populate_datastore.ANCESTOR)

    yield ancestor_key

    # In the emulator, destroy the query entities.
    if in_emulator:
        clear_datastore.remove_all_entities(client=aggregation_query_client)


def _make_query(aggregation_query_client, ancestor_key):
    return aggregation_query_client.query(kind="Character", ancestor=ancestor_key)


@pytest.fixture(scope="function")
def nested_query(aggregation_query_client, ancestor_key):
    return _make_query(aggregation_query_client, ancestor_key)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_count_query_default(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count()
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "property_1"
    expected_count = len(populate_datastore.CHARACTERS)
    assert r.value == expected_count


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
@pytest.mark.parametrize(
    "aggregation_type,aggregation_args,expected",
    [
        ("count", (), len(populate_datastore.CHARACTERS)),
        (
            "sum",
            ("appearances",),
            sum(c["appearances"] for c in populate_datastore.CHARACTERS),
        ),
        (
            "avg",
            ("appearances",),
            sum(c["appearances"] for c in populate_datastore.CHARACTERS)
            / len(populate_datastore.CHARACTERS),
        ),
    ],
)
def test_aggregation_query_in_transaction(
    aggregation_query_client,
    nested_query,
    database_id,
    aggregation_type,
    aggregation_args,
    expected,
):
    """
    When an aggregation query is run in a transaction, the transaction id should be sent with the request.
    The result is the same as when it is run outside of a transaction.
    """
    with aggregation_query_client.transaction():
        query = nested_query

        aggregation_query = aggregation_query_client.aggregation_query(query)
        getattr(aggregation_query, aggregation_type)(*aggregation_args)
        # run full query
        result = _do_fetch(aggregation_query)
        assert len(result) == 1
        assert len(result[0]) == 1
        r = result[0][0]
        assert r.alias == "property_1"
        assert r.value == expected


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_count_query_with_alias(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "total"
    expected_count = len(populate_datastore.CHARACTERS)
    assert r.value == expected_count


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_sum_query_default(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.sum("appearances")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "property_1"
    expected_sum = sum(c["appearances"] for c in populate_datastore.CHARACTERS)
    assert r.value == expected_sum


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_sum_query_with_alias(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.sum("appearances", alias="sum_appearances")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "sum_appearances"
    expected_sum = sum(c["appearances"] for c in populate_datastore.CHARACTERS)
    assert r.value == expected_sum


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_avg_query_default(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.avg("appearances")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "property_1"
    expected_avg = sum(c["appearances"] for c in populate_datastore.CHARACTERS) / len(
        populate_datastore.CHARACTERS
    )
    assert r.value == expected_avg


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_avg_query_with_alias(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.avg("appearances", alias="avg_appearances")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "avg_appearances"
    expected_avg = sum(c["appearances"] for c in populate_datastore.CHARACTERS) / len(
        populate_datastore.CHARACTERS
    )
    assert r.value == expected_avg


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_count_query_with_limit(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total")
    result = _do_fetch(aggregation_query)  # count without limit
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "total"
    expected_count = len(populate_datastore.CHARACTERS)
    assert r.value == expected_count

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total_up_to")
    limit = 2
    result = _do_fetch(aggregation_query, limit=limit)  # count with limit = 2
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "total_up_to"
    assert r.value == limit

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total_high_limit")
    limit = 2
    result = _do_fetch(
        aggregation_query, limit=expected_count * 2
    )  # count with limit > total
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "total_high_limit"
    assert r.value == expected_count


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_sum_query_with_limit(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.sum("appearances", alias="sum_limited")
    limit = 2
    result = _do_fetch(aggregation_query, limit=limit)  # count with limit = 2
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "sum_limited"
    expected = sum(c["appearances"] for c in populate_datastore.CHARACTERS[:limit])
    assert r.value == expected

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.sum("appearances", alias="sum_high_limit")
    num_characters = len(populate_datastore.CHARACTERS)
    result = _do_fetch(
        aggregation_query, limit=num_characters * 2
    )  # count with limit > total
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "sum_high_limit"
    assert r.value == sum(c["appearances"] for c in populate_datastore.CHARACTERS)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_avg_query_with_limit(aggregation_query_client, nested_query, database_id):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.avg("appearances", alias="avg_limited")
    limit = 2
    result = _do_fetch(aggregation_query, limit=limit)  # count with limit = 2
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "avg_limited"
    expected = (
        sum(c["appearances"] for c in populate_datastore.CHARACTERS[:limit]) / limit
    )
    assert r.value == expected

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.avg("appearances", alias="avg_high_limit")
    num_characters = len(populate_datastore.CHARACTERS)
    result = _do_fetch(
        aggregation_query, limit=num_characters * 2
    )  # count with limit > total
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "avg_high_limit"
    assert (
        r.value
        == sum(c["appearances"] for c in populate_datastore.CHARACTERS) / num_characters
    )


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_count_query_empty(aggregation_query_client, nested_query, database_id):
    query = nested_query
    query.add_filter("name", "=", "nonexistent")
    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "total"
    assert r.value == 0


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_sum_query_empty(aggregation_query_client, nested_query, database_id):
    query = nested_query
    query.add_filter("family", "=", "nonexistent")
    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.sum("appearances", alias="sum")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "sum"
    assert r.value == 0


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_avg_query_empty(aggregation_query_client, nested_query, database_id):
    query = nested_query
    query.add_filter("family", "=", "nonexistent")
    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.avg("appearances", alias="avg")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 1
    r = result[0][0]
    assert r.alias == "avg"
    assert r.value == 0


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_multiple_aggregations(
    aggregation_query_client, nested_query, database_id
):
    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total")
    aggregation_query.count(alias="all")
    aggregation_query.sum("appearances", alias="sum_appearances")
    aggregation_query.avg("appearances", alias="avg_appearances")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 4
    result_dict = {r.alias: r for r in result[0]}
    assert result_dict["total"].value == len(populate_datastore.CHARACTERS)
    assert result_dict["all"].value == len(populate_datastore.CHARACTERS)
    assert result_dict["sum_appearances"].value == sum(
        c["appearances"] for c in populate_datastore.CHARACTERS
    )
    assert result_dict["avg_appearances"].value == sum(
        c["appearances"] for c in populate_datastore.CHARACTERS
    ) / len(populate_datastore.CHARACTERS)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_add_aggregation(
    aggregation_query_client, nested_query, database_id
):
    from google.cloud.datastore.aggregation import (
        AvgAggregation,
        CountAggregation,
        SumAggregation,
    )

    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    count_aggregation = CountAggregation(alias="total")
    aggregation_query.add_aggregation(count_aggregation)

    sum_aggregation = SumAggregation("appearances", alias="sum_appearances")
    aggregation_query.add_aggregation(sum_aggregation)

    avg_aggregation = AvgAggregation("appearances", alias="avg_appearances")
    aggregation_query.add_aggregation(avg_aggregation)

    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 3
    result_dict = {r.alias: r for r in result[0]}
    assert result_dict["total"].value == len(populate_datastore.CHARACTERS)
    assert result_dict["sum_appearances"].value == sum(
        c["appearances"] for c in populate_datastore.CHARACTERS
    )
    assert result_dict["avg_appearances"].value == sum(
        c["appearances"] for c in populate_datastore.CHARACTERS
    ) / len(populate_datastore.CHARACTERS)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_add_aggregations(
    aggregation_query_client, nested_query, database_id
):
    from google.cloud.datastore.aggregation import (
        AvgAggregation,
        CountAggregation,
        SumAggregation,
    )

    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    count_aggregation_1 = CountAggregation(alias="total")
    count_aggregation_2 = CountAggregation(alias="all")
    sum_aggregation = SumAggregation("appearances", alias="sum_appearances")
    avg_aggregation = AvgAggregation("appearances", alias="avg_appearances")
    aggregation_query.add_aggregations(
        [count_aggregation_1, count_aggregation_2, sum_aggregation, avg_aggregation]
    )
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 4
    result_dict = {r.alias: r for r in result[0]}
    assert result_dict["total"].value == len(populate_datastore.CHARACTERS)
    assert result_dict["all"].value == len(populate_datastore.CHARACTERS)
    assert result_dict["sum_appearances"].value == sum(
        c["appearances"] for c in populate_datastore.CHARACTERS
    )
    assert result_dict["avg_appearances"].value == sum(
        c["appearances"] for c in populate_datastore.CHARACTERS
    ) / len(populate_datastore.CHARACTERS)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_add_aggregations_duplicated_alias(
    aggregation_query_client, nested_query, database_id
):
    from google.api_core.exceptions import BadRequest

    from google.cloud.datastore.aggregation import CountAggregation

    query = nested_query

    aggregation_query = aggregation_query_client.aggregation_query(query)
    count_aggregation_1 = CountAggregation(alias="total")
    count_aggregation_2 = CountAggregation(alias="total")
    aggregation_query.add_aggregations([count_aggregation_1, count_aggregation_2])
    with pytest.raises(BadRequest):
        _do_fetch(aggregation_query)

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.add_aggregation(count_aggregation_1)
    aggregation_query.add_aggregation(count_aggregation_2)
    with pytest.raises(BadRequest):
        _do_fetch(aggregation_query)

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total")
    aggregation_query.count(alias="total")
    with pytest.raises(BadRequest):
        _do_fetch(aggregation_query)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_with_nested_query_filtered(
    aggregation_query_client, nested_query, database_id
):
    query = nested_query

    query.add_filter("appearances", ">=", 20)
    expected_matches = 6

    # We expect 6, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total")
    aggregation_query.sum("appearances", alias="sum_appearances")
    aggregation_query.avg("appearances", alias="avg_appearances")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 3
    result_dict = {r.alias: r for r in result[0]}
    assert result_dict["total"].value == expected_matches
    expected_sum = sum(
        c["appearances"]
        for c in populate_datastore.CHARACTERS
        if c["appearances"] >= 20
    )
    assert result_dict["sum_appearances"].value == expected_sum
    assert result_dict["avg_appearances"].value == expected_sum / expected_matches


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_with_nested_query_multiple_filters(
    aggregation_query_client, nested_query, database_id
):
    query = nested_query

    query.add_filter("appearances", ">=", 26)
    query = query.add_filter("family", "=", "Stark")
    expected_matches = 4

    # We expect 4, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches

    aggregation_query = aggregation_query_client.aggregation_query(query)
    aggregation_query.count(alias="total")
    aggregation_query.sum("appearances", alias="sum_appearances")
    aggregation_query.avg("appearances", alias="avg_appearances")
    result = _do_fetch(aggregation_query)
    assert len(result) == 1
    assert len(result[0]) == 3
    result_dict = {r.alias: r for r in result[0]}
    assert result_dict["total"].value == expected_matches
    expected_sum = sum(
        c["appearances"]
        for c in populate_datastore.CHARACTERS
        if c["appearances"] >= 26 and "Stark" in c["family"]
    )
    assert result_dict["sum_appearances"].value == expected_sum
    assert result_dict["avg_appearances"].value == expected_sum / expected_matches


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_no_explain(
    aggregation_query_client, nested_query, database_id
):
    """
    When explain_options is not set, iterator.explain_metrics should raise an exception
    """
    from google.cloud.datastore.query_profile import QueryExplainError

    expected_error = "explain_options not set on query"

    agg_query = aggregation_query_client.aggregation_query(
        nested_query, explain_options=None
    )
    agg_query.count()
    agg_query.sum("appearances")
    agg_query.avg("appearances")
    iterator = agg_query.fetch()
    with pytest.raises(QueryExplainError) as excinfo:
        iterator.explain_metrics
    assert expected_error in str(excinfo.value)
    # exhaust the iterator and try again
    list(iterator)
    with pytest.raises(QueryExplainError) as excinfo:
        iterator.explain_metrics
    assert expected_error in str(excinfo.value)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_explain(aggregation_query_client, nested_query, database_id):
    """
    When explain_options(analyze=False) is set, iterator should contain explain_metrics field
    with plan_summary but no execution_stats
    """
    from google.cloud.datastore.query_profile import (
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    agg_query = aggregation_query_client.aggregation_query(
        nested_query, explain_options=ExplainOptions(analyze=False)
    )
    agg_query.count()
    agg_query.sum("appearances")
    agg_query.avg("appearances")
    iterator = agg_query.fetch()
    # should have plan_summary but no execution_stats
    stats = iterator.explain_metrics
    assert isinstance(stats, ExplainMetrics)
    assert isinstance(stats.plan_summary, PlanSummary)
    assert len(stats.plan_summary.indexes_used) > 0
    # execution_stats should not be present
    with pytest.raises(QueryExplainError) as excinfo:
        stats.execution_stats
    assert "execution_stats not available" in str(excinfo.value)
    # should have no results
    assert len(list(iterator)) == 0


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_explain_analyze(
    aggregation_query_client, nested_query, database_id
):
    """
    When explain_options(analyze=True) is set, iterator should contain explain_metrics field
    with plan_summary and execution_stats

    Should not be present until iterator is exhausted
    """
    from google.cloud.datastore.query_profile import (
        ExecutionStats,
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    expected_error = "explain_metrics not available until query is complete."
    agg_query = aggregation_query_client.aggregation_query(
        nested_query, explain_options=ExplainOptions(analyze=True)
    )
    agg_query.count()
    agg_query.sum("appearances")
    agg_query.avg("appearances")
    iterator = agg_query.fetch()
    # explain_metrics isn't present until iterator is exhausted
    with pytest.raises(QueryExplainError) as excinfo:
        iterator.explain_metrics
    assert expected_error in str(excinfo.value)
    # exhaust the iterator
    results = list(iterator)
    num_results = len(results)
    assert num_results > 0
    stats = iterator.explain_metrics
    assert isinstance(stats, ExplainMetrics)
    # verify plan_summary
    assert isinstance(stats.plan_summary, PlanSummary)
    assert len(stats.plan_summary.indexes_used) > 0
    assert (
        stats.plan_summary.indexes_used[0]["properties"]
        == "(appearances ASC, __name__ ASC)"
    )
    assert stats.plan_summary.indexes_used[0]["query_scope"] == "Includes ancestors"
    # verify execution_stats
    assert isinstance(stats.execution_stats, ExecutionStats)
    assert stats.execution_stats.results_returned == num_results
    assert stats.execution_stats.read_operations == num_results
    duration = stats.execution_stats.execution_duration.total_seconds()
    assert duration > 0
    assert duration < 1  # we expect a number closer to 0.05
    assert isinstance(stats.execution_stats.debug_stats, dict)
    assert "billing_details" in stats.execution_stats.debug_stats
    assert "documents_scanned" in stats.execution_stats.debug_stats
    assert "index_entries_scanned" in stats.execution_stats.debug_stats
    assert len(stats.execution_stats.debug_stats) > 0


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_aggregation_query_explain_in_transaction(
    aggregation_query_client, nested_query, database_id
):
    """
    When an aggregation query is run in a transaction, the transaction id should be sent with the request.
    The result is the same as when it is run outside of a transaction.
    """
    from google.cloud.datastore.query_profile import ExplainMetrics, ExplainOptions

    with aggregation_query_client.transaction():
        agg_query = aggregation_query_client.aggregation_query(
            nested_query, explain_options=ExplainOptions(analyze=True)
        )
        agg_query.count()
        agg_query.sum("appearances")
        agg_query.avg("appearances")
        iterator = agg_query.fetch()
        # run full query
        list(iterator)
        # check for stats
        stats = iterator.explain_metrics
        assert isinstance(stats, ExplainMetrics)
