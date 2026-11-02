# Copyright 2026 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
import sys
import uuid
from unittest import mock

import pytest
from google.protobuf import descriptor_pb2, descriptor_pool


def test_operations_descriptor_name():
    """Validates the canonical proto name registered in the descriptor pool."""
    from google.longrunning import operations_pb2

    # The descriptor name MUST be the canonical path 'google/longrunning/operations.proto'.
    # If named 'google/longrunning/operations_proto.proto', any downstream proto that
    # imports 'google/longrunning/operations.proto' will fail to resolve.
    assert operations_pb2.DESCRIPTOR.name == "google/longrunning/operations.proto"

    # Verify lookup by canonical path succeeds in the global descriptor pool
    pool = descriptor_pool.Default()
    file_desc = pool.FindFileByName("google/longrunning/operations.proto")
    assert file_desc is not None
    assert file_desc.name == "google/longrunning/operations.proto"


def test_operations_message_instantiation():
    """Validates message instantiation from both public module entry points."""
    from google.longrunning import operations_pb2, operations_proto_pb2

    op1 = operations_pb2.Operation(name="operations/123", done=True)
    assert op1.name == "operations/123"
    assert op1.done is True

    op2 = operations_proto_pb2.Operation(name="operations/456", done=False)
    assert op2.name == "operations/456"
    assert op2.done is False


def test_downstream_dependency_resolution():
    """Regression test for b/566222096.

    Downstream clients compile protos containing:
        import "google/longrunning/operations.proto";

    When their generated *_pb2 modules load, protobuf calls:

    ```
        _descriptor_pool.Default().AddSerializedFile(...)
    ```

    which checks that 'google/longrunning/operations.proto' exists in the pool.
    """
    # Ensure operations_pb2 is imported and registered
    from google.longrunning import operations_pb2  # noqa: F401

    pool = descriptor_pool.Default()

    # Create a uniquely named proto to avoid collision during repeated test runs
    unique_name = f"google/test/downstream_{uuid.uuid4().hex}.proto"

    downstream_file = descriptor_pb2.FileDescriptorProto()
    downstream_file.name = unique_name
    downstream_file.package = "google.test"
    downstream_file.dependency.append("google/longrunning/operations.proto")

    # 1. This step will throw the TypeError if operations.proto is missing (under C++ runtime).
    pool.Add(downstream_file)

    # 2. Retrieve the descriptor from the pool (required because pool.Add() returns None).
    file_descriptor = pool.FindFileByName(unique_name)
    assert file_descriptor is not None
    assert file_descriptor.name == unique_name
    assert "google/longrunning/operations.proto" in [
        dep.name for dep in file_descriptor.dependencies
    ]


def test_operations_servicer_interface():
    """Verifies OperationsServicer default method implementations raise NotImplementedError."""
    from google.longrunning import operations_pb2_grpc

    servicer = operations_pb2_grpc.OperationsServicer()
    context = mock.Mock()
    request = mock.Mock()

    # Servicer interface must define all RPCs and default to NotImplementedError
    for method in [
        servicer.ListOperations,
        servicer.GetOperation,
        servicer.DeleteOperation,
        servicer.CancelOperation,
        servicer.WaitOperation,
    ]:
        with pytest.raises(NotImplementedError):
            method(request, context)


def test_add_operations_servicer_to_server():
    """Verifies server handler registration for OperationsServicer."""
    from google.longrunning import operations_pb2_grpc

    servicer = operations_pb2_grpc.OperationsServicer()
    mock_server = mock.Mock()

    operations_pb2_grpc.add_OperationsServicer_to_server(servicer, mock_server)

    # Assert that generic RPC handlers were registered with the server
    assert mock_server.add_generic_rpc_handlers.called
    assert mock_server.add_generic_rpc_handlers.call_count == 1

    # Verify the handler structure passed to the server
    handlers = mock_server.add_generic_rpc_handlers.call_args[0][0]
    assert len(handlers) == 1
    assert hasattr(handlers[0], "service_name")
    assert handlers[0].service_name() == "google.longrunning.Operations"


def test_operations_client_stubs_and_static_methods():
    """Verifies OperationsStub client calls and static method dispatch."""
    from google.longrunning import operations_pb2_grpc

    # 1. Test OperationsStub channel binding and RPC dispatch
    mock_callable = mock.Mock(return_value=mock.Mock())
    mock_channel = mock.Mock()
    mock_channel.unary_unary = mock.Mock(return_value=mock_callable)
    mock_channel.unary_stream = mock.Mock(return_value=mock_callable)

    stub = operations_pb2_grpc.OperationsStub(mock_channel)
    assert mock_channel.unary_unary.call_count == 5

    request = mock.Mock()
    for rpc in [
        stub.ListOperations,
        stub.GetOperation,
        stub.DeleteOperation,
        stub.CancelOperation,
        stub.WaitOperation,
    ]:
        response = rpc(request)
        assert response is not None

    assert mock_callable.call_count == 5

    # 2. Test Operations static invocation helpers
    with mock.patch(
        "grpc.experimental.unary_unary", return_value=mock.Mock()
    ) as mock_unary:
        for static_rpc in [
            operations_pb2_grpc.Operations.ListOperations,
            operations_pb2_grpc.Operations.GetOperation,
            operations_pb2_grpc.Operations.DeleteOperation,
            operations_pb2_grpc.Operations.CancelOperation,
            operations_pb2_grpc.Operations.WaitOperation,
        ]:
            result = static_rpc(request, "localhost:50051")
            assert result is not None

        assert mock_unary.call_count == 5


def test_operations_pb2_non_grpc_fallback_environment():
    """Verifies module loading and class contract in non-gRPC environments.

    In environments where gRPC is unsupported, the module must fall back to pure
    protobuf-only imports without throwing exceptions, and all message classes
    must remain instantiable.
    """
    # 1. Simulate an environment where the gRPC-dependent pb2 module is unavailable
    with mock.patch.dict(sys.modules, {"google.longrunning.operations_grpc_pb2": None}):
        # Reload to force execution of the fallback import path
        if "google.longrunning.operations_pb2" in sys.modules:
            fallback_module = importlib.reload(
                sys.modules["google.longrunning.operations_pb2"]
            )
        else:
            import google.longrunning.operations_pb2 as fallback_module  # pragma: NO COVER

        # 2. Assert that canonical messages can still be resolved and instantiated
        assert hasattr(fallback_module, "Operation")
        assert hasattr(fallback_module, "GetOperationRequest")

        op = fallback_module.Operation(name="operations/789", done=True)
        assert op.name == "operations/789"
        assert op.done is True

    # 3. Restore the environment back to its gRPC-enabled state
    importlib.reload(sys.modules["google.longrunning.operations_pb2"])
