# Copyright 2017 Google LLC
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

import concurrent.futures
import datetime
import itertools
import math
import operator
from typing import Callable, Dict, List, Optional

import google.auth
import mock
import pytest
from google.api_core.exceptions import (
    AlreadyExists,
    FailedPrecondition,
    InvalidArgument,
    NotFound,
)
from google.cloud._helpers import _datetime_to_pb_timestamp
from google.oauth2 import service_account
from test__helpers import (
    EMULATOR_CREDS,
    ENTERPRISE_MODE_ERROR,
    FIRESTORE_CREDS,
    FIRESTORE_EMULATOR,
    FIRESTORE_ENTERPRISE_DB,
    FIRESTORE_OTHER_DB,
    FIRESTORE_PROJECT,
    MISSING_DOCUMENT,
    RANDOM_ID_REGEX,
    TEST_DATABASES,
    TEST_DATABASES_W_ENTERPRISE,
    UNIQUE_RESOURCE_ID,
)

from google.cloud import firestore_v1 as firestore
from google.cloud.firestore_v1.base_query import And, FieldFilter, Or
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
from google.cloud.firestore_v1.bson import (
    BSONBinary,
    BSONDecimal128,
    BSONInt32,
    BSONMaxKey,
    BSONMinKey,
    BSONObjectId,
    BSONRegex,
    BSONTimestamp,
)
from google.cloud.firestore_v1.vector import Vector


def _get_credentials_and_project():
    if FIRESTORE_EMULATOR:
        credentials = EMULATOR_CREDS
        project = FIRESTORE_PROJECT
    elif FIRESTORE_CREDS:
        credentials = service_account.Credentials.from_service_account_file(
            FIRESTORE_CREDS
        )
        project = FIRESTORE_PROJECT or credentials.project_id
    else:
        credentials, project = google.auth.default()
    return credentials, project


@pytest.fixture(scope="session")
def database(request):
    return request.param


@pytest.fixture(scope="module")
def client(database):
    credentials, project = _get_credentials_and_project()
    yield firestore.Client(project=project, credentials=credentials, database=database)


@pytest.fixture
def cleanup():
    operations = []
    yield operations.append

    with concurrent.futures.ThreadPoolExecutor() as executor:
        list(executor.map(lambda op: op(), operations))


@pytest.fixture
def verify_pipeline(subtests):
    """
    This fixture provides a subtest function which
    ensures a pipeline produces the same results as the query it is derived
    from.

    It can be attached to existing query tests to check both
    modalities at the same time

    Pipelines are only supported on enterprise dbs. Skip other environments
    """

    def _verifier(query):
        from google.cloud.firestore_v1.base_aggregation import BaseAggregationQuery

        with subtests.test(msg="verify_pipeline"):
            client = query._client
            if FIRESTORE_EMULATOR:
                pytest.skip("skip pipeline verification on emulator")
            if client._database != FIRESTORE_ENTERPRISE_DB:
                pytest.skip("pipelines only supports enterprise db")

            def _clean_results(results):
                if isinstance(results, dict):
                    return {k: _clean_results(v) for k, v in results.items()}
                elif isinstance(results, list):
                    return [_clean_results(r) for r in results]
                elif isinstance(results, float) and math.isnan(results):
                    return "__NAN_VALUE__"
                else:
                    return results

            query_exception = None
            query_results = None
            try:
                try:
                    if isinstance(query, BaseAggregationQuery):
                        # aggregation queries return a list of lists of aggregation results
                        query_results = _clean_results(
                            list(
                                itertools.chain.from_iterable(
                                    [[a._to_dict() for a in s] for s in query.get()]
                                )
                            )
                        )
                    else:
                        # other qureies return a simple list of results
                        query_results = _clean_results(
                            [s.to_dict() for s in query.get()]
                        )
                except Exception as e:
                    # if we expect the query to fail, capture the exception
                    query_exception = e
                pipeline = client.pipeline().create_from(query)
                if query_exception:
                    # ensure that the pipeline uses same error as query
                    with pytest.raises(query_exception.__class__):
                        pipeline.execute()
                else:
                    # ensure results match query
                    pipeline_results = _clean_results(
                        [s.data() for s in pipeline.execute()]
                    )
                    assert query_results == pipeline_results
            except FailedPrecondition as e:
                # if testing against a non-enterprise db, skip this check
                if ENTERPRISE_MODE_ERROR not in e.message:
                    raise e

    return _verifier


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_collections(client, database):
    collections = list(client.collections())
    assert isinstance(collections, list)


@pytest.mark.parametrize("database", TEST_DATABASES)
def test_collections_w_import(database):
    from google.cloud import firestore

    credentials, project = _get_credentials_and_project()
    client = firestore.Client(
        project=project, credentials=credentials, database=database
    )
    collections = list(client.collections())

    assert isinstance(collections, list)


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_collection_stream_or_get_w_no_explain_options(database, query_docs, method):
    from google.cloud.firestore_v1.query_profile import QueryExplainError

    collection, _, _ = query_docs

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(collection, method)
    results = method_under_test()

    # verify explain_metrics isn't available
    with pytest.raises(
        QueryExplainError,
        match="explain_options not set on query.",
    ):
        results.get_explain_metrics()


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["get", "stream"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_collection_stream_or_get_w_explain_options_analyze_false(
    database, method, query_docs
):
    from google.cloud.firestore_v1.query_profile import (
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    collection, _, _ = query_docs

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(collection, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=False))

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert plan_summary.indexes_used[0]["properties"] == "(__name__ ASC)"
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection"

    # Verify execution_stats isn't available.
    with pytest.raises(
        QueryExplainError,
        match="execution_stats not available when explain_options.analyze=False",
    ):
        explain_metrics.execution_stats


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["get", "stream"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_collection_stream_or_get_w_explain_options_analyze_true(
    database, method, query_docs
):
    from google.cloud.firestore_v1.query_profile import (
        ExecutionStats,
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    collection, _, _ = query_docs

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(collection, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=True))

    # In the case of `stream()`, an exception should be raised when accessing
    # explain_metrics before query finishes.
    if method == "stream":
        with pytest.raises(
            QueryExplainError,
            match="explain_metrics not available until query is complete",
        ):
            results.get_explain_metrics()

    # Finish iterating results, and explain_metrics should be available.
    num_results = len(list(results))

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert plan_summary.indexes_used[0]["properties"] == "(__name__ ASC)"
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection"

    # Verify execution_stats.
    execution_stats = explain_metrics.execution_stats
    assert isinstance(execution_stats, ExecutionStats)
    assert execution_stats.results_returned == num_results
    assert execution_stats.read_operations == num_results
    duration = execution_stats.execution_duration.total_seconds()
    assert duration > 0
    assert duration < 1  # we expect a number closer to 0.05
    assert isinstance(execution_stats.debug_stats, dict)
    assert "billing_details" in execution_stats.debug_stats
    assert "documents_scanned" in execution_stats.debug_stats
    assert "index_entries_scanned" in execution_stats.debug_stats
    assert len(execution_stats.debug_stats) > 0


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_collections_w_read_time(client, cleanup, database):
    first_collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    first_document_id = "doc" + UNIQUE_RESOURCE_ID
    first_document = client.document(first_collection_id, first_document_id)
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(first_document.delete)

    data = {"status": "new"}
    write_result = first_document.create(data)
    read_time = write_result.update_time

    second_collection_id = "doc-create" + UNIQUE_RESOURCE_ID + "-2"
    second_document_id = "doc" + UNIQUE_RESOURCE_ID + "-2"
    second_document = client.document(second_collection_id, second_document_id)
    cleanup(second_document.delete)
    second_document.create(data)

    # Test that listing current collections does have the second id.
    curr_collections = list(client.collections())
    ids = [collection.id for collection in curr_collections]
    assert second_collection_id in ids
    assert first_collection_id in ids

    # We're just testing that we added one collection at read_time, not two.
    collections = list(client.collections(read_time=read_time))
    ids = [collection.id for collection in collections]
    assert second_collection_id not in ids
    assert first_collection_id in ids


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_create_document(client, cleanup, database):
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    document_id = "doc" + UNIQUE_RESOURCE_ID
    document = client.document(collection_id, document_id)
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(document.delete)

    data = {
        "now": firestore.SERVER_TIMESTAMP,
        "eenta-ger": 11,
        "bites": b"\xe2\x98\x83 \xe2\x9b\xb5",
        "also": {"nestednow": firestore.SERVER_TIMESTAMP, "quarter": 0.25},
    }
    write_result = document.create(data)
    updated = write_result.update_time
    delta = updated - now
    # Allow a bit of clock skew, but make sure timestamps are close.
    assert -300.0 < delta.total_seconds() < 300.0

    with pytest.raises(AlreadyExists):
        document.create(data)

    # Verify the server times.
    snapshot = document.get()
    stored_data = snapshot.to_dict()
    server_now = stored_data["now"]

    delta = updated - server_now
    # NOTE: We could check the ``transform_results`` from the write result
    #       for the document transform, but this value gets dropped. Instead
    #       we make sure the timestamps are close.
    # TODO(microgen): this was 0.0 - 5.0 before. After microgen, This started
    # getting very small negative times.
    assert -0.2 <= delta.total_seconds() < 5.0
    expected_data = {
        "now": server_now,
        "eenta-ger": data["eenta-ger"],
        "bites": data["bites"],
        "also": {"nestednow": server_now, "quarter": data["also"]["quarter"]},
    }
    assert stored_data == expected_data


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_create_document_w_vector(client, cleanup, database):
    collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    document1 = client.document(collection_id, "doc1")
    document2 = client.document(collection_id, "doc2")
    document3 = client.document(collection_id, "doc3")
    data1 = {"embedding": Vector([1.0, 2.0, 3.0])}
    data2 = {"embedding": Vector([2, 2, 3.0])}
    data3 = {"embedding": Vector([2.0, 2.0])}

    document1.create(data1)
    document2.create(data2)
    document3.create(data3)

    assert [
        v.to_dict()
        for v in client.collection(collection_id).order_by("embedding").get()
    ] == [data3, data1, data2]

    vector_query_future = concurrent.futures.Future()

    def on_snapshot(docs, changes, read_time):
        on_snapshot.results += docs
        if len(on_snapshot.results) >= 3 and not vector_query_future.done():
            vector_query_future.set_result(True)

    on_snapshot.results = []
    client.collection(collection_id).order_by("embedding").on_snapshot(on_snapshot)

    vector_query_future.result(timeout=60.0)
    assert [v.to_dict() for v in on_snapshot.results[:3]] == [data3, data1, data2]


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
@pytest.mark.parametrize(
    "distance_measure",
    [
        DistanceMeasure.EUCLIDEAN,
        DistanceMeasure.COSINE,
    ],
)
def test_vector_search_collection(client, database, distance_measure):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection = client.collection(collection_id)

    vector_query = collection.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=1,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 1
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
    }


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
@pytest.mark.parametrize(
    "distance_measure",
    [
        DistanceMeasure.EUCLIDEAN,
        DistanceMeasure.COSINE,
    ],
)
def test_vector_search_collection_with_filter(client, database, distance_measure):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection = client.collection(collection_id)

    vector_query = collection.where("color", "==", "red").find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=1,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 1
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
    }


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_search_collection_with_distance_parameters_euclid(client, database):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection = client.collection(collection_id)

    vector_query = collection.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.EUCLIDEAN,
        limit=3,
        distance_result_field="vector_distance",
        distance_threshold=1.0,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 2
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
        "vector_distance": 0.0,
    }
    assert returned[1].to_dict() == {
        "embedding": Vector([2.0, 2.0, 3.0]),
        "color": "red",
        "vector_distance": 1.0,
    }


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_search_collection_with_distance_parameters_cosine(client, database):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection = client.collection(collection_id)

    vector_query = collection.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.COSINE,
        limit=3,
        distance_result_field="vector_distance",
        distance_threshold=0.02,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 2
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
        "vector_distance": 0.0,
    }
    assert returned[1].to_dict() == {
        "embedding": Vector([3.0, 4.0, 5.0]),
        "color": "yellow",
        "vector_distance": 0.017292370176009153,
    }


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
@pytest.mark.parametrize(
    "distance_measure",
    [
        DistanceMeasure.EUCLIDEAN,
        DistanceMeasure.COSINE,
    ],
)
def test_vector_search_collection_group(client, database, distance_measure):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection_group = client.collection_group(collection_id)

    vector_query = collection_group.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=1,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 1
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
    }


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize(
    "distance_measure",
    [
        DistanceMeasure.EUCLIDEAN,
        DistanceMeasure.COSINE,
    ],
)
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_search_collection_group_with_filter(client, database, distance_measure):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection_group = client.collection_group(collection_id)

    vector_query = collection_group.where("color", "==", "red").find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=1,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 1
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
    }


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_search_collection_group_with_distance_parameters_euclid(
    client, database
):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection_group = client.collection_group(collection_id)

    vector_query = collection_group.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.EUCLIDEAN,
        limit=3,
        distance_result_field="vector_distance",
        distance_threshold=1.0,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 2
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
        "vector_distance": 0.0,
    }
    assert returned[1].to_dict() == {
        "embedding": Vector([2.0, 2.0, 3.0]),
        "color": "red",
        "vector_distance": 1.0,
    }


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Require index and seed data")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_search_collection_group_with_distance_parameters_cosine(
    client, database
):
    # Documents and Indexes are a manual step from util/bootstrap_vector_index.py
    collection_id = "vector_search"
    collection_group = client.collection_group(collection_id)

    vector_query = collection_group.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.COSINE,
        limit=3,
        distance_result_field="vector_distance",
        distance_threshold=0.02,
    )
    returned = vector_query.get()
    assert isinstance(returned, list)
    assert len(returned) == 2
    assert returned[0].to_dict() == {
        "embedding": Vector([1.0, 2.0, 3.0]),
        "color": "red",
        "vector_distance": 0.0,
    }
    assert returned[1].to_dict() == {
        "embedding": Vector([3.0, 4.0, 5.0]),
        "color": "yellow",
        "vector_distance": 0.017292370176009153,
    }


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_query_stream_or_get_w_no_explain_options(client, database, method):
    from google.cloud.firestore_v1.query_profile import QueryExplainError

    collection_id = "vector_search"
    collection_group = client.collection_group(collection_id)

    vector_query = collection_group.where("color", "==", "red").find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.EUCLIDEAN,
        limit=1,
    )

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(vector_query, method)
    results = method_under_test()

    # verify explain_metrics isn't available
    with pytest.raises(
        QueryExplainError,
        match="explain_options not set on query.",
    ):
        results.get_explain_metrics()


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_query_stream_or_get_w_explain_options_analyze_true(
    client, database, method
):
    from google.cloud.firestore_v1.query_profile import (
        ExecutionStats,
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    collection_id = "vector_search"
    collection_group = client.collection_group(collection_id)

    vector_query = collection_group.where("color", "==", "red").find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.EUCLIDEAN,
        limit=1,
    )

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(vector_query, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=True))

    # With `stream()`, an exception should be raised when accessing
    # explain_metrics before query finishes.
    if method == "stream":
        with pytest.raises(
            QueryExplainError,
            match="explain_metrics not available until query is complete",
        ):
            results.get_explain_metrics()

    # Finish iterating results, and explain_metrics should be available.
    num_results = len(list(results))

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert (
        plan_summary.indexes_used[0]["properties"]
        == "(color ASC, __name__ ASC, embedding VECTOR<3>)"
    )
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection group"

    # Verify execution_stats.
    execution_stats = explain_metrics.execution_stats
    assert isinstance(execution_stats, ExecutionStats)
    assert execution_stats.results_returned == num_results
    assert execution_stats.read_operations > 0
    duration = execution_stats.execution_duration.total_seconds()
    assert duration > 0
    assert duration < 1  # we expect a number closer to 0.05
    assert isinstance(execution_stats.debug_stats, dict)
    assert "billing_details" in execution_stats.debug_stats
    assert "documents_scanned" in execution_stats.debug_stats
    assert "index_entries_scanned" in execution_stats.debug_stats
    assert len(execution_stats.debug_stats) > 0


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_vector_query_stream_or_get_w_explain_options_analyze_false(
    client, database, method
):
    from google.cloud.firestore_v1.query_profile import (
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    collection_id = "vector_search"
    collection_group = client.collection_group(collection_id)

    vector_query = collection_group.where("color", "==", "red").find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.EUCLIDEAN,
        limit=1,
    )
    # Tests either `stream()` or `get()`.
    method_under_test = getattr(vector_query, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=False))

    results_list = list(results)
    assert len(results_list) == 0

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert (
        plan_summary.indexes_used[0]["properties"]
        == "(color ASC, __name__ ASC, embedding VECTOR<3>)"
    )
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection group"

    # Verify execution_stats isn't available.
    with pytest.raises(
        QueryExplainError,
        match="execution_stats not available when explain_options.analyze=False",
    ):
        explain_metrics.execution_stats


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_create_document_w_subcollection(client, cleanup, database):
    collection_id = "doc-create-sub" + UNIQUE_RESOURCE_ID
    document_id = "doc" + UNIQUE_RESOURCE_ID
    document = client.document(collection_id, document_id)
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(document.delete)

    data = {"now": firestore.SERVER_TIMESTAMP}
    document.create(data)

    child_ids = ["child1", "child2"]

    for child_id in child_ids:
        subcollection = document.collection(child_id)
        _, subdoc = subcollection.add({"foo": "bar"})
        cleanup(subdoc.delete)

    children = document.collections()
    assert sorted(child.id for child in children) == sorted(child_ids)


