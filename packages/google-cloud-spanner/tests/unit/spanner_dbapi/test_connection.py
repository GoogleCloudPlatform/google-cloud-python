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

"""Cloud Spanner DB-API Connection class unit tests."""

import datetime
import unittest
import warnings

import mock
import pytest
from google.auth.credentials import AnonymousCredentials

from google.cloud.spanner_admin_database_v1 import DatabaseDialect
from google.cloud.spanner_dbapi import Connection
from google.cloud.spanner_dbapi.batch_dml_executor import BatchMode
from google.cloud.spanner_dbapi.connection import CLIENT_TRANSACTION_NOT_STARTED_WARNING
from google.cloud.spanner_dbapi.exceptions import (
    InterfaceError,
    OperationalError,
    ProgrammingError,
)
from google.cloud.spanner_dbapi.parsed_statement import (
    AutocommitDmlMode,
    ClientSideStatementType,
    ParsedStatement,
    Statement,
    StatementType,
)
from google.cloud.spanner_v1.database_sessions_manager import TransactionType
from tests._builders import build_connection, build_session

PROJECT = "test-project"
INSTANCE = "test-instance"
DATABASE = "test-database"
USER_AGENT = "user-agent"


class TestConnection(unittest.TestCase):
    def setUp(self):
        self._under_test = self._make_connection()

    def _get_client_info(self):
        from google.api_core.gapic_v1.client_info import ClientInfo

        return ClientInfo(user_agent=USER_AGENT)

    def _make_connection(
        self, database_dialect=DatabaseDialect.DATABASE_DIALECT_UNSPECIFIED, **kwargs
    ):
        from google.cloud.spanner_v1.client import Client
        from google.cloud.spanner_v1.instance import Instance

        # We don't need a real Client object to test the constructor
        client = Client(
            project="test",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )
        instance = Instance(INSTANCE, client=client)
        database = instance.database(DATABASE, database_dialect=database_dialect)
        return Connection(instance, database, **kwargs)

    @mock.patch("google.cloud.spanner_dbapi.connection.Connection.commit")
    def test_autocommit_setter_transaction_not_started(self, mock_commit):
        connection = self._make_connection()

        connection.autocommit = True

        mock_commit.assert_not_called()
        self.assertTrue(connection._autocommit)

        connection.autocommit = False
        mock_commit.assert_not_called()
        self.assertFalse(connection._autocommit)

    @mock.patch("google.cloud.spanner_dbapi.connection.Connection.commit")
    def test_autocommit_setter_transaction_started(self, mock_commit):
        connection = self._make_connection()
        connection._spanner_transaction_started = True

        connection.autocommit = True

        mock_commit.assert_called_once()
        self.assertTrue(connection._autocommit)

    @mock.patch("google.cloud.spanner_dbapi.connection.Connection.commit")
    def test_autocommit_setter_with_pending_ddl_statements(self, mock_commit):
        connection = self._make_connection()
        connection._ddl_statements = ["CREATE TABLE t (id INT64) PRIMARY KEY (id)"]

        connection.autocommit = True

        mock_commit.assert_called_once()
        self.assertTrue(connection._autocommit)

    def test_property_database(self):
        from google.cloud.spanner_v1.database import Database

        connection = self._make_connection()
        self.assertIsInstance(connection.database, Database)
        self.assertEqual(connection.database, connection._database)

    def test_property_instance(self):
        from google.cloud.spanner_v1.instance import Instance

        connection = self._make_connection()
        self.assertIsInstance(connection.instance, Instance)
        self.assertEqual(connection.instance, connection._instance)

    def test_property_current_schema_google_sql_dialect(self):
        from google.cloud.spanner_v1.database import Database

        connection = self._make_connection(
            database_dialect=DatabaseDialect.GOOGLE_STANDARD_SQL
        )
        self.assertIsInstance(connection.database, Database)
        self.assertEqual(connection.current_schema, "")

    def test_property_current_schema_postgres_sql_dialect(self):
        from google.cloud.spanner_v1.database import Database

        connection = self._make_connection(database_dialect=DatabaseDialect.POSTGRESQL)
        self.assertIsInstance(connection.database, Database)
        self.assertEqual(connection.current_schema, "public")

    def test_read_only_connection(self):
        connection = self._make_connection(read_only=True)
        self.assertTrue(connection.read_only)

        connection._spanner_transaction_started = True
        with self.assertRaisesRegex(
            ValueError,
            "Connection read/write mode can't be changed while a transaction is in progress. "
            "Commit or rollback the current transaction and try again.",
        ):
            connection.read_only = False

        # Verify that we can set the value to the same value as it already has.
        connection.read_only = True
        self.assertTrue(connection.read_only)

        connection._spanner_transaction_started = False
        connection.read_only = False
        self.assertFalse(connection.read_only)

    def test_property_data_boost_enabled(self):
        connection = self._make_connection()
        self.assertFalse(connection.data_boost_enabled)

        connection.data_boost_enabled = True
        self.assertTrue(connection.data_boost_enabled)

        connection.data_boost_enabled = False
        self.assertFalse(connection.data_boost_enabled)

    def test_property_auto_partition_mode(self):
        connection = self._make_connection()
        self.assertFalse(connection.auto_partition_mode)

        connection.auto_partition_mode = True
        self.assertTrue(connection.auto_partition_mode)

        connection.auto_partition_mode = False
        self.assertFalse(connection.auto_partition_mode)

    def test__session_checkout_read_only(self):
        connection = build_connection(read_only=True)
        database = connection._database
        sessions_manager = database._sessions_manager

        expected_session = build_session(database=database)
        sessions_manager.get_session = mock.MagicMock(return_value=expected_session)

        actual_session = connection._session_checkout()

        self.assertEqual(actual_session, expected_session)
        sessions_manager.get_session.assert_called_once_with(TransactionType.READ_ONLY)

    def test__session_checkout_read_write(self):
        connection = build_connection(read_only=False)
        database = connection._database
        sessions_manager = database._sessions_manager

        expected_session = build_session(database=database)
        sessions_manager.get_session = mock.MagicMock(return_value=expected_session)

        actual_session = connection._session_checkout()

        self.assertEqual(actual_session, expected_session)
        sessions_manager.get_session.assert_called_once_with(TransactionType.READ_WRITE)

    def test_session_checkout_database_error(self):
        connection = Connection(INSTANCE)

        with pytest.raises(ValueError):
            connection._session_checkout()

    def test__release_session(self):
        connection = build_connection()
        sessions_manager = connection._database._sessions_manager

        session = connection._session = build_session(database=connection._database)
        put_session = sessions_manager.put_session = mock.MagicMock()

        connection._release_session()

        put_session.assert_called_once_with(session)

    def test_release_session_database_error(self):
        connection = Connection(INSTANCE)
        connection._session = "session"
        with pytest.raises(ValueError):
            connection._release_session()

    def test_transaction_checkout(self):
        connection = Connection(INSTANCE, DATABASE)
        mock_checkout = mock.MagicMock(autospec=True)
        connection._session_checkout = mock_checkout

        connection.transaction_checkout()

        mock_checkout.assert_called_once_with()

        mock_transaction = mock.MagicMock()
        connection._transaction = mock_transaction
        connection._spanner_transaction_started = True

        self.assertEqual(connection.transaction_checkout(), mock_transaction)

        connection._autocommit = True
        self.assertIsNone(connection.transaction_checkout())

    def test_transaction_checkout_does_not_call_begin(self):
        """transaction_checkout must not call Transaction.begin().

        The transaction should be returned with _transaction_id=None so that
        execute_sql/execute_update can use inline begin via
        TransactionSelector(begin=...), eliminating a separate
        BeginTransaction RPC.
        """
        connection = Connection(INSTANCE, DATABASE)
        mock_session = mock.MagicMock()
        mock_transaction = mock.MagicMock()
        mock_session.transaction.return_value = mock_transaction
        connection._session_checkout = mock.MagicMock(return_value=mock_session)

        txn = connection.transaction_checkout()

        self.assertEqual(txn, mock_transaction)
        self.assertTrue(connection._spanner_transaction_started)
        mock_transaction.begin.assert_not_called()

    def test_snapshot_checkout(self):
        connection = build_connection(read_only=True)
        connection.autocommit = False

        session_checkout = mock.Mock(wraps=connection._session_checkout)
        release_session = mock.Mock(wraps=connection._release_session)
        connection._session_checkout = session_checkout
        connection._release_session = release_session

        snapshot = connection.snapshot_checkout()
        session_checkout.assert_called_once()

        self.assertEqual(snapshot, connection.snapshot_checkout())

        connection.commit()
        self.assertIsNotNone(connection._snapshot)
        release_session.assert_called_once()

        connection.snapshot_checkout()
        self.assertIsNotNone(connection._snapshot)

        connection.rollback()
        self.assertIsNotNone(connection._snapshot)
        self.assertEqual(release_session.call_count, 2)

        connection.autocommit = True
        self.assertIsNone(connection.snapshot_checkout())

    def test_close(self):
        from google.cloud.spanner_dbapi import InterfaceError, connect

        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )

        self.assertFalse(connection.is_closed)

        connection.close()

        self.assertTrue(connection.is_closed)

        with self.assertRaises(InterfaceError):
            connection.cursor()

        mock_transaction = mock.MagicMock()
        connection._transaction = mock_transaction
        connection._spanner_transaction_started = True

        mock_rollback = mock.MagicMock()
        mock_transaction.rollback = mock_rollback

        connection.close()

        mock_rollback.assert_called_once_with()

        connection._transaction = mock.MagicMock()
        connection._own_pool = False
        connection.close()

        self.assertTrue(connection.is_closed)

    @mock.patch.object(warnings, "warn")
    def test_commit_with_spanner_transaction_not_started(self, mock_warn):
        self._under_test._spanner_transaction_started = False

        with mock.patch(
            "google.cloud.spanner_dbapi.connection.Connection._release_session"
        ) as mock_release:
            self._under_test.commit()

        mock_release.assert_called()

    def test_commit(self):
        self._under_test._transaction = mock_transaction = mock.MagicMock()
        self._under_test._spanner_transaction_started = True
        mock_transaction.commit = mock_commit = mock.MagicMock()
        transaction_helper = self._under_test._transaction_helper
        transaction_helper._statement_result_details_list = [{}, {}]

        with mock.patch(
            "google.cloud.spanner_dbapi.connection.Connection._release_session"
        ) as mock_release:
            self._under_test.commit()

        mock_commit.assert_called_once_with()
        mock_release.assert_called_once_with()
        self.assertEqual(len(transaction_helper._statement_result_details_list), 0)

    def test_commit_with_failing_ddl_resets_connection(self):
        connection = self._under_test
        connection._spanner_transaction_started = True
        connection._ddl_statements = ["CREATE TABLE t (id INT64) PRIMARY KEY (id)"]
        connection.database.update_ddl = mock.MagicMock(
            side_effect=Exception("DDL execution failed")
        )

        with mock.patch.object(
            connection, "_reset_post_commit_or_rollback"
        ) as mock_reset:
            with pytest.raises(Exception, match="DDL execution failed"):
                connection.commit()

        mock_reset.assert_called_once()

    @mock.patch.object(warnings, "warn")
    def test_commit_in_autocommit_mode(self, mock_warn):
        self._under_test._autocommit = True

        self._under_test.commit()

        mock_warn.assert_called_once_with(
            CLIENT_TRANSACTION_NOT_STARTED_WARNING, UserWarning, stacklevel=2
        )

    @mock.patch.object(warnings, "warn")
    def test_commit_in_autocommit_mode_with_ignore_warnings(self, mock_warn):
        conn = self._make_connection(
            DatabaseDialect.DATABASE_DIALECT_UNSPECIFIED,
            ignore_transaction_warnings=True,
        )
        assert conn._ignore_transaction_warnings
        conn._autocommit = True

        conn.commit()

        assert not mock_warn.warn.called

    def test_commit_database_error(self):
        from google.cloud.spanner_dbapi import Connection

        connection = Connection(INSTANCE)

        with pytest.raises(ValueError):
            connection.commit()

    @mock.patch.object(warnings, "warn")
    def test_rollback_spanner_transaction_not_started(self, mock_warn):
        self._under_test._spanner_transaction_started = False

        with mock.patch(
            "google.cloud.spanner_dbapi.connection.Connection._release_session"
        ) as mock_release:
            self._under_test.rollback()

        mock_release.assert_called()

    @mock.patch.object(warnings, "warn")
    def test_rollback(self, mock_warn):
        mock_transaction = mock.MagicMock()
        self._under_test._spanner_transaction_started = True
        self._under_test._transaction = mock_transaction
        mock_rollback = mock.MagicMock()
        mock_transaction.rollback = mock_rollback
        transaction_helper = self._under_test._transaction_helper
        transaction_helper._statement_result_details_list = [{}, {}]
        self._under_test._ddl_statements = [
            "CREATE TABLE t (id INT64) PRIMARY KEY (id)"
        ]
        with mock.patch(
            "google.cloud.spanner_dbapi.connection.Connection._release_session"
        ) as mock_release:
            self._under_test.rollback()

        self.assertEqual(len(transaction_helper._statement_result_details_list), 0)
        self.assertEqual(self._under_test._ddl_statements, [])
        mock_rollback.assert_called_once_with()
        mock_release.assert_called_once_with()

    @mock.patch.object(warnings, "warn")
    def test_rollback_in_autocommit_mode(self, mock_warn):
        self._under_test._autocommit = True

        self._under_test.rollback()

        mock_warn.assert_called_once_with(
            CLIENT_TRANSACTION_NOT_STARTED_WARNING, UserWarning, stacklevel=2
        )

    def test_start_batch_dml_batch_mode_active(self):
        self._under_test._batch_mode = BatchMode.DML
        cursor = self._under_test.cursor()

        with self.assertRaises(ProgrammingError):
            self._under_test.start_batch_dml(cursor)

    def test_start_batch_dml_connection_read_only(self):
        self._under_test.read_only = True
        cursor = self._under_test.cursor()

        with self.assertRaises(ProgrammingError):
            self._under_test.start_batch_dml(cursor)

    def test_start_batch_dml(self):
        cursor = self._under_test.cursor()

        self._under_test.start_batch_dml(cursor)

        self.assertEqual(self._under_test._batch_mode, BatchMode.DML)

    def test_execute_batch_dml_batch_mode_inactive(self):
        self._under_test._batch_mode = BatchMode.NONE

        with self.assertRaises(ProgrammingError):
            self._under_test.execute_batch_dml_statement(
                ParsedStatement(StatementType.UPDATE, Statement("sql"))
            )

    @mock.patch(
        "google.cloud.spanner_dbapi.batch_dml_executor.BatchDmlExecutor", autospec=True
    )
    def test_execute_batch_dml(self, mock_batch_dml_executor):
        self._under_test._batch_mode = BatchMode.DML
        self._under_test._batch_dml_executor = mock_batch_dml_executor

        parsed_statement = ParsedStatement(StatementType.UPDATE, Statement("sql"))
        self._under_test.execute_batch_dml_statement(parsed_statement)

        mock_batch_dml_executor.execute_statement.assert_called_once_with(
            parsed_statement
        )

    @mock.patch(
        "google.cloud.spanner_dbapi.batch_dml_executor.BatchDmlExecutor", autospec=True
    )
    def test_run_batch_batch_mode_inactive(self, mock_batch_dml_executor):
        self._under_test._batch_mode = BatchMode.NONE
        self._under_test._batch_dml_executor = mock_batch_dml_executor

        with self.assertRaises(ProgrammingError):
            self._under_test.run_batch()

    @mock.patch(
        "google.cloud.spanner_dbapi.batch_dml_executor.BatchDmlExecutor", autospec=True
    )
    def test_run_batch(self, mock_batch_dml_executor):
        self._under_test._batch_mode = BatchMode.DML
        self._under_test._batch_dml_executor = mock_batch_dml_executor

        self._under_test.run_batch()

        mock_batch_dml_executor.run_batch_dml.assert_called_once_with()
        self.assertEqual(self._under_test._batch_mode, BatchMode.NONE)
        self.assertEqual(self._under_test._batch_dml_executor, None)

    @mock.patch(
        "google.cloud.spanner_dbapi.batch_dml_executor.BatchDmlExecutor", autospec=True
    )
    def test_abort_batch_batch_mode_inactive(self, mock_batch_dml_executor):
        self._under_test._batch_mode = BatchMode.NONE
        self._under_test._batch_dml_executor = mock_batch_dml_executor

        with self.assertRaises(ProgrammingError):
            self._under_test.abort_batch()

    @mock.patch(
        "google.cloud.spanner_dbapi.batch_dml_executor.BatchDmlExecutor", autospec=True
    )
    def test_abort_dml_batch(self, mock_batch_dml_executor):
        self._under_test._batch_mode = BatchMode.DML
        self._under_test._batch_dml_executor = mock_batch_dml_executor

        self._under_test.abort_batch()

        self.assertEqual(self._under_test._batch_mode, BatchMode.NONE)
        self.assertEqual(self._under_test._batch_dml_executor, None)

    def test_set_autocommit_dml_mode_with_autocommit_false(self):
        self._under_test.autocommit = False
        parsed_statement = ParsedStatement(
            StatementType.CLIENT_SIDE,
            Statement("sql"),
            ClientSideStatementType.SET_AUTOCOMMIT_DML_MODE,
            ["PARTITIONED_NON_ATOMIC"],
        )

        with self.assertRaises(ProgrammingError):
            self._under_test._set_autocommit_dml_mode(parsed_statement)

    def test_set_autocommit_dml_mode_with_readonly(self):
        self._under_test.autocommit = True
        self._under_test.read_only = True
        parsed_statement = ParsedStatement(
            StatementType.CLIENT_SIDE,
            Statement("sql"),
            ClientSideStatementType.SET_AUTOCOMMIT_DML_MODE,
            ["PARTITIONED_NON_ATOMIC"],
        )

        with self.assertRaises(ProgrammingError):
            self._under_test._set_autocommit_dml_mode(parsed_statement)

    def test_set_autocommit_dml_mode_with_batch_mode(self):
        self._under_test.autocommit = True
        parsed_statement = ParsedStatement(
            StatementType.CLIENT_SIDE,
            Statement("sql"),
            ClientSideStatementType.SET_AUTOCOMMIT_DML_MODE,
            ["PARTITIONED_NON_ATOMIC"],
        )

        self._under_test._set_autocommit_dml_mode(parsed_statement)

        assert (
            self._under_test.autocommit_dml_mode
            == AutocommitDmlMode.PARTITIONED_NON_ATOMIC
        )

    def test_set_autocommit_dml_mode(self):
        self._under_test.autocommit = True
        parsed_statement = ParsedStatement(
            StatementType.CLIENT_SIDE,
            Statement("sql"),
            ClientSideStatementType.SET_AUTOCOMMIT_DML_MODE,
            ["PARTITIONED_NON_ATOMIC"],
        )

        self._under_test._set_autocommit_dml_mode(parsed_statement)
        assert (
            self._under_test.autocommit_dml_mode
            == AutocommitDmlMode.PARTITIONED_NON_ATOMIC
        )

    @mock.patch("google.cloud.spanner_v1.database.Database", autospec=True)
    def test_run_prior_DDL_statements(self, mock_database):
        from google.cloud.spanner_dbapi import Connection, InterfaceError

        connection = Connection(INSTANCE, mock_database)

        connection.run_prior_DDL_statements()
        mock_database.update_ddl.assert_not_called()

        ddl = ["ddl"]
        connection._ddl_statements = ddl

        connection.run_prior_DDL_statements()
        mock_database.update_ddl.assert_called_once_with(ddl)

        connection.is_closed = True

        with self.assertRaises(InterfaceError):
            connection.run_prior_DDL_statements()

    def test_run_prior_DDL_statements_database_error(self):
        from google.cloud.spanner_dbapi import Connection

        connection = Connection(INSTANCE)
        with pytest.raises(ValueError):
            connection.run_prior_DDL_statements()

    def test_as_context_manager(self):
        connection = self._make_connection()
        with connection as conn:
            self.assertEqual(conn, connection)

        self.assertTrue(connection.is_closed)

    def test_begin_cursor_closed(self):
        self._under_test.close()

        with self.assertRaises(InterfaceError):
            self._under_test.begin()

        self.assertEqual(self._under_test._transaction_begin_marked, False)

    def test_begin_transaction_begin_marked(self):
        self._under_test._transaction_begin_marked = True

        with self.assertRaises(OperationalError):
            self._under_test.begin()

    def test_begin_transaction_started(self):
        self._under_test._spanner_transaction_started = True

        with self.assertRaises(OperationalError):
            self._under_test.begin()

        self.assertEqual(self._under_test._transaction_begin_marked, False)

    def test_begin(self):
        self._under_test.begin()

        self.assertEqual(self._under_test._transaction_begin_marked, True)

    def test_validate_ok(self):
        connection = self._make_connection()

        # mock snapshot context manager
        snapshot_obj = mock.Mock()
        snapshot_obj.execute_sql = mock.Mock(return_value=[[1]])

        snapshot_ctx = mock.Mock()
        snapshot_ctx.__enter__ = mock.Mock(return_value=snapshot_obj)
        snapshot_ctx.__exit__ = exit_ctx_func
        snapshot_method = mock.Mock(return_value=snapshot_ctx)

        connection.database.snapshot = snapshot_method

        connection.validate()
        snapshot_obj.execute_sql.assert_called_once_with("SELECT 1")

    def test_validate_fail(self):
        from google.cloud.spanner_dbapi.exceptions import OperationalError

        connection = self._make_connection()

        # mock snapshot context manager
        snapshot_obj = mock.Mock()
        snapshot_obj.execute_sql = mock.Mock(return_value=[[3]])

        snapshot_ctx = mock.Mock()
        snapshot_ctx.__enter__ = mock.Mock(return_value=snapshot_obj)
        snapshot_ctx.__exit__ = exit_ctx_func
        snapshot_method = mock.Mock(return_value=snapshot_ctx)

        connection.database.snapshot = snapshot_method

        with self.assertRaises(OperationalError):
            connection.validate()

        snapshot_obj.execute_sql.assert_called_once_with("SELECT 1")

    def test_validate_error(self):
        from google.cloud.exceptions import NotFound

        connection = self._make_connection()

        # mock snapshot context manager
        snapshot_obj = mock.Mock()
        snapshot_obj.execute_sql = mock.Mock(side_effect=NotFound("Not found"))

        snapshot_ctx = mock.Mock()
        snapshot_ctx.__enter__ = mock.Mock(return_value=snapshot_obj)
        snapshot_ctx.__exit__ = exit_ctx_func
        snapshot_method = mock.Mock(return_value=snapshot_ctx)

        connection.database.snapshot = snapshot_method

        with self.assertRaises(NotFound):
            connection.validate()

        snapshot_obj.execute_sql.assert_called_once_with("SELECT 1")

    def test_validate_database_error(self):
        from google.cloud.spanner_dbapi import Connection

        connection = Connection(INSTANCE)

        with pytest.raises(ValueError):
            connection.validate()

    def test_validate_closed(self):
        from google.cloud.spanner_dbapi.exceptions import InterfaceError

        connection = self._make_connection()
        connection.close()

        with self.assertRaises(InterfaceError):
            connection.validate()

    def test_staleness_invalid_value(self):
        """Check that `staleness` property accepts only correct values."""
        connection = self._make_connection()

        # incorrect staleness type
        with self.assertRaises(ValueError):
            connection.staleness = {"something": 4}

        # no expected staleness types
        with self.assertRaises(ValueError):
            connection.staleness = {}

    def test_staleness_inside_transaction(self):
        """
        Check that it's impossible to change the `staleness`
        option if a transaction is in progress.
        """
        connection = self._make_connection()
        connection._spanner_transaction_started = True
        connection._transaction = mock.Mock()

        with self.assertRaises(ValueError):
            connection.staleness = {"read_timestamp": datetime.datetime(2021, 9, 21)}

    def test_staleness_inside_transaction_same_value(self):
        """
        Verify that setting `staleness` to the same value in a transaction is allowed.
        """
        connection = self._make_connection()
        connection.staleness = {"read_timestamp": datetime.datetime(2021, 9, 21)}
        connection._spanner_transaction_started = True
        connection._transaction = mock.Mock()

        connection.staleness = {"read_timestamp": datetime.datetime(2021, 9, 21)}
        self.assertEqual(
            connection.staleness, {"read_timestamp": datetime.datetime(2021, 9, 21)}
        )

    def test_staleness_multi_use(self):
        """
        Check that `staleness` option is correctly
        sent to the `Snapshot()` constructor.

        READ_ONLY, NOT AUTOCOMMIT
        """
        timestamp = datetime.datetime(2021, 9, 20)

        connection = self._make_connection()
        connection._session = "session"
        connection.read_only = True
        connection.staleness = {"read_timestamp": timestamp}

        with mock.patch(
            "google.cloud.spanner_dbapi.connection.Snapshot"
        ) as snapshot_mock:
            connection.snapshot_checkout()

        snapshot_mock.assert_called_with(
            "session", multi_use=True, read_timestamp=timestamp
        )

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_staleness_single_use_autocommit(self, MockedPeekIterator):
        """
        Check that `staleness` option is correctly
        sent to the snapshot context manager.

        NOT READ_ONLY, AUTOCOMMIT
        """
        timestamp = datetime.datetime(2021, 9, 20)

        connection = self._make_connection()
        connection._session_checkout = mock.MagicMock(autospec=True)

        connection.autocommit = True
        connection.staleness = {"read_timestamp": timestamp}

        # mock snapshot context manager
        snapshot_obj = mock.Mock()
        _result_set = mock.Mock()
        snapshot_obj.execute_sql.return_value = _result_set
        _result_set.stats = None

        snapshot_ctx = mock.Mock()
        snapshot_ctx.__enter__ = mock.Mock(return_value=snapshot_obj)
        snapshot_ctx.__exit__ = exit_ctx_func
        snapshot_method = mock.Mock(return_value=snapshot_ctx)

        connection.database.snapshot = snapshot_method

        cursor = connection.cursor()
        cursor.execute("SELECT 1")

        connection.database.snapshot.assert_called_with(read_timestamp=timestamp)

    @mock.patch("google.cloud.spanner_dbapi.cursor.PeekIterator")
    def test_staleness_single_use_readonly_autocommit(self, MockedPeekIterator):
        """
        Check that `staleness` option is correctly sent to the
        snapshot context manager while in `autocommit` mode.

        READ_ONLY, AUTOCOMMIT
        """
        timestamp = datetime.datetime(2021, 9, 20)

        connection = self._make_connection()
        connection.autocommit = True
        connection.read_only = True
        connection._session_checkout = mock.MagicMock(autospec=True)

        connection.staleness = {"read_timestamp": timestamp}

        # mock snapshot context manager
        snapshot_obj = mock.Mock()
        _result_set = mock.Mock()
        _result_set.stats = None

        snapshot_obj.execute_sql.return_value = _result_set

        snapshot_ctx = mock.Mock()
        snapshot_ctx.__enter__ = mock.Mock(return_value=snapshot_obj)
        snapshot_ctx.__exit__ = exit_ctx_func
        snapshot_method = mock.Mock(return_value=snapshot_ctx)

        connection.database.snapshot = snapshot_method

        cursor = connection.cursor()
        cursor.execute("SELECT 1")

        connection.database.snapshot.assert_called_with(read_timestamp=timestamp)

    def test_request_priority(self):
        from google.cloud.spanner_dbapi.parsed_statement import Statement
        from google.cloud.spanner_v1 import RequestOptions

        sql = "SELECT 1"
        params = []
        param_types = {}
        priority = 2

        connection = self._make_connection()
        connection._spanner_transaction_started = True
        connection._transaction = mock.Mock()
        connection._transaction.execute_sql = mock.Mock()

        connection.request_priority = priority

        req_opts = RequestOptions(priority=priority)

        connection.run_statement(Statement(sql, params, param_types))

        connection._transaction.execute_sql.assert_called_with(
            sql, params, param_types=param_types, request_options=req_opts
        )
        assert connection.request_priority is None

        # check that priority is applied for only one request
        connection.run_statement(Statement(sql, params, param_types))

        connection._transaction.execute_sql.assert_called_with(
            sql, params, param_types=param_types, request_options=None
        )

    def test_custom_client_connection(self):
        from google.cloud.spanner_dbapi import connect

        client = _Client()
        connection = connect("test-instance", "test-database", client=client)
        self.assertTrue(connection.instance._client == client)

    def test_custom_database_role(self):
        from google.cloud.spanner_dbapi import connect

        role = "some_role"
        connection = connect(
            "test-instance",
            "test-database",
            project="test-project",
            database_role=role,
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "none"},
        )
        self.assertEqual(connection.database.database_role, role)

    def test_invalid_custom_client_connection(self):
        from google.cloud.spanner_dbapi import connect

        client = _Client()
        with pytest.raises(ValueError):
            connect(
                "test-instance",
                "test-database",
                project="invalid_project",
                client=client,
            )

    def test_connection_wo_database(self):
        from google.cloud.spanner_dbapi import connect

        connection = connect(
            "test-instance",
            credentials=AnonymousCredentials(),
            project="test-project",
            client_options={"api_endpoint": "none"},
        )
        self.assertTrue(connection.database is None)

    def test_connect_w_instance_type_omni(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.client import InstanceType

        connection = connect(
            "test-instance",
            credentials=AnonymousCredentials(),
            client_options={"api_endpoint": "omni-host:15000"},
            instance_type=InstanceType.OMNI,
        )
        self.assertEqual(connection.spanner_client.project, "default")
        self.assertEqual(connection.spanner_client.instance_type, InstanceType.OMNI)
        self.assertEqual(connection.spanner_client._host, "omni-host:15000")

    def test_connect_w_instance_type_omni_no_host_raises_error(self):
        from google.cloud.spanner_dbapi import connect
        from google.cloud.spanner_v1.client import InstanceType

        with self.assertRaises(ValueError) as ctx:
            connect(
                "test-instance",
                credentials=AnonymousCredentials(),
                instance_type=InstanceType.OMNI,
            )
        self.assertIn(
            "Host must be set for connecting to Spanner Omni instances",
            str(ctx.exception),
        )

    def test_connect_w_invalid_instance_type_raises_error(self):
        from google.cloud.spanner_dbapi import connect

        with self.assertRaises(ValueError) as ctx:
            connect(
                "test-instance",
                credentials=AnonymousCredentials(),
                instance_type="invalid-type",
            )
        self.assertIn(
            "instance_type must be one of 'cloud' or 'omni'", str(ctx.exception)
        )

    def test_partition_query_data_boost_enabled(self):
        from google.cloud.spanner_dbapi.parse_utils import classify_statement

        connection = self._make_connection(read_only=True, data_boost_enabled=True)
        batch_snapshot = mock.MagicMock()
        batch_snapshot.generate_query_batches.return_value = []
        batch_snapshot.get_batch_transaction_id.return_value = mock.MagicMock(
            transaction_id=b"tx", session_id="sess", read_timestamp=None
        )
        connection.database.batch_snapshot = mock.MagicMock(return_value=batch_snapshot)

        parsed_stmt = classify_statement("PARTITION SELECT 1")
        res = connection.partition_query(parsed_stmt)
        self.assertEqual(res, [])
        batch_snapshot.generate_query_batches.assert_called_once_with(
            "SELECT 1",
            None,
            None,
            query_options=None,
            data_boost_enabled=True,
        )

    def test_run_partitioned_query_data_boost_enabled(self):
        from google.cloud.spanner_dbapi.parse_utils import classify_statement

        connection = self._make_connection(read_only=True, data_boost_enabled=True)
        batch_snapshot = mock.MagicMock()
        batch_snapshot.run_partitioned_query.return_value = "merged_result_set"
        connection.database.batch_snapshot = mock.MagicMock(return_value=batch_snapshot)

        parsed_stmt = classify_statement("RUN PARTITIONED QUERY SELECT 1")
        res = connection.run_partitioned_query(parsed_stmt)
        self.assertEqual(res, "merged_result_set")
        batch_snapshot.run_partitioned_query.assert_called_once_with(
            "SELECT 1",
            None,
            None,
            data_boost_enabled=True,
        )


def exit_ctx_func(self, exc_type, exc_value, traceback):
    """Context __exit__ method mock."""
    pass


class _Client(object):
    def __init__(self, project="project_id"):
        self.project = project
        self.project_name = "projects/" + self.project
        self._client_context = None

    def instance(self, instance_id="instance_id"):
        return _Instance(name=instance_id, client=self)


class _Instance(object):
    def __init__(self, name="instance_id", client=None, experimental_host=None):
        self.name = name
        self._client = client
        self.experimental_host = experimental_host

    def database(
        self,
        database_id="database_id",
        pool=None,
        database_dialect=DatabaseDialect.GOOGLE_STANDARD_SQL,
        database_role=None,
        logger=None,
    ):
        return _Database(database_id, pool, database_dialect, database_role, logger)


class _Database(object):
    def __init__(
        self,
        database_id="database_id",
        pool=None,
        database_dialect=DatabaseDialect.GOOGLE_STANDARD_SQL,
        database_role=None,
        logger=None,
    ):
        self.name = database_id
        self.pool = pool
        self.database_dialect = database_dialect
        self.database_role = database_role
        self.logger = logger
