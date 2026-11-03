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

from unittest.mock import MagicMock

from google.cloud.spanner_v1 import param_types
from sqlalchemy.testing import eq_
from sqlalchemy.testing.plugin.plugin_base import fixtures

from google.cloud.sqlalchemy_spanner.sqlalchemy_spanner import SpannerDialect


class TestSpannerDialect(fixtures.TestBase):
    def test_get_multi_indexes_excludes_search_indexes_sql(self):
        """Test that get_multi_indexes SQL query excludes SEARCH indexes."""
        dialect = SpannerDialect()
        connection = MagicMock()
        mock_snapshot = MagicMock()
        mock_snapshot.execute_sql.return_value = []
        connection.connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        )

        dialect.get_multi_indexes(connection)

        # Retrieve the SQL executed by snapshot
        executed_sql = mock_snapshot.execute_sql.call_args[0][0]
        assert "i.index_type != 'SEARCH'" in executed_sql

    def test_get_multi_indexes_handles_none_column_ordering(self):
        """Test get_multi_indexes with None column ordering."""
        dialect = SpannerDialect()
        connection = MagicMock()
        mock_snapshot = MagicMock()
        # Mock row: schema, table, index_name, columns,
        # is_unique, column_orderings, storing_columns
        mock_row = [
            "public",
            "my_table",
            "idx_search",
            ["col1"],
            False,
            [None],  # column_ordering is None
            [],
        ]
        mock_snapshot.execute_sql.return_value = [mock_row]
        connection.connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        )

        res = dialect.get_multi_indexes(connection)
        assert ("public", "my_table") in res
        index_info = res[("public", "my_table")][0]
        eq_(index_info["column_sorting"], {})

    def test_get_multi_indexes_handles_null_column_orderings_array(self):
        """Test get_multi_indexes when column_orderings array is None."""
        dialect = SpannerDialect()
        connection = MagicMock()
        mock_snapshot = MagicMock()
        mock_row = [
            "public",
            "my_table",
            "idx_test",
            ["col1"],
            False,
            None,  # row[5] is None
            [],
        ]
        mock_snapshot.execute_sql.return_value = [mock_row]
        connection.connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        )

        res = dialect.get_multi_indexes(connection)
        assert ("public", "my_table") in res
        index_info = res[("public", "my_table")][0]
        eq_(index_info["column_sorting"], {})

    def test_max_size_exported(self):
        """Test MAX_SIZE export and int_from_size helper behavior."""
        from google.cloud.sqlalchemy_spanner import MAX_SIZE
        from google.cloud.sqlalchemy_spanner.sqlalchemy_spanner import (
            _max_size,
            int_from_size,
        )

        eq_(MAX_SIZE, 2621440)
        eq_(_max_size, MAX_SIZE)
        eq_(SpannerDialect.max_size, MAX_SIZE)
        eq_(int_from_size("MAX"), 2621440)
        eq_(int_from_size("100"), 100)

    @staticmethod
    def _mock_connection(rows=None):
        connection = MagicMock()
        mock_snapshot = MagicMock()
        mock_snapshot.execute_sql.return_value = rows if rows is not None else []
        connection.connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        )
        return connection, mock_snapshot

    def test_get_columns_binds_names_as_query_parameters(self):
        """Table and schema names are bound as query parameters instead of
        being interpolated into the INFORMATION_SCHEMA query."""
        dialect = SpannerDialect()
        connection, mock_snapshot = self._mock_connection()

        dialect.get_columns(connection, table_name="t' OR '1'='1", schema="s")

        sql = mock_snapshot.execute_sql.call_args[0][0]
        kwargs = mock_snapshot.execute_sql.call_args[1]
        assert "col.table_name IN UNNEST(@filter_names)" in sql
        assert "col.table_schema = @schema AND" in sql
        assert "'1'='1'" not in sql
        eq_(kwargs["params"], {"schema": "s", "filter_names": ["t' OR '1'='1"]})
        eq_(
            kwargs["param_types"],
            {
                "schema": param_types.STRING,
                "filter_names": param_types.Array(param_types.STRING),
            },
        )

    def test_get_multi_columns_without_filter_names(self):
        """Without filter names no table filter is added and only the schema
        is bound as a query parameter."""
        dialect = SpannerDialect()
        connection, mock_snapshot = self._mock_connection()

        dialect.get_multi_columns(connection)

        sql = mock_snapshot.execute_sql.call_args[0][0]
        kwargs = mock_snapshot.execute_sql.call_args[1]
        assert "@filter_names" not in sql
        assert "col.table_schema = @schema AND" in sql
        eq_(kwargs["params"], {"schema": ""})
        eq_(kwargs["param_types"], {"schema": param_types.STRING})

    def test_has_table_binds_names_as_query_parameters(self):
        dialect = SpannerDialect()
        connection, mock_snapshot = self._mock_connection()

        eq_(dialect.has_table(connection, table_name='a" OR "1"="1'), False)

        sql = mock_snapshot.execute_sql.call_args[0][0]
        kwargs = mock_snapshot.execute_sql.call_args[1]
        assert "WHERE TABLE_SCHEMA=@schema AND TABLE_NAME=@table_name" in sql
        assert '"1"="1"' not in sql
        eq_(kwargs["params"], {"schema": "", "table_name": 'a" OR "1"="1'})
        eq_(
            kwargs["param_types"],
            {"schema": param_types.STRING, "table_name": param_types.STRING},
        )

    def test_get_view_definition_binds_names_as_query_parameters(self):
        dialect = SpannerDialect()
        connection, mock_snapshot = self._mock_connection(rows=[["SELECT 1"]])

        definition = dialect.get_view_definition(connection, view_name="v", schema="s")

        eq_(definition, "SELECT 1")
        sql = mock_snapshot.execute_sql.call_args[0][0]
        kwargs = mock_snapshot.execute_sql.call_args[1]
        assert "WHERE TABLE_SCHEMA=@schema AND TABLE_NAME=@view_name" in sql
        eq_(kwargs["params"], {"schema": "s", "view_name": "v"})
        eq_(
            kwargs["param_types"],
            {"schema": param_types.STRING, "view_name": param_types.STRING},
        )

    def test_has_sequence_binds_names_as_query_parameters(self):
        dialect = SpannerDialect()
        connection, mock_snapshot = self._mock_connection(rows=[[True]])

        eq_(dialect.has_sequence(connection, sequence_name="seq"), True)

        sql = mock_snapshot.execute_sql.call_args[0][0]
        kwargs = mock_snapshot.execute_sql.call_args[1]
        assert "WHERE NAME=@sequence_name" in sql
        assert "AND SCHEMA=@schema" in sql
        eq_(kwargs["params"], {"schema": "", "sequence_name": "seq"})
        eq_(
            kwargs["param_types"],
            {"schema": param_types.STRING, "sequence_name": param_types.STRING},
        )
