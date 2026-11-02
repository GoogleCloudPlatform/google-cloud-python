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

"""Cursor() class unit tests."""

import sys
import unittest
from unittest import mock

from google.api_core.exceptions import Aborted
from google.auth.credentials import AnonymousCredentials
from google.rpc.code_pb2 import ABORTED

from google.cloud.spanner_dbapi.connection import connect
from google.cloud.spanner_dbapi.parsed_statement import (
    ParsedStatement,
    Statement,
    StatementType,
)


class TestCursor(unittest.TestCase):
    INSTANCE = "test-instance"
    DATABASE = "test-database"

    def _get_target_class(self):
        from google.cloud.spanner_dbapi import Cursor

        return Cursor

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def _make_connection(self, *args, **kwargs):
        from google.cloud.spanner_dbapi import Connection

        return Connection(*args, **kwargs)

    def _transaction_mock(self, mock_response=[]):
        from google.rpc.code_pb2 import OK

        transaction = mock.Mock()
        transaction.batch_update = mock.Mock(
            return_value=[mock.Mock(code=OK), mock_response]
        )
        return transaction

    def test_property_connection(self):
        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)
        self.assertEqual(cursor.connection, connection)

    def test_property_description(self):
        from google.cloud.spanner_dbapi._helpers import ColumnInfo

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)

        self.assertIsNone(cursor.description)
        cursor._result_set = res_set = mock.MagicMock()
        res_set.metadata.row_type.fields = [mock.MagicMock()]
        self.assertIsNotNone(cursor.description)
        self.assertIsInstance(cursor.description[0], ColumnInfo)

    def test_property_rowcount(self):
        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)

        self.assertEqual(cursor.rowcount, None)

    def test_callproc(self):
        from google.cloud.spanner_dbapi.exceptions import InterfaceError

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)
        cursor._is_closed = True
        with self.assertRaises(InterfaceError):
            cursor.callproc(procname=None)

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_close(self, mock_client):
        from google.cloud.spanner_dbapi import InterfaceError, connect

        connection = connect(self.INSTANCE, self.DATABASE)

        cursor = connection.cursor()
        self.assertFalse(cursor.is_closed)

        cursor.close()

        self.assertTrue(cursor.is_closed)

        with self.assertRaises(InterfaceError):
            cursor.execute("SELECT * FROM database")

    def test_do_execute_update(self):
        from google.cloud.spanner_v1 import ResultSetStats

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)
        transaction = mock.MagicMock()
        result_set = mock.MagicMock()
        result_set.stats = ResultSetStats(row_count_exact=1234)

        transaction.execute_sql.return_value = result_set
        cursor._do_execute_update_in_autocommit(
            transaction=transaction,
            sql="SELECT * WHERE true",
            params={},
        )

        self.assertEqual(cursor._result_set, result_set)
        self.assertEqual(cursor.rowcount, 1234)

    def test_do_execute_update_in_autocommit_eagerly_buffers_returning_rows(self):
        from google.cloud.spanner_v1 import ResultSetStats, Type, TypeCode
        from google.cloud.spanner_v1.types import ResultSetMetadata, StructType

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        connection.autocommit = True
        cursor = self._make_one(connection)

        tx_active = True

        def streaming_generator():
            if not tx_active:
                raise ValueError(
                    "Transaction has already been committed or rolled back"
                )
            yield [1, "Alice"]
            if not tx_active:
                raise ValueError(
                    "Transaction has already been committed or rolled back"
                )
            yield [2, "Bob"]

        field1 = StructType.Field(name="id", type=Type(code=TypeCode.INT64))
        field2 = StructType.Field(name="name", type=Type(code=TypeCode.STRING))
        row_type = StructType(fields=[field1, field2])
        metadata = ResultSetMetadata(row_type=row_type)

        mock_result_set = mock.MagicMock()
        mock_result_set.__iter__.side_effect = streaming_generator
        mock_result_set.metadata = metadata
        mock_result_set.stats = ResultSetStats(row_count_exact=2)

        def fake_run_in_transaction(func, *args, **kwargs):
            nonlocal tx_active
            mock_tx = mock.MagicMock()
            mock_tx.execute_sql.return_value = mock_result_set
            result = func(mock_tx, *args, **kwargs)
            tx_active = False
            return result

        connection.database.run_in_transaction = fake_run_in_transaction

        sql = "INSERT INTO table (id, name) VALUES (1, 'Alice'), (2, 'Bob') THEN RETURN id, name"
        cursor.execute(sql)

        self.assertIsNotNone(cursor.description)
        self.assertEqual(len(cursor.description), 2)
        self.assertEqual(cursor.description[0].name, "id")
        self.assertEqual(cursor.description[1].name, "name")
        self.assertEqual(cursor.rowcount, 2)
        self.assertEqual(cursor.fetchall(), [(1, "Alice"), (2, "Bob")])

    def test_do_batch_update(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.param_types import INT64
        from google.cloud.spanner_v1.types.spanner import Session

        sql = "DELETE FROM table WHERE col1 = %s"

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        connection.autocommit = True
        transaction = self._transaction_mock(mock_response=[1, 1, 1])
        cursor = connection.cursor()

        with mock.patch(
            "google.cloud.spanner_v1.services.spanner.client.SpannerClient.create_session",
            return_value=Session(),
        ):
            with mock.patch(
                "google.cloud.spanner_v1.session.Session.transaction",
                return_value=transaction,
            ):
                cursor.executemany(sql, [(1,), (2,), (3,)])

        transaction.batch_update.assert_called_once_with(
            [
                ("DELETE FROM table WHERE col1 = @a0", {"a0": 1}, {"a0": INT64}),
                ("DELETE FROM table WHERE col1 = @a0", {"a0": 2}, {"a0": INT64}),
                ("DELETE FROM table WHERE col1 = @a0", {"a0": 3}, {"a0": INT64}),
            ],
            last_statement=True,
        )
        self.assertEqual(cursor._row_count, 3)

    def test_execute_programming_error(self):
        from google.cloud.spanner_dbapi.exceptions import ProgrammingError

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)
        cursor.connection = None
        with self.assertRaises(ProgrammingError):
            cursor.execute(sql="")

    def test_execute_attribute_error(self):
        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)

        with self.assertRaises(AttributeError):
            cursor.execute(sql="SELECT 1")

    def test_execute_database_error(self):
        connection = self._make_connection(self.INSTANCE)
        cursor = self._make_one(connection)

        with self.assertRaises(ValueError):
            cursor.execute(sql="SELECT 1")

    def test_execute_autocommit_off(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor.connection._autocommit = False
        cursor.connection.transaction_checkout = mock.MagicMock(autospec=True)

        cursor.execute("sql")
        self.assertIsInstance(cursor._result_set, mock.MagicMock)

    def test_execute_insert_statement_autocommit_off(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor.connection._autocommit = False
        cursor.connection.transaction_checkout = mock.MagicMock(autospec=True)

        sql = "INSERT INTO django_migrations (app, name, applied) VALUES (%s, %s, %s)"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            with mock.patch(
                "google.cloud.spanner_dbapi.connection.Connection.run_statement",
                return_value=(mock.MagicMock()),
            ):
                cursor.execute(sql)
                self.assertIsInstance(cursor._result_set, mock.MagicMock)

    def test_execute_statement(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)

        sql = "sql"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            side_effect=[
                ParsedStatement(StatementType.DDL, Statement(sql)),
                ParsedStatement(StatementType.UPDATE, Statement(sql)),
            ],
        ) as mockclassify_statement:
            with self.assertRaises(ValueError):
                cursor.execute(sql=sql)
            mockclassify_statement.assert_called_with(sql)
            self.assertEqual(mockclassify_statement.call_count, 2)
            self.assertEqual(cursor.connection._ddl_statements, [])

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.DDL, Statement(sql)),
        ) as mockclassify_statement:
            sql = "sql"
            cursor.execute(sql=sql)
            mockclassify_statement.assert_called_with(sql)
            self.assertEqual(mockclassify_statement.call_count, 2)
            self.assertEqual(cursor.connection._ddl_statements, [sql])

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            with mock.patch(
                "google.cloud.spanner_dbapi.cursor.Cursor._handle_DQL",
                return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
            ) as mock_handle_ddl:
                connection.autocommit = True
                sql = "sql"
                cursor.execute(sql=sql)
                mock_handle_ddl.assert_called_once_with(sql, None)

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.connection._database = mock_db = mock.MagicMock()
            mock_db.run_in_transaction = mock_run_in = mock.MagicMock()
            cursor.execute(sql="sql")
            mock_run_in.assert_called_once_with(
                cursor._do_execute_update_in_autocommit, "sql", None
            )

    def test_execute_statement_with_cursor_not_in_retry_mode(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            cursor.execute(sql=sql)

        transaction_helper_mock.add_execute_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_not_called()

    def test_executemany_query_statement_with_cursor_not_in_retry_mode(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            cursor.executemany(operation=sql, seq_of_params=[])

        transaction_helper_mock.add_execute_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_not_called()

    def test_executemany_dml_statement_with_cursor_not_in_retry_mode(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.INSERT, Statement(sql)),
        ):
            cursor.executemany(operation=sql, seq_of_params=[])

        transaction_helper_mock.add_execute_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_not_called()

    def test_execute_statement_with_cursor_in_retry_mode(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor._in_retry_mode = True
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            cursor.execute(sql=sql)

        transaction_helper_mock.add_execute_statement_for_retry.assert_not_called()
        transaction_helper_mock.retry_transaction.assert_not_called()

    def test_executemany_statement_with_cursor_in_retry_mode(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor._in_retry_mode = True
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            cursor.executemany(operation=sql, seq_of_params=[])

        transaction_helper_mock.add_execute_statement_for_retry.assert_not_called()
        transaction_helper_mock.retry_transaction.assert_not_called()

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_statement_aborted_with_cursor_not_in_retry_mode(
        self, mock_peek_iterator
    ):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            connection.run_statement = mock.Mock(
                side_effect=(Aborted("Aborted"), None),
            )
            cursor.execute(sql=sql)

        transaction_helper_mock.add_execute_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_called_once()

    def test_execute_statement_aborted_with_cursor_in_retry_mode(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor._in_retry_mode = True
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            connection.run_statement = mock.Mock(
                side_effect=Aborted("Aborted"),
            )
            with self.assertRaises(Aborted):
                cursor.execute(sql=sql)

        transaction_helper_mock.add_execute_statement_for_retry.assert_not_called()
        transaction_helper_mock.retry_transaction.assert_not_called()

    def test_execute_statement_exception_with_cursor_not_in_retry_mode(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        sql = "sql"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement(sql)),
        ):
            connection.run_statement = mock.Mock(
                side_effect=(Exception("Exception"), None),
            )
            with self.assertRaises(Exception):
                cursor.execute(sql=sql)

        transaction_helper_mock.add_execute_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_not_called()

    def test_execute_integrity_error(self):
        from google.api_core import exceptions

        from google.cloud.spanner_dbapi.exceptions import IntegrityError

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            side_effect=exceptions.AlreadyExists("message"),
        ):
            with self.assertRaises(IntegrityError):
                cursor.execute(sql="sql")

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            side_effect=exceptions.FailedPrecondition("message"),
        ):
            with self.assertRaises(IntegrityError):
                cursor.execute(sql="sql")

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            side_effect=exceptions.OutOfRange("message"),
        ):
            with self.assertRaises(IntegrityError):
                cursor.execute("sql")

    def test_execute_invalid_argument(self):
        from google.api_core import exceptions

        from google.cloud.spanner_dbapi.exceptions import ProgrammingError

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            side_effect=exceptions.InvalidArgument("message"),
        ):
            with self.assertRaises(ProgrammingError):
                cursor.execute(sql="sql")

    def test_execute_internal_server_error(self):
        from google.api_core import exceptions

        from google.cloud.spanner_dbapi.exceptions import OperationalError

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            side_effect=exceptions.InternalServerError("message"),
        ):
            with self.assertRaises(OperationalError):
                cursor.execute(sql="sql")

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_executemany_on_closed_cursor(self, mock_client):
        from google.cloud.spanner_dbapi import InterfaceError, connect

        connection = connect("test-instance", "test-database")

        cursor = connection.cursor()
        cursor.close()

        with self.assertRaises(InterfaceError):
            cursor.executemany("""SELECT * FROM table1 WHERE "col1" = @a1""", ())

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_executemany_DLL(self, mock_client):
        from google.cloud.spanner_dbapi import ProgrammingError, connect

        connection = connect("test-instance", "test-database")

        cursor = connection.cursor()

        with self.assertRaises(ProgrammingError):
            cursor.executemany("""DROP DATABASE database_name""", ())

    def test_executemany_client_statement(self):
        from google.cloud.spanner_dbapi import ProgrammingError, connect

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        cursor = connection.cursor()

        with self.assertRaises(ProgrammingError) as error:
            cursor.executemany("""COMMIT TRANSACTION""", ())
        self.assertEqual(
            str(error.exception),
            "Executing the following operation: COMMIT TRANSACTION, with executemany() method is not allowed.",
        )

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_executemany(self, mock_client):
        from google.cloud.spanner_dbapi import connect

        operation = """SELECT * FROM table1 WHERE "col1" = @a1"""
        params_seq = ((1,), (2,))

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        cursor = connection.cursor()
        cursor._result_set = [1, 2, 3]
        cursor._itr = iter([1, 2, 3])

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor._execute"
        ) as execute_mock:
            cursor.executemany(operation, params_seq)

        execute_mock.assert_has_calls(
            (mock.call(operation, (1,), True), mock.call(operation, (2,), True))
        )

    def test_executemany_delete_batch_autocommit(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.param_types import INT64
        from google.cloud.spanner_v1.types.spanner import Session

        sql = "DELETE FROM table WHERE col1 = %s"

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        connection.autocommit = True
        transaction = self._transaction_mock()
        cursor = connection.cursor()

        with mock.patch(
            "google.cloud.spanner_v1.services.spanner.client.SpannerClient.create_session",
            return_value=Session(),
        ):
            with mock.patch(
                "google.cloud.spanner_v1.session.Session.transaction",
                return_value=transaction,
            ):
                cursor.executemany(sql, [(1,), (2,), (3,)])

        transaction.batch_update.assert_called_once_with(
            [
                ("DELETE FROM table WHERE col1 = @a0", {"a0": 1}, {"a0": INT64}),
                ("DELETE FROM table WHERE col1 = @a0", {"a0": 2}, {"a0": INT64}),
                ("DELETE FROM table WHERE col1 = @a0", {"a0": 3}, {"a0": INT64}),
            ],
            last_statement=True,
        )

    def test_executemany_update_batch_autocommit(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.param_types import INT64, STRING
        from google.cloud.spanner_v1.types.spanner import Session

        sql = "UPDATE table SET col1 = %s WHERE col2 = %s"

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        connection.autocommit = True
        transaction = self._transaction_mock()
        cursor = connection.cursor()

        with mock.patch(
            "google.cloud.spanner_v1.services.spanner.client.SpannerClient.create_session",
            return_value=Session(),
        ):
            with mock.patch(
                "google.cloud.spanner_v1.session.Session.transaction",
                return_value=transaction,
            ):
                cursor.executemany(sql, [(1, "a"), (2, "b"), (3, "c")])

        transaction.batch_update.assert_called_once_with(
            [
                (
                    "UPDATE table SET col1 = @a0 WHERE col2 = @a1",
                    {"a0": 1, "a1": "a"},
                    {"a0": INT64, "a1": STRING},
                ),
                (
                    "UPDATE table SET col1 = @a0 WHERE col2 = @a1",
                    {"a0": 2, "a1": "b"},
                    {"a0": INT64, "a1": STRING},
                ),
                (
                    "UPDATE table SET col1 = @a0 WHERE col2 = @a1",
                    {"a0": 3, "a1": "c"},
                    {"a0": INT64, "a1": STRING},
                ),
            ],
            last_statement=True,
        )

    def test_executemany_insert_batch_non_autocommit(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.param_types import INT64
        from google.cloud.spanner_v1.types.spanner import Session

        sql = """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (%s, %s, %s, %s)"""

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        transaction = self._transaction_mock()

        cursor = connection.cursor()
        with mock.patch(
            "google.cloud.spanner_v1.services.spanner.client.SpannerClient.create_session",
            return_value=Session(),
        ):
            with mock.patch(
                "google.cloud.spanner_v1.session.Session.transaction",
                return_value=transaction,
            ):
                cursor.executemany(sql, [(1, 2, 3, 4), (5, 6, 7, 8)])

        transaction.batch_update.assert_called_once_with(
            [
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 1, "a1": 2, "a2": 3, "a3": 4},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 5, "a1": 6, "a2": 7, "a3": 8},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
            ]
        )

    def test_executemany_insert_batch_autocommit(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.param_types import INT64
        from google.cloud.spanner_v1.types.spanner import Session

        sql = """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (%s, %s, %s, %s)"""

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        connection.autocommit = True

        transaction = self._transaction_mock()
        transaction.commit = mock.Mock()

        cursor = connection.cursor()
        with mock.patch(
            "google.cloud.spanner_v1.services.spanner.client.SpannerClient.create_session",
            return_value=Session(),
        ):
            with mock.patch(
                "google.cloud.spanner_v1.session.Session.transaction",
                return_value=transaction,
            ):
                cursor.executemany(sql, [(1, 2, 3, 4), (5, 6, 7, 8)])

        transaction.batch_update.assert_called_once_with(
            [
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 1, "a1": 2, "a2": 3, "a3": 4},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 5, "a1": 6, "a2": 7, "a3": 8},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
            ],
            last_statement=True,
        )
        transaction.commit.assert_called_once()

    def test_executemany_insert_batch_failed(self):
        from google.rpc.code_pb2 import UNKNOWN

        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_dbapi.exceptions import OperationalError
        from google.cloud.spanner_v1.types.spanner import Session

        sql = """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (%s, %s, %s, %s)"""
        err_details = "Details here"

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        connection.autocommit = True
        cursor = connection.cursor()

        transaction = mock.Mock()
        transaction.batch_update = mock.Mock(
            return_value=(mock.Mock(code=UNKNOWN, message=err_details), [])
        )

        with mock.patch(
            "google.cloud.spanner_v1.services.spanner.client.SpannerClient.create_session",
            return_value=Session(),
        ):
            with mock.patch(
                "google.cloud.spanner_v1.session.Session.transaction",
                return_value=transaction,
            ):
                with self.assertRaisesRegex(OperationalError, err_details):
                    cursor.executemany(sql, [(1, 2, 3, 4), (5, 6, 7, 8)])

    def test_executemany_insert_batch_aborted(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.param_types import INT64

        sql = """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (%s, %s, %s, %s)"""
        args = [(1, 2, 3, 4), (5, 6, 7, 8)]
        err_details = "Aborted details here"

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        transaction1 = mock.Mock()
        transaction1.batch_update = mock.Mock(
            side_effect=[(mock.Mock(code=ABORTED, message=err_details), [])]
        )

        transaction2 = self._transaction_mock()

        connection.transaction_checkout = mock.Mock(
            side_effect=[transaction1, transaction2]
        )

        cursor = connection.cursor()
        cursor.executemany(sql, args)

        transaction1.batch_update.assert_called_with(
            [
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 1, "a1": 2, "a2": 3, "a3": 4},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 5, "a1": 6, "a2": 7, "a3": 8},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
            ]
        )
        transaction2.batch_update.assert_called_with(
            [
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 1, "a1": 2, "a2": 3, "a3": 4},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
                (
                    """INSERT INTO table (col1, "col2", `col3`, `"col4"`) VALUES (@a0, @a1, @a2, @a3)""",
                    {"a0": 5, "a1": 6, "a2": 7, "a3": 8},
                    {"a0": INT64, "a1": INT64, "a2": INT64, "a3": INT64},
                ),
            ]
        )

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_executemany_database_error(self, mock_client):
        from google.cloud.spanner_dbapi import connect

        connection = connect("test-instance")
        cursor = connection.cursor()

        with self.assertRaises(ValueError):
            cursor.executemany("""SELECT * FROM table1 WHERE "col1" = @a1""", ())

    @unittest.skipIf(
        sys.version_info[0] < 3, "Python 2 has an outdated iterator definition"
    )
    def test_fetchone(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor._parsed_statement = mock.Mock()
        lst = [1, 2, 3]
        cursor._itr = iter(lst)
        for i in range(len(lst)):
            self.assertEqual(cursor.fetchone(), lst[i])
        self.assertIsNone(cursor.fetchone())

    @unittest.skipIf(
        sys.version_info[0] < 3, "Python 2 has an outdated iterator definition"
    )
    def test_fetchone_w_autocommit(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        connection.autocommit = True
        cursor = self._make_one(connection)
        lst = [1, 2, 3]
        cursor._itr = iter(lst)
        for i in range(len(lst)):
            self.assertEqual(cursor.fetchone(), lst[i])
        self.assertIsNone(cursor.fetchone())

    def test_fetchmany(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor._parsed_statement = mock.Mock()
        lst = [(1,), (2,), (3,)]
        cursor._itr = iter(lst)

        self.assertEqual(cursor.fetchmany(), [lst[0]])

        result = cursor.fetchmany(len(lst))
        self.assertEqual(result, lst[1:])

    def test_fetchmany_w_autocommit(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        connection.autocommit = True
        cursor = self._make_one(connection)
        lst = [(1,), (2,), (3,)]
        cursor._itr = iter(lst)

        self.assertEqual(cursor.fetchmany(), [lst[0]])

        result = cursor.fetchmany(len(lst))
        self.assertEqual(result, lst[1:])

    def test_fetchall(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor._parsed_statement = mock.Mock()
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        lst = [(1,), (2,), (3,)]
        cursor._itr = iter(lst)
        self.assertEqual(cursor.fetchall(), lst)

        transaction_helper_mock.add_fetch_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_not_called()

    def test_fetchall_w_autocommit(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        connection.autocommit = True
        cursor = self._make_one(connection)
        lst = [(1,), (2,), (3,)]
        cursor._itr = iter(lst)
        self.assertEqual(cursor.fetchall(), lst)

    def test_nextset(self):
        from google.cloud.spanner_dbapi import exceptions

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor.close()
        with self.assertRaises(exceptions.InterfaceError):
            cursor.nextset()

    def test_setinputsizes(self):
        from google.cloud.spanner_dbapi import exceptions

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor.close()
        with self.assertRaises(exceptions.InterfaceError):
            cursor.setinputsizes(sizes=None)

    def test_setoutputsize(self):
        from google.cloud.spanner_dbapi import exceptions

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        cursor.close()
        with self.assertRaises(exceptions.InterfaceError):
            cursor.setoutputsize(size=None)

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_handle_dql(self, MockedPeekIterator):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        ) = mock.MagicMock()
        cursor = self._make_one(connection)

        _result_set = mock.Mock()
        mock_snapshot.execute_sql.return_value = _result_set
        cursor._handle_DQL("sql", params=None)
        self.assertEqual(cursor._result_set, _result_set)
        self.assertEqual(cursor._itr, MockedPeekIterator())
        self.assertEqual(cursor._row_count, None)

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_handle_dql_priority(self, MockedPeekIterator):
        from google.cloud.spanner_v1 import RequestOptions

        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        ) = mock.MagicMock()
        connection.request_priority = 1

        cursor = self._make_one(connection)

        sql = "sql"
        _result_set = mock.Mock()
        mock_snapshot.execute_sql.return_value = _result_set
        cursor._handle_DQL(sql, params=None)
        self.assertEqual(cursor._result_set, _result_set)
        self.assertEqual(cursor._itr, MockedPeekIterator())
        self.assertEqual(cursor._row_count, None)
        mock_snapshot.execute_sql.assert_called_with(
            sql, None, None, request_options=RequestOptions(priority=1)
        )

    def test_execute_query_with_auto_partition_mode(self):
        from google.cloud import spanner

        connection = self._make_connection(
            self.INSTANCE,
            mock.MagicMock(),
            read_only=True,
            data_boost_enabled=True,
            auto_partition_mode=True,
        )
        batch_snapshot = connection.database.batch_snapshot.return_value = (
            mock.MagicMock()
        )
        mock_result_set = mock.MagicMock()
        batch_snapshot.run_partitioned_query.return_value = mock_result_set

        cursor = self._make_one(connection)
        cursor.execute("SELECT * FROM table WHERE col = %s", (10,))

        self.assertEqual(cursor._result_set, mock_result_set)
        self.assertEqual(cursor._itr, mock_result_set)
        batch_snapshot.run_partitioned_query.assert_called_once_with(
            "SELECT * FROM table WHERE col = @a0",
            params={"a0": 10},
            param_types={"a0": spanner.param_types.INT64},
            data_boost_enabled=True,
        )

    def test_execute_query_with_auto_partition_mode_rw_transaction_error(self):
        from google.cloud.spanner_dbapi.exceptions import ProgrammingError

        connection = self._make_connection(
            self.INSTANCE,
            mock.MagicMock(),
            read_only=False,
            auto_partition_mode=True,
        )
        connection._autocommit = False
        connection._transaction_begin_marked = True

        cursor = self._make_one(connection)
        with self.assertRaises(ProgrammingError):
            cursor.execute("SELECT * FROM table")

    def test_handle_dql_database_error(self):
        connection = self._make_connection(self.INSTANCE)
        cursor = self._make_one(connection)

        with self.assertRaises(ValueError):
            cursor._handle_DQL("sql", params=None)

    def test_context(self):
        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)
        with cursor as c:
            self.assertEqual(c, cursor)

        self.assertTrue(c.is_closed)

    def test_next(self):
        from google.cloud.spanner_dbapi import exceptions

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)
        with self.assertRaises(exceptions.ProgrammingError):
            cursor.__next__()

        lst = [(1,), (2,), (3,)]
        cursor._itr = iter(lst)
        i = 0
        for c in cursor._itr:
            self.assertEqual(c, lst[i])
            i += 1

    def test_iter(self):
        from google.cloud.spanner_dbapi import exceptions

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)
        with self.assertRaises(exceptions.ProgrammingError):
            _ = iter(cursor)

        iterator = iter([(1,), (2,), (3,)])
        cursor._itr = iterator
        self.assertEqual(iter(cursor), iterator)

    def test_list_tables(self):
        from google.cloud.spanner_dbapi import _helpers
        from google.cloud.spanner_v1 import param_types

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)

        table_list = ["table1", "table2", "table3"]
        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.run_sql_in_snapshot",
            return_value=table_list,
        ) as mock_run_sql:
            cursor.list_tables()
            mock_run_sql.assert_called_once_with(
                sql=_helpers.SQL_LIST_TABLES_AND_VIEWS,
                params={"table_schema": ""},
                param_types={"table_schema": param_types.STRING},
            )

    def test_run_sql_in_snapshot(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        ) = mock.MagicMock()
        cursor = self._make_one(connection)

        results = 1, 2, 3
        mock_snapshot.execute_sql.return_value = results
        self.assertEqual(cursor.run_sql_in_snapshot("sql"), list(results))

    def test_run_sql_in_snapshot_database_error(self):
        connection = self._make_connection(self.INSTANCE)
        cursor = self._make_one(connection)

        with self.assertRaises(ValueError):
            cursor.run_sql_in_snapshot("sql")

    def test_get_table_column_schema(self):
        from google.cloud.spanner_dbapi import _helpers
        from google.cloud.spanner_dbapi.cursor import ColumnDetails
        from google.cloud.spanner_v1 import param_types

        connection = self._make_connection(self.INSTANCE, self.DATABASE)
        cursor = self._make_one(connection)

        column_name = "column1"
        is_nullable = "YES"
        spanner_type = "spanner_type"
        rows = [(column_name, is_nullable, spanner_type)]
        expected = {column_name: ColumnDetails(null_ok=True, spanner_type=spanner_type)}
        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.run_sql_in_snapshot",
            return_value=rows,
        ) as mock_run_sql:
            table_name = "table1"
            result = cursor.get_table_column_schema(table_name=table_name)
            mock_run_sql.assert_called_once_with(
                sql=_helpers.SQL_GET_TABLE_COLUMN_SCHEMA,
                params={"schema_name": "", "table_name": table_name},
                param_types={
                    "schema_name": param_types.STRING,
                    "table_name": param_types.STRING,
                },
            )
            self.assertEqual(result, expected)

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_peek_iterator_aborted(self, mock_client):
        """
        Checking that an Aborted exception is retried in case it happened
        while streaming the first element with a PeekIterator.
        """
        from google.api_core.exceptions import Aborted

        from google.cloud.spanner_dbapi.connection import connect

        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        with mock.patch(
            "google.cloud.spanner_dbapi.utils.PeekIterator.__init__",
            side_effect=(Aborted("Aborted"), None),
        ):
            with mock.patch(
                "google.cloud.spanner_dbapi.transaction_helper.TransactionRetryHelper.retry_transaction"
            ) as retry_mock:
                with mock.patch(
                    "google.cloud.spanner_dbapi.connection.Connection.run_statement",
                    return_value=(1, 2, 3),
                ):
                    cursor.execute("SELECT * FROM table_name")

            retry_mock.assert_called_with()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetchone_aborted_with_cursor_not_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__next__",
            side_effect=(Aborted("Aborted"), iter([])),
        ):
            cursor.fetchone()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_called_once()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetchone_aborted_with_cursor_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        cursor._in_retry_mode = True
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__next__",
            side_effect=(Aborted("Aborted"), iter([])),
        ):
            cursor.fetchone()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_not_called()
        transaction_helper_mock.retry_transaction.assert_not_called()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetchall_aborted_with_cursor_not_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__iter__",
            side_effect=(Aborted("Aborted"), iter([])),
        ):
            cursor.fetchall()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_called_once()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetchall_aborted_with_cursor_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        cursor._in_retry_mode = True
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__iter__",
            side_effect=(Aborted("Aborted"), iter([])),
        ):
            cursor.fetchall()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_not_called()
        transaction_helper_mock.retry_transaction.assert_not_called()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetchmany_aborted_with_cursor_not_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__next__",
            side_effect=(Aborted("Aborted"), iter([])),
        ):
            cursor.fetchmany()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_called_once()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetchmany_aborted_with_cursor_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        cursor._in_retry_mode = True
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__next__",
            side_effect=(Aborted("Aborted"), iter([])),
        ):
            cursor.fetchmany()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_not_called()
        transaction_helper_mock.retry_transaction.assert_not_called()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetch_exception_with_cursor_not_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__iter__",
            side_effect=Exception("Exception"),
        ):
            cursor.fetchall()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_called_once()
        transaction_helper_mock.retry_transaction.assert_not_called()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_fetch_exception_with_cursor_in_retry_mode(self, mock_client):
        connection = connect("test-instance", "test-database")
        cursor = connection.cursor()
        cursor._in_retry_mode = True
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_dbapi.cursor.Cursor.__next__",
            side_effect=Exception("Exception"),
        ):
            cursor.fetchmany()

        transaction_helper_mock.add_fetch_statement_for_retry.assert_not_called()
        transaction_helper_mock.retry_transaction.assert_not_called()

    @mock.patch("google.cloud.spanner_v1.Client")
    def test_ddls_with_semicolon(self, mock_client):
        """
        Check that one script with several DDL statements separated
        with semicolons is splitted into several DDLs.
        """
        from google.cloud.spanner_dbapi.connection import connect

        EXP_DDLS = [
            "CREATE TABLE table_name (row_id INT64) PRIMARY KEY ()",
            "DROP INDEX index_name",
            (
                "CREATE TABLE papers ("
                "\n    id INT64,"
                "\n    authors ARRAY<STRING(100)>,"
                '\n    author_list STRING(MAX) AS (ARRAY_TO_STRING(authors, ";")) stored'
                ") PRIMARY KEY (id)"
            ),
            "DROP TABLE table_name",
        ]

        connection = connect("test-instance", "test-database")

        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE table_name (row_id INT64) PRIMARY KEY ();"
            "DROP INDEX index_name;\n"
            "CREATE TABLE papers ("
            "\n    id INT64,"
            "\n    authors ARRAY<STRING(100)>,"
            '\n    author_list STRING(MAX) AS (ARRAY_TO_STRING(authors, ";")) stored'
            ") PRIMARY KEY (id);"
            "DROP TABLE table_name;",
        )

        self.assertEqual(connection._ddl_statements, EXP_DDLS)

    def test_execute_ddl_statement_not_added_to_transaction_helper(self):
        connection = self._make_connection(self.INSTANCE, mock.MagicMock())
        cursor = self._make_one(connection)
        sql = "CREATE TABLE table_name (row_id INT64) PRIMARY KEY (row_id)"
        transaction_helper_mock = cursor.transaction_helper = mock.Mock()

        cursor.execute(sql=sql)

        self.assertEqual(connection._ddl_statements, [sql])
        transaction_helper_mock.add_execute_statement_for_retry.assert_not_called()

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_ddl_statement_exception_not_retried_on_aborted_dml(
        self, mock_peek_iterator
    ):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        invalid_ddl_sql = (
            "CREATE TABLE table_name (row_id INT64) PRIMARY KEY (row_id);"
            "UPDATE table_name SET row_id = 1"
        )
        update_sql = "UPDATE table_name SET row_id = 1"

        orig_batch_ddls = cursor.__class__._batch_DDLs
        with mock.patch.object(
            cursor.__class__,
            "_batch_DDLs",
            side_effect=lambda sql: orig_batch_ddls(cursor, sql),
        ) as mock_batch_ddls:
            with self.assertRaises(ValueError):
                cursor.execute(sql=invalid_ddl_sql)

            self.assertEqual(connection._ddl_statements, [])
            self.assertEqual(
                cursor.transaction_helper._statement_result_details_list, []
            )
            self.assertEqual(mock_batch_ddls.call_count, 1)

            metadata_mock = mock.Mock()
            metadata_mock.trailing_metadata.return_value = {}
            connection.run_statement = mock.Mock(
                side_effect=[
                    Aborted("Aborted", errors=[metadata_mock]),
                    mock.MagicMock(),
                ]
            )

            cursor.execute(sql=update_sql)
            self.assertEqual(connection.run_statement.call_count, 2)
            self.assertEqual(mock_batch_ddls.call_count, 1)
            mock_database.update_ddl.assert_not_called()

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_ddl_then_aborted_dml_does_not_requeue_ddl(
        self, mock_peek_iterator
    ):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE table_name (row_id INT64) PRIMARY KEY (row_id)"
        insert_sql = "INSERT INTO table_name (row_id) VALUES (1)"
        select_sql = "SELECT row_id FROM table_name"

        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        metadata_mock = mock.Mock()
        metadata_mock.trailing_metadata.return_value = {}
        connection.run_statement = mock.Mock(
            side_effect=[
                Aborted("Aborted", errors=[metadata_mock]),
                mock.MagicMock(),
                mock.MagicMock(),
            ]
        )

        cursor.execute(sql=insert_sql)
        self.assertEqual(connection._ddl_statements, [])
        mock_database.update_ddl.assert_called_once_with([ddl_sql])

        cursor.execute(sql=select_sql)
        mock_database.update_ddl.assert_called_once_with([ddl_sql])

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_ddl_then_dml_retry_replays_prior_dml_without_replaying_ddl(
        self, mock_peek_iterator
    ):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE table_name (row_id INT64) PRIMARY KEY (row_id)"
        insert_1_sql = "INSERT INTO table_name (row_id) VALUES (1)"
        insert_2_sql = "INSERT INTO table_name (row_id) VALUES (2)"

        # 1. Execute DDL
        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        metadata_mock = mock.Mock()
        metadata_mock.trailing_metadata.return_value = {}

        # 2. insert_1 succeeds; insert_2 aborts on attempt 1, triggering retry of insert_1 and retry of insert_2
        connection.run_statement = mock.Mock(
            side_effect=[
                mock.MagicMock(),  # insert_1 (attempt 1 -> succeeds)
                Aborted(
                    "Aborted", errors=[metadata_mock]
                ),  # insert_2 (attempt 1 -> aborts)
                mock.MagicMock(),  # insert_1 (replayed by retry_transaction)
                mock.MagicMock(),  # insert_2 (attempt 2 -> succeeds)
            ]
        )

        cursor.execute(sql=insert_1_sql)
        mock_database.update_ddl.assert_called_once_with([ddl_sql])
        self.assertEqual(connection._ddl_statements, [])
        self.assertEqual(
            len(cursor.transaction_helper._statement_result_details_list), 1
        )

        # 3. insert_2 aborts and triggers retry_transaction()
        cursor.execute(sql=insert_2_sql)

        # Assert insert_1 was replayed, insert_2 was retried, and update_ddl was NOT called a second time
        self.assertEqual(connection.run_statement.call_count, 4)
        mock_database.update_ddl.assert_called_once_with([ddl_sql])
        self.assertEqual(connection._ddl_statements, [])

    def test_execute_ddl_then_close_clears_ddl(self):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE canceled_table (id INT64) PRIMARY KEY (id)"

        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        connection.close()
        self.assertEqual(connection._ddl_statements, [])
        mock_database.update_ddl.assert_not_called()

    def test_execute_ddl_then_rollback_and_close_clears_ddl(self):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE canceled_table (id INT64) PRIMARY KEY (id)"

        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        connection.rollback()
        self.assertEqual(connection._ddl_statements, [])

        connection.close()
        mock_database.update_ddl.assert_not_called()

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_ddl_then_rollback_and_autocommit_query_does_not_execute_ddl(
        self, mock_peek_iterator
    ):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE canceled_table (id INT64) PRIMARY KEY (id)"

        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        connection.rollback()
        self.assertEqual(connection._ddl_statements, [])

        connection.autocommit = True
        cursor.execute(sql="SELECT 1")

        mock_database.update_ddl.assert_not_called()

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_ddl_then_autocommit_without_rollback_executes_ddl(
        self, mock_peek_iterator
    ):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE valid_table (id INT64) PRIMARY KEY (id)"

        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        connection.autocommit = True
        self.assertEqual(connection._ddl_statements, [])
        mock_database.update_ddl.assert_called_once_with([ddl_sql])

        cursor.execute(sql="SELECT 1")
        mock_database.update_ddl.assert_called_once_with([ddl_sql])

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_ddl_then_rollback_and_dml_does_not_execute_ddl(
        self, mock_peek_iterator
    ):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE canceled_table (id INT64) PRIMARY KEY (id)"
        insert_sql = "INSERT INTO users (id) VALUES (1)"

        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        connection.rollback()

        connection.run_statement = mock.Mock(return_value=mock.MagicMock())
        cursor.execute(sql=insert_sql)
        connection.commit()

        mock_database.update_ddl.assert_not_called()

    @mock.patch("google.cloud.spanner_dbapi.cursor.batch_dml_executor.run_batch_dml")
    def test_execute_ddl_then_rollback_and_executemany_does_not_execute_ddl(
        self, mock_run_batch_dml
    ):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        ddl_sql = "CREATE TABLE canceled_table (id INT64) PRIMARY KEY (id)"
        insert_sql = "INSERT INTO users (id) VALUES (%s)"

        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        connection.rollback()

        cursor.executemany(insert_sql, [(1,), (2,)])
        connection.commit()

        mock_database.update_ddl.assert_not_called()

    def test_execute_ddl_then_rollback_and_ddl_does_not_execute_canceled_ddl(self):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        canceled_ddl = "CREATE TABLE canceled_table (id INT64) PRIMARY KEY (id)"
        valid_ddl = "CREATE TABLE valid_table (id INT64) PRIMARY KEY (id)"

        cursor.execute(sql=canceled_ddl)
        self.assertEqual(connection._ddl_statements, [canceled_ddl])

        connection.rollback()

        cursor.execute(sql=valid_ddl)
        connection.commit()

        mock_database.update_ddl.assert_called_once_with([valid_ddl])
        self.assertEqual(connection._ddl_statements, [])

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_execute_dml_then_ddl_then_rollback_discards_ddl(self, mock_peek_iterator):
        mock_database = mock.MagicMock()
        connection = self._make_connection(self.INSTANCE, mock_database)
        cursor = self._make_one(connection)
        connection.run_statement = mock.Mock(return_value=mock.MagicMock())
        dml_sql = "INSERT INTO users (id) VALUES (1)"
        ddl_sql = "CREATE TABLE canceled_table (id INT64) PRIMARY KEY (id)"

        cursor.execute(sql=dml_sql)
        cursor.execute(sql=ddl_sql)
        self.assertEqual(connection._ddl_statements, [ddl_sql])

        connection.rollback()
        self.assertEqual(connection._ddl_statements, [])

        cursor.execute(sql="SELECT 1")
        connection.commit()
        mock_database.update_ddl.assert_not_called()
