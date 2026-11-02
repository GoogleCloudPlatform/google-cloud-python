# Copyright 2024 Google LLC All rights reserved.
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
from google.api_core import exceptions
from test_utils import retry

from google.cloud.spanner_v1 import (
    BeginTransactionRequest,
    CommitRequest,
    ExecuteBatchDmlRequest,
    ExecuteSqlRequest,
    TypeCode,
)
from google.cloud.spanner_v1.database_sessions_manager import TransactionType
from google.cloud.spanner_v1.testing.mock_spanner import SpannerServicer
from google.cloud.spanner_v1.transaction import Transaction
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    aborted_status,
    add_error,
    add_single_result,
    add_update_count,
)


def _is_aborted_error(exc):
    """Check if exception is Aborted."""
    return isinstance(exc, exceptions.Aborted)


# Retry on Aborted exceptions
retry_maybe_aborted_txn = retry.RetryErrors(
    exceptions.Aborted,
    error_predicate=_is_aborted_error,
    max_tries=5,
    delay=0,
    backoff=1,
)


class TestAbortedTransaction(MockServerTestBase):
    def test_run_in_transaction_commit_aborted(self):
        # Add an Aborted error for the Commit method on the mock server.
        add_error(SpannerServicer.Commit.__name__, aborted_status())
        # Run a transaction. The Commit method will return Aborted the first
        # time that the transaction tries to commit. It will then be retried
        # and succeed.
        self.database.run_in_transaction(_insert_mutations)
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [
                BeginTransactionRequest,
                CommitRequest,
                BeginTransactionRequest,
                CommitRequest,
            ],
            TransactionType.READ_WRITE,
        )

    def test_run_in_transaction_update_aborted(self):
        add_update_count("update my_table set my_col=1 where id=2", 1)
        add_error(SpannerServicer.ExecuteSql.__name__, aborted_status())
        self.database.run_in_transaction(_execute_update)
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest, ExecuteSqlRequest, CommitRequest],
            TransactionType.READ_WRITE,
        )

    def test_run_in_transaction_query_aborted(self):
        add_single_result(
            "select value from my_table where id=1",
            "value",
            TypeCode.STRING,
            "my-value",
        )
        add_error(SpannerServicer.ExecuteStreamingSql.__name__, aborted_status())
        self.database.run_in_transaction(_execute_query)
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest, ExecuteSqlRequest, CommitRequest],
            TransactionType.READ_WRITE,
        )

    def test_run_in_transaction_batch_dml_aborted(self):
        add_update_count("update my_table set my_col=1 where id=1", 1)
        add_update_count("update my_table set my_col=1 where id=2", 1)
        add_error(SpannerServicer.ExecuteBatchDml.__name__, aborted_status())
        self.database.run_in_transaction(_execute_batch_dml)
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteBatchDmlRequest, ExecuteBatchDmlRequest, CommitRequest],
            TransactionType.READ_WRITE,
        )

    def test_batch_commit_aborted(self):
        # Add an Aborted error for the Commit method on the mock server.
        add_error(SpannerServicer.Commit.__name__, aborted_status())
        with self.database.batch() as batch:
            batch.insert(
                table="Singers",
                columns=("SingerId", "FirstName", "LastName"),
                values=[
                    (1, "Marc", "Richards"),
                    (2, "Catalina", "Smith"),
                    (3, "Alice", "Trentor"),
                    (4, "Lea", "Martin"),
                    (5, "David", "Lomond"),
                ],
            )
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [CommitRequest, CommitRequest],
            TransactionType.READ_WRITE,
        )

    def test_retry_helper(self):
        # Add an Aborted error for the Commit method on the mock server.
        # The error is popped after the first use, so the retry will succeed.
        add_error(SpannerServicer.Commit.__name__, aborted_status())

        @retry_maybe_aborted_txn
        def do_commit():
            session = self.database.session()
            session.create()
            transaction = session.transaction()
            transaction.begin()
            transaction.insert("my_table", ["col1, col2"], [{"col1": 1, "col2": "One"}])
            transaction.commit()

        do_commit()


def _insert_mutations(transaction: Transaction):
    transaction.insert("my_table", ["col1", "col2"], ["value1", "value2"])


def _execute_update(transaction: Transaction):
    transaction.execute_update("update my_table set my_col=1 where id=2")


def _execute_query(transaction: Transaction):
    rows = transaction.execute_sql("select value from my_table where id=1")
    for _ in rows:
        pass


def _execute_batch_dml(transaction: Transaction):
    transaction.batch_update(
        [
            "update my_table set my_col=1 where id=1",
            "update my_table set my_col=1 where id=2",
        ]
    )
