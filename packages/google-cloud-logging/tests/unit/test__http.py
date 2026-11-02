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

import mock


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class TestConnection(unittest.TestCase):
    PROJECT = "project"
    FILTER = "logName:syslog AND severity>=ERROR"

    @staticmethod
    def _get_default_timeout():
        from google.cloud.logging_v2._http import _http

        return _http._DEFAULT_TIMEOUT

    @staticmethod
    def _get_target_class():
        from google.cloud.logging_v2._http import Connection

        return Connection

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_default_url(self):
        client = object()
        conn = self._make_one(client)
        self.assertIs(conn._client, client)

    def test_build_api_url_w_custom_endpoint(self):
        from urllib.parse import parse_qsl, urlsplit

        custom_endpoint = "https://foo-logging.googleapis.com"
        conn = self._make_one(object(), api_endpoint=custom_endpoint)
        uri = conn.build_api_url("/foo")
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual("%s://%s" % (scheme, netloc), custom_endpoint)
        self.assertEqual(path, "/".join(["", conn.API_VERSION, "foo"]))
        parms = dict(parse_qsl(qs))
        pretty_print = parms.pop("prettyPrint", "false")
        self.assertEqual(pretty_print, "false")
        self.assertEqual(parms, {})

    def test_extra_headers(self):
        import requests

        from google.cloud import _http as base_http

        http = mock.create_autospec(requests.Session, instance=True)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.request.return_value = response
        client = mock.Mock(_http=http, spec=["_http"])

        conn = self._make_one(client)
        req_data = "req-data-boring"
        result = conn.api_request("GET", "/rainbow", data=req_data, expect_json=False)
        self.assertEqual(result, data)

        expected_headers = {
            "Accept-Encoding": "gzip",
            base_http.CLIENT_INFO_HEADER: conn.user_agent,
            "User-Agent": conn.user_agent,
        }
        expected_uri = conn.build_api_url("/rainbow")
        http.request.assert_called_once_with(
            data=req_data,
            headers=expected_headers,
            method="GET",
            url=expected_uri,
            timeout=self._get_default_timeout(),
        )


