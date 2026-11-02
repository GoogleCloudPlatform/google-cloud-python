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


class Test_logger_name_from_path(unittest.TestCase):
    def _call_fut(self, path, project=None):
        from google.cloud.logging_v2.entries import logger_name_from_path

        return logger_name_from_path(path, project)

    def test_w_simple_name(self):
        LOGGER_NAME = "LOGGER_NAME"
        PROJECT = "my-project-1234"
        PATH = "projects/%s/logs/%s" % (PROJECT, LOGGER_NAME)
        logger_name = self._call_fut(PATH)
        self.assertEqual(logger_name, LOGGER_NAME)

    def test_w_name_w_all_extras(self):
        LOGGER_NAME = "LOGGER_NAME-part.one~part.two%part-three"
        PROJECT = "my-project-1234"
        PATH = "projects/%s/logs/%s" % (PROJECT, LOGGER_NAME)
        logger_name = self._call_fut(PATH)
        self.assertEqual(logger_name, LOGGER_NAME)

    def test_w_wrong_project(self):
        LOGGER_NAME = "LOGGER_NAME"
        IN_PROJECT = "in-project"
        PATH_PROJECT = "path-project"
        PATH = "projects/%s/logs/%s" % (PATH_PROJECT, LOGGER_NAME)
        with self.assertRaises(ValueError):
            self._call_fut(PATH, IN_PROJECT)

    def test_invalid_inputs(self):
        invalid_list = [
            "",
            "abc/123/logs/456",
            "projects//logs/",
            "projects/123/logs",
            "projects/123logs/",
            "projects123/logs",
            "project/123",
            "projects123logs456",
            "/logs/123",
        ]
        for path in invalid_list:
            with self.assertRaises(ValueError):
                self._call_fut(path)


