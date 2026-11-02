# Copyright 2024 Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the \"License\");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an \"AS IS\" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from unittest import mock

from google.protobuf.struct_pb2 import ListValue, Value

from google.cloud.spanner_v1._async.streamed import StreamedResultSet
from google.cloud.spanner_v1.types.result_set import ResultSetMetadata
from google.cloud.spanner_v1.types.type import Type, TypeCode


class TestStreamedResultSetExtra(unittest.IsolatedAsyncioTestCase):
    def test_decoders_not_started(self):
        # coverage for line 91
        iterator = mock.Mock()
        srs = StreamedResultSet(iterator)
        with self.assertRaises(ValueError):
            _ = srs._decoders

    def test_decode_row_errors(self):
        # coverage for line 182-183
        srs = StreamedResultSet(mock.Mock())
        with self.assertRaises(TypeError):
            srs.decode_row(None)

    def test_decode_column_errors(self):
        # coverage for line 197-198
        srs = StreamedResultSet(mock.Mock())
        with self.assertRaises(TypeError):
            srs.decode_column(None, 0)

    def test_lazy_decode_branches(self):
        # coverage for line 125
        iterator = mock.Mock()
        srs = StreamedResultSet(iterator, lazy_decode=True)
        # Mock metadata
        srs._metadata = ResultSetMetadata(
            row_type={"fields": [{"name": "f1", "type_": {"code": TypeCode.STRING}}]}
        )

        val = Value(string_value="v1")
        srs._merge_values([val])
        self.assertEqual(srs._rows[0][0], val)

    async def test_to_dict_list(self):
        # coverage for line 257-267
        iterator = mock.Mock()
        srs = StreamedResultSet(iterator)
        srs._metadata = ResultSetMetadata(
            row_type={"fields": [{"name": "f1", "type_": {"code": TypeCode.STRING}}]}
        )
        srs._rows = [["v1"]]
        srs._done = True

        res = await srs.to_dict_list()
        self.assertEqual(res, [{"f1": "v1"}])

    def test_decode_row_success(self):
        # coverage for line 184-187
        srs = StreamedResultSet(mock.Mock())
        srs._metadata = ResultSetMetadata(
            row_type={"fields": [{"type_": {"code": TypeCode.STRING}}]}
        )
        res = srs.decode_row([Value(string_value="v1")])
        self.assertEqual(res, ["v1"])

    def test_decode_column_success(self):
        # coverage for line 199-200
        srs = StreamedResultSet(mock.Mock())
        srs._metadata = ResultSetMetadata(
            row_type={"fields": [{"type_": {"code": TypeCode.STRING}}]}
        )
        res = srs.decode_column([Value(string_value="v1")], 0)
        self.assertEqual(res, "v1")

    def test_merge_struct_null_last(self):
        # coverage for line 371-372
        from google.cloud.spanner_v1._async.streamed import _merge_struct

        type_ = Type(
            code=TypeCode.STRUCT,
            struct_type={"fields": [{"type_": {"code": TypeCode.STRING}}]},
        )
        lhs = Value(list_value=ListValue(values=[Value(null_value=0)]))
        rhs = Value(list_value=ListValue(values=[Value(string_value="v1")]))

        res = _merge_struct(lhs, rhs, type_)
        self.assertEqual(len(res.list_value.values), 2)
        self.assertTrue(res.list_value.values[0].HasField("null_value"))
        self.assertEqual(res.list_value.values[1].string_value, "v1")
