# Copyright 2017, Google LLC
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

try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER  # noqa: F401
except ImportError:  # pragma: NO COVER
    import mock  # type: ignore

try:
    import grpc  # noqa: F401
except ImportError:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)

from google.longrunning import operations_pb2
from google.protobuf import struct_pb2
from google.rpc import code_pb2, status_pb2

from google.api_core import exceptions, operation_async, operations_v1, retry_async

TEST_OPERATION_NAME = "test/operation"


def make_operation_proto(
    name=TEST_OPERATION_NAME, metadata=None, response=None, error=None, **kwargs
):
    operation_proto = operations_pb2.Operation(name=name, **kwargs)

    if metadata is not None:
        operation_proto.metadata.Pack(metadata)

    if response is not None:
        operation_proto.response.Pack(response)

    if error is not None:
        operation_proto.error.CopyFrom(error)

    return operation_proto


def make_operation_future(client_operations_responses=None):
    if client_operations_responses is None:
        client_operations_responses = [make_operation_proto()]

    refresh = mock.AsyncMock(spec=["__call__"], side_effect=client_operations_responses)
    refresh.responses = client_operations_responses
    cancel = mock.AsyncMock(spec=["__call__"])
    operation_future = operation_async.AsyncOperation(
        client_operations_responses[0],
        refresh,
        cancel,
        result_type=struct_pb2.Struct,
        metadata_type=struct_pb2.Struct,
    )

    return operation_future, refresh, cancel


@pytest.mark.asyncio
async def test_constructor():
    future, refresh, _ = make_operation_future()

    assert future.operation == refresh.responses[0]
    assert future.operation.done is False
    assert future.operation.name == TEST_OPERATION_NAME
    assert future.metadata is None
    assert await future.running()


@pytest.mark.asyncio
async def test_metadata():
    expected_metadata = struct_pb2.Struct()
    future, _, _ = make_operation_future(
        [make_operation_proto(metadata=expected_metadata)]
    )

    assert future.metadata == expected_metadata


@pytest.mark.asyncio
async def test_cancellation():
    responses = [
        make_operation_proto(),
        # Second response indicates that the operation was cancelled.
        make_operation_proto(
            done=True, error=status_pb2.Status(code=code_pb2.CANCELLED)
        ),
    ]
    future, _, cancel = make_operation_future(responses)

    assert await future.cancel()
    assert await future.cancelled()
    cancel.assert_called_once_with()

    # Cancelling twice should have no effect.
    assert not await future.cancel()
    cancel.assert_called_once_with()


@pytest.mark.asyncio
async def test_result():
    expected_result = struct_pb2.Struct()
    responses = [
        make_operation_proto(),
        # Second operation response includes the result.
        make_operation_proto(done=True, response=expected_result),
    ]
    future, _, _ = make_operation_future(responses)

    result = await future.result()

    assert result == expected_result
    assert await future.done()


@pytest.mark.asyncio
async def test_done_w_retry():
    RETRY_PREDICATE = retry_async.if_exception_type(exceptions.TooManyRequests)
    test_retry = retry_async.AsyncRetry(predicate=RETRY_PREDICATE)

    expected_result = struct_pb2.Struct()
    responses = [
        make_operation_proto(),
        # Second operation response includes the result.
        make_operation_proto(done=True, response=expected_result),
    ]
    future, refresh, _ = make_operation_future(responses)

    await future.done(retry=test_retry)
    refresh.assert_called_once_with(retry=test_retry)


@pytest.mark.asyncio
async def test_exception():
    expected_exception = status_pb2.Status(message="meep")
    responses = [
        make_operation_proto(),
        # Second operation response includes the error.
        make_operation_proto(done=True, error=expected_exception),
    ]
    future, _, _ = make_operation_future(responses)

    exception = await future.exception()

    assert expected_exception.message in "{!r}".format(exception)


@mock.patch("asyncio.sleep", autospec=True)
@pytest.mark.asyncio
async def test_unexpected_result(unused_sleep):
    responses = [
        make_operation_proto(),
        # Second operation response is done, but has not error or response.
        make_operation_proto(done=True),
    ]
    future, _, _ = make_operation_future(responses)

    exception = await future.exception()

    assert "Unexpected state" in "{!r}".format(exception)


@pytest.mark.asyncio
async def test_from_gapic():
    operation_proto = make_operation_proto(done=True)
    operations_client = mock.create_autospec(
        operations_v1.OperationsAsyncClient, instance=True
    )

    future = operation_async.from_gapic(
        operation_proto,
        operations_client,
        struct_pb2.Struct,
        metadata_type=struct_pb2.Struct,
        grpc_metadata=[("x-goog-request-params", "foo")],
    )

    assert future._result_type == struct_pb2.Struct
    assert future._metadata_type == struct_pb2.Struct
    assert future.operation.name == TEST_OPERATION_NAME
    assert future.done
    assert future._refresh.keywords["metadata"] == [("x-goog-request-params", "foo")]
    assert future._cancel.keywords["metadata"] == [("x-goog-request-params", "foo")]


def test_deserialize():
    op = make_operation_proto(name="foobarbaz")
    serialized = op.SerializeToString()
    deserialized_op = operation_async.AsyncOperation.deserialize(serialized)
    assert op.name == deserialized_op.name
    assert type(op) is type(deserialized_op)