class Test__int_or_none(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud.logging_v2.entries import _int_or_none

        return _int_or_none(value)

    def test_w_none(self):
        self.assertIsNone(self._call_fut(None))

    def test_w_int(self):
        self.assertEqual(self._call_fut(123), 123)

    def test_w_str(self):
        self.assertEqual(self._call_fut("123"), 123)


class TestLogEntry(unittest.TestCase):
    PROJECT = "PROJECT"
    LOGGER_NAME = "LOGGER_NAME"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import LogEntry

        return LogEntry

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        from google.cloud.logging_v2.entries import _GLOBAL_RESOURCE

        entry = self._make_one()

        self.assertIsNone(entry.log_name)
        self.assertIsNone(entry.logger)
        self.assertIsNone(entry.labels)
        self.assertIsNone(entry.insert_id)
        self.assertIsNone(entry.severity)
        self.assertIsNone(entry.http_request)
        self.assertIsNone(entry.timestamp)
        self.assertIs(entry.resource, _GLOBAL_RESOURCE)
        self.assertIsNone(entry.trace)
        self.assertIsNone(entry.span_id)
        self.assertIsNone(entry.trace_sampled)
        self.assertIsNone(entry.source_location)
        self.assertIsNone(entry.operation)
        self.assertIsNone(entry.payload)

    def test_ctor_explicit(self):
        import datetime

        from google.cloud.logging import Resource

        LOG_NAME = "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        IID = "IID"
        TIMESTAMP = datetime.datetime.now()
        LABELS = {"foo": "bar", "baz": "qux"}
        SEVERITY = "CRITICAL"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = "500"
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        resource = Resource(type="global", labels={})
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        FILE = "my_file.py"
        LINE_NO = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": LINE_NO, "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        logger = _Logger(self.LOGGER_NAME, self.PROJECT)

        entry = self._make_one(
            log_name=LOG_NAME,
            logger=logger,
            insert_id=IID,
            timestamp=TIMESTAMP,
            labels=LABELS,
            severity=SEVERITY,
            http_request=REQUEST,
            resource=resource,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
            source_location=SOURCE_LOCATION,
            operation=OPERATION,
        )

        self.assertEqual(entry.log_name, LOG_NAME)
        self.assertIs(entry.logger, logger)
        self.assertEqual(entry.insert_id, IID)
        self.assertEqual(entry.timestamp, TIMESTAMP)
        self.assertEqual(entry.labels, LABELS)
        self.assertEqual(entry.severity, SEVERITY)
        self.assertEqual(entry.http_request["requestMethod"], METHOD)
        self.assertEqual(entry.http_request["requestUrl"], URI)
        self.assertEqual(entry.http_request["status"], STATUS)
        self.assertEqual(entry.resource, resource)
        self.assertEqual(entry.trace, TRACE)
        self.assertEqual(entry.span_id, SPANID)
        self.assertTrue(entry.trace_sampled)

        source_location = entry.source_location
        self.assertEqual(source_location["file"], FILE)
        self.assertEqual(source_location["line"], LINE_NO)
        self.assertEqual(source_location["function"], FUNCTION)

        self.assertEqual(entry.operation, OPERATION)
        self.assertIsNone(entry.payload)

    def test_from_api_repr_missing_data_no_loggers(self):
        client = _Client(self.PROJECT)
        LOG_NAME = "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        API_REPR = {"logName": LOG_NAME}
        klass = self._get_target_class()

        entry = klass.from_api_repr(API_REPR, client)

        self.assertEqual(entry.log_name, LOG_NAME)
        logger = entry.logger
        self.assertIsInstance(logger, _Logger)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertIsNone(entry.insert_id)
        self.assertIsNone(entry.timestamp)
        self.assertIsNone(entry.severity)
        self.assertIsNone(entry.http_request)
        self.assertIsNone(entry.trace)
        self.assertIsNone(entry.span_id)
        self.assertIsNone(entry.trace_sampled)
        self.assertIsNone(entry.source_location)
        self.assertIsNone(entry.operation)
        self.assertIs(logger.client, client)
        self.assertIsNone(entry.payload)

    def test_from_api_repr_w_loggers_no_logger_match(self):
        from datetime import datetime, timezone

        from google.cloud.logging import Resource

        klass = self._get_target_class()
        client = _Client(self.PROJECT)
        SEVERITY = "CRITICAL"
        IID = "IID"
        NOW = datetime.now(timezone.utc)
        TIMESTAMP = _datetime_to_rfc3339_w_nanos(NOW)
        LOG_NAME = "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        LABELS = {"foo": "bar", "baz": "qux"}
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        RESOURCE = Resource(
            type="gae_app",
            labels={
                "type": "gae_app",
                "labels": {"module_id": "default", "version": "test"},
            },
        )
        STATUS = "500"
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        FILE = "my_file.py"
        LINE_NO = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": str(LINE_NO), "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        API_REPR = {
            "logName": LOG_NAME,
            "insertId": IID,
            "timestamp": TIMESTAMP,
            "labels": LABELS,
            "severity": SEVERITY,
            "httpRequest": {
                "requestMethod": METHOD,
                "requestUrl": URI,
                "status": STATUS,
            },
            "resource": RESOURCE._to_dict(),
            "trace": TRACE,
            "spanId": SPANID,
            "traceSampled": True,
            "sourceLocation": SOURCE_LOCATION,
            "operation": OPERATION,
        }
        loggers = {}

        entry = klass.from_api_repr(API_REPR, client, loggers=loggers)

        self.assertEqual(entry.log_name, LOG_NAME)
        logger = entry.logger
        self.assertIsInstance(logger, _Logger)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertEqual(entry.insert_id, IID)
        self.assertEqual(entry.timestamp, NOW)
        self.assertIsNone(entry.received_timestamp)
        self.assertEqual(entry.labels, LABELS)
        self.assertEqual(entry.severity, SEVERITY)
        self.assertEqual(entry.http_request["requestMethod"], METHOD)
        self.assertEqual(entry.http_request["requestUrl"], URI)
        self.assertEqual(entry.http_request["status"], STATUS)
        self.assertIs(logger.client, client)
        self.assertEqual(logger.name, self.LOGGER_NAME)
        self.assertEqual(loggers, {LOG_NAME: logger})
        self.assertEqual(entry.resource, RESOURCE)
        self.assertEqual(entry.trace, TRACE)
        self.assertEqual(entry.span_id, SPANID)
        self.assertTrue(entry.trace_sampled)

        source_location = entry.source_location
        self.assertEqual(source_location["file"], FILE)
        self.assertEqual(source_location["line"], LINE_NO)
        self.assertEqual(source_location["function"], FUNCTION)

        self.assertEqual(entry.operation, OPERATION)
        self.assertIsNone(entry.payload)

    def test_from_api_repr_w_loggers_w_logger_match(self):
        from datetime import datetime, timedelta, timezone

        client = _Client(self.PROJECT)
        IID = "IID"
        NOW = datetime.now(timezone.utc)
        LATER = NOW + timedelta(seconds=1)
        TIMESTAMP = _datetime_to_rfc3339_w_nanos(NOW)
        RECEIVED = _datetime_to_rfc3339_w_nanos(LATER)
        LOG_NAME = "projects/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        LABELS = {"foo": "bar", "baz": "qux"}
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        FILE = "my_file.py"
        LINE_NO = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": str(LINE_NO), "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        API_REPR = {
            "logName": LOG_NAME,
            "insertId": IID,
            "timestamp": TIMESTAMP,
            "receiveTimestamp": RECEIVED,
            "labels": LABELS,
            "trace": TRACE,
            "spanId": SPANID,
            "traceSampled": True,
            "sourceLocation": SOURCE_LOCATION,
            "operation": OPERATION,
        }
        LOGGER = object()
        loggers = {LOG_NAME: LOGGER}
        klass = self._get_target_class()

        entry = klass.from_api_repr(API_REPR, client, loggers=loggers)

        self.assertEqual(entry.log_name, LOG_NAME)
        self.assertIs(entry.logger, LOGGER)
        self.assertEqual(entry.insert_id, IID)
        self.assertEqual(entry.timestamp, NOW)
        self.assertEqual(entry.received_timestamp, LATER)
        self.assertEqual(entry.labels, LABELS)
        self.assertEqual(entry.trace, TRACE)
        self.assertEqual(entry.span_id, SPANID)
        self.assertTrue(entry.trace_sampled)

        source_location = entry.source_location
        self.assertEqual(source_location["file"], FILE)
        self.assertEqual(source_location["line"], LINE_NO)
        self.assertEqual(source_location["function"], FUNCTION)

        self.assertEqual(entry.operation, OPERATION)
        self.assertIsNone(entry.payload)

    def test_from_api_repr_w_folder_path(self):
        from datetime import datetime, timedelta, timezone

        client = _Client(self.PROJECT)
        IID = "IID"
        NOW = datetime.now(timezone.utc)
        LATER = NOW + timedelta(seconds=1)
        TIMESTAMP = _datetime_to_rfc3339_w_nanos(NOW)
        RECEIVED = _datetime_to_rfc3339_w_nanos(LATER)
        LOG_NAME = "folders/%s/logs/%s" % (self.PROJECT, self.LOGGER_NAME)
        LABELS = {"foo": "bar", "baz": "qux"}
        TRACE = "12345678-1234-5678-1234-567812345678"
        SPANID = "000000000000004a"
        FILE = "my_file.py"
        LINE_NO = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": str(LINE_NO), "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        API_REPR = {
            "logName": LOG_NAME,
            "insertId": IID,
            "timestamp": TIMESTAMP,
            "receiveTimestamp": RECEIVED,
            "labels": LABELS,
            "trace": TRACE,
            "spanId": SPANID,
            "traceSampled": True,
            "sourceLocation": SOURCE_LOCATION,
            "operation": OPERATION,
        }
        klass = self._get_target_class()

        entry = klass.from_api_repr(API_REPR, client)

        self.assertEqual(entry.log_name, LOG_NAME)
        self.assertIsNone(entry.logger)
        self.assertEqual(entry.insert_id, IID)
        self.assertEqual(entry.timestamp, NOW)
        self.assertEqual(entry.received_timestamp, LATER)
        self.assertEqual(entry.labels, LABELS)
        self.assertEqual(entry.trace, TRACE)
        self.assertEqual(entry.span_id, SPANID)
        self.assertTrue(entry.trace_sampled)

        source_location = entry.source_location
        self.assertEqual(source_location["file"], FILE)
        self.assertEqual(source_location["line"], LINE_NO)
        self.assertEqual(source_location["function"], FUNCTION)

        self.assertEqual(entry.operation, OPERATION)
        self.assertIsNone(entry.payload)

    def test_to_api_repr_w_source_location_no_line(self):
        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        LOG_NAME = "test.log"
        FILE = "my_file.py"
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "function": FUNCTION}
        entry = self._make_one(log_name=LOG_NAME, source_location=SOURCE_LOCATION)
        expected = {
            "logName": LOG_NAME,
            "resource": _GLOBAL_RESOURCE._to_dict(),
            "sourceLocation": {"file": FILE, "line": "0", "function": FUNCTION},
        }
        self.assertEqual(entry.to_api_repr(), expected)

    def test_to_api_repr_explicit(self):
        import datetime

        from google.cloud._helpers import _datetime_to_rfc3339

        from google.cloud.logging import Resource

        LOG_NAME = "test.log"
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
        FILE = "my_file.py"
        LINE = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": LINE, "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        expected = {
            "logName": LOG_NAME,
            "labels": LABELS,
            "insertId": IID,
            "severity": SEVERITY,
            "httpRequest": REQUEST,
            "timestamp": _datetime_to_rfc3339(TIMESTAMP),
            "resource": RESOURCE._to_dict(),
            "trace": TRACE,
            "spanId": SPANID,
            "traceSampled": True,
            "sourceLocation": {"file": FILE, "line": str(LINE), "function": FUNCTION},
            "operation": OPERATION,
        }
        entry = self._make_one(
            log_name=LOG_NAME,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
            source_location=SOURCE_LOCATION,
            operation=OPERATION,
        )

        self.assertEqual(entry.to_api_repr(), expected)


