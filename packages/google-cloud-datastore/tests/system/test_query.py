# Copyright 2011 Google LLC
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

from google.cloud.datastore.query import And, Or, PropertyFilter

from . import _helpers
from .utils import clear_datastore, populate_datastore

retry_503 = RetryErrors(exceptions.ServiceUnavailable)


def _make_iterator(query, **kw):
    # Do retry for errors raised during initial API call
    return retry_503(query.fetch)(**kw)


def _pull_iterator(query, **kw):
    return list(_make_iterator(query, **kw))


def _do_fetch(query, **kw):
    # Do retry for errors raised during iteration
    return retry_503(_pull_iterator)(query, **kw)


@pytest.fixture(scope="session")
def query_client(datastore_client):
    return _helpers.clone_client(datastore_client, namespace=None)


@pytest.fixture(scope="session")
def ancestor_key(query_client, in_emulator):
    # In the emulator, re-populating the datastore is cheap.
    if in_emulator:
        populate_datastore.add_characters(client=query_client)

    ancestor_key = query_client.key(*populate_datastore.ANCESTOR)

    yield ancestor_key

    # In the emulator, destroy the query entities.
    if in_emulator:
        clear_datastore.remove_all_entities(client=query_client)


def _make_ancestor_query(query_client, ancestor_key, **kwargs):
    return query_client.query(kind="Character", ancestor=ancestor_key, **kwargs)