def assert_timestamp_less(timestamp_pb1, timestamp_pb2):
    assert timestamp_pb1 < timestamp_pb2


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_document_collections_w_read_time(client, cleanup, database):
    collection_id = "doc-create-sub" + UNIQUE_RESOURCE_ID
    document_id = "doc" + UNIQUE_RESOURCE_ID
    document = client.document(collection_id, document_id)
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(document.delete)

    data = {"now": firestore.SERVER_TIMESTAMP}
    document.create(data)

    original_child_ids = ["child1", "child2"]
    read_time = None

    for child_id in original_child_ids:
        subcollection = document.collection(child_id)
        update_time, subdoc = subcollection.add({"foo": "bar"})
        read_time = (
            update_time if read_time is None or update_time > read_time else read_time
        )
        cleanup(subdoc.delete)

    update_time, newdoc = document.collection("child3").add({"foo": "bar"})
    cleanup(newdoc.delete)
    assert update_time > read_time

    # Compare the query at read_time to the query at new update time.
    original_children = document.collections(read_time=read_time)
    assert sorted(child.id for child in original_children) == sorted(original_child_ids)

    original_children = document.collections()
    assert sorted(child.id for child in original_children) == sorted(
        original_child_ids + ["child3"]
    )


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_no_document(client, database):
    document_id = "no_document" + UNIQUE_RESOURCE_ID
    document = client.document("abcde", document_id)
    snapshot = document.get()
    assert snapshot.to_dict() is None


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_document_set(client, cleanup, database):
    document_id = "for-set" + UNIQUE_RESOURCE_ID
    document = client.document("i-did-it", document_id)
    # Add to clean-up before API request (in case ``set()`` fails).
    cleanup(document.delete)

    # 0. Make sure the document doesn't exist yet
    snapshot = document.get()
    assert snapshot.to_dict() is None

    # 1. Use ``create()`` to create the document.
    data1 = {"foo": 88}
    write_result1 = document.create(data1)
    snapshot1 = document.get()
    assert snapshot1.to_dict() == data1
    # Make sure the update is what created the document.
    assert snapshot1.create_time == snapshot1.update_time
    assert snapshot1.update_time == write_result1.update_time

    # 2. Call ``set()`` again to overwrite.
    data2 = {"bar": None}
    write_result2 = document.set(data2)
    snapshot2 = document.get()
    assert snapshot2.to_dict() == data2
    # Make sure the create time hasn't changed.
    assert snapshot2.create_time == snapshot1.create_time
    assert snapshot2.update_time == write_result2.update_time


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_document_integer_field(client, cleanup, database):
    document_id = "for-set" + UNIQUE_RESOURCE_ID
    document = client.document("i-did-it", document_id)
    # Add to clean-up before API request (in case ``set()`` fails).
    cleanup(document.delete)

    data1 = {"1a": {"2b": "3c", "ab": "5e"}, "6f": {"7g": "8h", "cd": "0j"}}
    document.create(data1)

    data2 = {"1a.ab": "4d", "6f.7g": "9h"}
    document.update(data2)
    snapshot = document.get()
    expected = {"1a": {"2b": "3c", "ab": "4d"}, "6f": {"7g": "9h", "cd": "0j"}}
    assert snapshot.to_dict() == expected


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_document_set_merge(client, cleanup, database):
    document_id = "for-set" + UNIQUE_RESOURCE_ID
    document = client.document("i-did-it", document_id)
    # Add to clean-up before API request (in case ``set()`` fails).
    cleanup(document.delete)

    # 0. Make sure the document doesn't exist yet
    snapshot = document.get()
    assert not snapshot.exists

    # 1. Use ``create()`` to create the document.
    data1 = {"name": "Sam", "address": {"city": "SF", "state": "CA"}}
    write_result1 = document.create(data1)
    snapshot1 = document.get()
    assert snapshot1.to_dict() == data1
    # Make sure the update is what created the document.
    assert snapshot1.create_time == snapshot1.update_time
    assert snapshot1.update_time == write_result1.update_time

    # 2. Call ``set()`` to merge
    data2 = {"address": {"city": "LA"}}
    write_result2 = document.set(data2, merge=True)
    snapshot2 = document.get()
    assert snapshot2.to_dict() == {
        "name": "Sam",
        "address": {"city": "LA", "state": "CA"},
    }
    # Make sure the create time hasn't changed.
    assert snapshot2.create_time == snapshot1.create_time
    assert snapshot2.update_time == write_result2.update_time


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_document_set_w_int_field(client, cleanup, database):
    document_id = "set-int-key" + UNIQUE_RESOURCE_ID
    document = client.document("i-did-it", document_id)
    # Add to clean-up before API request (in case ``set()`` fails).
    cleanup(document.delete)

    # 0. Make sure the document doesn't exist yet
    snapshot = document.get()
    assert not snapshot.exists

    # 1. Use ``create()`` to create the document.
    before = {"testing": "1"}
    document.create(before)

    # 2. Replace using ``set()``.
    data = {"14": {"status": "active"}}
    document.set(data)

    # 3. Verify replaced data.
    snapshot1 = document.get()
    assert snapshot1.to_dict() == data


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_document_update_w_int_field(client, cleanup, database):
    # Attempt to reproduce #5489.
    document_id = "update-int-key" + UNIQUE_RESOURCE_ID
    document = client.document("i-did-it", document_id)
    # Add to clean-up before API request (in case ``set()`` fails).
    cleanup(document.delete)

    # 0. Make sure the document doesn't exist yet
    snapshot = document.get()
    assert not snapshot.exists

    # 1. Use ``create()`` to create the document.
    before = {"testing": "1"}
    document.create(before)

    # 2. Add values using ``update()``.
    data = {"14": {"status": "active"}}
    document.update(data)

    # 3. Verify updated data.
    expected = before.copy()
    expected.update(data)
    snapshot1 = document.get()
    assert snapshot1.to_dict() == expected


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Internal Issue b/137867104")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_update_document(client, cleanup, database):
    document_id = "for-update" + UNIQUE_RESOURCE_ID
    document = client.document("made", document_id)
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(document.delete)

    # 0. Try to update before the document exists.
    with pytest.raises(NotFound) as exc_info:
        document.update({"not": "there"})
    assert exc_info.value.message.startswith(MISSING_DOCUMENT)
    assert document_id in exc_info.value.message

    # 1. Try to update before the document exists (now with an option).
    with pytest.raises(NotFound) as exc_info:
        document.update({"still": "not-there"})
    assert exc_info.value.message.startswith(MISSING_DOCUMENT)
    assert document_id in exc_info.value.message

    # 2. Update and create the document (with an option).
    data = {"foo": {"bar": "baz"}, "scoop": {"barn": 981}, "other": True}
    write_result2 = document.create(data)

    # 3. Send an update without a field path (no option).
    field_updates3 = {"foo": {"quux": 800}}
    write_result3 = document.update(field_updates3)
    assert_timestamp_less(write_result2.update_time, write_result3.update_time)
    snapshot3 = document.get()
    expected3 = {
        "foo": field_updates3["foo"],
        "scoop": data["scoop"],
        "other": data["other"],
    }
    assert snapshot3.to_dict() == expected3

    # 4. Send an update **with** a field path and a delete and a valid
    #    "last timestamp" option.
    field_updates4 = {"scoop.silo": None, "other": firestore.DELETE_FIELD}
    option4 = client.write_option(last_update_time=snapshot3.update_time)
    write_result4 = document.update(field_updates4, option=option4)
    assert_timestamp_less(write_result3.update_time, write_result4.update_time)
    snapshot4 = document.get()
    expected4 = {
        "foo": field_updates3["foo"],
        "scoop": {"barn": data["scoop"]["barn"], "silo": field_updates4["scoop.silo"]},
    }
    assert snapshot4.to_dict() == expected4

    # 5. Call ``update()`` with invalid (in the past) "last timestamp" option.
    assert_timestamp_less(option4._last_update_time, snapshot4.update_time)
    with pytest.raises(FailedPrecondition) as exc_info:
        document.update({"bad": "time-past"}, option=option4)

    # 6. Call ``update()`` with invalid (in future) "last timestamp" option.
    timestamp_pb = _datetime_to_pb_timestamp(snapshot4.update_time)
    timestamp_pb.seconds += 3600

    option6 = client.write_option(last_update_time=timestamp_pb)
    # TODO(microgen):invalid argument thrown after microgen.
    # with pytest.raises(FailedPrecondition) as exc_info:
    with pytest.raises(InvalidArgument) as exc_info:
        document.update({"bad": "time-future"}, option=option6)


def check_snapshot(snapshot, document, data, write_result):
    assert snapshot.reference is document
    assert snapshot.to_dict() == data
    assert snapshot.exists
    assert snapshot.create_time == write_result.update_time
    assert snapshot.update_time == write_result.update_time


