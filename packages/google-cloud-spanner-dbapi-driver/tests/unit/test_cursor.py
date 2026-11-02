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
import uuid
from unittest import mock

from google.cloud.spanner_v1 import ExecuteSqlRequest, TypeCode
from google.cloud.spanner_v1.types import StructField, Type

from google.cloud.spanner_driver import cursor


class TestCursor(unittest.TestCase):
    def setUp(self):
        self.mock_connection = mock.Mock()
        self.mock_internal_conn = mock.Mock()
        self.mock_connection._internal_conn = self.mock_internal_conn
        self.cursor = cursor.Cursor(self.mock_connection)

    def test_init(self):
        self.assertEqual(self.cursor._connection, self.mock_connection)

    def test_execute(self):
        operation = "SELECT * FROM table"
        mock_rows = mock.Mock()
        # Mocking description to be None so it treats as DML or query with no
        # result initially? If description calls metadata(), we need to mock
        # that. logic: if self.description: self._rowcount = -1

        # Scenario 1: SELECT query (returns rows)
        mock_metadata = mock.Mock()
        mock_metadata.row_type.fields = [
            StructField(name="col1", type_=Type(code=TypeCode.INT64))
        ]
        mock_rows.metadata.return_value = mock_metadata
        self.mock_internal_conn.execute.return_value = mock_rows

        self.cursor.execute(operation)

        self.mock_internal_conn.execute.assert_called_once()
        call_args = self.mock_internal_conn.execute.call_args
        self.assertIsInstance(call_args[0][0], ExecuteSqlRequest)
        self.assertEqual(call_args[0][0].sql, operation)
        self.assertEqual(self.cursor._rowcount, -1)
        self.assertEqual(self.cursor._rows, mock_rows)

    def test_execute_dml(self):
        operation = "UPDATE table SET col=1"
        mock_rows = mock.Mock()
        # Returns empty metadata or no metadata for DML?
        # Actually in Spanner, DML returns a ResultSet with stats.
        # But here we check `if self.description`.

        # Scenario 2: DML (no fields in metadata usually, or we can simulate
        # it) If metadata calls fail or return empty, description returns
        # usually None.
        mock_rows.metadata.return_value = None
        mock_rows.update_count.return_value = 10
        self.mock_internal_conn.execute.return_value = mock_rows

        self.cursor.execute(operation)

        self.assertEqual(self.cursor._rowcount, 10)
        # rows should be closed and set to None for DML in this driver
        # implementation
        mock_rows.close.assert_called_once()
        self.assertIsNone(self.cursor._rows)

    def test_execute_with_params(self):
        operation = "SELECT * FROM table WHERE id=@id"
        params = {"id": 1}
        mock_rows = mock.Mock()
        mock_rows.metadata.return_value = mock.Mock()
        self.mock_internal_conn.execute.return_value = mock_rows

        self.cursor.execute(operation, params)

        call_args = self.mock_internal_conn.execute.call_args
        request = call_args[0][0]
        self.assertEqual(request.sql, operation)
        self.assertEqual(request.sql, operation)
        self.assertEqual(request.params, {"id": "1"})

    def test_executemany(self):
        operation = "INSERT INTO table (id) VALUES (@id)"
        params_seq = [{"id": 1, "name": "val1"}, {"id": 2}]

        # Mock execute_batch response
        mock_response = mock.Mock()
        mock_result_set1 = mock.Mock()
        mock_result_set1.stats.row_count_exact = 1
        mock_result_set2 = mock.Mock()
        mock_result_set2.stats.row_count_exact = 1
        mock_response.result_sets = [mock_result_set1, mock_result_set2]

        self.mock_internal_conn.execute_batch.return_value = mock_response

        # Patch ExecuteBatchDmlRequest in cursor module
        with mock.patch(
            "google.cloud.spanner_driver.cursor.ExecuteBatchDmlRequest"
        ) as MockRequest:
            # Setup mock request instance and statements list behavior
            mock_request_instance = MockRequest.return_value
            mock_request_instance.statements = []  # Use a real list to verify append

            # Setup Statement mock
            MockStatement = mock.Mock()
            MockRequest.Statement = MockStatement

            self.cursor.executemany(operation, params_seq)

            # Verify execute_batch called with our mock request
            self.mock_internal_conn.execute_batch.assert_called_once_with(
                mock_request_instance
            )

            # Verify statements were created and appended
            self.assertEqual(len(mock_request_instance.statements), 2)

            # Verify first statement
            call1 = MockStatement.call_args_list[0]
            self.assertEqual(call1.kwargs["sql"], operation)

            self.assertEqual(MockStatement.call_count, 2)

            # Verify rowcount update
            self.assertEqual(self.cursor.rowcount, 2)

    def test_fetchone(self):
        mock_rows = mock.Mock()
        self.cursor._rows = mock_rows

        # Mock metadata for type information
        mock_metadata = mock.Mock()
        mock_metadata.row_type.fields = [
            StructField(name="col1", type_=Type(code=TypeCode.INT64))
        ]
        mock_rows.metadata.return_value = mock_metadata
        mock_rows.metadata.return_value = mock_metadata

        # Mock row as object with values attribute
        mock_row = mock.Mock()
        mock_val = mock.Mock()
        mock_val.WhichOneof.return_value = "string_value"
        mock_val.string_value = "1"
        mock_row.values = [mock_val]

        mock_rows.next.return_value = mock_row

        row = self.cursor.fetchone()
        self.assertEqual(row, (1,))
        mock_rows.next.assert_called_once()

    def test_fetchone_empty(self):
        mock_rows = mock.Mock()
        self.cursor._rows = mock_rows
        mock_rows.next.side_effect = StopIteration

        row = self.cursor.fetchone()
        self.assertIsNone(row)

    def test_fetchmany(self):
        mock_rows = mock.Mock()
        self.cursor._rows = mock_rows

        # Metadata
        mock_metadata = mock.Mock()
        mock_metadata.row_type.fields = [
            StructField(name="col1", type_=Type(code=TypeCode.INT64))
        ]
        mock_rows.metadata.return_value = mock_metadata
        mock_rows.metadata.return_value = mock_metadata

        # Rows
        mock_row1 = mock.Mock()
        v1 = mock.Mock()
        v1.WhichOneof.return_value = "string_value"
        v1.string_value = "1"
        mock_row1.values = [v1]

        mock_row2 = mock.Mock()
        v2 = mock.Mock()
        v2.WhichOneof.return_value = "string_value"
        v2.string_value = "2"
        mock_row2.values = [v2]

        mock_rows.next.side_effect = [mock_row1, mock_row2, StopIteration]

        rows = self.cursor.fetchmany(size=5)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows, [(1,), (2,)])

    def test_fetchall(self):
        mock_rows = mock.Mock()
        self.cursor._rows = mock_rows

        # Metadata
        mock_metadata = mock.Mock()
        mock_metadata.row_type.fields = [
            StructField(name="col1", type_=Type(code=TypeCode.INT64))
        ]
        mock_rows.metadata.return_value = mock_metadata
        mock_rows.metadata.return_value = mock_metadata

        # Rows
        mock_row1 = mock.Mock()
        v1 = mock.Mock()
        v1.WhichOneof.return_value = "string_value"
        v1.string_value = "1"
        mock_row1.values = [v1]

        mock_row2 = mock.Mock()
        v2 = mock.Mock()
        v2.WhichOneof.return_value = "string_value"
        v2.string_value = "2"
        mock_row2.values = [v2]

        mock_rows.next.side_effect = [mock_row1, mock_row2, StopIteration]

        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 2)

    def test_description(self):
        mock_rows = mock.Mock()
        self.cursor._rows = mock_rows

        mock_metadata = mock.Mock()
        mock_metadata.row_type.fields = [
            StructField(name="col1", type_=Type(code=TypeCode.INT64)),
            StructField(name="col2", type_=Type(code=TypeCode.STRING)),
        ]
        mock_rows.metadata.return_value = mock_metadata

        desc = self.cursor.description
        self.assertEqual(len(desc), 2)
        self.assertEqual(desc[0][0], "col1")
        self.assertEqual(desc[1][0], "col2")

    def test_close(self):
        mock_rows = mock.Mock()
        self.cursor._rows = mock_rows

        self.cursor.close()

        self.assertTrue(self.cursor._closed)
        mock_rows.close.assert_called_once()

    def test_context_manager(self):
        with self.cursor as c:
            self.assertEqual(c, self.cursor)
        self.assertTrue(self.cursor._closed)

    def test_iterator(self):
        mock_rows = mock.Mock()
        self.cursor._rows = mock_rows

        mock_metadata = mock.Mock()
        mock_metadata.row_type.fields = [
            StructField(name="col1", type_=Type(code=TypeCode.INT64))
        ]
        mock_rows.metadata.return_value = mock_metadata
        mock_rows.metadata.return_value = mock_metadata

        mock_row = mock.Mock()
        v1 = mock.Mock()
        v1.WhichOneof.return_value = "string_value"
        v1.string_value = "1"
        mock_row.values = [v1]

        mock_rows.next.side_effect = [mock_row, StopIteration]

        # __next__ calls fetchone
        it = iter(self.cursor)
        self.assertEqual(next(it), (1,))
        with self.assertRaises(StopIteration):
            next(it)

    def test_prepare_params(self):
        # Test 1: None
        converted, types = self.cursor._prepare_params(None)
        self.assertEqual(converted, {})
        self.assertEqual(types, {})

        # Test 2: Dict (GoogleSQL)
        uuid_val = uuid.uuid4()
        dt_val = datetime.datetime(2024, 1, 1, 12, 0, 0)
        date_val = datetime.date(2024, 1, 1)
        params = {
            "int_val": 123,
            "bool_val": True,
            "float_val": 1.23,
            "bytes_val": b"bytes",
            "str_val": "string",
            "uuid_val": uuid_val,
            "dt_val": dt_val,
            "date_val": date_val,
            "none_val": None,
        }
        converted, types = self.cursor._prepare_params(params)

        self.assertEqual(converted["int_val"], "123")
        self.assertEqual(types["int_val"].code, TypeCode.INT64)

        self.assertEqual(converted["bool_val"], True)
        self.assertEqual(types["bool_val"].code, TypeCode.BOOL)

        self.assertEqual(converted["float_val"], 1.23)
        self.assertEqual(types["float_val"].code, TypeCode.FLOAT64)

        self.assertEqual(converted["bytes_val"], b"bytes")
        self.assertEqual(types["bytes_val"].code, TypeCode.BYTES)

        self.assertEqual(converted["str_val"], "string")
        self.assertEqual(types["str_val"].code, TypeCode.STRING)

        self.assertEqual(converted["uuid_val"], str(uuid_val))
        self.assertEqual(types["uuid_val"].code, TypeCode.STRING)

        self.assertEqual(converted["dt_val"], str(dt_val))
        self.assertEqual(types["dt_val"].code, TypeCode.TIMESTAMP)

        self.assertEqual(converted["date_val"], str(date_val))
        self.assertEqual(types["date_val"].code, TypeCode.DATE)

        self.assertIsNone(converted["none_val"])
        self.assertNotIn("none_val", types)

        # Test 3: List (PostgreSQL)
        params_list = [1, "test"]
        converted, types = self.cursor._prepare_params(params_list)

        self.assertEqual(converted["P1"], "1")
        self.assertEqual(types["P1"].code, TypeCode.INT64)

        self.assertEqual(converted["P2"], "test")
        self.assertEqual(types["P2"].code, TypeCode.STRING)

    def test_prepare_params_unsupported_type(self):
        with self.assertRaises(cursor.errors.ProgrammingError):
            self.cursor._prepare_params(123)  # Int is not supported directly