class TestTextEntry(unittest.TestCase):
    PROJECT = "PROJECT"
    LOGGER_NAME = "LOGGER_NAME"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import TextEntry

        return TextEntry

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_to_api_repr_defaults(self):
        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        LOG_NAME = "test.log"
        TEXT = "TESTING"
        entry = self._make_one(log_name=LOG_NAME, payload=TEXT)
        expected = {
            "logName": LOG_NAME,
            "textPayload": TEXT,
            "resource": _GLOBAL_RESOURCE._to_dict(),
        }
        self.assertEqual(entry.to_api_repr(), expected)

    def test_to_api_repr_explicit(self):
        import datetime

        from google.cloud._helpers import _datetime_to_rfc3339

        from google.cloud.logging import Resource

        LOG_NAME = "test.log"
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
        FILE = "my_file.py"
        LINE = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": LINE, "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        expected = {
            "logName": LOG_NAME,
            "textPayload": TEXT,
            "labels": LABELS,
            "insertId": IID,
            "severity": SEVERITY,
            "httpRequest": REQUEST,
            "timestamp": _datetime_to_rfc3339(TIMESTAMP),
            "resource": RESOURCE._to_dict(),
            "trace": TRACE,
            "spanId": SPANID,
            "traceSampled": True,
            "sourceLocation": {"file": FILE, "line": str(LINE), "function": FUNCTION},
            "operation": OPERATION,
        }
        entry = self._make_one(
            log_name=LOG_NAME,
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
            source_location=SOURCE_LOCATION,
            operation=OPERATION,
        )

        self.assertEqual(entry.to_api_repr(), expected)


