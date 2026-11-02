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
from copy import deepcopy
from datetime import datetime, timedelta, timezone

import mock


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class TestLogger(unittest.TestCase):
    PROJECT = "test-project"
    LOGGER_NAME = "logger-name"
    TIME_FORMAT = '"%Y-%m-%dT%H:%M:%S.%f%z"'

    def setUp(self):
        import google.cloud.logging_v2

        # Test instrumentation behavior in only one test
        google.cloud.logging_v2._instrumentation_emitted = True

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import Logger

        return Logger

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        conn = object()
        client = _Client(self.PROJECT, conn)
        logger = self._make_one(self.LOGGER_NAME, client=client)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)
        self.assertEqual(
            logger.full_name, "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertEqual(
            logger.path, "/projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertIsNone(logger.labels)

    def test_ctor_explicit(self):
        LABELS = {"foo": "bar", "baz": "qux"}
        conn = object()
        client = _Client(self.PROJECT, conn)
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=LABELS)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.project, self.PROJECT)
        self.assertEqual(
            logger.full_name, "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertEqual(
            logger.path, "/projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        )
        self.assertEqual(logger.labels, LABELS)

    def test_batch_w_bound_client(self):
        from google.cloud.logging import Batch

        conn = object()
        client = _Client(self.PROJECT, conn)
        logger = self._make_one(self.LOGGER_NAME, client=client)
        batch = logger.batch()
        self.assertIsInstance(batch, Batch)
        self.assertIs(batch.logger, logger)
        self.assertIs(batch.client, client)

    def test_batch_w_alternate_client(self):
        from google.cloud.logging import Batch

        conn1 = object()
        conn2 = object()
        client1 = _Client(self.PROJECT, conn1)
        client2 = _Client(self.PROJECT, conn2)
        logger = self._make_one(self.LOGGER_NAME, client=client1)
        batch = logger.batch(client=client2)
        self.assertIsInstance(batch, Batch)
        self.assertIs(batch.logger, logger)
        self.assertIs(batch.client, client2)

    def test_log_empty_defaults_w_default_labels(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "resource": detect_resource(self.PROJECT)._to_dict(),
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_empty()

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_empty_w_explicit(self):
        import datetime

        from google.cloud.logging import Resource

        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_empty(
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_text_defaults(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        RESOURCE = detect_resource(self.PROJECT)._to_dict()
        TEXT = "TEXT"
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "textPayload": TEXT,
                "resource": RESOURCE,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log_text(TEXT)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_text_w_unicode_and_default_labels(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        TEXT = "TEXT"
        RESOURCE = detect_resource(self.PROJECT)._to_dict()
        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "textPayload": TEXT,
                "resource": RESOURCE,
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_text(TEXT)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_text_explicit(self):
        import datetime

        from google.cloud.logging import Resource

        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        TEXT = "TEXT"
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "textPayload": TEXT,
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_text(
            TEXT,
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_struct_defaults(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        STRUCT = {"message": "MESSAGE", "weather": "cloudy"}
        RESOURCE = detect_resource(self.PROJECT)._to_dict()
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "jsonPayload": STRUCT,
                "resource": RESOURCE,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log_struct(STRUCT)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_nested_struct(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        STRUCT = {"message": "MESSAGE", "weather": "cloudy", "nested": {"one": 2}}
        RESOURCE = detect_resource(self.PROJECT)._to_dict()
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "jsonPayload": STRUCT,
                "resource": RESOURCE,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log(STRUCT)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_struct_w_default_labels(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        STRUCT = {"message": "MESSAGE", "weather": "cloudy"}
        RESOURCE = detect_resource(self.PROJECT)._to_dict()
        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "jsonPayload": STRUCT,
                "resource": RESOURCE,
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_struct(STRUCT)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_struct_w_explicit(self):
        import datetime

        from google.cloud.logging import Resource

        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        STRUCT = {"message": "MESSAGE", "weather": "cloudy"}
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "jsonPayload": STRUCT,
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_struct(
            STRUCT,
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_struct_inference(self):
        """
        LogEntry fields in _STRUCT_EXTRACTABLE_FIELDS should be inferred from
        the payload data if not passed as a parameter
        """
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        STRUCT = {
            "message": "System test: test_log_struct_logentry_data",
            "severity": "warning",
            "trace": "123",
            "span_id": "456",
        }
        RESOURCE = detect_resource(self.PROJECT)._to_dict()
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "jsonPayload": STRUCT,
                "severity": "WARNING",
                "trace": "123",
                "spanId": "456",
                "resource": RESOURCE,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log_struct(STRUCT, resource=RESOURCE)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_w_dict_resource(self):
        """
        Users should be able to input a dictionary with type and labels instead
        of a Resource object
        """
        import pytest

        MESSAGE = "hello world"
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)
        broken_resource_dicts = [{}, {"type": ""}, {"labels": ""}]
        for resource in broken_resource_dicts:
            # ensure bad inputs result in a helpful error
            with pytest.raises(TypeError):
                logger.log(MESSAGE, resource=resource)
        # ensure well-formed dict is converted to a resource
        resource = {"type": "gae_app", "labels": []}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "textPayload": MESSAGE,
                "resource": resource,
            }
        ]
        logger.log(MESSAGE, resource=resource)
        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_lowercase_severity(self):
        """
        lower case severity strings should be accepted
        """
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        for lower_severity in [
            "default",
            "debug",
            "info",
            "notice",
            "warning",
            "error",
            "critical",
            "alert",
            "emergency",
        ]:
            MESSAGE = "hello world"
            RESOURCE = detect_resource(self.PROJECT)._to_dict()
            ENTRIES = [
                {
                    "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                    "textPayload": MESSAGE,
                    "resource": RESOURCE,
                    "severity": lower_severity.upper(),
                }
            ]
            client = _Client(self.PROJECT)
            api = client.logging_api = _DummyLoggingAPI()
            logger = self._make_one(self.LOGGER_NAME, client=client)

            logger.log(MESSAGE, severity=lower_severity)

            self.assertEqual(
                api._write_entries_called_with, (ENTRIES, None, None, None, True)
            )

    def test_log_proto_defaults(self):
        import json

        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        message = Struct(fields={"foo": Value(bool_value=True)})
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "protoPayload": json.loads(MessageToJson(message)),
                "resource": detect_resource(self.PROJECT)._to_dict(),
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log_proto(message)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_proto_w_default_labels(self):
        import json

        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        message = Struct(fields={"foo": Value(bool_value=True)})
        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "protoPayload": json.loads(MessageToJson(message)),
                "resource": detect_resource(self.PROJECT)._to_dict(),
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log_proto(message)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_proto_w_explicit(self):
        import datetime
        import json

        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import Resource

        message = Struct(fields={"foo": Value(bool_value=True)})
        ALT_LOG_NAME = "projects/foo/logs/alt.log.name"
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRIES = [
            {
                "logName": ALT_LOG_NAME,
                "protoPayload": json.loads(MessageToJson(message)),
                "labels": LABELS,
                "insertId": IID,
                "severity": SEVERITY,
                "httpRequest": REQUEST,
                "timestamp": "2016-12-31T00:01:02.999999Z",
                "resource": RESOURCE._to_dict(),
                "trace": TRACE,
                "spanId": SPANID,
                "traceSampled": True,
            }
        ]
        client1 = _Client(self.PROJECT)
        client2 = _Client(self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1, labels=DEFAULT_LABELS)

        logger.log_proto(
            message,
            log_name=ALT_LOG_NAME,
            client=client2,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_inference_empty(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        DEFAULT_LABELS = {"foo": "spam"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "resource": detect_resource(self.PROJECT)._to_dict(),
                "labels": DEFAULT_LABELS,
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)

        logger.log()

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_inference_text(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        TEXT = "TEXT"
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "textPayload": TEXT,
                "resource": detect_resource(self.PROJECT)._to_dict(),
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log(TEXT)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_inference_struct(self):
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        STRUCT = {"message": "MESSAGE", "weather": "cloudy"}
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "jsonPayload": STRUCT,
                "resource": detect_resource(self.PROJECT)._to_dict(),
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log(STRUCT)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_log_inference_proto(self):
        import json

        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        message = Struct(fields={"foo": Value(bool_value=True)})
        ENTRIES = [
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "protoPayload": json.loads(MessageToJson(message)),
                "resource": detect_resource(self.PROJECT)._to_dict(),
            }
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.log(message)

        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

    def test_delete_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client)

        logger.delete()

        self.assertEqual(
            api._logger_delete_called_with,
            (f"projects/{self.PROJECT}/logs/{self.LOGGER_NAME}"),
        )

    def test_delete_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client1)

        logger.delete(client=client2)

        self.assertEqual(
            api._logger_delete_called_with,
            (f"projects/{self.PROJECT}/logs/{self.LOGGER_NAME}"),
        )

    def test_list_entries_defaults(self):
        from google.cloud.logging import Client

        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {}
        client._connection = _Connection(returned)

        logger = self._make_one(self.LOGGER_NAME, client=client)

        iterator = logger.list_entries()
        entries = list(iterator)

        self.assertEqual(len(entries), 0)
        LOG_FILTER = "logName=projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)

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
            LOG_FILTER + " AND timestamp>=" + self.TIME_FORMAT,
        )
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        self.assertLess(yesterday - timestamp, timedelta(minutes=1))

    def test_list_entries_explicit(self):
        from google.cloud.logging import DESCENDING, Client

        PROJECT1 = "PROJECT1"
        PROJECT2 = "PROJECT2"
        INPUT_FILTER = "resource.type:global"
        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        client._connection = _Connection({})
        logger = self._make_one(self.LOGGER_NAME, client=client)
        iterator = logger.list_entries(
            resource_names=[f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
            filter_=INPUT_FILTER,
            order_by=DESCENDING,
            page_size=PAGE_SIZE,
            page_token=TOKEN,
        )
        entries = list(iterator)

        self.assertEqual(len(entries), 0)
        # self.assertEqual(client._listed, LISTED)
        # check call payload
        call_payload_no_filter = deepcopy(client._connection._called_with)
        call_payload_no_filter["data"]["filter"] = "removed"
        self.assertEqual(
            call_payload_no_filter,
            {
                "method": "POST",
                "path": "/entries:list",
                "data": {
                    "filter": "removed",
                    "orderBy": DESCENDING,
                    "pageSize": PAGE_SIZE,
                    "pageToken": TOKEN,
                    "resourceNames": [f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
                },
            },
        )
        # verify that default filter is 24 hours
        LOG_FILTER = "logName=projects/%s/logs/%s" % (
            self.PROJECT,
            self.LOGGER_NAME,
        )
        combined_filter = (
            INPUT_FILTER
            + " AND "
            + LOG_FILTER
            + " AND "
            + "timestamp>="
            + self.TIME_FORMAT
        )
        timestamp = datetime.strptime(
            client._connection._called_with["data"]["filter"], combined_filter
        )
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        self.assertLess(yesterday - timestamp, timedelta(minutes=1))

    def test_list_entries_explicit_timestamp(self):
        from google.cloud.logging import DESCENDING, Client

        PROJECT1 = "PROJECT1"
        PROJECT2 = "PROJECT2"
        INPUT_FILTER = 'resource.type:global AND timestamp="2020-10-13T21"'
        TOKEN = "TOKEN"
        PAGE_SIZE = 42
        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        client._connection = _Connection({})
        logger = self._make_one(self.LOGGER_NAME, client=client)
        iterator = logger.list_entries(
            resource_names=[f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
            filter_=INPUT_FILTER,
            order_by=DESCENDING,
            page_size=PAGE_SIZE,
            page_token=TOKEN,
        )
        entries = list(iterator)

        self.assertEqual(len(entries), 0)
        # self.assertEqual(client._listed, LISTED)
        # check call payload
        LOG_FILTER = "logName=projects/%s/logs/%s" % (
            self.PROJECT,
            self.LOGGER_NAME,
        )
        combined_filter = INPUT_FILTER + " AND " + LOG_FILTER
        self.assertEqual(
            client._connection._called_with,
            {
                "method": "POST",
                "path": "/entries:list",
                "data": {
                    "filter": combined_filter,
                    "orderBy": DESCENDING,
                    "pageSize": PAGE_SIZE,
                    "pageToken": TOKEN,
                    "resourceNames": [f"projects/{PROJECT1}", f"projects/{PROJECT2}"],
                },
            },
        )

    def test_list_entries_limit(self):
        from google.cloud.logging import (
            DESCENDING,
            Client,
            Logger,
            ProtobufEntry,
            StructEntry,
        )

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
        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        returned = {"entries": ENTRIES}
        client._connection = _Connection(returned)
        logger = self._make_one(self.LOGGER_NAME, client=client)

        iterator = logger.list_entries(
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

    def test_list_entries_folder(self):
        from google.cloud.logging import Client, TextEntry

        client = Client(
            project=self.PROJECT, credentials=_make_credentials(), _use_grpc=False
        )
        FOLDER_ID = "123"
        LOG_NAME = f"folders/{FOLDER_ID}/logs/cloudaudit.googleapis.com%2Fdata_access"

        ENTRIES = [
            {
                "textPayload": "hello world",
                "insertId": "1",
                "resource": {"type": "global"},
                "logName": LOG_NAME,
            },
        ]
        returned = {"entries": ENTRIES}
        client._connection = _Connection(returned)

        iterator = client.list_entries(
            resource_names=[f"folder/{FOLDER_ID}"],
        )
        entries = list(iterator)
        # Check the entries.
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertIsInstance(entry, TextEntry)
        self.assertIsNone(entry.logger)
        self.assertEqual(entry.log_name, LOG_NAME)

    def test_first_log_emits_instrumentation(self):
        import google.cloud.logging_v2
        from google.cloud.logging_v2._instrumentation import _create_diagnostic_entry
        from google.cloud.logging_v2.handlers._monitored_resources import (
            detect_resource,
        )

        google.cloud.logging_v2._instrumentation_emitted = False
        DEFAULT_LABELS = {"foo": "spam"}
        resource = detect_resource(self.PROJECT)
        instrumentation_entry = _create_diagnostic_entry(
            resource=resource,
            labels=DEFAULT_LABELS,
        ).to_api_repr()
        instrumentation_entry["logName"] = "projects/%s/logs/%s" % (
            self.PROJECT,
            self.LOGGER_NAME,
        )
        ENTRIES = [
            instrumentation_entry,
            {
                "logName": "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME),
                "resource": resource._to_dict(),
                "labels": DEFAULT_LABELS,
            },
        ]
        client = _Client(self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = self._make_one(self.LOGGER_NAME, client=client, labels=DEFAULT_LABELS)
        logger.log_empty()
        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )

        ENTRIES = ENTRIES[-1:]
        api = client.logging_api = _DummyLoggingAPI()
        logger.log_empty()
        self.assertEqual(
            api._write_entries_called_with, (ENTRIES, None, None, None, True)
        )


class TestBatch(unittest.TestCase):
    PROJECT = "test-project"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import Batch

        return Batch

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_ctor_defaults(self):
        logger = _Logger()
        client = _Client(project=self.PROJECT)
        batch = self._make_one(logger, client)
        self.assertIs(batch.logger, logger)
        self.assertIs(batch.client, client)
        self.assertEqual(len(batch.entries), 0)

    def test_log_empty_defaults(self):
        from google.cloud.logging import LogEntry

        ENTRY = LogEntry()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_empty()
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_empty_explicit(self):
        import datetime

        from google.cloud.logging import LogEntry, Resource

        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        ENTRY = LogEntry(
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_empty(
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_text_defaults(self):
        from google.cloud.logging import TextEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        ENTRY = TextEntry(payload=TEXT, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_text(TEXT)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_text_explicit(self):
        import datetime

        from google.cloud.logging import Resource, TextEntry

        TEXT = "This is the entry text"
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        ENTRY = TextEntry(
            payload=TEXT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_text(
            TEXT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_struct_defaults(self):
        from google.cloud.logging import StructEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        STRUCT = {"message": "Message text", "weather": "partly cloudy"}
        ENTRY = StructEntry(payload=STRUCT, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_struct(STRUCT)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_struct_explicit(self):
        import datetime

        from google.cloud.logging import Resource, StructEntry

        STRUCT = {"message": "Message text", "weather": "partly cloudy"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRY = StructEntry(
            payload=STRUCT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_struct(
            STRUCT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_proto_defaults(self):
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import ProtobufEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        message = Struct(fields={"foo": Value(bool_value=True)})
        ENTRY = ProtobufEntry(payload=message, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_proto(message)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_proto_explicit(self):
        import datetime

        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import ProtobufEntry, Resource

        message = Struct(fields={"foo": Value(bool_value=True)})
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRY = ProtobufEntry(
            payload=message,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log_proto(
            message,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_inference_empty(self):
        """
        When calling batch.log with empty input, it should
        call batch.log_empty
        """
        from google.cloud.logging import LogEntry

        ENTRY = LogEntry()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log()
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_inference_text(self):
        """
        When calling batch.log with text input, it should
        call batch.log_text
        """
        from google.cloud.logging import TextEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        ENTRY = TextEntry(payload=TEXT, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log(TEXT)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_inference_struct(self):
        """
        When calling batch.struct with text input, it should
        call batch.log_struct
        """
        from google.cloud.logging import StructEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        STRUCT = {"message": "Message text", "weather": "partly cloudy"}
        ENTRY = StructEntry(payload=STRUCT, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log(STRUCT)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_inference_proto(self):
        """
        When calling batch.log with proto input, it should
        call batch.log_proto
        """
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import ProtobufEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        message = Struct(fields={"foo": Value(bool_value=True)})
        ENTRY = ProtobufEntry(payload=message, resource=_GLOBAL_RESOURCE)
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log(message)
        self.assertEqual(batch.entries, [ENTRY])

    def test_log_inference_struct_explicit(self):
        """
        When calling batch.log with struct input, it should
        call batch.log_struct, along with input arguments
        """
        import datetime

        from google.cloud.logging import Resource, StructEntry

        STRUCT = {"message": "Message text", "weather": "partly cloudy"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )
        ENTRY = StructEntry(
            payload=STRUCT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )

        client = _Client(project=self.PROJECT, connection=_make_credentials())
        logger = _Logger()
        batch = self._make_one(logger, client=client)
        batch.log(
            STRUCT,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
        )
        self.assertEqual(batch.entries, [ENTRY])

    def test_commit_w_unknown_entry_type(self):
        from google.cloud.logging import LogEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        logger = _Logger()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        api = client.logging_api = _DummyLoggingAPI()
        batch = self._make_one(logger, client)
        batch.entries.append(LogEntry(severity="blah"))
        ENTRY = {"severity": "BLAH", "resource": _GLOBAL_RESOURCE._to_dict()}

        batch.commit()

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with,
            ([ENTRY], logger.full_name, None, None, True),
        )

    def test_commit_w_lowercase_severity_type(self):
        from google.cloud.logging import LogEntry
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        logger = _Logger()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        api = client.logging_api = _DummyLoggingAPI()
        batch = self._make_one(logger, client)
        batch.entries.append(LogEntry(severity="info"))
        batch.entries.append(LogEntry(severity="warn"))
        batch.entries.append(LogEntry(severity="error"))
        batch.entries.append(LogEntry(severity="fatal"))
        ENTRIES = [
            {"severity": "INFO", "resource": _GLOBAL_RESOURCE._to_dict()},
            {"severity": "WARN", "resource": _GLOBAL_RESOURCE._to_dict()},
            {"severity": "ERROR", "resource": _GLOBAL_RESOURCE._to_dict()},
            {"severity": "FATAL", "resource": _GLOBAL_RESOURCE._to_dict()},
        ]

        batch.commit()
        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, None, None, True),
        )

    def test_commit_w_resource_specified(self):
        from google.cloud.logging import Resource
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        logger = _Logger()
        client = _Client(project=self.PROJECT, connection=_make_credentials())
        api = client.logging_api = _DummyLoggingAPI()
        RESOURCE = Resource(
            type="gae_app", labels={"module_id": "default", "version_id": "test"}
        )

        batch = self._make_one(logger, client, resource=RESOURCE)
        MESSAGE = "This is the entry text"
        ENTRIES = [
            {"textPayload": MESSAGE},
            {"textPayload": MESSAGE, "resource": _GLOBAL_RESOURCE._to_dict()},
        ]
        batch.log_text(MESSAGE, resource=None)
        batch.log_text(MESSAGE)
        batch.commit()
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, RESOURCE._to_dict(), None, True),
        )

    def test_commit_w_bound_client(self):
        import datetime
        import json

        from google.cloud._helpers import _datetime_to_rfc3339
        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        message = Struct(fields={"foo": Value(bool_value=True)})
        IID1 = "IID1"
        IID2 = "IID2"
        IID3 = "IID3"
        TIMESTAMP1 = datetime.datetime(2016, 12, 31, 0, 0, 1, 999999)
        TIMESTAMP2 = datetime.datetime(2016, 12, 31, 0, 0, 2, 999999)
        TIMESTAMP3 = datetime.datetime(2016, 12, 31, 0, 0, 3, 999999)
        TRACE1 = "12345678-1234-5678-1234-567812345678"
        TRACE2 = "12345678-1234-5678-1234-567812345679"
        TRACE3 = "12345678-1234-5678-1234-567812345670"
        SPANID1 = "000000000000004a"
        SPANID2 = "000000000000004b"
        SPANID3 = "000000000000004c"
        ENTRIES = [
            {
                "textPayload": TEXT,
                "insertId": IID1,
                "timestamp": _datetime_to_rfc3339(TIMESTAMP1),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "trace": TRACE1,
                "spanId": SPANID1,
                "traceSampled": True,
            },
            {
                "jsonPayload": STRUCT,
                "insertId": IID2,
                "timestamp": _datetime_to_rfc3339(TIMESTAMP2),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "trace": TRACE2,
                "spanId": SPANID2,
                "traceSampled": False,
            },
            {
                "protoPayload": json.loads(MessageToJson(message)),
                "insertId": IID3,
                "timestamp": _datetime_to_rfc3339(TIMESTAMP3),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "trace": TRACE3,
                "spanId": SPANID3,
                "traceSampled": True,
            },
        ]
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = _Logger()
        batch = self._make_one(logger, client=client)

        batch.log_text(
            TEXT,
            insert_id=IID1,
            timestamp=TIMESTAMP1,
            trace=TRACE1,
            span_id=SPANID1,
            trace_sampled=True,
        )
        batch.log_struct(
            STRUCT,
            insert_id=IID2,
            timestamp=TIMESTAMP2,
            trace=TRACE2,
            span_id=SPANID2,
            trace_sampled=False,
        )
        batch.log_proto(
            message,
            insert_id=IID3,
            timestamp=TIMESTAMP3,
            trace=TRACE3,
            span_id=SPANID3,
            trace_sampled=True,
        )
        batch.commit()

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, None, None, True),
        )

    def test_commit_w_alternate_client(self):
        import json

        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import Logger
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        message = Struct(fields={"foo": Value(bool_value=True)})
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.logging_api = _DummyLoggingAPI()
        logger = Logger("logger_name", client1, labels=DEFAULT_LABELS)
        ENTRIES = [
            {
                "textPayload": TEXT,
                "labels": LABELS,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "jsonPayload": STRUCT,
                "severity": SEVERITY,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "protoPayload": json.loads(MessageToJson(message)),
                "httpRequest": REQUEST,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
        ]
        batch = self._make_one(logger, client=client1)

        batch.log_text(TEXT, labels=LABELS)
        batch.log_struct(STRUCT, severity=SEVERITY)
        batch.log_proto(message, http_request=REQUEST)
        batch.commit(client=client2, partial_success=False)

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, None, DEFAULT_LABELS, False),
        )

    def test_context_mgr_success(self):
        import json

        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import Logger
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        message = Struct(fields={"foo": Value(bool_value=True)})
        DEFAULT_LABELS = {"foo": "spam"}
        LABELS = {"foo": "bar", "baz": "qux"}
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = Logger("logger_name", client, labels=DEFAULT_LABELS)
        ENTRIES = [
            {
                "textPayload": TEXT,
                "httpRequest": REQUEST,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "jsonPayload": STRUCT,
                "labels": LABELS,
                "resource": _GLOBAL_RESOURCE._to_dict(),
            },
            {
                "protoPayload": json.loads(MessageToJson(message)),
                "resource": _GLOBAL_RESOURCE._to_dict(),
                "severity": SEVERITY,
            },
        ]
        batch = self._make_one(logger, client=client)

        with batch as other:
            other.log_text(TEXT, http_request=REQUEST)
            other.log_struct(STRUCT, labels=LABELS)
            other.log_proto(message, severity=SEVERITY)

        self.assertEqual(list(batch.entries), [])
        self.assertEqual(
            api._write_entries_called_with,
            (ENTRIES, logger.full_name, None, DEFAULT_LABELS, True),
        )

    def test_context_mgr_failure(self):
        import datetime

        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import ProtobufEntry, StructEntry, TextEntry

        TEXT = "This is the entry text"
        STRUCT = {"message": TEXT, "weather": "partly cloudy"}
        LABELS = {"foo": "bar", "baz": "qux"}
        IID = "IID"
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        TIMESTAMP = datetime.datetime(2016, 12, 31, 0, 1, 2, 999999)
        message = Struct(fields={"foo": Value(bool_value=True)})
        client = _Client(project=self.PROJECT)
        api = client.logging_api = _DummyLoggingAPI()
        logger = _Logger()
        UNSENT = [
            TextEntry(payload=TEXT, insert_id=IID, timestamp=TIMESTAMP),
            StructEntry(payload=STRUCT, severity=SEVERITY),
            ProtobufEntry(payload=message, labels=LABELS, http_request=REQUEST),
        ]
        batch = self._make_one(logger, client=client)

        try:
            with batch as other:
                other.log_text(TEXT, insert_id=IID, timestamp=TIMESTAMP)
                other.log_struct(STRUCT, severity=SEVERITY)
                other.log_proto(message, labels=LABELS, http_request=REQUEST)
                raise _Bugout()
        except _Bugout:
            pass

        self.assertEqual(list(batch.entries), UNSENT)
        self.assertIsNone(api._write_entries_called_with)

    def test_append_context_to_error(self):
        """
        If an InvalidArgument exception contains info on the log that threw it,
        we should be able to add it to the exceptiom message. If not, the
        exception should be unchanged
        """
        from google.api_core.exceptions import InvalidArgument
        from google.rpc.error_details_pb2 import DebugInfo

        from google.cloud.logging import TextEntry

        logger = _Logger()
        client = _Client(project=self.PROJECT)
        batch = self._make_one(logger, client=client)
        test_entries = [TextEntry(payload=str(i)) for i in range(11)]
        batch.entries = test_entries
        starting_message = "test"
        # test that properly formatted exceptions add log details
        for idx, entry in enumerate(test_entries):
            api_entry = entry.to_api_repr()
            err = InvalidArgument(
                starting_message, details=["padding", DebugInfo(detail=f"key: {idx}")]
            )
            batch._append_context_to_error(err)
            self.assertEqual(err.message, f"{starting_message}: {str(api_entry)}...")
            self.assertIn(str(idx), str(entry))
        # test with missing debug info
        err = InvalidArgument(starting_message, details=[])
        batch._append_context_to_error(err)
        self.assertEqual(
            err.message, starting_message, "message should have been unchanged"
        )
        # test with missing key
        err = InvalidArgument(
            starting_message, details=["padding", DebugInfo(detail="no k e y here")]
        )
        batch._append_context_to_error(err)
        self.assertEqual(
            err.message, starting_message, "message should have been unchanged"
        )
        # test with key out of range
        err = InvalidArgument(
            starting_message, details=["padding", DebugInfo(detail="key: 100")]
        )
        batch._append_context_to_error(err)
        self.assertEqual(
            err.message, starting_message, "message should have been unchanged"
        )

    def test_batch_error_gets_context(self):
        """
        Simulate an InvalidArgument sent as part of a batch commit, to ensure
        _append_context_to_error is thrown
        """
        from google.api_core.exceptions import InvalidArgument
        from google.rpc.error_details_pb2 import DebugInfo

        from google.cloud.logging import TextEntry

        logger = _Logger()
        client = _Client(project=self.PROJECT)
        starting_message = "hello"
        exception = InvalidArgument(
            starting_message, details=[DebugInfo(detail="key: 1")]
        )
        client.logging_api = _DummyLoggingExceptionAPI(exception)
        batch = self._make_one(logger, client=client)
        test_entries = [TextEntry(payload=str(i)) for i in range(11)]
        batch.entries = test_entries
        with self.assertRaises(InvalidArgument) as e:
            batch.commit()
            expected_log = test_entries[1]
            api_entry = expected_log.to_api_repr()
            self.assertEqual(e.message, f"{starting_message}: {str(api_entry)}...")


class _Logger(object):
    labels = None

    def __init__(self, name="NAME", project="PROJECT"):
        self.full_name = "projects/%s/logs/%s" % (project, name)


class _DummyLoggingAPI(object):
    _write_entries_called_with = None

    def write_entries(
        self,
        entries,
        *,
        logger_name=None,
        resource=None,
        labels=None,
        partial_success=False,
    ):
        self._write_entries_called_with = (
            entries,
            logger_name,
            resource,
            labels,
            partial_success,
        )

    def logger_delete(self, logger_name):
        self._logger_delete_called_with = logger_name


class _DummyLoggingExceptionAPI(object):
    def __init__(self, exception):
        self.exception = exception

    def write_entries(
        self,
        entries,
        *,
        logger_name=None,
        resource=None,
        labels=None,
        partial_success=False,
    ):
        raise self.exception

    def logger_delete(self, logger_name):
        raise self.exception


class _Client(object):
    def __init__(self, project, connection=None):
        self.project = project
        self._connection = connection


class _Bugout(Exception):
    pass


class _Connection(object):
    _called_with = None

    def __init__(self, *responses):
        self._responses = responses

    def api_request(self, **kw):
        self._called_with = kw
        response, self._responses = self._responses[0], self._responses[1:]
        return response
