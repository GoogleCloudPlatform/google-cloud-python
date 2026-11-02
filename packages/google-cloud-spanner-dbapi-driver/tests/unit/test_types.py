# Copyright 2026 Google LLC
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

import datetime
import unittest

from google.cloud.spanner_v1 import TypeCode

from google.cloud.spanner_driver import types


class TestTypes(unittest.TestCase):
    def test_date(self):
        d = types.Date(2025, 1, 1)
        self.assertEqual(d, datetime.date(2025, 1, 1))

    def test_time(self):
        t = types.Time(12, 30, 0)
        self.assertEqual(t, datetime.time(12, 30, 0))

    def test_timestamp(self):
        ts = types.Timestamp(2025, 1, 1, 12, 30, 0)
        self.assertEqual(ts, datetime.datetime(2025, 1, 1, 12, 30, 0))

    def test_binary(self):
        b = types.Binary("hello")
        self.assertEqual(b, b"hello")
        b2 = types.Binary(b"world")
        self.assertEqual(b2, b"world")

    def test_type_objects(self):
        self.assertEqual(types.STRING, types.STRING)
        self.assertNotEqual(types.STRING, types.NUMBER)
        self.assertEqual(types.STRING, "STRING")  # DBAPITypeObject compares using 'in'

    def test_type_code_mapping(self):
        self.assertEqual(types._type_code_to_dbapi_type(TypeCode.STRING), types.STRING)
        self.assertEqual(types._type_code_to_dbapi_type(TypeCode.INT64), types.NUMBER)
        self.assertEqual(types._type_code_to_dbapi_type(TypeCode.BOOL), types.BOOLEAN)
        self.assertEqual(types._type_code_to_dbapi_type(TypeCode.FLOAT64), types.NUMBER)
        self.assertEqual(types._type_code_to_dbapi_type(TypeCode.BYTES), types.BINARY)
        self.assertEqual(
            types._type_code_to_dbapi_type(TypeCode.TIMESTAMP), types.DATETIME
        )
        self.assertEqual(types._type_code_to_dbapi_type(TypeCode.DATE), types.DATETIME)
        self.assertEqual(types._type_code_to_dbapi_type(TypeCode.JSON), types.STRING)
