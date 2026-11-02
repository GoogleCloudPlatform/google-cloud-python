# Copyright 2025 Google LLC All rights reserved.
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
from google.cloud.spanner_v1 import (
    CommitRequest,
    ExecuteBatchDmlRequest,
    ExecuteSqlRequest,
    TypeCode,
)
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_single_result,
    add_update_count,
)


class TestDbapiAutoCommit(MockServerTestBase):
    def setUp(self):
        super().setUp()
        add_single_result(
            "select name from singers", "name", TypeCode.STRING, [("Some Singer",)]
        )
        add_update_count("insert into singers (id, name) values (1, 'Some Singer')", 1)

    def test_select_autocommit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("select name from singers")
            result_list = cursor.fetchall()
            for _ in result_list:
                pass
        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        self.assertFalse(requests[0].last_statement, requests[0])
        self.assertIsNotNone(requests[0].transaction, requests[0])
        self.assertIsNotNone(requests[0].transaction.single_use, requests[0])
        self.assertTrue(requests[0].transaction.single_use.read_only, requests[0])

    def test_dml_autocommit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")
            self.assertEqual(1, cursor.rowcount)
        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteSqlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        self.assertTrue(requests[0].last_statement, requests[0])
        commit_requests = list(
            filter(
                lambda msg: isinstance(msg, CommitRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(commit_requests))

    def test_executemany_autocommit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.executemany(
                "insert into singers (id, name) values (1, 'Some Singer')", [(), ()]
            )
            self.assertEqual(2, cursor.rowcount)
        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteBatchDmlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        self.assertTrue(requests[0].last_statements, requests[0])
        commit_requests = list(
            filter(
                lambda msg: isinstance(msg, CommitRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(commit_requests))

    def test_batch_dml_autocommit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("start batch dml")
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")
            cursor.execute("insert into singers (id, name) values (1, 'Some Singer')")
            cursor.execute("run batch")
            self.assertEqual(2, cursor.rowcount)
        requests = list(
            filter(
                lambda msg: isinstance(msg, ExecuteBatchDmlRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(requests))
        self.assertTrue(requests[0].last_statements, requests[0])
        commit_requests = list(
            filter(
                lambda msg: isinstance(msg, CommitRequest),
                self.spanner_service.requests,
            )
        )
        self.assertEqual(1, len(commit_requests))
