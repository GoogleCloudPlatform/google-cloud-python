# Copyright 2016 Google LLC All Rights Reserved.
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

import pytest


class TestContainerEngineHandler(unittest.TestCase):
    PROJECT = "PROJECT"

    def _get_target_class(self):
        from google.cloud.logging.handlers import ContainerEngineHandler

        return ContainerEngineHandler

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        with pytest.warns(
            DeprecationWarning,
            match="ContainerEngineHandler is deprecated. Use StructuredLogHandler instead",
        ):
            handler = self._make_one()
        self.assertIsNone(handler.name)

    def test_ctor_w_name(self):
        with pytest.warns(
            DeprecationWarning,
            match="ContainerEngineHandler is deprecated. Use StructuredLogHandler instead",
        ):
            handler = self._make_one(name="foo")
        self.assertEqual(handler.name, "foo")

    def test_format(self):
        import json
        import logging

        with pytest.warns(
            DeprecationWarning,
            match="ContainerEngineHandler is deprecated. Use StructuredLogHandler instead",
        ):
            handler = self._make_one()
        logname = "loggername"
        message = "hello world，嗨 世界"
        record = logging.LogRecord(
            logname, logging.INFO, None, None, message, None, None
        )
        record.created = 5.03
        expected_payload = {
            "message": message,
            "timestamp": {"seconds": 5, "nanos": int(0.03 * 1e9)},
            "thread": record.thread,
            "severity": record.levelname,
        }
        with pytest.warns(
            DeprecationWarning,
            match="format_stackdriver_json is deprecated. Use StructuredLogHandler instead",
        ):
            payload = handler.format(record)

        self.assertEqual(payload, json.dumps(expected_payload, ensure_ascii=False))
