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

from sqlalchemy import types
from sqlalchemy.testing import eq_, expect_warnings
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

    def test_designate_type_known_types(self):
        """Test the mapping of Spanner types that the dialect knows."""
        dialect = SpannerDialect()
        eq_(dialect._designate_type("INT64"), types.BIGINT)
        string_type = dialect._designate_type("STRING(MAX)")
        assert isinstance(string_type, types.String)
        eq_(string_type.length, 2621440)
        eq_(dialect._designate_type("BYTES(10)").length, 10)
        array_type = dialect._designate_type("ARRAY<STRING(MAX)>")
        assert isinstance(array_type, types.ARRAY)
        assert isinstance(array_type.item_type, types.String)

    def test_designate_type_vector_columns(self):
        """Test vector columns are reflected as arrays of their element type."""
        dialect = SpannerDialect()
        for str_repr, item_type in (
            ("ARRAY<FLOAT32>(vector_length=>128)", types.REAL),
            ("ARRAY<FLOAT64>(vector_length=>3)", types.Float),
        ):
            col_type = dialect._designate_type(str_repr)
            assert isinstance(col_type, types.ARRAY)
            assert isinstance(col_type.item_type, item_type)

    def test_designate_type_unrecognized_types(self):
        """Test unrecognized types, like PROTO and ENUM, are reflected as NullType."""
        dialect = SpannerDialect()
        for str_repr in ("`my.package.Message`", "`my.package.Status`"):
            with expect_warnings(f"Did not recognize Spanner type '{str_repr}'"):
                col_type = dialect._designate_type(str_repr)
            assert isinstance(col_type, types.NullType)

        with expect_warnings("Did not recognize Spanner type '`my.package.Message`'"):
            col_type = dialect._designate_type("ARRAY<`my.package.Message`>")
        assert isinstance(col_type, types.ARRAY)
        assert isinstance(col_type.item_type, types.NullType)

        # An array type without its closing ">" also falls back to NullType.
        with expect_warnings("Did not recognize Spanner type 'ARRAY<FLOAT32'"):
            col_type = dialect._designate_type("ARRAY<FLOAT32")
        assert isinstance(col_type, types.NullType)

    def test_get_multi_columns_with_unrecognized_type(self):
        """Test a column of an unrecognized type doesn't break reflection."""
        dialect = SpannerDialect()
        connection = MagicMock()
        mock_snapshot = MagicMock()
        # Mock rows: schema, table, column, spanner_type, is_nullable,
        # generation_expression, column_default
        mock_snapshot.execute_sql.return_value = [
            ["", "my_table", "id", "INT64", "NO", None, None],
            ["", "my_table", "message", "`my.package.Message`", "YES", None, None],
        ]
        connection.connection.database.snapshot.return_value.__enter__.return_value = (
            mock_snapshot
        )

        with expect_warnings("Did not recognize Spanner type"):
            res = dialect.get_multi_columns(connection)

        columns = res[(None, "my_table")]
        eq_([column["name"] for column in columns], ["id", "message"])
        assert isinstance(columns[1]["type"], types.NullType)
