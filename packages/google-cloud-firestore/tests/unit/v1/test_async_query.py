# Copyright 2020 Google LLC All rights reserved.
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

import datetime
import types

import mock
import pytest

from google.cloud.firestore_v1.query_profile import ExplainMetrics, QueryExplainError
from google.cloud.firestore_v1.query_results import QueryResultsList
from tests.unit.v1._test_helpers import (
    DEFAULT_TEST_PROJECT,
    make_async_client,
    make_async_query,
)
from tests.unit.v1.test__helpers import AsyncIter, AsyncMock
from tests.unit.v1.test_base_query import _make_cursor_pb, _make_query_response


def test_asyncquery_constructor():
    query = make_async_query(mock.sentinel.parent)
    assert query._parent is mock.sentinel.parent
    assert query._projection is None
    assert query._field_filters == ()
    assert query._orders == ()
    assert query._limit is None
    assert query._offset is None
    assert query._start_at is None
    assert query._end_at is None
    assert not query._all_descendants


async def _get_helper(retry=None, timeout=None, explain_options=None, read_time=None):
    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")

    # Add a dummy response to the minimal fake GAPIC.
    _, expected_prefix = parent._parent_info()
    name = "{}/sleep".format(expected_prefix)
    data = {"snooze": 10}
    explain_metrics = {"execution_stats": {"results_returned": 1}}

    response_pb = _make_query_response(
        name=name, data=data, explain_metrics=explain_metrics
    )
    firestore_api.run_query.return_value = AsyncIter([response_pb])
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Execute the query and check the response.
    query = make_async_query(parent)
    returned = await query.get(
        **kwargs, explain_options=explain_options, read_time=read_time
    )

    assert isinstance(returned, QueryResultsList)
    assert len(returned) == 1

    snapshot = returned[0]
    assert snapshot.reference._path == ("dee", "sleep")
    assert snapshot.to_dict() == data

    if explain_options is None:
        with pytest.raises(QueryExplainError, match="explain_options not set"):
            returned.get_explain_metrics()
    else:
        actual_explain_metrics = returned.get_explain_metrics()
        assert isinstance(actual_explain_metrics, ExplainMetrics)
        assert actual_explain_metrics.execution_stats.results_returned == 1

    # Create expected request body.
    parent_path, _ = parent._parent_info()
    request = {
        "parent": parent_path,
        "structured_query": query._to_protobuf(),
        "transaction": None,
    }
    if explain_options:
        request["explain_options"] = explain_options._to_dict()
    if read_time:
        request["read_time"] = read_time

    # Verify the mock call.
    firestore_api.run_query.assert_called_once_with(
        request=request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.asyncio
async def test_asyncquery_get():
    await _get_helper()


@pytest.mark.asyncio
async def test_asyncquery_get_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    await _get_helper(retry=retry, timeout=timeout)


@pytest.mark.asyncio
async def test_asyncquery_get_w_read_time():
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)
    await _get_helper(read_time=read_time)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "direction, expected_direction",
    [("DESCENDING", "ASCENDING"), ("ASCENDING", "DESCENDING")],
)
async def test_asyncquery_get_limit_to_last(direction, expected_direction):
    from google.cloud.firestore_v1.base_query import _enum_from_direction

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")

    # Add a dummy response to the minimal fake GAPIC.
    _, expected_prefix = parent._parent_info()
    name = "{}/sleep".format(expected_prefix)
    data = {"snooze": 10}
    data2 = {"snooze": 20}

    response_pb = _make_query_response(name=name, data=data)
    response_pb2 = _make_query_response(name=name, data=data2)

    firestore_api.run_query.return_value = AsyncIter([response_pb2, response_pb])

    # Execute the query and check the response.
    query = make_async_query(parent)
    query = query.order_by("snooze", direction=direction).limit_to_last(2)
    returned = await query.get()

    assert isinstance(returned, list)
    assert query._orders[0].direction == _enum_from_direction(expected_direction)
    assert len(returned) == 2

    snapshot = returned[0]
    assert snapshot.reference._path == ("dee", "sleep")
    assert snapshot.to_dict() == data

    snapshot2 = returned[1]
    assert snapshot2.reference._path == ("dee", "sleep")
    assert snapshot2.to_dict() == data2

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_get_w_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    await _get_helper(explain_options=explain_options)


