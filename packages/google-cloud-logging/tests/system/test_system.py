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

import logging
import numbers
import os
import sys
import unittest
import uuid
from datetime import datetime, timedelta, timezone

import pytest
from google.api_core.exceptions import (
    BadGateway,
    Conflict,
    InternalServerError,
    NotFound,
    ResourceExhausted,
    RetryError,
    ServiceUnavailable,
    TooManyRequests,
)
from google.cloud._helpers import UTC
from google.protobuf.struct_pb2 import ListValue, NullValue, Struct, Value
from test_utils.retry import RetryErrors, RetryResult
from test_utils.system import unique_resource_id

import google.cloud.logging
from google.cloud.logging_v2 import client
from google.cloud.logging_v2.entries import TextEntry
from google.cloud.logging_v2.handlers import CloudLoggingHandler
from google.cloud.logging_v2.handlers.transports import (
    BackgroundThreadTransport,
    SyncTransport,
)
from google.cloud.logging_v2.resource import Resource

_RESOURCE_ID = unique_resource_id("-")
DEFAULT_FILTER = "logName:syslog AND severity>=INFO"
DEFAULT_DESCRIPTION = "System testing"
_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"
retry_429 = RetryErrors(TooManyRequests)

_ten_mins_ago = datetime.now(timezone.utc) - timedelta(minutes=10)
_time_filter = f'timestamp>="{_ten_mins_ago.strftime(_TIME_FORMAT)}"'


def _consume_entries(logger):
    """Consume all recent log entries from logger iterator.
    :type logger: :class:`~google.cloud.logging.logger.Logger`
    :param logger: A Logger containing entries.
    :rtype: list
    :returns: List of all entries consumed.
    """
    return list(logger.list_entries(filter_=_time_filter))


def _list_entries(logger):
    """Retry-ing list entries in a logger.

    Retry until there are actual results and retry on any
    failures.

    :type logger: :class:`~google.cloud.logging.logger.Logger`
    :param logger: A Logger containing entries.

    :rtype: list
    :returns: List of all entries consumed.
    """
    inner = RetryResult(_has_entries, delay=2, backoff=2, max_tries=6)(_consume_entries)
    outer = RetryErrors(
        (ServiceUnavailable, ResourceExhausted, InternalServerError),
        delay=2,
        backoff=2,
        max_tries=6,
    )(inner)
    return outer(logger)


def _has_entries(result):
    return len(result) > 0


class Config(object):
    """Run-time configuration to be modified at set-up.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """

    CLIENT = None
    HTTP_CLIENT = None
    use_mtls = os.environ.get("GOOGLE_API_USE_MTLS_ENDPOINT", "never")


def setUpModule():
    # Use GOOGLE_CLOUD_PROJECT or PROJECT_ID
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("PROJECT_ID")

    # Check if we have credentials (either via file or environment)
    # google.auth.default() will check GOOGLE_APPLICATION_CREDENTIALS
    has_creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") is not None

    # Guard: Skip the entire module if the environment is not ready
    if not project_id or not has_creds:
        raise unittest.SkipTest(
            "System tests skipped: GOOGLE_CLOUD_PROJECT and "
            "GOOGLE_APPLICATION_CREDENTIALS must be set."
        )

    # Explicitly pass the project to the client
    # This prevents the client from attempting 'discovery' via the metadata server
    Config.CLIENT = client.Client(project=project_id)
    Config.HTTP_CLIENT = client.Client(_use_grpc=False, project=project_id)


# Skip the test cases using bigquery, storage and pubsub clients for mTLS testing.
# Bigquery and storage uses http which doesn't have mTLS support, pubsub doesn't
# have mTLS fix released yet.
# We also need to skip HTTP client test cases because mTLS is only available for
# gRPC clients.
skip_for_mtls = pytest.mark.skipif(
    Config.use_mtls == "always", reason="Skip the test case for mTLS testing"
)


def _cleanup_otel_sdk_modules(f):
    """
    Decorator to delete all references to opentelemetry SDK modules after a
    testcase is run. Test case should import opentelemetry SDK modules inside
    the function. This is to test situations where the opentelemetry SDK
    is not imported at all.
    """

    def wrapped(*args, **kwargs):
        f(*args, **kwargs)

        # Deleting from sys.modules should be good enough in this use case
        for module_name in list(sys.modules.keys()):
            if module_name.startswith("opentelemetry.sdk"):
                sys.modules.pop(module_name)

    return wrapped


