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
"""Tests for error handling in cursor.py and connection.py"""

import pytest

from google.cloud.spanner_driver import connect, errors

from ._helper import get_test_connection_string

DDL = """
CREATE TABLE Singers (
    SingerId INT64 NOT NULL,
    FirstName STRING(1024),
    LastName STRING(1024),
) PRIMARY KEY (SingerId)
"""


class TestErrors:
    def setup_method(self):
        """Re-create the table before each test."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS Singers")
                cursor.execute(DDL)

    def test_programming_error_table_not_found(self):
        """Test that selecting from a non-existent table
        raises expected error."""
        connection_string = get_test_connection_string()

        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                with pytest.raises(errors.ProgrammingError):
                    cursor.execute("SELECT * FROM NonExistentTable")

    def test_integrity_error_duplicate_pk(self):
        """Test that duplicate primary key raises IntegrityError."""
        connection_string = get_test_connection_string()

        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                sql = (
                    "INSERT INTO Singers (SingerId, FirstName, LastName) "
                    "VALUES (@id, @first, @last)"
                )
                params = {"id": 1, "first": "Alice", "last": "A"}

                cursor.execute(sql, params)

                # Second insert with same PK
                with pytest.raises(errors.IntegrityError):
                    cursor.execute(sql, params)

    def test_operational_error_syntax(self):
        """Test bad syntax raises ProgrammingError/OperationalError."""
        connection_string = get_test_connection_string()
        with connect(connection_string) as connection:
            with connection.cursor() as cursor:
                with pytest.raises(errors.ProgrammingError):
                    cursor.execute("SELECT * FROM Singers WHERE")
