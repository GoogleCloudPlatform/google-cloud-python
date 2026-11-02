# Copyright 2026 Google LLC
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

import unittest
from unittest import mock

from google.cloud import spanner_driver
from google.cloud.spanner_driver import connection, errors


class TestConnect(unittest.TestCase):
    def test_connect(self):
        connection_string = "spanner://projects/p/instances/i/databases/d"

        with mock.patch(
            "google.cloud.spannerlib.pool.Pool.create_pool"
        ) as mock_create_pool:
            mock_pool = mock.Mock()
            mock_create_pool.return_value = mock_pool
            mock_internal_conn = mock.Mock()
            mock_pool.create_connection.return_value = mock_internal_conn

            conn = spanner_driver.connect(connection_string)

            self.assertIsInstance(conn, connection.Connection)
            mock_create_pool.assert_called_once_with(connection_string)
            mock_pool.create_connection.assert_called_once()


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.mock_internal_conn = mock.Mock()
        self.conn = connection.Connection(self.mock_internal_conn)

    def test_cursor(self):
        cursor = self.conn.cursor()
        self.assertIsInstance(cursor, spanner_driver.Cursor)
        self.assertEqual(cursor._connection, self.conn)

    def test_cursor_closed(self):
        self.conn.close()
        with self.assertRaises(errors.InterfaceError):
            self.conn.cursor()

    def test_begin(self):
        self.conn.begin()
        self.mock_internal_conn.begin_transaction.assert_called_once()

    def test_begin_error(self):
        self.mock_internal_conn.begin_transaction.side_effect = Exception(
            "Internal Error"
        )
        with self.assertRaises(errors.DatabaseError):
            self.conn.begin()

    def test_commit(self):
        self.conn.commit()
        self.mock_internal_conn.commit.assert_called_once()

    def test_commit_error(self):
        self.mock_internal_conn.commit.side_effect = Exception("Commit Failed")
        with self.assertRaises(errors.DatabaseError):
            self.conn.commit()
        self.mock_internal_conn.commit.assert_called_once()

    def test_rollback(self):
        self.conn.rollback()
        self.mock_internal_conn.rollback.assert_called_once()

    def test_rollback_error(self):
        self.mock_internal_conn.rollback.side_effect = Exception("Rollback Failed")
        with self.assertRaises(errors.DatabaseError):
            self.conn.rollback()
        self.mock_internal_conn.rollback.assert_called_once()

    def test_close(self):
        self.assertFalse(self.conn._closed)
        self.conn.close()
        self.assertTrue(self.conn._closed)
        self.mock_internal_conn.close.assert_called_once()

    def test_close_idempotent(self):
        self.conn.close()
        self.mock_internal_conn.close.reset_mock()
        self.assertRaises(errors.InterfaceError, self.conn.close)

    def test_messages(self):
        self.assertEqual(self.conn.messages, [])

    def test_context_manager(self):
        with self.conn as c:
            self.assertEqual(c, self.conn)
            self.assertFalse(c._closed)
        self.assertTrue(self.conn._closed)
        self.mock_internal_conn.close.assert_called_once()
