# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from unittest import mock

import pytest
from google.api_core import exceptions
from google.protobuf import descriptor_pb2

from google.cloud.bigquery_storage_v1beta2 import exceptions as bqstorage_exceptions
from google.cloud.bigquery_storage_v1beta2 import types as gapic_types
from google.cloud.bigquery_storage_v1beta2.services import big_query_write

REQUEST_TEMPLATE = gapic_types.AppendRowsRequest()


@pytest.fixture(scope="module")
def module_under_test():
    from google.cloud.bigquery_storage_v1beta2 import writer

    return writer


def test_constructor_and_default_state(module_under_test):
    mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
    manager = module_under_test.AppendRowsStream(mock_client, REQUEST_TEMPLATE)

    # Public state
    assert manager.is_active is False

    # Private state
    assert manager._client is mock_client


def test_close_before_open(module_under_test):
    mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
    manager = module_under_test.AppendRowsStream(mock_client, REQUEST_TEMPLATE)
    manager.close()
    with pytest.raises(bqstorage_exceptions.StreamClosedError):
        manager.send(object())


@mock.patch("google.api_core.bidi.BidiRpc", autospec=True)
@mock.patch("google.api_core.bidi.BackgroundConsumer", autospec=True)
def test_initial_send(background_consumer, bidi_rpc, module_under_test):
    mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
    request_template = gapic_types.AppendRowsRequest(
        write_stream="stream-name-from-REQUEST_TEMPLATE",
        offset=0,
        proto_rows=gapic_types.AppendRowsRequest.ProtoData(
            writer_schema=gapic_types.ProtoSchema(
                proto_descriptor=descriptor_pb2.DescriptorProto()
            )
        ),
    )
    manager = module_under_test.AppendRowsStream(mock_client, request_template)
    type(bidi_rpc.return_value).is_active = mock.PropertyMock(
        return_value=(False, True)
    )
    proto_rows = gapic_types.ProtoRows()
    proto_rows.serialized_rows.append(b"hello, world")
    initial_request = gapic_types.AppendRowsRequest(
        write_stream="this-is-a-stream-resource-path",
        offset=42,
        proto_rows=gapic_types.AppendRowsRequest.ProtoData(rows=proto_rows),
    )

    future = manager.send(initial_request)

    assert isinstance(future, module_under_test.AppendRowsFuture)
    background_consumer.assert_called_once_with(manager._rpc, manager._on_response)
    background_consumer.return_value.start.assert_called_once()
    assert manager._consumer == background_consumer.return_value

    # Make sure the request template and the first request are merged as
    # expected. Needs to be especially careful that nested properties such as
    # writer_schema and rows are merged as expected.
    expected_request = gapic_types.AppendRowsRequest(
        write_stream="this-is-a-stream-resource-path",
        offset=42,
        proto_rows=gapic_types.AppendRowsRequest.ProtoData(
            writer_schema=gapic_types.ProtoSchema(
                proto_descriptor=descriptor_pb2.DescriptorProto()
            ),
            rows=proto_rows,
        ),
    )
    bidi_rpc.assert_called_once_with(
        start_rpc=mock_client.append_rows,
        initial_request=expected_request,
        # Extra header is required to route requests to the correct location.
        metadata=(
            ("x-goog-request-params", "write_stream=this-is-a-stream-resource-path"),
        ),
    )

    bidi_rpc.return_value.add_done_callback.assert_called_once_with(
        manager._on_rpc_done
    )
    assert manager._rpc == bidi_rpc.return_value

    manager._consumer.is_active = True
    assert manager.is_active is True


@mock.patch("google.api_core.bidi.BidiRpc", autospec=True)
@mock.patch("google.api_core.bidi.BackgroundConsumer", autospec=True)
def test_initial_send_with_timeout(background_consumer, bidi_rpc, module_under_test):
    mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
    manager = module_under_test.AppendRowsStream(mock_client, REQUEST_TEMPLATE)
    type(bidi_rpc.return_value).is_active = mock.PropertyMock(return_value=False)
    type(background_consumer.return_value).is_active = mock.PropertyMock(
        return_value=False
    )
    initial_request = gapic_types.AppendRowsRequest(
        write_stream="this-is-a-stream-resource-path"
    )

    now = time.monotonic()
    later = now + module_under_test._DEFAULT_TIMEOUT + 1
    with (
        mock.patch.object(module_under_test.time, "sleep"),
        mock.patch.object(
            module_under_test.time,
            "monotonic",
            mock.MagicMock(side_effect=(now, later)),
        ),
        pytest.raises(exceptions.Unknown),
    ):
        manager.send(initial_request)


def test_future_done_false(module_under_test):
    mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
    manager = module_under_test.AppendRowsStream(mock_client, REQUEST_TEMPLATE)
    future = module_under_test.AppendRowsFuture(manager)
    assert not future.done()


def test_future_done_true_with_result(module_under_test):
    mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
    manager = module_under_test.AppendRowsStream(mock_client, REQUEST_TEMPLATE)
    future = module_under_test.AppendRowsFuture(manager)
    future.set_result(object())
    assert future.done()


def test_future_done_true_with_exception(module_under_test):
    mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
    manager = module_under_test.AppendRowsStream(mock_client, REQUEST_TEMPLATE)
    future = module_under_test.AppendRowsFuture(manager)
    future.set_exception(ValueError())
    assert future.done()
