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

import queue
import threading
import time
import unittest
from unittest import mock

import pytest
from google.api_core import exceptions
from google.protobuf import descriptor_pb2

from google.cloud.bigquery_storage_v1 import exceptions as bqstorage_exceptions
from google.cloud.bigquery_storage_v1 import gapic_version as package_version
from google.cloud.bigquery_storage_v1 import types as gapic_types
from google.cloud.bigquery_storage_v1.services import big_query_write

REQUEST_TEMPLATE = gapic_types.AppendRowsRequest()


class TestAppendRowsStream(unittest.TestCase):
    @staticmethod
    def _make_mock_client():
        return mock.create_autospec(big_query_write.BigQueryWriteClient)

    @staticmethod
    def _make_mock_connection():
        from google.cloud.bigquery_storage_v1.writer import _Connection

        return mock.create_autospec(_Connection)

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery_storage_v1.writer import AppendRowsStream

        return AppendRowsStream

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        from google.cloud.bigquery_storage_v1.writer import (
            _Connection,
            _process_request_template,
        )

        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)

        assert stream._client is mock_client
        assert stream._initial_request_template == _process_request_template(
            REQUEST_TEMPLATE
        )
        assert stream._closed is False
        assert not stream._close_callbacks
        assert stream._metadata == ()
        assert stream._stream_name == ""
        assert isinstance(stream._thread_lock, type(threading.RLock()))

        assert isinstance(stream._connection, _Connection)
        assert stream._connection._client is mock_client
        assert stream._connection._writer is stream
        assert stream._connection._metadata == ()

    @mock.patch("google.cloud.bigquery_storage_v1.writer._Connection", autospec=True)
    def test_is_active(self, connection):
        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)

        type(connection.return_value).is_active = mock.PropertyMock(return_value=False)
        assert stream.is_active is False

        type(connection.return_value).is_active = mock.PropertyMock(return_value=True)
        assert stream.is_active is True

    def test_add_close_callback(self):
        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)

        assert not stream._close_callbacks

        callbacks = [lambda x: x + i for i in range(3)]
        for item in callbacks:
            stream.add_close_callback(item)

        assert stream._close_callbacks == callbacks

    @mock.patch("google.cloud.bigquery_storage_v1.writer._Connection", autospec=True)
    def test_send(self, connection):
        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)

        request = gapic_types.AppendRowsRequest(
            write_stream="this-is-a-stream-resource-path"
        )
        stream.send(request)

        assert stream._stream_name == "this-is-a-stream-resource-path"
        stream._connection.send.assert_called_once_with(request)

        # Send another request with the same stream name should succeed.
        stream.send(request)

    @mock.patch("google.cloud.bigquery_storage_v1.writer._Connection", autospec=True)
    def test_send_different_name(self, connection):
        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)

        request_1 = gapic_types.AppendRowsRequest(
            write_stream="this-is-a-stream-resource-path"
        )
        stream.send(request_1)

        request_2 = gapic_types.AppendRowsRequest(write_stream="different-stream-name")
        with pytest.raises(ValueError, match="Stream name is already set"):
            stream.send(request_2)

    @mock.patch("google.cloud.bigquery_storage_v1.writer._Connection", autospec=True)
    def test_close(self, connection):
        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)
        stream._close_callbacks = [mock.Mock() for _ in range(3)]
        mock_lock = mock.create_autospec(threading.RLock)()
        stream._thread_lock = mock_lock
        reason = Exception("test exception")

        assert stream._closed is False

        stream.close(reason=reason)

        assert stream._closed is True
        stream._connection.close.assert_called_once_with(reason=reason)
        for callback in stream._close_callbacks:
            callback.assert_called_once_with(stream, reason)

        # Verify that the lock was activated and closed.
        mock_lock.__enter__.assert_called_once()
        mock_lock.__exit__.assert_called_once()

    def test__renew_connection(self):
        from google.cloud.bigquery_storage_v1.writer import _Connection

        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)
        mock_lock = mock.create_autospec(threading.RLock)()
        stream._thread_lock = mock_lock
        reason = Exception("test exception")
        old_connection = stream._connection = self._make_mock_connection()

        stream._renew_connection(reason=reason)

        assert stream._connection is not old_connection
        assert isinstance(stream._connection, _Connection)
        old_connection._shutdown.assert_called_once_with(reason=reason)

        # Verify that the lock was activated and closed.
        mock_lock.__enter__.assert_called_once()
        mock_lock.__exit__.assert_called_once()

    @mock.patch("threading.Thread", autospec=True)
    def test__on_rpc_done(self, thread):
        from google.cloud.bigquery_storage_v1.writer import _RPC_ERROR_THREAD_NAME

        mock_client = self._make_mock_client()
        stream = self._make_one(mock_client, REQUEST_TEMPLATE)
        reason = Exception("test exception")

        stream._on_rpc_done(reason=reason)

        # Verify class instantiation.
        thread.assert_called_once_with(
            name=_RPC_ERROR_THREAD_NAME,
            target=stream._renew_connection,
            kwargs={"reason": reason},
        )

        # Verify that class method and attribute are accessed.
        thread().start.assert_called_once()
        assert thread().daemon is True