class Test_LoggingAPI(unittest.TestCase):
    PROJECT = "project"
    PROJECT_PATH = "projects/project"
    LIST_ENTRIES_PATH = "entries:list"
    WRITE_ENTRIES_PATH = "entries:write"
    LOGGER_NAME = "LOGGER_NAME"
    LOGGER_PATH = "projects/project/logs/LOGGER_NAME"
    FILTER = "logName:syslog AND severity>=ERROR"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging_v2._http import _LoggingAPI

        return _LoggingAPI

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        connection = _Connection()
        client = _Client(connection)
        api = self._make_one(client)
        self.assertIs(api._client, client)
        self.assertEqual(api.api_request, connection.api_request)

    @staticmethod
    def _make_timestamp():
        import datetime
        from datetime import timezone

        NOW = datetime.datetime.now(timezone.utc)
        return NOW, _datetime_to_rfc3339_w_nanos(NOW)

    def test_list_entries_with_limits(self):
        from google.cloud.logging import Client, Logger, TextEntry

        NOW, TIMESTAMP = self._make_timestamp()
        IID = "IID"
        IID1 = "IID1"
        IID2 = "IID2"
        TEXT = "TEXT"
        SENT = {"resourceNames": [self.PROJECT_PATH]}
        PAYLOAD = {"message": "MESSAGE", "weather": "partly cloudy"}
        PROTO_PAYLOAD = PAYLOAD.copy()
        PROTO_PAYLOAD["@type"] = "type.googleapis.com/testing.example"
        RETURNED = {
            "entries": [
                {
                    "textPayload": TEXT,
                    "insertId": IID,
                    "resource": {"type": "global"},
                    "timestamp": TIMESTAMP,
                    "logName": f"projects/{self.PROJECT}/logs/{self.LOGGER_NAME}",
                },
                {
                    "jsonPayload": PAYLOAD,
                    "insertId": IID1,
                    "resource": {"type": "global"},
                    "timestamp": TIMESTAMP,
                    "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                },
                {
                    "protoPayload": PROTO_PAYLOAD,
                    "insertId": IID2,
                    "resource": {"type": "global"},
                    "timestamp": TIMESTAMP,
                    "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                },
            ],
        }
        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        # try with negative max_results
        with self.assertRaises(ValueError):
            client._connection = _Connection(RETURNED)
            api = self._make_one(client)
            empty = list(api.list_entries([self.PROJECT_PATH], max_results=-1))
        # try with max_results of 0
        client._connection = _Connection(RETURNED)
        api = self._make_one(client)
        empty = list(api.list_entries([self.PROJECT_PATH], max_results=0))
        self.assertEqual(empty, [])
        # try with single result
        client._connection = _Connection(RETURNED)
        api = self._make_one(client)
        iterator = api.list_entries([self.PROJECT_PATH], max_results=1)
        entries = list(iterator)
        # check the entries returned.
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertIsInstance(entry, TextEntry)
        self.assertEqual(entry.payload, TEXT)
        self.assertIsInstance(entry.logger, Logger)
        self.assertEqual(entry.logger.name, self.LOGGER_NAME)
        self.assertEqual(entry.insert_id, IID)
        self.assertEqual(entry.timestamp, NOW)
        self.assertIsNone(entry.labels)
        self.assertIsNone(entry.severity)
        self.assertIsNone(entry.http_request)

        called_with = client._connection._called_with
        expected_path = "/%s" % (self.LIST_ENTRIES_PATH,)
        self.assertEqual(
            called_with, {"method": "POST", "path": expected_path, "data": SENT}
        )

    def test_list_entries(self):
        from google.cloud.logging import (
            DESCENDING,
            Client,
            Logger,
            ProtobufEntry,
            StructEntry,
        )

        PROJECT1 = "PROJECT1"
        PROJECT1_PATH = f"projects/{PROJECT1}"
        PROJECT2 = "PROJECT2"
        PROJECT2_PATH = f"projects/{PROJECT2}"
        NOW, TIMESTAMP = self._make_timestamp()
        IID1 = "IID1"
        IID2 = "IID2"
        PAYLOAD = {"message": "MESSAGE", "weather": "partly cloudy"}
        PROTO_PAYLOAD = PAYLOAD.copy()
        PROTO_PAYLOAD["@type"] = "type.googleapis.com/testing.example"
        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        SENT = {
            "resourceNames": [PROJECT1_PATH, PROJECT2_PATH],
            "filter": self.FILTER,
            "orderBy": DESCENDING,
            "pageSize": PAGE_SIZE,
            "pageToken": TOKEN,
        }
        RETURNED = {
            "entries": [
                {
                    "jsonPayload": PAYLOAD,
                    "insertId": IID1,
                    "resource": {"type": "global"},
                    "timestamp": TIMESTAMP,
                    "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                },
                {
                    "protoPayload": PROTO_PAYLOAD,
                    "insertId": IID2,
                    "resource": {"type": "global"},
                    "timestamp": TIMESTAMP,
                    "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                },
            ]
        }
        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        client._connection = _Connection(RETURNED)
        api = self._make_one(client)

        iterator = api.list_entries(
            resource_names=[PROJECT1_PATH, PROJECT2_PATH],
            filter_=self.FILTER,
            order_by=DESCENDING,
            page_size=PAGE_SIZE,
            page_token=TOKEN,
        )
        entries = list(iterator)

        # Check the entries returned.
        self.assertEqual(len(entries), 2)
        entry1 = entries[0]
        self.assertIsInstance(entry1, StructEntry)
        self.assertEqual(entry1.payload, PAYLOAD)
        self.assertIsInstance(entry1.logger, Logger)
        self.assertEqual(entry1.logger.name, self.LOGGER_NAME)
        self.assertEqual(entry1.insert_id, IID1)
        self.assertEqual(entry1.timestamp, NOW)
        self.assertIsNone(entry1.labels)
        self.assertIsNone(entry1.severity)
        self.assertIsNone(entry1.http_request)

        entry2 = entries[1]
        self.assertIsInstance(entry2, ProtobufEntry)
        self.assertEqual(entry2.payload, PROTO_PAYLOAD)
        self.assertIsInstance(entry2.logger, Logger)
        self.assertEqual(entry2.logger.name, self.LOGGER_NAME)
        self.assertEqual(entry2.insert_id, IID2)
        self.assertEqual(entry2.timestamp, NOW)
        self.assertIsNone(entry2.labels)
        self.assertIsNone(entry2.severity)
        self.assertIsNone(entry2.http_request)

        called_with = client._connection._called_with
        expected_path = "/%s" % (self.LIST_ENTRIES_PATH,)
        self.assertEqual(
            called_with, {"method": "POST", "path": expected_path, "data": SENT}
        )

    def test_write_entries_single(self):
        TEXT = "TEXT"
        ENTRY = {
            "textPayload": TEXT,
            "resource": {"type": "global"},
            "logName": "projects/{self.PROJECT}/logs/{self.LOGGER_NAME}",
        }
        SENT = {"entries": [ENTRY], "partialSuccess": False, "dry_run": False}
        conn = _Connection({})
        client = _Client(conn)
        api = self._make_one(client)

        api.write_entries([ENTRY], partial_success=False)

        self.assertEqual(conn._called_with["method"], "POST")
        path = f"/{self.WRITE_ENTRIES_PATH}"
        self.assertEqual(conn._called_with["path"], path)
        self.assertEqual(conn._called_with["data"], SENT)

    def test_write_entries_multiple(self):
        TEXT = "TEXT"
        LOG_NAME = f"projects/{self.PROJECT}/logs/{self.LOGGER_NAME}"
        RESOURCE = {"type": "global"}
        LABELS = {"baz": "qux", "spam": "eggs"}
        ENTRY1 = {"textPayload": TEXT}
        ENTRY2 = {"jsonPayload": {"foo": "bar"}}
        SENT = {
            "logName": LOG_NAME,
            "resource": RESOURCE,
            "labels": LABELS,
            "entries": [ENTRY1, ENTRY2],
            "partialSuccess": True,
            "dry_run": False,
        }
        conn = _Connection({})
        client = _Client(conn)
        api = self._make_one(client)

        api.write_entries(
            [ENTRY1, ENTRY2], logger_name=LOG_NAME, resource=RESOURCE, labels=LABELS
        )

        self.assertEqual(conn._called_with["method"], "POST")
        path = f"/{self.WRITE_ENTRIES_PATH}"
        self.assertEqual(conn._called_with["path"], path)
        self.assertEqual(conn._called_with["data"], SENT)

    def test_logger_delete(self):
        path = f"/projects/{self.PROJECT}/logs/{self.LOGGER_NAME}"
        conn = _Connection({})
        client = _Client(conn)
        api = self._make_one(client)

        api.logger_delete(self.LOGGER_PATH)

        self.assertEqual(conn._called_with["method"], "DELETE")
        self.assertEqual(conn._called_with["path"], path)


class Test_SinksAPI(unittest.TestCase):
    PROJECT = "project"
    PROJECT_PATH = "projects/project"
    FILTER = "logName:syslog AND severity>=ERROR"
    LIST_SINKS_PATH = f"projects/{PROJECT}/sinks"
    SINK_NAME = "sink_name"
    SINK_PATH = f"projects/{PROJECT}/sinks/{SINK_NAME}"
    DESTINATION_URI = "faux.googleapis.com/destination"
    WRITER_IDENTITY = "serviceAccount:project-123@example.com"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging_v2._http import _SinksAPI

        return _SinksAPI

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        connection = _Connection()
        client = _Client(connection)
        api = self._make_one(client)
        self.assertIs(api._client, client)
        self.assertEqual(api.api_request, connection.api_request)

    def test_list_sinks_max_returned(self):
        from google.cloud.logging import Sink

        RETURNED = {
            "sinks": [
                {
                    "name": self.SINK_PATH,
                    "filter": self.FILTER,
                    "destination": self.DESTINATION_URI,
                },
                {"name": "test", "filter": "test", "destination": "test"},
            ],
        }
        # try with negative max_results
        with self.assertRaises(ValueError):
            conn = _Connection(RETURNED)
            client = _Client(conn)
            api = self._make_one(client)
            empty = list(api.list_sinks(self.PROJECT_PATH, max_results=-1))
        # try with max_results of 0
        conn = _Connection(RETURNED)
        client = _Client(conn)
        api = self._make_one(client)
        empty = list(api.list_sinks(self.PROJECT_PATH, max_results=0))
        self.assertEqual(empty, [])
        # try with single result
        conn = _Connection(RETURNED)
        client = _Client(conn)
        api = self._make_one(client)
        iterator = api.list_sinks(self.PROJECT_PATH, max_results=1)
        sinks = list(iterator)
        # Check the sinks returned.
        self.assertEqual(len(sinks), 1)
        sink = sinks[0]
        self.assertIsInstance(sink, Sink)
        self.assertEqual(sink.name, self.SINK_PATH)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertIs(sink.client, client)

        called_with = conn._called_with
        path = f"/{self.LIST_SINKS_PATH}"
        self.assertEqual(
            called_with, {"method": "GET", "path": path, "query_params": {}}
        )

    def test_list_sinks(self):
        from google.cloud.logging import Sink

        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        RETURNED = {
            "sinks": [
                {
                    "name": self.SINK_PATH,
                    "filter": self.FILTER,
                    "destination": self.DESTINATION_URI,
                }
            ]
        }
        conn = _Connection(RETURNED)
        client = _Client(conn)
        api = self._make_one(client)

        iterator = api.list_sinks(
            self.PROJECT_PATH, page_size=PAGE_SIZE, page_token=TOKEN
        )
        sinks = list(iterator)
        # Check the sinks returned.
        self.assertEqual(len(sinks), 1)
        sink = sinks[0]
        self.assertIsInstance(sink, Sink)
        self.assertEqual(sink.name, self.SINK_PATH)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertIs(sink.client, client)

        called_with = conn._called_with
        path = f"/{self.LIST_SINKS_PATH}"
        self.assertEqual(
            called_with,
            {
                "method": "GET",
                "path": path,
                "query_params": {"pageSize": PAGE_SIZE, "pageToken": TOKEN},
            },
        )

    def test_sink_create_conflict(self):
        from google.cloud.exceptions import Conflict

        sent = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
        }
        conn = _Connection()
        conn._raise_conflict = True
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(Conflict):
            api.sink_create(
                self.PROJECT_PATH, self.SINK_NAME, self.FILTER, self.DESTINATION_URI
            )

        path = f"/projects/{self.PROJECT}/sinks"
        expected = {
            "method": "POST",
            "path": path,
            "data": sent,
            "query_params": {"uniqueWriterIdentity": False},
        }
        self.assertEqual(conn._called_with, expected)

    def test_sink_create_ok(self):
        sent = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
        }
        after_create = sent.copy()
        after_create["writerIdentity"] = self.WRITER_IDENTITY
        conn = _Connection(after_create)
        client = _Client(conn)
        api = self._make_one(client)

        returned = api.sink_create(
            self.PROJECT_PATH,
            self.SINK_NAME,
            self.FILTER,
            self.DESTINATION_URI,
            unique_writer_identity=True,
        )

        self.assertEqual(returned, after_create)
        path = f"/projects/{self.PROJECT}/sinks"
        expected = {
            "method": "POST",
            "path": path,
            "data": sent,
            "query_params": {"uniqueWriterIdentity": True},
        }
        self.assertEqual(conn._called_with, expected)

    def test_sink_get_miss(self):
        from google.cloud.exceptions import NotFound

        conn = _Connection()
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(NotFound):
            api.sink_get(self.SINK_PATH)

        self.assertEqual(conn._called_with["method"], "GET")
        path = f"/projects/{self.PROJECT}/sinks/{self.SINK_NAME}"
        self.assertEqual(conn._called_with["path"], path)

    def test_sink_get_hit(self):
        RESPONSE = {
            "name": self.SINK_PATH,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
        }
        conn = _Connection(RESPONSE)
        client = _Client(conn)
        api = self._make_one(client)

        response = api.sink_get(self.SINK_PATH)

        self.assertEqual(response, RESPONSE)
        self.assertEqual(conn._called_with["method"], "GET")
        path = f"/projects/{self.PROJECT}/sinks/{self.SINK_NAME}"
        self.assertEqual(conn._called_with["path"], path)

    def test_sink_update_miss(self):
        from google.cloud.exceptions import NotFound

        sent = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
        }
        conn = _Connection()
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(NotFound):
            api.sink_update(self.SINK_PATH, self.FILTER, self.DESTINATION_URI)

        path = f"/projects/{self.PROJECT}/sinks/{self.SINK_NAME}"
        expected = {
            "method": "PUT",
            "path": path,
            "data": sent,
            "query_params": {"uniqueWriterIdentity": False},
        }
        self.assertEqual(conn._called_with, expected)

    def test_sink_update_hit(self):
        sent = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
        }
        after_update = sent.copy()
        after_update["writerIdentity"] = self.WRITER_IDENTITY
        conn = _Connection(after_update)
        client = _Client(conn)
        api = self._make_one(client)

        returned = api.sink_update(
            self.SINK_PATH,
            self.FILTER,
            self.DESTINATION_URI,
            unique_writer_identity=True,
        )

        self.assertEqual(returned, after_update)
        path = f"/projects/{self.PROJECT}/sinks/{self.SINK_NAME}"
        expected = {
            "method": "PUT",
            "path": path,
            "data": sent,
            "query_params": {"uniqueWriterIdentity": True},
        }
        self.assertEqual(conn._called_with, expected)

    def test_sink_delete_miss(self):
        from google.cloud.exceptions import NotFound

        conn = _Connection()
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(NotFound):
            api.sink_delete(self.SINK_PATH)

        self.assertEqual(conn._called_with["method"], "DELETE")
        path = f"/projects/{self.PROJECT}/sinks/{self.SINK_NAME}"
        self.assertEqual(conn._called_with["path"], path)

    def test_sink_delete_hit(self):
        conn = _Connection({})
        client = _Client(conn)
        api = self._make_one(client)

        api.sink_delete(self.SINK_PATH)

        self.assertEqual(conn._called_with["method"], "DELETE")
        path = f"/projects/{self.PROJECT}/sinks/{self.SINK_NAME}"
        self.assertEqual(conn._called_with["path"], path)


