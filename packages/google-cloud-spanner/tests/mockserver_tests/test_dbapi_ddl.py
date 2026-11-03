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

from google.cloud.spanner_dbapi.connection import Connection
from google.cloud.spanner_dbapi.exceptions import ProgrammingError
from google.cloud.spanner_v1 import ExecuteBatchDmlRequest, ExecuteSqlRequest
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_select1_result,
    add_update_count,
)


class TestDbapiDdl(MockServerTestBase):
    def test_ddl_autocommit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        ddl_statement = (
            "CREATE TABLE Singers ("
            "SingerId INT64 NOT NULL, "
            "Name STRING(1024)"
            ") PRIMARY KEY (SingerId)"
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(ddl_statement)

            self.assertEqual(1, len(self.database_admin_service.requests))
            request = self.database_admin_service.requests[0]
            self.assertEqual(self.database.name, request.database)
            self.assertEqual([ddl_statement], request.statements)
        finally:
            connection.close()

    def test_ddl_buffered_until_commit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        ddl_statement = (
            "CREATE TABLE Singers ("
            "SingerId INT64 NOT NULL, "
            "Name STRING(1024)"
            ") PRIMARY KEY (SingerId)"
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(ddl_statement)

            self.assertEqual(0, len(self.database_admin_service.requests))
            connection.commit()

            self.assertEqual(1, len(self.database_admin_service.requests))
            request = self.database_admin_service.requests[0]
            self.assertEqual(self.database.name, request.database)
            self.assertEqual([ddl_statement], request.statements)
        finally:
            connection.close()

    def test_ddl_multiple_statements_buffered_until_commit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        statement1 = "CREATE TABLE Table1 (Id INT64) PRIMARY KEY (Id)"
        statement2 = "CREATE TABLE Table2 (Id INT64) PRIMARY KEY (Id)"

        try:
            with connection.cursor() as cursor:
                cursor.execute(statement1)
                cursor.execute(statement2)

            self.assertEqual(0, len(self.database_admin_service.requests))
            connection.commit()

            self.assertEqual(1, len(self.database_admin_service.requests))
            request = self.database_admin_service.requests[0]
            self.assertEqual(self.database.name, request.database)
            self.assertEqual([statement1, statement2], request.statements)
        finally:
            connection.close()

    def test_ddl_semicolon_separated_statements_autocommit(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = True
        statement1 = "CREATE TABLE Table1 (Id INT64) PRIMARY KEY (Id)"
        statement2 = "CREATE TABLE Table2 (Id INT64) PRIMARY KEY (Id)"

        try:
            with connection.cursor() as cursor:
                cursor.execute(f"{statement1}; {statement2}")

            self.assertEqual(1, len(self.database_admin_service.requests))
            request = self.database_admin_service.requests[0]
            self.assertEqual(self.database.name, request.database)
            self.assertEqual([statement1, statement2], request.statements)
        finally:
            connection.close()

    def test_ddl_flushed_before_subsequent_execute(self):
        dml_statement = "INSERT INTO Singers (SingerId, Name) VALUES (1, 'first-name')"
        add_update_count(dml_statement, 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        ddl_statement = (
            "CREATE TABLE Singers ("
            "SingerId INT64 NOT NULL, "
            "Name STRING(1024)"
            ") PRIMARY KEY (SingerId)"
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(ddl_statement)
                self.assertEqual(0, len(self.database_admin_service.requests))

                cursor.execute(dml_statement)
                self.assertEqual(1, len(self.database_admin_service.requests))
                request = self.database_admin_service.requests[0]
                self.assertEqual(self.database.name, request.database)
                self.assertEqual([ddl_statement], request.statements)
                self.assertEqual(1, cursor.rowcount)

            execute_requests = [
                req
                for req in self.spanner_service.requests
                if isinstance(req, ExecuteSqlRequest)
            ]
            self.assertEqual(1, len(execute_requests))
            self.assertEqual(dml_statement, execute_requests[0].sql)

            connection.commit()
            self.assertEqual(1, len(self.database_admin_service.requests))
        finally:
            connection.close()

    def test_ddl_flushed_before_subsequent_executemany(self):
        dml_statement = "INSERT INTO Singers (SingerId, Name) VALUES (1, 'first-name')"
        add_update_count(dml_statement, 1)

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        ddl_statement = (
            "CREATE TABLE Singers ("
            "SingerId INT64 NOT NULL, "
            "Name STRING(1024)"
            ") PRIMARY KEY (SingerId)"
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(ddl_statement)
                self.assertEqual(0, len(self.database_admin_service.requests))

                cursor.executemany(dml_statement, [()])
                self.assertEqual(1, len(self.database_admin_service.requests))
                request = self.database_admin_service.requests[0]
                self.assertEqual(self.database.name, request.database)
                self.assertEqual([ddl_statement], request.statements)
                self.assertEqual(1, cursor.rowcount)

            batch_requests = [
                req
                for req in self.spanner_service.requests
                if isinstance(req, ExecuteBatchDmlRequest)
            ]
            self.assertEqual(1, len(batch_requests))
            self.assertEqual(dml_statement, batch_requests[0].statements[0].sql)

            connection.commit()
            self.assertEqual(1, len(self.database_admin_service.requests))
        finally:
            connection.close()

    def test_ddl_flushed_before_subsequent_query(self):
        add_select1_result()

        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        ddl_statement = (
            "CREATE TABLE Singers ("
            "SingerId INT64 NOT NULL, "
            "Name STRING(1024)"
            ") PRIMARY KEY (SingerId)"
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute(ddl_statement)
                self.assertEqual(0, len(self.database_admin_service.requests))

                cursor.execute("SELECT 1")
                self.assertEqual(1, len(self.database_admin_service.requests))
                request = self.database_admin_service.requests[0]
                self.assertEqual(self.database.name, request.database)
                self.assertEqual([ddl_statement], request.statements)

            connection.commit()
            self.assertEqual(1, len(self.database_admin_service.requests))
        finally:
            connection.close()

    def test_ddl_uncommitted_on_close(self):
        connection = Connection(self.instance, self.database)
        connection.autocommit = False
        ddl_statement = (
            "CREATE TABLE Singers ("
            "SingerId INT64 NOT NULL, "
            "Name STRING(1024)"
            ") PRIMARY KEY (SingerId)"
        )

        with connection.cursor() as cursor:
            cursor.execute(ddl_statement)

        connection.close()
        self.assertEqual(0, len(self.database_admin_service.requests))

    def test_ddl_executemany_rejected_client_side(self):
        connection = Connection(self.instance, self.database)
        ddl_statement = "CREATE TABLE Singers (SingerId INT64) PRIMARY KEY (SingerId)"

        try:
            for autocommit in (False, True):
                connection.autocommit = autocommit
                with connection.cursor() as cursor:
                    with self.assertRaises(ProgrammingError):
                        cursor.executemany(ddl_statement, [])

                self.assertEqual(0, len(self.database_admin_service.requests))
        finally:
            connection.close()
