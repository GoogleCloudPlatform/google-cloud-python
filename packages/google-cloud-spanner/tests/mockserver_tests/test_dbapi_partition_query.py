# Copyright 2026 Google LLC All rights reserved.
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


from google.cloud.spanner_dbapi.connection import Connection
from google.cloud.spanner_dbapi.parsed_statement import ParsedStatement, Statement
from google.cloud.spanner_v1 import TypeCode
from google.cloud.spanner_v1.types import spanner as spanner_types
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_single_result,
)


class TestDbapiPartitionQuery(MockServerTestBase):
    def test_partition_query_and_run_partition(self):
        sql = "SELECT name FROM users WHERE active = true"

        # 1. Set up mock results for PartitionQuery RPC in the mock servicer
        partition_response = spanner_types.PartitionResponse()
        partition_response.partitions.extend(
            [
                spanner_types.Partition(partition_token=b"mock-token-1"),
                spanner_types.Partition(partition_token=b"mock-token-2"),
            ]
        )
        self.spanner_service.mock_spanner.add_partition_result(sql, partition_response)

        # 2. Set up mock results for ExecuteSql when executing the partitions
        add_single_result(sql, "name", TypeCode.STRING, [("Alice",), ("Bob",)])

        # 3. Connect via DB-API and mark connection as read-only (required for partitioning)
        connection = Connection(self.instance, self.database)
        connection._read_only = True

        # Define partitioning parameters inside DB-API Statement
        from google.cloud.spanner_dbapi.parsed_statement import (
            ClientSideStatementType,
            StatementType,
        )

        parsed = ParsedStatement(
            statement_type=StatementType.CLIENT_SIDE,
            statement=Statement(sql),
            client_side_statement_type=ClientSideStatementType.PARTITION_QUERY,
            client_side_statement_params=["SELECT name FROM users WHERE active = true"],
        )

        # Generate serialized token strings (Base64 + GZip JSON)
        partition_ids = connection.partition_query(parsed)
        self.assertEqual(2, len(partition_ids))

        # 4. Reconstruct & Execute the partitions by deserializing their tokens
        all_names = []
        for token in partition_ids:
            result_stream = connection.run_partition(token)
            for row in result_stream:
                all_names.append(row[0])

        # Verify results are successfully round-tripped and parsed
        self.assertIn("Alice", all_names)
        self.assertIn("Bob", all_names)

    def test_partition_query_with_complex_parameters(self):
        import datetime
        import decimal

        sql = "SELECT name FROM users WHERE active = @active AND salary > @salary AND signup_time = @signup_time"

        # Set up complex parameter values (bool, Decimal, datetime)
        params = {
            "active": True,
            "salary": decimal.Decimal("75000.50"),
            "signup_time": datetime.datetime(
                2026, 5, 10, 12, 34, 56, tzinfo=datetime.timezone.utc
            ),
        }
        from google.cloud.spanner_v1 import Type

        param_types = {
            "active": Type(code=TypeCode.BOOL),
            "salary": Type(code=TypeCode.NUMERIC),
            "signup_time": Type(code=TypeCode.TIMESTAMP),
        }

        # 1. Mock results for the partition generation RPC
        partition_response = spanner_types.PartitionResponse()
        partition_response.partitions.extend(
            [spanner_types.Partition(partition_token=b"complex-mock-token-1")]
        )
        self.spanner_service.mock_spanner.add_partition_result(sql, partition_response)

        # 2. Mock results for execution of partition streaming SQL
        add_single_result(sql, "name", TypeCode.STRING, [("Charlie",)])

        # 3. Establish Connection
        connection = Connection(self.instance, self.database)
        connection._read_only = True

        from google.cloud.spanner_dbapi.parsed_statement import (
            ClientSideStatementType,
            StatementType,
        )

        parsed = ParsedStatement(
            statement_type=StatementType.CLIENT_SIDE,
            statement=Statement(sql, params=params, param_types=param_types),
            client_side_statement_type=ClientSideStatementType.PARTITION_QUERY,
            client_side_statement_params=[sql],
        )

        # Execute partition generation - this serializes query parameters!
        partition_ids = connection.partition_query(parsed)
        self.assertEqual(1, len(partition_ids))

        # 4. Reconstruct and run the partition E2E
        all_names = []
        for token in partition_ids:
            result_stream = connection.run_partition(token)
            for row in result_stream:
                all_names.append(row[0])

        self.assertEqual(["Charlie"], all_names)
