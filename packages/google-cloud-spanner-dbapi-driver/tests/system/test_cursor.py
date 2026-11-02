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
"""Tests for cursor.py"""

from google.cloud.spanner_driver import connect, types

from ._helper import get_test_connection_string


class TestCursor:
    def test_execute(self):
        """Test the execute method."""
        connection_string = get_test_connection_string()

        # Test Context Manager
        with connect(connection_string) as connection:
            assert connection is not None

            # Test Cursor Context Manager
            with connection.cursor() as cursor:
                assert cursor is not None

                # Test execute and fetchone
                cursor.execute("SELECT 1 AS col1")
                assert cursor.description is not None
                assert cursor.description[0][0] == "col1"
                assert (
                    cursor.description[0][1] == types.NUMBER
                )  # TypeCode.INT64 maps to types.NUMBER

                result = cursor.fetchone()
                assert result == (1,)

    def test_execute_params(self):
        """Test the execute method with parameters."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                sql = "SELECT @a AS col1"
                params = {"a": 1}
                cursor.execute(sql, params)
                result = cursor.fetchone()
                assert result == (1,)

    def test_execute_dml(self):
        """Test DML execution."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS Singers")

                # Create table
                cursor.execute(
                    """
                    CREATE TABLE Singers (
                        SingerId INT64 NOT NULL,
                        FirstName STRING(1024),
                        LastName STRING(1024),
                    ) PRIMARY KEY (SingerId)
                    """
                )

                # Insert
                cursor.execute(
                    "INSERT INTO Singers (SingerId, FirstName, LastName) "
                    "VALUES (@id, @first, @last)",
                    {"id": 1, "first": "John", "last": "Doe"},
                )
                assert cursor.rowcount == 1

                # Update
                cursor.execute(
                    "UPDATE Singers SET FirstName = 'Jane' WHERE SingerId = 1"
                )
                assert cursor.rowcount == 1

                # Select back to verify
                cursor.execute("SELECT FirstName FROM Singers WHERE SingerId = 1")
                row = cursor.fetchone()
                assert row == ("Jane",)

                # Cleanup (optional if emulator is reset)

    def test_fetch_methods(self):
        """Test fetchmany and fetchall."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                # Use UNNEST to generate rows
                cursor.execute(
                    "SELECT * FROM UNNEST([1, 2, 3, 4, 5]) AS numbers ORDER BY numbers"
                )

                # Fetch one
                row = cursor.fetchone()
                assert row == (1,)

                # Fetch many
                rows = cursor.fetchmany(2)
                assert len(rows) == 2
                assert rows[0] == (2,)
                assert rows[1] == (3,)

                # Fetch all remaining
                rows = cursor.fetchall()
                assert len(rows) == 2
                assert rows[0] == (4,)
                assert rows[1] == (5,)

    def test_data_types(self):
        """Test various data types."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                sql = """
                    SELECT
                        1 AS int_val,
                        3.14 AS float_val,
                        TRUE AS bool_val,
                        'hello' AS str_val,
                        b'bytes' AS bytes_val,
                        DATE '2023-01-01' AS date_val,
                        TIMESTAMP '2023-01-01T12:00:00Z' AS timestamp_val
                """
                cursor.execute(sql)
                row = cursor.fetchone()

                assert row[0] == 1
                assert row[1] == 3.14
                assert row[2] is True
                assert row[3] == "hello"
                assert row[4] == b"bytes"
