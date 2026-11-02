# Copyright 2021 Google LLC All rights reserved.
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
import base64
import datetime
import decimal
import time
from collections import defaultdict

import pytest
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud._helpers import UTC

from google.cloud import spanner_v1
from google.cloud.spanner_dbapi.connection import Connection, connect
from google.cloud.spanner_dbapi.exceptions import (
    OperationalError,
    ProgrammingError,
    RetryAborted,
)
from google.cloud.spanner_dbapi.parsed_statement import AutocommitDmlMode
from google.cloud.spanner_v1 import JsonObject
from google.cloud.spanner_v1 import gapic_version as package_version
from google.cloud.spanner_v1.database_sessions_manager import TransactionType
from tests._helpers import is_multiplexed_enabled

from . import _helpers

DATABASE_NAME = "dbapi-txn"
SPANNER_RPC_PREFIX = "/google.spanner.v1.Spanner/"
EXECUTE_BATCH_DML_METHOD = SPANNER_RPC_PREFIX + "ExecuteBatchDml"
COMMIT_METHOD = SPANNER_RPC_PREFIX + "Commit"
EXECUTE_SQL_METHOD = SPANNER_RPC_PREFIX + "ExecuteSql"
EXECUTE_STREAMING_SQL_METHOD = SPANNER_RPC_PREFIX + "ExecuteStreamingSql"

DDL = """CREATE TABLE contacts (
        contact_id INT64,
        first_name STRING(1024),
        last_name STRING(1024),
        email STRING(1024)
    )
    PRIMARY KEY (contact_id);
    CREATE VIEW contacts_emails
    SQL SECURITY INVOKER
    AS
    SELECT c.email
    FROM contacts AS c;

    CREATE TABLE all_types (
        id int64,
        col_bool bool,
        col_bytes bytes(max),
        col_date date,
        col_float32 float32,
        col_float64 float64,
        col_int64 int64,
        col_json json,
        col_numeric numeric,
        col_string string(max),
        coL_timestamp timestamp,
    ) primary key (col_int64);
    """

DDL_STATEMENTS = [stmt.strip() for stmt in DDL.split(";") if stmt.strip()]


@pytest.fixture(scope="session")
def raw_database(shared_instance, database_operation_timeout, not_postgres):
    database_id = _helpers.unique_id("dbapi-txn")
    pool = spanner_v1.BurstyPool(labels={"testcase": "database_api"})
    database = shared_instance.database(
        database_id,
        ddl_statements=DDL_STATEMENTS,
        pool=pool,
        enable_interceptors_in_tests=True,
    )
    op = database.create()
    op.result(database_operation_timeout)  # raises on failure / timeout.

    yield database

    database.drop()


