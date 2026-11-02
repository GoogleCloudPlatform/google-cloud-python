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

from google.cloud.firestore_v1._helpers import encode_value, make_retry_timeout_kwargs
from google.cloud.firestore_v1.async_stream_generator import AsyncStreamGenerator
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
from google.cloud.firestore_v1.query_profile import (
    ExplainMetrics,
    ExplainOptions,
    QueryExplainError,
)
from google.cloud.firestore_v1.query_results import QueryResultsList
from google.cloud.firestore_v1.types.query import StructuredQuery
from google.cloud.firestore_v1.vector import Vector
from tests.unit.v1._test_helpers import (
    make_async_client,
    make_async_query,
    make_async_vector_query,
    make_query,
)
from tests.unit.v1.test__helpers import AsyncIter, AsyncMock
from tests.unit.v1.test_base_query import _make_query_response

_PROJECT = "PROJECT"
_TXN_ID = b"\x00\x00\x01-work-\xf2"


def _transaction(client):
    transaction = client.transaction()
    txn_id = _TXN_ID
    transaction._id = txn_id
    return transaction


def _expected_pb(
    parent,
    vector_field,
    vector,
    distance_type,
    limit,
    distance_result_field=None,
    distance_threshold=None,
):
    query = make_query(parent)
    expected_pb = query._to_protobuf()
    expected_pb.find_nearest = StructuredQuery.FindNearest(
        vector_field=StructuredQuery.FieldReference(field_path=vector_field),
        query_vector=encode_value(vector.to_map_value()),
        distance_measure=distance_type,
        limit=limit,
        distance_result_field=distance_result_field,
        distance_threshold=distance_threshold,
    )
    return expected_pb


