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

"""Tests that the DBAPI uses inline begin for read-write transactions.

After removing the explicit ``Transaction.begin()`` call from
``Connection.transaction_checkout()``, the DBAPI should piggyback
``BeginTransaction`` on the first ``ExecuteSql`` / ``ExecuteUpdate`` request
via ``TransactionSelector(begin=...)``, eliminating one gRPC round-trip
per transaction.

Read-only transactions are unaffected — they still use an explicit
``BeginTransaction`` RPC via ``snapshot_checkout()``.
"""

from google.rpc import code_pb2, status_pb2

from google.cloud.spanner_dbapi import Connection
from google.cloud.spanner_dbapi.exceptions import OperationalError, ProgrammingError
from google.cloud.spanner_v1 import (
    BeginTransactionRequest,
    CommitRequest,
    ExecuteBatchDmlRequest,
    ExecuteSqlRequest,
    RollbackRequest,
    TypeCode,
)
from google.cloud.spanner_v1.database_sessions_manager import TransactionType
from google.cloud.spanner_v1.testing.mock_spanner import SpannerServicer
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    aborted_status,
    add_error,
    add_single_result,
    add_update_count,
    invalid_argument_status,
)


class TestDbapiInlineBegin(MockServerTestBase):
    def setUp(self):
        super().setUp()
        add_single_result(
            "select name from singers", "name", TypeCode.STRING, [("Some Singer",)]
        )
        add_update_count("insert into singers (id, name) values (1, 'Some Singer')", 1)

    def test_read_write_inline_begin(self):
        """Comprehensive check for a single-statement read-write transaction.

        Verifies:
        - No BeginTransactionRequest is sent
        - The ExecuteSqlRequest uses TransactionSelector(begin=ReadWrite(...))
        - The request sequence is [ExecuteSqlRequest, CommitRequest]
        - The query returns correct data
        """
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
        connection.commit()

        self.assertEqual(
            [("Some Singer",)],
            rows,
            "Query should return the mocked result set",
        )

        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            0,
            len(begin_requests),
            "Read-write DBAPI transactions should not send "
            "a separate BeginTransactionRequest",
        )

        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertGreaterEqual(len(sql_requests), 1)
        first_sql = sql_requests[0]
        self.assertTrue(
            first_sql.transaction.begin.read_write
            == first_sql.transaction.begin.read_write,
        )
        self.assertIn(
            "read_write",
            first_sql.transaction.begin,
            "First ExecuteSqlRequest should use inline begin with "
            "TransactionSelector(begin=ReadWrite(...))",
        )

        self.assert_requests_sequence(
            self.spanner_service.requests,
            [ExecuteSqlRequest, CommitRequest],
            TransactionType.READ_WRITE,
        )

    def test_read_write_dml_request_sequence(self):
        """DML write via DBAPI: ExecuteSql + Commit (no BeginTransaction)."""
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")
        connection.commit()

        self.assert_requests_sequence(
            self.spanner_service.requests,
            [ExecuteSqlRequest, CommitRequest],
            TransactionType.READ_WRITE,
        )

    def test_read_then_write_full_lifecycle(self):
        """Read + write in same transaction: verifies the complete inline begin lifecycle.

        Checks:
        - First ExecuteSqlRequest uses TransactionSelector(begin=ReadWrite(...))
        - Second ExecuteSqlRequest uses TransactionSelector(id=<txn_id>)
        - CommitRequest uses the same transaction_id as the second statement
        - Query returns correct data
        - Request sequence is [ExecuteSql, ExecuteSql, Commit]
        """
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")
        connection.commit()

        self.assertEqual(
            [("Some Singer",)],
            rows,
            "Query should return the mocked result set",
        )

        self.assert_requests_sequence(
            self.spanner_service.requests,
            [ExecuteSqlRequest, ExecuteSqlRequest, CommitRequest],
            TransactionType.READ_WRITE,
        )

        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(2, len(sql_requests))

        first = sql_requests[0]
        self.assertIn(
            "read_write",
            first.transaction.begin,
            "First statement should use inline begin",
        )

        second = sql_requests[1]
        self.assertNotEqual(
            b"",
            second.transaction.id,
            "Second statement should use TransactionSelector(id=...) "
            "with the transaction_id returned from inline begin",
        )

        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(1, len(commit_requests))
        self.assertEqual(
            second.transaction.id,
            commit_requests[0].transaction_id,
            "CommitRequest must reference the same transaction_id "
            "that the second ExecuteSqlRequest used",
        )

    def test_read_only_still_uses_explicit_begin(self):
        """Read-only transactions should still use explicit BeginTransaction."""
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        connection.read_only = True
        with connection.cursor() as cursor:
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
        connection.commit()

        self.assertEqual(
            [("Some Singer",)],
            rows,
            "Read-only query should return the mocked result set",
        )

        self.assert_requests_sequence(
            self.spanner_service.requests,
            [BeginTransactionRequest, ExecuteSqlRequest],
            TransactionType.READ_ONLY,
        )

    def test_rollback_after_inline_begin(self):
        """Rollback after DML sends RollbackRequest with the correct transaction_id."""
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")
        connection.rollback()

        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            0,
            len(begin_requests),
            "Rollback path should not use BeginTransactionRequest",
        )

        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(1, len(sql_requests))

        rollback_requests = [
            r for r in self.spanner_service.requests if isinstance(r, RollbackRequest)
        ]
        self.assertEqual(
            1,
            len(rollback_requests),
            "A RollbackRequest should be sent after DML + rollback",
        )

        txn_id_from_inline_begin = sql_requests[0].transaction.begin
        self.assertIn(
            "read_write",
            txn_id_from_inline_begin,
            "DML should have used inline begin",
        )

        self.assertNotEqual(
            b"",
            rollback_requests[0].transaction_id,
            "RollbackRequest must carry the transaction_id obtained via inline begin",
        )

    def test_inline_begin_with_abort_retry(self):
        """Transaction retry after abort should work with inline begin.

        The DBAPI replays recorded statements on abort. With inline begin,
        the retried ExecuteSqlRequest should again use inline begin.
        """
        add_error(SpannerServicer.Commit.__name__, aborted_status())

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")
        connection.commit()

        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            0,
            len(begin_requests),
            "Retried transaction should also use inline begin, "
            "not explicit BeginTransactionRequest",
        )

        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(
            2, len(sql_requests), "Expected 2 ExecuteSqlRequests: original + retry"
        )
        for i, req in enumerate(sql_requests):
            self.assertIn(
                "read_write",
                req.transaction.begin,
                f"ExecuteSqlRequest[{i}] should use inline begin",
            )

        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            2,
            len(commit_requests),
            "Expected 2 CommitRequests: the aborted original + the successful retry",
        )
        for i, cr in enumerate(commit_requests):
            self.assertNotEqual(
                b"",
                cr.transaction_id,
                f"CommitRequest[{i}] must carry a transaction_id from inline begin",
            )

    def test_dml_fails_retry_succeeds_continues_transaction(self):
        """If the first statement (inline begin) fails with a non-abort error,
        it does not return a transaction ID. The driver should immediately
        execute an explicit BeginTransaction RPC and retry the first statement.
        The second statement should then use the transaction ID returned by the
        explicit BeginTransaction RPC.
        """
        add_error(
            SpannerServicer.ExecuteStreamingSql.__name__, invalid_argument_status()
        )
        add_update_count(
            "insert into singers (id, name) values (2, 'Invalid Singer')", 0
        )
        add_update_count("insert into singers (id, name) values (1, 'Some Singer')", 0)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            # First statement attempt 1 fails (inline begin), attempt 2 (retry) succeeds.
            # We no longer expect an exception since retry succeeds.
            cursor.execute(
                "insert into singers (id, name) values (2, 'Invalid Singer')"
            )

            # Application continues transaction with a second statement.
            # This should still be part of the same transaction (or rather,
            # Spanner DBAPI must use the valid transaction ID acquired during
            # the retry of the first statement).
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")

        connection.commit()

        # Check that we eventually sent a CommitRequest
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            1,
            len(commit_requests),
            "A CommitRequest should be sent for the transaction",
        )

        # Check ExecuteSqlRequests
        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(
            3,
            len(sql_requests),
            "Expected three ExecuteSqlRequests (first failed, first retry succeeded, second succeeded)",
        )

        # Verify transaction states
        first = sql_requests[0]
        self.assertIn(
            "read_write",
            first.transaction.begin,
            "First failed statement should have used inline begin",
        )

        second = sql_requests[1]
        self.assertEqual(
            first.sql,
            second.sql,
            "Second statement should be a retry of the first statement",
        )
        self.assertNotEqual(
            b"",
            second.transaction.id,
            "Second statement (retry) should use TransactionSelector(id=...) from an explicit BeginTransaction",
        )

        third = sql_requests[2]
        self.assertNotEqual(
            first.sql, third.sql, "Third statement should be the new statement"
        )
        self.assertEqual(
            second.transaction.id,
            third.transaction.id,
            "Third statement should use the same explicit transaction as the retry",
        )
        # Verify that a BeginTransactionRequest was sent.
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            1, len(begin_requests), "Expected exactly 1 BeginTransactionRequest"
        )

    def test_query_fails_retry_succeeds_continues_transaction(self):
        """If the first statement (inline begin) is a query and it fails with a non-abort error,
        it does not return a transaction ID. The driver should immediately
        execute an explicit BeginTransaction RPC and retry the query.
        The second statement should then use the transaction ID returned by the
        explicit BeginTransaction RPC.
        """
        add_error(
            SpannerServicer.ExecuteStreamingSql.__name__, invalid_argument_status()
        )
        add_single_result(
            "select name from singers", "name", TypeCode.STRING, [("Some Singer",)]
        )
        add_update_count("insert into singers (id, name) values (1, 'Some Singer')", 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            # First statement attempt 1 fails (inline begin), attempt 2 (retry) succeeds.
            # We no longer expect an exception since retry succeeds.
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
            self.assertEqual([("Some Singer",)], rows)

            # Application continues transaction
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")

        connection.commit()

        # Check that we eventually sent a CommitRequest
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            1,
            len(commit_requests),
            "A CommitRequest should be sent for the transaction",
        )

        # Verify that a BeginTransactionRequest was sent.
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            1, len(begin_requests), "Expected exactly 1 BeginTransactionRequest"
        )

        # Check ExecuteStreamingSqlRequests
        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(3, len(sql_requests), "Expected exactly 3 ExecuteSqlRequests")

    def test_executemany_fails_retry_succeeds_continues_transaction(self):
        """If the first statement (inline begin) is an executemany (Batch DML) and it fails with a non-abort error,
        it does not return a transaction ID. The driver should immediately
        execute an explicit BeginTransaction RPC and retry the executemany.
        The second statement should then use the transaction ID returned by the
        explicit BeginTransaction RPC.
        """
        add_error(SpannerServicer.ExecuteBatchDml.__name__, invalid_argument_status())
        add_update_count("insert into singers (id, name) values (@a0, @a1)", 1)
        add_update_count("insert into singers (id, name) values (3, 'Third Singer')", 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            cursor.executemany(
                "insert into singers (id, name) values (%s, %s)",
                [(1, "Some Singer"), (2, "Another Singer")],
            )

            cursor.execute("insert into singers (id, name) values (3, 'Third Singer')")

        connection.commit()

        # Check that we eventually sent a CommitRequest
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            1,
            len(commit_requests),
            "A CommitRequest should be sent for the transaction",
        )

        # Verify that a BeginTransactionRequest was sent.
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            1, len(begin_requests), "Expected exactly 1 BeginTransactionRequest"
        )

        # Check ExecuteBatchDmlRequests
        batch_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, ExecuteBatchDmlRequest)
        ]
        self.assertEqual(
            2, len(batch_requests), "Expected exactly 2 ExecuteBatchDmlRequests"
        )

        # Check ExecuteSqlRequests (the second statement)
        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(1, len(sql_requests), "Expected exactly 1 ExecuteSqlRequests")

    def test_executemany_fails_with_status_continues_transaction(self):
        """Batch DML fails by returning a non-OK status in the response,
        but the response still includes a transaction ID from inline begin.
        No explicit BeginTransaction is necessary. The second statement
        should use the transaction ID returned by the ExecuteBatchDml response.
        """
        self.spanner_service.add_batch_dml_response_status(
            status_pb2.Status(
                code=code_pb2.INVALID_ARGUMENT, message="Invalid argument."
            )
        )
        add_update_count("insert into singers (id, name) values (@a0, @a1)", 1)
        add_update_count("insert into singers (id, name) values (3, 'Third Singer')", 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            try:
                cursor.executemany(
                    "insert into singers (id, name) values (%s, %s)",
                    [(1, "Some Singer"), (2, "Another Singer")],
                )
                self.fail("Expected OperationalError")
            except OperationalError:
                pass

            cursor.execute("insert into singers (id, name) values (3, 'Third Singer')")

        connection.commit()

        # Check that we eventually sent a CommitRequest
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            1,
            len(commit_requests),
            "A CommitRequest should be sent for the transaction",
        )

        # Verify that NO BeginTransactionRequest was sent.
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            0, len(begin_requests), "Expected exactly 0 BeginTransactionRequests"
        )

        # Check ExecuteBatchDmlRequests
        batch_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, ExecuteBatchDmlRequest)
        ]
        self.assertEqual(
            1, len(batch_requests), "Expected exactly 1 ExecuteBatchDmlRequest"
        )

        # Check ExecuteSqlRequests (the second statement)
        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(1, len(sql_requests), "Expected exactly 1 ExecuteSqlRequest")

        batch_req = batch_requests[0]
        self.assertIn(
            "read_write",
            batch_req.transaction.begin,
            "First statement should have used inline begin",
        )

        sql_req = sql_requests[0]
        self.assertNotEqual(
            b"",
            sql_req.transaction.id,
            "Second statement should use TransactionSelector(id=...) returned from ExecuteBatchDml inline begin",
        )
        self.assertEqual(
            sql_req.transaction.id,
            commit_requests[0].transaction_id,
            "Commit request should use the same explicit transaction as the second statement",
        )

    def test_executemany_fails_with_status_no_transaction_id_retries_and_continues_transaction(
        self,
    ):
        """Batch DML fails by returning a non-OK status in the response,
        and without a transaction ID.
        The driver should immediately execute an explicit BeginTransaction RPC
        and retry the ExecuteBatchDml.
        The second statement should use the transaction ID returned by the explicit BeginTransaction.
        """
        self.spanner_service.add_batch_dml_response_status(
            status_pb2.Status(
                code=code_pb2.INVALID_ARGUMENT, message="Invalid argument."
            ),
            include_transaction_id=False,
        )
        add_update_count("insert into singers (id, name) values (@a0, @a1)", 1)
        add_update_count("insert into singers (id, name) values (3, 'Third Singer')", 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            # First attempt fails with INVALID_ARGUMENT but NO transaction ID.
            # Driver catches this, starts explicit transaction, and retries.
            # Retry succeeds. No exception is raised.
            cursor.executemany(
                "insert into singers (id, name) values (%s, %s)",
                [(1, "Some Singer"), (2, "Another Singer")],
            )

            cursor.execute("insert into singers (id, name) values (3, 'Third Singer')")

        connection.commit()

        # Check requests
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(1, len(commit_requests))

        # We expect an explicit BeginTransactionRequest because the first response had no transaction_id
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(1, len(begin_requests))

        batch_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, ExecuteBatchDmlRequest)
        ]
        self.assertEqual(2, len(batch_requests))

        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(1, len(sql_requests))

        first_batch = batch_requests[0]
        self.assertIn("read_write", first_batch.transaction.begin)

        second_batch = batch_requests[1]
        self.assertNotEqual(b"", second_batch.transaction.id)

        sql_req = sql_requests[0]
        self.assertEqual(second_batch.transaction.id, sql_req.transaction.id)
        self.assertEqual(second_batch.transaction.id, commit_requests[0].transaction_id)

    def test_executemany_fails_retry_fails_continues_transaction(self):
        """If the first statement (inline begin) is an executemany (Batch DML) and it fails with a non-abort error,
        it does not return a transaction ID. The driver should immediately
        execute an explicit BeginTransaction RPC and retry the executemany.
        If the immediate retry ALSO fails, the exception is propagated to the user.
        If the application catches this exception and continues, the second statement
        should still use the transaction ID returned by the explicit BeginTransaction.
        """
        add_error(SpannerServicer.ExecuteBatchDml.__name__, invalid_argument_status())
        add_error(SpannerServicer.ExecuteBatchDml.__name__, invalid_argument_status())
        add_update_count("insert into singers (id, name) values (3, 'Third Singer')", 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            try:
                cursor.executemany(
                    "insert into singers (id, name) values (%s, %s)",
                    [(1, "Some Singer"), (2, "Another Singer")],
                )
                self.fail("Expected InvalidArgument")
            except ProgrammingError:
                # Expect error (e.g., INVALID_ARGUMENT because of invalid syntax)
                pass

            cursor.execute("insert into singers (id, name) values (3, 'Third Singer')")

        connection.commit()

        # Check that we eventually sent a CommitRequest
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            1,
            len(commit_requests),
            "A CommitRequest should be sent for the transaction",
        )

        # Verify that a BeginTransactionRequest was sent.
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            1, len(begin_requests), "Expected exactly 1 BeginTransactionRequest"
        )

        # Check ExecuteBatchDmlRequests
        batch_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, ExecuteBatchDmlRequest)
        ]
        self.assertEqual(
            2, len(batch_requests), "Expected exactly 2 ExecuteBatchDmlRequests"
        )

        first_batch = batch_requests[0]
        self.assertIn(
            "read_write",
            first_batch.transaction.begin,
            "First failed statement should have used inline begin",
        )

        second_batch = batch_requests[1]
        self.assertEqual(
            first_batch.statements,
            second_batch.statements,
            "Second statement should be a retry of the first statement",
        )
        self.assertNotEqual(
            b"",
            second_batch.transaction.id,
            "Second statement (retry) should use TransactionSelector(id=...) from an explicit BeginTransaction",
        )

        # Check ExecuteSqlRequests (the second statement)
        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(1, len(sql_requests), "Expected exactly 1 ExecuteSqlRequests")

        sql_req = sql_requests[0]
        self.assertEqual(
            second_batch.transaction.id,
            sql_req.transaction.id,
            "Third statement should use the same explicit transaction as the retry",
        )

    def test_dml_fails_retry_fails_continues_transaction(self):
        """If the first statement (inline begin) fails with a non-abort error,
        it does not return a transaction ID. The driver should immediately
        execute an explicit BeginTransaction RPC and retry the first statement.
        If the immediate retry ALSO fails, the exception is propagated to the user.
        If the application catches this exception and continues, the second statement
        should still use the transaction ID returned by the explicit BeginTransaction.
        """
        add_error(
            SpannerServicer.ExecuteStreamingSql.__name__, invalid_argument_status()
        )
        add_error(
            SpannerServicer.ExecuteStreamingSql.__name__, invalid_argument_status()
        )
        add_update_count("insert into singers (id, name) values (1, 'Some Singer')", 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "insert into singers (id, name) values (2, 'Invalid Singer')"
                )
                self.fail("Expected ProgrammingError")
            except ProgrammingError:
                # Expect error (e.g., INVALID_ARGUMENT because of invalid syntax)
                pass

            # Application catches the error from the failed retry and continues.
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")

        connection.commit()

        # Check that we eventually sent a CommitRequest
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            1,
            len(commit_requests),
            "A CommitRequest should be sent for the transaction",
        )

        # Verify that a BeginTransactionRequest was sent.
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            1, len(begin_requests), "Expected exactly 1 BeginTransactionRequest"
        )

        # Check ExecuteSqlRequests
        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(3, len(sql_requests), "Expected exactly 3 ExecuteSqlRequests")

    def test_query_fails_retry_fails_continues_transaction(self):
        """If the first statement (inline begin) is a query and it fails with a non-abort error,
        it does not return a transaction ID. The driver should immediately
        execute an explicit BeginTransaction RPC and retry the query.
        If the immediate retry ALSO fails, the exception is propagated to the user.
        If the application catches this exception and continues, the second statement
        should still use the transaction ID returned by the explicit BeginTransaction.
        """
        add_error(
            SpannerServicer.ExecuteStreamingSql.__name__, invalid_argument_status()
        )
        add_error(
            SpannerServicer.ExecuteStreamingSql.__name__, invalid_argument_status()
        )
        add_update_count("insert into singers (id, name) values (1, 'Some Singer')", 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        with connection.cursor() as cursor:
            try:
                cursor.execute("select name from invalid_singers")
                cursor.fetchall()
                self.fail("Expected ProgrammingError")
            except ProgrammingError:
                # Expect error (e.g., INVALID_ARGUMENT because of invalid syntax)
                pass

            # Application catches the error from the failed retry and continues.
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")

        connection.commit()

        # Check that we eventually sent a CommitRequest
        commit_requests = [
            r for r in self.spanner_service.requests if isinstance(r, CommitRequest)
        ]
        self.assertEqual(
            1,
            len(commit_requests),
            "A CommitRequest should be sent for the transaction",
        )

        # Verify that a BeginTransactionRequest was sent.
        begin_requests = [
            r
            for r in self.spanner_service.requests
            if isinstance(r, BeginTransactionRequest)
        ]
        self.assertEqual(
            1, len(begin_requests), "Expected exactly 1 BeginTransactionRequest"
        )

        # Check ExecuteSqlRequests
        sql_requests = [
            r for r in self.spanner_service.requests if isinstance(r, ExecuteSqlRequest)
        ]
        self.assertEqual(3, len(sql_requests), "Expected exactly 3 ExecuteSqlRequests")

        first = sql_requests[0]
        self.assertIn(
            "read_write",
            first.transaction.begin,
            "First failed statement should have used inline begin",
        )

        second = sql_requests[1]
        self.assertEqual(
            first.sql,
            second.sql,
            "Second statement should be a retry of the first statement",
        )
        self.assertNotEqual(
            b"",
            second.transaction.id,
            "Second statement (retry) should use TransactionSelector(id=...) from an explicit BeginTransaction",
        )

        third = sql_requests[2]
        self.assertNotEqual(
            first.sql, third.sql, "Third statement should be the new statement"
        )
        self.assertEqual(
            second.transaction.id,
            third.transaction.id,
            "Third statement should use the same explicit transaction as the retry",
        )