# We explicitly parameterize test_document_get with FIRESTORE_OTHER_DB to test
# named database path routing natively, without inflating the rest of the test suite.
@pytest.mark.parametrize("database", [None, FIRESTORE_OTHER_DB], indirect=True)
def test_document_get(client, cleanup, database):
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    document_id = "for-get" + UNIQUE_RESOURCE_ID
    document = client.document("created", document_id)
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(document.delete)

    # First make sure it doesn't exist.
    assert not document.get().exists

    ref_doc = client.document("top", "middle1", "middle2", "bottom")
    data = {
        "turtle": "power",
        "cheese": 19.5,
        "fire": 199099299,
        "referee": ref_doc,
        "gio": firestore.GeoPoint(45.5, 90.0),
        "deep": ["some", b"\xde\xad\xbe\xef"],
        "map": {"ice": True, "water": None, "vapor": {"deeper": now}},
    }
    write_result = document.create(data)
    snapshot = document.get()
    check_snapshot(snapshot, document, data, write_result)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_document_delete(client, cleanup, database):
    document_id = "deleted" + UNIQUE_RESOURCE_ID
    document = client.document("here-to-be", document_id)
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(document.delete)
    document.create({"not": "much"})

    # 1. Call ``delete()`` with invalid (in the past) "last timestamp" option.
    snapshot1 = document.get()
    timestamp_pb = _datetime_to_pb_timestamp(snapshot1.update_time)
    timestamp_pb.seconds += 3600

    option1 = client.write_option(last_update_time=timestamp_pb)
    # TODO(microgen):invalid argument thrown after microgen.
    # with pytest.raises(FailedPrecondition):
    with pytest.raises(InvalidArgument):
        document.delete(option=option1)

    # 2. Call ``delete()`` with invalid (in future) "last timestamp" option.
    timestamp_pb = _datetime_to_pb_timestamp(snapshot1.update_time)
    timestamp_pb.seconds += 3600

    option2 = client.write_option(last_update_time=timestamp_pb)
    # TODO(microgen):invalid argument thrown after microgen.
    # with pytest.raises(FailedPrecondition):
    with pytest.raises(InvalidArgument):
        document.delete(option=option2)

    # 3. Actually ``delete()`` the document.
    delete_time3 = document.delete()

    # 4. ``delete()`` again, even though we know the document is gone.
    delete_time4 = document.delete()
    assert_timestamp_less(delete_time3, delete_time4)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_collection_add(client, cleanup, database):
    # TODO(microgen): list_documents is returning a generator, not a list.
    # Consider if this is desired. Also, Document isn't hashable.
    collection_id = "coll-add" + UNIQUE_RESOURCE_ID
    collection1 = client.collection(collection_id)
    collection2 = client.collection(collection_id, "doc", "child")
    collection3 = client.collection(collection_id, "table", "child")
    explicit_doc_id = "hula" + UNIQUE_RESOURCE_ID

    assert set(collection1.list_documents()) == set()
    assert set(collection2.list_documents()) == set()
    assert set(collection3.list_documents()) == set()

    # Auto-ID at top-level.
    data1 = {"foo": "bar"}
    update_time1, document_ref1 = collection1.add(data1)
    cleanup(document_ref1.delete)
    assert set(collection1.list_documents()) == {document_ref1}
    assert set(collection2.list_documents()) == set()
    assert set(collection3.list_documents()) == set()
    snapshot1 = document_ref1.get()
    assert snapshot1.to_dict() == data1
    assert snapshot1.update_time == update_time1
    assert RANDOM_ID_REGEX.match(document_ref1.id)

    # Explicit ID at top-level.
    data2 = {"baz": 999}
    update_time2, document_ref2 = collection1.add(data2, document_id=explicit_doc_id)
    cleanup(document_ref2.delete)
    assert set(collection1.list_documents()) == {document_ref1, document_ref2}
    assert set(collection2.list_documents()) == set()
    assert set(collection3.list_documents()) == set()
    snapshot2 = document_ref2.get()
    assert snapshot2.to_dict() == data2
    assert snapshot2.create_time == update_time2
    assert snapshot2.update_time == update_time2
    assert document_ref2.id == explicit_doc_id

    nested_ref = collection1.document("doc")

    # Auto-ID for nested collection.
    data3 = {"quux": b"\x00\x01\x02\x03"}
    update_time3, document_ref3 = collection2.add(data3)
    cleanup(document_ref3.delete)
    assert set(collection1.list_documents()) == {
        document_ref1,
        document_ref2,
        nested_ref,
    }
    assert set(collection2.list_documents()) == {document_ref3}
    assert set(collection3.list_documents()) == set()
    snapshot3 = document_ref3.get()
    assert snapshot3.to_dict() == data3
    assert snapshot3.update_time == update_time3
    assert RANDOM_ID_REGEX.match(document_ref3.id)

    # Explicit for nested collection.
    data4 = {"kazaam": None, "bad": False}
    update_time4, document_ref4 = collection2.add(data4, document_id=explicit_doc_id)
    cleanup(document_ref4.delete)
    assert set(collection1.list_documents()) == {
        document_ref1,
        document_ref2,
        nested_ref,
    }
    assert set(collection2.list_documents()) == {document_ref3, document_ref4}
    assert set(collection3.list_documents()) == set()
    snapshot4 = document_ref4.get()
    assert snapshot4.to_dict() == data4
    assert snapshot4.create_time == update_time4
    assert snapshot4.update_time == update_time4
    assert document_ref4.id == explicit_doc_id

    # Exercise "missing" document (no doc, but subcollection).
    data5 = {"bam": 123, "folyk": False}
    update_time5, document_ref5 = collection3.add(data5)
    cleanup(document_ref5.delete)
    missing_ref = collection1.document("table")
    assert set(collection1.list_documents()) == {
        document_ref1,
        document_ref2,
        nested_ref,
        missing_ref,
    }
    assert set(collection2.list_documents()) == {document_ref3, document_ref4}
    assert set(collection3.list_documents()) == {document_ref5}


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_list_collections_with_read_time(client, cleanup, database):
    # TODO(microgen): list_documents is returning a generator, not a list.
    # Consider if this is desired. Also, Document isn't hashable.
    collection_id = "coll-add" + UNIQUE_RESOURCE_ID
    collection = client.collection(collection_id)

    assert set(collection.list_documents()) == set()

    data1 = {"foo": "bar"}
    update_time1, document_ref1 = collection.add(data1)
    cleanup(document_ref1.delete)
    assert set(collection.list_documents()) == {document_ref1}

    data2 = {"bar": "baz"}
    update_time2, document_ref2 = collection.add(data2)
    cleanup(document_ref2.delete)
    assert set(collection.list_documents()) == {document_ref1, document_ref2}
    assert set(collection.list_documents(read_time=update_time1)) == {document_ref1}
    assert set(collection.list_documents(read_time=update_time2)) == {
        document_ref1,
        document_ref2,
    }


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_unicode_doc(client, cleanup, database):
    collection_id = "coll-unicode" + UNIQUE_RESOURCE_ID
    collection = client.collection(collection_id)
    explicit_doc_id = "中餐" + UNIQUE_RESOURCE_ID

    assert set(collection.list_documents()) == set()

    data = {"baz": 0}
    update_time, document_ref = collection.add(data, document_id=explicit_doc_id)
    cleanup(document_ref.delete)
    assert set(collection.list_documents()) == {document_ref, document_ref}
    snapshot = document_ref.get()
    assert snapshot.to_dict() == data
    assert snapshot.create_time == update_time
    assert snapshot.update_time == update_time
    assert document_ref.id == explicit_doc_id
    assert snapshot.reference.id == explicit_doc_id

    # update doc
    data2 = {"baz": 9}
    snapshot.reference.update(data2)
    snapshot2 = document_ref.get()
    assert snapshot2.to_dict() == data2
    assert snapshot2.reference.id == explicit_doc_id


@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_bson_document_read_and_write(client, cleanup, database):
    """Test read and write operations for BSON types on Enterprise DB."""
    collection_id = "bson_type_read_write_" + UNIQUE_RESOURCE_ID
    doc_ref = client.collection(collection_id).document("bson_doc")
    cleanup(doc_ref.delete)

    bson_payload = {
        "user_id": BSONObjectId("507f191e810c19729de860ea"),
        "min_key": BSONMinKey(),
        "max_key": BSONMaxKey(),
        "int32_val": BSONInt32(42),
        "binary_val_sub0": b"hello",
        "binary_val_sub128": BSONBinary(b"world", subtype=128),
        "timestamp_val": BSONTimestamp(1700000000, 1),
        "regex_val": BSONRegex("^hello.*$", options="i"),
        "decimal128_val": BSONDecimal128("123.45"),
    }

    doc_ref.set(bson_payload)

    snapshot = doc_ref.get()
    assert snapshot.exists
    assert snapshot.to_dict() == bson_payload


@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_bson_regex_invalid_options(client, cleanup, database):
    """Test write operations for BSONRegex with invalid options against backend."""
    collection_id = "bson_regex_invalid_" + UNIQUE_RESOURCE_ID
    doc_ref = client.collection(collection_id).document("invalid_regex")
    cleanup(doc_ref.delete)

    # Backend enforces supported BSON regex flags ('i', 'm', 's', 'u', 'x')
    # and rejects unsupported options (e.g. 'l') with InvalidArgument.
    with pytest.raises(InvalidArgument) as exc_info:
        doc_ref.set({"regex_val": BSONRegex("hello", options="l")})
    assert "Invalid regex option" in exc_info.value.message


@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_bson_decimal128_special_values(client, cleanup, database):
    """Test write and read operations for BSONDecimal128 special values against backend."""
    collection_id = "bson_decimal128_special_" + UNIQUE_RESOURCE_ID
    doc_ref = client.collection(collection_id).document("special_decimals")
    cleanup(doc_ref.delete)

    # Firestore backend accepts "inf", "-inf", and "NaN", automatically
    # normalizing them to "Infinity", "-Infinity", and "NaN" upon storage.
    doc_ref.set(
        {
            "inf_val": BSONDecimal128("inf"),
            "neg_inf_val": BSONDecimal128("-inf"),
            "nan_val": BSONDecimal128("NaN"),
        }
    )

    snapshot = doc_ref.get()
    assert snapshot.exists
    assert snapshot.to_dict() == {
        "inf_val": BSONDecimal128("Infinity"),
        "neg_inf_val": BSONDecimal128("-Infinity"),
        "nan_val": BSONDecimal128("NaN"),
    }


@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_bson_query_ordering(client, cleanup, database):
    """Test server query ordering for BSON types."""
    collection_id = "bson_ordering_" + UNIQUE_RESOURCE_ID
    coll_ref = client.collection(collection_id)

    doc1 = coll_ref.document("doc1")
    doc2 = coll_ref.document("doc2")
    doc3 = coll_ref.document("doc3")
    cleanup(doc1.delete)
    cleanup(doc2.delete)
    cleanup(doc3.delete)

    doc1.set({"val": BSONMinKey()})
    doc2.set({"val": BSONInt32(10)})
    doc3.set({"val": BSONMaxKey()})

    query = coll_ref.order_by("val")
    results = [doc.to_dict()["val"] for doc in query.stream()]
    assert results == [BSONMinKey(), BSONInt32(10), BSONMaxKey()]


@pytest.fixture(scope="module")
def query_docs(client, database):
    collection_id = "qs" + UNIQUE_RESOURCE_ID
    sub_collection = "child" + UNIQUE_RESOURCE_ID
    collection = client.collection(collection_id, "doc", sub_collection)

    cleanup = []
    stored = {}
    num_vals = 5
    allowed_vals = range(num_vals)
    for a_val in allowed_vals:
        for b_val in allowed_vals:
            document_data = {
                "a": a_val,
                "b": b_val,
                "c": [a_val, num_vals * 100],
                "stats": {"sum": a_val + b_val, "product": a_val * b_val},
            }
            _, doc_ref = collection.add(document_data)
            # Add to clean-up.
            cleanup.append(doc_ref.delete)
            stored[doc_ref.id] = document_data

    yield collection, stored, allowed_vals

    for operation in cleanup:
        operation()


@pytest.fixture(scope="module")
def collection(query_docs):
    collection, _, _ = query_docs
    return collection