async def _async_vector_query_get_helper(
    distance_measure,
    expected_distance,
    explain_options=None,
):
    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    parent_path, expected_prefix = parent._parent_info()

    data = {"snooze": 10, "embedding": Vector([1.0, 2.0, 3.0])}
    if explain_options:
        explain_metrics = {"execution_stats": {"results_returned": 1}}
    else:
        explain_metrics = None
    response_pb1 = _make_query_response(
        name="{}/test_doc".format(expected_prefix),
        data=data,
        explain_metrics=explain_metrics,
    )

    kwargs = make_retry_timeout_kwargs(retry=None, timeout=None)

    # Execute the vector query and check the response.
    firestore_api.run_query.return_value = AsyncIter([response_pb1])

    vector_async_query = parent.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=5,
    )

    returned = await vector_async_query.get(
        transaction=_transaction(client), explain_options=explain_options, **kwargs
    )
    assert isinstance(returned, QueryResultsList)
    assert len(returned) == 1
    assert returned[0].to_dict() == data

    if explain_options is None:
        with pytest.raises(QueryExplainError, match="explain_options not set"):
            returned.get_explain_metrics()
    else:
        actual_explain_metrics = returned.get_explain_metrics()
        assert isinstance(actual_explain_metrics, ExplainMetrics)
        assert actual_explain_metrics.execution_stats.results_returned == 1

    # Create expected request body.
    expected_pb = _expected_pb(
        parent=parent,
        vector_field="embedding",
        vector=Vector([1.0, 2.0, 3.0]),
        distance_type=expected_distance,
        limit=5,
    )
    request = {
        "parent": parent_path,
        "structured_query": expected_pb,
        "transaction": _TXN_ID,
    }
    if explain_options:
        request["explain_options"] = explain_options._to_dict()

    firestore_api.run_query.assert_called_once_with(
        request=request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


def test_async_vector_query_int_threshold_constructor_to_pb():
    client = make_async_client()
    parent = client.collection("dee")
    query = make_async_query(parent)
    vector_query = make_async_vector_query(query)

    assert vector_query._nested_query == query
    assert vector_query._client == query._parent._client

    vector_query.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.EUCLIDEAN,
        limit=5,
        distance_threshold=5,
    )

    expected_pb = query._to_protobuf()
    expected_pb.find_nearest = StructuredQuery.FindNearest(
        vector_field=StructuredQuery.FieldReference(field_path="embedding"),
        query_vector=encode_value(Vector([1.0, 2.0, 3.0]).to_map_value()),
        distance_measure=StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        limit=5,
        distance_threshold=5.0,
    )
    assert vector_query._to_protobuf() == expected_pb


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_async_vector_query_get(distance_measure, expected_distance):
    await _async_vector_query_get_helper(distance_measure, expected_distance)


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_async_vector_query_get_w_explain_options(
    distance_measure, expected_distance
):
    explain_options = ExplainOptions(analyze=True)
    await _async_vector_query_get_helper(
        distance_measure, expected_distance, explain_options
    )


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_async_vector_query_with_filter(distance_measure, expected_distance):
    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    query = make_async_query(parent)
    parent_path, expected_prefix = parent._parent_info()

    data = {"snooze": 10, "embedding": Vector([1.0, 2.0, 3.0])}
    response_pb1 = _make_query_response(
        name="{}/test_doc".format(expected_prefix), data=data
    )
    response_pb2 = _make_query_response(
        name="{}/test_doc".format(expected_prefix), data=data
    )

    kwargs = make_retry_timeout_kwargs(retry=None, timeout=None)

    # Execute the vector query and check the response.
    firestore_api.run_query.return_value = AsyncIter([response_pb1, response_pb2])

    vector_async_query = query.where("snooze", "==", 10).find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=5,
    )

    returned = await vector_async_query.get(transaction=_transaction(client), **kwargs)
    assert isinstance(returned, list)
    assert len(returned) == 2
    assert returned[0].to_dict() == data

    expected_pb = _expected_pb(
        parent=parent,
        vector_field="embedding",
        vector=Vector([1.0, 2.0, 3.0]),
        distance_type=expected_distance,
        limit=5,
    )
    expected_pb.where = StructuredQuery.Filter(
        field_filter=StructuredQuery.FieldFilter(
            field=StructuredQuery.FieldReference(field_path="snooze"),
            op=StructuredQuery.FieldFilter.Operator.EQUAL,
            value=encode_value(10),
        )
    )

    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": expected_pb,
            "transaction": _TXN_ID,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_async_vector_query_with_distance_result_field(
    distance_measure, expected_distance
):
    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    query = make_async_query(parent)
    parent_path, expected_prefix = parent._parent_info()

    data = {"snooze": 10, "embedding": Vector([1.0, 2.0, 3.5]), "vector_distance": 0.5}
    response_pb1 = _make_query_response(
        name="{}/test_doc".format(expected_prefix), data=data
    )
    response_pb2 = _make_query_response(
        name="{}/test_doc".format(expected_prefix), data=data
    )

    kwargs = make_retry_timeout_kwargs(retry=None, timeout=None)

    # Execute the vector query and check the response.
    firestore_api.run_query.return_value = AsyncIter([response_pb1, response_pb2])

    vector_async__query = query.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=5,
        distance_result_field="vector_distance",
    )

    returned = await vector_async__query.get(transaction=_transaction(client), **kwargs)
    assert isinstance(returned, list)
    assert len(returned) == 2
    assert returned[0].to_dict() == data

    expected_pb = _expected_pb(
        parent=parent,
        vector_field="embedding",
        vector=Vector([1.0, 2.0, 3.0]),
        distance_type=expected_distance,
        limit=5,
        distance_result_field="vector_distance",
    )

    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": expected_pb,
            "transaction": _TXN_ID,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_async_vector_query_with_distance_threshold(
    distance_measure, expected_distance
):
    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    query = make_async_query(parent)
    parent_path, expected_prefix = parent._parent_info()

    data = {"snooze": 10, "embedding": Vector([1.0, 2.0, 3.5])}
    response_pb1 = _make_query_response(
        name="{}/test_doc".format(expected_prefix), data=data
    )
    response_pb2 = _make_query_response(
        name="{}/test_doc".format(expected_prefix), data=data
    )

    kwargs = make_retry_timeout_kwargs(retry=None, timeout=None)

    # Execute the vector query and check the response.
    firestore_api.run_query.return_value = AsyncIter([response_pb1, response_pb2])

    vector_async__query = query.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=5,
        distance_threshold=125.5,
    )

    returned = await vector_async__query.get(transaction=_transaction(client), **kwargs)
    assert isinstance(returned, list)
    assert len(returned) == 2
    assert returned[0].to_dict() == data

    expected_pb = _expected_pb(
        parent=parent,
        vector_field="embedding",
        vector=Vector([1.0, 2.0, 3.0]),
        distance_type=expected_distance,
        limit=5,
        distance_threshold=125.5,
    )

    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": expected_pb,
            "transaction": _TXN_ID,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_vector_query_collection_group(distance_measure, expected_distance):
    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection group reference as parent.
    collection_group_ref = client.collection_group("dee")

    data = {"snooze": 10, "embedding": Vector([1.0, 2.0, 3.0])}
    response_pb = _make_query_response(name="xxx/test_doc", data=data)

    kwargs = make_retry_timeout_kwargs(retry=None, timeout=None)

    # Execute the vector query and check the response.
    firestore_api.run_query.return_value = AsyncIter([response_pb])

    vector_query = collection_group_ref.where("snooze", "==", 10).find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=5,
    )

    returned = await vector_query.get(transaction=_transaction(client), **kwargs)
    assert isinstance(returned, list)
    assert len(returned) == 1
    assert returned[0].to_dict() == data

    parent = client.collection("dee")
    parent_path, expected_prefix = parent._parent_info()

    expected_pb = _expected_pb(
        parent=parent,
        vector_field="embedding",
        vector=Vector([1.0, 2.0, 3.0]),
        distance_type=expected_distance,
        limit=5,
    )
    expected_pb.where = StructuredQuery.Filter(
        field_filter=StructuredQuery.FieldFilter(
            field=StructuredQuery.FieldReference(field_path="snooze"),
            op=StructuredQuery.FieldFilter.Operator.EQUAL,
            value=encode_value(10),
        )
    )
    expected_pb.from_ = [
        StructuredQuery.CollectionSelector(collection_id="dee", all_descendants=True)
    ]

    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": expected_pb,
            "transaction": _TXN_ID,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.asyncio
