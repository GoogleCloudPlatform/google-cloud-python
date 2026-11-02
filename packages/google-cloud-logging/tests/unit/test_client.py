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

import re
import unittest
from copy import deepcopy
from datetime import datetime, timedelta, timezone

import mock

VENEER_HEADER_REGEX = re.compile(
    r"gapic\/[0-9]+\.[\w.-]+ gax\/[0-9]+\.[\w.-]+ gccl\/[0-9]+\.[\w.-]+ gl-python\/[0-9]+\.[\w.-]+ grpc\/[0-9]+\.[\w.-]+"
)


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class TestClient(unittest.TestCase):
    PROJECT = "PROJECT"
    PROJECT_PATH = f"projects/{PROJECT}"
    LOGGER_NAME = "LOGGER_NAME"
    SINK_NAME = "SINK_NAME"
    FILTER = "logName:syslog AND severity>=ERROR"
    DESTINATION_URI = "faux.googleapis.com/destination"
    METRIC_NAME = "metric_name"
    FILTER = "logName:syslog AND severity>=ERROR"
    DESCRIPTION = "DESCRIPTION"
    TIME_FORMAT = '"%Y-%m-%dT%H:%M:%S.%f%z"'

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        from google.cloud._http import ClientInfo

        from google.cloud.logging_v2._http import Connection

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        self.assertEqual(client.project, self.PROJECT)
        self.assertIsInstance(client._connection, Connection)
        self.assertIsInstance(client._connection._client_info, ClientInfo)

    def test_ctor_explicit(self):
        from google.cloud._http import ClientInfo

        from google.cloud.logging_v2._http import Connection

        creds = _make_credentials()
        client_info = ClientInfo()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, client_info=client_info
        )
        self.assertEqual(client.project, self.PROJECT)
        self.assertIs(client._client_info, client_info)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection._client_info, client_info)

    def test_ctor_w_empty_client_options(self):
        from google.api_core.client_options import ClientOptions

        creds = _make_credentials()
        client_options = ClientOptions()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, client_options=client_options
        )
        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )

    def test_ctor_w_client_options_object(self):
        from google.api_core.client_options import ClientOptions

        creds = _make_credentials()
        client_options = ClientOptions(
            api_endpoint="https://foo-logging.googleapis.com"
        )
        client = self._make_one(
            project=self.PROJECT, credentials=creds, client_options=client_options
        )
        self.assertEqual(
            client._connection.API_BASE_URL, "https://foo-logging.googleapis.com"
        )

    def test_ctor_w_client_options_dict(self):
        creds = _make_credentials()
        client_options = {"api_endpoint": "https://foo-logging.googleapis.com"}
        client = self._make_one(
            project=self.PROJECT, credentials=creds, client_options=client_options
        )
        self.assertEqual(
            client._connection.API_BASE_URL, "https://foo-logging.googleapis.com"
        )

    def test_logging_api_wo_gapic(self):
        from google.cloud.logging_v2._http import _LoggingAPI

        client = self._make_one(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )

        conn = client._connection = _Connection()
        api = client.logging_api

        self.assertIsInstance(api, _LoggingAPI)
        self.assertEqual(api.api_request, conn.api_request)
        # API instance is cached
        again = client.logging_api
        self.assertIs(again, api)

    def test_logging_api_w_gapic(self):
        clients = []
        api_obj = object()

        def make_api(client_obj):
            clients.append(client_obj)
            return api_obj

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds, _use_grpc=True)

        patch = mock.patch("google.cloud.logging_v2.client._gapic")
        with patch as gapic_module:
            gapic_module.make_logging_api.side_effect = make_api
            api = client.logging_api

        self.assertIs(api, api_obj)
        self.assertEqual(clients, [client])
        # API instance is cached
        again = client.logging_api
        self.assertIs(again, api)

    def test_veneer_grpc_headers(self):
        # test that client APIs have client_info populated with the expected veneer headers
        # required for proper instrumentation
        creds = _make_credentials()
        # ensure client info is set on client object
        client = self._make_one(project=self.PROJECT, credentials=creds, _use_grpc=True)
        self.assertIsNotNone(client._client_info)
        user_agent_sorted = " ".join(
            sorted(client._client_info.to_user_agent().split(" "))
        )
        self.assertTrue(VENEER_HEADER_REGEX.match(user_agent_sorted))
        # ensure client info is propagated to gapic wrapped methods
        patch = mock.patch("google.api_core.gapic_v1.method.wrap_method")
        with patch as gapic_mock:
            client.logging_api  # initialize logging api
            client.metrics_api  # initialize metrics api
            client.sinks_api  # initialize sinks api
            wrapped_call_list = gapic_mock.call_args_list
            num_api_calls = 37  # expected number of distinct APIs in all gapic services (logging,metrics,sinks)
            self.assertGreaterEqual(
                len(wrapped_call_list),
                num_api_calls,
                "unexpected number of APIs wrapped",
            )
            for call in wrapped_call_list:
                client_info = call.kwargs["client_info"]
                self.assertIsNotNone(client_info)
                wrapped_user_agent_sorted = " ".join(
                    sorted(client_info.to_user_agent().split(" "))
                )
                self.assertTrue(VENEER_HEADER_REGEX.match(wrapped_user_agent_sorted))

    def test_veneer_http_headers(self):
        # test that http APIs have client_info populated with the expected veneer headers
        # required for proper instrumentation
        creds = _make_credentials()
        # ensure client info is set on client object
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _use_grpc=False
        )
        self.assertIsNotNone(client._client_info)
        user_agent_sorted = " ".join(
            sorted(client._client_info.to_user_agent().split(" "))
        )
        self.assertTrue(VENEER_HEADER_REGEX.match(user_agent_sorted))
        # ensure client info is propagated to _connection object
        connection_user_agent = client._connection._client_info.to_user_agent()
        self.assertIsNotNone(connection_user_agent)
        connection_user_agent_sorted = " ".join(
            sorted(connection_user_agent.split(" "))
        )
        self.assertTrue(VENEER_HEADER_REGEX.match(connection_user_agent_sorted))

    def test_no_gapic_ctor(self):
        from google.cloud.logging_v2._http import _LoggingAPI

        creds = _make_credentials()
        patch = mock.patch("google.cloud.logging_v2.client._USE_GRPC", new=True)
        with patch:
            client = self._make_one(
                project=self.PROJECT, credentials=creds, _use_grpc=False
            )

        api = client.logging_api
        self.assertIsInstance(api, _LoggingAPI)

    def test_sinks_api_wo_gapic(self):
        from google.cloud.logging_v2._http import _SinksAPI

        client = self._make_one(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )

        conn = client._connection = _Connection()
        api = client.sinks_api

        self.assertIsInstance(api, _SinksAPI)
        self.assertEqual(api.api_request, conn.api_request)
        # API instance is cached
        again = client.sinks_api
        self.assertIs(again, api)

    def test_sinks_api_w_gapic(self):
        clients = []
        api_obj = object()

        def make_api(client_obj):
            clients.append(client_obj)
            return api_obj

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds, _use_grpc=True)

        patch = mock.patch("google.cloud.logging_v2.client._gapic")
        with patch as gapic_module:
            gapic_module.make_sinks_api.side_effect = make_api
            api = client.sinks_api

        self.assertIs(api, api_obj)
        self.assertEqual(clients, [client])
        # API instance is cached
        again = client.sinks_api
        self.assertIs(again, api)

    def test_metrics_api_wo_gapic(self):
        from google.cloud.logging_v2._http import _MetricsAPI

        client = self._make_one(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )

        conn = client._connection = _Connection()
        api = client.metrics_api

        self.assertIsInstance(api, _MetricsAPI)
        self.assertEqual(api.api_request, conn.api_request)
        # API instance is cached
        again = client.metrics_api
        self.assertIs(again, api)

    def test_metrics_api_w_gapic(self):
        clients = []
        api_obj = object()

        def make_api(client_obj):
            clients.append(client_obj)
            return api_obj

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds, _use_grpc=True)

        patch = mock.patch("google.cloud.logging_v2.client._gapic")
        with patch as gapic_module:
            gapic_module.make_metrics_api.side_effect = make_api
            api = client.metrics_api

        self.assertIs(api, api_obj)
        self.assertEqual(clients, [client])
        # API instance is cached
        again = client.metrics_api
        self.assertIs(again, api)

    def test_logger(self):
        from google.cloud.logging import Logger
        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        labels = {"test": "true"}
        logger = client.logger(
            self.LOGGER_NAME, resource=_GLOBAL_RESOURCE, labels=labels
        )
        self.assertIsInstance(logger, Logger)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)
        self.assertEqual(logger.default_resource, _GLOBAL_RESOURCE)
        self.assertEqual(logger.labels, labels)

    def test_list_entries_defaults(self):
        from google.cloud.logging import TextEntry

        IID = "IID"
        TEXT = "TEXT"
        ENTRIES = [
            {
                "textPayload": TEXT,
                "insertId": IID,
                "resource": {"type": "global"},
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
            }
        ]
        creds = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _use_grpc=False
        )
        returned = {"entries": ENTRIES}
        client._connection = _Connection(returned)

        iterator = client.list_entries()
        entries = list(iterator)

        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertIsInstance(entry, TextEntry)
        self.assertEqual(entry.insert_id, IID)
        self.assertEqual(entry.payload, TEXT)
        logger = entry.logger
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)

        # check call payload
        call_payload_no_filter = deepcopy(client._connection._called_with)
        call_payload_no_filter["data"]["filter"] = "removed"
        self.assertEqual(
            call_payload_no_filter,
            {
                "path": "/entries:list",
                "method": "POST",
                "data": {
                    "filter": "removed",
                    "resourceNames": [f"projects/{self.PROJECT}"],
                },
            },
        )
        # verify that default filter is 24 hours
        timestamp = datetime.strptime(
            client._connection._called_with["data"]["filter"],
            "timestamp>=" + self.TIME_FORMAT,
        )
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        self.assertLess(yesterday - timestamp, timedelta(minutes=1))

    def test_list_entries_explicit(self):
        from google.cloud.logging import DESCENDING, Logger, ProtobufEntry, StructEntry

        PROJECT1 = "PROJECT1"
        PROJECT2 = "PROJECT2"
        INPUT_FILTER = "logName:LOGNAME"
        IID1 = "IID1"
        IID2 = "IID2"
        PAYLOAD = {"message": "MESSAGE", "weather": "partly cloudy"}
        PROTO_PAYLOAD = PAYLOAD.copy()
        PROTO_PAYLOAD["@type"] = "type.googleapis.com/testing.example"
        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        ENTRIES = [
            {
                "jsonPayload": PAYLOAD,
                "insertId": IID1,
                "resource": {"type": "global"},
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
            },
            {
                "protoPayload": PROTO_PAYLOAD,
                "insertId": IID2,
                "resource": {"type": "global"},
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
            },
            {
                "protoPayload": "ignored",
                "insertId": "ignored",
                "resource": {"type": "global"},
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
            },
        ]
        client = self._make_one(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"entries": ENTRIES}
        client._connection = _Connection(returned)

        iterator = client.list_entries(
            resource_names=[f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
            filter_=INPUT_FILTER,
            order_by=DESCENDING,
            page_size=PAGE_SIZE,
            page_token=TOKEN,
            max_results=2,
        )
        entries = list(iterator)
        # Check the entries.
        self.assertEqual(len(entries), 2)
        entry = entries[0]
        self.assertIsInstance(entry, StructEntry)
        self.assertEqual(entry.insert_id, IID1)
        self.assertEqual(entry.payload, PAYLOAD)
        logger = entry.logger
        self.assertIsInstance(logger, Logger)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)

        entry = entries[1]
        self.assertIsInstance(entry, ProtobufEntry)
        self.assertEqual(entry.insert_id, IID2)
        self.assertEqual(entry.payload, PROTO_PAYLOAD)
        logger = entry.logger
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)

        self.assertIs(entries[0].logger, entries[1].logger)

        # check call payload
        call_payload_no_filter = deepcopy(client._connection._called_with)
        call_payload_no_filter["data"]["filter"] = "removed"
        self.assertEqual(
            call_payload_no_filter,
            {
                "path": "/entries:list",
                "method": "POST",
                "data": {
                    "filter": "removed",
                    "orderBy": DESCENDING,
                    "pageSize": PAGE_SIZE,
                    "pageToken": TOKEN,
                    "resourceNames": [f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
                },
            },
        )
        # verify that default timestamp filter is added
        timestamp = datetime.strptime(
            client._connection._called_with["data"]["filter"],
            INPUT_FILTER + " AND timestamp>=" + self.TIME_FORMAT,
        )
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        self.assertLess(yesterday - timestamp, timedelta(minutes=1))

    def test_list_entries_explicit_timestamp(self):
        from google.cloud.logging import DESCENDING, Logger, ProtobufEntry, StructEntry

        PROJECT1 = "PROJECT1"
        PROJECT2 = "PROJECT2"
        INPUT_FILTER = 'logName:LOGNAME AND timestamp="2020-10-13T21"'
        IID1 = "IID1"
        IID2 = "IID2"
        PAYLOAD = {"message": "MESSAGE", "weather": "partly cloudy"}
        PROTO_PAYLOAD = PAYLOAD.copy()
        PROTO_PAYLOAD["@type"] = "type.googleapis.com/testing.example"
        PAGE_SIZE = 42
        ENTRIES = [
            {
                "jsonPayload": PAYLOAD,
                "insertId": IID1,
                "resource": {"type": "global"},
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
            },
            {
                "protoPayload": PROTO_PAYLOAD,
                "insertId": IID2,
                "resource": {"type": "global"},
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
            },
        ]
        client = self._make_one(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"entries": ENTRIES}
        client._connection = _Connection(returned)

        iterator = client.list_entries(
            resource_names=[f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
            filter_=INPUT_FILTER,
            order_by=DESCENDING,
            page_size=PAGE_SIZE,
        )
        entries = list(iterator)
        # Check the entries.
        self.assertEqual(len(entries), 2)
        entry = entries[0]
        self.assertIsInstance(entry, StructEntry)
        self.assertEqual(entry.insert_id, IID1)
        self.assertEqual(entry.payload, PAYLOAD)
        logger = entry.logger
        self.assertIsInstance(logger, Logger)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)

        entry = entries[1]
        self.assertIsInstance(entry, ProtobufEntry)
        self.assertEqual(entry.insert_id, IID2)
        self.assertEqual(entry.payload, PROTO_PAYLOAD)
        logger = entry.logger
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)

        self.assertIs(entries[0].logger, entries[1].logger)

        # check call payload
        # filter should not be changed
        self.assertEqual(
            client._connection._called_with,
            {
                "path": "/entries:list",
                "method": "POST",
                "data": {
                    "filter": INPUT_FILTER,
                    "orderBy": DESCENDING,
                    "pageSize": PAGE_SIZE,
                    "resourceNames": [f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
                },
            },
        )

    def test_sink_defaults(self):
        from google.cloud.logging import Sink

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        sink = client.sink(self.SINK_NAME)
        self.assertIsInstance(sink, Sink)
        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertIsNone(sink.filter_)
        self.assertIsNone(sink.destination)
        self.assertIs(sink.client, client)
        self.assertEqual(sink.parent, self.PROJECT_PATH)

    def test_sink_explicit(self):
        from google.cloud.logging import Sink

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        sink = client.sink(
            self.SINK_NAME, filter_=self.FILTER, destination=self.DESTINATION_URI
        )
        self.assertIsInstance(sink, Sink)
        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertIs(sink.client, client)
        self.assertEqual(sink.parent, self.PROJECT_PATH)

    def test_list_sinks_no_paging(self):
        from google.cloud.logging import Sink

        PROJECT = "PROJECT"
        SINK_NAME = "sink_name"
        FILTER = "logName:syslog AND severity>=ERROR"
        SINKS = [
            {"name": SINK_NAME, "filter": FILTER, "destination": self.DESTINATION_URI}
        ]
        client = self._make_one(
            project=PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"sinks": SINKS}
        client._connection = _Connection(returned)

        iterator = client.list_sinks()
        sinks = list(iterator)

        # Check the sinks returned.
        self.assertEqual(len(sinks), 1)
        sink = sinks[0]
        self.assertIsInstance(sink, Sink)
        self.assertEqual(sink.name, SINK_NAME)
        self.assertEqual(sink.filter_, FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertIs(sink.client, client)

        # Verify the mocked transport.
        called_with = client._connection._called_with
        path = "/projects/%s/sinks" % (self.PROJECT,)
        self.assertEqual(
            called_with, {"method": "GET", "path": path, "query_params": {}}
        )

    def test_list_sinks_with_paging(self):
        from google.cloud.logging import Sink

        PROJECT = "PROJECT"
        SINK_NAME = "sink_name"
        FILTER = "logName:syslog AND severity>=ERROR"
        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        SINKS = [
            {"name": SINK_NAME, "filter": FILTER, "destination": self.DESTINATION_URI},
            {"name": "test", "filter": "test", "destination": "test"},
        ]
        client = self._make_one(
            project=PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"sinks": SINKS}
        client._connection = _Connection(returned)

        iterator = client.list_sinks(
            page_size=PAGE_SIZE, page_token=TOKEN, max_results=1
        )
        sinks = list(iterator)
        # Check the sinks returned.
        self.assertEqual(len(sinks), 1)
        sink = sinks[0]
        self.assertIsInstance(sink, Sink)
        self.assertEqual(sink.name, SINK_NAME)
        self.assertEqual(sink.filter_, FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertIs(sink.client, client)

        # Verify the mocked transport.
        called_with = client._connection._called_with
        path = "/projects/%s/sinks" % (self.PROJECT,)
        self.assertEqual(
            called_with,
            {
                "method": "GET",
                "path": path,
                "query_params": {"pageSize": PAGE_SIZE, "pageToken": TOKEN},
            },
        )

    def test_metric_defaults(self):
        from google.cloud.logging import Metric

        creds = _make_credentials()

        client_obj = self._make_one(project=self.PROJECT, credentials=creds)
        metric = client_obj.metric(self.METRIC_NAME)
        self.assertIsInstance(metric, Metric)
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertIsNone(metric.filter_)
        self.assertEqual(metric.description, "")
        self.assertIs(metric.client, client_obj)
        self.assertEqual(metric.project, self.PROJECT)

    def test_metric_explicit(self):
        from google.cloud.logging import Metric

        creds = _make_credentials()

        client_obj = self._make_one(project=self.PROJECT, credentials=creds)
        metric = client_obj.metric(
            self.METRIC_NAME, filter_=self.FILTER, description=self.DESCRIPTION
        )
        self.assertIsInstance(metric, Metric)
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, self.DESCRIPTION)
        self.assertIs(metric.client, client_obj)
        self.assertEqual(metric.project, self.PROJECT)

    def test_list_metrics_no_paging(self):
        from google.cloud.logging import Metric

        metrics = [
            {
                "name": self.METRIC_NAME,
                "filter": self.FILTER,
                "description": self.DESCRIPTION,
            }
        ]
        client = self._make_one(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"metrics": metrics}
        client._connection = _Connection(returned)

        # Execute request.
        iterator = client.list_metrics()
        metrics = list(iterator)

        # Check the metrics returned.
        self.assertEqual(len(metrics), 1)
        metric = metrics[0]
        self.assertIsInstance(metric, Metric)
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, self.DESCRIPTION)
        self.assertIs(metric.client, client)

        # Verify mocked transport.
        called_with = client._connection._called_with
        path = "/projects/%s/metrics" % (self.PROJECT,)
        self.assertEqual(
            called_with, {"method": "GET", "path": path, "query_params": {}}
        )

    def test_list_metrics_with_paging(self):
        from google.cloud.logging import Metric

        token = "TOKEN"
        page_size = 42
        metrics = [
            {
                "name": self.METRIC_NAME,
                "filter": self.FILTER,
                "description": self.DESCRIPTION,
            },
            {"name": "test", "filter": "test", "description": "test"},
        ]
        client = self._make_one(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"metrics": metrics}
        client._connection = _Connection(returned)

        # Execute request.
        iterator = client.list_metrics(
            page_size=page_size, page_token=token, max_results=1
        )
        metrics = list(iterator)
        # Check the metrics returned.
        self.assertEqual(len(metrics), 1)
        metric = metrics[0]
        self.assertIsInstance(metric, Metric)
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, self.DESCRIPTION)
        self.assertIs(metric.client, client)

        # Verify mocked transport.
        called_with = client._connection._called_with
        path = "/projects/%s/metrics" % (self.PROJECT,)
        self.assertEqual(
            called_with,
            {
                "method": "GET",
                "path": path,
                "query_params": {"pageSize": page_size, "pageToken": token},
            },
        )

    def test_get_default_handler_app_engine(self):
        import os

        from google.cloud._testing import _Monkey

        from google.cloud.logging.handlers import CloudLoggingHandler
        from google.cloud.logging_v2.handlers._monitored_resources import _GAE_ENV_VARS

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        gae_env_vars = {var: "TRUE" for var in _GAE_ENV_VARS}

        with _Monkey(os, environ=gae_env_vars):
            handler = client.get_default_handler()

        handler.transport.worker.stop()

        self.assertIsInstance(handler, CloudLoggingHandler)

    def test_get_default_handler_container_engine(self):
        from google.cloud.logging.handlers import StructuredLogHandler

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            return_value="test-gke-cluster",
        )

        with patch:
            handler = client.get_default_handler()

        self.assertIsInstance(handler, StructuredLogHandler)

    def test_get_default_handler_general(self):
        import io

        from google.cloud.logging import Resource
        from google.cloud.logging.handlers import CloudLoggingHandler

        name = "test-logger"
        resource = Resource("resource_type", {"resource_label": "value"})
        labels = {"handler_label": "value"}
        stream = io.BytesIO()

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        handler = client.get_default_handler(
            name=name, resource=resource, labels=labels, stream=stream
        )

        handler.transport.worker.stop()

        self.assertIsInstance(handler, CloudLoggingHandler)
        self.assertEqual(handler.name, name)
        self.assertEqual(handler.resource, resource)
        self.assertEqual(handler.labels, labels)

    def test_setup_logging(self):
        from google.cloud.logging.handlers import CloudLoggingHandler

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        with mock.patch("google.cloud.logging_v2.client.setup_logging") as mocked:
            client.setup_logging()

        self.assertEqual(len(mocked.mock_calls), 1)
        _, args, kwargs = mocked.mock_calls[0]

        (handler,) = args
        self.assertIsInstance(handler, CloudLoggingHandler)
        self.assertIn(handler, client._handlers)

        handler.transport.worker.stop()

        expected_kwargs = {
            "excluded_loggers": (
                "google.api_core.bidi",
                "werkzeug",
            ),
            "log_level": 20,
        }
        self.assertEqual(kwargs, expected_kwargs)

    def test_setup_logging_w_extra_kwargs(self):
        import io

        from google.cloud.logging import Resource
        from google.cloud.logging.handlers import CloudLoggingHandler

        name = "test-logger"
        resource = Resource("resource_type", {"resource_label": "value"})
        labels = {"handler_label": "value"}
        stream = io.BytesIO()

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        with mock.patch("google.cloud.logging_v2.client.setup_logging") as mocked:
            client.setup_logging(
                name=name, resource=resource, labels=labels, stream=stream
            )

        self.assertEqual(len(mocked.mock_calls), 1)
        _, args, kwargs = mocked.mock_calls[0]

        (handler,) = args
        self.assertIsInstance(handler, CloudLoggingHandler)
        self.assertEqual(handler.name, name)
        self.assertEqual(handler.resource, resource)
        self.assertEqual(handler.labels, labels)
        self.assertIn(handler, client._handlers)

        handler.transport.worker.stop()

        expected_kwargs = {
            "excluded_loggers": (
                "google.api_core.bidi",
                "werkzeug",
            ),
            "log_level": 20,
        }
        self.assertEqual(kwargs, expected_kwargs)

    def test_setup_logging_w_extra_kwargs_structured_log(self):
        import io

        from google.cloud.logging import Resource
        from google.cloud.logging.handlers import StructuredLogHandler
        from google.cloud.logging_v2.client import _GKE_RESOURCE_TYPE

        name = "test-logger"
        resource = Resource(_GKE_RESOURCE_TYPE, {"resource_label": "value"})
        labels = {"handler_label": "value"}
        stream = io.BytesIO()

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        with mock.patch("google.cloud.logging_v2.client.setup_logging") as mocked:
            client.setup_logging(
                name=name, resource=resource, labels=labels, stream=stream
            )

        self.assertEqual(len(mocked.mock_calls), 1)
        _, args, kwargs = mocked.mock_calls[0]

        (handler,) = args
        self.assertIsInstance(handler, StructuredLogHandler)

        expected_kwargs = {
            "excluded_loggers": (
                "google.api_core.bidi",
                "werkzeug",
            ),
            "log_level": 20,
        }
        self.assertEqual(kwargs, expected_kwargs)
        self.assertIn(handler, client._handlers)

    def test_flush_handlers_cloud_logging_handler(self):
        import io

        from google.cloud.logging import Resource
        from google.cloud.logging.handlers import CloudLoggingHandler

        name = "test-logger"
        resource = Resource("resource_type", {"resource_label": "value"})
        labels = {"handler_label": "value"}
        stream = io.BytesIO()

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        with mock.patch("google.cloud.logging_v2.client.setup_logging") as mocked:
            client.setup_logging(
                name=name, resource=resource, labels=labels, stream=stream
            )

        self.assertEqual(len(mocked.mock_calls), 1)
        _, args, kwargs = mocked.mock_calls[0]

        (handler,) = args
        self.assertIsInstance(handler, CloudLoggingHandler)

        handler.flush = mock.Mock()
        client.flush_handlers()
        handler.flush.assert_called_once_with()

    def test_flush_handlers_cloud_logging_handler_no_setup_logging(self):
        from google.cloud.logging.handlers import CloudLoggingHandler

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        handler = CloudLoggingHandler(client)
        self.assertIn(handler, client._handlers)

        handler.flush = mock.Mock()
        client.flush_handlers()
        handler.flush.assert_called_once_with()

    def test_flush_handlers_structured_log(self):
        import io

        from google.cloud.logging import Resource
        from google.cloud.logging.handlers import StructuredLogHandler
        from google.cloud.logging_v2.client import _GKE_RESOURCE_TYPE

        name = "test-logger"
        resource = Resource(_GKE_RESOURCE_TYPE, {"resource_label": "value"})
        labels = {"handler_label": "value"}
        stream = io.BytesIO()

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        with mock.patch("google.cloud.logging_v2.client.setup_logging") as mocked:
            client.setup_logging(
                name=name, resource=resource, labels=labels, stream=stream
            )

        self.assertEqual(len(mocked.mock_calls), 1)
        _, args, kwargs = mocked.mock_calls[0]

        (handler,) = args
        self.assertIsInstance(handler, StructuredLogHandler)

        handler.flush = mock.Mock()
        client.flush_handlers()
        handler.flush.assert_called_once_with()

    def test_close_cloud_logging_handler(self):
        import contextlib
        import io

        from google.cloud.logging import Resource
        from google.cloud.logging.handlers import CloudLoggingHandler

        name = "test-logger"
        resource = Resource("resource_type", {"resource_label": "value"})
        labels = {"handler_label": "value"}
        stream = io.BytesIO()

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        with mock.patch("google.cloud.logging_v2.client.setup_logging") as mocked:
            client.setup_logging(
                name=name, resource=resource, labels=labels, stream=stream
            )

        self.assertEqual(len(mocked.mock_calls), 1)
        _, args, kwargs = mocked.mock_calls[0]

        (handler,) = args
        self.assertIsInstance(handler, CloudLoggingHandler)

        handler.close = mock.Mock()
        with contextlib.closing(client):
            pass

        handler.close.assert_called_once_with()

    def test_close_cloud_logging_handler_no_setup_logging(self):
        import contextlib

        from google.cloud.logging.handlers import CloudLoggingHandler

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        handler = CloudLoggingHandler(client)
        self.assertIn(handler, client._handlers)

        handler.close = mock.Mock()
        with contextlib.closing(client):
            pass

        handler.close.assert_called_once_with()

    def test_close_structured_log_handler(self):
        import contextlib
        import io

        from google.cloud.logging import Resource
        from google.cloud.logging.handlers import StructuredLogHandler
        from google.cloud.logging_v2.client import _GKE_RESOURCE_TYPE

        name = "test-logger"
        resource = Resource(_GKE_RESOURCE_TYPE, {"resource_label": "value"})
        labels = {"handler_label": "value"}
        stream = io.BytesIO()

        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )

        with mock.patch("google.cloud.logging_v2.client.setup_logging") as mocked:
            client.setup_logging(
                name=name, resource=resource, labels=labels, stream=stream
            )

        self.assertEqual(len(mocked.mock_calls), 1)
        _, args, kwargs = mocked.mock_calls[0]

        (handler,) = args
        self.assertIsInstance(handler, StructuredLogHandler)

        handler.close = mock.Mock()
        with contextlib.closing(client):
            pass

        handler.close.assert_called_once_with()


class _Connection(object):
    _called_with = None

    def __init__(self, *responses):
        self._responses = responses

    def api_request(self, **kw):
        self._called_with = kw
        response, self._responses = self._responses[0], self._responses[1:]
        return response
