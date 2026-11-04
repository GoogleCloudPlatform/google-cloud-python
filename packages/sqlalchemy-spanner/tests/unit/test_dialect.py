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

from types import SimpleNamespace
from unittest.mock import MagicMock

import sqlalchemy as sa
from sqlalchemy.sql.compiler import OPERATORS
from sqlalchemy.sql.operators import json_getitem_op
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

    def test_json_getitem_sql_injection_prevented(self):
        """Test that malicious JSON keys cannot inject SQL."""
        dialect = SpannerDialect()
        records = sa.Table("records", sa.MetaData(), sa.Column("data", sa.JSON))
        malicious_key = (
            'display") FROM records WHERE FALSE UNION ALL '
            "SELECT (SELECT secret FROM secrets) -- injected"
        )

        stmt = sa.select(records.c.data[malicious_key].as_string())

        # 1. Default parameterized compilation
        compiled = stmt.compile(dialect=dialect)
        eq_(
            compiled.string,
            "SELECT JSON_VALUE(records.data, :data_1) AS anon_1 \nFROM records",
        )
        assert "UNION ALL" not in compiled.string
        assert "secrets" not in compiled.string
        raw_params = compiled.construct_params()
        eq_(len(raw_params), 1)
        param_name, raw_val = next(iter(raw_params.items()))
        processed_val = compiled._bind_processors[param_name](raw_val)
        eq_(
            processed_val,
            '$."display\\") FROM records WHERE FALSE UNION ALL '
            'SELECT (SELECT secret FROM secrets) -- injected"',
        )

        # 2. Literal binds compilation (e.g., Computed columns or literal_binds=True)
        compiled_literal = stmt.compile(
            dialect=dialect, compile_kwargs={"literal_binds": True}
        )
        eq_(
            compiled_literal.string,
            'SELECT JSON_VALUE(records.data, "$.\\"display\\\\\\") '
            "FROM records WHERE FALSE UNION ALL "
            'SELECT (SELECT secret FROM secrets) -- injected\\"") AS anon_1 \n'
            "FROM records",
        )

        # 3. Direct call to _generate_generic_binary
        binary_expr = records.c.data[malicious_key]
        direct_compiler = dialect.statement_compiler(dialect, sa.select(records.c.data))
        direct_sql = direct_compiler._generate_generic_binary(
            binary_expr, OPERATORS[json_getitem_op]
        )
        eq_(direct_sql, "JSON_VALUE(records.data, :data_1)")

    def test_json_getitem_adversarial_keys_and_types(self):
        """Test JSON indexing with 0, empty string, backslashes, and quotes."""
        dialect = SpannerDialect(paramstyle="format")
        records = sa.Table("records", sa.MetaData(), sa.Column("data", sa.JSON))

        cases = [
            ("display", '$."display"', '"$.\\"display\\""'),
            (0, "$[0]", '"$[0]"'),
            (3, "$[3]", '"$[3]"'),
            (True, '$."True"', '"$.\\"True\\""'),
            (False, '$."False"', '"$.\\"False\\""'),
            ("", '$.""', '"$.\\"\\""'),
            ('a"b', '$."a\\"b"', '"$.\\"a\\\\\\"b\\""'),
            ("a'b", '$."a\'b"', '"$.\\"a\\\'b\\""'),
            ("a\\b", '$."a\\b"', '"$.\\"a\\\\b\\""'),
            ("a\\", '$."a\\\\"', '"$.\\"a\\\\\\\\\\""'),
            ("foo\\\n", '$."foo\\\n"', '"$.\\"foo\\\\\\n\\""'),
            ('a\\"b', '$."a\\\\\\"b"', '"$.\\"a\\\\\\\\\\\\\\"b\\""'),
            ('"""', '$."\\"\\"\\""', '"$.\\"\\\\\\"\\\\\\"\\\\\\"\\""'),
            (
                "a\nb\tc\rd\0e\x7f",
                '$."a\nb\tc\rd\0e\x7f"',
                '"$.\\"a\\nb\\tc\\rd\\u0000e\\u007f\\""',
            ),
            ("%s", '$."%s"', '"$.\\"%%s\\""'),
        ]

        for key, expected_bind, expected_literal in cases:
            stmt = sa.select(records.c.data[key].as_string())
            compiled = stmt.compile(dialect=dialect)
            eq_(
                compiled.string,
                "SELECT JSON_VALUE(records.data, %s) AS anon_1 \nFROM records",
            )
            param_name, raw_val = next(iter(compiled.construct_params().items()))
            processed = compiled._bind_processors[param_name](raw_val)
            eq_(processed, expected_bind)

            compiled_lit = stmt.compile(
                dialect=dialect, compile_kwargs={"literal_binds": True}
            )
            eq_(
                compiled_lit.string,
                f"SELECT JSON_VALUE(records.data, {expected_literal}) AS anon_1 \n"
                "FROM records",
            )

        # Also test non-ClauseElement fallback in _generate_generic_binary
        compiler = dialect.statement_compiler(dialect, sa.select(records.c.data))
        for right_obj in (
            SimpleNamespace(value='display") --'),
            MagicMock(value='display") --'),
        ):
            fake_binary = SimpleNamespace(
                left=records.c.data,
                right=right_obj,
                operator=json_getitem_op,
            )
            eq_(
                compiler._generate_generic_binary(
                    fake_binary, OPERATORS[json_getitem_op]
                ),
                'JSON_VALUE(records.data, "$.\\"display\\\\\\") --\\"")',
            )

    def test_json_path_getitem_compilation_and_escaping(self):
        """Test JSON path tuple indexing in parameterized and literal modes."""
        dialect = SpannerDialect(paramstyle="format")
        records = sa.Table("records", sa.MetaData(), sa.Column("data", sa.JSON))
        path = ("users", 0, True, 'first"name', "back\\")

        stmt = sa.select(records.c.data[path].as_string())
        compiled = stmt.compile(dialect=dialect)
        eq_(
            compiled.string,
            "SELECT JSON_VALUE(records.data, %s) AS anon_1 \nFROM records",
        )
        param_name, raw_val = next(iter(compiled.construct_params().items()))
        processed = compiled._bind_processors[param_name](raw_val)
        eq_(processed, '$."users"[0]."True"."first\\"name"."back\\\\"')

        compiled_lit = stmt.compile(
            dialect=dialect, compile_kwargs={"literal_binds": True}
        )
        eq_(
            compiled_lit.string,
            "SELECT JSON_VALUE(records.data, "
            '"$.\\"users\\"[0].\\"True\\".\\"first\\\\\\"name\\".\\"back\\\\\\\\\\"") '
            "AS anon_1 \nFROM records",
        )

    def test_json_getitem_statement_cache_and_bindparam_reuse(self):
        """Test statement caching and explicit bindparam reuse without mutation."""
        dialect = SpannerDialect()
        records = sa.Table(
            "records",
            sa.MetaData(),
            sa.Column("data", sa.JSON),
            sa.Column("name", sa.String),
        )
        cache = {}

        stmt1 = sa.select(records.c.data["key1"].as_string())
        stmt2 = sa.select(records.c.data["key2"].as_string())

        c1, params1, *_ = stmt1._compile_w_cache(
            dialect, compiled_cache=cache, column_keys=[]
        )
        c2, params2, *_ = stmt2._compile_w_cache(
            dialect, compiled_cache=cache, column_keys=[]
        )
        eq_(len(cache), 1)

        constructed1 = c1.construct_params(extracted_parameters=params1)
        constructed2 = c2.construct_params(extracted_parameters=params2)
        bname1, val1 = next(iter(constructed1.items()))
        bname2, val2 = next(iter(constructed2.items()))

        eq_(c1._bind_processors[bname1](val1), '$."key1"')
        eq_(c2._bind_processors[bname2](val2), '$."key2"')

        # Explicit valued bindparam reused across JSON and non-JSON expressions
        bp = sa.bindparam("k", "shared_key")
        bp_cache = {}
        stmt_bp1 = sa.select(records.c.data[bp].as_string())
        stmt_bp2 = sa.select(records.c.data[bp].as_string())
        c_bp1, p_bp1, *_ = stmt_bp1._compile_w_cache(
            dialect, compiled_cache=bp_cache, column_keys=[]
        )
        c_bp2, p_bp2, *_ = stmt_bp2._compile_w_cache(
            dialect, compiled_cache=bp_cache, column_keys=[]
        )
        eq_(len(bp_cache), 1)
        eq_(
            c_bp2._bind_processors["k"](
                c_bp2.construct_params(extracted_parameters=p_bp2)["k"]
            ),
            '$."shared_key"',
        )

        # Ensure bp.type was not mutated in-place for non-JSON comparisons
        stmt_name = sa.select(records.c.name).where(records.c.name == bp)
        c_name = stmt_name.compile(dialect=dialect)
        name_val = c_name.construct_params()["k"]
        if "k" in c_name._bind_processors:
            name_val = c_name._bind_processors["k"](name_val)
        eq_(name_val, "shared_key")

        # Explicit bindparam with tuple path (compile-time, cache hit, and runtime)
        path_cache = {}
        stmt_path = sa.select(
            records.c.data[sa.bindparam("p", value=("a", 0, "b"))].as_string()
        )
        stmt_untyped = sa.select(records.c.data[sa.bindparam("p")].as_string())
        c_path, p_path, *_ = stmt_path._compile_w_cache(
            dialect, compiled_cache=path_cache, column_keys=[]
        )
        c_untyped, _, *_ = stmt_untyped._compile_w_cache(
            dialect, compiled_cache=path_cache, column_keys=[]
        )
        eq_(len(path_cache), 1)
        eq_(
            c_path._bind_processors["p"](
                c_path.construct_params(extracted_parameters=p_path)["p"]
            ),
            '$."a"[0]."b"',
        )
        eq_(c_untyped._bind_processors["p"]("my_key"), '$."my_key"')
        eq_(c_untyped._bind_processors["p"](0), "$[0]")
        eq_(c_untyped._bind_processors["p"](("x", 1, "y")), '$."x"[1]."y"')

    def test_render_literal_value_triple_quote_and_trailing_escape(self):
        """Test render_literal_value escapes strings breaking raw triple quotes."""
        dialect = SpannerDialect(paramstyle="format")
        compiler = dialect.statement_compiler(dialect, sa.select(sa.literal("x")))

        eq_(
            compiler.render_literal_value('a"""b', sa.String()),
            '"a\\"\\"\\"b"',
        )
        eq_(
            compiler.render_literal_value('ends_with_quote"', sa.String()),
            '"ends_with_quote\\""',
        )
        eq_(
            compiler.render_literal_value("ends_with_backslash\\", sa.String()),
            '"ends_with_backslash\\\\"',
        )
        eq_(
            compiler.render_literal_value("has\rcarriage_return", sa.String()),
            '"has\\rcarriage_return"',
        )
        eq_(
            compiler.render_literal_value("has\x00null", sa.String()),
            '"has\\u0000null"',
        )
        eq_(
            compiler.render_literal_value('100% "quoted" mid', sa.String()),
            'r"""100%% "quoted" mid"""',
        )