async def test_async_query_stream_multiple_empty_response_in_stream():
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
    async_vector_query = parent.where("snooze", "==", 10).find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=DistanceMeasure.EUCLIDEAN,
        limit=5,
    )

    result = [snapshot async for snapshot in async_vector_query.stream()]

    assert list(result) == []

    # Verify the mock call.
    parent_path, _ = parent._parent_info()
    firestore_api.run_query.assert_called_once_with(
        request={
            "parent": parent_path,
            "structured_query": async_vector_query._to_protobuf(),
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


async def _async_vector_query_stream_helper(
    distance_measure,
    expected_distance,
    explain_options=None,
):
    # Create a minimal fake GAPIC.
    firestore_api = AsyncMock(spec=["run_query"])
    client = make_async_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")
    parent_path, expected_prefix = parent._parent_info()

    data = {"snooze": 10, "embedding": Vector([1.0, 2.0, 3.0])}
    if explain_options:
        explain_metrics = {"execution_stats": {"results_returned": 1}}
    else:
        explain_metrics = None
    response_pb1 = _make_query_response(
        name="{}/test_doc".format(expected_prefix),
        data=data,
        explain_metrics=explain_metrics,
    )

    kwargs = make_retry_timeout_kwargs(retry=None, timeout=None)

    # Execute the vector query and check the response.
    firestore_api.run_query.return_value = AsyncIter([response_pb1])

    vector_async_query = parent.find_nearest(
        vector_field="embedding",
        query_vector=Vector([1.0, 2.0, 3.0]),
        distance_measure=distance_measure,
        limit=5,
    )

    returned = vector_async_query.stream(
        transaction=_transaction(client), explain_options=explain_options, **kwargs
    )
    assert isinstance(returned, AsyncStreamGenerator)

    results_list = [item async for item in returned]
    await returned.aclose()
    assert len(results_list) == 1
    assert results_list[0].to_dict() == data

    if explain_options is None:
        with pytest.raises(QueryExplainError, match="explain_options not set"):
            await returned.get_explain_metrics()
    else:
        actual_explain_metrics = await returned.get_explain_metrics()
        assert isinstance(actual_explain_metrics, ExplainMetrics)
        assert actual_explain_metrics.execution_stats.results_returned == 1

    # Create expected request body.
    expected_pb = _expected_pb(
        parent=parent,
        vector_field="embedding",
        vector=Vector([1.0, 2.0, 3.0]),
        distance_type=expected_distance,
        limit=5,
    )
    request = {
        "parent": parent_path,
        "structured_query": expected_pb,
        "transaction": _TXN_ID,
    }
    if explain_options:
        request["explain_options"] = explain_options._to_dict()

    firestore_api.run_query.assert_called_once_with(
        request=request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_async_vector_query_stream(distance_measure, expected_distance):
    await _async_vector_query_stream_helper(distance_measure, expected_distance)


@pytest.mark.parametrize(
    "distance_measure, expected_distance",
    [
        (
            DistanceMeasure.EUCLIDEAN,
            StructuredQuery.FindNearest.DistanceMeasure.EUCLIDEAN,
        ),
        (DistanceMeasure.COSINE, StructuredQuery.FindNearest.DistanceMeasure.COSINE),
        (
            DistanceMeasure.DOT_PRODUCT,
            StructuredQuery.FindNearest.DistanceMeasure.DOT_PRODUCT,
        ),
    ],
)
@pytest.mark.asyncio
async def test_async_vector_query_stream_w_explain_options(
    distance_measure, expected_distance
):
    explain_options = ExplainOptions(analyze=True)
    await _async_vector_query_stream_helper(
        distance_measure, expected_distance, explain_options
    )