def test_asyncquery_sum():
    from google.cloud.firestore_v1.base_aggregation import SumAggregation
    from google.cloud.firestore_v1.field_path import FieldPath

    client = make_async_client()
    parent = client.collection("dee")
    field_str = "field_str"
    field_path = FieldPath("foo", "bar")
    query = make_async_query(parent)
    # test with only field populated
    sum_query = query.sum(field_str)
    sum_agg = sum_query._aggregations[0]
    assert isinstance(sum_agg, SumAggregation)
    assert sum_agg.field_ref == field_str
    assert sum_agg.alias is None
    # test with field and alias populated
    sum_query = query.sum(field_str, alias="alias")
    sum_agg = sum_query._aggregations[0]
    assert isinstance(sum_agg, SumAggregation)
    assert sum_agg.field_ref == field_str
    assert sum_agg.alias == "alias"
    # test with field_path
    sum_query = query.sum(field_path, alias="alias")
    sum_agg = sum_query._aggregations[0]
    assert isinstance(sum_agg, SumAggregation)
    assert sum_agg.field_ref == "foo.bar"
    assert sum_agg.alias == "alias"


def test_asyncquery_avg():
    from google.cloud.firestore_v1.base_aggregation import AvgAggregation
    from google.cloud.firestore_v1.field_path import FieldPath

    client = make_async_client()
    parent = client.collection("dee")
    field_str = "field_str"
    field_path = FieldPath("foo", "bar")
    query = make_async_query(parent)
    # test with only field populated
    avg_query = query.avg(field_str)
    avg_agg = avg_query._aggregations[0]
    assert isinstance(avg_agg, AvgAggregation)
    assert avg_agg.field_ref == field_str
    assert avg_agg.alias is None
    # test with field and alias populated
    avg_query = query.avg(field_str, alias="alias")
    avg_agg = avg_query._aggregations[0]
    assert isinstance(avg_agg, AvgAggregation)
    assert avg_agg.field_ref == field_str
    assert avg_agg.alias == "alias"
    # test with field_path
    avg_query = query.avg(field_path, alias="alias")
    avg_agg = avg_query._aggregations[0]
    assert isinstance(avg_agg, AvgAggregation)
    assert avg_agg.field_ref == "foo.bar"
    assert avg_agg.alias == "alias"


@pytest.mark.asyncio
async def test_asyncquery_chunkify_w_empty():
    client = make_async_client()
    firestore_api = AsyncMock(spec=["run_query"])
    firestore_api.run_query.return_value = AsyncIter([])
    client._firestore_api_internal = firestore_api
    query = client.collection("asdf")._query()

    chunks = []
    async for chunk in query._chunkify(10):
        chunks.append(chunk)

    assert chunks == [[]]


@pytest.mark.asyncio
async def test_asyncquery_chunkify_w_chunksize_lt_limit():
    from google.cloud.firestore_v1.types import document, firestore

    client = make_async_client()
    firestore_api = AsyncMock(spec=["run_query"])
    doc_ids = [
        f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/asdf/{index}"
        for index in range(5)
    ]
    responses1 = [
        firestore.RunQueryResponse(
            document=document.Document(name=doc_id),
        )
        for doc_id in doc_ids[:2]
    ]
    responses2 = [
        firestore.RunQueryResponse(
            document=document.Document(name=doc_id),
        )
        for doc_id in doc_ids[2:4]
    ]
    responses3 = [
        firestore.RunQueryResponse(
            document=document.Document(name=doc_id),
        )
        for doc_id in doc_ids[4:]
    ]
    firestore_api.run_query.side_effect = [
        AsyncIter(responses1),
        AsyncIter(responses2),
        AsyncIter(responses3),
    ]
    client._firestore_api_internal = firestore_api
    query = client.collection("asdf")._query()

    chunks = []
    async for chunk in query._chunkify(2):
        chunks.append(chunk)

    assert len(chunks) == 3
    expected_ids = [str(index) for index in range(5)]
    assert [snapshot.id for snapshot in chunks[0]] == expected_ids[:2]
    assert [snapshot.id for snapshot in chunks[1]] == expected_ids[2:4]
    assert [snapshot.id for snapshot in chunks[2]] == expected_ids[4:]


