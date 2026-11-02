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

import unittest

from google.cloud.spanner_dbapi.client_side_statement_executor import (
    _get_isolation_level,
)
from google.cloud.spanner_dbapi.parse_utils import classify_statement
from google.cloud.spanner_v1 import TransactionOptions


class TestParseUtils(unittest.TestCase):
    def test_get_isolation_level(self):
        self.assertIsNone(_get_isolation_level(classify_statement("begin")))
        self.assertEqual(
            TransactionOptions.IsolationLevel.SERIALIZABLE,
            _get_isolation_level(
                classify_statement("begin isolation level serializable")
            ),
        )
        self.assertEqual(
            TransactionOptions.IsolationLevel.SERIALIZABLE,
            _get_isolation_level(
                classify_statement(
                    "begin  transaction  isolation    level     serializable    "
                )
            ),
        )
        self.assertEqual(
            TransactionOptions.IsolationLevel.REPEATABLE_READ,
            _get_isolation_level(
                classify_statement("begin isolation level repeatable read")
            ),
        )
        self.assertEqual(
            TransactionOptions.IsolationLevel.REPEATABLE_READ,
            _get_isolation_level(
                classify_statement(
                    "begin    transaction  isolation    level   repeatable    read "
                )
            ),
        )


class TestClientSideStatementExecutor(unittest.TestCase):
    def test_execute_set_data_boost_enabled(self):
        from unittest import mock

        from google.cloud.spanner_dbapi.client_side_statement_executor import execute
        from google.cloud.spanner_dbapi.exceptions import ProgrammingError

        cursor = mock.MagicMock()
        cursor.connection.is_closed = False
        cursor.connection.data_boost_enabled = False

        stmt = classify_statement("SET DATA_BOOST_ENABLED = TRUE")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertTrue(cursor.connection.data_boost_enabled)

        stmt = classify_statement("SET DATA_BOOST_ENABLED = FALSE")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertFalse(cursor.connection.data_boost_enabled)

        stmt = classify_statement("SET DATA_BOOST_ENABLED = TRUE;")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertTrue(cursor.connection.data_boost_enabled)

        stmt = classify_statement("SET DATA_BOOST_ENABLED = 'FALSE';")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertFalse(cursor.connection.data_boost_enabled)

        stmt = classify_statement("SET DATA_BOOST_ENABLED = INVALID")
        with self.assertRaises(ProgrammingError):
            execute(cursor, stmt)

    def test_execute_show_data_boost_enabled(self):
        from unittest import mock

        from google.cloud.spanner_dbapi.client_side_statement_executor import execute
        from google.cloud.spanner_v1 import TypeCode

        cursor = mock.MagicMock()
        cursor.connection.is_closed = False
        cursor.connection.data_boost_enabled = True

        stmt = classify_statement("SHOW VARIABLE DATA_BOOST_ENABLED")
        res = execute(cursor, stmt)
        rows = list(res)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], True)
        self.assertEqual(res.fields[0].name, "DATA_BOOST_ENABLED")
        self.assertEqual(res.fields[0].type_.code, TypeCode.BOOL)

        stmt_semicolon = classify_statement("SHOW VARIABLE DATA_BOOST_ENABLED;")
        res_semicolon = execute(cursor, stmt_semicolon)
        rows_semicolon = list(res_semicolon)
        self.assertEqual(len(rows_semicolon), 1)
        self.assertEqual(rows_semicolon[0][0], True)

        cursor.connection.data_boost_enabled = False
        res = execute(cursor, stmt)
        rows = list(res)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], False)

    def test_execute_set_auto_partition_mode(self):
        from unittest import mock

        from google.cloud.spanner_dbapi.client_side_statement_executor import execute
        from google.cloud.spanner_dbapi.exceptions import ProgrammingError

        cursor = mock.MagicMock()
        cursor.connection.is_closed = False
        cursor.connection.auto_partition_mode = False

        stmt = classify_statement("SET AUTO_PARTITION_MODE = TRUE")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertTrue(cursor.connection.auto_partition_mode)

        stmt = classify_statement("SET AUTO_PARTITION_MODE = FALSE")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertFalse(cursor.connection.auto_partition_mode)

        stmt = classify_statement("SET AUTO_PARTITION_MODE = TRUE;")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertTrue(cursor.connection.auto_partition_mode)

        stmt = classify_statement("SET AUTO_PARTITION_MODE = 'FALSE';")
        res = execute(cursor, stmt)
        self.assertIsNone(res)
        self.assertFalse(cursor.connection.auto_partition_mode)

        stmt = classify_statement("SET AUTO_PARTITION_MODE = INVALID")
        with self.assertRaises(ProgrammingError):
            execute(cursor, stmt)

    def test_execute_show_auto_partition_mode(self):
        from unittest import mock

        from google.cloud.spanner_dbapi.client_side_statement_executor import execute
        from google.cloud.spanner_v1 import TypeCode

        cursor = mock.MagicMock()
        cursor.connection.is_closed = False
        cursor.connection.auto_partition_mode = True

        stmt = classify_statement("SHOW VARIABLE AUTO_PARTITION_MODE")
        res = execute(cursor, stmt)
        rows = list(res)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], True)
        self.assertEqual(res.fields[0].name, "AUTO_PARTITION_MODE")
        self.assertEqual(res.fields[0].type_.code, TypeCode.BOOL)

        cursor.connection.auto_partition_mode = False
        res = execute(cursor, stmt)
        rows = list(res)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], False)