class TestStructEntry(unittest.TestCase):
    PROJECT = "PROJECT"
    LOGGER_NAME = "LOGGER_NAME"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import StructEntry

        return StructEntry

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_to_api_repr_defaults(self):
        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        LOG_NAME = "test.log"
        JSON_PAYLOAD = {"key": "value"}
        entry = self._make_one(log_name=LOG_NAME, payload=JSON_PAYLOAD)
        expected = {
            "logName": LOG_NAME,
            "jsonPayload": JSON_PAYLOAD,
            "resource": _GLOBAL_RESOURCE._to_dict(),
        }
        self.assertEqual(entry.to_api_repr(), expected)

    def test_to_api_repr_struct(self):
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        LOG_NAME = "struct.log"
        message = Struct(fields={"foo": Value(bool_value=True)})
        entry = self._make_one(log_name=LOG_NAME, payload=message)
        expected = {
            "logName": LOG_NAME,
            "jsonPayload": message,
            "resource": _GLOBAL_RESOURCE._to_dict(),
        }
        self.assertEqual(entry.to_api_repr(), expected)

    def test_to_api_repr_explicit(self):
        import datetime

        from google.cloud._helpers import _datetime_to_rfc3339

        from google.cloud.logging import Resource

        LOG_NAME = "test.log"
        JSON_PAYLOAD = {"key": "value"}
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
        FILE = "my_file.py"
        LINE = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": LINE, "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        expected = {
            "logName": LOG_NAME,
            "jsonPayload": JSON_PAYLOAD,
            "labels": LABELS,
            "insertId": IID,
            "severity": SEVERITY,
            "httpRequest": REQUEST,
            "timestamp": _datetime_to_rfc3339(TIMESTAMP),
            "resource": RESOURCE._to_dict(),
            "trace": TRACE,
            "spanId": SPANID,
            "traceSampled": True,
            "sourceLocation": {"file": FILE, "line": str(LINE), "function": FUNCTION},
            "operation": OPERATION,
        }
        entry = self._make_one(
            log_name=LOG_NAME,
            payload=JSON_PAYLOAD,
            labels=LABELS,
            insert_id=IID,
            severity=SEVERITY,
            http_request=REQUEST,
            timestamp=TIMESTAMP,
            resource=RESOURCE,
            trace=TRACE,
            span_id=SPANID,
            trace_sampled=True,
            source_location=SOURCE_LOCATION,
            operation=OPERATION,
        )

        self.assertEqual(entry.to_api_repr(), expected)