@pytest.mark.asyncio
async def test_asyncquery_chunkify_w_chunksize_gt_limit():
    from google.cloud.firestore_v1.types import document, firestore

    client = make_async_client()

    firestore_api = AsyncMock(spec=["run_query"])
    responses = [
        firestore.RunQueryResponse(
            document=document.Document(
                name=(
                    f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/"
                    f"documents/asdf/{index}"
                ),
            ),
        )
        for index in range(5)
    ]
    firestore_api.run_query.return_value = AsyncIter(responses)
    client._firestore_api_internal = firestore_api

    query = client.collection("asdf")._query()

    chunks = []
    async for chunk in query.limit(5)._chunkify(10):
        chunks.append(chunk)

    assert len(chunks) == 1
    expected_ids = [str(index) for index in range(5)]
    assert [snapshot.id for snapshot in chunks[0]] == expected_ids


async def _stream_helper(
    retry=None, timeout=None, explain_options=None, read_time=None
):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")

    # Add a dummy response to the minimal fake GAPIC.
    _, expected_prefix = parent._parent_info()
    name = "{}/sleep".format(expected_prefix)
    data = {"snooze": 10}
    if explain_options is not None:
        explain_metrics = {"execution_stats": {"results_returned": 1}}
    else:
        explain_metrics = None
    response_pb = _make_query_response(
        name=name, data=data, explain_metrics=explain_metrics
    )
    firestore_api.run_query.return_value = AsyncIter([response_pb])
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Execute the query and check the response.
    query = make_async_query(parent)

    stream_response = query.stream(
        **kwargs, explain_options=explain_options, read_time=read_time
    )
    assert isinstance(stream_response, AsyncStreamGenerator)

    returned = [x async for x in stream_response]
    await stream_response.aclose()
    assert len(returned) == 1
    snapshot = returned[0]
    assert snapshot.reference._path == ("dee", "sleep")
    assert snapshot.to_dict() == data

    # Verify explain_metrics.
    if explain_options is None:
        with pytest.raises(QueryExplainError, match="explain_options not set"):
            await stream_response.get_explain_metrics()
    else:
        explain_metrics = await stream_response.get_explain_metrics()
        assert isinstance(explain_metrics, ExplainMetrics)
        assert explain_metrics.execution_stats.results_returned == 1

    # Create expected request body.
    parent_path, _ = parent._parent_info()
    request = {
        "parent": parent_path,
        "structured_query": query._to_protobuf(),
        "transaction": None,
    }
    if explain_options is not None:
        request["explain_options"] = explain_options._to_dict()
    if read_time is not None:
        request["read_time"] = read_time

    # Verify the mock call.
    firestore_api.run_query.assert_called_once_with(
        request=request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_simple():
    await _stream_helper()


@pytest.mark.asyncio
async def test_asyncquery_stream_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    await _stream_helper(retry=retry, timeout=timeout)


@pytest.mark.asyncio
async def test_asyncquery_stream_w_read_time():
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)
    await _stream_helper(read_time=read_time)


@pytest.mark.asyncio
async def test_asyncquery_stream_with_limit_to_last():
    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    # Execute the query and check the response.
    query = make_async_query(parent)
    query = query.limit_to_last(2)

    stream_response = query.stream()

    with pytest.raises(ValueError):
        [d async for d in stream_response]


