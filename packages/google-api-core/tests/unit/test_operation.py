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


from unittest import mock

import pytest

try:
    import grpc  # noqa: F401
except ImportError:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)

from google.longrunning import operations_pb2
from google.protobuf import struct_pb2
from google.rpc import code_pb2, status_pb2

from google.api_core import exceptions, operation, operations_v1, retry

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

    refresh = mock.Mock(spec=["__call__"], side_effect=client_operations_responses)
    refresh.responses = client_operations_responses
    cancel = mock.Mock(spec=["__call__"])
    operation_future = operation.Operation(
        client_operations_responses[0],
        refresh,
        cancel,
        result_type=struct_pb2.Struct,
        metadata_type=struct_pb2.Struct,
    )

    return operation_future, refresh, cancel


def test_constructor():
    future, refresh, _ = make_operation_future()

    assert future.operation == refresh.responses[0]
    assert future.operation.done is False
    assert future.operation.name == TEST_OPERATION_NAME
    assert future.metadata is None
    assert future.running()


def test_metadata():
    expected_metadata = struct_pb2.Struct()
    future, _, _ = make_operation_future(
        [make_operation_proto(metadata=expected_metadata)]
    )

    assert future.metadata == expected_metadata


def test_cancellation():
    responses = [
        make_operation_proto(),
        # Second response indicates that the operation was cancelled.
        make_operation_proto(
            done=True, error=status_pb2.Status(code=code_pb2.CANCELLED)
        ),
    ]
    future, _, cancel = make_operation_future(responses)

    assert future.cancel()
    assert future.cancelled()
    cancel.assert_called_once_with()

    # Cancelling twice should have no effect.
    assert not future.cancel()
    cancel.assert_called_once_with()


def test_result():
    expected_result = struct_pb2.Struct()
    responses = [
        make_operation_proto(),
        # Second operation response includes the result.
        make_operation_proto(done=True, response=expected_result),
    ]
    future, _, _ = make_operation_future(responses)

    result = future.result()

    assert result == expected_result
    assert future.done()


def test_done_w_retry():
    RETRY_PREDICATE = retry.if_exception_type(exceptions.TooManyRequests)
    test_retry = retry.Retry(predicate=RETRY_PREDICATE)

    expected_result = struct_pb2.Struct()
    responses = [
        make_operation_proto(),
        # Second operation response includes the result.
        make_operation_proto(done=True, response=expected_result),
    ]
    future, _, _ = make_operation_future(responses)
    future._refresh = mock.Mock()

    future.done(retry=test_retry)
    future._refresh.assert_called_once_with(retry=test_retry)


def test_exception():
    expected_exception = status_pb2.Status(message="meep")
    responses = [
        make_operation_proto(),
        # Second operation response includes the error.
        make_operation_proto(done=True, error=expected_exception),
    ]
    future, _, _ = make_operation_future(responses)

    exception = future.exception()

    assert expected_exception.message in "{!r}".format(exception)


def test_exception_with_error_code():
    expected_exception = status_pb2.Status(message="meep", code=5)
    responses = [
        make_operation_proto(),
        # Second operation response includes the error.
        make_operation_proto(done=True, error=expected_exception),
    ]
    future, _, _ = make_operation_future(responses)

    exception = future.exception()

    assert expected_exception.message in "{!r}".format(exception)
    # Status Code 5 maps to Not Found
    # https://developers.google.com/maps-booking/reference/grpc-api/status_codes
    assert isinstance(exception, exceptions.NotFound)


def test_unexpected_result():
    responses = [
        make_operation_proto(),
        # Second operation response is done, but has not error or response.
        make_operation_proto(done=True),
    ]
    future, _, _ = make_operation_future(responses)

    exception = future.exception()

    assert "Unexpected state" in "{!r}".format(exception)


def test__refresh_http():
    json_response = {"name": TEST_OPERATION_NAME, "done": True}
    api_request = mock.Mock(return_value=json_response)

    result = operation._refresh_http(api_request, TEST_OPERATION_NAME)

    assert isinstance(result, operations_pb2.Operation)
    assert result.name == TEST_OPERATION_NAME
    assert result.done is True

    api_request.assert_called_once_with(
        method="GET", path="operations/{}".format(TEST_OPERATION_NAME)
    )


def test__refresh_http_w_retry():
    json_response = {"name": TEST_OPERATION_NAME, "done": True}
    api_request = mock.Mock()
    retry = mock.Mock()
    retry.return_value.return_value = json_response

    result = operation._refresh_http(api_request, TEST_OPERATION_NAME, retry=retry)

    assert isinstance(result, operations_pb2.Operation)
    assert result.name == TEST_OPERATION_NAME
    assert result.done is True

    api_request.assert_not_called()
    retry.assert_called_once_with(api_request)
    retry.return_value.assert_called_once_with(
        method="GET", path="operations/{}".format(TEST_OPERATION_NAME)
    )


def test__cancel_http():
    api_request = mock.Mock()

    operation._cancel_http(api_request, TEST_OPERATION_NAME)

    api_request.assert_called_once_with(
        method="POST", path="operations/{}:cancel".format(TEST_OPERATION_NAME)
    )


def test_from_http_json():
    operation_json = {"name": TEST_OPERATION_NAME, "done": True}
    api_request = mock.sentinel.api_request

    future = operation.from_http_json(
        operation_json, api_request, struct_pb2.Struct, metadata_type=struct_pb2.Struct
    )

    assert future._result_type == struct_pb2.Struct
    assert future._metadata_type == struct_pb2.Struct
    assert future.operation.name == TEST_OPERATION_NAME
    assert future.done


def test__refresh_grpc():
    operations_stub = mock.Mock(spec=["GetOperation"])
    expected_result = make_operation_proto(done=True)
    operations_stub.GetOperation.return_value = expected_result

    result = operation._refresh_grpc(operations_stub, TEST_OPERATION_NAME)

    assert result == expected_result
    expected_request = operations_pb2.GetOperationRequest(name=TEST_OPERATION_NAME)
    operations_stub.GetOperation.assert_called_once_with(expected_request)


def test__refresh_grpc_w_retry():
    operations_stub = mock.Mock(spec=["GetOperation"])
    expected_result = make_operation_proto(done=True)
    retry = mock.Mock()
    retry.return_value.return_value = expected_result

    result = operation._refresh_grpc(operations_stub, TEST_OPERATION_NAME, retry=retry)

    assert result == expected_result
    expected_request = operations_pb2.GetOperationRequest(name=TEST_OPERATION_NAME)
    operations_stub.GetOperation.assert_not_called()
    retry.assert_called_once_with(operations_stub.GetOperation)
    retry.return_value.assert_called_once_with(expected_request)


def test__cancel_grpc():
    operations_stub = mock.Mock(spec=["CancelOperation"])

    operation._cancel_grpc(operations_stub, TEST_OPERATION_NAME)

    expected_request = operations_pb2.CancelOperationRequest(name=TEST_OPERATION_NAME)
    operations_stub.CancelOperation.assert_called_once_with(expected_request)


def test_from_grpc():
    operation_proto = make_operation_proto(done=True)
    operations_stub = mock.sentinel.operations_stub

    future = operation.from_grpc(
        operation_proto,
        operations_stub,
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


def test_from_gapic():
    operation_proto = make_operation_proto(done=True)
    operations_client = mock.create_autospec(
        operations_v1.OperationsClient, instance=True
    )

    future = operation.from_gapic(
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
    deserialized_op = operation.Operation.deserialize(serialized)
    assert op.name == deserialized_op.name
    assert type(op) is type(deserialized_op)