class TestDbApi:
    @staticmethod
    def clear_table(transaction):
        transaction.execute_update("DELETE FROM contacts WHERE true")
        transaction.execute_update("DELETE FROM all_types WHERE true")

    @pytest.fixture(scope="function")
    def dbapi_database(self, raw_database):
        # Resetting the count so that each test gives correct count of the api
        # methods called during that test
        raw_database._method_count_interceptor._counts = defaultdict(int)
        raw_database.run_in_transaction(self.clear_table)

        yield raw_database

    @pytest.fixture(autouse=True)
    def init_connection(self, request, shared_instance, dbapi_database):
        if "noautofixt" not in request.keywords:
            self._conn = Connection(shared_instance, dbapi_database)
            self._cursor = self._conn.cursor()
        yield
        if "noautofixt" not in request.keywords:
            self._cursor.close()
            self._conn.close()

    def _execute_common_statements(self, cursor):
        # execute several DML statements within one transaction
        cursor.execute(
            """
                INSERT INTO contacts (contact_id, first_name, last_name, email)
                VALUES (1, 'first-name', 'last-name', 'test.email@domen.ru')
                """
        )
        cursor.execute(
            """
                UPDATE contacts
                SET first_name = 'updated-first-name'
                WHERE first_name = 'first-name'
                """
        )
        cursor.execute(
            """
                UPDATE contacts
                SET email = 'test.email_updated@domen.ru'
                WHERE email = 'test.email@domen.ru'
                """
        )
        return (
            1,
            "updated-first-name",
            "last-name",
            "test.email_updated@domen.ru",
        )

    @pytest.mark.parametrize("client_side", [True, False])
    def test_commit(self, client_side):
        """Test committing a transaction with several statements."""
        updated_row = self._execute_common_statements(self._cursor)
        if client_side:
            self._cursor.execute("""COMMIT""")
        else:
            self._conn.commit()

        # read the resulting data from the database
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()

        assert got_rows == [updated_row]

    @pytest.mark.skipif(
        _helpers.USE_EMULATOR,
        reason="Emulator does not support multiple parallel transactions.",
    )
    def test_commit_exception(self):
        """Test that if exception during commit method is caught, then
        subsequent operations on same Cursor and Connection object works
        properly."""

        if is_multiplexed_enabled(transaction_type=TransactionType.READ_WRITE):
            pytest.skip(
                "Mutiplexed session can't be deleted and this test relies on session deletion."
            )

        self._execute_common_statements(self._cursor)
        # deleting the session to fail the commit
        self._conn._session.delete()
        try:
            self._conn.commit()
        except Exception:
            pass

        # Testing that the connection and Cursor are in proper state post commit
        # and a new transaction is started
        updated_row = self._execute_common_statements(self._cursor)
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()

        assert got_rows == [updated_row]

    @pytest.mark.skipif(
        _helpers.USE_EMULATOR,
        reason="Emulator does not support multiple parallel transactions.",
    )
    def test_rollback_exception(self):
        """Test that if exception during rollback method is caught, then
        subsequent operations on same Cursor and Connection object works
        properly."""
        self._execute_common_statements(self._cursor)
        # deleting the session to fail the rollback
        self._conn._session.delete()
        try:
            self._conn.rollback()
        except Exception:
            pass

        # Testing that the connection and Cursor are in proper state post
        # exception in rollback and a new transaction is started
        updated_row = self._execute_common_statements(self._cursor)
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()

        assert got_rows == [updated_row]

    def test_cursor_execute_exception(self):
        """Test that if exception in Cursor's execute method is caught when
        Connection is not in autocommit mode, then subsequent operations on
        same Cursor and Connection object works properly."""
        updated_row = self._execute_common_statements(self._cursor)
        try:
            self._cursor.execute("SELECT * FROM unknown_table")
        except Exception:
            pass
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()
        assert got_rows == [updated_row]

        # Testing that the connection and Cursor are in proper state post commit
        # and a new transaction is started
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()
        assert got_rows == [updated_row]

    def test_cursor_execute_exception_autocommit(self):
        """Test that if exception in Cursor's execute method is caught when
        Connection is in autocommit mode, then subsequent operations on
        same Cursor and Connection object works properly."""
        self._conn.autocommit = True
        updated_row = self._execute_common_statements(self._cursor)
        try:
            self._cursor.execute("SELECT * FROM unknown_table")
        except Exception:
            pass
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        assert got_rows == [updated_row]

    def test_cursor_execute_exception_begin_client_side(self):
        """Test that if exception in Cursor's execute method is caught when
        beginning a transaction using client side statement, then subsequent
        operations on same Cursor and Connection object works properly."""
        self._conn.autocommit = True
        self._cursor.execute("begin transaction")
        updated_row = self._execute_common_statements(self._cursor)
        try:
            self._cursor.execute("SELECT * FROM unknown_table")
        except Exception:
            pass
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()
        assert got_rows == [updated_row]

        # Testing that the connection and Cursor are in proper state post commit
        self._conn.autocommit = False
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()
        assert got_rows == [updated_row]

    @pytest.mark.noautofixt
    def test_begin_client_side(self, shared_instance, dbapi_database):
        """Test beginning a transaction using client side statement,
        where connection is in autocommit mode."""

        conn1 = Connection(shared_instance, dbapi_database)
        conn1.autocommit = True
        cursor1 = conn1.cursor()
        cursor1.execute("begin transaction")
        updated_row = self._execute_common_statements(cursor1)

        assert conn1._transaction_begin_marked is True
        conn1.commit()
        assert conn1._transaction_begin_marked is False
        cursor1.close()
        conn1.close()

        # As the connection conn1 is committed a new connection should see its results
        conn3 = Connection(shared_instance, dbapi_database)
        cursor3 = conn3.cursor()
        cursor3.execute("SELECT * FROM contacts")
        got_rows = cursor3.fetchall()
        conn3.commit()
        cursor3.close()
        conn3.close()
        assert got_rows == [updated_row]

    def test_noop_sql_statements(self, dbapi_database):
        """Test beginning and then committing a transaction is a Noop"""
        dbapi_database._method_count_interceptor.reset()
        self._cursor.execute("begin transaction")
        self._cursor.execute("commit transaction")
        assert dbapi_database._method_count_interceptor._counts == {}
        self._cursor.execute("SELECT * FROM contacts")
        self._conn.commit()
        assert self._cursor.fetchall() == []

        """Test beginning and then rolling back a transaction is a Noop"""
        dbapi_database._method_count_interceptor.reset()
        self._cursor.execute("begin transaction")
        self._cursor.execute("rollback transaction")
        assert dbapi_database._method_count_interceptor._counts == {}
        self._cursor.execute("SELECT * FROM contacts")
        assert self._cursor.fetchall() == []
        self._conn.commit()

        dbapi_database._method_count_interceptor.reset()
        self._cursor.execute("start batch dml")
        self._cursor.execute("run batch")
        assert dbapi_database._method_count_interceptor._counts == {}

    def test_read_and_commit_timestamps(self):
        """Test COMMIT_TIMESTAMP is not available after read statement and
        READ_TIMESTAMP is not available after write statement in autocommit
        mode."""
        self._conn.autocommit = True
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.execute(
            """
            INSERT INTO contacts (contact_id, first_name, last_name, email)
            VALUES (1, 'first-name', 'last-name', 'test.email@domen.ru')
            """
        )

        self._cursor.execute("SHOW VARIABLE COMMIT_TIMESTAMP")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 1

        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 0

        self._cursor.execute("SELECT * FROM contacts")

        self._cursor.execute("SHOW VARIABLE COMMIT_TIMESTAMP")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 0

        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 1

    def test_commit_timestamp_client_side_transaction(self):
        """Test executing SHOW_COMMIT_TIMESTAMP client side statement in a
        transaction."""

        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (1, 'first-name', 'last-name', 'test.email@domen.ru')
        """
        )
        self._cursor.execute("SHOW VARIABLE COMMIT_TIMESTAMP")
        got_rows = self._cursor.fetchall()
        # As the connection is not committed we will get 0 rows
        assert len(got_rows) == 0
        assert len(self._cursor.description) == 1

        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
        """
        )
        self._conn.commit()
        self._cursor.execute("SHOW VARIABLE COMMIT_TIMESTAMP")

        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 1
        assert len(got_rows[0]) == 1
        assert len(self._cursor.description) == 1
        assert self._cursor.description[0].name == "SHOW_COMMIT_TIMESTAMP"
        assert isinstance(got_rows[0][0], DatetimeWithNanoseconds)

    def test_commit_timestamp_client_side_autocommit(self):
        """Test executing SHOW_COMMIT_TIMESTAMP client side statement in a
        transaction when connection is in autocommit mode."""

        self._conn.autocommit = True
        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
        """
        )
        self._cursor.execute("SHOW VARIABLE COMMIT_TIMESTAMP")

        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 1
        assert len(got_rows[0]) == 1
        assert len(self._cursor.description) == 1
        assert self._cursor.description[0].name == "SHOW_COMMIT_TIMESTAMP"
        assert isinstance(got_rows[0][0], DatetimeWithNanoseconds)

    def test_read_timestamp_client_side(self):
        """Test executing SHOW_READ_TIMESTAMP client side statement in a
        transaction."""

        self._conn.read_only = True
        self._cursor.execute("SELECT * FROM contacts")
        assert self._cursor.fetchall() == []

        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        read_timestamp_query_result_1 = self._cursor.fetchall()

        self._cursor.execute("SELECT * FROM contacts")
        assert self._cursor.fetchall() == []

        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        read_timestamp_query_result_2 = self._cursor.fetchall()

        self._conn.commit()

        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        read_timestamp_query_result_3 = self._cursor.fetchall()
        assert len(self._cursor.description) == 1
        assert self._cursor.description[0].name == "SHOW_READ_TIMESTAMP"

        assert (
            read_timestamp_query_result_1
            == read_timestamp_query_result_2
            == read_timestamp_query_result_3
        )
        assert len(read_timestamp_query_result_1) == 1
        assert len(read_timestamp_query_result_1[0]) == 1
        assert isinstance(read_timestamp_query_result_1[0][0], DatetimeWithNanoseconds)

        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        read_timestamp_query_result_4 = self._cursor.fetchall()
        self._conn.commit()
        assert read_timestamp_query_result_1 != read_timestamp_query_result_4

    def test_read_timestamp_client_side_autocommit(self):
        """Test executing SHOW_READ_TIMESTAMP client side statement in a
        transaction when connection is in autocommit mode."""

        self._conn.autocommit = True

        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
        """
        )
        self._conn.read_only = True
        self._cursor.execute("SELECT * FROM contacts")
        assert self._cursor.fetchall() == [
            (2, "first-name", "last-name", "test.email@domen.ru")
        ]
        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        read_timestamp_query_result_1 = self._cursor.fetchall()

        assert len(read_timestamp_query_result_1) == 1
        assert len(read_timestamp_query_result_1[0]) == 1
        assert len(self._cursor.description) == 1
        assert self._cursor.description[0].name == "SHOW_READ_TIMESTAMP"
        assert isinstance(read_timestamp_query_result_1[0][0], DatetimeWithNanoseconds)

        self._conn.read_only = False
        self._insert_row(3)

        self._conn.read_only = True
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.execute("SHOW VARIABLE READ_TIMESTAMP")
        read_timestamp_query_result_2 = self._cursor.fetchall()
        assert read_timestamp_query_result_1 != read_timestamp_query_result_2

    @pytest.mark.parametrize("auto_commit", [False, True])
    def test_batch_dml(self, auto_commit, dbapi_database):
        """Test batch dml."""

        method_count_interceptor = dbapi_database._method_count_interceptor
        method_count_interceptor.reset()
        if auto_commit:
            self._conn.autocommit = True
        self._insert_row(1)

        self._cursor.execute("start batch dml")
        self._insert_row(2)
        self._insert_row(3)
        self._cursor.execute("run batch")

        self._insert_row(4)

        # Test starting another dml batch in same transaction works
        self._cursor.execute("start batch dml")
        self._insert_row(5)
        self._insert_row(6)
        self._cursor.execute("run batch")

        if not auto_commit:
            self._conn.commit()

        self._cursor.execute("SELECT * FROM contacts")
        assert (
            self._cursor.fetchall().sort()
            == (
                [
                    (1, "first-name-1", "last-name-1", "test.email@domen.ru"),
                    (2, "first-name-2", "last-name-2", "test.email@domen.ru"),
                    (3, "first-name-3", "last-name-3", "test.email@domen.ru"),
                    (4, "first-name-4", "last-name-4", "test.email@domen.ru"),
                    (5, "first-name-5", "last-name-5", "test.email@domen.ru"),
                    (6, "first-name-6", "last-name-6", "test.email@domen.ru"),
                ]
            ).sort()
        )

        # Test starting another dml batch in same connection post commit works
        self._cursor.execute("start batch dml")
        self._insert_row(7)
        self._insert_row(8)
        self._cursor.execute("run batch")

        self._insert_row(9)

        if not auto_commit:
            self._conn.commit()

        self._cursor.execute("SELECT * FROM contacts")
        assert len(self._cursor.fetchall()) == 9
        # Test that ExecuteBatchDml rpc is called
        assert method_count_interceptor._counts[EXECUTE_BATCH_DML_METHOD] == 3

    def test_abort_batch_dml(self):
        """Test abort batch dml."""

        self._cursor.execute("start batch dml")
        self._insert_row(1)
        self._insert_row(2)
        self._cursor.execute("abort batch")

        self._insert_row(3)
        self._conn.commit()

        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 1
        assert got_rows == [(3, "first-name-3", "last-name-3", "test.email@domen.ru")]

    def test_batch_dml_invalid_statements(self):
        """Test batch dml having invalid statements."""

        # Test first statement in batch is invalid
        self._cursor.execute("start batch dml")
        self._cursor.execute(
            """
            INSERT INTO unknown_table (contact_id, first_name, last_name, email)
            VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
            """
        )
        self._insert_row(1)
        self._insert_row(2)
        with pytest.raises(OperationalError):
            self._cursor.execute("run batch")

        # Test middle statement in batch is invalid
        self._cursor.execute("start batch dml")
        self._insert_row(1)
        self._cursor.execute(
            """
            INSERT INTO unknown_table (contact_id, first_name, last_name, email)
            VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
            """
        )
        self._insert_row(2)
        with pytest.raises(OperationalError):
            self._cursor.execute("run batch")

        # Test last statement in batch is invalid
        self._cursor.execute("start batch dml")
        self._insert_row(1)
        self._insert_row(2)
        self._cursor.execute(
            """
            INSERT INTO unknown_table (contact_id, first_name, last_name, email)
            VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
            """
        )
        with pytest.raises(OperationalError):
            self._cursor.execute("run batch")

    def test_partitioned_query(self):
        """Test partition query works in read-only mode."""
        self._cursor.execute("start batch dml")
        for i in range(1, 11):
            self._insert_row(i)
        self._cursor.execute("run batch")
        self._conn.commit()

        self._conn.read_only = True
        self._cursor.execute("PARTITION SELECT * FROM contacts")
        partition_id_rows = self._cursor.fetchall()
        assert len(partition_id_rows) > 0

        rows = []
        for partition_id_row in partition_id_rows:
            self._cursor.execute("RUN PARTITION " + partition_id_row[0])
            rows = rows + self._cursor.fetchall()
        assert len(rows) == 10
        self._conn.commit()

    def test_partitioned_query_in_rw_transaction(self):
        """Test partition query throws exception when connection is not in
        read-only mode and neither in auto-commit mode."""
        self._cursor.execute("start batch dml")
        for i in range(1, 11):
            self._insert_row(i)
        self._cursor.execute("run batch")
        self._conn.commit()

        with pytest.raises(ProgrammingError):
            self._cursor.execute("PARTITION SELECT * FROM contacts")

    def test_partitioned_query_with_dml_query(self):
        """Test partition query throws exception when sql query is a DML query."""
        self._cursor.execute("start batch dml")
        for i in range(1, 11):
            self._insert_row(i)
        self._cursor.execute("run batch")
        self._conn.commit()

        self._conn.read_only = True
        with pytest.raises(ProgrammingError):
            self._cursor.execute(
                """
                PARTITION INSERT INTO contacts (contact_id, first_name, last_name, email)
                VALUES (1111, 'first-name', 'last-name', 'test.email@domen.ru')
                """
            )

    def test_partitioned_query_in_autocommit_mode(self):
        """Test partition query works when connection is not in read-only mode
        but is in auto-commit mode."""
        self._cursor.execute("start batch dml")
        for i in range(1, 11):
            self._insert_row(i)
        self._cursor.execute("run batch")
        self._conn.commit()

        self._conn.autocommit = True
        self._cursor.execute("PARTITION SELECT * FROM contacts")
        partition_id_rows = self._cursor.fetchall()
        assert len(partition_id_rows) > 0

        rows = []
        for partition_id_row in partition_id_rows:
            self._cursor.execute("RUN PARTITION " + partition_id_row[0])
            rows = rows + self._cursor.fetchall()
        assert len(rows) == 10
        self._conn.commit()

    def test_partitioned_query_with_client_transaction_started(self):
        """Test partition query throws exception when connection is in
        auto-commit mode but transaction started using client side statement."""
        self._cursor.execute("start batch dml")
        for i in range(1, 11):
            self._insert_row(i)
        self._cursor.execute("run batch")
        self._conn.commit()

        self._conn.autocommit = True
        self._cursor.execute("begin transaction")
        with pytest.raises(ProgrammingError):
            self._cursor.execute("PARTITION SELECT * FROM contacts")

    def test_run_partitioned_query(self):
        """Test run partitioned query works in read-only mode."""
        self._cursor.execute("start batch dml")
        for i in range(1, 11):
            self._insert_row(i)
        self._cursor.execute("run batch")
        self._conn.commit()

        self._conn.read_only = True
        self._cursor.execute("RUN PARTITIONED QUERY SELECT * FROM contacts")
        assert self._cursor.description is not None
        assert self._cursor.rowcount == -1
        rows = self._cursor.fetchall()
        assert len(rows) == 10
        self._conn.commit()

    def test_partitioned_dml_query(self):
        """Test partitioned_dml query works in autocommit mode."""
        self._cursor.execute("start batch dml")
        for i in range(1, 11):
            self._insert_row(i)
        self._cursor.execute("run batch")
        self._conn.commit()

        self._conn.autocommit = True
        self._cursor.execute("set autocommit_dml_mode = PARTITIONED_NON_ATOMIC")
        self._cursor.execute("DELETE FROM contacts WHERE contact_id > 3")
        assert self._cursor.rowcount == 7

        self._cursor.execute("set autocommit_dml_mode = TRANSACTIONAL")
        assert self._conn.autocommit_dml_mode == AutocommitDmlMode.TRANSACTIONAL

        self._conn.autocommit = False
        # Test changing autocommit_dml_mode is not allowed when connection is in autocommit mode
        with pytest.raises(ProgrammingError):
            self._cursor.execute("set autocommit_dml_mode = PARTITIONED_NON_ATOMIC")

    def _insert_row(self, i):
        self._cursor.execute(
            f"""
            INSERT INTO contacts (contact_id, first_name, last_name, email)
            VALUES ({i}, 'first-name-{i}', 'last-name-{i}', 'test.email@domen.ru')
            """
        )

    def test_commit_abort_retry(self, dbapi_database):
        """Test that when commit failed with Abort exception, then the retry
        succeeds with transaction having insert as well as query type of
        statements along with batch dml statements.
        We are trying to test all types of statements like execute, executemany,
        fetchone, fetchmany, fetchall"""

        method_count_interceptor = dbapi_database._method_count_interceptor
        method_count_interceptor.reset()
        # called 2 times
        self._insert_row(1)
        # called 2 times
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.fetchall()
        self._cursor.execute("start batch dml")
        self._insert_row(2)
        self._insert_row(3)
        # called 2 times for batch dml rpc
        self._cursor.execute("run batch")
        row_data = [
            (4, "first-name4", "last-name4", "test.email4@example.com"),
            (5, "first-name5", "last-name5", "test.email5@example.com"),
        ]
        # called 2 times for batch dml rpc
        self._cursor.executemany(
            """
                INSERT INTO contacts (contact_id, first_name, last_name, email)
                VALUES (%s, %s, %s, %s)
            """,
            row_data,
        )
        # called 2 times and as this would make 3 execute streaming sql calls
        # so total 6 calls
        self._cursor.executemany(
            """SELECT * FROM contacts WHERE contact_id = %s""",
            ((1,), (2,), (3,)),
        )
        self._cursor.fetchone()
        self._cursor.fetchmany(2)
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            COMMIT_METHOD, self._conn
        )
        # called (at least) 2 times
        self._conn.commit()
        dbapi_database._method_abort_interceptor.reset()
        # Verify the number of calls.
        # We don't know the exact number of calls, as Spanner could also
        # abort the transaction.
        assert method_count_interceptor._counts[COMMIT_METHOD] >= 2
        assert method_count_interceptor._counts[EXECUTE_BATCH_DML_METHOD] >= 4
        assert method_count_interceptor._counts[EXECUTE_STREAMING_SQL_METHOD] >= 10

        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 5

    @pytest.mark.skipif(
        _helpers.USE_EMULATOR,
        reason="Emulator does not support concurrent transactions.",
    )
    def test_retry_aborted_exception(self, shared_instance, dbapi_database):
        """Test that retry fails with RetryAborted error when rows are updated during retry."""

        conn1 = Connection(shared_instance, dbapi_database)
        cursor1 = conn1.cursor()
        cursor1.execute(
            """
            INSERT INTO contacts (contact_id, first_name, last_name, email)
            VALUES (1, 'first-name', 'last-name', 'test.email@domen.ru')
            """
        )
        conn1.commit()
        cursor1.execute("SELECT * FROM contacts")
        cursor1.fetchall()

        conn2 = Connection(shared_instance, dbapi_database)
        cursor2 = conn2.cursor()
        cursor2.execute(
            """
            UPDATE contacts
            SET email = 'test.email_updated@domen.ru'
            WHERE contact_id = 1
            """
        )
        conn2.commit()

        dbapi_database._method_abort_interceptor.set_method_to_abort(
            COMMIT_METHOD, conn1
        )
        with pytest.raises(RetryAborted):
            conn1.commit()
        dbapi_database._method_abort_interceptor.reset()

    def test_execute_sql_abort_retry_multiple_times(self, dbapi_database):
        """Test that when execute sql failed 2 times with Abort exception, then
        the retry succeeds 3rd time."""

        method_count_interceptor = dbapi_database._method_count_interceptor
        method_count_interceptor.reset()
        self._cursor.execute("start batch dml")
        self._insert_row(1)
        self._insert_row(2)
        self._cursor.execute("run batch")
        # aborting method 2 times before succeeding
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            EXECUTE_STREAMING_SQL_METHOD, self._conn, 2
        )
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.fetchmany(2)
        dbapi_database._method_abort_interceptor.reset()
        self._conn.commit()
        # Check that all RPCs except commit should be called at least 3 times
        # We don't know the exact number of attempts, as the transaction could
        # also be aborted by Spanner (and not only the test interceptor).
        assert method_count_interceptor._counts[COMMIT_METHOD] >= 1
        assert method_count_interceptor._counts[EXECUTE_BATCH_DML_METHOD] >= 3
        assert method_count_interceptor._counts[EXECUTE_STREAMING_SQL_METHOD] >= 3

        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 2

    def test_execute_batch_dml_abort_retry(self, dbapi_database):
        """Test that when any execute batch dml failed with Abort exception,
        then the retry succeeds with transaction having insert as well as query
        type of statements along with batch dml statements."""

        method_count_interceptor = dbapi_database._method_count_interceptor
        method_count_interceptor.reset()
        # called 3 times
        self._insert_row(1)
        # called 3 times
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.fetchall()
        self._cursor.execute("start batch dml")
        self._insert_row(2)
        self._insert_row(3)
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            EXECUTE_BATCH_DML_METHOD, self._conn, 2
        )
        # called 3 times
        self._cursor.execute("run batch")
        dbapi_database._method_abort_interceptor.reset()
        self._conn.commit()
        assert method_count_interceptor._counts[COMMIT_METHOD] >= 1
        assert method_count_interceptor._counts[EXECUTE_BATCH_DML_METHOD] >= 3
        assert method_count_interceptor._counts[EXECUTE_STREAMING_SQL_METHOD] >= 6

        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 3

    def test_multiple_aborts_in_transaction(self, dbapi_database):
        """Test that when there are multiple Abort exceptions in a transaction
        on different statements, then the retry succeeds."""

        method_count_interceptor = dbapi_database._method_count_interceptor
        method_count_interceptor.reset()
        # called at least 3 times
        self._insert_row(1)
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            EXECUTE_STREAMING_SQL_METHOD, self._conn
        )
        # called at least 3 times
        self._cursor.execute("SELECT * FROM contacts")
        dbapi_database._method_abort_interceptor.reset()
        self._cursor.fetchall()
        # called at least 2 times
        self._insert_row(2)
        # called at least 2 times
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.fetchone()
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            COMMIT_METHOD, self._conn
        )
        # called at least 2 times
        self._conn.commit()
        dbapi_database._method_abort_interceptor.reset()
        assert method_count_interceptor._counts[COMMIT_METHOD] >= 2
        assert method_count_interceptor._counts[EXECUTE_STREAMING_SQL_METHOD] >= 10

        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 2

    def test_consecutive_aborted_transactions(self, dbapi_database):
        """Test 2 consecutive transactions with Abort exceptions on the same
        connection works."""

        method_count_interceptor = dbapi_database._method_count_interceptor
        method_count_interceptor.reset()
        self._insert_row(1)
        self._insert_row(2)
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.fetchall()
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            COMMIT_METHOD, self._conn
        )
        self._conn.commit()
        dbapi_database._method_abort_interceptor.reset()
        assert method_count_interceptor._counts[COMMIT_METHOD] >= 2
        assert method_count_interceptor._counts[EXECUTE_STREAMING_SQL_METHOD] >= 6

        method_count_interceptor = dbapi_database._method_count_interceptor
        method_count_interceptor.reset()
        self._insert_row(3)
        self._insert_row(4)
        self._cursor.execute("SELECT * FROM contacts")
        self._cursor.fetchall()
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            COMMIT_METHOD, self._conn
        )
        self._conn.commit()
        dbapi_database._method_abort_interceptor.reset()
        assert method_count_interceptor._counts[COMMIT_METHOD] >= 2
        assert method_count_interceptor._counts[EXECUTE_STREAMING_SQL_METHOD] >= 6

        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        assert len(got_rows) == 4

    def test_abort_retry_multiple_cursors(self, dbapi_database):
        """Test that retry works when multiple cursors are involved in the transaction."""

        self._insert_row(1)
        self._insert_row(2)
        self._insert_row(3)
        self._insert_row(4)
        self._conn.commit()

        cur1 = self._conn.cursor()
        cur1.execute("SELECT * FROM contacts WHERE contact_id IN (1, 2)")
        cur2 = self._conn.cursor()
        cur2.execute("SELECT * FROM contacts WHERE contact_id IN (3, 4)")
        row1 = cur1.fetchone()
        row2 = cur2.fetchone()
        row3 = cur1.fetchone()
        row4 = cur2.fetchone()
        dbapi_database._method_abort_interceptor.set_method_to_abort(
            COMMIT_METHOD, self._conn
        )
        self._conn.commit()
        dbapi_database._method_abort_interceptor.reset()

        assert set([row1, row3]) == set(
            [
                (1, "first-name-1", "last-name-1", "test.email@domen.ru"),
                (2, "first-name-2", "last-name-2", "test.email@domen.ru"),
            ]
        )
        assert set([row2, row4]) == set(
            [
                (3, "first-name-3", "last-name-3", "test.email@domen.ru"),
                (4, "first-name-4", "last-name-4", "test.email@domen.ru"),
            ]
        )

    def test_begin_success_post_commit(self):
        """Test beginning a new transaction post commiting an existing transaction
        is possible on a connection, when connection is in autocommit mode."""
        want_row = (2, "first-name", "last-name", "test.email@domen.ru")
        self._conn.autocommit = True
        self._cursor.execute("begin transaction")
        self._cursor.execute(
            """
            INSERT INTO contacts (contact_id, first_name, last_name, email)
            VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
            """
        )
        self._conn.commit()

        self._cursor.execute("begin transaction")
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()
        assert got_rows == [want_row]

    def test_begin_error_before_commit(self):
        """Test beginning a new transaction before commiting an existing transaction is not possible on a connection, when connection is in autocommit mode."""
        self._conn.autocommit = True
        self._cursor.execute("begin transaction")
        self._cursor.execute(
            """
            INSERT INTO contacts (contact_id, first_name, last_name, email)
            VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
            """
        )

        with pytest.raises(OperationalError):
            self._cursor.execute("begin transaction")

    @pytest.mark.parametrize("client_side", [False, True])
    def test_rollback(self, client_side):
        """Test rollbacking a transaction with several statements."""
        want_row = (2, "first-name", "last-name", "test.email@domen.ru")

        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
        """
        )
        self._conn.commit()

        # execute several DMLs with one transaction
        self._cursor.execute(
            """
    UPDATE contacts
    SET first_name = 'updated-first-name'
    WHERE first_name = 'first-name'
    """
        )
        self._cursor.execute(
            """
    UPDATE contacts
    SET email = 'test.email_updated@domen.ru'
    WHERE email = 'test.email@domen.ru'
    """
        )

        if client_side:
            self._cursor.execute("ROLLBACK")
        else:
            self._conn.rollback()

        # read the resulting data from the database
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()
        self._conn.commit()

        assert got_rows == [want_row]

    def test_autocommit_mode_change(self):
        """Test auto committing a transaction on `autocommit` mode change."""
        want_row = (
            2,
            "updated-first-name",
            "last-name",
            "test.email@domen.ru",
        )

        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (2, 'first-name', 'last-name', 'test.email@domen.ru')
        """
        )
        self._cursor.execute(
            """
    UPDATE contacts
    SET first_name = 'updated-first-name'
    WHERE first_name = 'first-name'
    """
        )
        self._conn.autocommit = True

        # read the resulting data from the database
        self._cursor.execute("SELECT * FROM contacts")
        got_rows = self._cursor.fetchall()

        assert got_rows == [want_row]

    @pytest.mark.noautofixt
    def test_rollback_on_connection_closing(self, shared_instance, dbapi_database):
        """
        When closing a connection all the pending transactions
        must be rollbacked. Testing if it's working this way.
        """
        want_row = (1, "first-name", "last-name", "test.email@domen.ru")
        # connect to the test database
        conn = Connection(shared_instance, dbapi_database)
        cursor = conn.cursor()

        cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (1, 'first-name', 'last-name', 'test.email@domen.ru')
        """
        )
        conn.commit()

        cursor.execute(
            """
    UPDATE contacts
    SET first_name = 'updated-first-name'
    WHERE first_name = 'first-name'
    """
        )
        conn.close()

        # connect again, as the previous connection is no-op after closing
        conn = Connection(shared_instance, dbapi_database)
        cursor = conn.cursor()

        # read the resulting data from the database
        cursor.execute("SELECT * FROM contacts")
        got_rows = cursor.fetchall()
        conn.commit()

        assert got_rows == [want_row]

        cursor.close()
        conn.close()

    def test_execute_many(self):
        row_data = [
            (1, "first-name", "last-name", "test.email@example.com"),
            (2, "first-name2", "last-name2", "test.email2@example.com"),
        ]
        self._cursor.executemany(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (%s, %s, %s, %s)
        """,
            row_data,
        )
        self._conn.commit()

        self._cursor.executemany(
            """SELECT * FROM contacts WHERE contact_id = %s""",
            ((1,), (2,)),
        )
        res = self._cursor.fetchall()
        self._conn.commit()

        assert len(res) == len(row_data)
        for found, expected in zip(res, row_data):
            assert found[0] == expected[0]

        # checking that execute() and executemany()
        # results are not mixed together
        self._cursor.execute(
            """
    SELECT * FROM contacts WHERE contact_id = 1
    """,
        )
        res = self._cursor.fetchone()
        self._conn.commit()

        assert res[0] == 1

    @pytest.mark.skipif(_helpers.USE_EMULATOR, reason="Emulator does not support json.")
    def test_autocommit_with_json_data(self):
        """Check that json fields in autocommit mode are inserted and queried."""
        try:
            self._conn.autocommit = True
            self._cursor.execute(
                "INSERT INTO all_types (col_int64, col_json) VALUES (%s, %s)",
                (123, JsonObject({"name": "Jakob", "age": "26"})),
            )
            self._cursor.execute(
                "SELECT col_int64, col_json FROM all_types WHERE col_int64 = 123"
            )
            got_rows = self._cursor.fetchall()
            assert len(got_rows) == 1
            assert got_rows[0][0] == 123
            assert got_rows[0][1] == {"age": "26", "name": "Jakob"}
        finally:
            self._cursor.execute("DELETE FROM all_types WHERE col_int64 = 123")

    @pytest.mark.skipif(_helpers.USE_EMULATOR, reason="Emulator does not support json.")
    def test_json_array(self):
        try:
            self._conn.autocommit = True
            self._cursor.execute(
                "INSERT INTO all_types (col_int64, col_json) VALUES (%s, %s)",
                [1, JsonObject([1, 2, 3])],
            )

            self._cursor.execute(
                "SELECT col_int64, col_json FROM all_types WHERE col_int64 = 1"
            )
            row = self._cursor.fetchone()
            assert isinstance(row[1], JsonObject)
            assert row[1].serialize() == "[1,2,3]"
        finally:
            self._cursor.execute("DELETE FROM all_types WHERE col_int64 = 1")

    def test_ping(self):
        """Check connection validation method."""
        self._conn.validate()

    @pytest.mark.noautofixt
    def test_user_agent(self, shared_instance, dbapi_database):
        """Check that DB API uses an appropriate user agent."""
        conn = connect(
            shared_instance.name,
            dbapi_database.name,
            client_options={"api_endpoint": _helpers.SPANNER_OMNI}
            if _helpers.USE_SPANNER_OMNI
            else None,
            instance_type="omni" if _helpers.USE_SPANNER_OMNI else None,
            use_plain_text=_helpers.USE_PLAIN_TEXT,
            ca_certificate=_helpers.CA_CERTIFICATE,
            client_certificate=_helpers.CLIENT_CERTIFICATE,
            client_key=_helpers.CLIENT_KEY,
            username=_helpers.SPANNER_OMNI_USER,
            password=_helpers.SPANNER_OMNI_PASSWORD,
        )
        assert (
            conn.instance._client._client_info.user_agent
            == "gl-dbapi/" + package_version.__version__
        )
        assert (
            conn.instance._client._client_info.client_library_version
            == package_version.__version__
        )

    def test_read_only(self):
        """
        Check that connection set to `read_only=True` uses
        ReadOnly transactions.
        """

        self._conn.read_only = True
        self._cursor.execute("SELECT * FROM contacts")
        assert self._cursor.fetchall() == []
        self._conn.commit()

    def test_read_only_dml(self):
        """
        Check that connection set to `read_only=True` leads to exception when
        executing dml statements.
        """

        self._conn.read_only = True
        with pytest.raises(ProgrammingError):
            self._cursor.execute(
                """
    UPDATE contacts
    SET first_name = 'updated-first-name'
    WHERE first_name = 'first-name'
    """
            )

    def test_staleness(self):
        """Check the DB API `staleness` option."""

        before_insert = datetime.datetime.utcnow().replace(tzinfo=UTC)
        time.sleep(0.25)

        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (1, 'first-name', 'last-name', 'test.email@example.com')
        """
        )
        self._conn.commit()

        self._conn.read_only = True
        self._conn.staleness = {"read_timestamp": before_insert}
        self._cursor.execute("SELECT * FROM contacts")
        self._conn.commit()
        assert len(self._cursor.fetchall()) == 0

        self._conn.staleness = None
        self._cursor.execute("SELECT * FROM contacts")
        self._conn.commit()
        assert len(self._cursor.fetchall()) == 1

    @pytest.mark.parametrize("autocommit", [False, True])
    def test_rowcount(self, autocommit):
        self._conn.autocommit = autocommit

        # executemany sets rowcount to the total modified rows
        rows = [(i, f"Singer {i}") for i in range(100)]
        self._cursor.executemany(
            "INSERT INTO contacts (contact_id, first_name) VALUES (%s, %s)",
            rows[:98],
        )
        assert self._cursor.rowcount == 98

        # execute with INSERT
        self._cursor.execute(
            "INSERT INTO contacts (contact_id, first_name) VALUES (%s, %s), (%s, %s)",
            [x for row in rows[98:] for x in row],
        )
        assert self._cursor.rowcount == 2

        # execute with UPDATE
        self._cursor.execute(
            "UPDATE contacts SET first_name = 'Cher' WHERE contact_id < 25"
        )
        assert self._cursor.rowcount == 25

        # execute with SELECT
        self._cursor.execute("SELECT first_name FROM contacts WHERE contact_id < 75")
        assert len(self._cursor.fetchall()) == 75
        # rowcount is not available for SELECT
        assert self._cursor.rowcount == -1

        # execute with DELETE
        self._cursor.execute("DELETE FROM contacts WHERE true")
        assert self._cursor.rowcount == 100

        # execute with UPDATE matching 0 rows
        self._cursor.execute(
            "UPDATE contacts SET first_name = 'Cher' WHERE contact_id < 25"
        )
        if not autocommit:
            self._conn.commit()

    @pytest.mark.parametrize("autocommit", [False, True])
    @pytest.mark.skipif(
        _helpers.USE_EMULATOR, reason="Emulator does not support DML Returning."
    )
    def test_dml_returning_insert(self, autocommit):
        self._conn.autocommit = autocommit
        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (1, 'first-name', 'last-name', 'test.email@example.com')
    THEN RETURN contact_id, first_name
        """
        )
        assert self._cursor.fetchone() == (1, "first-name")
        assert self._cursor.rowcount == 1
        self._conn.commit()

    @pytest.mark.parametrize("autocommit", [False, True])
    @pytest.mark.skipif(
        _helpers.USE_EMULATOR, reason="Emulator does not support DML Returning."
    )
    def test_dml_returning_update(self, autocommit):
        self._conn.autocommit = autocommit
        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (1, 'first-name', 'last-name', 'test.email@example.com')
        """
        )
        assert self._cursor.rowcount == 1
        self._cursor.execute(
            """
    UPDATE contacts SET first_name = 'new-name' WHERE contact_id = 1
    THEN RETURN contact_id, first_name
        """
        )
        assert self._cursor.fetchone() == (1, "new-name")
        assert self._cursor.rowcount == 1
        self._conn.commit()

    @pytest.mark.parametrize("autocommit", [False, True])
    @pytest.mark.skipif(
        _helpers.USE_EMULATOR, reason="Emulator does not support DML Returning."
    )
    def test_dml_returning_delete(self, autocommit):
        self._conn.autocommit = autocommit
        self._cursor.execute(
            """
    INSERT INTO contacts (contact_id, first_name, last_name, email)
    VALUES (1, 'first-name', 'last-name', 'test.email@example.com')
        """
        )
        assert self._cursor.rowcount == 1
        self._cursor.execute(
            """
    DELETE FROM contacts WHERE contact_id = 1
    THEN RETURN contact_id, first_name
        """
        )
        assert self._cursor.fetchone() == (1, "first-name")
        assert self._cursor.rowcount == 1
        self._conn.commit()

    @pytest.mark.parametrize("include_views", [True, False])
    def test_list_tables(self, include_views):
        tables = self._cursor.list_tables(include_views=include_views)
        table_names = set(table[0] for table in tables)

        assert "contacts" in table_names

        if include_views:
            assert "contacts_emails" in table_names
        else:  # if not include_views:
            assert "contacts_emails" not in table_names

    def test_invalid_statement_error(self):
        with pytest.raises(ProgrammingError):
            self._cursor.execute("-- comment only")

    def test_insert_all_types(self):
        """Test inserting all supported data types"""

        self._conn.autocommit = True
        self._cursor.execute(
            """
    INSERT INTO all_types (id, col_bool, col_bytes, col_date, col_float32, col_float64,
                           col_int64, col_json, col_numeric, col_string, col_timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            (
                1,
                True,
                base64.b64encode(b"test-bytes"),
                datetime.date(2024, 12, 3),
                3.14,
                3.14,
                123,
                JsonObject({"key": "value"}),
                decimal.Decimal("3.14"),
                "test-string",
                datetime.datetime(2024, 12, 3, 17, 30, 14),
            ),
        )
        assert self._cursor.rowcount == 1