class Test_Connection(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery_storage_v1.writer import _Connection

        return _Connection

    @staticmethod
    def _make_mock_client():
        return mock.create_autospec(big_query_write.BigQueryWriteClient)

    @staticmethod
    def _make_mock_stream(initial_template=REQUEST_TEMPLATE):
        from google.cloud.bigquery_storage_v1.writer import _process_request_template

        writer = mock.Mock()
        template = mock.PropertyMock(
            return_value=_process_request_template(initial_template)
        )
        type(writer)._initial_request_template = template
        return writer

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)

        assert connection._client is mock_client
        assert connection._writer is mock_stream

        assert connection._metadata == ()

        assert isinstance(connection._thread_lock, type(threading.RLock()))
        assert connection._rpc is None
        assert connection._consumer is None
        assert connection._stream_name == ""
        assert isinstance(connection._queue, queue.Queue)

        assert connection._closed is False

    def test_is_active(self):
        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)

        assert connection.is_active is False

        with mock.patch("google.api_core.bidi.BackgroundConsumer") as MockConsumer:
            MockConsumer.return_value.is_active = True
            connection._consumer = MockConsumer()
            assert connection.is_active is True

    @mock.patch("google.api_core.bidi.BidiRpc", autospec=True)
    @mock.patch("google.api_core.bidi.BackgroundConsumer", autospec=True)
    def test_initial_send(self, background_consumer, bidi_rpc):
        from google.cloud.bigquery_storage_v1.writer import AppendRowsFuture

        initial_request_template = gapic_types.AppendRowsRequest(
            write_stream="stream-name-from-REQUEST_TEMPLATE",
            offset=0,
            proto_rows=gapic_types.AppendRowsRequest.ProtoData(
                writer_schema=gapic_types.ProtoSchema(
                    proto_descriptor=descriptor_pb2.DescriptorProto()
                )
            ),
        )
        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream(initial_template=initial_request_template)
        connection = self._make_one(mock_client, mock_stream)

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

        future = connection.send(initial_request)

        assert isinstance(future, AppendRowsFuture)
        background_consumer.assert_called_once_with(
            connection._rpc, connection._on_response
        )
        background_consumer.return_value.start.assert_called_once()
        assert connection._consumer == background_consumer.return_value

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
            trace_id=f"python-writer:{package_version.__version__}",
        )
        bidi_rpc.assert_called_once_with(
            start_rpc=mock_client.append_rows,
            initial_request=expected_request,
            # Extra header is required to route requests to the correct location.
            metadata=(
                (
                    "x-goog-request-params",
                    "write_stream=this-is-a-stream-resource-path",
                ),
            ),
        )

        bidi_rpc.return_value.add_done_callback.assert_called_once_with(
            connection._on_rpc_done
        )
        assert connection._rpc == bidi_rpc.return_value

        connection._consumer.is_active = True
        assert connection.is_active is True

    @mock.patch("google.api_core.bidi.BidiRpc", autospec=True)
    @mock.patch("google.api_core.bidi.BackgroundConsumer", autospec=True)
    def test_initial_send_with_timeout(self, background_consumer, bidi_rpc):
        from google.cloud.bigquery_storage_v1 import writer

        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)

        type(bidi_rpc.return_value).is_active = mock.PropertyMock(return_value=False)
        type(background_consumer.return_value).is_active = mock.PropertyMock(
            return_value=False
        )
        initial_request = gapic_types.AppendRowsRequest(
            write_stream="this-is-a-stream-resource-path"
        )
        now = time.monotonic()
        later = now + writer._DEFAULT_TIMEOUT + 1
        with (
            mock.patch.object(writer.time, "sleep"),
            mock.patch.object(
                writer.time, "monotonic", mock.MagicMock(side_effect=(now, later))
            ),
            pytest.raises(exceptions.Unknown),
        ):
            connection.send(initial_request)

    @mock.patch("google.api_core.bidi.BidiRpc", autospec=True)
    @mock.patch("google.api_core.bidi.BackgroundConsumer", autospec=True)
    def test_send(self, background_consumer, bidi_rpc):
        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)

        connection._consumer = background_consumer
        connection._rpc = bidi_rpc

        type(background_consumer.return_value).is_active = mock.PropertyMock(
            return_value=True
        )
        request = gapic_types.AppendRowsRequest(
            write_stream="this-is-a-stream-resource-path"
        )
        connection.send(request)

        bidi_rpc.send.assert_called_once_with(request)
        assert connection._queue.qsize() == 1

    @mock.patch("google.api_core.bidi.BidiRpc", autospec=True)
    @mock.patch("google.api_core.bidi.BackgroundConsumer", autospec=True)
    def test_close(self, background_consumer, bidi_rpc):
        from google.cloud.bigquery_storage_v1 import writer

        type(background_consumer.return_value).is_active = mock.PropertyMock(
            return_value=True
        )
        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)

        connection._consumer = background_consumer
        connection._rpc = bidi_rpc

        futures = [writer.AppendRowsFuture(connection._writer) for _ in range(3)]
        for f in futures:
            connection._queue.put(f)
        close_exception = Exception("test exception")

        assert connection._closed is False

        with self.assertLogs(writer._LOGGER, level="DEBUG") as cm:
            connection.close(reason=close_exception)
        assert "Stopping consumer." in str(cm.output)
        assert "Finished stopping manager." in str(cm.output)

        assert connection._closed is True
        assert connection._queue.empty() is True
        assert connection._consumer is None
        bidi_rpc.close.assert_called_once()
        background_consumer.stop.assert_called_once()
        for f in futures:
            assert f.done() is True
            with pytest.raises(Exception, match="test exception"):
                f.result()

    def test__on_response_closed(self):
        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)

        response = gapic_types.AppendRowsResponse()

        connection._closed = True
        with pytest.raises(
            bqstorage_exceptions.StreamClosedError, match="Stream closed"
        ):
            connection._on_response(response)

    def test__on_response_exception(self):
        from google.cloud.bigquery_storage_v1.writer import AppendRowsFuture

        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)
        connection._queue = mock.Mock()
        future = AppendRowsFuture(mock_stream)
        connection._queue.get_nowait.return_value = future
        response = gapic_types.AppendRowsResponse(
            {
                "error": {
                    "code": 404,
                    "message": "test error",
                }
            }
        )

        connection._on_response(response)

        assert future._is_done is True
        with pytest.raises(Exception, match="test error"):
            future.result()

    def test__on_response_result(self):
        from google.cloud.bigquery_storage_v1.writer import AppendRowsFuture

        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)
        connection._queue = mock.Mock()
        future = AppendRowsFuture(mock_stream)
        connection._queue.get_nowait.return_value = future
        response = gapic_types.AppendRowsResponse()

        connection._on_response(response)

        assert future._is_done is True
        future.result()

    def test__on_rpc_done(self):
        from google.cloud.bigquery_storage_v1.writer import AppendRowsFuture

        mock_client = self._make_mock_client()
        mock_stream = self._make_mock_stream()
        connection = self._make_one(mock_client, mock_stream)
        future = AppendRowsFuture(mock_stream)

        connection._on_rpc_done(future)

        mock_stream._on_rpc_done.assert_called_once()
        _, _, call_args = mock_stream._on_rpc_done.mock_calls[0]
        reason = call_args["reason"]
        assert isinstance(reason, Exception)
        assert reason.args[0] is future

    def test__process_request_template(self):
        from google.cloud.bigquery_storage_v1.writer import _process_request_template

        request = gapic_types.AppendRowsRequest(
            write_stream="this-is-a-stream-resource-path"
        )

        new_request = _process_request_template(request)

        # Verify this is deep copy
        assert new_request is not request

        # Verify that proto3-only fields are deleted
        proto_descriptor = new_request.proto_rows.writer_schema.proto_descriptor
        assert len(proto_descriptor.field) == 0
        assert len(proto_descriptor.oneof_decl) == 0


class TestAppendRowsFuture(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery_storage_v1.writer import AppendRowsFuture

        return AppendRowsFuture

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_future_done_false(self):
        from google.cloud.bigquery_storage_v1.writer import AppendRowsStream

        mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
        manager = AppendRowsStream(mock_client, REQUEST_TEMPLATE)
        future = self._make_one(manager)
        assert not future.done()

    def test_future_done_true_with_result(self):
        from google.cloud.bigquery_storage_v1.writer import AppendRowsStream

        mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
        manager = AppendRowsStream(mock_client, REQUEST_TEMPLATE)
        future = self._make_one(manager)
        future.set_result(object())
        assert future.done()

    def test_future_done_true_with_exception(self):
        from google.cloud.bigquery_storage_v1.writer import AppendRowsStream

        mock_client = mock.create_autospec(big_query_write.BigQueryWriteClient)
        manager = AppendRowsStream(mock_client, REQUEST_TEMPLATE)
        future = self._make_one(manager)
        future.set_exception(ValueError())
        assert future.done()
