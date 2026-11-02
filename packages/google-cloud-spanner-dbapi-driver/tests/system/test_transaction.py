#  Copyright 2026 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Tests for transaction support in connection.py"""

from google.cloud.spanner_driver import connect

from ._helper import get_test_connection_string

DDL = """
CREATE TABLE Singers (
    SingerId INT64 NOT NULL,
    FirstName STRING(1024),
    LastName STRING(1024),
) PRIMARY KEY (SingerId)
"""


class TestTransaction:
    def setup_method(self):
        """Re-create the table before each test."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS Singers")
                cursor.execute(DDL)

    def test_commit(self):
        """Test that changes are visible after commit."""
        connection_string = get_test_connection_string()

        # 1. Insert in a transaction
        with connect(connection_string) as conn1:
            conn1.begin()
            with conn1.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Singers (SingerId, FirstName, LastName) "
                    "VALUES (@id, @first, @last)",
                    {"id": 1, "first": "John", "last": "Doe"},
                )
            conn1.commit()

        # 2. Verify visibility from another connection
        with connect(connection_string) as conn2:
            with conn2.cursor() as cursor:
                cursor.execute("SELECT FirstName FROM Singers WHERE SingerId = 1")
                row = cursor.fetchone()
                assert row == ("John",)

    def test_rollback(self):
        """Test that changes are discarded after rollback."""
        connection_string = get_test_connection_string()

        # 1. Insert then rollback
        with connect(connection_string) as conn1:
            conn1.begin()
            with conn1.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Singers (SingerId, FirstName, LastName) "
                    "VALUES (@id, @first, @last)",
                    {"id": 2, "first": "Jane", "last": "Doe"},
                )
            conn1.rollback()

        # 2. Verify NOT visible
        with connect(connection_string) as conn2:
            with conn2.cursor() as cursor:
                cursor.execute("SELECT FirstName FROM Singers WHERE SingerId = 2")
                row = cursor.fetchone()
                assert row is None

    def test_isolation(self):
        """Test that uncommitted changes are not visible to others."""
        connection_string = get_test_connection_string()

        conn1 = connect(connection_string)
        conn2 = connect(connection_string)

        try:
            conn1.begin()
            curs1 = conn1.cursor()
            curs2 = conn2.cursor()

            # Insert in conn1 (uncommitted)
            curs1.execute(
                "INSERT INTO Singers (SingerId, FirstName, LastName) "
                "VALUES (@id, @first, @last)",
                {"id": 3, "first": "Bob", "last": "Smith"},
            )

            # Check from conn2
            curs2.execute("SELECT FirstName FROM Singers WHERE SingerId = 3")
            row = curs2.fetchone()
            assert row is None

            # Commit conn1
            conn1.commit()

            # Check from conn2
            curs2.execute("SELECT FirstName FROM Singers WHERE SingerId = 3")
            row = curs2.fetchone()
            assert row == ("Bob",)

        finally:
            conn1.close()
            conn2.close()