@pytest.fixture(scope="function")
def ancestor_query(query_client, ancestor_key):
    return _make_ancestor_query(query_client, ancestor_key)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_ancestor(ancestor_query, database_id):
    query = ancestor_query
    expected_matches = 8

    # We expect 8, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_in_transaction(ancestor_query, database_id):
    """
    when a query is run in a transaction, the transaction id should be sent with the request.
    the result is the same as when it is run outside of a transaction.
    """
    query = ancestor_query
    client = query._client
    expected_matches = 8
    with client.transaction():
        # run full query
        entities = _do_fetch(query)
        assert len(entities) == expected_matches


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_limit_paging(ancestor_query, database_id):
    query = ancestor_query
    limit = 5

    # Fetch characters.
    iterator = query.fetch(limit=limit)
    page = next(iterator.pages)
    character_entities = list(page)
    cursor = iterator.next_page_token
    assert len(character_entities) == limit

    # Check cursor after fetch.
    assert cursor is not None

    # Fetch remaining characters.
    new_character_entities = _do_fetch(query, start_cursor=cursor)
    characters_remaining = len(populate_datastore.CHARACTERS) - limit
    assert len(new_character_entities) == characters_remaining


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_simple_filter(ancestor_query, database_id):
    query = ancestor_query
    query.add_filter(filter=PropertyFilter("appearances", ">=", 20))
    expected_matches = 6

    # We expect 6, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_multiple_filters(ancestor_query, database_id):
    query = ancestor_query
    query.add_filter(filter=PropertyFilter("appearances", ">=", 26))
    query = query.add_filter(filter=PropertyFilter("family", "=", "Stark"))
    expected_matches = 4

    # We expect 4, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_key_filter(query_client, ancestor_query, database_id):
    # Use the client for this test instead of the global.
    query = ancestor_query
    rickard_key = query_client.key(*populate_datastore.RICKARD)
    query.key_filter(rickard_key)
    expected_matches = 1

    # We expect 1, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_order(ancestor_query, database_id):
    query = ancestor_query
    query.order = "appearances"
    expected_matches = 8

    # We expect 8, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches

    # Actually check the ordered data returned.
    assert entities[0]["name"] == populate_datastore.CHARACTERS[0]["name"]
    assert entities[7]["name"] == populate_datastore.CHARACTERS[3]["name"]


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_projection(ancestor_query, database_id):
    filtered_query = ancestor_query
    filtered_query.projection = ["name", "family"]
    filtered_query.order = ["name", "family"]

    # NOTE: There are 9 responses because of Catelyn. She has both
    #       Stark and Tully as her families, hence occurs twice in
    #       the results.
    expected_matches = 9

    # We expect 9, but allow the query to get 1 extra.
    entities = list(filtered_query.fetch(limit=expected_matches + 1))
    assert len(entities) == expected_matches

    arya_entity = entities[0]
    catelyn_stark_entity = entities[2]
    catelyn_tully_entity = entities[3]
    sansa_entity = entities[8]

    assert dict(arya_entity) == {"name": "Arya", "family": "Stark"}

    # Check both Catelyn keys are the same.
    assert catelyn_stark_entity.key == catelyn_tully_entity.key
    assert dict(catelyn_stark_entity) == {"name": "Catelyn", "family": "Stark"}
    assert dict(catelyn_tully_entity) == {"name": "Catelyn", "family": "Tully"}

    assert dict(sansa_entity) == {"name": "Sansa", "family": "Stark"}


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_paginate_simple_uuid_keys(query_client, database_id):
    # See issue #4264
    page_query = query_client.query(kind="uuid_key")
    iterator = page_query.fetch()
    seen = set()
    page_count = 0

    for page in iterator.pages:
        page_count += 1
        for entity in page:
            uuid_str = entity.key.name
            assert uuid_str not in seen
            seen.add(uuid_str)

    assert page_count > 1


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_paginate_simple_timestamp_keys(query_client, database_id):
    # See issue #4264
    page_query = query_client.query(kind="timestamp_key")
    iterator = page_query.fetch()
    seen = set()
    page_count = 0

    for page in iterator.pages:
        page_count += 1
        for entity in page:
            timestamp = entity.key.id
            assert timestamp not in seen
            seen.add(timestamp)

    assert page_count > 1


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_offset_w_timestamp_keys(query_client, database_id):
    # See issue #4675
    max_all = 10000
    offset = 1
    max_offset = max_all - offset
    query = query_client.query(kind="timestamp_key")

    all_w_limit = _do_fetch(query, limit=max_all)
    assert len(all_w_limit) == max_all

    offset_w_limit = _do_fetch(query, offset=offset, limit=max_offset)
    assert offset_w_limit == all_w_limit[offset:]


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_paginate_with_offset(ancestor_query, database_id):
    page_query = ancestor_query
    page_query.order = "appearances"
    offset = 2
    limit = 3

    iterator = page_query.fetch(limit=limit, offset=offset)

    # Fetch characters.
    page = next(iterator.pages)
    entities = list(page)
    assert len(entities) == limit
    assert entities[0]["name"] == "Robb"
    assert entities[1]["name"] == "Bran"
    assert entities[2]["name"] == "Catelyn"

    cursor = iterator.next_page_token

    # Fetch next set of characters.
    new_iterator = page_query.fetch(limit=limit, offset=0, start_cursor=cursor)

    entities = list(new_iterator)
    assert len(entities) == limit
    assert entities[0]["name"] == "Sansa"
    assert entities[1]["name"] == "Jon Snow"
    assert entities[2]["name"] == "Arya"


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_paginate_with_start_cursor(query_client, ancestor_key, database_id):
    # Don't use fixture, because we need to create a clean copy later.
    page_query = _make_ancestor_query(query_client, ancestor_key)
    page_query.order = "appearances"
    limit = 3
    offset = 2

    iterator = page_query.fetch(limit=limit, offset=offset)

    # Fetch characters.
    page = next(iterator.pages)
    entities = list(page)
    assert len(entities) == limit

    cursor = iterator.next_page_token

    # Use cursor to create a fresh query.
    fresh_query = _make_ancestor_query(query_client, ancestor_key)
    fresh_query.order = "appearances"

    new_entities = list(fresh_query.fetch(start_cursor=cursor, limit=limit))

    characters_remaining = len(populate_datastore.CHARACTERS) - limit - offset
    assert len(new_entities) == characters_remaining
    assert new_entities[0]["name"] == "Sansa"
    assert new_entities[2]["name"] == "Arya"


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_distinct_on(ancestor_query, database_id):
    query = ancestor_query
    query.distinct_on = ["alive"]
    expected_matches = 2

    # We expect 2, but allow the query to get 1 extra.
    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches
    assert entities[0]["name"] == "Catelyn"
    assert entities[1]["name"] == "Arya"


