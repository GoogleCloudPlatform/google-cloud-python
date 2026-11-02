# Copyright 2023 Google LLC All rights reserved.
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

from google.cloud.spanner_dbapi import ProgrammingError
from google.cloud.spanner_dbapi.batch_dml_executor import BatchDmlExecutor
from google.cloud.spanner_dbapi.parsed_statement import (
    ParsedStatement,
    Statement,
    StatementType,
)


class TestBatchDmlExecutor(unittest.TestCase):
    @mock.patch("google.cloud.spanner_dbapi.cursor.Cursor")
    def setUp(self, mock_cursor):
        self._under_test = BatchDmlExecutor(mock_cursor)

    def test_execute_statement_non_dml_statement_type(self):
        parsed_statement = ParsedStatement(StatementType.QUERY, Statement("sql"))

        with self.assertRaises(ProgrammingError):
            self._under_test.execute_statement(parsed_statement)

    def test_execute_statement_insert_statement_type(self):
        statement = Statement("sql")

        self._under_test.execute_statement(
            ParsedStatement(StatementType.INSERT, statement)
        )

        self.assertEqual(self._under_test._statements, [statement])

    def test_execute_statement_update_statement_type(self):
        statement = Statement("sql")

        self._under_test.execute_statement(
            ParsedStatement(StatementType.UPDATE, statement)
        )

        self.assertEqual(self._under_test._statements, [statement])
