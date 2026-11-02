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

from unittest import mock

import pytest

try:
    from grpc import Compression, aio
except ImportError:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)

from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.api_core import grpc_helpers_async, operations_v1, page_iterator_async


def _mock_grpc_objects(response):
    fake_call = grpc_helpers_async.FakeUnaryUnaryCall(response)
    method = mock.Mock(spec=aio.UnaryUnaryMultiCallable, return_value=fake_call)
    mocked_channel = mock.Mock()
    mocked_channel.unary_unary = mock.Mock(return_value=method)
    return mocked_channel, method, fake_call


@pytest.mark.asyncio
async def test_get_operation():
    mocked_channel, method, fake_call = _mock_grpc_objects(
        operations_pb2.Operation(name="meep")
    )
    client = operations_v1.OperationsAsyncClient(mocked_channel)

    response = await client.get_operation(
        "name", metadata=[("header", "foo")], compression=Compression.Gzip
    )
    assert method.call_count == 1
    assert tuple(method.call_args_list[0])[0][0].name == "name"
    assert ("header", "foo") in tuple(method.call_args_list[0])[1]["metadata"]
    assert tuple(method.call_args_list[0])[1]["compression"] == Compression.Gzip
    assert ("x-goog-request-params", "name=name") in tuple(method.call_args_list[0])[1][
        "metadata"
    ]
    assert response == fake_call.response


@pytest.mark.asyncio
async def test_list_operations():
    operations = [
        operations_pb2.Operation(name="1"),
        operations_pb2.Operation(name="2"),
    ]
    list_response = operations_pb2.ListOperationsResponse(operations=operations)

    mocked_channel, method, fake_call = _mock_grpc_objects(list_response)
    client = operations_v1.OperationsAsyncClient(mocked_channel)

    pager = await client.list_operations(
        "name", "filter", metadata=[("header", "foo")], compression=Compression.Gzip
    )

    assert isinstance(pager, page_iterator_async.AsyncIterator)
    responses = []
    async for response in pager:
        responses.append(response)

    assert responses == operations

    assert method.call_count == 1
    assert ("header", "foo") in tuple(method.call_args_list[0])[1]["metadata"]
    assert tuple(method.call_args_list[0])[1]["compression"] == Compression.Gzip
    assert ("x-goog-request-params", "name=name") in tuple(method.call_args_list[0])[1][
        "metadata"
    ]
    request = tuple(method.call_args_list[0])[0][0]
    assert isinstance(request, operations_pb2.ListOperationsRequest)
    assert request.name == "name"
    assert request.filter == "filter"


@pytest.mark.asyncio
async def test_delete_operation():
    mocked_channel, method, fake_call = _mock_grpc_objects(empty_pb2.Empty())
    client = operations_v1.OperationsAsyncClient(mocked_channel)

    await client.delete_operation(
        "name", metadata=[("header", "foo")], compression=Compression.Gzip
    )

    assert method.call_count == 1
    assert tuple(method.call_args_list[0])[0][0].name == "name"
    assert ("header", "foo") in tuple(method.call_args_list[0])[1]["metadata"]
    assert tuple(method.call_args_list[0])[1]["compression"] == Compression.Gzip
    assert ("x-goog-request-params", "name=name") in tuple(method.call_args_list[0])[1][
        "metadata"
    ]


@pytest.mark.asyncio
async def test_cancel_operation():
    mocked_channel, method, fake_call = _mock_grpc_objects(empty_pb2.Empty())
    client = operations_v1.OperationsAsyncClient(mocked_channel)

    await client.cancel_operation(
        "name", metadata=[("header", "foo")], compression=Compression.Gzip
    )

    assert method.call_count == 1
    assert tuple(method.call_args_list[0])[0][0].name == "name"
    assert ("header", "foo") in tuple(method.call_args_list[0])[1]["metadata"]
    assert tuple(method.call_args_list[0])[1]["compression"] == Compression.Gzip
    assert ("x-goog-request-params", "name=name") in tuple(method.call_args_list[0])[1][
        "metadata"
    ]