@pytest.fixture(scope="module")
def query(collection):
    return collection.where(filter=FieldFilter("a", "==", 1))


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_legacy_where(query_docs, database, verify_pipeline):
    """Assert the legacy code still works and returns value"""
    collection, stored, allowed_vals = query_docs
    with pytest.warns(
        UserWarning,
        match="Detected filter using positional arguments",
    ):
        query = collection.where("a", "==", 1)
        values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
        assert len(values) == len(allowed_vals)
        for key, value in values.items():
            assert stored[key] == value
            assert value["a"] == 1
        verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_simple_field_eq_op(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    query = collection.where(filter=FieldFilter("a", "==", 1))
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(values) == len(allowed_vals)
    for key, value in values.items():
        assert stored[key] == value
        assert value["a"] == 1
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_simple_field_array_contains_op(
    query_docs, database, verify_pipeline
):
    collection, stored, allowed_vals = query_docs
    query = collection.where(filter=FieldFilter("c", "array_contains", 1))
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(values) == len(allowed_vals)
    for key, value in values.items():
        assert stored[key] == value
        assert value["a"] == 1
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_simple_field_in_op(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(filter=FieldFilter("a", "in", [1, num_vals + 100]))
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(values) == len(allowed_vals)
    for key, value in values.items():
        assert stored[key] == value
        assert value["a"] == 1
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_not_eq_op(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    query = collection.where(filter=FieldFilter("stats.sum", "!=", 4))
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(values) == 20
    ab_pairs2 = set()
    for key, value in values.items():
        assert stored[key] == value
        ab_pairs2.add((value["a"], value["b"]))

    expected_ab_pairs = set(
        [
            (a_val, b_val)
            for a_val in allowed_vals
            for b_val in allowed_vals
            if a_val + b_val != 4
        ]
    )
    assert expected_ab_pairs == ab_pairs2
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_simple_not_in_op(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(
        filter=FieldFilter("stats.sum", "not-in", [2, num_vals + 100])
    )
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}

    assert len(values) == 22
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_simple_field_array_contains_any_op(
    query_docs, database, verify_pipeline
):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(
        filter=FieldFilter("c", "array_contains_any", [1, num_vals * 200])
    )
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(values) == len(allowed_vals)
    for key, value in values.items():
        assert stored[key] == value
        assert value["a"] == 1
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_order_by(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    query = collection.order_by("b", direction=firestore.Query.DESCENDING)
    values = [(snapshot.id, snapshot.to_dict()) for snapshot in query.stream()]
    assert len(values) == len(stored)
    b_vals = []
    for key, value in values:
        assert stored[key] == value
        b_vals.append(value["b"])
    # Make sure the ``b``-values are in DESCENDING order.
    assert sorted(b_vals, reverse=True) == b_vals
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_field_path(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    query = collection.where(filter=FieldFilter("stats.sum", ">", 4))
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(values) == 10
    ab_pairs2 = set()
    for key, value in values.items():
        assert stored[key] == value
        ab_pairs2.add((value["a"], value["b"]))

    expected_ab_pairs = set(
        [
            (a_val, b_val)
            for a_val in allowed_vals
            for b_val in allowed_vals
            if a_val + b_val > 4
        ]
    )
    assert expected_ab_pairs == ab_pairs2
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_stream_w_start_end_cursor(query_docs, database):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = (
        collection.order_by("a")
        .start_at({"a": num_vals - 2})
        .end_before({"a": num_vals - 1})
    )
    values = [(snapshot.id, snapshot.to_dict()) for snapshot in query.stream()]
    assert len(values) == num_vals
    for key, value in values:
        assert stored[key] == value
        assert value["a"] == num_vals - 2


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_wo_results(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(filter=FieldFilter("b", "==", num_vals + 100))
    values = list(query.stream())
    assert len(values) == 0
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_stream_w_projection(query_docs, database):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(filter=FieldFilter("b", "<=", 1)).select(
        ["a", "stats.product"]
    )
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(values) == num_vals * 2  # a ANY, b in (0, 1)
    for key, value in values.items():
        expected = {
            "a": stored[key]["a"],
            "stats": {"product": stored[key]["stats"]["product"]},
        }
        assert expected == value


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_multiple_filters(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    query = collection.where(filter=FieldFilter("stats.product", ">", 5)).where(
        filter=FieldFilter("stats.product", "<", 10)
    )
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    matching_pairs = [
        (a_val, b_val)
        for a_val in allowed_vals
        for b_val in allowed_vals
        if 5 < a_val * b_val < 10
    ]
    assert len(values) == len(matching_pairs)
    for key, value in values.items():
        assert stored[key] == value
        pair = (value["a"], value["b"])
        assert pair in matching_pairs
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_w_offset(query_docs, database, verify_pipeline):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    offset = 3
    query = collection.where(filter=FieldFilter("b", "==", 2)).offset(offset)
    values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    # NOTE: We don't check the ``a``-values, since that would require
    #       an ``order_by('a')``, which combined with the ``b == 2``
    #       filter would necessitate an index.
    assert len(values) == num_vals - offset
    for key, value in values.items():
        assert stored[key] == value
        assert value["b"] == 2
    verify_pipeline(query)


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_stream_or_get_w_no_explain_options(
    query_docs, database, method, verify_pipeline
):
    from google.cloud.firestore_v1.query_profile import QueryExplainError

    collection, _, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(filter=FieldFilter("a", "in", [1, num_vals + 100]))

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(query, method)
    results = method_under_test()

    # If no explain_option is passed, raise an exception if explain_metrics
    # is called
    with pytest.raises(QueryExplainError, match="explain_options not set on query"):
        results.get_explain_metrics()
    verify_pipeline(query)


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_stream_or_get_w_explain_options_analyze_true(
    query_docs, database, method
):
    from google.cloud.firestore_v1.query_profile import (
        ExecutionStats,
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    collection, _, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(filter=FieldFilter("a", "in", [1, num_vals + 100]))

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(query, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=True))

    # With `stream()`, an exception should be raised when accessing
    # explain_metrics before query finishes.
    if method == "stream":
        with pytest.raises(
            QueryExplainError,
            match="explain_metrics not available until query is complete",
        ):
            results.get_explain_metrics()

    # Finish iterating results, and explain_metrics should be available.
    num_results = len(list(results))

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert plan_summary.indexes_used[0]["properties"] == "(a ASC, __name__ ASC)"
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection"

    # Verify execution_stats.
    execution_stats = explain_metrics.execution_stats
    assert isinstance(execution_stats, ExecutionStats)
    assert execution_stats.results_returned == num_results
    assert execution_stats.read_operations == num_results
    duration = execution_stats.execution_duration.total_seconds()
    assert duration > 0
    assert duration < 1  # we expect a number closer to 0.05
    assert isinstance(execution_stats.debug_stats, dict)
    assert "billing_details" in execution_stats.debug_stats
    assert "documents_scanned" in execution_stats.debug_stats
    assert "index_entries_scanned" in execution_stats.debug_stats
    assert len(execution_stats.debug_stats) > 0


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_stream_or_get_w_explain_options_analyze_false(
    query_docs, database, method
):
    from google.cloud.firestore_v1.query_profile import (
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    collection, _, allowed_vals = query_docs
    num_vals = len(allowed_vals)
    query = collection.where(filter=FieldFilter("a", "in", [1, num_vals + 100]))

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(query, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=False))

    # Verify that no results are returned.
    results_list = list(results)
    assert len(results_list) == 0

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert plan_summary.indexes_used[0]["properties"] == "(a ASC, __name__ ASC)"
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection"

    # Verify execution_stats isn't available.
    with pytest.raises(
        QueryExplainError,
        match="execution_stats not available when explain_options.analyze=False",
    ):
        explain_metrics.execution_stats


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["execute", "stream"])
@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_pipeline_explain_options_explain_mode(database, method, query_docs):
    from google.cloud.firestore_v1.query_profile import (
        ExplainStats,
        PipelineExplainOptions,
    )
    from google.cloud.firestore_v1.types.explain_stats import (
        ExplainStats as ExplainStats_pb,
    )

    collection, _, _ = query_docs
    client = collection._client
    query = collection.where(filter=FieldFilter("a", "==", 1))
    pipeline = client.pipeline().create_from(query)

    # Tests either `execute()` or `stream()`.
    method_under_test = getattr(pipeline, method)
    explain_options = PipelineExplainOptions(mode="explain")

    results = method_under_test(explain_options=explain_options)
    results_list = list(results)
    assert len(results_list) == 0

    # Verify explain_stats.
    explain_stats = results.explain_stats
    assert isinstance(explain_stats, ExplainStats)
    assert isinstance(explain_stats.get_raw(), ExplainStats_pb)


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["execute", "stream"])
@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_pipeline_explain_options_analyze_mode(database, method, query_docs):
    from google.cloud.firestore_v1.query_profile import (
        ExplainStats,
        PipelineExplainOptions,
        QueryExplainError,
    )
    from google.cloud.firestore_v1.types.explain_stats import (
        ExplainStats as ExplainStats_pb,
    )

    collection, _, allowed_vals = query_docs
    client = collection._client
    query = collection.where(filter=FieldFilter("a", "==", 1))
    pipeline = client.pipeline().create_from(query)

    # Tests either `execute()` or `stream()`.
    method_under_test = getattr(pipeline, method)
    results = method_under_test(explain_options=PipelineExplainOptions())

    if method == "stream":
        # check for error accessing explain stats before iterating
        with pytest.raises(
            QueryExplainError,
            match="explain_stats not available until query is complete",
        ):
            results.explain_stats

    # Finish iterating results, and explain_stats should be available.
    results_list = list(results)
    num_results = len(results_list)
    assert num_results == len(allowed_vals)

    # Verify explain_stats.
    explain_stats = results.explain_stats
    assert isinstance(explain_stats, ExplainStats)

    assert isinstance(explain_stats.get_raw(), ExplainStats_pb)
    text_stats = explain_stats.get_text()
    assert "Execution:" in text_stats


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["execute", "stream"])
@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_pipeline_explain_options_using_additional_options(
    database, method, query_docs
):
    """additional_options field allows passing in arbitrary options. Test with explain_options"""
    from google.cloud.firestore_v1.query_profile import (
        ExplainStats,
        PipelineExplainOptions,
    )
    from google.cloud.firestore_v1.types.explain_stats import (
        ExplainStats as ExplainStats_pb,
    )

    collection, _, allowed_vals = query_docs
    client = collection._client
    query = collection.where(filter=FieldFilter("a", "==", 1))
    pipeline = client.pipeline().create_from(query)

    # Tests either `execute()` or `stream()`.
    method_under_test = getattr(pipeline, method)

    encoded_options = {"explain_options": PipelineExplainOptions()._to_value()}

    results = method_under_test(
        explain_options=mock.Mock(), additional_options=encoded_options
    )

    # Finish iterating results, and explain_stats should be available./w_read
    results_list = list(results)
    num_results = len(results_list)
    assert num_results == len(allowed_vals)

    # Verify explain_stats.
    explain_stats = results.explain_stats
    assert isinstance(explain_stats, ExplainStats)

    assert isinstance(explain_stats.get_raw(), ExplainStats_pb)
    text_stats = explain_stats.get_text()
    assert "Execution:" in text_stats


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_stream_w_read_time(query_docs, cleanup, database):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)

    # Find the most recent read_time in collections
    read_time = max(docref.get().read_time for docref in collection.list_documents())
    new_data = {
        "a": 9000,
        "b": 1,
        "c": [10000, 1000],
        "stats": {"sum": 9001, "product": 9000},
    }
    _, new_ref = collection.add(new_data)
    # Add to clean-up.
    cleanup(new_ref.delete)
    stored[new_ref.id] = new_data

    # Compare query at read_time to query at current time.
    query = collection.where(filter=FieldFilter("b", "==", 1))
    values = {
        snapshot.id: snapshot.to_dict()
        for snapshot in query.stream(read_time=read_time)
    }
    assert len(values) == num_vals
    assert new_ref.id not in values
    for key, value in values.items():
        assert stored[key] == value
        assert value["b"] == 1
        assert value["a"] != 9000
        assert key != new_ref

    new_values = {snapshot.id: snapshot.to_dict() for snapshot in query.stream()}
    assert len(new_values) == num_vals + 1
    assert new_ref.id in new_values
    assert new_values[new_ref.id] == new_data


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Pipeline query not supported in emulator."
)
@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_pipeline_w_read_time(query_docs, cleanup, database):
    collection, stored, allowed_vals = query_docs
    num_vals = len(allowed_vals)

    # Find a read_time before adding the new document.
    snapshots = collection.get()
    read_time = snapshots[0].read_time

    new_data = {
        "a": 9000,
        "b": 1,
    }
    _, new_ref = collection.add(new_data)
    # Add to clean-up.
    cleanup(new_ref.delete)
    stored[new_ref.id] = new_data

    client = collection._client
    query = collection.where(filter=FieldFilter("b", "==", 1))
    pipeline = client.pipeline().create_from(query)

    # new query should have new_data
    new_results = list(pipeline.stream())
    new_values = {result.ref.id: result.data() for result in new_results}
    assert len(new_values) == num_vals + 1
    assert new_ref.id in new_values
    assert new_values[new_ref.id] == new_data

    # query with read_time should not have new)data
    results = list(pipeline.stream(read_time=read_time))

    values = {result.ref.id: result.data() for result in results}

    assert len(values) == num_vals
    assert new_ref.id not in values
    for key, value in values.items():
        assert stored[key] == value
        assert value["b"] == 1
        assert value["a"] != 9000
        assert key != new_ref.id


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_with_order_dot_key(client, cleanup, database):
    db = client
    collection_id = "collek" + UNIQUE_RESOURCE_ID
    collection = db.collection(collection_id)
    for index in range(100, -1, -1):
        doc = collection.document("test_{:09d}".format(index))
        data = {"count": 10 * index, "wordcount": {"page1": index * 10 + 100}}
        doc.set(data)
        cleanup(doc.delete)
    query = collection.order_by("wordcount.page1").limit(3)
    data = [doc.to_dict()["wordcount"]["page1"] for doc in query.stream()]
    assert [100, 110, 120] == data
    query2 = collection.order_by("wordcount.page1").limit(3)
    for snapshot in query2.stream():
        last_value = snapshot.get("wordcount.page1")
    cursor_with_nested_keys = {"wordcount": {"page1": last_value}}
    query3 = (
        collection.order_by("wordcount.page1")
        .start_after(cursor_with_nested_keys)
        .limit(3)
    )
    found = list(query3.stream())
    found_data = [
        {"count": 30, "wordcount": {"page1": 130}},
        {"count": 40, "wordcount": {"page1": 140}},
        {"count": 50, "wordcount": {"page1": 150}},
    ]
    assert found_data == [snap.to_dict() for snap in found]
    cursor_with_dotted_paths = {"wordcount.page1": last_value}
    query4 = (
        collection.order_by("wordcount.page1")
        .start_after(cursor_with_dotted_paths)
        .limit(3)
    )
    cursor_with_key_data = list(query4.stream())
    assert found_data == [snap.to_dict() for snap in cursor_with_key_data]


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_unary(client, cleanup, database, verify_pipeline):
    collection_name = "unary" + UNIQUE_RESOURCE_ID
    collection = client.collection(collection_name)
    field_name = "foo"

    _, document0 = collection.add({field_name: None})
    # Add to clean-up.
    cleanup(document0.delete)

    nan_val = float("nan")
    _, document1 = collection.add({field_name: nan_val})
    # Add to clean-up.
    cleanup(document1.delete)

    _, document2 = collection.add({field_name: 123})
    # Add to clean-up.
    cleanup(document2.delete)

    # 0. Query for null.
    query0 = collection.where(filter=FieldFilter(field_name, "==", None))
    values0 = list(query0.stream())
    assert len(values0) == 1
    snapshot0 = values0[0]
    assert snapshot0.reference._path == document0._path
    assert snapshot0.to_dict() == {field_name: None}
    verify_pipeline(query0)

    # 1. Query for a NAN.
    query1 = collection.where(filter=FieldFilter(field_name, "==", nan_val))
    values1 = list(query1.stream())
    assert len(values1) == 1
    snapshot1 = values1[0]
    assert snapshot1.reference._path == document1._path
    data1 = snapshot1.to_dict()
    assert len(data1) == 1
    assert math.isnan(data1[field_name])
    verify_pipeline(query1)

    # 2. Query for not null
    query2 = collection.where(filter=FieldFilter(field_name, "!=", None))
    values2 = list(query2.stream())
    assert len(values2) == 2
    # should fetch documents 1 (NaN) and 2 (int)
    assert any(snapshot.reference._path == document1._path for snapshot in values2)
    assert any(snapshot.reference._path == document2._path for snapshot in values2)

    # 3. Query for not NAN.
    query3 = collection.where(filter=FieldFilter(field_name, "!=", nan_val))
    values3 = list(query3.stream())
    assert len(values3) == 1
    snapshot3 = values3[0]
    assert snapshot3.reference._path == document2._path
    # only document2 is not NaN
    assert snapshot3.to_dict() == {field_name: 123}


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_collection_group_queries(client, cleanup, database, verify_pipeline):
    collection_group = "b" + UNIQUE_RESOURCE_ID

    doc_paths = [
        "abc/123/" + collection_group + "/cg-doc1",
        "abc/123/" + collection_group + "/cg-doc2",
        collection_group + "/cg-doc3",
        collection_group + "/cg-doc4",
        "def/456/" + collection_group + "/cg-doc5",
        collection_group + "/virtual-doc/nested-coll/not-cg-doc",
        "x" + collection_group + "/not-cg-doc",
        collection_group + "x/not-cg-doc",
        "abc/123/" + collection_group + "x/not-cg-doc",
        "abc/123/x" + collection_group + "/not-cg-doc",
        "abc/" + collection_group,
    ]

    batch = client.batch()
    for doc_path in doc_paths:
        doc_ref = client.document(doc_path)
        batch.set(doc_ref, {"x": 1})
        cleanup(doc_ref.delete)

    batch.commit()

    query = client.collection_group(collection_group)
    snapshots = list(query.stream())
    found = [snapshot.id for snapshot in snapshots]
    expected = ["cg-doc1", "cg-doc2", "cg-doc3", "cg-doc4", "cg-doc5"]
    assert set(found) == set(expected)
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_collection_group_queries_startat_endat(client, cleanup, database):
    collection_group = "b" + UNIQUE_RESOURCE_ID

    doc_paths = [
        "a/a/" + collection_group + "/cg-doc1",
        "a/b/a/b/" + collection_group + "/cg-doc2",
        "a/b/" + collection_group + "/cg-doc3",
        "a/b/c/d/" + collection_group + "/cg-doc4",
        "a/c/" + collection_group + "/cg-doc5",
        collection_group + "/cg-doc6",
        "a/b/nope/nope",
    ]

    batch = client.batch()
    for doc_path in doc_paths:
        doc_ref = client.document(doc_path)
        batch.set(doc_ref, {"x": doc_path})
        cleanup(doc_ref.delete)

    batch.commit()

    query = (
        client.collection_group(collection_group)
        .order_by("__name__")
        .start_at([client.document("a/b")])
        .end_at([client.document("a/b0")])
    )
    snapshots = list(query.stream())
    found = set(snapshot.id for snapshot in snapshots)
    assert found == set(["cg-doc2", "cg-doc3", "cg-doc4"])

    query = (
        client.collection_group(collection_group)
        .order_by("__name__")
        .start_after([client.document("a/b")])
        .end_before([client.document("a/b/" + collection_group + "/cg-doc3")])
    )
    snapshots = list(query.stream())
    found = set(snapshot.id for snapshot in snapshots)
    assert found == set(["cg-doc2"])


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_collection_group_queries_filters(client, cleanup, database, verify_pipeline):
    collection_group = "b" + UNIQUE_RESOURCE_ID

    doc_paths = [
        "a/a/" + collection_group + "/cg-doc1",
        "a/b/a/b/" + collection_group + "/cg-doc2",
        "a/b/" + collection_group + "/cg-doc3",
        "a/b/c/d/" + collection_group + "/cg-doc4",
        "a/c/" + collection_group + "/cg-doc5",
        collection_group + "/cg-doc6",
        "a/b/nope/nope",
    ]

    batch = client.batch()

    for index, doc_path in enumerate(doc_paths):
        doc_ref = client.document(doc_path)
        batch.set(doc_ref, {"x": index})
        cleanup(doc_ref.delete)

    batch.commit()

    query = (
        client.collection_group(collection_group)
        .where(
            filter=FieldFilter(
                firestore.field_path.FieldPath.document_id(),
                ">=",
                client.document("a/b"),
            )
        )
        .where(
            filter=FieldFilter(
                firestore.field_path.FieldPath.document_id(),
                "<=",
                client.document("a/b0"),
            )
        )
    )
    snapshots = list(query.stream())
    found = set(snapshot.id for snapshot in snapshots)
    assert found == set(["cg-doc2", "cg-doc3", "cg-doc4"])
    verify_pipeline(query)

    query = (
        client.collection_group(collection_group)
        .where(
            filter=FieldFilter(
                firestore.field_path.FieldPath.document_id(),
                ">",
                client.document("a/b"),
            )
        )
        .where(
            filter=FieldFilter(
                firestore.field_path.FieldPath.document_id(),
                "<",
                client.document("a/b/{}/cg-doc3".format(collection_group)),
            )
        )
    )
    snapshots = list(query.stream())
    found = set(snapshot.id for snapshot in snapshots)
    assert found == set(["cg-doc2"])
    verify_pipeline(query)


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="PartitionQuery not implemented in emulator"
)
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_partition_query_no_partitions(client, cleanup, database):
    collection_group = "b" + UNIQUE_RESOURCE_ID

    # less than minimum partition size
    doc_paths = [
        "abc/123/" + collection_group + "/cg-doc1",
        "abc/123/" + collection_group + "/cg-doc2",
        collection_group + "/cg-doc3",
        collection_group + "/cg-doc4",
        "def/456/" + collection_group + "/cg-doc5",
    ]

    batch = client.batch()
    cleanup_batch = client.batch()
    cleanup(cleanup_batch.commit)
    for doc_path in doc_paths:
        doc_ref = client.document(doc_path)
        batch.set(doc_ref, {"x": 1})
        cleanup_batch.delete(doc_ref)

    batch.commit()

    query = client.collection_group(collection_group)
    partitions = list(query.get_partitions(3))
    streams = [partition.query().stream() for partition in partitions]
    snapshots = itertools.chain(*streams)
    found = [snapshot.id for snapshot in snapshots]
    expected = ["cg-doc1", "cg-doc2", "cg-doc3", "cg-doc4", "cg-doc5"]
    assert found == expected


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="PartitionQuery not implemented in emulator"
)
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_partition_query(client, cleanup, database):
    collection_group = "b" + UNIQUE_RESOURCE_ID
    n_docs = 128 * 2 + 127  # Minimum partition size is 128
    parents = itertools.cycle(("", "abc/123/", "def/456/", "ghi/789/"))
    batch = client.batch()
    cleanup_batch = client.batch()
    cleanup(cleanup_batch.commit)
    expected = []
    for i, parent in zip(range(n_docs), parents):
        doc_path = parent + collection_group + f"/cg-doc{i:03d}"
        doc_ref = client.document(doc_path)
        batch.set(doc_ref, {"x": i})
        cleanup_batch.delete(doc_ref)
        expected.append(doc_path)

    batch.commit()

    query = client.collection_group(collection_group)
    partitions = list(query.get_partitions(3))
    streams = [partition.query().stream() for partition in partitions]
    snapshots = itertools.chain(*streams)
    found = [snapshot.reference.path for snapshot in snapshots]
    expected.sort()
    assert found == expected


