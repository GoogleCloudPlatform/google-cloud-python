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

from sqlalchemy import Column, Integer, MetaData, Table
from sqlalchemy.schema import CreateTable
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

    def _compile_create_table(self, column):
        """Compile ``CREATE TABLE`` for a one-column primary key table."""
        table = Table("some_table", MetaData(), column)
        return str(CreateTable(table).compile(dialect=SpannerDialect()))

    def test_primary_key_reserved_word_is_quoted(self):
        """A reserved-word primary key column is quoted in the PRIMARY KEY clause."""
        ddl = self._compile_create_table(Column("from", Integer, primary_key=True))
        assert "PRIMARY KEY (`from`)" in ddl

    def test_primary_key_backtick_is_escaped(self):
        """A backtick in a primary key column name cannot terminate the identifier."""
        name = "id`) STORING (x); DROP TABLE t; --"
        ddl = self._compile_create_table(Column(name, Integer, primary_key=True))
        assert "PRIMARY KEY (`id\\`) STORING (x); DROP TABLE t; --`)" in ddl

    def test_primary_key_plain_name_is_unquoted(self):
        """A regular identifier is left unquoted, so existing DDL is unchanged."""
        ddl = self._compile_create_table(Column("user_id", Integer, primary_key=True))
        assert "PRIMARY KEY (user_id)" in ddl

    def test_preparer_escapes_backtick_and_backslash(self):
        """The identifier preparer backslash-escapes backticks and backslashes."""
        preparer = SpannerDialect().identifier_preparer
        eq_(preparer.quote("a`b"), "`a\\`b`")
        eq_(preparer.quote("a\\b"), "`a\\\\b`")

    def test_interleave_in_parent_string_is_quoted(self):
        """A string interleave parent is routed through the identifier preparer."""
        table = Table(
            "child",
            MetaData(),
            Column("id", Integer, primary_key=True),
            spanner_interleave_in="from",
        )
        ddl = str(CreateTable(table).compile(dialect=SpannerDialect()))
        assert "INTERLEAVE IN PARENT `from`" in ddl

    def test_interleave_in_parent_table_object_is_quoted(self):
        """A Table interleave parent is quoted by its name rather than repr."""
        parent = Table("from", MetaData(), Column("id", Integer, primary_key=True))
        table = Table(
            "child",
            MetaData(),
            Column("id", Integer, primary_key=True),
            spanner_interleave_in=parent,
        )
        ddl = str(CreateTable(table).compile(dialect=SpannerDialect()))
        assert "INTERLEAVE IN PARENT `from`" in ddl

    def test_interleave_in_parent_table_object_keeps_schema(self):
        """A Table interleave parent with a schema is emitted as schema.name."""
        parent = Table(
            "from",
            MetaData(),
            Column("id", Integer, primary_key=True),
            schema="sch",
        )
        table = Table(
            "child",
            MetaData(),
            Column("id", Integer, primary_key=True),
            spanner_interleave_in=parent,
        )
        ddl = str(CreateTable(table).compile(dialect=SpannerDialect()))
        assert "INTERLEAVE IN PARENT sch.`from`" in ddl

    def test_interleave_in_parent_dotted_string_quotes_each_part(self):
        """A schema-qualified string parent quotes the schema and name separately."""
        table = Table(
            "child",
            MetaData(),
            Column("id", Integer, primary_key=True),
            spanner_interleave_in="sch.from",
        )
        ddl = str(CreateTable(table).compile(dialect=SpannerDialect()))
        assert "INTERLEAVE IN PARENT sch.`from`" in ddl