@pytest.fixture(scope="session")
def large_query_client(datastore_client):
    large_query_client = _helpers.clone_client(
        datastore_client,
        namespace=populate_datastore.LARGE_CHARACTER_NAMESPACE,
    )
    # Populate the datastore if necessary.
    populate_datastore.add_large_character_entities(client=large_query_client)

    return large_query_client


@pytest.fixture(scope="session")
def mergejoin_query_client(datastore_client):
    mergejoin_query_client = _helpers.clone_client(
        datastore_client,
        namespace=populate_datastore.MERGEJOIN_DATASET_NAMESPACE,
    )
    populate_datastore.add_mergejoin_dataset_entities(client=mergejoin_query_client)

    return mergejoin_query_client


@pytest.fixture(scope="function")
def large_query(large_query_client):
    # Use the client for this test instead of the global.
    return large_query_client.query(
        kind=populate_datastore.LARGE_CHARACTER_KIND,
        namespace=populate_datastore.LARGE_CHARACTER_NAMESPACE,
    )


@pytest.fixture(scope="function")
def mergejoin_query(mergejoin_query_client):
    # Use the client for this test instead of the global.
    return mergejoin_query_client.query(
        kind=populate_datastore.MERGEJOIN_DATASET_KIND,
        namespace=populate_datastore.MERGEJOIN_DATASET_NAMESPACE,
    )


@pytest.mark.parametrize(
    "limit,offset,expected",
    [
        # with no offset there are the correct # of results
        (
            None,
            None,
            populate_datastore.LARGE_CHARACTER_TOTAL_OBJECTS,
        ),
        # with no limit there are results (offset provided)
        (
            None,
            900,
            populate_datastore.LARGE_CHARACTER_TOTAL_OBJECTS - 900,
        ),
        # Offset beyond items larger: verify 200 items found
        (
            200,
            1100,
            200,
        ),
        # offset within range, expect 50 despite larger limit")
        (100, populate_datastore.LARGE_CHARACTER_TOTAL_OBJECTS - 50, 50),
        # Offset beyond items larger Verify no items found")
        (200, populate_datastore.LARGE_CHARACTER_TOTAL_OBJECTS + 1000, 0),
    ],
)
@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_large_query(large_query, limit, offset, expected, database_id):
    page_query = large_query
    page_query.add_filter(filter=PropertyFilter("family", "=", "Stark"))
    page_query.add_filter(filter=PropertyFilter("alive", "=", False))

    iterator = page_query.fetch(limit=limit, offset=offset)

    entities = [e for e in iterator]
    assert len(entities) == expected