@pytest.mark.skipif(FIRESTORE_EMULATOR, reason="Internal Issue b/137865992")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_get_all(client, cleanup, database):
    collection_name = "get-all" + UNIQUE_RESOURCE_ID

    document1 = client.document(collection_name, "a")
    document2 = client.document(collection_name, "b")
    document3 = client.document(collection_name, "c")
    # Add to clean-up before API requests (in case ``create()`` fails).
    cleanup(document1.delete)
    cleanup(document2.delete)
    cleanup(document3.delete)

    data1 = {"a": {"b": 2, "c": 3}, "d": 4, "e": 0}
    write_result1 = document1.create(data1)
    data3 = {"a": {"b": 5, "c": 6}, "d": 7, "e": 100}
    write_result3 = document3.create(data3)

    read_time = write_result3.update_time

    # 0. Get 3 unique documents, one of which is missing.
    snapshots = list(client.get_all([document1, document2, document3]))

    assert snapshots[0].exists
    assert snapshots[1].exists
    assert not snapshots[2].exists

    snapshots = [snapshot for snapshot in snapshots if snapshot.exists]
    id_attr = operator.attrgetter("id")
    snapshots.sort(key=id_attr)

    snapshot1, snapshot3 = snapshots
    check_snapshot(snapshot1, document1, data1, write_result1)
    check_snapshot(snapshot3, document3, data3, write_result3)

    # 1. Get 2 colliding documents.
    document1_also = client.document(collection_name, "a")
    snapshots = list(client.get_all([document1, document1_also]))

    assert len(snapshots) == 1
    assert document1 is not document1_also
    check_snapshot(snapshots[0], document1_also, data1, write_result1)

    # 2. Use ``field_paths`` / projection in ``get_all()``.
    snapshots = list(client.get_all([document1, document3], field_paths=["a.b", "d"]))

    assert len(snapshots) == 2
    snapshots.sort(key=id_attr)

    snapshot1, snapshot3 = snapshots
    restricted1 = {"a": {"b": data1["a"]["b"]}, "d": data1["d"]}
    check_snapshot(snapshot1, document1, restricted1, write_result1)
    restricted3 = {"a": {"b": data3["a"]["b"]}, "d": data3["d"]}
    check_snapshot(snapshot3, document3, restricted3, write_result3)

    # 3. Use ``read_time`` in ``get_all``
    new_data = {"a": {"b": 8, "c": 9}, "d": 10, "e": 1010}
    document1.update(new_data)
    document2.create(new_data)
    document3.update(new_data)

    snapshots = list(
        client.get_all([document1, document2, document3], read_time=read_time)
    )
    assert snapshots[0].exists
    assert snapshots[1].exists
    assert not snapshots[2].exists

    snapshots = [snapshot for snapshot in snapshots if snapshot.exists]
    id_attr = operator.attrgetter("id")
    snapshots.sort(key=id_attr)

    snapshot1, snapshot3 = snapshots
    check_snapshot(snapshot1, document1, data1, write_result1)
    check_snapshot(snapshot3, document3, data3, write_result3)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_batch(client, cleanup, database):
    collection_name = "batch" + UNIQUE_RESOURCE_ID

    document1 = client.document(collection_name, "abc")
    document2 = client.document(collection_name, "mno")
    document3 = client.document(collection_name, "xyz")
    # Add to clean-up before API request (in case ``create()`` fails).
    cleanup(document1.delete)
    cleanup(document2.delete)
    cleanup(document3.delete)

    data2 = {"some": {"deep": "stuff", "and": "here"}, "water": 100.0}
    document2.create(data2)
    document3.create({"other": 19})

    batch = client.batch()
    data1 = {"all": True}
    batch.create(document1, data1)
    new_value = "there"
    batch.update(document2, {"some.and": new_value})
    batch.delete(document3)
    write_results = batch.commit()

    assert len(write_results) == 3

    write_result1 = write_results[0]
    write_result2 = write_results[1]
    write_result3 = write_results[2]
    assert not write_result3._pb.HasField("update_time")

    snapshot1 = document1.get()
    assert snapshot1.to_dict() == data1
    assert snapshot1.create_time == write_result1.update_time
    assert snapshot1.update_time == write_result1.update_time

    snapshot2 = document2.get()
    assert snapshot2.to_dict() != data2
    data2["some"]["and"] = new_value
    assert snapshot2.to_dict() == data2
    assert_timestamp_less(snapshot2.create_time, write_result2.update_time)
    assert snapshot2.update_time == write_result2.update_time

    assert not document3.get().exists


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_live_bulk_writer(client, cleanup, database):
    from google.cloud.firestore_v1.bulk_writer import BulkWriter
    from google.cloud.firestore_v1.client import Client

    db: Client = client
    bw: BulkWriter = db.bulk_writer()
    col = db.collection(f"bulkitems{UNIQUE_RESOURCE_ID}")

    for index in range(50):
        doc_ref = col.document(f"id-{index}")
        bw.create(doc_ref, {"index": index})
        cleanup(doc_ref.delete)

    bw.close()
    assert bw._total_batches_sent >= 3  # retries could lead to more than 3 batches
    assert bw._total_write_operations >= 50  # same retries rule applies again
    assert bw._in_flight_documents == 0
    assert len(bw._operations) == 0

    # And now assert that the documents were in fact written to the database
    assert len(col.get()) == 50


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_watch_document(client, cleanup, database):
    db = client
    collection_ref = db.collection("wd-users" + UNIQUE_RESOURCE_ID)
    doc_ref = collection_ref.document("alovelace")

    # Initial setting
    doc_ref.set({"first": "Jane", "last": "Doe", "born": 1900})
    cleanup(doc_ref.delete)

    # Setup listener
    ada_future = concurrent.futures.Future()

    def on_snapshot(docs, changes, read_time):
        on_snapshot.called_count += 1
        if docs and docs[0].get("first") == "Ada" and not ada_future.done():
            ada_future.set_result(True)

    on_snapshot.called_count = 0

    doc_ref.on_snapshot(on_snapshot)

    # Alter document
    doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

    # Wait for the event-driven callback to resolve the future
    ada_future.result(timeout=60.0)

    if on_snapshot.called_count not in (1, 2):
        raise AssertionError(
            "Failed to get one or two document changes: count: "
            + str(on_snapshot.called_count)
        )


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_watch_collection(client, cleanup, database):
    db = client
    collection_ref = db.collection("wc-users" + UNIQUE_RESOURCE_ID)
    doc_ref = collection_ref.document("alovelace")

    # Initial setting
    doc_ref.set({"first": "Jane", "last": "Doe", "born": 1900})
    cleanup(doc_ref.delete)

    # Setup listener
    born_1815_future = concurrent.futures.Future()

    def on_snapshot(docs, changes, read_time):
        for doc in [doc for doc in docs if doc.id == doc_ref.id]:
            if doc.get("born") == 1815 and not born_1815_future.done():
                born_1815_future.set_result(True)

    collection_ref.on_snapshot(on_snapshot)

    doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

    born_1815_future.result(timeout=60.0)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_watch_query(client, cleanup, database):
    db = client
    collection_ref = db.collection("wq-users" + UNIQUE_RESOURCE_ID)
    doc_ref = collection_ref.document("alovelace")
    query_ref = collection_ref.where(filter=FieldFilter("first", "==", "Ada"))

    # Initial setting
    doc_ref.set({"first": "Jane", "last": "Doe", "born": 1900})
    cleanup(doc_ref.delete)

    # Setup listener
    one_doc_future = concurrent.futures.Future()

    def on_snapshot(docs, changes, read_time):
        on_snapshot.called_count += 1

        if docs:
            # A snapshot should return the same thing as if a query ran now.
            query_ran_query = collection_ref.where(
                filter=FieldFilter("first", "==", "Ada")
            )
            query_ran = query_ran_query.stream()
            assert len(docs) == len([i for i in query_ran])
            if not one_doc_future.done():
                one_doc_future.set_result(True)

    on_snapshot.called_count = 0

    query_ref.on_snapshot(on_snapshot)

    # Alter document
    doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

    one_doc_future.result(timeout=60.0)

    if on_snapshot.called_count not in (1, 2):
        raise AssertionError(
            "Failed to get expected document change count: "
            + str(on_snapshot.called_count)
        )


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_array_union(client, cleanup, database):
    doc_ref = client.document(f"gcp-7523-{UNIQUE_RESOURCE_ID}", "test-document")
    cleanup(doc_ref.delete)
    doc_ref.delete()
    tree_1 = {"forest": {"tree-1": "oak"}}
    tree_2 = {"forest": {"tree-2": "pine"}}
    tree_3 = {"forest": {"tree-3": firestore.ArrayUnion(["spruce"])}}

    doc_ref.set(tree_1)
    expected = tree_1.copy()
    assert doc_ref.get().to_dict() == expected

    doc_ref.set(tree_2, merge=True)
    expected["forest"]["tree-2"] = tree_2["forest"]["tree-2"]
    assert doc_ref.get().to_dict() == expected

    doc_ref.set(tree_3, merge=True)
    expected["forest"]["tree-3"] = ["spruce"]
    assert doc_ref.get().to_dict() == expected

    tree_3_part_2 = {"forest": {"tree-3": firestore.ArrayUnion(["palm"])}}
    expected["forest"]["tree-3"].append("palm")
    doc_ref.set(tree_3_part_2, merge=True)
    assert doc_ref.get().to_dict() == expected