@pytest.mark.asyncio
async def test_asyncquery_stream_with_transaction():
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Create a real-ish transaction for this client.
    transaction = client.transaction()
    txn_id = b"\x00\x00\x01-work-\xf2"
    transaction._id = txn_id

    # Make a **real** collection reference as parent.
    parent = client.collection("declaration")

    # Add a dummy response to the minimal fake GAPIC.
    parent_path, expected_prefix = parent._parent_info()
    name = "{}/burger".format(expected_prefix)
    data = {"lettuce": b"\xee\x87"}
    response_pb = _make_query_response(name=name, data=data)
    firestore_api.run_query.return_value = AsyncIter([response_pb])

    # Execute the query and check the response.
    query = make_async_query(parent)
    get_response = query.stream(transaction=transaction)
    assert isinstance(get_response, AsyncStreamGenerator)
    returned = [x async for x in get_response]
    assert len(returned) == 1
    snapshot = returned[0]
    assert snapshot.reference._path == ("declaration", "burger")
    assert snapshot.to_dict() == data

    # Verify the mock call.
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": txn_id,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_with_transaction_and_read_time():
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Create a real-ish transaction for this client.
    transaction = client.transaction()
    txn_id = b"\x00\x00\x01-work-\xf2"
    transaction._id = txn_id

    # Create a read_time for this client.
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)

    # Make a **real** collection reference as parent.
    parent = client.collection("declaration")

    # Add a dummy response to the minimal fake GAPIC.
    parent_path, expected_prefix = parent._parent_info()
    name = "{}/burger".format(expected_prefix)
    data = {"lettuce": b"\xee\x87"}
    response_pb = _make_query_response(name=name, data=data)
    firestore_api.run_query.return_value = AsyncIter([response_pb])

    # Execute the query and check the response.
    query = make_async_query(parent)
    get_response = query.stream(transaction=transaction, read_time=read_time)
    assert isinstance(get_response, AsyncStreamGenerator)
    returned = [x async for x in get_response]
    assert len(returned) == 1
    snapshot = returned[0]
    assert snapshot.reference._path == ("declaration", "burger")
    assert snapshot.to_dict() == data

    # Verify the mock call.
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": txn_id,
            "read_time": read_time,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_no_results():
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = AsyncMock(spec=["run_query"])
    empty_response = _make_query_response()
    run_query_response = AsyncIter([empty_response])
    firestore_api.run_query.return_value = run_query_response

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dah", "dah", "dum")
    query = make_async_query(parent)

    get_response = query.stream()
    assert isinstance(get_response, AsyncStreamGenerator)
    assert [x async for x in get_response] == []

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_second_response_in_empty_stream():
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = AsyncMock(spec=["run_query"])
    empty_response1 = _make_query_response()
    empty_response2 = _make_query_response()
    run_query_response = AsyncIter([empty_response1, empty_response2])
    firestore_api.run_query.return_value = run_query_response

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dah", "dah", "dum")
    query = make_async_query(parent)

    get_response = query.stream()
    assert isinstance(get_response, AsyncStreamGenerator)
    assert [x async for x in get_response] == []

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_with_skipped_results():
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("talk", "and", "chew-gum")

    # Add two dummy responses to the minimal fake GAPIC.
    _, expected_prefix = parent._parent_info()
    response_pb1 = _make_query_response(skipped_results=1)
    name = "{}/clock".format(expected_prefix)
    data = {"noon": 12, "nested": {"bird": 10.5}}
    response_pb2 = _make_query_response(name=name, data=data)
    firestore_api.run_query.return_value = AsyncIter([response_pb1, response_pb2])

    # Execute the query and check the response.
    query = make_async_query(parent)
    get_response = query.stream()
    assert isinstance(get_response, AsyncStreamGenerator)
    returned = [x async for x in get_response]
    assert len(returned) == 1
    snapshot = returned[0]
    assert snapshot.reference._path == ("talk", "and", "chew-gum", "clock")
    assert snapshot.to_dict() == data

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_empty_after_first_response():
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("charles")

    # Add two dummy responses to the minimal fake GAPIC.
    _, expected_prefix = parent._parent_info()
    name = "{}/bark".format(expected_prefix)
    data = {"lee": "hoop"}
    response_pb1 = _make_query_response(name=name, data=data)
    response_pb2 = _make_query_response()
    firestore_api.run_query.return_value = AsyncIter([response_pb1, response_pb2])

    # Execute the query and check the response.
    query = make_async_query(parent)
    get_response = query.stream()
    assert isinstance(get_response, AsyncStreamGenerator)
    returned = [x async for x in get_response]
    assert len(returned) == 1
    snapshot = returned[0]
    assert snapshot.reference._path == ("charles", "bark")
    assert snapshot.to_dict() == data

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_w_collection_group():
    from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("charles")
    other = client.collection("dora")

    # Add two dummy responses to the minimal fake GAPIC.
    _, other_prefix = other._parent_info()
    name = "{}/bark".format(other_prefix)
    data = {"lee": "hoop"}
    response_pb1 = _make_query_response(name=name, data=data)
    response_pb2 = _make_query_response()
    firestore_api.run_query.return_value = AsyncIter([response_pb1, response_pb2])

    # Execute the query and check the response.
    query = make_async_query(parent)
    query._all_descendants = True
    get_response = query.stream()
    assert isinstance(get_response, AsyncStreamGenerator)
    returned = [x async for x in get_response]
    assert len(returned) == 1
    snapshot = returned[0]
    to_match = other.document("bark")
    assert snapshot.reference._document_path == to_match._document_path
    assert snapshot.to_dict() == data

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": query._to_protobuf(),
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.asyncio
async def test_asyncquery_stream_w_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    await _stream_helper(explain_options=explain_options)


def _make_async_collection_group(*args, **kwargs):
    from google.cloud.firestore_v1.async_query import AsyncCollectionGroup

    return AsyncCollectionGroup(*args, **kwargs)


