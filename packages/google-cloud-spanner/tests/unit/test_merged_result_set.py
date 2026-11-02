# Copyright 2025 Google LLC All rights reserved.
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

from google.cloud.spanner_v1.streamed import StreamedResultSet


class TestMergedResultSet(unittest.TestCase):
    def _get_target_class(self):
        from google.cloud.spanner_v1.merged_result_set import MergedResultSet

        return MergedResultSet

    def _make_one(self, *args, **kwargs):
        klass = self._get_target_class()
        obj = super(klass, klass).__new__(klass)
        from threading import Event, Lock

        obj.metadata_event = Event()
        obj.metadata_lock = Lock()
        obj._metadata = None
        obj._result_set = None
        return obj

    @staticmethod
    def _make_value(value):
        from google.cloud.spanner_v1._helpers import _make_value_pb

        return _make_value_pb(value)

    @staticmethod
    def _make_scalar_field(name, type_):
        from google.cloud.spanner_v1 import StructType, Type

        return StructType.Field(name=name, type_=Type(code=type_))

    @staticmethod
    def _make_result_set_metadata(fields=()):
        from google.cloud.spanner_v1 import ResultSetMetadata, StructType

        metadata = ResultSetMetadata(row_type=StructType(fields=[]))
        for field in fields:
            metadata.row_type.fields.append(field)
        return metadata

    def test_stats_property(self):
        merged = self._make_one()
        # The property is currently not implemented, so it should just return None.
        self.assertIsNone(merged.stats)

    def test_decode_row(self):
        merged = self._make_one()

        merged._result_set = mock.create_autospec(StreamedResultSet, instance=True)
        merged._result_set.decode_row.return_value = ["Phred", 42]

        raw_row = [self._make_value("Phred"), self._make_value(42)]
        decoded_row = merged.decode_row(raw_row)

        self.assertEqual(decoded_row, ["Phred", 42])
        merged._result_set.decode_row.assert_called_once_with(raw_row)

    def test_decode_row_no_result_set(self):
        merged = self._make_one()
        merged._result_set = None
        with self.assertRaisesRegex(ValueError, "iterator not started"):
            merged.decode_row([])

    def test_decode_row_type_error(self):
        merged = self._make_one()
        merged._result_set = mock.create_autospec(StreamedResultSet, instance=True)
        merged._result_set.decode_row.side_effect = TypeError

        with self.assertRaises(TypeError):
            merged.decode_row("not a list")

    def test_decode_column(self):
        merged = self._make_one()
        merged._result_set = mock.create_autospec(StreamedResultSet, instance=True)
        merged._result_set.decode_column.side_effect = ["Phred", 42]

        raw_row = [self._make_value("Phred"), self._make_value(42)]
        decoded_name = merged.decode_column(raw_row, 0)
        decoded_age = merged.decode_column(raw_row, 1)

        self.assertEqual(decoded_name, "Phred")
        self.assertEqual(decoded_age, 42)
        merged._result_set.decode_column.assert_has_calls(
            [mock.call(raw_row, 0), mock.call(raw_row, 1)]
        )

    def test_decode_column_no_result_set(self):
        merged = self._make_one()
        merged._result_set = None
        with self.assertRaisesRegex(ValueError, "iterator not started"):
            merged.decode_column([], 0)

    def test_decode_column_type_error(self):
        merged = self._make_one()
        merged._result_set = mock.create_autospec(StreamedResultSet, instance=True)
        merged._result_set.decode_column.side_effect = TypeError

        with self.assertRaises(TypeError):
            merged.decode_column("not a list", 0)