def _persist_documents(
    client: firestore.Client,
    collection_name: str,
    documents: List[Dict],
    cleanup: Optional[Callable] = None,
):
    """Assuming `documents` is a recursive list of dictionaries representing
    documents and subcollections, this method writes all of those through
    `client.collection(...).document(...).create()`.

    `documents` must be of this structure:
    ```py
    documents = [
        {
            # Required key
            "data": <dictionary with "name" key>,

            # Optional key
            "subcollections": <same structure as `documents`>,
        },
        ...
    ]
    ```
    """
    for block in documents:
        col_ref = client.collection(collection_name)
        document_id: str = block["data"]["name"]
        doc_ref = col_ref.document(document_id)
        doc_ref.set(block["data"])
        if cleanup is not None:
            cleanup(doc_ref.delete)

        if "subcollections" in block:
            for subcollection_name, inner_blocks in block["subcollections"].items():
                _persist_documents(
                    client,
                    f"{collection_name}/{document_id}/{subcollection_name}",
                    inner_blocks,
                )


# documents compatible with `_persist_documents`
philosophers_data_set = [
    {
        "data": {"name": "Socrates", "favoriteCity": "Athens"},
        "subcollections": {
            "pets": [{"data": {"name": "Scruffy"}}, {"data": {"name": "Snowflake"}}],
            "hobbies": [
                {"data": {"name": "pontificating"}},
                {"data": {"name": "journaling"}},
            ],
            "philosophers": [
                {"data": {"name": "Aristotle"}},
                {"data": {"name": "Plato"}},
            ],
        },
    },
    {
        "data": {"name": "Aristotle", "favoriteCity": "Sparta"},
        "subcollections": {
            "pets": [{"data": {"name": "Floof-Boy"}}, {"data": {"name": "Doggy-Dog"}}],
            "hobbies": [
                {"data": {"name": "questioning-stuff"}},
                {"data": {"name": "meditation"}},
            ],
        },
    },
    {
        "data": {"name": "Plato", "favoriteCity": "Corinth"},
        "subcollections": {
            "pets": [
                {"data": {"name": "Cuddles"}},
                {"data": {"name": "Sergeant-Puppers"}},
            ],
            "hobbies": [
                {"data": {"name": "abstraction"}},
                {"data": {"name": "hypotheticals"}},
            ],
        },
    },
]


def _do_recursive_delete(client, bulk_writer, empty_philosophers=False):
    if empty_philosophers:
        doc_paths = philosophers = []
    else:
        philosophers = [philosophers_data_set[0]]

        doc_paths = [
            "",
            "/pets/Scruffy",
            "/pets/Snowflake",
            "/hobbies/pontificating",
            "/hobbies/journaling",
            "/philosophers/Aristotle",
            "/philosophers/Plato",
        ]

    _persist_documents(client, f"philosophers{UNIQUE_RESOURCE_ID}", philosophers)

    # Assert all documents were created so that when they're missing after the
    # delete, we're actually testing something.
    collection_ref = client.collection(f"philosophers{UNIQUE_RESOURCE_ID}")
    for path in doc_paths:
        snapshot = collection_ref.document(f"Socrates{path}").get()
        assert snapshot.exists, f"Snapshot at Socrates{path} should have been created"

    # Now delete.
    num_deleted = client.recursive_delete(collection_ref, bulk_writer=bulk_writer)
    assert num_deleted == len(doc_paths)

    # Now they should all be missing
    for path in doc_paths:
        snapshot = collection_ref.document(f"Socrates{path}").get()
        assert not snapshot.exists, (
            f"Snapshot at Socrates{path} should have been deleted"
        )


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_recursive_delete_parallelized(client, cleanup, database):
    from google.cloud.firestore_v1.bulk_writer import BulkWriterOptions, SendMode

    bw = client.bulk_writer(options=BulkWriterOptions(mode=SendMode.parallel))
    _do_recursive_delete(client, bw)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_recursive_delete_serialized(client, cleanup, database):
    from google.cloud.firestore_v1.bulk_writer import BulkWriterOptions, SendMode

    bw = client.bulk_writer(options=BulkWriterOptions(mode=SendMode.serial))
    _do_recursive_delete(client, bw)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_recursive_delete_parallelized_empty(client, cleanup, database):
    from google.cloud.firestore_v1.bulk_writer import BulkWriterOptions, SendMode

    bw = client.bulk_writer(options=BulkWriterOptions(mode=SendMode.parallel))
    _do_recursive_delete(client, bw, empty_philosophers=True)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_recursive_delete_serialized_empty(client, cleanup, database):
    from google.cloud.firestore_v1.bulk_writer import BulkWriterOptions, SendMode

    bw = client.bulk_writer(options=BulkWriterOptions(mode=SendMode.serial))
    _do_recursive_delete(client, bw, empty_philosophers=True)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_recursive_query(client, cleanup, database):
    col_id: str = f"philosophers-recursive-query{UNIQUE_RESOURCE_ID}"
    _persist_documents(client, col_id, philosophers_data_set, cleanup)

    query = client.collection_group(col_id).recursive()
    ids = [doc.id for doc in query.get()]

    expected_ids = [
        # Aristotle doc and subdocs
        "Aristotle",
        "meditation",
        "questioning-stuff",
        "Doggy-Dog",
        "Floof-Boy",
        # Plato doc and subdocs
        "Plato",
        "abstraction",
        "hypotheticals",
        "Cuddles",
        "Sergeant-Puppers",
        # Socrates doc and subdocs
        "Socrates",
        "journaling",
        "pontificating",
        "Scruffy",
        "Snowflake",
        "Aristotle",
        "Plato",
    ]

    assert len(ids) == len(expected_ids)

    for index in range(len(ids)):
        error_msg = (
            f"Expected '{expected_ids[index]}' at spot {index}, got '{{ids[index]}}'"
        )
        assert ids[index] == expected_ids[index], error_msg


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_nested_recursive_query(client, cleanup, database):
    col_id: str = f"philosophers-nested-recursive-query{UNIQUE_RESOURCE_ID}"
    _persist_documents(client, col_id, philosophers_data_set, cleanup)

    collection_ref = client.collection(col_id)
    aristotle = collection_ref.document("Aristotle")
    query = aristotle.collection("pets").recursive()
    ids = [doc.id for doc in query.get()]

    expected_ids = [
        # Aristotle pets
        "Doggy-Dog",
        "Floof-Boy",
    ]

    assert len(ids) == len(expected_ids)

    for index in range(len(ids)):
        error_msg = (
            f"Expected '{expected_ids[index]}' at spot {index}, got '{{ids[index]}}'"
        )
        assert ids[index] == expected_ids[index], error_msg


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_chunked_query(client, cleanup, database):
    col = client.collection(f"chunked-test{UNIQUE_RESOURCE_ID}")
    for index in range(10):
        doc_ref = col.document(f"document-{index + 1}")
        doc_ref.set({"index": index})
        cleanup(doc_ref.delete)

    iter = col._chunkify(3)
    assert len(next(iter)) == 3
    assert len(next(iter)) == 3
    assert len(next(iter)) == 3
    assert len(next(iter)) == 1


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_chunked_query_smaller_limit(client, cleanup, database):
    col = client.collection(f"chunked-test-smaller-limit{UNIQUE_RESOURCE_ID}")
    for index in range(10):
        doc_ref = col.document(f"document-{index + 1}")
        doc_ref.set({"index": index})
        cleanup(doc_ref.delete)

    iter = col.limit(5)._chunkify(9)
    assert len(next(iter)) == 5


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_chunked_and_recursive(client, cleanup, database):
    col_id = f"chunked-recursive-test{UNIQUE_RESOURCE_ID}"
    documents = [
        {
            "data": {"name": "Root-1"},
            "subcollections": {
                "children": [
                    {"data": {"name": f"Root-1--Child-{index + 1}"}}
                    for index in range(5)
                ]
            },
        },
        {
            "data": {"name": "Root-2"},
            "subcollections": {
                "children": [
                    {"data": {"name": f"Root-2--Child-{index + 1}"}}
                    for index in range(5)
                ]
            },
        },
    ]
    _persist_documents(client, col_id, documents, cleanup)
    collection_ref = client.collection(col_id)
    iter = collection_ref.recursive()._chunkify(5)

    page_1_ids = [
        "Root-1",
        "Root-1--Child-1",
        "Root-1--Child-2",
        "Root-1--Child-3",
        "Root-1--Child-4",
    ]
    assert [doc.id for doc in next(iter)] == page_1_ids

    page_2_ids = [
        "Root-1--Child-5",
        "Root-2",
        "Root-2--Child-1",
        "Root-2--Child-2",
        "Root-2--Child-3",
    ]
    assert [doc.id for doc in next(iter)] == page_2_ids

    page_3_ids = ["Root-2--Child-4", "Root-2--Child-5"]
    assert [doc.id for doc in next(iter)] == page_3_ids


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_watch_query_order(client, cleanup, database):
    db = client
    collection_ref = db.collection("users")
    doc_ref1 = collection_ref.document("alovelace" + UNIQUE_RESOURCE_ID)
    doc_ref2 = collection_ref.document("asecondlovelace" + UNIQUE_RESOURCE_ID)
    doc_ref3 = collection_ref.document("athirdlovelace" + UNIQUE_RESOURCE_ID)
    doc_ref4 = collection_ref.document("afourthlovelace" + UNIQUE_RESOURCE_ID)
    doc_ref5 = collection_ref.document("afifthlovelace" + UNIQUE_RESOURCE_ID)

    query_ref = collection_ref.where(filter=FieldFilter("first", "==", "Ada")).order_by(
        "last"
    )

    # Setup listener
    five_docs_future = concurrent.futures.Future()

    def on_snapshot(docs, changes, read_time):
        try:
            docs = [i for i in docs if i.id.endswith(UNIQUE_RESOURCE_ID)]
            if len(docs) != 5:
                return
            # A snapshot should return the same thing as if a query ran now.
            query_ran = query_ref.stream()
            query_ran_results = [
                i for i in query_ran if i.id.endswith(UNIQUE_RESOURCE_ID)
            ]
            assert len(docs) == len(query_ran_results)

            # compare the order things are returned
            for snapshot, query in zip(docs, query_ran_results):
                assert snapshot.get("last") == query.get("last"), (
                    "expect the sort order to match, last"
                )
                assert snapshot.get("born") == query.get("born"), (
                    "expect the sort order to match, born"
                )
            if not five_docs_future.done():
                five_docs_future.set_result(True)
        except Exception as e:
            if not five_docs_future.done():
                five_docs_future.set_exception(e)

    query_ref.on_snapshot(on_snapshot)

    doc_ref1.set({"first": "Ada", "last": "Lovelace", "born": 1815})
    cleanup(doc_ref1.delete)

    doc_ref2.set({"first": "Ada", "last": "SecondLovelace", "born": 1815})
    cleanup(doc_ref2.delete)

    doc_ref3.set({"first": "Ada", "last": "ThirdLovelace", "born": 1815})
    cleanup(doc_ref3.delete)

    doc_ref4.set({"first": "Ada", "last": "FourthLovelace", "born": 1815})
    cleanup(doc_ref4.delete)

    doc_ref5.set({"first": "Ada", "last": "lovelace", "born": 1815})
    cleanup(doc_ref5.delete)

    # Wait for the future to be resolved
    five_docs_future.result(timeout=60.0)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_repro_429(client, cleanup, database, verify_pipeline):
    # See: https://github.com/googleapis/python-firestore/issues/429
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    collection = client.collection("repro-429" + UNIQUE_RESOURCE_ID)

    for document_id in [f"doc-{doc_id:02d}" for doc_id in range(30)]:
        data = {"now": now, "paymentId": None}
        _, document = collection.add(data, document_id)
        cleanup(document.delete)

    query = (
        collection.where(filter=FieldFilter("paymentId", "==", None))
        .limit(10)
        .order_by("__name__")
    )

    last_snapshot = None
    for snapshot in query.stream():
        print(f"id: {snapshot.id}")
        last_snapshot = snapshot

    query2 = query.start_after(last_snapshot)

    for snapshot in query2.stream():
        print(f"id: {snapshot.id}")
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_repro_391(client, cleanup, database):
    # See: https://github.com/googleapis/python-firestore/issues/391
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    collection = client.collection("repro-391" + UNIQUE_RESOURCE_ID)

    document_ids = [f"doc-{doc_id:02d}" for doc_id in range(30)]

    for document_id in [f"doc-{doc_id:02d}" for doc_id in range(30)]:
        data = {"now": now}
        _, document = collection.add(data, document_id)

    assert len(set(collection.stream())) == len(document_ids)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_get_default_alias(query, database):
    count_query = query.count()
    result = count_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "field_1"


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_get_with_alias(query, database):
    count_query = query.count(alias="total")
    result = count_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_get_with_limit(query, database):
    # count without limit
    count_query = query.count(alias="total")
    result = count_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 5

    # count with limit
    count_query = query.limit(2).count(alias="total")

    result = count_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 2


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_get_multiple_aggregations(query, database):
    count_query = query.count(alias="total").count(alias="all")

    result = count_query.get()
    assert len(result[0]) == 2

    expected_aliases = ["total", "all"]
    found_alias = set(
        [r.alias for r in result[0]]
    )  # ensure unique elements in the result
    assert len(found_alias) == 2
    assert found_alias == set(expected_aliases)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_get_multiple_aggregations_duplicated_alias(query, database):
    count_query = query.count(alias="total").count(alias="total")

    with pytest.raises(InvalidArgument) as exc_info:
        count_query.get()

    assert "Aggregation aliases contain duplicate alias" in exc_info.value.message


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_get_empty_aggregation(query, database):
    from google.cloud.firestore_v1.aggregation import AggregationQuery

    aggregation_query = AggregationQuery(query)

    with pytest.raises(InvalidArgument) as exc_info:
        aggregation_query.get()

    assert "Aggregations can not be empty" in exc_info.value.message


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_stream_default_alias(query, database):
    count_query = query.count()
    for result in count_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "field_1"


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_stream_with_alias(query, database):
    count_query = query.count(alias="total")
    for result in count_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_stream_with_limit(query, database):
    # count without limit
    count_query = query.count(alias="total")
    for result in count_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 5

    # count with limit
    count_query = query.limit(2).count(alias="total")

    for result in count_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 2


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_stream_multiple_aggregations(query, database):
    count_query = query.count(alias="total").count(alias="all")

    for result in count_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias in ["total", "all"]


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_stream_multiple_aggregations_duplicated_alias(query, database):
    count_query = query.count(alias="total").count(alias="total")

    with pytest.raises(InvalidArgument) as exc_info:
        for _ in count_query.stream():
            pass

    assert "Aggregation aliases contain duplicate alias" in exc_info.value.message


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_stream_empty_aggregation(query, database):
    from google.cloud.firestore_v1.aggregation import AggregationQuery

    aggregation_query = AggregationQuery(query)

    with pytest.raises(InvalidArgument) as exc_info:
        for _ in aggregation_query.stream():
            pass

    assert "Aggregations can not be empty" in exc_info.value.message


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_count_query_with_start_at(query, database):
    """
    Ensure that count aggregation queries work when chained with a start_at

    eg `col.where(...).startAt(...).count()`
    """
    result = query.get()
    start_doc = result[1]
    # find count excluding first result
    expected_count = len(result) - 1
    # start new query that starts at the second result
    count_query = query.start_at(start_doc).count("a")
    # ensure that the first doc was skipped in sum aggregation
    for result in count_query.stream():
        for aggregation_result in result:
            assert aggregation_result.value == expected_count


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_get_default_alias(collection, database):
    sum_query = collection.sum("stats.product")
    result = sum_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "field_1"
        assert r.value == 100


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_get_with_alias(collection, database):
    sum_query = collection.sum("stats.product", alias="total")
    result = sum_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 100


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_get_with_limit(collection, database):
    # sum without limit
    sum_query = collection.sum("stats.product", alias="total")
    result = sum_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 100

    # sum with limit
    # limit query = [0,0,0,0,0,0,0,0,0,1,2,2]
    sum_query = collection.limit(12).sum("stats.product", alias="total")

    result = sum_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 5


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_get_multiple_aggregations(collection, database):
    sum_query = collection.sum("stats.product", alias="total").sum(
        "stats.product", alias="all"
    )

    result = sum_query.get()
    assert len(result[0]) == 2

    expected_aliases = ["total", "all"]
    found_alias = set(
        [r.alias for r in result[0]]
    )  # ensure unique elements in the result
    assert len(found_alias) == 2
    assert found_alias == set(expected_aliases)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_stream_default_alias(collection, database):
    sum_query = collection.sum("stats.product")
    for result in sum_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "field_1"
            assert aggregation_result.value == 100


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_stream_with_alias(collection, database):
    sum_query = collection.sum("stats.product", alias="total")
    for result in sum_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 100


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_stream_with_limit(collection, database):
    # sum without limit
    sum_query = collection.sum("stats.product", alias="total")
    for result in sum_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 100

    # sum with limit
    sum_query = collection.limit(12).sum("stats.product", alias="total")

    for result in sum_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 5


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_stream_multiple_aggregations(collection, database):
    sum_query = collection.sum("stats.product", alias="total").sum(
        "stats.product", alias="all"
    )

    for result in sum_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias in ["total", "all"]


