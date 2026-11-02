# Copyright 2022 Google LLC
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

import google.cloud.logging_v2._instrumentation as i


class TestInstrumentation(unittest.TestCase):
    TEST_NAME = "python"
    # LONG_NAME > 14 characters
    LONG_NAME = TEST_NAME + "789ABCDEF"

    TEST_VERSION = "1.0.0"
    # LONG_VERSION > 16 characters
    LONG_VERSION = TEST_VERSION + "6789ABCDEF12"

    def _get_diagnostic_value(self, entry, key):
        return entry.payload[i._DIAGNOSTIC_INFO_KEY][i._INSTRUMENTATION_SOURCE_KEY][-1][
            key
        ]

    def test_default_diagnostic_info(self):
        entry = i._create_diagnostic_entry()
        self.assertEqual(
            i._PYTHON_LIBRARY_NAME,
            self._get_diagnostic_value(entry, "name"),
        )
        self.assertEqual(
            i._LIBRARY_VERSION, self._get_diagnostic_value(entry, "version")
        )

    def test_custom_diagnostic_info(self):
        entry = i._create_diagnostic_entry(
            name=self.TEST_NAME, version=self.TEST_VERSION
        )
        self.assertEqual(
            self.TEST_NAME,
            self._get_diagnostic_value(entry, "name"),
        )
        self.assertEqual(
            self.TEST_VERSION, self._get_diagnostic_value(entry, "version")
        )

    def test_truncate_long_values(self):
        entry = i._create_diagnostic_entry(
            name=self.LONG_NAME, version=self.LONG_VERSION
        )

        expected_name = self.LONG_NAME[: i._MAX_NAME_LENGTH] + "*"
        expected_version = self.LONG_VERSION[: i._MAX_VERSION_LENGTH] + "*"

        self.assertEqual(expected_name, self._get_diagnostic_value(entry, "name"))
        self.assertEqual(expected_version, self._get_diagnostic_value(entry, "version"))

    def test_drop_labels(self):
        """Labels should not be copied in instrumentation log"""
        test_logname = "test-name"
        test_labels = {"hello": "world"}
        entry = i._create_diagnostic_entry(
            name=self.LONG_NAME,
            version=self.LONG_VERSION,
            log_name=test_logname,
            labels=test_labels,
        )
        self.assertEqual(entry.log_name, test_logname)
        self.assertIsNone(entry.labels)
        # ensure only expected fields exist in entry
        expected_keys = set(["logName", "resource", "jsonPayload"])
        self.assertEqual(set(entry.to_api_repr().keys()), expected_keys)