@pytest.mark.parametrize("database_id", [_helpers.TEST_DATABASE], indirect=True)
def test_mergejoin_query(mergejoin_query, database_id):
    query = mergejoin_query
    query.add_filter(filter=PropertyFilter("a", "=", 1))
    query.add_filter(filter=PropertyFilter("b", "=", 1))

    # There should be 2 * MERGEJOIN_QUERY_NUM_RESULTS results total
    expected_total = 2 * populate_datastore.MERGEJOIN_QUERY_NUM_RESULTS
    for offset in range(0, expected_total + 1):
        iterator = query.fetch(offset=offset)
        num_entities = len([e for e in iterator])
        assert num_entities == expected_total - offset


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_add_property_filter(ancestor_query, database_id):
    query = ancestor_query

    query.add_filter(filter=PropertyFilter("appearances", ">=", 26))
    expected_matches = 4

    entities = _do_fetch(query, limit=expected_matches + 1)

    assert len(entities) == expected_matches
    for e in entities:
        assert e["appearances"] >= 26


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_and_composite_filter(ancestor_query, database_id):
    query = ancestor_query

    query.add_filter(
        filter=And(
            [
                PropertyFilter("family", "=", "Stark"),
                PropertyFilter("name", "=", "Jon Snow"),
            ]
        )
    )
    expected_matches = 1

    entities = _do_fetch(query)

    assert len(entities) == expected_matches
    assert entities[0]["family"] == "Stark"
    assert entities[0]["name"] == "Jon Snow"


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_or_composite_filter(ancestor_query, database_id):
    query = ancestor_query

    # name = Arya or name = Jon Snow
    query.add_filter(
        filter=Or(
            [
                PropertyFilter("name", "=", "Arya"),
                PropertyFilter("name", "=", "Jon Snow"),
            ]
        )
    )
    expected_matches = 2

    entities = _do_fetch(query)

    assert len(entities) == expected_matches

    assert entities[0]["name"] == "Arya"
    assert entities[1]["name"] == "Jon Snow"


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_add_filters(ancestor_query, database_id):
    query = ancestor_query

    # family = Stark AND name = Jon Snow
    query.add_filter(filter=PropertyFilter("family", "=", "Stark"))
    query.add_filter(filter=PropertyFilter("name", "=", "Jon Snow"))

    expected_matches = 1

    entities = _do_fetch(query)

    assert len(entities) == expected_matches
    assert entities[0]["family"] == "Stark"
    assert entities[0]["name"] == "Jon Snow"


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_add_complex_filters(ancestor_query, database_id):
    query = ancestor_query

    # (alive = True OR appearances >= 26) AND (family = Stark)
    query.add_filter(
        filter=(
            Or(
                [
                    PropertyFilter("alive", "=", True),
                    PropertyFilter("appearances", ">=", 26),
                ]
            )
        )
    )
    query.add_filter(filter=PropertyFilter("family", "IN", ["Stark"]))

    entities = _do_fetch(query)

    alive_count = 0
    appearance_count = 0
    stark_family_count = 0
    for e in entities:
        if e["appearances"] >= 26:
            appearance_count += 1
        if e["alive"] is True:
            alive_count += 1
        if "Stark" in e["family"]:
            stark_family_count += 1

    assert alive_count == 4
    assert appearance_count == 4
    assert stark_family_count == 5


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_no_explain(query_client, ancestor_key, database_id):
    """
    When explain_options is not set, iterator.explain_metrics should raise an exception
    """
    from google.cloud.datastore.query_profile import QueryExplainError

    expected_error = "explain_options not set on query"
    query = _make_ancestor_query(query_client, ancestor_key, explain_options=None)
    iterator = query.fetch()
    with pytest.raises(QueryExplainError) as excinfo:
        iterator.explain_metrics
    assert expected_error in str(excinfo.value)
    # exhaust the iterator and try again
    list(iterator)
    with pytest.raises(QueryExplainError) as excinfo:
        iterator.explain_metrics
    assert expected_error in str(excinfo.value)


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_explain(query_client, ancestor_key, database_id):
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

    query = _make_ancestor_query(
        query_client, ancestor_key, explain_options=ExplainOptions(analyze=False)
    )
    iterator = query.fetch()
    # should have plan_summary but no execution_stats
    stats = iterator.explain_metrics
    assert isinstance(stats, ExplainMetrics)
    assert isinstance(stats.plan_summary, PlanSummary)
    assert len(stats.plan_summary.indexes_used) > 0
    assert stats.plan_summary.indexes_used[0]["properties"] == "(__name__ ASC)"
    assert stats.plan_summary.indexes_used[0]["query_scope"] == "Collection group"
    # execution_stats should not be present
    with pytest.raises(QueryExplainError) as excinfo:
        stats.execution_stats
    expected_error = "execution_stats not available when explain_options.analyze=False."
    assert expected_error in str(excinfo.value)
    # should have no results
    assert list(iterator) == []


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_explain_analyze(query_client, ancestor_key, database_id):
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
    query = _make_ancestor_query(
        query_client, ancestor_key, explain_options=ExplainOptions(analyze=True)
    )
    iterator = query.fetch()
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
    assert stats.plan_summary.indexes_used[0]["properties"] == "(__name__ ASC)"
    assert stats.plan_summary.indexes_used[0]["query_scope"] == "Collection group"
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
def test_query_explain_in_transaction(query_client, ancestor_key, database_id):
    """
    Should be able to access explain metrics when called in a transaction
    """
    from google.cloud.datastore.query_profile import ExplainMetrics, ExplainOptions

    query = _make_ancestor_query(
        query_client, ancestor_key, explain_options=ExplainOptions(analyze=True)
    )
    client = query._client
    with client.transaction():
        # run full query
        iterator = query.fetch()
        list(iterator)
        # check for stats
        stats = iterator.explain_metrics
        assert isinstance(stats, ExplainMetrics)