# tests for issue reported in b/306241058
# we will skip test in client for now, until backend fix is implemented
@pytest.mark.skip(reason="backend fix required")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_sum_query_with_start_at(query, database):
    """
    Ensure that sum aggregation queries work when chained with a start_at

    eg `col.where(...).startAt(...).sum()`
    """
    result = query.get()
    start_doc = result[1]
    # find sum excluding first result
    expected_sum = sum([doc.get("a") for doc in result[1:]])
    # start new query that starts at the second result
    sum_result = query.start_at(start_doc).sum("a").get()
    assert len(sum_result) == 1
    # ensure that the first doc was skipped in sum aggregation
    assert sum_result[0].value == expected_sum


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_get_default_alias(collection, database):
    avg_query = collection.avg("stats.product")
    result = avg_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "field_1"
        assert r.value == 4.0
        assert isinstance(r.value, float)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_get_with_alias(collection, database):
    avg_query = collection.avg("stats.product", alias="total")
    result = avg_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 4


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_get_with_limit(collection, database):
    # avg without limit
    avg_query = collection.avg("stats.product", alias="total")
    result = avg_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 4.0

    # avg with limit
    # limit result = [0,0,0,0,0,0,0,0,0,1,2,2]
    avg_query = collection.limit(12).avg("stats.product", alias="total")

    result = avg_query.get()
    assert len(result) == 1
    for r in result[0]:
        assert r.alias == "total"
        assert r.value == 5 / 12
        assert isinstance(r.value, float)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_get_multiple_aggregations(collection, database):
    avg_query = collection.avg("stats.product", alias="total").avg(
        "stats.product", alias="all"
    )

    result = avg_query.get()
    assert len(result[0]) == 2

    expected_aliases = ["total", "all"]
    found_alias = set(
        [r.alias for r in result[0]]
    )  # ensure unique elements in the result
    assert len(found_alias) == 2
    assert found_alias == set(expected_aliases)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_stream_default_alias(collection, database):
    avg_query = collection.avg("stats.product")
    for result in avg_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "field_1"
            assert aggregation_result.value == 4


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_stream_with_alias(collection, database):
    avg_query = collection.avg("stats.product", alias="total")
    for result in avg_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 4


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_stream_with_limit(collection, database):
    # avg without limit
    avg_query = collection.avg("stats.product", alias="total")
    for result in avg_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 4

    # avg with limit
    avg_query = collection.limit(12).avg("stats.product", alias="total")

    for result in avg_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias == "total"
            assert aggregation_result.value == 5 / 12


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_stream_multiple_aggregations(collection, database):
    avg_query = collection.avg("stats.product", alias="total").avg(
        "stats.product", alias="all"
    )

    for result in avg_query.stream():
        for aggregation_result in result:
            assert aggregation_result.alias in ["total", "all"]


# tests for issue reported in b/306241058
# we will skip test in client for now, until backend fix is implemented
@pytest.mark.skip(reason="backend fix required")
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_avg_query_with_start_at(query, database):
    """
    Ensure that avg aggregation queries work when chained with a start_at

    eg `col.where(...).startAt(...).avg()`
    """
    from statistics import mean

    result = query.get()
    start_doc = result[1]
    # find average, excluding first result
    expected_avg = mean([doc.get("a") for doc in result[1:]])
    # start new query that starts at the second result
    avg_result = query.start_at(start_doc).avg("a").get()
    assert len(avg_result) == 1
    # ensure that the first doc was skipped in avg aggregation
    assert avg_result[0].value == expected_avg


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_aggregation_query_stream_or_get_w_no_explain_options(query, database, method):
    # Because all aggregation methods end up calling AggregationQuery.get() or
    # AggregationQuery.stream(), only use count() for testing here.
    from google.cloud.firestore_v1.query_profile import QueryExplainError

    result = query.get()
    start_doc = result[1]

    # start new query that starts at the second result
    count_query = query.start_at(start_doc).count("a")

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(count_query, method)
    results = method_under_test()

    # If no explain_option is passed, raise an exception if explain_metrics
    # is called
    with pytest.raises(QueryExplainError, match="explain_options not set on query"):
        results.get_explain_metrics()


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_aggregation_query_stream_or_get_w_explain_options_analyze_true(
    query, database, method
):
    # Because all aggregation methods end up calling AggregationQuery.get() or
    # AggregationQuery.stream(), only use count() for testing here.
    from google.cloud.firestore_v1.query_profile import (
        ExecutionStats,
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    result = query.get()
    start_doc = result[1]

    # start new query that starts at the second result
    count_query = query.start_at(start_doc).count("a")

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(count_query, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=True))

    # With `stream()`, an exception should be raised when accessing
    # explain_metrics before query finishes.
    if method == "stream":
        with pytest.raises(
            QueryExplainError,
            match="explain_metrics not available until query is complete",
        ):
            results.get_explain_metrics()

    # Finish iterating results, and explain_metrics should be available.
    num_results = len(list(results))

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert plan_summary.indexes_used[0]["properties"] == "(a ASC, __name__ ASC)"
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection"

    # Verify execution_stats.
    execution_stats = explain_metrics.execution_stats
    assert isinstance(execution_stats, ExecutionStats)
    assert execution_stats.results_returned == num_results
    assert execution_stats.read_operations == num_results
    duration = execution_stats.execution_duration.total_seconds()
    assert duration > 0
    assert duration < 1  # we expect a number closer to 0.05
    assert isinstance(execution_stats.debug_stats, dict)
    assert "billing_details" in execution_stats.debug_stats
    assert "documents_scanned" in execution_stats.debug_stats
    assert "index_entries_scanned" in execution_stats.debug_stats
    assert len(execution_stats.debug_stats) > 0


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("method", ["stream", "get"])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_aggregation_query_stream_or_get_w_explain_options_analyze_false(
    query, database, method
):
    # Because all aggregation methods end up calling AggregationQuery.get() or
    # AggregationQuery.stream(), only use count() for testing here.
    from google.cloud.firestore_v1.query_profile import (
        ExplainMetrics,
        ExplainOptions,
        PlanSummary,
        QueryExplainError,
    )

    result = query.get()
    start_doc = result[1]

    # start new query that starts at the second result
    count_query = query.start_at(start_doc).count("a")

    # Tests either `stream()` or `get()`.
    method_under_test = getattr(count_query, method)
    results = method_under_test(explain_options=ExplainOptions(analyze=False))

    # Verify explain_metrics and plan_summary.
    explain_metrics = results.get_explain_metrics()
    assert isinstance(explain_metrics, ExplainMetrics)
    plan_summary = explain_metrics.plan_summary
    assert isinstance(plan_summary, PlanSummary)
    assert len(plan_summary.indexes_used) > 0
    assert plan_summary.indexes_used[0]["properties"] == "(a ASC, __name__ ASC)"
    assert plan_summary.indexes_used[0]["query_scope"] == "Collection"

    # Verify execution_stats isn't available.
    with pytest.raises(
        QueryExplainError,
        match="execution_stats not available when explain_options.analyze=False",
    ):
        explain_metrics.execution_stats


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_with_and_composite_filter(collection, database, verify_pipeline):
    and_filter = And(
        filters=[
            FieldFilter("stats.product", ">", 5),
            FieldFilter("stats.product", "<", 10),
        ]
    )

    query = collection.where(filter=and_filter)
    for result in query.stream():
        assert result.get("stats.product") > 5
        assert result.get("stats.product") < 10
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_with_or_composite_filter(collection, database, verify_pipeline):
    or_filter = Or(
        filters=[
            FieldFilter("stats.product", ">", 5),
            FieldFilter("stats.product", "<", 10),
        ]
    )
    query = collection.where(filter=or_filter)
    gt_5 = 0
    lt_10 = 0
    for result in query.stream():
        value = result.get("stats.product")
        assert value > 5 or value < 10
        if value > 5:
            gt_5 += 1
        if value < 10:
            lt_10 += 1

    assert gt_5 > 0
    assert lt_10 > 0
    verify_pipeline(query)


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
@pytest.mark.parametrize(
    "aggregation_type,expected_value", [("count", 5), ("sum", 100), ("avg", 4.0)]
)
def test_aggregation_queries_with_read_time(
    collection,
    query,
    cleanup,
    database,
    aggregation_type,
    expected_value,
    verify_pipeline,
):
    """
    Ensure that all aggregation queries work when read_time is passed into
    a query.<aggregation_type>.().get() method
    """
    # Find the most recent read_time in collections
    read_time = max(docref.get().read_time for docref in collection.list_documents())
    document_data = {
        "a": 1,
        "b": 9000,
        "c": [1, 123123123],
        "stats": {"sum": 9001, "product": 9000},
    }

    _, doc_ref = collection.add(document_data)
    cleanup(doc_ref.delete)

    if aggregation_type == "count":
        aggregation_query = query.count()
    elif aggregation_type == "sum":
        aggregation_query = collection.sum("stats.product")
    elif aggregation_type == "avg":
        aggregation_query = collection.avg("stats.product")

    # Check that adding the new document data affected the results of the aggregation queries.
    new_result = aggregation_query.get()
    assert len(new_result) == 1
    for r in new_result[0]:
        assert r.value != expected_value

    old_result = aggregation_query.get(read_time=read_time)
    assert len(old_result) == 1
    for r in old_result[0]:
        assert r.value == expected_value
    verify_pipeline(aggregation_query)


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_query_with_complex_composite_filter(collection, database, verify_pipeline):
    field_filter = FieldFilter("b", "==", 0)
    or_filter = Or(
        filters=[FieldFilter("stats.sum", "==", 0), FieldFilter("stats.sum", "==", 4)]
    )
    # b == 0 && (stats.sum == 0 || stats.sum == 4)
    query = collection.where(filter=field_filter).where(filter=or_filter)

    sum_0 = 0
    sum_4 = 0
    for result in query.stream():
        assert result.get("b") == 0
        assert result.get("stats.sum") == 0 or result.get("stats.sum") == 4
        if result.get("stats.sum") == 0:
            sum_0 += 1
        if result.get("stats.sum") == 4:
            sum_4 += 1

    assert sum_0 > 0
    assert sum_4 > 0
    verify_pipeline(query)

    # b == 3 || (stats.sum == 4  && a == 4)
    comp_filter = Or(
        filters=[
            FieldFilter("b", "==", 3),
            And([FieldFilter("stats.sum", "==", 4), FieldFilter("a", "==", 4)]),
        ]
    )
    query = collection.where(filter=comp_filter)

    b_3 = False
    b_not_3 = False
    for result in query.stream():
        if result.get("b") == 3:
            b_3 = True
        else:
            b_not_3 = True
            assert result.get("stats.sum") == 4
            assert result.get("a") == 4

    assert b_3 is True
    assert b_not_3 is True
    verify_pipeline(query)