def test_asynccollectiongroup_constructor():
    query = _make_async_collection_group(mock.sentinel.parent)
    assert query._parent is mock.sentinel.parent
    assert query._projection is None
    assert query._field_filters == ()
    assert query._orders == ()
    assert query._limit is None
    assert query._offset is None
    assert query._start_at is None
    assert query._end_at is None
    assert query._all_descendants


def test_asynccollectiongroup_constructor_all_descendents_is_false():
    with pytest.raises(ValueError):
        _make_async_collection_group(mock.sentinel.parent, all_descendants=False)


@pytest.mark.asyncio
async def _get_partitions_helper(retry=None, timeout=None, read_time=None):
    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["partition_query"])

    # Attach the fake GAPIC to a real client.
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("charles")

    # Make two **real** document references to use as cursors
    document1 = parent.document("one")
    document2 = parent.document("two")

    # Add cursor pb's to the minimal fake GAPIC.
    cursor_pb1 = _make_cursor_pb(([document1], False))
    cursor_pb2 = _make_cursor_pb(([document2], False))
    firestore_api.partition_query.return_value = AsyncIter([cursor_pb1, cursor_pb2])
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Execute the query and check the response.
    query = _make_async_collection_group(parent)
    get_response = query.get_partitions(2, read_time=read_time, **kwargs)

    assert isinstance(get_response, types.AsyncGeneratorType)
    returned = [i async for i in get_response]
    assert len(returned) == 3

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    partition_query = _make_async_collection_group(
        parent,
        orders=(query._make_order("__name__", query.ASCENDING),),
    )
    expected_request = {
        "parent": parent_path,
        "structured_query": partition_query._to_protobuf(),
        "partition_count": 2,
    }
    if read_time is not None:
        expected_request["read_time"] = read_time
    firestore_api.partition_query.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.asyncio
async def test_asynccollectiongroup_get_partitions():
    await _get_partitions_helper()


@pytest.mark.asyncio
async def test_asynccollectiongroup_get_partitions_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    await _get_partitions_helper(retry=retry, timeout=timeout)


@pytest.mark.asyncio
async def test_asynccollectiongroup_get_partitions_w_read_time():
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)
    await _get_partitions_helper(read_time=read_time)


@pytest.mark.asyncio
async def test_asynccollectiongroup_get_partitions_w_filter():
    # Make a **real** collection reference as parent.
    client = make_async_client()
    parent = client.collection("charles")

    # Make a query that fails to partition
    query = _make_async_collection_group(parent).where("foo", "==", "bar")
    with pytest.raises(ValueError):
        [i async for i in query.get_partitions(2)]


@pytest.mark.asyncio
async def test_asynccollectiongroup_get_partitions_w_projection():
    # Make a **real** collection reference as parent.
    client = make_async_client()
    parent = client.collection("charles")

    # Make a query that fails to partition
    query = _make_async_collection_group(parent).select("foo")
    with pytest.raises(ValueError):
        [i async for i in query.get_partitions(2)]


@pytest.mark.asyncio
async def test_asynccollectiongroup_get_partitions_w_limit():
    # Make a **real** collection reference as parent.
    client = make_async_client()
    parent = client.collection("charles")

    # Make a query that fails to partition
    query = _make_async_collection_group(parent).limit(10)
    with pytest.raises(ValueError):
        [i async for i in query.get_partitions(2)]


@pytest.mark.asyncio
async def test_asynccollectiongroup_get_partitions_w_offset():
    # Make a **real** collection reference as parent.
    client = make_async_client()
    parent = client.collection("charles")

    # Make a query that fails to partition
    query = _make_async_collection_group(parent).offset(10)
    with pytest.raises(ValueError):
        [i async for i in query.get_partitions(2)]


def test_asyncquery_collection_pipeline_type():
    from google.cloud.firestore_v1.async_pipeline import AsyncPipeline

    client = make_async_client()
    parent = client.collection("test")
    query = parent._query()
    ppl = query._build_pipeline(client.pipeline())
    assert isinstance(ppl, AsyncPipeline)


def test_asyncquery_collectiongroup_pipeline_type():
    from google.cloud.firestore_v1.async_pipeline import AsyncPipeline

    client = make_async_client()
    query = client.collection_group("test")
    ppl = query._build_pipeline(client.pipeline())
    assert isinstance(ppl, AsyncPipeline)
