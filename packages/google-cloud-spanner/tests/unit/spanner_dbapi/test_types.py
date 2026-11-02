# Copyright 2020 Google LLC All rights reserved.
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
from time import timezone


class TestTypes(unittest.TestCase):
    TICKS = 1572822862.9782631 + timezone  # Sun 03 Nov 2019 23:14:22 UTC

    def test__date_from_ticks(self):
        import datetime

        from google.cloud.spanner_dbapi import types

        actual = types._date_from_ticks(self.TICKS)
        expected = datetime.date(2019, 11, 3)

        self.assertEqual(actual, expected)

    def test__time_from_ticks(self):
        import datetime

        from google.cloud.spanner_dbapi import types

        actual = types._time_from_ticks(self.TICKS)
        expected = datetime.time(23, 14, 22)

        self.assertEqual(actual, expected)

    def test__timestamp_from_ticks(self):
        import datetime

        from google.cloud.spanner_dbapi import types

        actual = types._timestamp_from_ticks(self.TICKS)
        expected = datetime.datetime(2019, 11, 3, 23, 14, 22)

        self.assertEqual(actual, expected)

    def test_type_equal(self):
        from google.cloud.spanner_dbapi import types

        self.assertEqual(types.BINARY, "TYPE_CODE_UNSPECIFIED")
        self.assertEqual(types.BINARY, "BYTES")
        self.assertEqual(types.BINARY, "ARRAY")
        self.assertEqual(types.BINARY, "STRUCT")
        self.assertNotEqual(types.BINARY, "STRING")

        self.assertEqual(types.NUMBER, "BOOL")
        self.assertEqual(types.NUMBER, "INT64")
        self.assertEqual(types.NUMBER, "FLOAT64")
        self.assertEqual(types.NUMBER, "NUMERIC")
        self.assertNotEqual(types.NUMBER, "STRING")

        self.assertEqual(types.DATETIME, "TIMESTAMP")
        self.assertEqual(types.DATETIME, "DATE")
        self.assertNotEqual(types.DATETIME, "STRING")