@pytest.mark.parametrize(
    "aggregation_type,aggregation_args,expected",
    [("count", (), 3), ("sum", ("b"), 12), ("avg", ("b"), 4)],
)
@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_aggregation_query_in_transaction(
    client,
    cleanup,
    database,
    aggregation_type,
    aggregation_args,
    expected,
    verify_pipeline,
):
    """
    Test creating an aggregation query inside a transaction
    Should send transaction id along with request. Results should be consistent with non-transactional query
    """
    collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    doc_ids = [f"doc{i}" + UNIQUE_RESOURCE_ID for i in range(4)]
    doc_refs = [client.document(collection_id, doc_id) for doc_id in doc_ids]
    for doc_ref in doc_refs:
        cleanup(doc_ref.delete)
    doc_refs[0].create({"a": 3, "b": 1})
    doc_refs[1].create({"a": 5, "b": 1})
    doc_refs[2].create({"a": 5, "b": 10})
    doc_refs[3].create({"a": 10, "b": 0})  # should be ignored by query

    collection = client.collection(collection_id)
    query = collection.where(filter=FieldFilter("b", ">", 0))
    aggregation_query = getattr(query, aggregation_type)(*aggregation_args)

    with client.transaction() as transaction:
        # should fail if transaction has not been initiated
        with pytest.raises(ValueError):
            aggregation_query.get(transaction=transaction)

        # should work when transaction is initiated through transactional decorator
        @firestore.transactional
        def in_transaction(transaction):
            global inner_fn_ran
            result = aggregation_query.get(transaction=transaction)
            assert len(result) == 1
            assert len(result[0]) == 1
            assert result[0][0].value == expected
            inner_fn_ran = True
            verify_pipeline(aggregation_query)

        in_transaction(transaction)
        # make sure we didn't skip assertions in inner function
        assert inner_fn_ran is True


@pytest.mark.parametrize("database", TEST_DATABASES_W_ENTERPRISE, indirect=True)
def test_or_query_in_transaction(client, cleanup, database, verify_pipeline):
    """
    Test running or query inside a transaction. Should pass transaction id along with request
    """
    collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    doc_ids = [f"doc{i}" + UNIQUE_RESOURCE_ID for i in range(5)]
    doc_refs = [client.document(collection_id, doc_id) for doc_id in doc_ids]
    for doc_ref in doc_refs:
        cleanup(doc_ref.delete)
    doc_refs[0].create({"a": 1, "b": 2})
    doc_refs[1].create({"a": 1, "b": 1})
    doc_refs[2].create({"a": 2, "b": 1})  # should be ignored by query
    doc_refs[3].create({"a": 1, "b": 0})  # should be ignored by query

    collection = client.collection(collection_id)
    query = collection.where(filter=FieldFilter("a", "==", 1)).where(
        filter=Or([FieldFilter("b", "==", 1), FieldFilter("b", "==", 2)])
    )

    with client.transaction() as transaction:
        # should fail if transaction has not been initiated
        with pytest.raises(ValueError):
            query.get(transaction=transaction)

        # should work when transaction is initiated through transactional decorator
        @firestore.transactional
        def in_transaction(transaction):
            global inner_fn_ran
            result = query.get(transaction=transaction)
            assert len(result) == 2
            # both documents should have a == 1
            assert result[0].get("a") == 1
            assert result[1].get("a") == 1
            # one document should have b == 1 and the other should have b == 2
            assert (result[0].get("b") == 1 and result[1].get("b") == 2) or (
                result[0].get("b") == 2 and result[1].get("b") == 1
            )
            inner_fn_ran = True
            verify_pipeline(query)

        in_transaction(transaction)
        # make sure we didn't skip assertions in inner function
        assert inner_fn_ran is True


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_transaction_w_uuid(client, cleanup, database):
    """
    https://github.com/googleapis/python-firestore/issues/1012
    """
    collection_id = "uuid_collection" + UNIQUE_RESOURCE_ID
    doc_ref = client.document(collection_id, "doc")
    cleanup(doc_ref.delete)
    key = "b7992822-eacb-40be-8af6-559b9e2fb0b7"
    doc_ref.create({key: "I'm a UUID!"})

    @firestore.transactional
    def update_doc(tx, doc_ref, key, value):
        tx.update(doc_ref, {key: value})

    expected = "UPDATED VALUE"
    update_doc(client.transaction(), doc_ref, key, expected)
    # read updated doc
    snapshot = doc_ref.get()
    assert snapshot.to_dict()[key] == expected


@pytest.mark.skipif(
    FIRESTORE_EMULATOR, reason="Query profile not supported in emulator."
)
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_in_transaction_with_explain_options(client, cleanup, database):
    """
    Test query profiling in transactions.
    """
    from google.cloud.firestore_v1.query_profile import (
        ExplainMetrics,
        ExplainOptions,
        QueryExplainError,
    )

    collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    doc_ids = [f"doc{i}" + UNIQUE_RESOURCE_ID for i in range(5)]
    doc_refs = [client.document(collection_id, doc_id) for doc_id in doc_ids]
    for doc_ref in doc_refs:
        cleanup(doc_ref.delete)
    doc_refs[0].create({"a": 1, "b": 2})
    doc_refs[1].create({"a": 1, "b": 1})

    collection = client.collection(collection_id)
    query = collection.where(filter=FieldFilter("a", "==", 1))

    with client.transaction() as transaction:
        # should work when transaction is initiated through transactional decorator
        @firestore.transactional
        def in_transaction(transaction):
            global inner_fn_ran

            # When no explain_options value is passed,  an exception shoud be
            # raised when accessing explain_metrics.
            result_1 = query.get(transaction=transaction)
            with pytest.raises(
                QueryExplainError, match="explain_options not set on query."
            ):
                result_1.get_explain_metrics()

            result_2 = query.get(
                transaction=transaction,
                explain_options=ExplainOptions(analyze=True),
            )
            explain_metrics = result_2.get_explain_metrics()
            assert isinstance(explain_metrics, ExplainMetrics)
            assert explain_metrics.plan_summary is not None
            assert explain_metrics.execution_stats is not None

            inner_fn_ran = True

        in_transaction(transaction)
        # make sure we didn't skip assertions in inner function
        assert inner_fn_ran is True


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_query_in_transaction_with_read_time(client, cleanup, database):
    """
    Test query profiling in transactions.
    """
    collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    doc_ids = [f"doc{i}" + UNIQUE_RESOURCE_ID for i in range(5)]
    doc_refs = [client.document(collection_id, doc_id) for doc_id in doc_ids]
    for doc_ref in doc_refs:
        cleanup(doc_ref.delete)
    doc_refs[0].create({"a": 1, "b": 2})
    doc_refs[1].create({"a": 1, "b": 1})

    read_time = max(docref.get().read_time for docref in doc_refs)
    doc_refs[2].create({"a": 1, "b": 3})

    collection = client.collection(collection_id)
    query = collection.where(filter=FieldFilter("a", "==", 1))

    with client.transaction() as transaction:
        # should work when transaction is initiated through transactional decorator
        @firestore.transactional
        def in_transaction(transaction):
            global inner_fn_ran

            new_b_values = [
                docs.get("b") for docs in transaction.get(query, read_time=read_time)
            ]
            assert len(new_b_values) == 2
            assert 1 in new_b_values
            assert 2 in new_b_values
            assert 3 not in new_b_values

            new_b_values = [docs.get("b") for docs in transaction.get(query)]
            assert len(new_b_values) == 3
            assert 1 in new_b_values
            assert 2 in new_b_values
            assert 3 in new_b_values

            inner_fn_ran = True

        in_transaction(transaction)
        # make sure we didn't skip assertions in inner function
        assert inner_fn_ran is True


@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_update_w_uuid(client, cleanup, database):
    """
    https://github.com/googleapis/python-firestore/issues/1012
    """
    collection_id = "uuid_collection" + UNIQUE_RESOURCE_ID
    doc_ref = client.document(collection_id, "doc")
    cleanup(doc_ref.delete)
    key = "b7992822-eacb-40be-8af6-559b9e2fb0b7"
    doc_ref.create({key: "I'm a UUID!"})

    expected = "UPDATED VALUE"
    doc_ref.update({key: expected})
    # read updated doc
    snapshot = doc_ref.get()
    assert snapshot.to_dict()[key] == expected


@pytest.mark.parametrize("with_rollback,expected", [(True, 2), (False, 3)])
@pytest.mark.parametrize("database", TEST_DATABASES, indirect=True)
def test_transaction_rollback(client, cleanup, database, with_rollback, expected):
    """
    Create a document in a transaction that is rolled back
    Document should not show up in later queries
    """
    collection_id = "doc-create" + UNIQUE_RESOURCE_ID
    doc_ids = [f"doc{i}" + UNIQUE_RESOURCE_ID for i in range(3)]
    doc_refs = [client.document(collection_id, doc_id) for doc_id in doc_ids]
    for doc_ref in doc_refs:
        cleanup(doc_ref.delete)
    doc_refs[0].create({"a": 1})
    doc_refs[1].create({"a": 1})
    doc_refs[2].create({"a": 2})  # should be ignored by query

    transaction = client.transaction()

    @firestore.transactional
    def in_transaction(transaction, rollback):
        """
        create a document in a transaction that is rolled back (raises an exception)
        """
        new_document_id = "in_transaction_doc" + UNIQUE_RESOURCE_ID
        new_document_ref = client.document(collection_id, new_document_id)
        cleanup(new_document_ref.delete)
        transaction.create(new_document_ref, {"a": 1})
        if rollback:
            raise RuntimeError("rollback")

    if with_rollback:
        # run transaction in function that results in a rollback
        with pytest.raises(RuntimeError) as exc:
            in_transaction(transaction, with_rollback)
        assert str(exc.value) == "rollback"
    else:
        # no rollback expected
        in_transaction(transaction, with_rollback)

    collection = client.collection(collection_id)

    query = collection.where(filter=FieldFilter("a", "==", 1)).count()
    result = query.get()
    assert len(result) == 1
    assert len(result[0]) == 1
    assert result[0][0].value == expected


@pytest.mark.skip(reason="Temporarily skipped. Not yet in production.")
@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_large_document_standard_writes(client, cleanup, database):
    """Test standard write and read operations for 5MB document on Enterprise DB."""
    collection_id = "large_docs_" + UNIQUE_RESOURCE_ID
    doc_ref = client.collection(collection_id).document("large_doc")
    cleanup(doc_ref.delete)

    large_payload = "a" * (5 * 1024 * 1024)
    doc_ref.set({"payload": large_payload})

    snapshot = doc_ref.get()
    assert snapshot.exists
    assert snapshot.to_dict() == {"payload": large_payload}


@pytest.mark.skip(reason="Temporarily skipped. Not yet in production.")
@pytest.mark.parametrize("method", ["execute", "stream"])
@pytest.mark.parametrize("database", [FIRESTORE_ENTERPRISE_DB], indirect=True)
def test_large_document_pipeline(client, cleanup, database, method):
    """Test pipeline execution over 5MB document on Enterprise DB."""
    collection_id = "large_pipeline_" + UNIQUE_RESOURCE_ID
    col_ref = client.collection(collection_id)
    doc_ref = col_ref.document("large_doc")
    cleanup(doc_ref.delete)

    large_payload = "b" * (5 * 1024 * 1024)
    doc_ref.set({"payload": large_payload})

    pipeline = client.pipeline().collection(collection_id)
    method_under_test = getattr(pipeline, method)

    results = list(method_under_test())
    assert [doc.data() for doc in results] == [{"payload": large_payload}]
