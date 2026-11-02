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


class TestSyncHandler(unittest.TestCase):
    PROJECT = "PROJECT"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging.handlers.transports import SyncTransport

        return SyncTransport

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        client = _Client(self.PROJECT)
        NAME = "python_logger"
        transport = self._make_one(client, NAME)
        self.assertEqual(transport.logger.name, "python_logger")

    def test_send(self):
        from google.cloud.logging_v2._helpers import LogSeverity
        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        client = _Client(self.PROJECT)

        client_name = "python"
        python_logger_name = "mylogger"
        transport = self._make_one(client, client_name)
        message = "hello world"
        record = logging.LogRecord(
            python_logger_name, logging.INFO, None, None, message, None, None
        )

        transport.send(record, message, resource=_GLOBAL_RESOURCE)
        EXPECTED_SENT = (
            message,
            LogSeverity.INFO,
            _GLOBAL_RESOURCE,
            {"python_logger": python_logger_name},
            None,
            None,
            None,
        )
        self.assertEqual(transport.logger.log_called_with, EXPECTED_SENT)

    def test_send_struct(self):
        from google.cloud.logging_v2._helpers import LogSeverity
        from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

        client = _Client(self.PROJECT)

        client_name = "python"
        python_logger_name = "mylogger"
        transport = self._make_one(client, client_name)
        message = {"message": "hello world", "extra": "test", "nested": {"one": 2}}
        record = logging.LogRecord(
            python_logger_name, logging.INFO, None, None, message, None, None
        )

        transport.send(record, message, resource=_GLOBAL_RESOURCE)
        EXPECTED_SENT = (
            message,
            LogSeverity.INFO,
            _GLOBAL_RESOURCE,
            {"python_logger": python_logger_name},
            None,
            None,
            None,
        )
        self.assertEqual(transport.logger.log_called_with, EXPECTED_SENT)


class _Logger(object):
    from google.cloud.logging_v2.logger import _GLOBAL_RESOURCE

    def __init__(self, name, resource=_GLOBAL_RESOURCE):
        self.name = name
        self.resource = resource

    def log(
        self,
        message,
        severity=None,
        resource=_GLOBAL_RESOURCE,
        labels=None,
        trace=None,
        span_id=None,
        http_request=None,
    ):
        self.log_called_with = (
            message,
            severity,
            resource,
            labels,
            trace,
            span_id,
            http_request,
        )


class _Client(object):
    def __init__(self, project):
        self.project = project

    def logger(self, name, resource=None):  # pylint: disable=unused-argument
        self._logger = _Logger(name, resource=resource)
        return self._logger


class _Handler(object):
    def __init__(self, level):
        self.level = level  # pragma: NO COVER

    def acquire(self):
        pass  # pragma: NO COVER

    def release(self):
        pass  # pragma: NO COVER