class TestProtobufEntry(unittest.TestCase):
    PROJECT = "PROJECT"
    LOGGER_NAME = "LOGGER_NAME"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import ProtobufEntry

        return ProtobufEntry

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_constructor_basic(self):
        payload = {"foo": "bar"}

        pb_entry = self._make_one(payload=payload, logger=mock.sentinel.logger)

        self.assertIs(pb_entry.payload, payload)
        self.assertIsNone(pb_entry.payload_pb)
        self.assertIs(pb_entry.payload_json, payload)
        self.assertIs(pb_entry.logger, mock.sentinel.logger)
        self.assertIsNone(pb_entry.insert_id)
        self.assertIsNone(pb_entry.timestamp)
        self.assertIsNone(pb_entry.labels)
        self.assertIsNone(pb_entry.severity)
        self.assertIsNone(pb_entry.http_request)
        self.assertIsNone(pb_entry.trace)
        self.assertIsNone(pb_entry.span_id)
        self.assertIsNone(pb_entry.trace_sampled)
        self.assertIsNone(pb_entry.source_location)

    def test_constructor_with_any(self):
        from google.protobuf.any_pb2 import Any

        payload = Any()

        pb_entry = self._make_one(payload=payload, logger=mock.sentinel.logger)

        self.assertIs(pb_entry.payload, payload)
        self.assertIs(pb_entry.payload_pb, payload)
        self.assertIsNone(pb_entry.payload_json)
        self.assertIs(pb_entry.logger, mock.sentinel.logger)
        self.assertIsNone(pb_entry.insert_id)
        self.assertIsNone(pb_entry.timestamp)
        self.assertIsNone(pb_entry.labels)
        self.assertIsNone(pb_entry.severity)
        self.assertIsNone(pb_entry.http_request)
        self.assertIsNone(pb_entry.trace)
        self.assertIsNone(pb_entry.span_id)
        self.assertIsNone(pb_entry.trace_sampled)
        self.assertIsNone(pb_entry.source_location)

    def test_parse_message(self):
        import json

        from google.protobuf.json_format import MessageToJson
        from google.protobuf.struct_pb2 import Struct, Value

        message = Struct(fields={"foo": Value(bool_value=False)})
        with_true = Struct(fields={"foo": Value(bool_value=True)})
        payload = json.loads(MessageToJson(with_true))
        entry = self._make_one(payload=payload, logger=mock.sentinel.logger)

        entry.parse_message(message)

        self.assertTrue(message.fields["foo"])

    def test_to_api_repr_proto_defaults(self):
        from google.protobuf.json_format import MessageToDict
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        LOG_NAME = "test.log"
        message = Struct(fields={"foo": Value(bool_value=True)})

        entry = self._make_one(log_name=LOG_NAME, payload=message)
        expected = {
            "logName": LOG_NAME,
            "protoPayload": MessageToDict(message),
            "resource": _GLOBAL_RESOURCE._to_dict(),
        }
        self.assertEqual(entry.to_api_repr(), expected)

    def test_to_api_repr_proto_inner_struct_field(self):
        from google.protobuf.json_format import MessageToDict
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        LOG_NAME = "test.log"
        inner_struct = Struct(fields={"foo": Value(string_value="bar")})
        message = Struct(fields={"inner": Value(struct_value=inner_struct)})

        entry = self._make_one(log_name=LOG_NAME, payload=message)
        expected = {
            "logName": LOG_NAME,
            "protoPayload": MessageToDict(message),
            "resource": _GLOBAL_RESOURCE._to_dict(),
        }
        self.assertEqual(entry.to_api_repr(), expected)

    def test_to_api_repr_proto_inner_list_field(self):
        from google.protobuf.json_format import MessageToDict
        from google.protobuf.struct_pb2 import ListValue, Struct, Value

        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        LOG_NAME = "test.log"
        lines = ListValue(
            values=[Value(string_value="line1"), Value(string_value="line2")]
        )
        message = Struct(fields={"lines": Value(list_value=lines)})

        entry = self._make_one(log_name=LOG_NAME, payload=message)
        expected = {
            "logName": LOG_NAME,
            "protoPayload": MessageToDict(message),
            "resource": _GLOBAL_RESOURCE._to_dict(),
        }
        self.assertEqual(entry.to_api_repr(), expected)

    def test_to_api_repr_proto_explicit(self):
        import datetime

        from google.cloud._helpers import _datetime_to_rfc3339
        from google.protobuf.json_format import MessageToDict
        from google.protobuf.struct_pb2 import Struct, Value

        from google.cloud.logging import Resource

        LOG_NAME = "test.log"
        message = Struct(fields={"foo": Value(bool_value=True)})
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
        FILE = "my_file.py"
        LINE = 123
        FUNCTION = "my_function"
        SOURCE_LOCATION = {"file": FILE, "line": LINE, "function": FUNCTION}
        OP_ID = "OP_ID"
        PRODUCER = "PRODUCER"
        OPERATION = {"id": OP_ID, "producer": PRODUCER, "first": True, "last": False}
        expected = {
            "logName": LOG_NAME,
            "protoPayload": MessageToDict(message),
            "labels": LABELS,
            "insertId": IID,
            "severity": SEVERITY,
            "httpRequest": REQUEST,
            "timestamp": _datetime_to_rfc3339(TIMESTAMP),
            "resource": RESOURCE._to_dict(),
            "trace": TRACE,
            "spanId": SPANID,
            "traceSampled": True,
            "sourceLocation": {"file": FILE, "line": str(LINE), "function": FUNCTION},
            "operation": OPERATION,
        }

        entry = self._make_one(
            log_name=LOG_NAME,
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
            source_location=SOURCE_LOCATION,
            operation=OPERATION,
        )

        self.assertEqual(entry.to_api_repr(), expected)


def _datetime_to_rfc3339_w_nanos(value):
    from google.cloud._helpers import _RFC3339_NO_FRACTION

    no_fraction = value.strftime(_RFC3339_NO_FRACTION)
    return "%s.%09dZ" % (no_fraction, value.microsecond * 1000)


class _Logger(object):
    def __init__(self, name, client):
        self.name = name
        self.client = client


class _Client(object):
    def __init__(self, project):
        self.project = project

    def logger(self, name):
        return _Logger(name, self)
