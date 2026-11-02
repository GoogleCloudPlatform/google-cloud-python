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

from google.cloud.spanner_admin_database_v1.types import spanner_database_admin
from google.cloud.spanner_dbapi import Connection
from google.cloud.spanner_dbapi.parsed_statement import AutocommitDmlMode
from google.cloud.spanner_v1 import (
    BeginTransactionRequest,
    ExecuteBatchDmlRequest,
    ExecuteSqlRequest,
    TransactionOptions,
    TypeCode,
)
from google.cloud.spanner_v1.database_sessions_manager import TransactionType
from google.cloud.spanner_v1.testing.mock_spanner import SpannerServicer
from google.cloud.spanner_v1.transaction import Transaction
from tests._helpers import is_multiplexed_enabled
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    _make_partial_result_sets,
    add_error,
    add_execute_streaming_sql_results,
    add_select1_result,
    add_single_result,
    add_update_count,
    unavailable_status,
)


class TestBasics(MockServerTestBase):
    def test_select1(self):
        add_select1_result()
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql("select 1")
            result_list = []
            for row in results:
                result_list.append(row)
                self.assertEqual(1, row[0])
            self.assertEqual(1, len(result_list))
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest],
            TransactionType.READ_ONLY,
        )

    def test_create_table(self):
        database_admin_api = self.client.database_admin_api
        request = spanner_database_admin.UpdateDatabaseDdlRequest(
            dict(
                database=database_admin_api.database_path(
                    "test-project", "test-instance", "test-database"
                ),
                statements=[
                    "CREATE TABLE Test (Id INT64, Value STRING(MAX)) PRIMARY KEY (Id)",
                ],
            )
        )
        operation = database_admin_api.update_database_ddl(request)
        operation.result(1)

    # TODO: Move this to a separate class once the mock server test setup has
    #       been re-factored to use a base class for the boiler plate code.
    def test_dbapi_partitioned_dml(self):
        sql = "UPDATE singers SET foo='bar' WHERE active = true"
        add_update_count(sql, 100, AutocommitDmlMode.PARTITIONED_NON_ATOMIC)
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        connection.set_autocommit_dml_mode(AutocommitDmlMode.PARTITIONED_NON_ATOMIC)
        with connection.cursor() as cursor:
            # Note: SQLAlchemy uses [] as the list of parameters for statements
            # with no parameters.
            cursor.execute(sql, [])
            self.assertEqual(100, cursor.rowcount)
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [BeginTransactionRequest, ExecuteSqlRequest],
            TransactionType.PARTITIONED,
            allow_multiple_batch_create=True,
        )
        # Find the first BeginTransactionRequest after session creation
        idx = 0
        from google.cloud.spanner_v1 import (
            BatchCreateSessionsRequest,
            CreateSessionRequest,
        )

        while idx < len(requests) and isinstance(
            requests[idx], BatchCreateSessionsRequest
        ):
            idx += 1
        if (
            is_multiplexed_enabled(TransactionType.PARTITIONED)
            and idx < len(requests)
            and isinstance(requests[idx], CreateSessionRequest)
        ):
            idx += 1
        begin_request: BeginTransactionRequest = requests[idx]
        self.assertEqual(
            TransactionOptions(dict(partitioned_dml={})), begin_request.options
        )

    def test_batch_create_sessions_unavailable(self):
        add_select1_result()
        add_error(SpannerServicer.BatchCreateSessions.__name__, unavailable_status())
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql("select 1")
            result_list = []
            for row in results:
                result_list.append(row)
                self.assertEqual(1, row[0])
            self.assertEqual(1, len(result_list))
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest],
            TransactionType.READ_ONLY,
            allow_multiple_batch_create=True,
        )

    def test_execute_streaming_sql_unavailable(self):
        add_select1_result()
        # Add an UNAVAILABLE error that is returned the first time the
        # ExecuteStreamingSql RPC is called.
        add_error(SpannerServicer.ExecuteStreamingSql.__name__, unavailable_status())
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql("select 1")
            result_list = []
            for row in results:
                result_list.append(row)
                self.assertEqual(1, row[0])
            self.assertEqual(1, len(result_list))
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest, ExecuteSqlRequest],
            TransactionType.READ_ONLY,
        )

    def test_last_statement_update(self):
        sql = "update my_table set my_col=1 where id=2"
        add_update_count(sql, 1)
        self.database.run_in_transaction(
            lambda transaction: transaction.execute_update(sql, last_statement=True)
        )
        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests), msg=requests)
        self.assertTrue(requests[0].last_statement, requests[0])

    def test_last_statement_batch_update(self):
        sql = "update my_table set my_col=1 where id=2"
        add_update_count(sql, 1)
        self.database.run_in_transaction(
            lambda transaction: transaction.batch_update(
                [sql, sql], last_statement=True
            )
        )
        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteBatchDmlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests), msg=requests)
        self.assertTrue(requests[0].last_statements, requests[0])

    def test_last_statement_query(self):
        sql = "insert into my_table (value) values ('One') then return id"
        add_single_result(sql, "c", TypeCode.INT64, [("1",)])
        self.database.run_in_transaction(
            lambda transaction: _execute_query(transaction, sql)
        )
        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests), msg=requests)
        self.assertTrue(requests[0].last_statement, requests[0])

    def test_execute_streaming_sql_last_field(self):
        partial_result_sets = _make_partial_result_sets(
            [("ID", TypeCode.INT64), ("NAME", TypeCode.STRING)],
            [
                {"values": ["1", "ABC", "2", "DEF"]},
                {"values": ["3", "GHI"], "last": True},
            ],
        )

        sql = "select * from my_table"
        add_execute_streaming_sql_results(sql, partial_result_sets)
        count = 1
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql(sql)
            result_list = []
            for row in results:
                result_list.append(row)
                self.assertEqual(count, row[0])
                count += 1
            self.assertEqual(3, len(result_list))
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest],
            TransactionType.READ_ONLY,
        )


def _execute_query(transaction: Transaction, sql: str):
    rows = transaction.execute_sql(sql, last_statement=True)
    for _ in rows:
        pass
