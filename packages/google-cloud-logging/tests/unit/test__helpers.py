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
import unittest
from datetime import datetime, timedelta, timezone

import mock


class Test_entry_from_resource(unittest.TestCase):
    @staticmethod
    def _call_fut(resource, client, loggers):
        from google.cloud.logging_v2._helpers import entry_from_resource

        return entry_from_resource(resource, client, loggers)

    def _payload_helper(self, key, class_name):
        import mock

        resource = {}
        if key is not None:
            resource[key] = "yup"
        client = object()
        loggers = {}
        mock_class = EntryMock()

        name = "google.cloud.logging_v2._helpers." + class_name
        with mock.patch(name, new=mock_class):
            result = self._call_fut(resource, client, loggers)

        self.assertIs(result, mock_class.sentinel)
        self.assertEqual(mock_class.called, (resource, client, loggers))

    def test_wo_payload(self):
        self._payload_helper(None, "LogEntry")

    def test_text_payload(self):
        self._payload_helper("textPayload", "TextEntry")

    def test_json_payload(self):
        self._payload_helper("jsonPayload", "StructEntry")

    def test_proto_payload(self):
        self._payload_helper("protoPayload", "ProtobufEntry")


class Test_retrieve_metadata_server(unittest.TestCase):
    @staticmethod
    def _call_fut(metadata_key):
        from google.cloud.logging_v2._helpers import retrieve_metadata_server

        return retrieve_metadata_server(metadata_key)

    def test_metadata_exists(self):
        status_code_ok = 200
        response_text = "my-gke-cluster"
        metadata_key = "test_key"

        response_mock = ResponseMock(status_code=status_code_ok)
        response_mock.text = response_text

        requests_mock = mock.Mock()
        requests_mock.get.return_value = response_mock
        requests_mock.codes.ok = status_code_ok

        patch = mock.patch("google.cloud.logging_v2._helpers.requests", requests_mock)

        with patch:
            metadata = self._call_fut(metadata_key)

        self.assertEqual(metadata, response_text)

    def test_metadata_does_not_exist(self):
        status_code_ok = 200
        status_code_not_found = 404
        metadata_key = "test_key"

        response_mock = ResponseMock(status_code=status_code_not_found)

        requests_mock = mock.Mock()
        requests_mock.get.return_value = response_mock
        requests_mock.codes.ok = status_code_ok

        patch = mock.patch("google.cloud.logging_v2._helpers.requests", requests_mock)

        with patch:
            metadata = self._call_fut(metadata_key)

        self.assertIsNone(metadata)

    def test_request_exception(self):
        import requests

        metadata_key = "test_url_cannot_connect"
        metadata_url = "http://metadata.invalid/"

        requests_get_mock = mock.Mock(spec=["__call__"])
        requests_get_mock.side_effect = requests.exceptions.RequestException

        requests_get_patch = mock.patch("requests.get", requests_get_mock)

        url_patch = mock.patch(
            "google.cloud.logging_v2._helpers.METADATA_URL", new=metadata_url
        )

        with requests_get_patch:
            with url_patch:
                metadata = self._call_fut(metadata_key)

        self.assertIsNone(metadata)


class Test__normalize_severity(unittest.TestCase):
    @staticmethod
    def _stackdriver_severity():
        from google.cloud.logging_v2._helpers import LogSeverity

        return LogSeverity

    def _normalize_severity_helper(self, stdlib_level, enum_level):
        from google.cloud.logging_v2._helpers import _normalize_severity

        self.assertEqual(_normalize_severity(stdlib_level), enum_level)

    def test__normalize_severity_critical(self):
        severity = self._stackdriver_severity()
        self._normalize_severity_helper(logging.CRITICAL, severity.CRITICAL)

    def test__normalize_severity_error(self):
        severity = self._stackdriver_severity()
        self._normalize_severity_helper(logging.ERROR, severity.ERROR)

    def test__normalize_severity_warning(self):
        severity = self._stackdriver_severity()
        self._normalize_severity_helper(logging.WARNING, severity.WARNING)

    def test__normalize_severity_info(self):
        severity = self._stackdriver_severity()
        self._normalize_severity_helper(logging.INFO, severity.INFO)

    def test__normalize_severity_debug(self):
        severity = self._stackdriver_severity()
        self._normalize_severity_helper(logging.DEBUG, severity.DEBUG)

    def test__normalize_severity_notset(self):
        severity = self._stackdriver_severity()
        self._normalize_severity_helper(logging.NOTSET, severity.DEFAULT)

    def test__normalize_severity_non_standard(self):
        unknown_level = 35
        self._normalize_severity_helper(unknown_level, unknown_level)


class Test__add_defaults_to_filter(unittest.TestCase):
    @staticmethod
    def _time_format():
        return "%Y-%m-%dT%H:%M:%S.%f%z"

    @staticmethod
    def _add_defaults_to_filter(filter_):
        from google.cloud.logging_v2._helpers import _add_defaults_to_filter

        return _add_defaults_to_filter(filter_)

    def test_filter_defaults_empty_input(self):
        """Filter should default to return logs < 24 hours old"""
        out_filter = self._add_defaults_to_filter(None)
        timestamp = datetime.strptime(
            out_filter, 'timestamp>="' + self._time_format() + '"'
        )
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        self.assertLess(yesterday - timestamp, timedelta(minutes=1))

    def test_filter_defaults_no_timestamp(self):
        """Filter should append 24 hour timestamp filter to input string"""
        test_inputs = [
            "",
            "  ",
            "logName=/projects/test/test",
            "test1 AND test2 AND test3",
            "time AND stamp  ",
        ]
        for in_filter in test_inputs:
            out_filter = self._add_defaults_to_filter(in_filter)
            self.assertTrue(in_filter in out_filter)
            self.assertTrue("timestamp" in out_filter)

            timestamp = datetime.strptime(
                out_filter, in_filter + ' AND timestamp>="' + self._time_format() + '"'
            )
            yesterday = datetime.now(timezone.utc) - timedelta(days=1)
            self.assertLess(yesterday - timestamp, timedelta(minutes=1))

    def test_filter_defaults_only_timestamp(self):
        """If user inputs a timestamp filter, don't add default"""
        in_filter = "timestamp=test"
        out_filter = self._add_defaults_to_filter(in_filter)
        self.assertEqual(in_filter, out_filter)

    def test_filter_defaults_capitalized_timestamp(self):
        """Should work with capitalized timestamp strings"""
        in_filter = "TIMESTAMP=test"
        out_filter = self._add_defaults_to_filter(in_filter)
        self.assertEqual(in_filter, out_filter)


class EntryMock(object):
    def __init__(self):
        self.sentinel = object()
        self.called = None

    def from_api_repr(self, resource, client, loggers):
        self.called = (resource, client, loggers)
        return self.sentinel


class ResponseMock(object):
    def __init__(self, status_code, text="test_response_text"):
        self.status_code = status_code
        self.text = text
