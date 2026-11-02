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
"""Tests for executemany support in cursor.py"""

from google.cloud.spanner_driver import connect

from ._helper import get_test_connection_string

DDL = """
CREATE TABLE Singers (
    SingerId INT64 NOT NULL,
    FirstName STRING(1024),
    LastName STRING(1024),
) PRIMARY KEY (SingerId)
"""


class TestExecuteMany:
    def setup_method(self):
        """Re-create the table before each test."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS Singers")
                cursor.execute(DDL)

    def test_executemany(self):
        """Test executemany with multiple rows."""
        connection_string = get_test_connection_string()

        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                sql = (
                    "INSERT INTO Singers (SingerId, FirstName, LastName) "
                    "VALUES (@id, @first, @last)"
                )
                params_seq = [
                    {"id": 1, "first": "Alice", "last": "A"},
                    {"id": 2, "first": "Bob", "last": "B"},
                    {"id": 3, "first": "Charlie", "last": "C"},
                ]

                cursor.executemany(sql, params_seq)

                assert cursor.rowcount == 3

                # Verify rows
                cursor.execute("SELECT * FROM Singers ORDER BY SingerId")
                rows = cursor.fetchall()
                assert len(rows) == 3
                assert rows[0] == (1, "Alice", "A")
                assert rows[1] == (2, "Bob", "B")
                assert rows[2] == (3, "Charlie", "C")
