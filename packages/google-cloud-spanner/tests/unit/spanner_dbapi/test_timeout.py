# Copyright 2026 Google LLC All rights reserved.
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

"""Unit tests for timeout handling in Spanner DB-API."""

import unittest
from unittest import mock

from google.auth.credentials import AnonymousCredentials
from google.rpc.code_pb2 import OK

from google.cloud.spanner_dbapi import Connection, connect
from google.cloud.spanner_dbapi.parsed_statement import (
    ParsedStatement,
    Statement,
    StatementType,
)


class TestDBAPITimeout(unittest.TestCase):
    INSTANCE = "test-instance"
    DATABASE = "test-database"

    def _make_connection(self, timeout=None, **kwargs):
        from google.cloud.spanner_v1.client import Client
        from google.cloud.spanner_v1.instance import Instance

        client = Client(
            project="test",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )
        instance = Instance(self.INSTANCE, client=client)
        database = instance.database(self.DATABASE)
        return Connection(instance, database, timeout=timeout, **kwargs)

    def test_connection_timeout_default_is_none(self):
        connection = self._make_connection()
        self.assertIsNone(connection.timeout)

    def test_connection_timeout_init(self):
        connection = self._make_connection(timeout=30.0)
        self.assertEqual(connection.timeout, 30.0)

    def test_connect_accepts_timeout(self):
        connection = connect(
            self.INSTANCE,
            self.DATABASE,
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
            timeout=45.0,
        )
        self.assertEqual(connection.timeout, 45.0)

    def test_run_statement_passes_timeout(self):
        connection = self._make_connection(timeout=25.0)
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        connection._transaction = mock_transaction

        sql = "SELECT 1"
        stmt = Statement(sql, [], {})
        connection.run_statement(stmt)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 25.0)

    def test_run_statement_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        connection._transaction = mock_transaction

        sql = "SELECT 1"
        stmt = Statement(sql, [], {})
        connection.run_statement(stmt)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertNotIn("timeout", kwargs)

    def test_run_statement_explicit_timeout_override(self):
        connection = self._make_connection(timeout=25.0)
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        connection._transaction = mock_transaction

        sql = "SELECT 1"
        stmt = Statement(sql, [], {})
        connection.run_statement(stmt, timeout=5.0)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 5.0)

    def test_cursor_dql_snapshot_passes_timeout(self):
        connection = self._make_connection(timeout=12.0)
        connection.autocommit = True
        cursor = connection.cursor()

        mock_snapshot = mock.MagicMock()
        mock_result_set = mock.MagicMock()
        mock_result_set.metadata.transaction.read_timestamp = None
        mock_snapshot.execute_sql.return_value = mock_result_set

        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement("SELECT 1")),
        ):
            cursor.execute("SELECT 1")

        mock_snapshot.execute_sql.assert_called_once()
        _, kwargs = mock_snapshot.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 12.0)

    def test_cursor_autocommit_dml_passes_timeout(self):
        connection = self._make_connection(timeout=18.0)
        connection.autocommit = True
        cursor = connection.cursor()

        mock_transaction = mock.MagicMock()
        mock_result_set = mock.MagicMock()
        mock_transaction.execute_sql.return_value = mock_result_set

        def fake_run_in_transaction(func, *args, **kwargs):
            return func(mock_transaction, *args, **kwargs)

        connection.database.run_in_transaction = fake_run_in_transaction

        sql = "UPDATE t SET col = 1"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.execute(sql)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 18.0)
        self.assertTrue(kwargs.get("last_statement"))

    def test_batch_dml_transaction_passes_timeout(self):
        connection = self._make_connection(timeout=7.0)
        connection.autocommit = True
        cursor = connection.cursor()

        mock_transaction = mock.MagicMock()
        mock_transaction.batch_update.return_value = [mock.MagicMock(code=OK), [1, 1]]

        def fake_run_in_transaction(func, *args, **kwargs):
            return func(mock_transaction, *args, **kwargs)

        connection.database.run_in_transaction = fake_run_in_transaction

        sql = "UPDATE t SET col = %s"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.executemany(sql, [(1,), (2,)])

        mock_transaction.batch_update.assert_called_once()
        _, kwargs = mock_transaction.batch_update.call_args
        self.assertEqual(kwargs.get("timeout"), 7.0)
        self.assertTrue(kwargs.get("last_statement"))

    def test_cursor_timeout_property(self):
        connection = self._make_connection(timeout=30.0)
        cursor = connection.cursor()
        self.assertEqual(cursor.timeout, 30.0)

        cursor.timeout = 10.0
        self.assertEqual(cursor.timeout, 10.0)
        self.assertEqual(connection.timeout, 30.0)

        cursor.timeout = None
        self.assertEqual(cursor.timeout, 30.0)

    def test_validate_passes_timeout(self):
        connection = self._make_connection(timeout=15.0)
        mock_snapshot = mock.MagicMock()
        mock_snapshot.execute_sql.return_value = [[1]]
        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        connection.validate()

        mock_snapshot.execute_sql.assert_called_once_with("SELECT 1", timeout=15.0)

    def test_validate_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        mock_snapshot = mock.MagicMock()
        mock_snapshot.execute_sql.return_value = [[1]]
        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        connection.validate()

        mock_snapshot.execute_sql.assert_called_once_with("SELECT 1")

    def test_cursor_dql_snapshot_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        connection.autocommit = True
        cursor = connection.cursor()

        mock_snapshot = mock.MagicMock()
        mock_result_set = mock.MagicMock()
        mock_result_set.metadata.transaction.read_timestamp = None
        mock_snapshot.execute_sql.return_value = mock_result_set

        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement("SELECT 1")),
        ):
            cursor.execute("SELECT 1")

        mock_snapshot.execute_sql.assert_called_once()
        _, kwargs = mock_snapshot.execute_sql.call_args
        self.assertNotIn("timeout", kwargs)

    def test_cursor_dql_snapshot_uses_cursor_timeout(self):
        connection = self._make_connection(timeout=12.0)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.timeout = 4.0

        mock_snapshot = mock.MagicMock()
        mock_result_set = mock.MagicMock()
        mock_result_set.metadata.transaction.read_timestamp = None
        mock_snapshot.execute_sql.return_value = mock_result_set

        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.QUERY, Statement("SELECT 1")),
        ):
            cursor.execute("SELECT 1")

        mock_snapshot.execute_sql.assert_called_once()
        _, kwargs = mock_snapshot.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 4.0)

    def test_cursor_autocommit_dml_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        connection.autocommit = True
        cursor = connection.cursor()

        mock_transaction = mock.MagicMock()
        mock_result_set = mock.MagicMock()
        mock_transaction.execute_sql.return_value = mock_result_set

        def fake_run_in_transaction(func, *args, **kwargs):
            return func(mock_transaction, *args, **kwargs)

        connection.database.run_in_transaction = fake_run_in_transaction

        sql = "UPDATE t SET col = 1"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.execute(sql)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertNotIn("timeout", kwargs)
        self.assertTrue(kwargs.get("last_statement"))

    def test_cursor_autocommit_dml_uses_cursor_timeout(self):
        connection = self._make_connection(timeout=18.0)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.timeout = 6.0

        mock_transaction = mock.MagicMock()
        mock_result_set = mock.MagicMock()
        mock_transaction.execute_sql.return_value = mock_result_set

        def fake_run_in_transaction(func, *args, **kwargs):
            return func(mock_transaction, *args, **kwargs)

        connection.database.run_in_transaction = fake_run_in_transaction

        sql = "UPDATE t SET col = 1"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.execute(sql)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 6.0)
        self.assertTrue(kwargs.get("last_statement"))

    def test_cursor_rw_transaction_execute_passes_timeout(self):
        connection = self._make_connection(timeout=14.0)
        connection.autocommit = False
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        mock_transaction.execute_sql.return_value = iter([])
        connection._transaction = mock_transaction

        cursor = connection.cursor()
        sql = "UPDATE t SET col = 1"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.execute(sql)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 14.0)

    def test_cursor_rw_transaction_execute_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        connection.autocommit = False
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        mock_transaction.execute_sql.return_value = iter([])
        connection._transaction = mock_transaction

        cursor = connection.cursor()
        sql = "UPDATE t SET col = 1"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.execute(sql)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertNotIn("timeout", kwargs)

    def test_cursor_rw_transaction_execute_uses_cursor_timeout(self):
        connection = self._make_connection(timeout=14.0)
        connection.autocommit = False
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        mock_transaction.execute_sql.return_value = iter([])
        connection._transaction = mock_transaction

        cursor = connection.cursor()
        cursor.timeout = 3.0
        sql = "UPDATE t SET col = 1"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.execute(sql)

        mock_transaction.execute_sql.assert_called_once()
        _, kwargs = mock_transaction.execute_sql.call_args
        self.assertEqual(kwargs.get("timeout"), 3.0)

    def test_run_sql_in_snapshot_passes_timeout(self):
        connection = self._make_connection(timeout=20.0)
        cursor = connection.cursor()

        mock_snapshot = mock.MagicMock()
        mock_snapshot.execute_sql.return_value = [["row1"]]
        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        res = cursor.run_sql_in_snapshot("SELECT 1")
        self.assertEqual(res, [["row1"]])
        mock_snapshot.execute_sql.assert_called_once_with(
            "SELECT 1", None, None, timeout=20.0
        )

    def test_run_sql_in_snapshot_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        cursor = connection.cursor()

        mock_snapshot = mock.MagicMock()
        mock_snapshot.execute_sql.return_value = [["row1"]]
        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        res = cursor.run_sql_in_snapshot("SELECT 1")
        self.assertEqual(res, [["row1"]])
        mock_snapshot.execute_sql.assert_called_once_with("SELECT 1", None, None)

    def test_run_sql_in_snapshot_uses_cursor_timeout(self):
        connection = self._make_connection(timeout=20.0)
        cursor = connection.cursor()
        cursor.timeout = 8.0

        mock_snapshot = mock.MagicMock()
        mock_snapshot.execute_sql.return_value = [["row1"]]
        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_snapshot
        connection.database.snapshot = mock.MagicMock(return_value=mock_ctx)

        res = cursor.run_sql_in_snapshot("SELECT 1")
        self.assertEqual(res, [["row1"]])
        mock_snapshot.execute_sql.assert_called_once_with(
            "SELECT 1", None, None, timeout=8.0
        )

    def test_batch_dml_autocommit_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        connection.autocommit = True
        cursor = connection.cursor()

        mock_transaction = mock.MagicMock()
        mock_transaction.batch_update.return_value = [mock.MagicMock(code=OK), [1, 1]]

        def fake_run_in_transaction(func, *args, **kwargs):
            return func(mock_transaction, *args, **kwargs)

        connection.database.run_in_transaction = fake_run_in_transaction

        sql = "UPDATE t SET col = %s"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.executemany(sql, [(1,), (2,)])

        mock_transaction.batch_update.assert_called_once()
        _, kwargs = mock_transaction.batch_update.call_args
        self.assertNotIn("timeout", kwargs)
        self.assertTrue(kwargs.get("last_statement"))

    def test_batch_dml_autocommit_uses_cursor_timeout(self):
        connection = self._make_connection(timeout=7.0)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.timeout = 2.0

        mock_transaction = mock.MagicMock()
        mock_transaction.batch_update.return_value = [mock.MagicMock(code=OK), [1, 1]]

        def fake_run_in_transaction(func, *args, **kwargs):
            return func(mock_transaction, *args, **kwargs)

        connection.database.run_in_transaction = fake_run_in_transaction

        sql = "UPDATE t SET col = %s"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.executemany(sql, [(1,), (2,)])

        mock_transaction.batch_update.assert_called_once()
        _, kwargs = mock_transaction.batch_update.call_args
        self.assertEqual(kwargs.get("timeout"), 2.0)
        self.assertTrue(kwargs.get("last_statement"))

    def test_batch_dml_in_rw_transaction_passes_timeout(self):
        connection = self._make_connection(timeout=11.0)
        connection.autocommit = False
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        mock_transaction.batch_update.return_value = [mock.MagicMock(code=OK), [1, 1]]
        connection._transaction = mock_transaction

        cursor = connection.cursor()
        sql = "UPDATE t SET col = %s"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.executemany(sql, [(1,), (2,)])

        mock_transaction.batch_update.assert_called_once()
        _, kwargs = mock_transaction.batch_update.call_args
        self.assertEqual(kwargs.get("timeout"), 11.0)

    def test_batch_dml_in_rw_transaction_without_timeout_omits_kwarg(self):
        connection = self._make_connection()
        connection.autocommit = False
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        mock_transaction.batch_update.return_value = [mock.MagicMock(code=OK), [1, 1]]
        connection._transaction = mock_transaction

        cursor = connection.cursor()
        sql = "UPDATE t SET col = %s"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.executemany(sql, [(1,), (2,)])

        mock_transaction.batch_update.assert_called_once()
        _, kwargs = mock_transaction.batch_update.call_args
        self.assertNotIn("timeout", kwargs)

    def test_batch_dml_in_rw_transaction_uses_cursor_timeout(self):
        connection = self._make_connection(timeout=11.0)
        connection.autocommit = False
        connection._spanner_transaction_started = True
        mock_transaction = mock.MagicMock()
        mock_transaction.batch_update.return_value = [mock.MagicMock(code=OK), [1, 1]]
        connection._transaction = mock_transaction

        cursor = connection.cursor()
        cursor.timeout = 3.5
        sql = "UPDATE t SET col = %s"
        with mock.patch(
            "google.cloud.spanner_dbapi.parse_utils.classify_statement",
            return_value=ParsedStatement(StatementType.UPDATE, Statement(sql)),
        ):
            cursor.executemany(sql, [(1,), (2,)])

        mock_transaction.batch_update.assert_called_once()
        _, kwargs = mock_transaction.batch_update.call_args
        self.assertEqual(kwargs.get("timeout"), 3.5)
