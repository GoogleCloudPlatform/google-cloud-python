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

import pytest

try:
    import grpc  # noqa: F401
except ImportError:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)

from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.api_core import grpc_helpers, operations_v1, page_iterator
from google.api_core.operations_v1 import operations_client_config


def test_get_operation():
    channel = grpc_helpers.ChannelStub()
    client = operations_v1.OperationsClient(channel)
    channel.GetOperation.response = operations_pb2.Operation(name="meep")

    response = client.get_operation("name", metadata=[("header", "foo")])

    assert ("header", "foo") in channel.GetOperation.calls[0].metadata
    assert ("x-goog-request-params", "name=name") in channel.GetOperation.calls[
        0
    ].metadata
    assert len(channel.GetOperation.requests) == 1
    assert channel.GetOperation.requests[0].name == "name"
    assert response == channel.GetOperation.response


def test_list_operations():
    channel = grpc_helpers.ChannelStub()
    client = operations_v1.OperationsClient(channel)
    operations = [
        operations_pb2.Operation(name="1"),
        operations_pb2.Operation(name="2"),
    ]
    list_response = operations_pb2.ListOperationsResponse(operations=operations)
    channel.ListOperations.response = list_response

    response = client.list_operations("name", "filter", metadata=[("header", "foo")])

    assert isinstance(response, page_iterator.Iterator)
    assert list(response) == operations

    assert ("header", "foo") in channel.ListOperations.calls[0].metadata
    assert ("x-goog-request-params", "name=name") in channel.ListOperations.calls[
        0
    ].metadata
    assert len(channel.ListOperations.requests) == 1
    request = channel.ListOperations.requests[0]
    assert isinstance(request, operations_pb2.ListOperationsRequest)
    assert request.name == "name"
    assert request.filter == "filter"


def test_delete_operation():
    channel = grpc_helpers.ChannelStub()
    client = operations_v1.OperationsClient(channel)
    channel.DeleteOperation.response = empty_pb2.Empty()

    client.delete_operation("name", metadata=[("header", "foo")])

    assert ("header", "foo") in channel.DeleteOperation.calls[0].metadata
    assert ("x-goog-request-params", "name=name") in channel.DeleteOperation.calls[
        0
    ].metadata
    assert len(channel.DeleteOperation.requests) == 1
    assert channel.DeleteOperation.requests[0].name == "name"


def test_cancel_operation():
    channel = grpc_helpers.ChannelStub()
    client = operations_v1.OperationsClient(channel)
    channel.CancelOperation.response = empty_pb2.Empty()

    client.cancel_operation("name", metadata=[("header", "foo")])

    assert ("header", "foo") in channel.CancelOperation.calls[0].metadata
    assert ("x-goog-request-params", "name=name") in channel.CancelOperation.calls[
        0
    ].metadata
    assert len(channel.CancelOperation.requests) == 1
    assert channel.CancelOperation.requests[0].name == "name"


def test_operations_client_config():
    assert operations_client_config.config["interfaces"]


def test_operations_v1_transport_base_to_dict_protobuf_versions(monkeypatch):
    from google.auth import credentials as ga_credentials
    from google.longrunning import operations_pb2

    from google.api_core.operations_v1.transports import base

    message = operations_pb2.Operation(name="test_op")
    transport = base.OperationsTransport(
        credentials=ga_credentials.AnonymousCredentials()
    )

    calls = []

    def mock_message_to_dict(*args, **kwargs):
        calls.append(kwargs)
        return {"name": "test_op"}

    monkeypatch.setattr(base.json_format, "MessageToDict", mock_message_to_dict)

    monkeypatch.setattr(base, "PROTOBUF_VERSION", "3.20.0")
    res3 = transport._convert_protobuf_message_to_dict(message)
    assert res3.get("name") == "test_op"
    assert "including_default_value_fields" in calls[-1]

    monkeypatch.setattr(base, "PROTOBUF_VERSION", "5.26.0")
    res5 = transport._convert_protobuf_message_to_dict(message)
    assert res5.get("name") == "test_op"
    assert "always_print_fields_with_no_presence" in calls[-1]


def test_operations_v1_init_import_error_fallback(monkeypatch):
    import importlib

    import google.api_core.operations_v1 as op_v1

    orig_import = __import__

    def mock_import(name, globals=None, locals=None, fromlist=(), level=0):
        if "operations_rest_client_async" in name or (
            fromlist and "AsyncOperationsRestClient" in fromlist
        ):
            raise ImportError("Simulated async rest import error")
        return orig_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr("builtins.__import__", mock_import)
    monkeypatch.setattr(op_v1, "_has_async_rest", True)
    importlib.reload(op_v1)
