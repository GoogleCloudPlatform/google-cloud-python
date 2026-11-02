# Copyright 2016 Google LLC
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

import unittest
from datetime import datetime

import google.auth.credentials
import mock

import google.cloud.logging
from google.cloud import logging_v2
from google.cloud.logging_v2 import _gapic
from google.cloud.logging_v2.services.config_service_v2 import ConfigServiceV2Client
from google.cloud.logging_v2.services.logging_service_v2 import LoggingServiceV2Client
from google.cloud.logging_v2.services.metrics_service_v2 import MetricsServiceV2Client
from google.cloud.logging_v2.types import LogEntry as LogEntryPB
from google.cloud.logging_v2.types import LogSink

PROJECT = "PROJECT"
PROJECT_PATH = f"projects/{PROJECT}"
FILTER = "logName:syslog AND severity>=ERROR"


class Test_LoggingAPI(unittest.TestCase):
    LOG_NAME = "log_name"
    LOG_PATH = f"projects/{PROJECT}/logs/{LOG_NAME}"

    @staticmethod
    def make_logging_api():
        # Create a dummy credentials object to help ensure unit test isolation
        creds = mock.Mock(spec=google.auth.credentials.Credentials)

        # Pass those credentials to the GAPIC client
        gapic_client = LoggingServiceV2Client(credentials=creds)
        handwritten_client = mock.Mock()
        api = _gapic._LoggingAPI(gapic_client, handwritten_client)
        return api

    def test_ctor(self):
        # Create a dummy credentials object to help ensure unit test isolation
        creds = mock.Mock(spec=google.auth.credentials.Credentials)

        # Pass those credentials to the GAPIC client
        gapic_client = LoggingServiceV2Client(credentials=creds)
        api = _gapic._LoggingAPI(gapic_client, mock.sentinel.client)
        assert api._gapic_api is gapic_client
        assert api._client is mock.sentinel.client

    def test_list_entries(self):
        client = self.make_logging_api()

        log_entry_msg = LogEntryPB(log_name=self.LOG_PATH, text_payload="text")

        with mock.patch.object(
            type(client._gapic_api.transport.list_log_entries), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListLogEntriesResponse(
                entries=[log_entry_msg]
            )
            result = client.list_entries(
                [PROJECT_PATH], filter_=FILTER, order_by=logging_v2.DESCENDING
            )

        entries = list(result)

        # Check the response
        assert len(entries) == 1
        entry = entries[0]

        assert isinstance(entry, logging_v2.entries.TextEntry)
        assert entry.payload == "text"

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.resource_names == [PROJECT_PATH]
        assert request.filter == FILTER
        assert request.order_by == logging_v2.DESCENDING

    def test_list_entries_with_options(self):
        client = self.make_logging_api()

        with mock.patch.object(
            type(client._gapic_api.transport.list_log_entries), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListLogEntriesResponse(entries=[])

            result = client.list_entries(
                [PROJECT_PATH],
                filter_=FILTER,
                order_by=google.cloud.logging.ASCENDING,
                page_size=42,
                page_token="token",
            )

        list(result)

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.resource_names == [PROJECT_PATH]
        assert request.filter == FILTER
        assert request.order_by == google.cloud.logging.ASCENDING
        assert request.page_size == 42
        assert request.page_token == "token"

    def test_list_logs_with_max_results(self):
        client = self.make_logging_api()
        log_entry_msg = LogEntryPB(log_name=self.LOG_PATH, text_payload="text")

        with mock.patch.object(
            type(client._gapic_api.transport.list_log_entries), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListLogEntriesResponse(
                entries=[log_entry_msg, log_entry_msg]
            )
            result = client.list_entries(
                [PROJECT_PATH],
                filter_=FILTER,
                order_by=google.cloud.logging.ASCENDING,
                page_size=42,
                page_token="token",
                max_results=1,
            )

        # Check the request
        call.assert_called_once()
        assert len(list(result)) == 1

    def test_list_logs_negative_max_results(self):
        client = self.make_logging_api()

        with self.assertRaises(ValueError):
            with mock.patch.object(
                type(client._gapic_api.transport.list_log_entries), "__call__"
            ) as call:
                call.return_value = logging_v2.types.ListLogEntriesResponse(entries=[])
                result = client.list_entries(
                    [PROJECT_PATH],
                    filter_=FILTER,
                    order_by=google.cloud.logging.ASCENDING,
                    page_size=42,
                    page_token="token",
                    max_results=-1,
                )
            # Check the request
            list(result)
            call.assert_called_once()

    def test_write_entries_single(self):
        client = self.make_logging_api()

        with mock.patch.object(
            type(client._gapic_api.transport.write_log_entries), "__call__"
        ) as call:
            call.return_value = logging_v2.types.WriteLogEntriesResponse()
            entry = {
                "logName": self.LOG_PATH,
                "resource": {"type": "global"},
                "textPayload": "text",
            }
            client.write_entries([entry])

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.partial_success is True
        assert len(request.entries) == 1
        assert request.entries[0].log_name == entry["logName"]
        assert request.entries[0].resource.type == entry["resource"]["type"]
        assert request.entries[0].text_payload == "text"

    def test_write_entries_parse_error(self):
        client = self.make_logging_api()
        with self.assertRaises(ValueError):
            with mock.patch.object(
                type(client._gapic_api.transport.write_log_entries), "__call__"
            ) as call:
                entry = {
                    "logName": self.LOG_PATH,
                    "resource": {"type": "global"},
                    "jsonPayload": {"time": datetime.now()},
                }
                client.write_entries([entry])

        call.assert_not_called()

    def test_logger_delete(self):
        client = self.make_logging_api()

        with mock.patch.object(
            type(client._gapic_api.transport.delete_log), "__call__"
        ) as call:
            client.logger_delete(self.LOG_PATH)
        call.assert_called_once()
        assert call.call_args.args[0].log_name == self.LOG_PATH


class Test_SinksAPI(unittest.TestCase):
    SINK_NAME = "sink_name"
    PARENT_PATH = f"projects/{PROJECT}"
    SINK_PATH = f"projects/{PROJECT}/sinks/{SINK_NAME}"
    DESTINATION_URI = "faux.googleapis.com/destination"
    SINK_WRITER_IDENTITY = "serviceAccount:project-123@example.com"

    @staticmethod
    def make_sinks_api():
        # Create a dummy credentials object to help ensure unit test isolation
        creds = mock.Mock(spec=google.auth.credentials.Credentials)

        # Pass those credentials to the GAPIC client
        gapic_client = ConfigServiceV2Client(credentials=creds)
        handwritten_client = mock.Mock()
        api = _gapic._SinksAPI(gapic_client, handwritten_client)
        return api

    def test_ctor(self):
        # Create a dummy credentials object to help ensure unit test isolation
        creds = mock.Mock(spec=google.auth.credentials.Credentials)

        # Pass those credentials to the GAPIC client
        gapic_client = ConfigServiceV2Client(credentials=creds)
        api = _gapic._SinksAPI(gapic_client, mock.sentinel.client)
        assert api._gapic_api is gapic_client
        assert api._client is mock.sentinel.client

    def test_list_sinks(self):
        client = self.make_sinks_api()

        sink_msg = LogSink(
            name=self.SINK_NAME, destination=self.DESTINATION_URI, filter=FILTER
        )
        with mock.patch.object(
            type(client._gapic_api.transport.list_sinks), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListSinksResponse(sinks=[sink_msg])

            result = client.list_sinks(
                self.PARENT_PATH,
            )

        sinks = list(result)

        # Check the response
        assert len(sinks) == 1
        sink = sinks[0]
        assert isinstance(sink, google.cloud.logging.Sink)
        assert sink.name == self.SINK_NAME
        assert sink.destination == self.DESTINATION_URI
        assert sink.filter_ == FILTER

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.parent == self.PARENT_PATH

    def test_list_sinks_with_options(self):
        client = self.make_sinks_api()

        with mock.patch.object(
            type(client._gapic_api.transport.list_sinks), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListSinksResponse(sinks=[])
            result = client.list_sinks(
                self.PARENT_PATH, page_size=42, page_token="token"
            )
        list(result)

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.parent == self.PARENT_PATH
        assert request.page_size == 42
        assert request.page_token == "token"

    def test_list_sinks_with_max_results(self):
        client = self.make_sinks_api()
        sink_msg = LogSink(
            name=self.SINK_NAME, destination=self.DESTINATION_URI, filter=FILTER
        )

        with mock.patch.object(
            type(client._gapic_api.transport.list_sinks), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListSinksResponse(
                sinks=[sink_msg, sink_msg]
            )
            result = client.list_sinks(
                self.PARENT_PATH, page_size=42, page_token="token", max_results=1
            )
        # Check the request
        call.assert_called_once()
        assert len(list(result)) == 1

    def test_list_sinks_negative_max_results(self):
        client = self.make_sinks_api()

        with self.assertRaises(ValueError):
            with mock.patch.object(
                type(client._gapic_api.transport.list_sinks), "__call__"
            ) as call:
                call.return_value = logging_v2.types.ListSinksResponse(sinks=[])
                result = client.list_sinks(
                    self.PARENT_PATH, page_size=42, page_token="token", max_results=-1
                )
            # Check the request
            list(result)
            call.assert_called_once()

    def test_sink_create(self):
        client = self.make_sinks_api()
        with mock.patch.object(
            type(client._gapic_api.transport.create_sink), "__call__"
        ) as call:
            call.return_value = logging_v2.types.LogSink(
                name=self.SINK_NAME,
                destination=self.DESTINATION_URI,
                filter=FILTER,
                writer_identity=self.SINK_WRITER_IDENTITY,
            )

            result = client.sink_create(
                self.PARENT_PATH,
                self.SINK_NAME,
                FILTER,
                self.DESTINATION_URI,
                unique_writer_identity=True,
            )

        # Check response
        # TODO: response has extra fields (blank fields) is this OK?
        assert result["name"] == self.SINK_NAME
        assert result["filter"] == FILTER
        assert result["destination"] == self.DESTINATION_URI
        assert result["writerIdentity"] == self.SINK_WRITER_IDENTITY

        # Check request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.parent == self.PARENT_PATH
        assert request.unique_writer_identity is True
        assert request.sink.name == self.SINK_NAME
        assert request.sink.filter == FILTER
        assert request.sink.destination == self.DESTINATION_URI

    def test_sink_get(self):
        client = self.make_sinks_api()
        with mock.patch.object(
            type(client._gapic_api.transport.get_sink), "__call__"
        ) as call:
            call.return_value = logging_v2.types.LogSink(
                name=self.SINK_NAME, destination=self.DESTINATION_URI, filter=FILTER
            )

            response = client.sink_get(self.SINK_PATH)

        # Check response
        assert response == {
            "name": self.SINK_NAME,
            "filter": FILTER,
            "destination": self.DESTINATION_URI,
        }

        # Check request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.sink_name == self.SINK_PATH

    def test_sink_update(self):
        client = self.make_sinks_api()
        with mock.patch.object(
            type(client._gapic_api.transport.update_sink), "__call__"
        ) as call:
            call.return_value = logging_v2.types.LogSink(
                name=self.SINK_NAME,
                destination=self.DESTINATION_URI,
                filter=FILTER,
                writer_identity=self.SINK_WRITER_IDENTITY,
            )

            result = client.sink_update(
                self.SINK_PATH,
                FILTER,
                self.DESTINATION_URI,
                unique_writer_identity=True,
            )

        # Check response
        assert result == {
            "name": self.SINK_NAME,
            "filter": FILTER,
            "destination": self.DESTINATION_URI,
            "writerIdentity": self.SINK_WRITER_IDENTITY,
        }

        # Check request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.sink_name == self.SINK_PATH
        assert request.unique_writer_identity is True
        assert request.sink.name == self.SINK_NAME
        assert request.sink.filter == FILTER
        assert request.sink.destination == self.DESTINATION_URI

    def test_sink_delete(self):
        client = self.make_sinks_api()
        with mock.patch.object(
            type(client._gapic_api.transport.get_sink), "__call__"
        ) as call:
            client.sink_delete(self.SINK_PATH)

        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.sink_name == self.SINK_PATH


class Test_MetricsAPI(unittest.TestCase):
    METRIC_NAME = "metric_name"
    METRIC_PATH = f"projects/{PROJECT}/metrics/{METRIC_NAME}"
    DESCRIPTION = "Description"

    @staticmethod
    def make_metrics_api():
        # Create a dummy credentials object to help ensure unit test isolation
        creds = mock.Mock(spec=google.auth.credentials.Credentials)

        # Pass those credentials to the GAPIC client
        gapic_client = MetricsServiceV2Client(credentials=creds)
        handwritten_client = mock.Mock()
        api = _gapic._MetricsAPI(gapic_client, handwritten_client)
        return api

    def test_ctor(self):
        # Create a dummy credentials object to help ensure unit test isolation
        creds = mock.Mock(spec=google.auth.credentials.Credentials)

        # Pass those credentials to the GAPIC client
        gapic_client = MetricsServiceV2Client(credentials=creds)
        api = _gapic._MetricsAPI(gapic_client, mock.sentinel.client)
        assert api._gapic_api is gapic_client
        assert api._client is mock.sentinel.client

    def test_list_metrics(self):
        client = self.make_metrics_api()

        metric = logging_v2.types.LogMetric(
            name=self.METRIC_PATH, description=self.DESCRIPTION, filter=FILTER
        )
        with mock.patch.object(
            type(client._gapic_api.transport.list_log_metrics), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListLogMetricsResponse(
                metrics=[metric]
            )
            result = client.list_metrics(PROJECT)
        metrics = list(result)

        # Check the response
        assert len(metrics) == 1
        metric = metrics[0]
        assert isinstance(metric, google.cloud.logging.Metric)
        assert metric.name == self.METRIC_PATH
        assert metric.description == self.DESCRIPTION
        assert metric.filter_ == FILTER

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.parent == PROJECT_PATH

    def test_list_metrics_options(self):
        client = self.make_metrics_api()

        with mock.patch.object(
            type(client._gapic_api.transport.list_log_metrics), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListLogMetricsResponse(metrics=[])

            result = client.list_metrics(PROJECT, page_size=42, page_token="token")
        list(result)

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.parent == PROJECT_PATH
        assert request.page_size == 42
        assert request.page_token == "token"

    def test_list_metrics_with_max_results(self):
        client = self.make_metrics_api()
        metric = logging_v2.types.LogMetric(
            name=self.METRIC_PATH, description=self.DESCRIPTION, filter=FILTER
        )
        with mock.patch.object(
            type(client._gapic_api.transport.list_log_metrics), "__call__"
        ) as call:
            call.return_value = logging_v2.types.ListLogMetricsResponse(
                metrics=[metric, metric]
            )
            result = client.list_metrics(
                PROJECT, page_size=42, page_token="token", max_results=1
            )
        # Check the request
        call.assert_called_once()
        assert len(list(result)) == 1

    def test_list_metrics_negative_max_results(self):
        client = self.make_metrics_api()

        with self.assertRaises(ValueError):
            with mock.patch.object(
                type(client._gapic_api.transport.list_log_metrics), "__call__"
            ) as call:
                call.return_value = logging_v2.types.ListLogMetricsResponse(metrics=[])
                result = client.list_metrics(
                    PROJECT, page_size=42, page_token="token", max_results=-1
                )
            # Check the request
            list(result)
            call.assert_called_once()

    def test_metric_create(self):
        client = self.make_metrics_api()

        with mock.patch.object(
            type(client._gapic_api.transport.create_log_metric), "__call__"
        ) as call:
            client.metric_create(PROJECT, self.METRIC_NAME, FILTER, self.DESCRIPTION)

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.parent == PROJECT_PATH
        assert request.metric.name == self.METRIC_NAME
        assert request.metric.filter == FILTER
        assert request.metric.description == self.DESCRIPTION

    def test_metric_get(self):
        client = self.make_metrics_api()

        with mock.patch.object(
            type(client._gapic_api.transport.get_log_metric), "__call__"
        ) as call:
            call.return_value = logging_v2.types.LogMetric(
                name=self.METRIC_PATH, description=self.DESCRIPTION, filter=FILTER
            )
            response = client.metric_get(PROJECT, self.METRIC_NAME)

        # Check the response
        assert response == {
            "name": self.METRIC_PATH,
            "filter": FILTER,
            "description": self.DESCRIPTION,
        }

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.metric_name == self.METRIC_PATH

    def test_metric_update(self):
        client = self.make_metrics_api()

        with mock.patch.object(
            type(client._gapic_api.transport.update_log_metric), "__call__"
        ) as call:
            call.return_value = logging_v2.types.LogMetric(
                name=self.METRIC_PATH, description=self.DESCRIPTION, filter=FILTER
            )

            response = client.metric_update(
                PROJECT, self.METRIC_NAME, FILTER, self.DESCRIPTION
            )

        # Check the response
        assert response == {
            "name": self.METRIC_PATH,
            "filter": FILTER,
            "description": self.DESCRIPTION,
        }

        # Check the request
        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.metric_name == self.METRIC_PATH
        assert request.metric.name == self.METRIC_PATH
        assert request.metric.filter == FILTER
        assert request.metric.description == self.DESCRIPTION

    def test_metric_delete(self):
        client = self.make_metrics_api()
        with mock.patch.object(
            type(client._gapic_api.transport.delete_log_metric), "__call__"
        ) as call:
            client.metric_delete(PROJECT, self.METRIC_NAME)

        call.assert_called_once()
        request = call.call_args.args[0]
        assert request.metric_name == self.METRIC_PATH


class Test__parse_log_entry(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.logging_v2._gapic import _parse_log_entry

        return _parse_log_entry(*args, **kwargs)

    def test_simple(self):
        entry_pb = LogEntryPB(log_name="lol-jk", text_payload="bah humbug")
        result = self._call_fut(LogEntryPB.pb(entry_pb))
        expected = {"logName": entry_pb.log_name, "textPayload": entry_pb.text_payload}
        self.assertEqual(result, expected)

    @mock.patch("google.cloud.logging_v2._gapic.MessageToDict", side_effect=TypeError)
    def test_non_registry_failure(self, msg_to_dict_mock):
        entry_pb = mock.Mock(spec=["HasField"])
        entry_pb.HasField.return_value = False
        with self.assertRaises(TypeError):
            self._call_fut(entry_pb)

        entry_pb.HasField.assert_called_once_with("proto_payload")
        msg_to_dict_mock.assert_called_once_with(
            entry_pb,
            preserving_proto_field_name=False,
        )

    def test_unregistered_type(self):
        from google.protobuf import any_pb2, descriptor_pool
        from google.protobuf.timestamp_pb2 import Timestamp

        pool = descriptor_pool.Default()
        type_name = "google.bigtable.admin.v2.UpdateClusterMetadata"
        # Make sure the descriptor is not known in the registry.
        with self.assertRaises(KeyError):
            pool.FindMessageTypeByName(type_name)

        type_url = "type.googleapis.com/" + type_name
        metadata_bytes = b"\n\n\n\x03foo\x12\x03bar\x12\x06\x08\xbd\xb6\xfb\xc6\x05"
        any_pb = any_pb2.Any(type_url=type_url, value=metadata_bytes)
        timestamp = Timestamp(seconds=61, nanos=1234000)

        entry_pb = LogEntryPB(proto_payload=any_pb, timestamp=timestamp)
        result = self._call_fut(LogEntryPB.pb(entry_pb))
        self.assertEqual(len(result), 2)
        self.assertEqual(result["timestamp"], "1970-01-01T00:01:01.001234Z")
        # NOTE: This "hack" is needed on Windows, where the equality check
        #       for an ``Any`` instance fails on unregistered types.
        self.assertEqual(result["protoPayload"].type_url, type_url)
        self.assertEqual(result["protoPayload"].value, metadata_bytes)

    def test_registered_type(self):
        from google.protobuf import any_pb2, descriptor_pool
        from google.protobuf.struct_pb2 import Struct, Value

        pool = descriptor_pool.Default()
        type_name = "google.protobuf.Struct"
        # Make sure the descriptor is known in the registry.
        descriptor = pool.FindMessageTypeByName(type_name)
        self.assertEqual(descriptor.name, "Struct")

        type_url = "type.googleapis.com/" + type_name
        field_name = "foo"
        field_value = "Bar"
        struct_pb = Struct(fields={field_name: Value(string_value=field_value)})
        any_pb = any_pb2.Any(type_url=type_url, value=struct_pb.SerializeToString())

        entry_pb = LogEntryPB(proto_payload=any_pb, log_name="all-good")
        result = self._call_fut(LogEntryPB.pb(entry_pb))
        expected_proto = {
            "logName": entry_pb.log_name,
            "protoPayload": {"@type": type_url, "value": {field_name: field_value}},
        }
        self.assertEqual(result, expected_proto)


class Test__log_entry_mapping_to_pb(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.logging_v2._gapic import _log_entry_mapping_to_pb

        return _log_entry_mapping_to_pb(*args, **kwargs)

    def test_simple(self):
        result = self._call_fut({})
        self.assertEqual(result, LogEntryPB())

    def test_unregistered_type(self):
        from google.protobuf import descriptor_pool
        from google.protobuf.json_format import ParseError

        pool = descriptor_pool.Default()
        type_name = "google.bigtable.admin.v2.UpdateClusterMetadata"
        # Make sure the descriptor is not known in the registry.
        with self.assertRaises(KeyError):
            pool.FindMessageTypeByName(type_name)

        type_url = "type.googleapis.com/" + type_name
        json_mapping = {
            "protoPayload": {
                "@type": type_url,
                "originalRequest": {"name": "foo", "location": "bar"},
                "requestTime": {"seconds": 1491000125},
            }
        }
        with self.assertRaises(ParseError):
            self._call_fut(json_mapping)

    def test_registered_type(self):
        from google.protobuf import any_pb2, descriptor_pool

        pool = descriptor_pool.Default()
        type_name = "google.protobuf.Struct"
        # Make sure the descriptor is known in the registry.
        descriptor = pool.FindMessageTypeByName(type_name)
        self.assertEqual(descriptor.name, "Struct")

        type_url = "type.googleapis.com/" + type_name
        field_name = "foo"
        field_value = "Bar"
        json_mapping = {
            "logName": "hi-everybody",
            "protoPayload": {"@type": type_url, "value": {field_name: field_value}},
        }
        # Convert to a valid LogEntry.
        result = self._call_fut(json_mapping)
        entry_pb = LogEntryPB(
            log_name=json_mapping["logName"],
            proto_payload=any_pb2.Any(
                type_url=type_url, value=b"\n\014\n\003foo\022\005\032\003Bar"
            ),
        )
        self.assertEqual(result, entry_pb)


@mock.patch("google.cloud.logging_v2._gapic.LoggingServiceV2Client", autospec=True)
def test_make_logging_api(gapic_client):
    client = mock.Mock(spec=["_credentials", "_client_info", "_client_options"])
    api = _gapic.make_logging_api(client)
    assert api._client == client
    assert api._gapic_api == gapic_client.return_value
    gapic_client.assert_called_once_with(
        credentials=client._credentials,
        client_info=client._client_info,
        client_options=client._client_options,
    )


@mock.patch("google.cloud.logging_v2._gapic.MetricsServiceV2Client", autospec=True)
def test_make_metrics_api(gapic_client):
    client = mock.Mock(spec=["_credentials", "_client_info", "_client_options"])
    api = _gapic.make_metrics_api(client)
    assert api._client == client
    assert api._gapic_api == gapic_client.return_value
    gapic_client.assert_called_once_with(
        credentials=client._credentials,
        client_info=client._client_info,
        client_options=client._client_options,
    )


@mock.patch("google.cloud.logging_v2._gapic.ConfigServiceV2Client", autospec=True)
def test_make_sinks_api(gapic_client):
    client = mock.Mock(spec=["_credentials", "_client_info", "_client_options"])
    api = _gapic.make_sinks_api(client)
    assert api._client == client
    assert api._gapic_api == gapic_client.return_value
    gapic_client.assert_called_once_with(
        credentials=client._credentials,
        client_info=client._client_info,
        client_options=client._client_options,
    )
