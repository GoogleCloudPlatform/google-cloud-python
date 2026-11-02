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
"""Tests for connection.py"""

from google.cloud.spanner_driver import connect

from ._helper import get_test_connection_string


class TestConnect:
    def test_cursor(self):
        """Test the connect method."""
        connection_string = get_test_connection_string()

        # Test Context Manager
        with connect(connection_string) as connection:
            assert connection is not None

            # Test Cursor Context Manager
            with connection.cursor() as cursor:
                assert cursor is not None


class TestConnectMethod:
    """Tests for the connection.py module."""

    def test_connect(self):
        """Test the connect method."""
        connection_string = get_test_connection_string()

        # Test Context Manager
        with connect(connection_string) as connection:
            assert connection is not None
