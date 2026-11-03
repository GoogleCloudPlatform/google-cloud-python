import asyncio
from unittest import IsolatedAsyncioTestCase

import mock
import pytest

from google.cloud.aio._cross_sync import CrossSync

# Copyright 2016 Google LLC All rights reserved.
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


class IsolatedAsyncioTestCase(IsolatedAsyncioTestCase):
    def run(self, result=None):
        if asyncio.iscoroutinefunction(getattr(self, self._testMethodName)):
            testMethod = getattr(self, self._testMethodName)

            def wrapper(*args, **kwargs):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    return loop.run_until_complete(testMethod(*args, **kwargs))
                finally:
                    loop.close()

            setattr(self, self._testMethodName, wrapper)
        super().run(result)


@CrossSync.convert_class(
    replace_symbols={
        "google.cloud.spanner_v1._async": "google.cloud.spanner_v1",
        "tests.unit._async": "tests.unit",
        "IsolatedAsyncioTestCase": "IsolatedAsyncioTestCase",
        "CrossSync.Mock": "mock.Mock",
    }
)
class TestStreamedResultSet(IsolatedAsyncioTestCase):
    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.streamed import StreamedResultSet

        return StreamedResultSet

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    @CrossSync.pytest
    async def test_ctor_defaults(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        self.assertIs(streamed._response_iterator, iterator)
        self.assertEqual([i async for i in streamed], [])
        self.assertIsNone(streamed.metadata)
        self.assertIsNone(streamed.stats)

    @CrossSync.pytest
    async def test_ctor_w_source(self):
        iterator = _MockCancellableIterator()
        source = object()
        streamed = self._make_one(iterator, source=source)
        self.assertIs(streamed._response_iterator, iterator)
        self.assertEqual([i async for i in streamed], [])
        self.assertIsNone(streamed.metadata)
        self.assertIsNone(streamed.stats)

    @CrossSync.pytest
    async def test_fields_unset(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        with pytest.raises(AttributeError):
            streamed.fields

    @staticmethod
    def _make_scalar_field(name, type_):
        from google.cloud.spanner_v1 import StructType, Type

        return StructType.Field(name=name, type_=Type(code=type_))

    @staticmethod
    def _make_array_field(name, element_type_code=None, element_type=None):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode

        if element_type is None:
            element_type = Type(code=element_type_code)
        array_type = Type(code=TypeCode.ARRAY, array_element_type=element_type)
        return StructType.Field(name=name, type_=array_type)

    @staticmethod
    def _make_struct_type(struct_type_fields):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode

        fields = [
            StructType.Field(name=key, type_=Type(code=value))
            for key, value in struct_type_fields
        ]
        struct_type = StructType(fields=fields)
        return Type(code=TypeCode.STRUCT, struct_type=struct_type)

    @staticmethod
    def _make_value(value):
        from google.cloud.spanner_v1._helpers import _make_value_pb

        return _make_value_pb(value)

    @staticmethod
    def _make_list_value(values=(), value_pbs=None):
        from google.protobuf.struct_pb2 import ListValue, Value

        from google.cloud.spanner_v1._helpers import _make_list_value_pb

        if value_pbs is not None:
            return Value(list_value=ListValue(values=value_pbs))
        return Value(list_value=_make_list_value_pb(values))

    @staticmethod
    def _make_result_set_metadata(fields=(), transaction_id=None):
        from google.cloud.spanner_v1 import ResultSetMetadata, StructType

        metadata = ResultSetMetadata(row_type=StructType(fields=[]))
        for field in fields:
            metadata.row_type.fields.append(field)
        if transaction_id is not None:
            metadata.transaction.id = transaction_id
        return metadata

    @staticmethod
    def _make_result_set_stats(query_plan=None, **kw):
        from google.protobuf.struct_pb2 import Struct

        from google.cloud.spanner_v1 import ResultSetStats
        from google.cloud.spanner_v1._helpers import _make_value_pb

        query_stats = Struct(
            fields={key: _make_value_pb(value) for key, value in kw.items()}
        )
        return ResultSetStats(query_plan=query_plan, query_stats=query_stats)

    @staticmethod
    def _make_partial_result_set(
        values, metadata=None, stats=None, chunked_value=False, last=False
    ):
        from google.cloud.spanner_v1 import PartialResultSet

        results = PartialResultSet(
            metadata=metadata, stats=stats, chunked_value=chunked_value, last=last
        )
        for v in values:
            results.values.append(v)
        return results

    @CrossSync.pytest
    async def test_properties_set(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
        ]
        metadata = streamed._metadata = self._make_result_set_metadata(FIELDS)
        stats = streamed._stats = self._make_result_set_stats()
        self.assertEqual(list(streamed.fields), FIELDS)
        self.assertIs(streamed.metadata._pb, metadata)
        self.assertIs(streamed.stats, stats)

    @CrossSync.pytest
    async def test__merge_chunk_bool(self):
        from google.cloud.spanner_v1 import TypeCode
        from google.cloud.spanner_v1._async.streamed import Unmergeable

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("registered_voter", TypeCode.BOOL)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = True
        chunk = False

        with pytest.raises(Unmergeable):
            streamed._merge_chunk(chunk)

    @CrossSync.pytest
    async def test__PartialResultSetWithLastFlag(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("ID", TypeCode.INT64),
            self._make_scalar_field("NAME", TypeCode.STRING),
        ]
        for length in range(4, 6):
            metadata = self._make_result_set_metadata(fields)
            result_sets = [
                self._make_partial_result_set(
                    [self._make_value(0), "google_0"], metadata=metadata
                )
            ]
            for i in range(1, 5):
                bares = [i]
                values = [
                    [self._make_value(bare), "google_" + str(bare)] for bare in bares
                ]
                result_sets.append(
                    self._make_partial_result_set(
                        *values, metadata=metadata, last=(i == length - 1)
                    )
                )

            iterator = _MockCancellableIterator(*result_sets)
            streamed = self._make_one(iterator)
            count = 0
            async for row in streamed:
                self.assertEqual(row[0], count)
                self.assertEqual(row[1], "google_" + str(count))
                count += 1
            self.assertEqual(count, length)

    @CrossSync.pytest
    async def test__merge_chunk_numeric(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("total", TypeCode.NUMERIC)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value("1234.")
        chunk = self._make_value("5678")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "1234.5678")

    @CrossSync.pytest
    async def test__merge_chunk_int64(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("age", TypeCode.INT64)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value(42)
        chunk = self._make_value(13)

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "4213")
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_float64_nan_string(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("weight", TypeCode.FLOAT64)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value("Na")
        chunk = self._make_value("N")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "NaN")

    @CrossSync.pytest
    async def test__merge_chunk_float64_w_empty(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("weight", TypeCode.FLOAT64)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value(3.14159)
        chunk = self._make_value("")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.number_value, 3.14159)

    @CrossSync.pytest
    async def test__merge_chunk_float64_w_float64(self):
        from google.cloud.spanner_v1 import TypeCode
        from google.cloud.spanner_v1._async.streamed import Unmergeable

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("weight", TypeCode.FLOAT64)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value(3.14159)
        chunk = self._make_value(2.71828)

        with pytest.raises(Unmergeable):
            streamed._merge_chunk(chunk)

    @CrossSync.pytest
    async def test__merge_chunk_float32_nan_string(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        fields = [self._make_scalar_field("weight", TypeCode.FLOAT32)]
        streamed._metadata = self._make_result_set_metadata(fields)
        streamed._pending_chunk = self._make_value("Na")
        chunk = self._make_value("N")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "NaN")

    @CrossSync.pytest
    async def test__merge_chunk_float32_w_empty(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        fields = [self._make_scalar_field("weight", TypeCode.FLOAT32)]
        streamed._metadata = self._make_result_set_metadata(fields)
        streamed._pending_chunk = self._make_value(1.25)
        chunk = self._make_value("")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.number_value, 1.25)

    @CrossSync.pytest
    async def test__merge_chunk_float32_w_float32(self):
        from google.cloud.spanner_v1 import TypeCode
        from google.cloud.spanner_v1._async.streamed import Unmergeable

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        fields = [self._make_scalar_field("weight", TypeCode.FLOAT32)]
        streamed._metadata = self._make_result_set_metadata(fields)
        streamed._pending_chunk = self._make_value(1.25)
        chunk = self._make_value(2.5)

        with pytest.raises(Unmergeable):
            streamed._merge_chunk(chunk)

    @CrossSync.pytest
    async def test__merge_chunk_date(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        fields = [self._make_scalar_field("anniversary", TypeCode.DATE)]
        streamed._metadata = self._make_result_set_metadata(fields)
        streamed._pending_chunk = self._make_value("2026-")
        chunk = self._make_value("10-08")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "2026-10-08")

    @CrossSync.pytest
    async def test__merge_chunk_timestamp(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        fields = [self._make_scalar_field("created_at", TypeCode.TIMESTAMP)]
        streamed._metadata = self._make_result_set_metadata(fields)
        streamed._pending_chunk = self._make_value("2026-10-08T13:")
        chunk = self._make_value("15:00Z")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "2026-10-08T13:15:00Z")

    @CrossSync.pytest
    async def test__merge_chunk_interval(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        fields = [self._make_scalar_field("duration", TypeCode.INTERVAL)]
        streamed._metadata = self._make_result_set_metadata(fields)
        streamed._pending_chunk = self._make_value("P1Y2M")
        chunk = self._make_value("3DT4H")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "P1Y2M3DT4H")

    @CrossSync.pytest
    async def test__merge_chunk_uuid(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        fields = [self._make_scalar_field("session_id", TypeCode.UUID)]
        streamed._metadata = self._make_result_set_metadata(fields)
        streamed._pending_chunk = self._make_value("12345678-1234-")
        chunk = self._make_value("5678-1234-567812345678")

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "12345678-1234-5678-1234-567812345678")

    @CrossSync.pytest
    async def test__merge_chunk_string(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("name", TypeCode.STRING)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value("phred")
        chunk = self._make_value("wylma")

        merged = streamed._merge_chunk(chunk)

        self.assertEqual(merged.string_value, "phredwylma")
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_string_w_bytes(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("image", TypeCode.BYTES)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA"
            "6fptVAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA\n"
        )
        chunk = self._make_value(
            "B3RJTUUH4QQGFwsBTL3HMwAAABJpVFh0Q29tbWVudAAAAAAAU0FNUExF"
            "MG3E+AAAAApJREFUCNdj\nYAAAAAIAAeIhvDMAAAAASUVORK5CYII=\n"
        )

        merged = streamed._merge_chunk(chunk)

        self.assertEqual(
            merged.string_value,
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA6fptVAAAACXBIWXMAAAsTAAAL"
            "EwEAmpwYAAAA\nB3RJTUUH4QQGFwsBTL3HMwAAABJpVFh0Q29tbWVudAAAAAAAU0"
            "FNUExFMG3E+AAAAApJREFUCNdj\nYAAAAAIAAeIhvDMAAAAASUVORK5CYII=\n",
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_proto(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("proto", TypeCode.PROTO)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA"
            "6fptVAAAACXBIWXMAAAsTAAALEwEAmpwYAAAA\n"
        )
        chunk = self._make_value(
            "B3RJTUUH4QQGFwsBTL3HMwAAABJpVFh0Q29tbWVudAAAAAAAU0FNUExF"
            "MG3E+AAAAApJREFUCNdj\nYAAAAAIAAeIhvDMAAAAASUVORK5CYII=\n"
        )

        merged = streamed._merge_chunk(chunk)

        self.assertEqual(
            merged.string_value,
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA6fptVAAAACXBIWXMAAAsTAAAL"
            "EwEAmpwYAAAA\nB3RJTUUH4QQGFwsBTL3HMwAAABJpVFh0Q29tbWVudAAAAAAAU0"
            "FNUExFMG3E+AAAAApJREFUCNdj\nYAAAAAIAAeIhvDMAAAAASUVORK5CYII=\n",
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_enum(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_scalar_field("age", TypeCode.ENUM)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value(42)
        chunk = self._make_value(13)

        merged = streamed._merge_chunk(chunk)
        self.assertEqual(merged.string_value, "4213")
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_bool(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_array_field("name", element_type_code=TypeCode.BOOL)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value([True, True])
        chunk = self._make_list_value([False, False, False])

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value([True, True, False, False, False])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_int(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_array_field("name", element_type_code=TypeCode.INT64)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value([0, 1, 2])
        chunk = self._make_list_value([3, 4, 5])

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value([0, 1, 23, 4, 5])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_float(self):
        import math

        from google.cloud.spanner_v1 import TypeCode

        PI = math.pi
        EULER = math.e
        SQRT_2 = math.sqrt(2.0)
        LOG_10 = math.log(10)
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_array_field("name", element_type_code=TypeCode.FLOAT64)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value([PI, SQRT_2])
        chunk = self._make_list_value(["", EULER, LOG_10])

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value([PI, SQRT_2, EULER, LOG_10])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_string_with_empty(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_array_field("name", element_type_code=TypeCode.STRING)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value(["A", "B", "C"])
        chunk = self._make_list_value([])

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value(["A", "B", "C"])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_string(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_array_field("name", element_type_code=TypeCode.STRING)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value(["A", "B", "C"])
        chunk = self._make_list_value(["D", "E"])

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value(["A", "B", "CD", "E"])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_string_with_null(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_array_field("name", element_type_code=TypeCode.STRING)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value(["A", "B", "C"])
        chunk = self._make_list_value([None, "D", "E"])

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value(["A", "B", "C", None, "D", "E"])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_string_with_null_pending(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [self._make_array_field("name", element_type_code=TypeCode.STRING)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value(["A", "B", "C", None])
        chunk = self._make_list_value(["D", "E"])
        merged = streamed._merge_chunk(chunk)
        expected = self._make_list_value(["A", "B", "C", None, "D", "E"])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_array_of_int(self):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode

        subarray_type = Type(
            code=TypeCode.ARRAY, array_element_type=Type(code=TypeCode.INT64)
        )
        array_type = Type(code=TypeCode.ARRAY, array_element_type=subarray_type)
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [StructType.Field(name="loloi", type_=array_type)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value(
            value_pbs=[self._make_list_value([0, 1]), self._make_list_value([2])]
        )
        chunk = self._make_list_value(
            value_pbs=[self._make_list_value([3]), self._make_list_value([4, 5])]
        )

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value(
            value_pbs=[
                self._make_list_value([0, 1]),
                self._make_list_value([23]),
                self._make_list_value([4, 5]),
            ]
        )
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_array_of_string(self):
        from google.cloud.spanner_v1 import StructType, Type, TypeCode

        subarray_type = Type(
            code=TypeCode.ARRAY, array_element_type=Type(code=TypeCode.STRING)
        )
        array_type = Type(code=TypeCode.ARRAY, array_element_type=subarray_type)
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [StructType.Field(name="lolos", type_=array_type)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_list_value(
            value_pbs=[
                self._make_list_value(["A", "B"]),
                self._make_list_value(["C"]),
            ]
        )
        chunk = self._make_list_value(
            value_pbs=[
                self._make_list_value(["D"]),
                self._make_list_value(["E", "F"]),
            ]
        )

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value(
            value_pbs=[
                self._make_list_value(["A", "B"]),
                self._make_list_value(["CD"]),
                self._make_list_value(["E", "F"]),
            ]
        )
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_struct(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        struct_type = self._make_struct_type(
            [("name", TypeCode.STRING), ("age", TypeCode.INT64)]
        )
        FIELDS = [self._make_array_field("test", element_type=struct_type)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        partial = self._make_list_value(["Phred "])
        streamed._pending_chunk = self._make_list_value(value_pbs=[partial])
        rest = self._make_list_value(["Phlyntstone", 31])
        chunk = self._make_list_value(value_pbs=[rest])

        merged = streamed._merge_chunk(chunk)

        struct = self._make_list_value(["Phred Phlyntstone", 31])
        expected = self._make_list_value(value_pbs=[struct])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_struct_with_empty(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        struct_type = self._make_struct_type(
            [("name", TypeCode.STRING), ("age", TypeCode.INT64)]
        )
        FIELDS = [self._make_array_field("test", element_type=struct_type)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        partial = self._make_list_value(["Phred "])
        streamed._pending_chunk = self._make_list_value(value_pbs=[partial])
        rest = self._make_list_value([])
        chunk = self._make_list_value(value_pbs=[rest])

        merged = streamed._merge_chunk(chunk)

        expected = self._make_list_value(value_pbs=[partial])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_struct_unmergeable(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        struct_type = self._make_struct_type(
            [
                ("name", TypeCode.STRING),
                ("registered", TypeCode.BOOL),
                ("voted", TypeCode.BOOL),
            ]
        )
        FIELDS = [self._make_array_field("test", element_type=struct_type)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        partial = self._make_list_value(["Phred Phlyntstone", True])
        streamed._pending_chunk = self._make_list_value(value_pbs=[partial])
        rest = self._make_list_value([True])
        chunk = self._make_list_value(value_pbs=[rest])

        merged = streamed._merge_chunk(chunk)

        struct = self._make_list_value(["Phred Phlyntstone", True, True])
        expected = self._make_list_value(value_pbs=[struct])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test__merge_chunk_array_of_struct_unmergeable_split(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        struct_type = self._make_struct_type(
            [("name", "STRING"), ("height", "FLOAT64"), ("eye_color", "STRING")]
        )
        FIELDS = [self._make_array_field("test", element_type=struct_type)]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        partial = self._make_list_value(["Phred Phlyntstone", 1.65])
        streamed._pending_chunk = self._make_list_value(value_pbs=[partial])
        rest = self._make_list_value(["brown"])
        chunk = self._make_list_value(value_pbs=[rest])

        merged = streamed._merge_chunk(chunk)

        struct = self._make_list_value(["Phred Phlyntstone", 1.65, "brown"])
        expected = self._make_list_value(value_pbs=[struct])
        self.assertEqual(merged, expected)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test_merge_values_empty_and_empty(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._current_row = []
        streamed._merge_values([])
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, [])

    @CrossSync.pytest
    async def test_merge_values_empty_and_partial(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        BARE = ["Phred Phlyntstone", 42]
        VALUES = [self._make_value(bare) for bare in BARE]
        streamed._current_row = []
        streamed._merge_values(VALUES)
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, BARE)

    @CrossSync.pytest
    async def test_merge_values_empty_and_filled(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        BARE = ["Phred Phlyntstone", 42, True]
        VALUES = [self._make_value(bare) for bare in BARE]
        streamed._current_row = []
        streamed._merge_values(VALUES)
        self.assertEqual([i async for i in streamed], [BARE])
        self.assertEqual(streamed._current_row, [])

    @CrossSync.pytest
    async def test_merge_values_empty_and_filled_plus(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        BARE = [
            "Phred Phlyntstone",
            42,
            True,
            "Bharney Rhubble",
            39,
            True,
            "Wylma Phlyntstone",
        ]
        VALUES = [self._make_value(bare) for bare in BARE]
        streamed._current_row = []
        streamed._merge_values(VALUES)
        self.assertEqual([i async for i in streamed], [BARE[0:3], BARE[3:6]])
        self.assertEqual(streamed._current_row, BARE[6:])

    @CrossSync.pytest
    async def test_merge_values_partial_and_empty(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        BEFORE = ["Phred Phlyntstone"]
        streamed._current_row[:] = BEFORE
        streamed._merge_values([])
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, BEFORE)

    @CrossSync.pytest
    async def test_merge_values_partial_and_partial(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        BEFORE = ["Phred Phlyntstone"]
        streamed._current_row[:] = BEFORE
        MERGED = [42]
        TO_MERGE = [self._make_value(item) for item in MERGED]
        streamed._merge_values(TO_MERGE)
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, BEFORE + MERGED)

    @CrossSync.pytest
    async def test_merge_values_partial_and_filled(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        BEFORE = ["Phred Phlyntstone"]
        streamed._current_row[:] = BEFORE
        MERGED = [42, True]
        TO_MERGE = [self._make_value(item) for item in MERGED]
        streamed._merge_values(TO_MERGE)
        self.assertEqual([i async for i in streamed], [BEFORE + MERGED])
        self.assertEqual(streamed._current_row, [])

    @CrossSync.pytest
    async def test_merge_values_partial_and_filled_plus(self):
        from google.cloud.spanner_v1 import TypeCode

        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        BEFORE = [self._make_value("Phred Phlyntstone")]
        streamed._current_row[:] = BEFORE
        MERGED = [42, True, "Bharney Rhubble", 39, True, "Wylma Phlyntstone"]
        TO_MERGE = [self._make_value(item) for item in MERGED]
        VALUES = BEFORE + MERGED
        streamed._merge_values(TO_MERGE)
        self.assertEqual([i async for i in streamed], [VALUES[0:3], VALUES[3:6]])
        self.assertEqual(streamed._current_row, VALUES[6:])

    @CrossSync.pytest
    async def test_one_or_none_no_value(self):
        streamed = self._make_one(_MockCancellableIterator())
        with mock.patch.object(streamed, "_consume_next") as consume_next:
            consume_next.side_effect = StopAsyncIteration
            self.assertIsNone(await streamed.one_or_none())

    @CrossSync.pytest
    async def test_one_or_none_single_value(self):
        streamed = self._make_one(_MockCancellableIterator())
        streamed._rows = ["foo"]
        with mock.patch.object(streamed, "_consume_next") as consume_next:
            consume_next.side_effect = StopAsyncIteration
            self.assertEqual(await streamed.one_or_none(), "foo")

    @CrossSync.pytest
    async def test_one_or_none_multiple_values(self):
        streamed = self._make_one(_MockCancellableIterator())
        streamed._rows = ["foo", "bar"]
        with pytest.raises(ValueError):
            await streamed.one_or_none()

    @CrossSync.pytest
    async def test_one_or_none_consumed_stream(self):
        streamed = self._make_one(_MockCancellableIterator())
        streamed._metadata = object()
        with pytest.raises(RuntimeError):
            await streamed.one_or_none()

    @CrossSync.pytest
    async def test_one_single_value(self):
        streamed = self._make_one(_MockCancellableIterator())
        streamed._rows = ["foo"]
        with mock.patch.object(streamed, "_consume_next") as consume_next:
            consume_next.side_effect = StopAsyncIteration
            self.assertEqual(await streamed.one(), "foo")

    @CrossSync.pytest
    async def test_one_no_value(self):
        from google.cloud import exceptions

        iterator = _MockCancellableIterator(["foo"])
        streamed = self._make_one(iterator)
        with mock.patch.object(streamed, "_consume_next") as consume_next:
            consume_next.side_effect = StopAsyncIteration
            with pytest.raises(exceptions.NotFound):
                await streamed.one()

    @CrossSync.pytest
    async def test_consume_next_empty(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        with pytest.raises(StopAsyncIteration):
            await streamed._consume_next()

    @CrossSync.pytest
    async def test_consume_next_first_set_partial(self):
        from google.cloud.spanner_v1 import TypeCode

        TXN_ID = b"DEADBEEF"
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(FIELDS, transaction_id=TXN_ID)
        BARE = ["Phred Phlyntstone", 42]
        VALUES = [self._make_value(bare) for bare in BARE]
        result_set = self._make_partial_result_set(VALUES, metadata=metadata)
        iterator = _MockCancellableIterator(result_set)
        source = CrossSync.Mock(_transaction_id=None, spec=["_transaction_id"])
        streamed = self._make_one(iterator, source=source)
        await streamed._consume_next()
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, BARE)
        self.assertEqual(streamed.metadata, metadata)

    @CrossSync.pytest
    async def test_consume_next_first_set_partial_existing_txn_id(self):
        from google.cloud.spanner_v1 import TypeCode

        TXN_ID = b"DEADBEEF"
        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(FIELDS, transaction_id=b"")
        BARE = ["Phred Phlyntstone", 42]
        VALUES = [self._make_value(bare) for bare in BARE]
        result_set = self._make_partial_result_set(VALUES, metadata=metadata)
        iterator = _MockCancellableIterator(result_set)
        source = CrossSync.Mock(_transaction_id=TXN_ID, spec=["_transaction_id"])
        streamed = self._make_one(iterator, source=source)
        await streamed._consume_next()
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, BARE)
        self.assertEqual(streamed.metadata, metadata)
        self.assertEqual(source._transaction_id, TXN_ID)

    @CrossSync.pytest
    async def test_consume_next_w_partial_result(self):
        from google.cloud.spanner_v1 import TypeCode

        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        VALUES = [self._make_value("Phred ")]
        result_set = self._make_partial_result_set(VALUES, chunked_value=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        await streamed._consume_next()
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, [])
        self.assertEqual(streamed._pending_chunk, VALUES[0])

    @CrossSync.pytest
    async def test_consume_next_w_pending_chunk(self):
        from google.cloud.spanner_v1 import TypeCode

        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        BARE = [
            "Phlyntstone",
            42,
            True,
            "Bharney Rhubble",
            39,
            True,
            "Wylma Phlyntstone",
        ]
        VALUES = [self._make_value(bare) for bare in BARE]
        result_set = self._make_partial_result_set(VALUES)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        streamed._metadata = self._make_result_set_metadata(FIELDS)
        streamed._pending_chunk = self._make_value("Phred ")
        await streamed._consume_next()
        self.assertEqual(
            [i async for i in streamed],
            [["Phred Phlyntstone", BARE[1], BARE[2]], [BARE[3], BARE[4], BARE[5]]],
        )
        self.assertEqual(streamed._current_row, [BARE[6]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test_consume_next_last_set(self):
        from google.cloud.spanner_v1 import TypeCode

        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(FIELDS)
        stats = self._make_result_set_stats(
            rows_returned="1", elapsed_time="1.23 secs", cpu_time="0.98 secs"
        )
        BARE = ["Phred Phlyntstone", 42, True]
        VALUES = [self._make_value(bare) for bare in BARE]
        result_set = self._make_partial_result_set(VALUES, stats=stats)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        streamed._metadata = metadata
        await streamed._consume_next()
        self.assertEqual([i async for i in streamed], [BARE])
        self.assertEqual(streamed._current_row, [])
        self.assertEqual(streamed._stats, stats)

    @CrossSync.pytest
    async def test___iter___empty(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        found = [i async for i in streamed]
        self.assertEqual(found, [])

    @CrossSync.pytest
    async def test___iter___one_result_set_partial(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import TypeCode

        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(FIELDS)
        BARE = ["Phred Phlyntstone", 42]
        VALUES = [self._make_value(bare) for bare in BARE]
        for val in VALUES:
            self.assertIsInstance(val, Value)
        result_set = self._make_partial_result_set(VALUES, metadata=metadata)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        found = [i async for i in streamed]
        self.assertEqual(found, [])
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, BARE)
        self.assertEqual(streamed.metadata, metadata)

    @CrossSync.pytest
    async def test___iter___multiple_result_sets_filled(self):
        from google.cloud.spanner_v1 import TypeCode

        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(FIELDS)
        BARE = [
            "Phred Phlyntstone",
            42,
            True,
            "Bharney Rhubble",
            39,
            True,
            "Wylma Phlyntstone",
            41,
            True,
        ]
        VALUES = [self._make_value(bare) for bare in BARE]
        result_set1 = self._make_partial_result_set(VALUES[:4], metadata=metadata)
        result_set2 = self._make_partial_result_set(VALUES[4:])
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator)
        found = [i async for i in streamed]
        self.assertEqual(
            found,
            [
                [BARE[0], BARE[1], BARE[2]],
                [BARE[3], BARE[4], BARE[5]],
                [BARE[6], BARE[7], BARE[8]],
            ],
        )
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, [])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___w_existing_rows_read(self):
        from google.cloud.spanner_v1 import TypeCode

        FIELDS = [
            self._make_scalar_field("full_name", TypeCode.STRING),
            self._make_scalar_field("age", TypeCode.INT64),
            self._make_scalar_field("married", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(FIELDS)
        ALREADY = [["Pebbylz Phlyntstone", 4, False], ["Dino Rhubble", 4, False]]
        BARE = [
            "Phred Phlyntstone",
            42,
            True,
            "Bharney Rhubble",
            39,
            True,
            "Wylma Phlyntstone",
            41,
            True,
        ]
        VALUES = [self._make_value(bare) for bare in BARE]
        result_set1 = self._make_partial_result_set(VALUES[:4], metadata=metadata)
        result_set2 = self._make_partial_result_set(VALUES[4:])
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator)
        streamed._rows[:] = ALREADY
        found = [i async for i in streamed]
        self.assertEqual(
            found,
            ALREADY
            + [
                [BARE[0], BARE[1], BARE[2]],
                [BARE[3], BARE[4], BARE[5]],
                [BARE[6], BARE[7], BARE[8]],
            ],
        )
        self.assertEqual([i async for i in streamed], [])
        self.assertEqual(streamed._current_row, [])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___large_batch(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        expected_rows = [[index, f"name_{index}"] for index in range(500)]
        values = [self._make_value(cell) for row in expected_rows for cell in row]

        result_set = self._make_partial_result_set(values, metadata=metadata)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, expected_rows)
        self.assertEqual([row async for row in streamed], [])

    @CrossSync.pytest
    async def test___iter___stepwise_consumption(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        expected_rows = [[index, f"name_{index}"] for index in range(20)]
        values = [self._make_value(cell) for row in expected_rows for cell in row]

        result_set = self._make_partial_result_set(values, metadata=metadata)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        stream_iter = streamed.__aiter__()
        first_five = [await stream_iter.__anext__() for _ in range(5)]
        self.assertEqual(first_five, expected_rows[:5])
        remaining = [row async for row in stream_iter]
        self.assertEqual(remaining, expected_rows[5:])

    @CrossSync.pytest
    async def test___iter___stepwise_across_chunks(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        chunk1_rows = [[index, f"name_{index}"] for index in range(10)]
        chunk2_rows = [[index, f"name_{index}"] for index in range(10, 20)]
        values1 = [self._make_value(cell) for row in chunk1_rows for cell in row]
        values2 = [self._make_value(cell) for row in chunk2_rows for cell in row]

        result_set1 = self._make_partial_result_set(values1, metadata=metadata)
        result_set2 = self._make_partial_result_set(values2)
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator)
        stream_iter = streamed.__aiter__()
        first_part = [await stream_iter.__anext__() for _ in range(5)]
        self.assertEqual(first_part, chunk1_rows[:5])
        middle_part = [await stream_iter.__anext__() for _ in range(10)]
        self.assertEqual(middle_part, chunk1_rows[5:] + chunk2_rows[:5])
        final_part = [row async for row in stream_iter]
        self.assertEqual(final_part, chunk2_rows[5:])

    @CrossSync.pytest
    async def test___iter___early_break(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        expected_rows = [[index, f"name_{index}"] for index in range(10)]
        values = [self._make_value(cell) for row in expected_rows for cell in row]

        result_set = self._make_partial_result_set(values, metadata=metadata)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        consumed = []
        async for row in streamed:
            consumed.append(row)
            if len(consumed) == 3:
                break

        self.assertEqual(consumed, expected_rows[:3])

    @CrossSync.pytest
    async def test___iter___mid_stream_error(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        chunk1_rows = [[index, f"name_{index}"] for index in range(5)]
        values1 = [self._make_value(cell) for row in chunk1_rows for cell in row]
        result_set1 = self._make_partial_result_set(values1, metadata=metadata)

        async def mock_iterator():
            yield result_set1
            raise RuntimeError("Stream error midway")

        streamed = self._make_one(mock_iterator())
        consumed = []
        with self.assertRaises(RuntimeError) as context:
            async for row in streamed:
                consumed.append(row)

        self.assertEqual(consumed, chunk1_rows)
        self.assertIn("Stream error midway", str(context.exception))

    @CrossSync.pytest
    async def test_decode_rows_direct_width_one(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("count", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        expected_rows = [[42]]
        values = [self._make_value(42)]

        result_set = self._make_partial_result_set(values, metadata=metadata, last=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, expected_rows)
        self.assertTrue(streamed._done)

    @CrossSync.pytest
    async def test_decode_rows_direct_multi_column(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
            self._make_scalar_field("active", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(fields)
        expected_rows = [[1, "alpha", True], [2, "beta", False]]
        values = [self._make_value(cell) for row in expected_rows for cell in row]

        result_set = self._make_partial_result_set(values, metadata=metadata, last=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, expected_rows)
        self.assertTrue(streamed._done)

    @CrossSync.pytest
    async def test_decode_rows_direct_with_null_values(self):
        from google.protobuf.struct_pb2 import NULL_VALUE, Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        values = [
            self._make_value(1),
            Value(null_value=NULL_VALUE),
            self._make_value(2),
            self._make_value("Alice"),
        ]
        expected_rows = [[1, None], [2, "Alice"]]

        result_set = self._make_partial_result_set(values, metadata=metadata, last=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, expected_rows)

    @CrossSync.pytest
    async def test_decode_rows_direct_lazy_decode_width_one(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        raw_value = self._make_value(100)
        values = [raw_value]

        result_set = self._make_partial_result_set(values, metadata=metadata, last=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], [raw_value])
        self.assertEqual(streamed.decode_row(found[0]), [100])

    @CrossSync.pytest
    async def test_decode_rows_direct_lazy_decode_multi_column(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(1)
        value_name = self._make_value("test")
        values = [value_id, value_name]

        result_set = self._make_partial_result_set(values, metadata=metadata, last=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], [value_id, value_name])
        self.assertEqual(streamed.decode_row(found[0]), [1, "test"])

    @CrossSync.pytest
    async def test_decode_rows_direct_trailing_partial_row(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        values1 = [
            self._make_value(1),
            self._make_value("a"),
            self._make_value(2),
        ]
        values2 = [
            self._make_value("b"),
            self._make_value(3),
            self._make_value("c"),
        ]

        result_set1 = self._make_partial_result_set(values1, metadata=metadata)
        result_set2 = self._make_partial_result_set(values2, last=True)
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [1, "a"],
                [2, "b"],
                [3, "c"],
            ],
        )

    @CrossSync.pytest
    async def test_decode_rows_direct_trailing_partial_row_lazy_decode(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value1 = self._make_value(1)
        value_a = self._make_value("a")
        value2 = self._make_value(2)
        value_b = self._make_value("b")

        result_set1 = self._make_partial_result_set(
            [value1, value_a, value2], metadata=metadata
        )
        result_set2 = self._make_partial_result_set([value_b], last=True)
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(len(found), 2)
        self.assertEqual(found[0], [value1, value_a])
        self.assertEqual(found[1], [value2, value_b])
        self.assertEqual(streamed.decode_row(found[0]), [1, "a"])
        self.assertEqual(streamed.decode_row(found[1]), [2, "b"])

    @CrossSync.pytest
    async def test_decode_rows_direct_trailing_partial_row_with_null(self):
        from google.protobuf.struct_pb2 import NULL_VALUE, Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        values1 = [
            self._make_value(1),
            self._make_value("a"),
            Value(null_value=NULL_VALUE),
        ]
        values2 = [
            self._make_value("b"),
        ]

        result_set1 = self._make_partial_result_set(values1, metadata=metadata)
        result_set2 = self._make_partial_result_set(values2, last=True)
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [1, "a"],
                [None, "b"],
            ],
        )

    @CrossSync.pytest
    async def test_decode_rows_direct_prefix_partial_row_with_null(self):
        from google.protobuf.struct_pb2 import NULL_VALUE, Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        values1 = [
            self._make_value(1),
            self._make_value("a"),
            self._make_value(2),
        ]
        values2 = [
            Value(null_value=NULL_VALUE),
            self._make_value(3),
            self._make_value("c"),
        ]

        result_set1 = self._make_partial_result_set(values1, metadata=metadata)
        result_set2 = self._make_partial_result_set(values2, last=True)
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [1, "a"],
                [2, None],
                [3, "c"],
            ],
        )

    @CrossSync.pytest
    async def test_decode_rows_direct_width_one_with_null(self):
        from google.protobuf.struct_pb2 import NULL_VALUE, Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        values = [
            self._make_value(1),
            Value(null_value=NULL_VALUE),
            self._make_value(2),
        ]

        result_set = self._make_partial_result_set(values, metadata=metadata, last=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[1], [None], [2]])

    @CrossSync.pytest
    async def test_decode_rows_direct_three_chunk_split_row(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
            self._make_scalar_field("active", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(fields)
        prs1 = self._make_partial_result_set([self._make_value(1)], metadata=metadata)
        prs2 = self._make_partial_result_set([self._make_value("alpha")])
        prs3 = self._make_partial_result_set([self._make_value(True)], last=True)

        iterator = _MockCancellableIterator(prs1, prs2, prs3)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[1, "alpha", True]])

    @CrossSync.pytest
    async def test_decode_rows_direct_three_chunk_split_row_lazy_decode(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
            self._make_scalar_field("active", TypeCode.BOOL),
        ]
        metadata = self._make_result_set_metadata(fields)
        val1 = self._make_value(1)
        val2 = self._make_value("alpha")
        val3 = self._make_value(True)
        prs1 = self._make_partial_result_set([val1], metadata=metadata)
        prs2 = self._make_partial_result_set([val2])
        prs3 = self._make_partial_result_set([val3], last=True)

        iterator = _MockCancellableIterator(prs1, prs2, prs3)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(found, [[val1, val2, val3]])
        self.assertEqual(streamed.decode_row(found[0]), [1, "alpha", True])

    @CrossSync.pytest
    async def test_decode_rows_direct_empty_values(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)

        result_set1 = self._make_partial_result_set([], metadata=metadata)
        result_set2 = self._make_partial_result_set([self._make_value(1)], last=True)
        iterator = _MockCancellableIterator(result_set1, result_set2)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[1]])

    @CrossSync.pytest
    async def test_merge_values_zero_fields(self):
        from google.cloud.spanner_v1 import ResultSetMetadata, StructType

        metadata = ResultSetMetadata(row_type=StructType(fields=[]))
        result_set = self._make_partial_result_set([], metadata=metadata, last=True)
        iterator = _MockCancellableIterator(result_set)
        streamed = self._make_one(iterator)
        _ = [row async for row in streamed]
        streamed._merge_values([self._make_value(1)])
        self.assertEqual(streamed._rows, [])

    @CrossSync.pytest
    async def test___iter___chunked_values_empty_string_start(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("column_one", TypeCode.STRING),
            self._make_scalar_field("column_two", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [
                self._make_value("tail-after-empty"),
                self._make_value("value_two"),
                self._make_value("value_three"),
                self._make_value(""),
            ],
            chunked_value=True,
        )
        chunk_three = self._make_partial_result_set(
            [self._make_value("tail-two")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two, chunk_three)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                ["tail-after-empty", "value_two"],
                ["value_three", "tail-two"],
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_empty_list_head_and_tail(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_array_field("column_one", TypeCode.STRING),
            self._make_array_field("column_two", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_list_value([])],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [
                self._make_list_value(["a", "b"]),
                self._make_list_value([]),
            ],
            chunked_value=True,
        )
        chunk_three = self._make_partial_result_set(
            [
                self._make_list_value(["v1", "v2"]),
                self._make_list_value(["x", "y"]),
            ],
            chunked_value=True,
        )
        chunk_four = self._make_partial_result_set(
            [
                self._make_list_value([]),
                self._make_list_value(["w1", "w2"]),
            ],
            chunked_value=True,
        )
        chunk_five = self._make_partial_result_set(
            [
                self._make_list_value([]),
                self._make_list_value([]),
            ],
            chunked_value=True,
        )
        chunk_six = self._make_partial_result_set(
            [
                self._make_list_value([]),
                self._make_list_value(["z1", "z2"]),
            ],
            last=True,
        )
        iterator = _MockCancellableIterator(
            chunk_one, chunk_two, chunk_three, chunk_four, chunk_five, chunk_six
        )
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [["a", "b"], ["v1", "v2"]],
                [["x", "y"], ["w1", "w2"]],
                [[], ["z1", "z2"]],
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_bytes_and_bytes_array(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("raw_bytes", TypeCode.BYTES),
            self._make_array_field("bytes_array", TypeCode.BYTES),
        ]
        metadata = self._make_result_set_metadata(fields)

        full_bytes = b"hello-chunked-bytes-world"
        bytes_part_one = "hello-chunked-"
        bytes_part_two = "bytes-world"

        element_one = b"first-element"
        element_two = b"second-chunked-element"
        element_two_part_one = "second-chunked-"
        element_two_part_two = "element"
        element_three = b"third-element"

        chunk_one = self._make_partial_result_set(
            [self._make_value(bytes_part_one)],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [
                self._make_value(bytes_part_two),
                self._make_list_value(
                    value_pbs=[
                        self._make_value("first-element"),
                        Value(null_value="NULL_VALUE"),
                        self._make_value(element_two_part_one),
                    ]
                ),
            ],
            chunked_value=True,
        )
        chunk_three = self._make_partial_result_set(
            [
                self._make_list_value(
                    value_pbs=[
                        self._make_value(element_two_part_two),
                        self._make_value("third-element"),
                    ]
                )
            ],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two, chunk_three)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [
                    full_bytes,
                    [element_one, None, element_two, element_three],
                ]
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_intermediate_single_value_chunk(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("identifier", TypeCode.STRING),
            self._make_scalar_field("text_payload", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("id1"), self._make_value("hello-")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("world-")],
            chunked_value=True,
        )
        chunk_three = self._make_partial_result_set(
            [
                self._make_value("again"),
                self._make_value("id2"),
                self._make_value("text2"),
            ],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two, chunk_three)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                ["id1", "hello-world-again"],
                ["id2", "text2"],
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___multi_row_multi_chunk_interleaved_splits(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("identifier", TypeCode.INT64),
            self._make_scalar_field("text_payload", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value(1), self._make_value("spl")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [
                self._make_value("it_text_row1"),
                self._make_value(2),
                self._make_value("split_"),
            ],
            chunked_value=True,
        )
        chunk_three = self._make_partial_result_set(
            [self._make_value("text_row2")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two, chunk_three)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [1, "split_text_row1"],
                [2, "split_text_row2"],
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___subsequent_metadata_ignored(self):
        from google.cloud.spanner_v1 import TypeCode

        fields_one = [self._make_scalar_field("primary_column", TypeCode.STRING)]
        metadata_one = self._make_result_set_metadata(fields_one)
        fields_two = [self._make_scalar_field("ignored_column", TypeCode.STRING)]
        metadata_two = self._make_result_set_metadata(fields_two)

        chunk_one = self._make_partial_result_set(
            [self._make_value("alpha")],
            metadata=metadata_one,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("beta")],
            metadata=metadata_two,
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [["alpha"], ["beta"]])
        self.assertEqual(streamed.fields[0].name, "primary_column")

    @CrossSync.pytest
    async def test___iter___empty_chunk_in_middle_of_stream(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("column_name", TypeCode.STRING)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("value_one")],
            metadata=metadata,
        )
        chunk_two = self._make_partial_result_set([])
        chunk_three = self._make_partial_result_set(
            [self._make_value("value_two")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two, chunk_three)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [["value_one"], ["value_two"]])

    @CrossSync.pytest
    async def test___iter___chunked_values_incompatible_types_error(self):
        from google.cloud.spanner_v1 import TypeCode
        from google.cloud.spanner_v1._async.streamed import Unmergeable

        fields = [self._make_scalar_field("registered", TypeCode.BOOL)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value(True)],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value(False)],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        with self.assertRaises(Unmergeable):
            _ = [row async for row in streamed]

    @CrossSync.pytest
    async def test___iter___resumption_across_chunked_value_retry(self):
        from google.api_core.exceptions import ServiceUnavailable

        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("identifier", TypeCode.STRING),
            self._make_scalar_field("data_payload", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)

        attempt_count = 0
        last_resume_token = None

        async def create_stream_attempt(resume_token=None):
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count == 1:
                self.assertIsNone(resume_token)
                chunk_one = self._make_partial_result_set(
                    [self._make_value("id1"), self._make_value("part1-")],
                    metadata=metadata,
                    chunked_value=True,
                )
                chunk_one.resume_token = b"token-1"
                yield chunk_one
                raise ServiceUnavailable("transient error during chunked scalar")
            else:
                self.assertEqual(resume_token, b"token-1")
                chunk_two = self._make_partial_result_set(
                    [self._make_value("part2-actual-")],
                    chunked_value=True,
                )
                chunk_two.resume_token = b"token-2"
                yield chunk_two
                chunk_three = self._make_partial_result_set(
                    [self._make_value("part3-")],
                    chunked_value=True,
                )
                yield chunk_three
                chunk_four = self._make_partial_result_set(
                    [
                        self._make_value("part4"),
                        self._make_value("id2"),
                        self._make_value("data2"),
                    ],
                    last=True,
                )
                yield chunk_four

        class ResumableResponseIterator:
            def __init__(self):
                self._current_generator = create_stream_attempt(None)

            def __aiter__(self):
                return self

            async def __anext__(self):
                nonlocal last_resume_token
                while True:
                    try:
                        item = await anext(self._current_generator)
                        if item.resume_token:
                            last_resume_token = item.resume_token
                        return item
                    except ServiceUnavailable:
                        await self._current_generator.aclose()
                        self._current_generator = create_stream_attempt(
                            last_resume_token
                        )

            async def aclose(self):
                if self._current_generator is not None:
                    await self._current_generator.aclose()

        iterator = ResumableResponseIterator()
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        await iterator.aclose()
        self.assertEqual(
            found,
            [
                ["id1", "part1-part2-actual-part3-part4"],
                ["id2", "data2"],
            ],
        )
        self.assertEqual(attempt_count, 2)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___resumption_across_chunked_array_retry(self):
        from google.api_core.exceptions import ServiceUnavailable

        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("identifier", TypeCode.STRING),
            self._make_array_field("tags", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)

        attempt_count = 0
        last_resume_token = None

        async def create_stream_attempt(resume_token=None):
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count == 1:
                self.assertIsNone(resume_token)
                chunk_one = self._make_partial_result_set(
                    [
                        self._make_value("id1"),
                        self._make_list_value(["tag1", "tag2-"]),
                    ],
                    metadata=metadata,
                    chunked_value=True,
                )
                chunk_one.resume_token = b"token-array"
                yield chunk_one
                raise ServiceUnavailable("transient error during chunked array")
            else:
                self.assertEqual(resume_token, b"token-array")
                chunk_two = self._make_partial_result_set(
                    [self._make_list_value(["tag2-tail", "tag3"])],
                    last=True,
                )
                yield chunk_two

        class ResumableResponseIterator:
            def __init__(self):
                self._current_generator = create_stream_attempt(None)

            def __aiter__(self):
                return self

            async def __anext__(self):
                nonlocal last_resume_token
                while True:
                    try:
                        item = await anext(self._current_generator)
                        if item.resume_token:
                            last_resume_token = item.resume_token
                        return item
                    except ServiceUnavailable:
                        await self._current_generator.aclose()
                        self._current_generator = create_stream_attempt(
                            last_resume_token
                        )

            async def aclose(self):
                if self._current_generator is not None:
                    await self._current_generator.aclose()

        iterator = ResumableResponseIterator()
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        await iterator.aclose()
        self.assertEqual(
            found,
            [
                ["id1", ["tag1", "tag2-tag2-tail", "tag3"]],
            ],
        )
        self.assertEqual(attempt_count, 2)
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_numeric(self):
        import decimal

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("amount", TypeCode.NUMERIC)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("1234.")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("5678")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[decimal.Decimal("1234.5678")]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_json(self):
        from google.cloud.spanner_v1 import JsonObject, TypeCode

        fields = [self._make_scalar_field("payload", TypeCode.JSON)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value('{"user": "')],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value('alice", "score": 10}')],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[JsonObject({"user": "alice", "score": 10})]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_lazy_decode(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("name", TypeCode.STRING)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("hello-")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("world")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(found, [[Value(string_value="hello-world")]])
        self.assertEqual(streamed.decode_row(found[0]), ["hello-world"])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_float32(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("ratio", TypeCode.FLOAT32)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("Infi")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("nity")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[float("inf")]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_float32_array(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_array_field("ratios", TypeCode.FLOAT32)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_list_value([1.5, 2.5])],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_list_value(["", 3.5])],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[[1.5, 2.5, 3.5]]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_date(self):
        import datetime

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("anniversary", TypeCode.DATE)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("2026-")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("10-08")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[datetime.date(2026, 10, 8)]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_date_array(self):
        import datetime

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_array_field("dates", TypeCode.DATE)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_list_value(["2026-01-01", "2026-02-"])],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_list_value(["01", "2026-03-01"])],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [
                    [
                        datetime.date(2026, 1, 1),
                        datetime.date(2026, 2, 1),
                        datetime.date(2026, 3, 1),
                    ]
                ]
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_timestamp(self):
        import datetime

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("created_at", TypeCode.TIMESTAMP)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("2026-10-08T13:")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("15:00Z")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [[datetime.datetime(2026, 10, 8, 13, 15, 0, tzinfo=datetime.timezone.utc)]],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_timestamp_array(self):
        import datetime

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_array_field("timestamps", TypeCode.TIMESTAMP)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_list_value(["2026-01-01T00:00:00Z", "2026-02-01T00:"])],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_list_value(["00:00Z", "2026-03-01T00:00:00Z"])],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [
                    [
                        datetime.datetime(
                            2026, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
                        ),
                        datetime.datetime(
                            2026, 2, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
                        ),
                        datetime.datetime(
                            2026, 3, 1, 0, 0, 0, tzinfo=datetime.timezone.utc
                        ),
                    ]
                ]
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_interval(self):
        from google.cloud.spanner_v1 import Interval, TypeCode

        fields = [self._make_scalar_field("duration", TypeCode.INTERVAL)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("P1Y2M")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("3DT4H")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[Interval.from_str("P1Y2M3DT4H")]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_interval_array(self):
        from google.cloud.spanner_v1 import Interval, TypeCode

        fields = [self._make_array_field("durations", TypeCode.INTERVAL)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_list_value(["P1Y", "P2"])],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_list_value(["M", "P3D"])],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [
                    [
                        Interval.from_str("P1Y"),
                        Interval.from_str("P2M"),
                        Interval.from_str("P3D"),
                    ]
                ]
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_uuid(self):
        import uuid

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("session_id", TypeCode.UUID)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [self._make_value("12345678-1234-")],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_value("5678-1234-567812345678")],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[uuid.UUID("12345678-1234-5678-1234-567812345678")]])
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test___iter___chunked_values_uuid_array(self):
        import uuid

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_array_field("ids", TypeCode.UUID)]
        metadata = self._make_result_set_metadata(fields)
        chunk_one = self._make_partial_result_set(
            [
                self._make_list_value(
                    ["12345678-1234-5678-1234-567812345678", "00000000-0000-"]
                )
            ],
            metadata=metadata,
            chunked_value=True,
        )
        chunk_two = self._make_partial_result_set(
            [self._make_list_value(["0000-0000-000000000000"])],
            last=True,
        )
        iterator = _MockCancellableIterator(chunk_one, chunk_two)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(
            found,
            [
                [
                    [
                        uuid.UUID("12345678-1234-5678-1234-567812345678"),
                        uuid.UUID("00000000-0000-0000-0000-000000000000"),
                    ]
                ]
            ],
        )
        self.assertIsNone(streamed._pending_chunk)

    @CrossSync.pytest
    async def test_consume_next_non_chunked_zero_copy_repeated_container(self):
        from google.cloud.spanner_v1 import (
            PartialResultSet,
            ResultSetMetadata,
            TypeCode,
        )

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)

        partial_result_set_pb = PartialResultSet.pb()()
        partial_result_set_pb.metadata.CopyFrom(ResultSetMetadata.pb(metadata))
        partial_result_set_pb.values.add().string_value = "42"
        partial_result_set_pb.last = True
        partial_result_set = PartialResultSet.wrap(partial_result_set_pb)

        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[42]])

    @CrossSync.pytest
    async def test_single_chunk_point_select_multi_column_fast_path(self):
        from google.protobuf.struct_pb2 import NULL_VALUE, Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
            self._make_scalar_field("nullable_col", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(1)
        value_name = self._make_value("Alice")
        value_null = Value(null_value=NULL_VALUE)

        partial_result_set = self._make_partial_result_set(
            [value_id, value_name, value_null], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[1, "Alice", None]])

    @CrossSync.pytest
    async def test_single_chunk_point_select_lazy_decode_fast_path(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(1)
        value_name = self._make_value("Alice")

        partial_result_set = self._make_partial_result_set(
            [value_id, value_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], [value_id, value_name])
        self.assertEqual(streamed.decode_row(found[0]), [1, "Alice"])

    @CrossSync.pytest
    async def test_single_chunk_multi_row_fast_path(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        row1_id = self._make_value(1)
        row1_name = self._make_value("Alice")
        row2_id = self._make_value(2)
        row2_name = self._make_value("Bob")

        partial_result_set = self._make_partial_result_set(
            [row1_id, row1_name, row2_id, row2_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [[1, "Alice"], [2, "Bob"]])

    @CrossSync.pytest
    async def test_single_chunk_zero_rows(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)

        partial_result_set = self._make_partial_result_set(
            [], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        found = [row async for row in streamed]
        self.assertEqual(found, [])

    @CrossSync.pytest
    async def test_single_chunk_one_or_none_single_row(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(1)
        value_name = self._make_value("Alice")

        partial_result_set = self._make_partial_result_set(
            [value_id, value_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        row = await streamed.one_or_none()
        self.assertEqual(row, [1, "Alice"])
        self.assertTrue(streamed._done)

    @CrossSync.pytest
    async def test_single_chunk_one_or_none_zero_rows(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)

        partial_result_set = self._make_partial_result_set(
            [], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        row = await streamed.one_or_none()
        self.assertIsNone(row)
        self.assertTrue(streamed._done)

    @CrossSync.pytest
    async def test_single_chunk_one_or_none_multiple_rows(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        row1_id = self._make_value(1)
        row1_name = self._make_value("Alice")
        row2_id = self._make_value(2)
        row2_name = self._make_value("Bob")

        partial_result_set = self._make_partial_result_set(
            [row1_id, row1_name, row2_id, row2_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        with pytest.raises(ValueError):
            await streamed.one_or_none()

    @CrossSync.pytest
    async def test_single_chunk_one_single_row(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(42)
        value_name = self._make_value("Answer")

        partial_result_set = self._make_partial_result_set(
            [value_id, value_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        row = await streamed.one()
        self.assertEqual(row, [42, "Answer"])

    @CrossSync.pytest
    async def test_single_chunk_multi_row_lazy_decode_fast_path(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        row1_id = self._make_value(1)
        row1_name = self._make_value("Alice")
        row2_id = self._make_value(2)
        row2_name = self._make_value("Bob")

        partial_result_set = self._make_partial_result_set(
            [row1_id, row1_name, row2_id, row2_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(len(found), 2)
        self.assertEqual(found[0], [row1_id, row1_name])
        self.assertEqual(found[1], [row2_id, row2_name])
        self.assertEqual(streamed.decode_row(found[0]), [1, "Alice"])
        self.assertEqual(streamed.decode_row(found[1]), [2, "Bob"])

    @CrossSync.pytest
    async def test_single_chunk_single_column_lazy_decode(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        row1_id = self._make_value(1)
        row2_id = self._make_value(2)

        partial_result_set = self._make_partial_result_set(
            [row1_id, row2_id], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(len(found), 2)
        self.assertEqual(found[0], [row1_id])
        self.assertEqual(found[1], [row2_id])
        self.assertEqual(streamed.decode_row(found[0]), [1])
        self.assertEqual(streamed.decode_row(found[1]), [2])

    @CrossSync.pytest
    async def test_multi_chunk_one_or_none_single_row(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(42)

        chunk1 = self._make_partial_result_set(
            [value_id], metadata=metadata, last=False
        )
        chunk2 = self._make_partial_result_set([], last=True)
        iterator = _MockCancellableIterator(chunk1, chunk2)
        streamed = self._make_one(iterator)
        row = await streamed.one_or_none()
        self.assertEqual(row, [42])
        self.assertTrue(streamed._done)

    @CrossSync.pytest
    async def test_multi_chunk_one_or_none_zero_rows(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)

        chunk1 = self._make_partial_result_set([], metadata=metadata, last=False)
        chunk2 = self._make_partial_result_set([], last=True)
        iterator = _MockCancellableIterator(chunk1, chunk2)
        streamed = self._make_one(iterator)
        row = await streamed.one_or_none()
        self.assertIsNone(row)
        self.assertTrue(streamed._done)

    @CrossSync.pytest
    async def test_multi_chunk_one_or_none_multiple_rows(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        value1 = self._make_value(1)
        value2 = self._make_value(2)

        chunk1 = self._make_partial_result_set([value1], metadata=metadata, last=False)
        chunk2 = self._make_partial_result_set([value2], last=True)
        iterator = _MockCancellableIterator(chunk1, chunk2)
        streamed = self._make_one(iterator)
        with pytest.raises(ValueError):
            await streamed.one_or_none()

    @CrossSync.pytest
    async def test_streamed_reiteration_after_done(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        value = self._make_value(1)

        partial_result_set = self._make_partial_result_set(
            [value], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        first_pass = [row async for row in streamed]
        self.assertEqual(first_pass, [[1]])
        second_pass = [row async for row in streamed]
        self.assertEqual(second_pass, [])

    @CrossSync.pytest
    async def test_single_chunk_one_single_row_null_value(self):
        from google.protobuf.struct_pb2 import NULL_VALUE, Value

        from google.cloud.spanner_v1 import TypeCode

        fields = [self._make_scalar_field("id", TypeCode.INT64)]
        metadata = self._make_result_set_metadata(fields)
        value_null = Value(null_value=NULL_VALUE)

        partial_result_set = self._make_partial_result_set(
            [value_null], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        row = await streamed.one()
        self.assertEqual(row, [None])

    @CrossSync.pytest
    async def test_single_chunk_single_row_lazy_decode_fast_path(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(1)
        value_name = self._make_value("Alice")

        partial_result_set = self._make_partial_result_set(
            [value_id, value_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator, lazy_decode=True)
        found = [row async for row in streamed]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], [value_id, value_name])
        self.assertEqual(streamed.decode_row(found[0]), [1, "Alice"])

    @CrossSync.pytest
    async def test_single_chunk_to_dict_list_multi_row(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        row1_id = self._make_value(1)
        row1_name = self._make_value("Alice")
        row2_id = self._make_value(2)
        row2_name = self._make_value("Bob")

        partial_result_set = self._make_partial_result_set(
            [row1_id, row1_name, row2_id, row2_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        found = await streamed.to_dict_list()
        self.assertEqual(found, [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])

    @CrossSync.pytest
    async def test_single_chunk_to_dict_list_empty(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)

        partial_result_set = self._make_partial_result_set(
            [], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator)
        found = await streamed.to_dict_list()
        self.assertEqual(found, [])

    @CrossSync.pytest
    async def test_stats_property(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        self.assertIsNone(streamed.stats)
        streamed._stats = "fake_stats"
        self.assertEqual(streamed.stats, "fake_stats")

    @CrossSync.pytest
    async def test_decode_row_type_error(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        with pytest.raises(TypeError):
            streamed.decode_row(123)

    @CrossSync.pytest
    async def test_decode_column_type_error(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        with pytest.raises(TypeError):
            streamed.decode_column(123, 0)

    @CrossSync.pytest
    async def test_decode_column_success(self):
        from google.cloud.spanner_v1 import TypeCode

        fields = [
            self._make_scalar_field("id", TypeCode.INT64),
            self._make_scalar_field("name", TypeCode.STRING),
        ]
        metadata = self._make_result_set_metadata(fields)
        value_id = self._make_value(42)
        value_name = self._make_value("Answer")

        partial_result_set = self._make_partial_result_set(
            [value_id, value_name], metadata=metadata, last=True
        )
        iterator = _MockCancellableIterator(partial_result_set)
        streamed = self._make_one(iterator, lazy_decode=True)
        rows = [row async for row in streamed]
        self.assertEqual(streamed.decode_column(rows[0], 0), 42)
        self.assertEqual(streamed.decode_column(rows[0], 1), "Answer")

    @CrossSync.pytest
    async def test_decoders_not_started(self):
        iterator = _MockCancellableIterator()
        streamed = self._make_one(iterator)
        with self.assertRaises(ValueError):
            _ = streamed._decoders

    @CrossSync.pytest
    async def test_merge_struct_null_last(self):
        from google.protobuf.struct_pb2 import ListValue, Value

        from google.cloud.spanner_v1._async.streamed import _merge_struct
        from google.cloud.spanner_v1.types.type import Type, TypeCode

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


class _MockCancellableIterator(object):
    cancel_calls = 0

    def __init__(self, *values):
        self.iter_values = iter(values)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iter_values)
        except StopIteration:
            raise StopAsyncIteration


@CrossSync.convert_class(
    replace_symbols={
        "google.cloud.spanner_v1._async": "google.cloud.spanner_v1",
        "tests.unit._async": "tests.unit",
        "IsolatedAsyncioTestCase": "IsolatedAsyncioTestCase",
        "CrossSync.Mock": "mock.Mock",
    }
)
class TestStreamedResultSet_JSON_acceptance_tests(IsolatedAsyncioTestCase):
    _json_tests = None

    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.streamed import StreamedResultSet

        return StreamedResultSet

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _load_json_test(self, test_name):
        import os

        if self.__class__._json_tests is None:
            dirname = os.path.dirname(__file__)
            if os.path.basename(dirname) == "_async":
                dirname = os.path.dirname(dirname)
            filename = os.path.join(dirname, "streaming-read-acceptance-test.json")
            raw = _parse_streaming_read_acceptance_tests(filename)
            tests = self.__class__._json_tests = {}
            for name, partial_result_sets, results in raw:
                tests[name] = partial_result_sets, results
        return self.__class__._json_tests[test_name]

    # Non-error cases

    async def _match_results(self, testcase_name, assert_equality=None):
        partial_result_sets, expected = self._load_json_test(testcase_name)
        iterator = _MockCancellableIterator(*partial_result_sets)
        partial = self._make_one(iterator)
        if assert_equality is not None:
            assert_equality([i async for i in partial], expected)
        else:
            self.assertEqual([i async for i in partial], expected)

    @CrossSync.pytest
    async def test_basic(self):
        await self._match_results("Basic Test")

    @CrossSync.pytest
    async def test_string_chunking(self):
        await self._match_results("String Chunking Test")

    @CrossSync.pytest
    async def test_string_array_chunking(self):
        await self._match_results("String Array Chunking Test")

    @CrossSync.pytest
    async def test_string_array_chunking_with_nulls(self):
        await self._match_results("String Array Chunking Test With Nulls")

    @CrossSync.pytest
    async def test_string_array_chunking_with_empty_strings(self):
        await self._match_results("String Array Chunking Test With Empty Strings")

    @CrossSync.pytest
    async def test_string_array_chunking_with_one_large_string(self):
        await self._match_results("String Array Chunking Test With One Large String")

    @CrossSync.pytest
    async def test_int64_array_chunking(self):
        await self._match_results("INT64 Array Chunking Test")

    @CrossSync.pytest
    async def test_float64_array_chunking(self):
        import math

        def assert_float_equality(lhs, rhs):
            # NaN, +Inf, and -Inf can't be tested for equality
            if lhs is None:
                self.assertIsNone(rhs)
            elif math.isnan(lhs):
                self.assertTrue(math.isnan(rhs))
            elif math.isinf(lhs):
                self.assertTrue(math.isinf(rhs))
                # but +Inf and -Inf can be tested for magnitude
                self.assertTrue((lhs > 0) == (rhs > 0))
            else:
                self.assertEqual(lhs, rhs)

        def assert_rows_equality(lhs, rhs):
            self.assertEqual(len(lhs), len(rhs))
            for l_rows, r_rows in zip(lhs, rhs):
                self.assertEqual(len(l_rows), len(r_rows))
                for l_row, r_row in zip(l_rows, r_rows):
                    self.assertEqual(len(l_row), len(r_row))
                    for l_cell, r_cell in zip(l_row, r_row):
                        assert_float_equality(l_cell, r_cell)

        await self._match_results("FLOAT64 Array Chunking Test", assert_rows_equality)

    @CrossSync.pytest
    async def test_struct_array_chunking(self):
        await self._match_results("Struct Array Chunking Test")

    @CrossSync.pytest
    async def test_nested_struct_array(self):
        await self._match_results("Nested Struct Array Test")

    @CrossSync.pytest
    async def test_nested_struct_array_chunking(self):
        await self._match_results("Nested Struct Array Chunking Test")

    @CrossSync.pytest
    async def test_struct_array_and_string_chunking(self):
        await self._match_results("Struct Array And String Chunking Test")

    @CrossSync.pytest
    async def test_multiple_row_single_chunk(self):
        await self._match_results("Multiple Row Single Chunk")

    @CrossSync.pytest
    async def test_multiple_row_multiple_chunks(self):
        await self._match_results("Multiple Row Multiple Chunks")

    @CrossSync.pytest
    async def test_multiple_row_chunks_non_chunks_interleaved(self):
        await self._match_results("Multiple Row Chunks/Non Chunks Interleaved")

    @CrossSync.pytest
    async def test_json_array_chunking(self):
        await self._match_results("JSON Array Chunking Test")

    @CrossSync.pytest
    async def test_numeric_array_chunking(self):
        await self._match_results("NUMERIC Array Chunking Test")

    @CrossSync.pytest
    async def test_nested_struct_array_chunking_with_null(self):
        await self._match_results("Nested Struct Array Chunking Test With null")


def _generate_partial_result_sets(prs_text_pbs):
    from google.cloud.spanner_v1 import PartialResultSet

    partial_result_sets = []

    for prs_text_pb in prs_text_pbs:
        prs = PartialResultSet.from_json(prs_text_pb)
        partial_result_sets.append(prs)

    return partial_result_sets


def _normalize_int_array(cell):
    normalized = []
    for subcell in cell:
        if subcell is not None:
            subcell = int(subcell)
        normalized.append(subcell)
    return normalized


def _normalize_float(cell):
    if cell == "Infinity":
        return float("inf")
    if cell == "-Infinity":
        return float("-inf")
    if cell == "NaN":
        return float("nan")
    if cell is not None:
        return float(cell)


def _normalize_results(rows_data, fields):
    """Helper for _parse_streaming_read_acceptance_tests"""
    import decimal

    from google.cloud.spanner_v1 import JsonObject, TypeCode

    normalized = []
    for row_data in rows_data:
        row = []
        assert len(row_data) == len(fields)
        for cell, field in zip(row_data, fields):
            if field.type_.code == TypeCode.INT64:
                cell = int(cell) if cell is not None else None
            elif field.type_.code == TypeCode.FLOAT64:
                cell = _normalize_float(cell)
            elif field.type_.code == TypeCode.NUMERIC:
                cell = decimal.Decimal(cell) if cell is not None else None
            elif field.type_.code == TypeCode.JSON:
                cell = JsonObject.from_str(cell) if cell is not None else None
            elif field.type_.code == TypeCode.BYTES:
                cell = cell.encode("utf8") if cell is not None else None
            elif field.type_.code == TypeCode.ARRAY:
                if cell is None:
                    pass
                elif field.type_.array_element_type.code == TypeCode.INT64:
                    cell = _normalize_int_array(cell)
                elif field.type_.array_element_type.code == TypeCode.FLOAT64:
                    cell = [_normalize_float(subcell) for subcell in cell]
                elif field.type_.array_element_type.code == TypeCode.NUMERIC:
                    cell = [
                        decimal.Decimal(subcell) if subcell is not None else None
                        for subcell in cell
                    ]
                elif field.type_.array_element_type.code == TypeCode.JSON:
                    cell = [
                        JsonObject.from_str(subcell) if subcell is not None else None
                        for subcell in cell
                    ]
            row.append(cell)
        normalized.append(row)
    return normalized


def _parse_streaming_read_acceptance_tests(filename):
    """Parse acceptance tests from JSON

    See streaming-read-acceptance-test.json
    """
    import json

    with open(filename) as json_file:
        test_json = json.load(json_file)

    for test in test_json["tests"]:
        name = test["name"]
        partial_result_sets = _generate_partial_result_sets(test["chunks"])
        fields = partial_result_sets[0].metadata.row_type.fields
        result = _normalize_results(test["result"]["value"], fields)
        yield name, partial_result_sets, result