class TestLogging(unittest.TestCase):
    JSON_PAYLOAD = {
        "message": "System test: test_log_struct",
        "weather": {
            "clouds": "party or partly",
            "temperature": 70,
            "precipitation": False,
        },
    }
    TYPE_FILTER = 'protoPayload.@type = "{}"'

    def setUp(self):
        self.to_delete = []
        self._handlers_cache = logging.getLogger().handlers[:]

    def tearDown(self):
        retry_not_found = RetryErrors((NotFound), max_tries=4)
        retry_other = RetryErrors((TooManyRequests, RetryError))
        for doomed in self.to_delete:
            try:
                retry_not_found(retry_other(doomed.delete))()
            except AttributeError:
                client, dataset = doomed
                retry_not_found(retry_other(client.delete_dataset))(dataset)
            except NotFound:
                pass
        logging.getLogger().handlers = self._handlers_cache[:]

    @staticmethod
    def _logger_name(prefix):
        return prefix + unique_resource_id("-")

    @staticmethod
    def _to_value(data):
        if data is None:
            return Value(null_value=NullValue.NULL_VALUE)
        elif isinstance(data, numbers.Number):
            return Value(number_value=data)
        elif isinstance(data, str):
            return Value(string_value=data)
        elif isinstance(data, bool):
            return Value(bool_value=data)
        elif isinstance(data, (list, tuple, set)):
            return Value(
                list_value=ListValue(values=(TestLogging._to_value(e) for e in data))
            )
        elif isinstance(data, dict):
            return Value(struct_value=TestLogging._dict_to_struct(data))
        else:
            raise TypeError("Unknown data type: %r" % type(data))

    @staticmethod
    def _dict_to_struct(data):
        return Struct(fields={k: TestLogging._to_value(v) for k, v in data.items()})

    def test_list_entry_with_auditlog(self):
        """
        Test emitting and listing logs containing a google.cloud.audit.AuditLog proto message
        """
        from google.protobuf import descriptor_pool

        from google.cloud.logging_v2 import entries

        pool = descriptor_pool.Default()
        type_name = "google.cloud.audit.AuditLog"
        type_url = "type.googleapis.com/" + type_name
        # Make sure the descriptor is known in the registry.
        # Raises KeyError if unknown
        pool.FindMessageTypeByName(type_name)

        # create log
        audit_dict = {
            "@type": type_url,
            "methodName": "test",
            "resourceName": "test",
            "serviceName": "test",
            "requestMetadata": {"callerIp": "127.0.0.1"},
        }
        audit_struct = self._dict_to_struct(audit_dict)

        gapic_logger = Config.CLIENT.logger(f"audit-proto-{uuid.uuid1()}")
        http_logger = Config.HTTP_CLIENT.logger(f"audit-proto-{uuid.uuid1()}-http")
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            logger.log_proto(audit_struct)

            # retrieve log
            retry = RetryErrors((TooManyRequests, StopIteration), max_tries=8)
            protobuf_entry = retry(lambda: next(logger.list_entries()))()

            self.assertIsInstance(protobuf_entry, entries.ProtobufEntry)
            self.assertIsNone(protobuf_entry.payload_pb)
            self.assertIsInstance(protobuf_entry.payload_json, dict)
            self.assertEqual(protobuf_entry.payload_json["@type"], type_url)
            self.assertEqual(
                protobuf_entry.payload_json["methodName"], audit_dict["methodName"]
            )
            self.assertEqual(
                protobuf_entry.to_api_repr()["protoPayload"]["@type"], type_url
            )
            self.assertEqual(
                protobuf_entry.to_api_repr()["protoPayload"]["methodName"],
                audit_dict["methodName"],
            )
            self.assertEqual(
                protobuf_entry.to_api_repr()["protoPayload"]["requestMetadata"][
                    "callerIp"
                ],
                audit_dict["requestMetadata"]["callerIp"],
            )

    def test_list_entry_with_requestlog(self):
        """
        Test emitting and listing logs containing a google.appengine.logging.v1.RequestLog proto message
        """
        from google.protobuf import descriptor_pool

        from google.cloud.logging_v2 import entries

        pool = descriptor_pool.Default()
        type_name = "google.appengine.logging.v1.RequestLog"
        type_url = "type.googleapis.com/" + type_name
        # Make sure the descriptor is known in the registry.
        # Raises KeyError if unknown
        pool.FindMessageTypeByName(type_name)

        # create log
        req_dict = {
            "@type": type_url,
            "ip": "0.0.0.0",
            "appId": "test",
            "versionId": "test",
            "requestId": "12345",
            "latency": "500.0s",
            "method": "GET",
            "status": 500,
            "resource": "test",
            "httpVersion": "HTTP/1.1",
        }
        req_struct = self._dict_to_struct(req_dict)

        gapic_logger = Config.CLIENT.logger(f"req-proto-{uuid.uuid1()}")
        http_logger = Config.CLIENT.logger(f"req-proto-{uuid.uuid1()}-http")
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            logger.log_proto(req_struct)

            # retrieve log
            retry = RetryErrors((TooManyRequests, StopIteration), max_tries=8)
            protobuf_entry = retry(lambda: next(logger.list_entries()))()

            self.assertIsInstance(protobuf_entry, entries.ProtobufEntry)
            self.assertIsNone(protobuf_entry.payload_pb)
            self.assertIsInstance(protobuf_entry.payload_json, dict)
            self.assertEqual(protobuf_entry.payload_json["@type"], type_url)
            self.assertEqual(
                protobuf_entry.to_api_repr()["protoPayload"]["@type"], type_url
            )

    def test_list_entry_with_auditdata(self):
        """
        Test emitting and listing logs containing a google.iam.v1.logging.AuditData proto message
        """
        from google.protobuf import descriptor_pool

        from google.cloud.logging_v2 import entries

        pool = descriptor_pool.Default()
        type_name = "google.iam.v1.logging.AuditData"
        type_url = "type.googleapis.com/" + type_name
        # Make sure the descriptor is known in the registry.
        # Raises KeyError if unknown
        pool.FindMessageTypeByName(type_name)

        # create log
        req_dict = {"@type": type_url, "policyDelta": {}}
        req_struct = self._dict_to_struct(req_dict)

        logger = Config.CLIENT.logger(f"auditdata-proto-{uuid.uuid1()}")
        logger.log_proto(req_struct)

        # retrieve log
        retry = RetryErrors((TooManyRequests, StopIteration), max_tries=8)
        protobuf_entry = retry(lambda: next(logger.list_entries()))()

        self.assertIsInstance(protobuf_entry, entries.ProtobufEntry)
        self.assertIsNone(protobuf_entry.payload_pb)
        self.assertIsInstance(protobuf_entry.payload_json, dict)
        self.assertEqual(protobuf_entry.payload_json["@type"], type_url)
        self.assertEqual(
            protobuf_entry.to_api_repr()["protoPayload"]["@type"], type_url
        )

    def test_log_text(self):
        TEXT_PAYLOAD = "System test: test_log_text"
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_text"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_text_http"))
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)
            logger.log_text(TEXT_PAYLOAD)
            entries = _list_entries(logger)
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].payload, TEXT_PAYLOAD)
            self.assertTrue(isinstance(entries[0], TextEntry))

    def test_log_text_with_timestamp(self):
        text_payload = "System test: test_log_text_with_timestamp"
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_text_ts"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_text_ts_http"))
        now = datetime.now(timezone.utc)
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)
            logger.log_text(text_payload, timestamp=now)
            entries = _list_entries(logger)
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].payload, text_payload)
            self.assertEqual(entries[0].timestamp, now.replace(tzinfo=UTC))
            self.assertIsInstance(entries[0].received_timestamp, datetime)

    def test_log_text_with_resource(self):
        text_payload = "System test: test_log_text_with_timestamp"

        gapic_logger = Config.CLIENT.logger(self._logger_name("log_text_res"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_text_res_http"))
        now = datetime.now(timezone.utc)
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            resource = Resource(
                type="gae_app",
                labels={"module_id": "default", "version_id": "test", "zone": ""},
            )

            self.to_delete.append(logger)

            logger.log_text(text_payload, timestamp=now, resource=resource)
            entries = _list_entries(logger)
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].payload, text_payload)
            # project_id is output only so we don't want it in assertion
            del entries[0].resource.labels["project_id"]
            self.assertEqual(entries[0].resource, resource)

    def test_log_text_w_metadata(self):
        TEXT_PAYLOAD = "System test: test_log_text"
        INSERT_ID = "INSERTID"
        SEVERITY = "INFO"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = 500
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_text_md"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_text_md_http"))
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)

            logger.log_text(
                TEXT_PAYLOAD,
                insert_id=INSERT_ID,
                severity=SEVERITY,
                http_request=REQUEST,
            )
            entries = _list_entries(logger)

            self.assertEqual(len(entries), 1)

            entry = entries[0]
            self.assertEqual(entry.payload, TEXT_PAYLOAD)
            self.assertEqual(entry.insert_id, INSERT_ID)
            self.assertEqual(entry.severity, SEVERITY)

            request = entry.http_request
            self.assertEqual(request["requestMethod"], METHOD)
            self.assertEqual(request["requestUrl"], URI)
            self.assertEqual(request["status"], STATUS)

    def test_log_struct(self):
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_struct"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_struct_http"))
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)

            logger.log_struct(self.JSON_PAYLOAD)
            entries = _list_entries(logger)

            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].payload, self.JSON_PAYLOAD)

    def test_log_struct_w_metadata(self):
        INSERT_ID = "INSERTID"
        SEVERITY = "INFO"
        METHOD = "POST"
        URI = "https://api.example.com/endpoint"
        STATUS = 500
        REQUEST = {"requestMethod": METHOD, "requestUrl": URI, "status": STATUS}
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_struct_md"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_struct_md_http"))
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)

            logger.log_struct(
                self.JSON_PAYLOAD,
                insert_id=INSERT_ID,
                severity=SEVERITY,
                http_request=REQUEST,
            )
            entries = _list_entries(logger)

            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].payload, self.JSON_PAYLOAD)
            self.assertEqual(entries[0].insert_id, INSERT_ID)
            self.assertEqual(entries[0].severity, SEVERITY)
            request = entries[0].http_request
            self.assertEqual(request["requestMethod"], METHOD)
            self.assertEqual(request["requestUrl"], URI)
            self.assertEqual(request["status"], STATUS)

    def test_log_w_text(self):
        TEXT_PAYLOAD = "System test: test_log_w_text"
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_w_text"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_w_text"))
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)
            logger.log(TEXT_PAYLOAD)
            entries = _list_entries(logger)
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].payload, TEXT_PAYLOAD)

    def test_log_w_struct(self):
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_w_struct"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_w_struct_http"))
        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)

            logger.log(self.JSON_PAYLOAD)
            entries = _list_entries(logger)

            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].payload, self.JSON_PAYLOAD)

    def test_log_empty(self):
        gapic_logger = Config.CLIENT.logger(self._logger_name("log_empty"))
        http_logger = Config.HTTP_CLIENT.logger(self._logger_name("log_empty_http"))

        loggers = (
            [gapic_logger]
            if Config.use_mtls == "always"
            else [gapic_logger, http_logger]
        )
        for logger in loggers:
            self.to_delete.append(logger)

            logger.log()
            entries = _list_entries(logger)

            self.assertEqual(len(entries), 1)
            self.assertIsNone(entries[0].payload)
            self.assertFalse(entries[0].trace_sampled)

    def test_log_struct_logentry_data(self):
        logger = Config.CLIENT.logger(self._logger_name("log_w_struct"))
        self.to_delete.append(logger)

        JSON_PAYLOAD = {
            "message": "System test: test_log_struct_logentry_data",
            "severity": "warning",
            "trace": "123",
            "span_id": "456",
        }
        logger.log(JSON_PAYLOAD)
        entries = _list_entries(logger)

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].payload, JSON_PAYLOAD)
        self.assertEqual(entries[0].severity, "WARNING")
        self.assertEqual(entries[0].trace, JSON_PAYLOAD["trace"])
        self.assertEqual(entries[0].span_id, JSON_PAYLOAD["span_id"])
        self.assertFalse(entries[0].trace_sampled)

    def test_log_handler_async(self):
        LOG_MESSAGE = "It was the worst of times"

        handler_name = self._logger_name("handler_async")
        handler = CloudLoggingHandler(Config.CLIENT, name=handler_name)
        # only create the logger to delete, hidden otherwise
        logger = Config.CLIENT.logger(handler_name)
        self.to_delete.append(logger)

        cloud_logger = logging.getLogger(handler.name)
        cloud_logger.addHandler(handler)
        cloud_logger.warning(LOG_MESSAGE)
        handler.flush()
        entries = _list_entries(logger)
        expected_payload = LOG_MESSAGE
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].payload, expected_payload)

    def test_log_handler_sync(self):
        LOG_MESSAGE = "It was the best of times."

        handler_name = self._logger_name("handler_sync")
        handler = CloudLoggingHandler(
            Config.CLIENT, name=handler_name, transport=SyncTransport
        )

        # only create the logger to delete, hidden otherwise
        logger = Config.CLIENT.logger(handler.name)
        self.to_delete.append(logger)

        LOGGER_NAME = "mylogger"
        cloud_logger = logging.getLogger(LOGGER_NAME)
        cloud_logger.addHandler(handler)
        cloud_logger.warning(LOG_MESSAGE)

        entries = _list_entries(logger)
        expected_payload = LOG_MESSAGE
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].payload, expected_payload)

    def test_handlers_w_extras(self):
        LOG_MESSAGE = "Testing with injected extras."
        LOGGER_NAME = "handler_extras"
        handler_name = self._logger_name(LOGGER_NAME)

        handler = CloudLoggingHandler(
            Config.CLIENT, name=handler_name, transport=SyncTransport
        )

        # only create the logger to delete, hidden otherwise
        logger = Config.CLIENT.logger(handler.name)
        self.to_delete.append(logger)

        cloud_logger = logging.getLogger(LOGGER_NAME)
        cloud_logger.addHandler(handler)
        expected_request = {"requestUrl": "localhost"}
        expected_source = {"file": "test.py"}
        extra = {
            "trace": "123",
            "span_id": "456",
            "trace_sampled": True,
            "http_request": expected_request,
            "source_location": expected_source,
            "resource": Resource(type="global", labels={}),
            "labels": {"test-label": "manual"},
        }
        cloud_logger.warning(LOG_MESSAGE, extra=extra)

        entries = _list_entries(logger)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].trace, extra["trace"])
        self.assertEqual(entries[0].span_id, extra["span_id"])
        self.assertTrue(entries[0].trace_sampled)
        self.assertEqual(entries[0].http_request, expected_request)
        self.assertEqual(
            entries[0].labels, {**extra["labels"], "python_logger": LOGGER_NAME}
        )
        self.assertEqual(entries[0].resource.type, extra["resource"].type)

    def test_handlers_w_json_fields(self):
        LOG_MESSAGE = "Testing with json_field extras."
        LOGGER_NAME = "json_field_extras"
        handler_name = self._logger_name(LOGGER_NAME)

        handler = CloudLoggingHandler(
            Config.CLIENT, name=handler_name, transport=SyncTransport
        )

        # only create the logger to delete, hidden otherwise
        logger = Config.CLIENT.logger(handler.name)
        self.to_delete.append(logger)

        cloud_logger = logging.getLogger(LOGGER_NAME)
        cloud_logger.addHandler(handler)
        extra = {"json_fields": {"hello": "world", "two": 2}}
        cloud_logger.warning(LOG_MESSAGE, extra=extra)

        entries = _list_entries(logger)
        self.assertEqual(len(entries), 1)
        payload = entries[0].payload
        self.assertEqual(payload["message"], LOG_MESSAGE)
        self.assertEqual(payload["hello"], "world")
        self.assertEqual(payload["two"], 2)

    def test_log_root_handler(self):
        LOG_MESSAGE = "It was the best of times."

        handler = CloudLoggingHandler(
            Config.CLIENT, name=self._logger_name("handler_root")
        )
        # only create the logger to delete, hidden otherwise
        logger = Config.CLIENT.logger(handler.name)
        self.to_delete.append(logger)

        google.cloud.logging.handlers.handlers.setup_logging(handler)
        logging.warning(LOG_MESSAGE)

        entries = _list_entries(logger)
        expected_payload = LOG_MESSAGE

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].payload, expected_payload)

    @_cleanup_otel_sdk_modules
    def test_log_handler_otel_integration(self):
        # Doing OTel imports here to not taint the other tests with OTel SDK imports
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider

        LOG_MESSAGE = "This is a test of OpenTelemetry"
        LOGGER_NAME = "otel-integration"
        handler_name = self._logger_name(LOGGER_NAME)

        handler = CloudLoggingHandler(
            Config.CLIENT, name=handler_name, transport=SyncTransport
        )
        # only create the logger to delete, hidden otherwise
        logger = Config.CLIENT.logger(handler.name)
        self.to_delete.append(logger)

        # Set up OTel SDK
        provider = TracerProvider()

        tracer = provider.get_tracer("test_system")
        with tracer.start_as_current_span("test-span") as span:
            context = span.get_span_context()
            expected_trace_id = f"projects/{Config.CLIENT.project}/traces/{trace.format_trace_id(context.trace_id)}"
            expected_span_id = trace.format_span_id(context.span_id)
            expected_tracesampled = context.trace_flags.sampled

            cloud_logger = logging.getLogger(LOGGER_NAME)
            cloud_logger.addHandler(handler)
            cloud_logger.warning(LOG_MESSAGE)

            entries = _list_entries(logger)
            self.assertEqual(len(entries), 1)
            self.assertEqual(entries[0].trace, expected_trace_id)
            self.assertEqual(entries[0].span_id, expected_span_id)
            self.assertTrue(entries[0].trace_sampled, expected_tracesampled)

    def test_log_handler_close(self):
        import multiprocessing

        from google.cloud import logging as cloud_logging  # Ensure import is available

        ctx = multiprocessing.get_context("fork")
        LOG_MESSAGE = "This is a test of handler.close before exiting."
        LOGGER_NAME = "close-test"
        handler_name = self._logger_name(LOGGER_NAME)

        # only create the logger to delete, hidden otherwise
        logger = Config.CLIENT.logger(handler_name)
        self.to_delete.append(logger)

        # Run a simulation of logging an entry then immediately shutting down.
        # The .close() function before the process exits should prevent the
        # thread shutdown error and let us log the message.
        def subprocess_main():
            # Create a fresh client inside the child process to avoid gRPC fork issues.
            # Do not use the shared Config.CLIENT here.
            sub_client = cloud_logging.Client()

            handler = CloudLoggingHandler(
                sub_client, name=handler_name, transport=BackgroundThreadTransport
            )
            cloud_logger = logging.getLogger(LOGGER_NAME)
            cloud_logger.addHandler(handler)
            cloud_logger.warning(LOG_MESSAGE)
            handler.close()

        proc = ctx.Process(target=subprocess_main)
        proc.start()
        proc.join()
        entries = _list_entries(logger)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].payload, LOG_MESSAGE)

    def test_log_client_flush_handlers(self):
        import multiprocessing

        from google.cloud import logging as cloud_logging  # Ensure import is available

        ctx = multiprocessing.get_context("fork")
        LOG_MESSAGE = "This is a test of client.flush_handlers before exiting."
        LOGGER_NAME = "close-test"
        handler_name = self._logger_name(LOGGER_NAME)

        logger = Config.CLIENT.logger(handler_name)
        self.to_delete.append(logger)

        def subprocess_main():
            # Create a fresh client inside the child process to avoid gRPC fork issues.
            # Do not use the shared Config.CLIENT here.
            sub_client = cloud_logging.Client()

            handler = CloudLoggingHandler(
                sub_client, name=handler_name, transport=BackgroundThreadTransport
            )
            cloud_logger = logging.getLogger(LOGGER_NAME)
            cloud_logger.addHandler(handler)
            cloud_logger.warning(LOG_MESSAGE)

            # Flush using the subprocess-local client
            sub_client.flush_handlers()

        proc = ctx.Process(target=subprocess_main)
        proc.start()
        proc.join()

        # The parent's Config.CLIENT remains clean and can now list entries
        entries = _list_entries(logger)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].payload, LOG_MESSAGE)

    def test_create_metric(self):
        METRIC_NAME = "test-create-metric%s" % (_RESOURCE_ID,)
        metric = Config.CLIENT.metric(
            METRIC_NAME, filter_=DEFAULT_FILTER, description=DEFAULT_DESCRIPTION
        )
        self.assertFalse(metric.exists())
        retry = RetryErrors(Conflict)

        retry(metric.create)()

        self.to_delete.append(metric)
        self.assertTrue(metric.exists())

    def test_list_metrics(self):
        METRIC_NAME = "test-list-metrics%s" % (_RESOURCE_ID,)
        metric = Config.CLIENT.metric(
            METRIC_NAME, filter_=DEFAULT_FILTER, description=DEFAULT_DESCRIPTION
        )
        self.assertFalse(metric.exists())
        before_metrics = list(Config.CLIENT.list_metrics())
        before_names = set(before.name for before in before_metrics)
        self.assertFalse(metric.name in before_names)
        retry = RetryErrors(Conflict)
        retry(metric.create)()
        self.to_delete.append(metric)
        self.assertTrue(metric.exists())

        after_metrics = list(Config.CLIENT.list_metrics())

        after_names = set(after.name for after in after_metrics)
        self.assertTrue(metric.name in after_names)

    def test_reload_metric(self):
        METRIC_NAME = "test-reload-metric%s" % (_RESOURCE_ID,)
        retry = RetryErrors(Conflict)
        metric = Config.CLIENT.metric(
            METRIC_NAME, filter_=DEFAULT_FILTER, description=DEFAULT_DESCRIPTION
        )
        self.assertFalse(metric.exists())
        retry(metric.create)()
        self.to_delete.append(metric)
        metric.filter_ = "logName:other"
        metric.description = "local changes"

        metric.reload()

        self.assertEqual(metric.filter_, DEFAULT_FILTER)
        self.assertEqual(metric.description, DEFAULT_DESCRIPTION)

    def test_update_metric(self):
        METRIC_NAME = "test-update-metric%s" % (_RESOURCE_ID,)
        retry = RetryErrors(Conflict)
        NEW_FILTER = "logName:other"
        NEW_DESCRIPTION = "updated"
        metric = Config.CLIENT.metric(
            METRIC_NAME, filter_=DEFAULT_FILTER, description=DEFAULT_DESCRIPTION
        )
        self.assertFalse(metric.exists())
        retry(metric.create)()
        self.to_delete.append(metric)
        metric.filter_ = NEW_FILTER
        metric.description = NEW_DESCRIPTION

        metric.update()

        after_metrics = list(Config.CLIENT.list_metrics())
        after_info = {metric.name: metric for metric in after_metrics}
        after = after_info[METRIC_NAME]
        self.assertEqual(after.filter_, NEW_FILTER)
        self.assertEqual(after.description, NEW_DESCRIPTION)

    def _init_storage_bucket(self):
        from google.cloud import storage

        BUCKET_NAME = "g-c-python-testing%s" % (_RESOURCE_ID,)
        BUCKET_URI = "storage.googleapis.com/%s" % (BUCKET_NAME,)

        # Create the destination bucket, and set up the ACL to allow
        # Stackdriver Logging to write into it.
        retry = RetryErrors((Conflict, TooManyRequests, ServiceUnavailable))
        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)
        retry(bucket.create)()
        self.to_delete.append(bucket)
        bucket.acl.reload()
        logs_group = bucket.acl.group("cloud-logs@google.com")
        logs_group.grant_owner()
        bucket.acl.add_entity(logs_group)
        bucket.acl.save()

        return BUCKET_URI

    @skip_for_mtls
    def test_create_sink_storage_bucket(self):
        uri = self._init_storage_bucket()
        SINK_NAME = "test-create-sink-bucket%s" % (_RESOURCE_ID,)

        retry = RetryErrors((Conflict, ServiceUnavailable), max_tries=10)
        sink = Config.CLIENT.sink(SINK_NAME, filter_=DEFAULT_FILTER, destination=uri)
        self.assertFalse(sink.exists())

        retry(sink.create)()

        self.to_delete.append(sink)
        self.assertTrue(sink.exists())

    @skip_for_mtls
    def test_create_sink_pubsub_topic(self):
        from google.cloud import pubsub_v1

        SINK_NAME = "test-create-sink-topic%s" % (_RESOURCE_ID,)
        TOPIC_NAME = "logging-systest{}".format(unique_resource_id("-"))

        # Create the destination topic, and set up the IAM policy to allow
        # Stackdriver Logging to write into it.
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(Config.CLIENT.project, TOPIC_NAME)
        self.to_delete.append(_DeleteWrapper(publisher, topic_path))
        publisher.create_topic(request={"name": topic_path})

        policy = publisher.get_iam_policy(request={"resource": topic_path})
        policy.bindings.add(role="roles/owner", members=["group:cloud-logs@google.com"])
        publisher.set_iam_policy(request={"resource": topic_path, "policy": policy})

        TOPIC_URI = "pubsub.googleapis.com/%s" % (topic_path,)

        retry = RetryErrors((Conflict, ServiceUnavailable), max_tries=10)
        sink = Config.CLIENT.sink(
            SINK_NAME, filter_=DEFAULT_FILTER, destination=TOPIC_URI
        )
        self.assertFalse(sink.exists())

        retry(sink.create)()

        self.to_delete.append(sink)
        self.assertTrue(sink.exists())

    def _init_bigquery_dataset(self):
        from google.cloud.bigquery.dataset import AccessEntry

        from google.cloud import bigquery

        dataset_name = ("system_testing_dataset" + _RESOURCE_ID).replace("-", "_")
        dataset_uri = "bigquery.googleapis.com/projects/%s/datasets/%s" % (
            Config.CLIENT.project,
            dataset_name,
        )

        # Create the destination dataset, and set up the ACL to allow
        # Stackdriver Logging to write into it.
        retry = RetryErrors((TooManyRequests, BadGateway, ServiceUnavailable))
        bigquery_client = bigquery.Client()
        dataset_ref = bigquery.DatasetReference(Config.CLIENT.project, dataset_name)
        dataset = retry(bigquery_client.create_dataset)(bigquery.Dataset(dataset_ref))
        self.to_delete.append((bigquery_client, dataset))
        bigquery_client.get_dataset(dataset)
        access = AccessEntry("WRITER", "groupByEmail", "cloud-logs@google.com")
        dataset.access_entries.append(access)
        bigquery_client.update_dataset(dataset, ["access_entries"])
        return dataset_uri

    @skip_for_mtls
    def test_create_sink_bigquery_dataset(self):
        SINK_NAME = "test-create-sink-dataset%s" % (_RESOURCE_ID,)
        retry = RetryErrors((Conflict, ServiceUnavailable), max_tries=10)
        uri = self._init_bigquery_dataset()
        sink = Config.CLIENT.sink(SINK_NAME, filter_=DEFAULT_FILTER, destination=uri)
        self.assertFalse(sink.exists())

        retry(sink.create)()

        self.to_delete.append(sink)
        self.assertTrue(sink.exists())

    @skip_for_mtls
    def test_list_sinks(self):
        SINK_NAME = "test-list-sinks%s" % (_RESOURCE_ID,)
        uri = self._init_storage_bucket()
        retry = RetryErrors((Conflict, ServiceUnavailable), max_tries=10)
        sink = Config.CLIENT.sink(SINK_NAME, filter_=DEFAULT_FILTER, destination=uri)
        self.assertFalse(sink.exists())
        before_sinks = list(Config.CLIENT.list_sinks())
        before_names = set(before.name for before in before_sinks)
        self.assertFalse(sink.name in before_names)
        retry(sink.create)()
        self.to_delete.append(sink)
        self.assertTrue(sink.exists())

        after_sinks = list(Config.CLIENT.list_sinks())

        after_names = set(after.name for after in after_sinks)
        self.assertTrue(sink.name in after_names)

    @skip_for_mtls
    def test_reload_sink(self):
        SINK_NAME = "test-reload-sink%s" % (_RESOURCE_ID,)
        retry = RetryErrors((Conflict, ServiceUnavailable), max_tries=10)
        uri = self._init_bigquery_dataset()
        sink = Config.CLIENT.sink(SINK_NAME, filter_=DEFAULT_FILTER, destination=uri)
        self.assertFalse(sink.exists())
        retry(sink.create)()
        self.to_delete.append(sink)
        sink.filter_ = "BOGUS FILTER"
        sink.destination = "BOGUS DESTINATION"

        sink.reload()

        self.assertEqual(sink.filter_, DEFAULT_FILTER)
        self.assertEqual(sink.destination, uri)

    @skip_for_mtls
    def test_update_sink(self):
        SINK_NAME = "test-update-sink%s" % (_RESOURCE_ID,)
        retry = RetryErrors((Conflict, ServiceUnavailable), max_tries=10)
        bucket_uri = self._init_storage_bucket()
        dataset_uri = self._init_bigquery_dataset()
        UPDATED_FILTER = "logName:syslog"
        sink = Config.CLIENT.sink(
            SINK_NAME, filter_=DEFAULT_FILTER, destination=bucket_uri
        )
        self.assertFalse(sink.exists())
        retry(sink.create)()
        self.to_delete.append(sink)
        sink.filter_ = UPDATED_FILTER
        sink.destination = dataset_uri

        sink.update()

        self.assertEqual(sink.filter_, UPDATED_FILTER)
        self.assertEqual(sink.destination, dataset_uri)

    @skip_for_mtls
    def test_api_equality_list_logs(self):
        import google.cloud.logging_v2

        # Skip diagnostic log for this system test
        google.cloud.logging_v2._instrumentation_emitted = True

        unique_id = uuid.uuid1()
        gapic_logger = Config.CLIENT.logger(f"api-list-{unique_id}")
        http_logger = Config.HTTP_CLIENT.logger(f"api-list-{unique_id}")
        # write logs
        log_count = 5
        for i in range(log_count):
            gapic_logger.log_text(f"test {i}")

        def retryable():
            max_results = 3
            gapic_generator = gapic_logger.list_entries(max_results=max_results)
            http_generator = http_logger.list_entries(max_results=max_results)
            # returned objects should be consistent
            self.assertEqual(type(gapic_generator), type(http_generator))
            gapic_list, http_list = list(gapic_generator), list(http_generator)
            # max_results should limit the number of logs returned
            self.assertEqual(len(gapic_list), max_results)
            self.assertEqual(len(http_list), max_results)
            # returned logs should be the same
            self.assertEqual(gapic_list[0].insert_id, http_list[0].insert_id)
            # should return in ascending order
            self.assertEqual(gapic_list[0].payload, "test 0")
            # test reverse ordering
            gapic_generator = gapic_logger.list_entries(
                max_results=max_results, order_by=google.cloud.logging_v2.DESCENDING
            )
            http_generator = http_logger.list_entries(
                max_results=max_results, order_by=google.cloud.logging_v2.DESCENDING
            )
            gapic_list, http_list = list(gapic_generator), list(http_generator)
            self.assertEqual(len(gapic_list), max_results)
            self.assertEqual(len(http_list), max_results)
            # http and gapic results should be consistent
            self.assertEqual(gapic_list[0].insert_id, http_list[0].insert_id)
            # returned logs should be in descending order
            self.assertEqual(gapic_list[0].payload, f"test {log_count - 1}")

        RetryErrors(
            (ServiceUnavailable, InternalServerError, AssertionError),
            delay=2,
            backoff=2,
            max_tries=3,
        )(retryable)()


class _DeleteWrapper(object):
    def __init__(self, publisher, topic_path):
        self.publisher = publisher
        self.topic_path = topic_path

    def delete(self):
        self.publisher.delete_topic(request={"topic": self.topic_path})