class Test_MetricsAPI(unittest.TestCase):
    PROJECT = "project"
    FILTER = "logName:syslog AND severity>=ERROR"
    LIST_METRICS_PATH = "projects/%s/metrics" % (PROJECT,)
    METRIC_NAME = "metric_name"
    METRIC_PATH = "projects/%s/metrics/%s" % (PROJECT, METRIC_NAME)
    DESCRIPTION = "DESCRIPTION"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging_v2._http import _MetricsAPI

        return _MetricsAPI

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_list_metrics_max_results(self):
        from google.cloud.logging import Metric

        RETURNED = {
            "metrics": [
                {"name": self.METRIC_PATH, "filter": self.FILTER},
                {"name": "test", "filter": "test"},
            ],
        }
        # try with negative max_results
        with self.assertRaises(ValueError):
            conn = _Connection(RETURNED)
            client = _Client(conn)
            api = self._make_one(client)
            empty = list(api.list_metrics(self.PROJECT, max_results=-1))
        # try with max_results of 0
        conn = _Connection(RETURNED)
        client = _Client(conn)
        api = self._make_one(client)
        empty = list(api.list_metrics(self.PROJECT, max_results=0))
        self.assertEqual(empty, [])
        # try with single result
        conn = _Connection(RETURNED)
        client = _Client(conn)
        api = self._make_one(client)

        iterator = api.list_metrics(self.PROJECT, max_results=1)
        metrics = list(iterator)
        # Check the metrics returned.
        self.assertEqual(len(metrics), 1)
        metric = metrics[0]
        self.assertIsInstance(metric, Metric)
        self.assertEqual(metric.name, self.METRIC_PATH)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, "")
        self.assertIs(metric.client, client)

        called_with = conn._called_with
        path = "/%s" % (self.LIST_METRICS_PATH,)
        self.assertEqual(
            called_with, {"method": "GET", "path": path, "query_params": {}}
        )

    def test_list_metrics(self):
        from google.cloud.logging import Metric

        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        RETURNED = {"metrics": [{"name": self.METRIC_PATH, "filter": self.FILTER}]}
        conn = _Connection(RETURNED)
        client = _Client(conn)
        api = self._make_one(client)

        iterator = api.list_metrics(self.PROJECT, page_size=PAGE_SIZE, page_token=TOKEN)
        metrics = list(iterator)
        # Check the metrics returned.
        self.assertEqual(len(metrics), 1)
        metric = metrics[0]
        self.assertIsInstance(metric, Metric)
        self.assertEqual(metric.name, self.METRIC_PATH)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, "")
        self.assertIs(metric.client, client)

        called_with = conn._called_with
        path = "/%s" % (self.LIST_METRICS_PATH,)
        self.assertEqual(
            called_with,
            {
                "method": "GET",
                "path": path,
                "query_params": {"pageSize": PAGE_SIZE, "pageToken": TOKEN},
            },
        )

    def test_metric_create_conflict(self):
        from google.cloud.exceptions import Conflict

        SENT = {
            "name": self.METRIC_NAME,
            "filter": self.FILTER,
            "description": self.DESCRIPTION,
        }
        conn = _Connection()
        conn._raise_conflict = True
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(Conflict):
            api.metric_create(
                self.PROJECT, self.METRIC_NAME, self.FILTER, self.DESCRIPTION
            )

        self.assertEqual(conn._called_with["method"], "POST")
        path = "/projects/%s/metrics" % (self.PROJECT,)
        self.assertEqual(conn._called_with["path"], path)
        self.assertEqual(conn._called_with["data"], SENT)

    def test_metric_create_ok(self):
        SENT = {
            "name": self.METRIC_NAME,
            "filter": self.FILTER,
            "description": self.DESCRIPTION,
        }
        conn = _Connection({})
        client = _Client(conn)
        api = self._make_one(client)

        api.metric_create(self.PROJECT, self.METRIC_NAME, self.FILTER, self.DESCRIPTION)

        self.assertEqual(conn._called_with["method"], "POST")
        path = "/projects/%s/metrics" % (self.PROJECT,)
        self.assertEqual(conn._called_with["path"], path)
        self.assertEqual(conn._called_with["data"], SENT)

    def test_metric_get_miss(self):
        from google.cloud.exceptions import NotFound

        conn = _Connection()
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(NotFound):
            api.metric_get(self.PROJECT, self.METRIC_NAME)

        self.assertEqual(conn._called_with["method"], "GET")
        path = "/projects/%s/metrics/%s" % (self.PROJECT, self.METRIC_NAME)
        self.assertEqual(conn._called_with["path"], path)

    def test_metric_get_hit(self):
        RESPONSE = {
            "name": self.METRIC_NAME,
            "filter": self.FILTER,
            "description": self.DESCRIPTION,
        }
        conn = _Connection(RESPONSE)
        client = _Client(conn)
        api = self._make_one(client)

        response = api.metric_get(self.PROJECT, self.METRIC_NAME)

        self.assertEqual(response, RESPONSE)
        self.assertEqual(conn._called_with["method"], "GET")
        path = "/projects/%s/metrics/%s" % (self.PROJECT, self.METRIC_NAME)
        self.assertEqual(conn._called_with["path"], path)

    def test_metric_update_miss(self):
        from google.cloud.exceptions import NotFound

        SENT = {
            "name": self.METRIC_NAME,
            "filter": self.FILTER,
            "description": self.DESCRIPTION,
        }
        conn = _Connection()
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(NotFound):
            api.metric_update(
                self.PROJECT, self.METRIC_NAME, self.FILTER, self.DESCRIPTION
            )

        self.assertEqual(conn._called_with["method"], "PUT")
        path = "/projects/%s/metrics/%s" % (self.PROJECT, self.METRIC_NAME)
        self.assertEqual(conn._called_with["path"], path)
        self.assertEqual(conn._called_with["data"], SENT)

    def test_metric_update_hit(self):
        SENT = {
            "name": self.METRIC_NAME,
            "filter": self.FILTER,
            "description": self.DESCRIPTION,
        }
        conn = _Connection({})
        client = _Client(conn)
        api = self._make_one(client)

        api.metric_update(self.PROJECT, self.METRIC_NAME, self.FILTER, self.DESCRIPTION)

        self.assertEqual(conn._called_with["method"], "PUT")
        path = "/projects/%s/metrics/%s" % (self.PROJECT, self.METRIC_NAME)
        self.assertEqual(conn._called_with["path"], path)
        self.assertEqual(conn._called_with["data"], SENT)

    def test_metric_delete_miss(self):
        from google.cloud.exceptions import NotFound

        conn = _Connection()
        client = _Client(conn)
        api = self._make_one(client)

        with self.assertRaises(NotFound):
            api.metric_delete(self.PROJECT, self.METRIC_NAME)

        self.assertEqual(conn._called_with["method"], "DELETE")
        path = "/projects/%s/metrics/%s" % (self.PROJECT, self.METRIC_NAME)
        self.assertEqual(conn._called_with["path"], path)

    def test_metric_delete_hit(self):
        conn = _Connection({})
        client = _Client(conn)
        api = self._make_one(client)

        api.metric_delete(self.PROJECT, self.METRIC_NAME)

        self.assertEqual(conn._called_with["method"], "DELETE")
        path = "/projects/%s/metrics/%s" % (self.PROJECT, self.METRIC_NAME)
        self.assertEqual(conn._called_with["path"], path)


class _Connection(object):
    _called_with = None
    _raise_conflict = False

    def __init__(self, *responses):
        self._responses = responses

    def api_request(self, **kw):
        from google.cloud.exceptions import Conflict, NotFound

        self._called_with = kw
        if self._raise_conflict:
            raise Conflict("oops")
        try:
            response, self._responses = self._responses[0], self._responses[1:]
        except IndexError:
            raise NotFound("miss")
        return response


def _datetime_to_rfc3339_w_nanos(value):
    from google.cloud._helpers import _RFC3339_NO_FRACTION

    no_fraction = value.strftime(_RFC3339_NO_FRACTION)
    return "%s.%09dZ" % (no_fraction, value.microsecond * 1000)


class _Client(object):
    def __init__(self, connection):
        self._connection = connection
