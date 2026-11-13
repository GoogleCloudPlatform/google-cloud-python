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

from google.cloud.spanner_dbapi import Connection
from google.cloud.spanner_dbapi.parsed_statement import (
    ClientSideStatementType,
    ParsedStatement,
    Statement,
    StatementType,
)
from google.cloud.spanner_v1 import (
    ExecuteSqlRequest,
    TypeCode,
)
from google.cloud.spanner_v1.types import spanner as spanner_types
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_single_result,
)


class TestDbapiDataBoost(MockServerTestBase):
    def setUp(self):
        super().setUp()
        add_single_result(
            "select name from singers", "name", TypeCode.STRING, [("Some Singer",)]
        )

    def test_select_with_data_boost_enabled_autocommit(self):
        # Non-partitioned queries should NOT have data_boost_enabled=True on ExecuteSqlRequest,
        # because Spanner rejects data_boost_enabled without a partition_token.
        connection = Connection(self.instance, self.database, data_boost_enabled=True)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
            self.assertEqual(1, len(rows))
            self.assertEqual("Some Singer", rows[0][0])

        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        self.assertFalse(requests[0].data_boost_enabled)

    def test_select_with_data_boost_enabled_read_only(self):
        connection = Connection(
            self.instance, self.database, read_only=True, data_boost_enabled=True
        )
        with connection.cursor() as cursor:
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
            self.assertEqual(1, len(rows))
            self.assertEqual("Some Singer", rows[0][0])

        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        self.assertFalse(requests[0].data_boost_enabled)

    def test_select_with_data_boost_disabled_by_default(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
            self.assertEqual(1, len(rows))

        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        self.assertFalse(requests[0].data_boost_enabled)

    def test_select_with_set_data_boost_statement(self):
        connection = Connection(self.instance, self.database, data_boost_enabled=False)
        connection.autocommit = True
        with connection.cursor() as cursor:
            # Enable DataBoost via SQL client-side statement
            cursor.execute("SET DATA_BOOST_ENABLED = TRUE")
            self.assertTrue(cursor.connection.data_boost_enabled)
            cursor.execute("select name from singers")
            rows = cursor.fetchall()
            self.assertEqual(1, len(rows))

        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        # Non-partitioned query should still be False
        self.assertFalse(requests[0].data_boost_enabled)

    def test_partition_query_and_run_partition_with_data_boost_enabled(self):
        sql = "SELECT name FROM users WHERE active = true"

        partition_response = spanner_types.PartitionResponse()
        partition_response.partitions.extend(
            [
                spanner_types.Partition(partition_token=b"mock-token-1"),
            ]
        )
        self.spanner_service.mock_spanner.add_partition_result(sql, partition_response)
        add_single_result(sql, "name", TypeCode.STRING, [("Alice",)])

        connection = Connection(
            self.instance, self.database, read_only=True, data_boost_enabled=True
        )

        parsed = ParsedStatement(
            statement_type=StatementType.CLIENT_SIDE,
            statement=Statement(sql),
            client_side_statement_type=ClientSideStatementType.PARTITION_QUERY,
            client_side_statement_params=[sql],
        )

        partition_ids = connection.partition_query(parsed)
        self.assertEqual(1, len(partition_ids))

        # Execute the partition and verify the ExecuteSqlRequest has data_boost_enabled=True
        result_stream = connection.run_partition(partition_ids[0])
        rows = list(result_stream)
        self.assertEqual(1, len(rows))
        self.assertEqual("Alice", rows[0][0])

        execute_requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(execute_requests))
        self.assertTrue(execute_requests[0].data_boost_enabled)
        self.assertEqual(b"mock-token-1", execute_requests[0].partition_token)

    def test_run_partitioned_query_with_data_boost_enabled(self):
        sql = "SELECT name FROM users WHERE active = true"

        partition_response = spanner_types.PartitionResponse()
        partition_response.partitions.extend(
            [
                spanner_types.Partition(partition_token=b"mock-token-1"),
            ]
        )
        self.spanner_service.mock_spanner.add_partition_result(sql, partition_response)
        add_single_result(sql, "name", TypeCode.STRING, [("Alice",)])

        connection = Connection(
            self.instance, self.database, read_only=True, data_boost_enabled=True
        )

        parsed = ParsedStatement(
            statement_type=StatementType.CLIENT_SIDE,
            statement=Statement(sql),
            client_side_statement_type=ClientSideStatementType.RUN_PARTITIONED_QUERY,
            client_side_statement_params=[sql],
        )

        result_set = connection.run_partitioned_query(parsed)
        rows = list(result_set)
        self.assertEqual(1, len(rows))
        self.assertEqual("Alice", rows[0][0])

        execute_requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(execute_requests))
        self.assertTrue(execute_requests[0].data_boost_enabled)

    def test_auto_partition_mode_with_data_boost_enabled(self):
        sql = "SELECT name FROM users WHERE active = true"

        partition_response = spanner_types.PartitionResponse()
        partition_response.partitions.extend(
            [
                spanner_types.Partition(partition_token=b"mock-token-auto-1"),
            ]
        )
        self.spanner_service.mock_spanner.add_partition_result(sql, partition_response)
        add_single_result(sql, "name", TypeCode.STRING, [("Alice",)])

        connection = Connection(
            self.instance,
            self.database,
            read_only=True,
            auto_partition_mode=True,
            data_boost_enabled=True,
        )

        with connection.cursor() as cursor:
            # Plain cursor.execute automatically runs as partitioned query with DataBoost
            cursor.execute(sql)
            rows = cursor.fetchall()
            self.assertEqual(1, len(rows))
            self.assertEqual("Alice", rows[0][0])

        execute_requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(execute_requests))
        self.assertTrue(execute_requests[0].data_boost_enabled)
        self.assertEqual(b"mock-token-auto-1", execute_requests[0].partition_token)

    def test_auto_partition_mode_via_statement(self):
        sql = "SELECT name FROM users WHERE active = true"

        partition_response = spanner_types.PartitionResponse()
        partition_response.partitions.extend(
            [
                spanner_types.Partition(partition_token=b"mock-token-auto-2"),
            ]
        )
        self.spanner_service.mock_spanner.add_partition_result(sql, partition_response)
        add_single_result(sql, "name", TypeCode.STRING, [("Bob",)])

        connection = Connection(self.instance, self.database, read_only=True)

        with connection.cursor() as cursor:
            cursor.execute("SET AUTO_PARTITION_MODE = TRUE")
            cursor.execute("SET DATA_BOOST_ENABLED = TRUE")
            self.assertTrue(cursor.connection.auto_partition_mode)
            self.assertTrue(cursor.connection.data_boost_enabled)

            cursor.execute(sql)
            rows = cursor.fetchall()
            self.assertEqual(1, len(rows))
            self.assertEqual("Bob", rows[0][0])

        execute_requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(execute_requests))
        self.assertTrue(execute_requests[0].data_boost_enabled)
        self.assertEqual(b"mock-token-auto-2", execute_requests[0].partition_token)
