# Copyright 2023 Google LLC All rights reserved.
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
from unittest import mock

from google.api_core.exceptions import Aborted

from google.cloud.spanner_dbapi.checksum import ResultsChecksum
from google.cloud.spanner_dbapi.exceptions import RetryAborted
from google.cloud.spanner_dbapi.parsed_statement import ParsedStatement, StatementType
from google.cloud.spanner_dbapi.transaction_helper import (
    CursorStatementType,
    ExecuteStatement,
    FetchStatement,
    ResultType,
    TransactionRetryHelper,
)


def _get_checksum(row):
    checksum = ResultsChecksum()
    checksum.consume_result(row)
    return checksum


SQL = "SELECT 1"
ARGS = []


class TestTransactionHelper(unittest.TestCase):
    @mock.patch("google.cloud.spanner_dbapi.cursor.Cursor")
    @mock.patch("google.cloud.spanner_dbapi.connection.Connection")
    def setUp(self, mock_connection, mock_cursor):
        self._under_test = TransactionRetryHelper(mock_connection)
        self._mock_cursor = mock_cursor

    def test_retry_transaction_execute(self):
        """
        Test retrying a transaction with an execute statement works.
        """
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.NONE,
            result_details=None,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor().execute = mock.Mock()

        self._under_test.retry_transaction()

        run_mock.assert_called_with(SQL, ARGS)

    def test_retry_transaction_dml_execute(self):
        """
        Test retrying a transaction with an execute DML statement works.
        """
        update_count = 3
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.ROW_COUNT,
            result_details=update_count,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor = mock.Mock()
        run_mock().rowcount = update_count

        self._under_test.retry_transaction()

        run_mock().execute.assert_called_with(SQL, ARGS)

    def test_retry_transaction_dml_execute_exception(self):
        """
        Test retrying a transaction with an execute DML statement with different
        row update count than original throws RetryAborted exception.
        """
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.ROW_COUNT,
            result_details=2,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor = mock.Mock()
        run_mock().rowcount = 3

        with self.assertRaises(RetryAborted):
            self._under_test.retry_transaction()

        run_mock().execute.assert_called_with(SQL, ARGS)

    def test_retry_transaction_execute_many(self):
        """
        Test retrying a transaction with an executemany on Query statement works.
        """
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE_MANY,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.NONE,
            result_details=None,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor().executemany = mock.Mock()

        self._under_test.retry_transaction()

        run_mock.assert_called_with(SQL, ARGS)

    def test_retry_transaction_dml_execute_many(self):
        """
        Test retrying a transaction with an executemany on DML statement works.
        """
        update_count = 3
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE_MANY,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.ROW_COUNT,
            result_details=update_count,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor = mock.Mock()
        run_mock().rowcount = update_count

        self._under_test.retry_transaction()

        run_mock().executemany.assert_called_with(SQL, ARGS)

    def test_retry_transaction_dml_executemany_exception(self):
        """
        Test retrying a transaction with an executemany DML statement with different
        row update count than original throws RetryAborted exception.
        """
        rows_inserted = [3, 4]
        self._mock_cursor._batch_dml_rows_count = rows_inserted
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE_MANY,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.BATCH_DML_ROWS_COUNT,
            result_details=rows_inserted,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor = mock.Mock()
        run_mock()._batch_dml_rows_count = [4, 3]

        with self.assertRaises(RetryAborted):
            self._under_test.retry_transaction()

        run_mock().executemany.assert_called_with(SQL, ARGS)

    def test_retry_transaction_fetchall(self):
        """
        Test retrying a transaction on a fetchall statement works.
        """
        result_row = ("field1", "field2")
        fetch_statement = FetchStatement(
            cursor=self._mock_cursor,
            statement_type=CursorStatementType.FETCH_ALL,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(result_row),
        )
        self._under_test._statement_result_details_list.append(fetch_statement)
        run_mock = self._under_test._connection.cursor().fetchall = mock.Mock()
        run_mock.return_value = [result_row]

        self._under_test.retry_transaction()

        run_mock.assert_called_with()

    def test_retry_transaction_fetchall_exception(self):
        """
        Test retrying a transaction on a fetchall statement throws exception
        when results is different from original in retry.
        """
        result_row = ("field1", "field2")
        fetch_statement = FetchStatement(
            cursor=self._mock_cursor,
            statement_type=CursorStatementType.FETCH_ALL,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(result_row),
        )
        self._under_test._statement_result_details_list.append(fetch_statement)
        run_mock = self._under_test._connection.cursor().fetchall = mock.Mock()
        retried_result_row = "field3"
        run_mock.return_value = [retried_result_row]

        with self.assertRaises(RetryAborted):
            self._under_test.retry_transaction()

        run_mock.assert_called_with()

    def test_retry_transaction_fetchmany(self):
        """
        Test retrying a transaction on a fetchmany statement works.
        """
        result_row = ("field1", "field2")
        fetch_statement = FetchStatement(
            cursor=self._mock_cursor,
            statement_type=CursorStatementType.FETCH_MANY,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(result_row),
            size=1,
        )
        self._under_test._statement_result_details_list.append(fetch_statement)
        run_mock = self._under_test._connection.cursor().fetchmany = mock.Mock()
        run_mock.return_value = [result_row]

        self._under_test.retry_transaction()

        run_mock.assert_called_with(1)

    def test_retry_transaction_fetchmany_exception(self):
        """
        Test retrying a transaction on a fetchmany statement throws exception
        when results is different from original in retry.
        """
        result_row = ("field1", "field2")
        fetch_statement = FetchStatement(
            cursor=self._mock_cursor,
            statement_type=CursorStatementType.FETCH_MANY,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(result_row),
            size=1,
        )
        self._under_test._statement_result_details_list.append(fetch_statement)
        run_mock = self._under_test._connection.cursor().fetchmany = mock.Mock()
        retried_result_row = "field3"
        run_mock.return_value = [retried_result_row]

        with self.assertRaises(RetryAborted):
            self._under_test.retry_transaction()

        run_mock.assert_called_with(1)

    def test_retry_transaction_same_exception(self):
        """
        Test retrying a transaction with statement throwing same exception in
        retry works.
        """
        exception = Exception("Test")
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.EXCEPTION,
            result_details=exception,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor().execute = mock.Mock()
        run_mock.side_effect = exception

        self._under_test.retry_transaction()

        run_mock.assert_called_with(SQL, ARGS)

    def test_retry_transaction_different_exception(self):
        """
        Test retrying a transaction with statement throwing different exception
        in retry results in RetryAborted exception.
        """
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.EXCEPTION,
            result_details=Exception("Test"),
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor().execute = mock.Mock()
        run_mock.side_effect = Exception("Test2")

        with self.assertRaises(RetryAborted):
            self._under_test.retry_transaction()

        run_mock.assert_called_with(SQL, ARGS)

    def test_retry_transaction_aborted_retry(self):
        """
        Check that in case of a retried transaction aborted,
        it will be retried once again.
        """
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.NONE,
            result_details=None,
        )
        self._under_test._statement_result_details_list.append(execute_statement)
        run_mock = self._under_test._connection.cursor().execute = mock.Mock()
        metadata_mock = mock.Mock()
        metadata_mock.trailing_metadata.return_value = {}
        run_mock.side_effect = [
            Aborted("Aborted", errors=[metadata_mock]),
            None,
        ]

        self._under_test.retry_transaction(default_retry_delay=0)

        run_mock.assert_has_calls(
            (
                mock.call(SQL, ARGS),
                mock.call(SQL, ARGS),
            )
        )

    def test_add_execute_statement_for_retry(self):
        """
        Test add_execute_statement_for_retry method works
        """
        self._mock_cursor._parsed_statement = ParsedStatement(
            statement_type=StatementType.INSERT, statement=None
        )

        sql = "INSERT INTO Table"
        rows_inserted = 3
        self._mock_cursor.rowcount = rows_inserted
        self._mock_cursor._batch_dml_rows_count = None
        self._under_test.add_execute_statement_for_retry(
            self._mock_cursor, sql, [], None, False
        )

        expected_statement_result_details = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=sql,
            args=[],
            result_type=ResultType.ROW_COUNT,
            result_details=rows_inserted,
        )
        self.assertEqual(
            self._under_test._last_statement_details_per_cursor,
            {self._mock_cursor: expected_statement_result_details},
        )
        self.assertEqual(
            self._under_test._statement_result_details_list,
            [expected_statement_result_details],
        )

    def test_add_execute_statement_for_retry_with_exception(self):
        """
        Test add_execute_statement_for_retry method with exception
        """
        self._mock_cursor._parsed_statement = ParsedStatement(
            statement_type=StatementType.INSERT, statement=None
        )
        self._mock_cursor.rowcount = -1

        sql = "INSERT INTO Table"
        exception = Exception("Test")
        self._under_test.add_execute_statement_for_retry(
            self._mock_cursor, sql, [], exception, False
        )

        expected_statement_result_details = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=sql,
            args=[],
            result_type=ResultType.EXCEPTION,
            result_details=exception,
        )
        self.assertEqual(
            self._under_test._last_statement_details_per_cursor,
            {self._mock_cursor: expected_statement_result_details},
        )
        self.assertEqual(
            self._under_test._statement_result_details_list,
            [expected_statement_result_details],
        )

    def test_add_execute_statement_for_retry_query_statement(self):
        """
        Test add_execute_statement_for_retry method works for non DML statement
        """
        self._mock_cursor._parsed_statement = ParsedStatement(
            statement_type=StatementType.QUERY, statement=None
        )
        self._mock_cursor._row_count = None
        self._mock_cursor._batch_dml_rows_count = None

        sql = "SELECT 1"
        self._under_test.add_execute_statement_for_retry(
            self._mock_cursor, sql, [], None, False
        )

        expected_statement_result_details = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=sql,
            args=[],
            result_type=ResultType.NONE,
            result_details=None,
        )
        self.assertEqual(
            self._under_test._last_statement_details_per_cursor,
            {self._mock_cursor: expected_statement_result_details},
        )
        self.assertEqual(
            self._under_test._statement_result_details_list,
            [expected_statement_result_details],
        )

    def test_add_execute_many_statement_for_retry(self):
        """
        Test add_execute_statement_for_retry method works for executemany
        """
        self._mock_cursor._parsed_statement = ParsedStatement(
            statement_type=StatementType.INSERT, statement=None
        )

        sql = "INSERT INTO Table"
        rows_inserted = [3, 4]
        self._mock_cursor._batch_dml_rows_count = rows_inserted
        self._under_test.add_execute_statement_for_retry(
            self._mock_cursor, sql, [], None, True
        )

        expected_statement_result_details = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE_MANY,
            cursor=self._mock_cursor,
            sql=sql,
            args=[],
            result_type=ResultType.BATCH_DML_ROWS_COUNT,
            result_details=rows_inserted,
        )
        self.assertEqual(
            self._under_test._last_statement_details_per_cursor,
            {self._mock_cursor: expected_statement_result_details},
        )
        self.assertEqual(
            self._under_test._statement_result_details_list,
            [expected_statement_result_details],
        )

    def test_add_fetch_statement_for_retry(self):
        """
        Test add_fetch_statement_for_retry method when last_statement_result_details is a
        Fetch statement
        """
        result_row = ("field1", "field2")
        result_checksum = _get_checksum(result_row)
        original_checksum_digest = result_checksum.checksum.digest()
        last_statement_result_details = FetchStatement(
            statement_type=CursorStatementType.FETCH_MANY,
            cursor=self._mock_cursor,
            result_type=ResultType.CHECKSUM,
            result_details=result_checksum,
            size=1,
        )
        self._under_test._last_statement_details_per_cursor = {
            self._mock_cursor: last_statement_result_details
        }
        new_rows = [("field3", "field4"), ("field5", "field6")]

        self._under_test.add_fetch_statement_for_retry(
            self._mock_cursor, new_rows, None, False
        )

        updated_last_statement_result_details = (
            self._under_test._last_statement_details_per_cursor.get(self._mock_cursor)
        )
        self.assertEqual(
            updated_last_statement_result_details.size,
            3,
        )
        self.assertNotEqual(
            updated_last_statement_result_details.result_details.checksum.digest(),
            original_checksum_digest,
        )

    def test_add_fetch_statement_for_retry_with_exception(self):
        """
        Test add_fetch_statement_for_retry method with exception
        """
        result_row = ("field1", "field2")
        fetch_statement = FetchStatement(
            statement_type=CursorStatementType.FETCH_MANY,
            cursor=self._mock_cursor,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(result_row),
            size=1,
        )
        self._under_test._last_statement_details_per_cursor = {
            self._mock_cursor: fetch_statement
        }
        exception = Exception("Test")

        self._under_test.add_fetch_statement_for_retry(
            self._mock_cursor, [], exception, False
        )

        self.assertEqual(
            self._under_test._last_statement_details_per_cursor.get(self._mock_cursor),
            FetchStatement(
                statement_type=CursorStatementType.FETCH_MANY,
                cursor=self._mock_cursor,
                result_type=ResultType.EXCEPTION,
                result_details=exception,
                size=1,
            ),
        )

    def test_add_fetch_statement_for_retry_last_statement_not_exists(self):
        """
        Test add_fetch_statement_for_retry method when last_statement_result_details
        doesn't exists
        """
        row = ("field3", "field4")

        self._under_test.add_fetch_statement_for_retry(
            self._mock_cursor, [row], None, False
        )

        expected_statement = FetchStatement(
            statement_type=CursorStatementType.FETCH_MANY,
            cursor=self._mock_cursor,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(row),
            size=1,
        )
        self.assertEqual(
            self._under_test._last_statement_details_per_cursor,
            {self._mock_cursor: expected_statement},
        )
        self.assertEqual(
            self._under_test._statement_result_details_list,
            [expected_statement],
        )

    def test_add_fetch_statement_for_retry_fetch_all_statement(self):
        """
        Test add_fetch_statement_for_retry method for fetchall statement
        """
        row = ("field3", "field4")

        self._under_test.add_fetch_statement_for_retry(
            self._mock_cursor, [row], None, True
        )

        expected_statement = FetchStatement(
            statement_type=CursorStatementType.FETCH_ALL,
            cursor=self._mock_cursor,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(row),
        )
        self.assertEqual(
            self._under_test._last_statement_details_per_cursor,
            {self._mock_cursor: expected_statement},
        )
        self.assertEqual(
            self._under_test._statement_result_details_list,
            [expected_statement],
        )

    def test_add_fetch_statement_for_retry_when_last_statement_is_not_fetch(self):
        """
        Test add_fetch_statement_for_retry method when last statement is not
        a fetch type of statement
        """
        execute_statement = ExecuteStatement(
            statement_type=CursorStatementType.EXECUTE,
            cursor=self._mock_cursor,
            sql=SQL,
            args=ARGS,
            result_type=ResultType.ROW_COUNT,
            result_details=2,
        )
        self._under_test._last_statement_details_per_cursor = {
            self._mock_cursor: execute_statement
        }
        self._under_test._statement_result_details_list.append(execute_statement)
        row = ("field3", "field4")

        self._under_test.add_fetch_statement_for_retry(
            self._mock_cursor, [row], None, False
        )

        expected_fetch_statement = FetchStatement(
            statement_type=CursorStatementType.FETCH_MANY,
            cursor=self._mock_cursor,
            result_type=ResultType.CHECKSUM,
            result_details=_get_checksum(row),
            size=1,
        )
        self.assertEqual(
            self._under_test._last_statement_details_per_cursor,
            {self._mock_cursor: expected_fetch_statement},
        )
        self.assertEqual(
            self._under_test._statement_result_details_list,
            [execute_statement, expected_fetch_statement],
        )
