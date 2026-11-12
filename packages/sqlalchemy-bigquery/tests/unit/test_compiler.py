# Copyright (c) 2021 The sqlalchemy-bigquery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import pytest
import sqlalchemy.exc
from sqlalchemy.sql.functions import cube, grouping_sets, rollup

from sqlalchemy_bigquery import SafeCast, safe_cast

from .conftest import setup_table, sqlalchemy_2_0_or_higher, sqlalchemy_before_2_0


@pytest.fixture
def table(faux_conn, metadata):
    # Fixture to create a sample table for testing

    table = setup_table(
        faux_conn,
        "table1",
        metadata,
        sqlalchemy.Column("foo", sqlalchemy.Integer),
        sqlalchemy.Column("bar", sqlalchemy.ARRAY(sqlalchemy.Integer)),
    )

    yield table

    table.drop(faux_conn)


def test_constraints_are_ignored(faux_conn, metadata):
    sqlalchemy.Table(
        "ref",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer),
    )
    sqlalchemy.Table(
        "some_table",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column(
            "ref_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("ref.id")
        ),
        sqlalchemy.UniqueConstraint("id", "ref_id", name="uix_1"),
    )
    metadata.create_all(faux_conn.engine)
    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `id` INT64 NOT NULL, `ref_id` INT64 )"
    )


def test_compile_column(faux_conn):
    table = setup_table(faux_conn, "t", sqlalchemy.Column("c", sqlalchemy.Integer))
    assert table.c.c.compile(faux_conn).string == "`c`"


def test_cant_compile_unnamed_column(faux_conn, metadata):
    with pytest.raises(
        sqlalchemy.exc.CompileError,
        match="Cannot compile Column object until its 'name' is assigned.",
    ):
        sqlalchemy.Column(sqlalchemy.Integer).compile(faux_conn)


def test_no_alias_for_known_tables(faux_conn, metadata):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/353
    table = setup_table(
        faux_conn,
        "table1",
        metadata,
        sqlalchemy.Column("foo", sqlalchemy.Integer),
        sqlalchemy.Column("bar", sqlalchemy.ARRAY(sqlalchemy.Integer)),
    )
    F = sqlalchemy.func
    q = sqlalchemy.select(table.c.foo).where(F.unnest(table.c.bar).column_valued() == 1)

    expected_sql = (
        "SELECT `table1`.`foo` \n"
        "FROM `table1`, unnest(`table1`.`bar`) AS `anon_1` \n"
        "WHERE `anon_1` = %(param_1:INT64)s"
    )
    found_sql = q.compile(faux_conn).string
    assert found_sql == expected_sql


def test_no_alias_for_known_tables_cte(faux_conn, metadata):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/368
    table = setup_table(
        faux_conn,
        "table1",
        metadata,
        sqlalchemy.Column("foo", sqlalchemy.Integer),
        sqlalchemy.Column("bars", sqlalchemy.ARRAY(sqlalchemy.Integer)),
    )
    F = sqlalchemy.func

    # Set up initiali query
    q = sqlalchemy.select(table.c.foo, F.unnest(table.c.bars).column_valued("bar"))

    expected_initial_sql = (
        "SELECT `table1`.`foo`, `bar` \nFROM `table1`, unnest(`table1`.`bars`) AS `bar`"
    )
    found_initial_sql = q.compile(faux_conn).string
    assert found_initial_sql == expected_initial_sql

    q = q.cte("cte")
    q = sqlalchemy.select(*q.columns)

    expected_cte_sql = (
        "WITH `cte` AS \n"
        "(SELECT `table1`.`foo` AS `foo`, `bar` \n"
        "FROM `table1`, unnest(`table1`.`bars`) AS `bar`)\n"
        " SELECT `cte`.`foo`, `cte`.`bar` \n"
        "FROM `cte`"
    )
    found_cte_sql = q.compile(faux_conn).string
    assert found_cte_sql == expected_cte_sql


def prepare_implicit_join_base_query(
    faux_conn, metadata, select_from_table2, old_syntax
):
    table1 = setup_table(
        faux_conn, "table1", metadata, sqlalchemy.Column("foo", sqlalchemy.Integer)
    )
    table2 = setup_table(
        faux_conn,
        "table2",
        metadata,
        sqlalchemy.Column("foos", sqlalchemy.ARRAY(sqlalchemy.Integer)),
        sqlalchemy.Column("bar", sqlalchemy.Integer),
    )
    F = sqlalchemy.func

    unnested_col_name = "unnested_foos"
    unnested_foos = F.unnest(table2.c.foos).alias(unnested_col_name)
    unnested_foo_col = sqlalchemy.Column(unnested_col_name)

    # Set up initial query
    cols = [table1.c.foo, table2.c.bar] if select_from_table2 else [table1.c.foo]
    q = sqlalchemy.select(cols) if old_syntax else sqlalchemy.select(*cols)
    q = q.select_from(unnested_foos.join(table1, table1.c.foo == unnested_foo_col))
    return q


# Test vendored method update_from_clause()
# from sqlalchemy_bigquery_vendored.sqlalchemy.postgresql.base.PGCompiler
def test_update_from_clause(faux_conn, metadata):
    table1 = setup_table(
        faux_conn,
        "table1",
        metadata,
        sqlalchemy.Column("foo", sqlalchemy.String),
        sqlalchemy.Column("bar", sqlalchemy.Integer),
    )
    table2 = setup_table(
        faux_conn,
        "table2",
        metadata,
        sqlalchemy.Column("foo", sqlalchemy.String),
        sqlalchemy.Column("bar", sqlalchemy.Integer),
    )

    stmt = (
        sqlalchemy.update(table1)
        .where(table1.c.foo == table2.c.foo)
        .where(table2.c.bar == 1)
        .values(bar=2)
    )
    expected_sql = "UPDATE `table1` SET `bar`=%(bar:INT64)s FROM `table2` WHERE `table1`.`foo` = `table2`.`foo` AND `table2`.`bar` = %(bar_1:INT64)s"
    found_sql = stmt.compile(faux_conn).string
    assert found_sql == expected_sql


@sqlalchemy_before_2_0
def test_no_implicit_join_asterix_for_inner_unnest_before_2_0(faux_conn, metadata):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/368
    q = prepare_implicit_join_base_query(faux_conn, metadata, True, False)
    expected_initial_sql = (
        "SELECT `table1`.`foo`, `table2`.`bar` \n"
        "FROM `table2`, unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`"
    )
    found_initial_sql = q.compile(faux_conn).string
    assert found_initial_sql == expected_initial_sql

    q = q.subquery()
    q = sqlalchemy.select("*").select_from(q)

    expected_outer_sql = (
        "SELECT * \n"
        "FROM (SELECT `table1`.`foo` AS `foo`, `table2`.`bar` AS `bar` \n"
        "FROM `table2`, unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`) AS `anon_1`"
    )
    found_outer_sql = q.compile(faux_conn).string
    assert found_outer_sql == expected_outer_sql


@sqlalchemy_2_0_or_higher
def test_no_implicit_join_asterix_for_inner_unnest(faux_conn, metadata):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/368
    q = prepare_implicit_join_base_query(faux_conn, metadata, True, False)
    expected_initial_sql = (
        "SELECT `table1`.`foo`, `table2`.`bar` \n"
        "FROM unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`, `table2`"
    )
    found_initial_sql = q.compile(faux_conn).string
    assert found_initial_sql == expected_initial_sql

    q = q.subquery()
    q = sqlalchemy.select("*").select_from(q)

    expected_outer_sql = (
        "SELECT * \n"
        "FROM (SELECT `table1`.`foo` AS `foo`, `table2`.`bar` AS `bar` \n"
        "FROM unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`, `table2`) AS `anon_1`"
    )
    found_outer_sql = q.compile(faux_conn).string
    assert found_outer_sql == expected_outer_sql


@sqlalchemy_before_2_0
def test_no_implicit_join_for_inner_unnest_before_2_0(faux_conn, metadata):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/368
    q = prepare_implicit_join_base_query(faux_conn, metadata, True, False)
    expected_initial_sql = (
        "SELECT `table1`.`foo`, `table2`.`bar` \n"
        "FROM `table2`, unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`"
    )
    found_initial_sql = q.compile(faux_conn).string
    assert found_initial_sql == expected_initial_sql

    q = q.subquery()
    q = sqlalchemy.select(q.c.foo).select_from(q)

    expected_outer_sql = (
        "SELECT `anon_1`.`foo` \n"
        "FROM (SELECT `table1`.`foo` AS `foo`, `table2`.`bar` AS `bar` \n"
        "FROM `table2`, unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`) AS `anon_1`"
    )
    found_outer_sql = q.compile(faux_conn).string
    assert found_outer_sql == expected_outer_sql


@sqlalchemy_2_0_or_higher
def test_no_implicit_join_for_inner_unnest(faux_conn, metadata):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/368
    q = prepare_implicit_join_base_query(faux_conn, metadata, True, False)
    expected_initial_sql = (
        "SELECT `table1`.`foo`, `table2`.`bar` \n"
        "FROM unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`, `table2`"
    )
    found_initial_sql = q.compile(faux_conn).string
    assert found_initial_sql == expected_initial_sql

    q = q.subquery()
    q = sqlalchemy.select(q.c.foo).select_from(q)

    expected_outer_sql = (
        "SELECT `anon_1`.`foo` \n"
        "FROM (SELECT `table1`.`foo` AS `foo`, `table2`.`bar` AS `bar` \n"
        "FROM unnest(`table2`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`, `table2`) AS `anon_1`"
    )
    found_outer_sql = q.compile(faux_conn).string
    assert found_outer_sql == expected_outer_sql


def test_no_implicit_join_asterix_for_inner_unnest_no_table2_column(
    faux_conn, metadata
):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/368
    q = prepare_implicit_join_base_query(faux_conn, metadata, False, False)
    expected_initial_sql = (
        "SELECT `table1`.`foo` \n"
        "FROM `table2` `table2_1`, unnest(`table2_1`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`"
    )
    found_initial_sql = q.compile(faux_conn).string
    assert found_initial_sql == expected_initial_sql

    q = q.subquery()
    q = sqlalchemy.select("*").select_from(q)

    expected_outer_sql = (
        "SELECT * \n"
        "FROM (SELECT `table1`.`foo` AS `foo` \n"
        "FROM `table2` `table2_1`, unnest(`table2_1`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`) AS `anon_1`"
    )
    found_outer_sql = q.compile(faux_conn).string
    assert found_outer_sql == expected_outer_sql


def test_no_implicit_join_for_inner_unnest_no_table2_column(faux_conn, metadata):
    # See: https://github.com/googleapis/python-bigquery-sqlalchemy/issues/368
    q = prepare_implicit_join_base_query(faux_conn, metadata, False, False)
    expected_initial_sql = (
        "SELECT `table1`.`foo` \n"
        "FROM `table2` `table2_1`, unnest(`table2_1`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`"
    )
    found_initial_sql = q.compile(faux_conn).string
    assert found_initial_sql == expected_initial_sql

    q = q.subquery()
    q = sqlalchemy.select(q.c.foo).select_from(q)

    expected_outer_sql = (
        "SELECT `anon_1`.`foo` \n"
        "FROM (SELECT `table1`.`foo` AS `foo` \n"
        "FROM `table2` `table2_1`, unnest(`table2_1`.`foos`) AS `unnested_foos` JOIN `table1` ON `table1`.`foo` = `unnested_foos`) AS `anon_1`"
    )
    found_outer_sql = q.compile(faux_conn).string
    assert found_outer_sql == expected_outer_sql


grouping_ops = (
    "grouping_op, grouping_op_func",
    [("GROUPING SETS", grouping_sets), ("ROLLUP", rollup), ("CUBE", cube)],
)


@pytest.mark.parametrize(*grouping_ops)
def test_grouping_ops_vs_single_column(faux_conn, table, grouping_op, grouping_op_func):
    # Tests each of the grouping ops against a single column

    q = sqlalchemy.select(table.c.foo).group_by(grouping_op_func(table.c.foo))
    found_sql = q.compile(faux_conn).string

    expected_sql = (
        f"SELECT `table1`.`foo` \nFROM `table1` GROUP BY {grouping_op}(`table1`.`foo`)"
    )

    assert found_sql == expected_sql


@pytest.mark.parametrize(*grouping_ops)
def test_grouping_ops_vs_multi_columns(faux_conn, table, grouping_op, grouping_op_func):
    # Tests each of the grouping ops against multiple columns

    q = sqlalchemy.select(table.c.foo, table.c.bar).group_by(
        grouping_op_func(table.c.foo, table.c.bar)
    )
    found_sql = q.compile(faux_conn).string

    expected_sql = (
        f"SELECT `table1`.`foo`, `table1`.`bar` \n"
        f"FROM `table1` GROUP BY {grouping_op}(`table1`.`foo`, `table1`.`bar`)"
    )

    assert found_sql == expected_sql


@pytest.mark.parametrize(*grouping_ops)
def test_grouping_op_with_grouping_op(faux_conn, table, grouping_op, grouping_op_func):
    # Tests multiple grouping ops in a single statement

    q = sqlalchemy.select(table.c.foo, table.c.bar).group_by(
        grouping_op_func(table.c.foo, table.c.bar), grouping_op_func(table.c.foo)
    )
    found_sql = q.compile(faux_conn).string

    expected_sql = (
        f"SELECT `table1`.`foo`, `table1`.`bar` \n"
        f"FROM `table1` GROUP BY {grouping_op}(`table1`.`foo`, `table1`.`bar`), {grouping_op}(`table1`.`foo`)"
    )

    assert found_sql == expected_sql


@pytest.mark.parametrize(*grouping_ops)
def test_grouping_ops_vs_group_by(faux_conn, table, grouping_op, grouping_op_func):
    # Tests grouping op against regular group by statement

    q = sqlalchemy.select(table.c.foo, table.c.bar).group_by(
        table.c.foo, grouping_op_func(table.c.bar)
    )
    found_sql = q.compile(faux_conn).string

    expected_sql = (
        f"SELECT `table1`.`foo`, `table1`.`bar` \n"
        f"FROM `table1` GROUP BY `table1`.`foo`, {grouping_op}(`table1`.`bar`)"
    )

    assert found_sql == expected_sql


@pytest.mark.parametrize(*grouping_ops)
def test_complex_grouping_ops_vs_nested_grouping_ops(
    faux_conn, table, grouping_op, grouping_op_func
):
    # Tests grouping ops nested within grouping ops

    q = sqlalchemy.select(table.c.foo, table.c.bar).group_by(
        grouping_sets(table.c.foo, grouping_op_func(table.c.bar))
    )
    found_sql = q.compile(faux_conn).string

    expected_sql = (
        f"SELECT `table1`.`foo`, `table1`.`bar` \n"
        f"FROM `table1` GROUP BY GROUPING SETS(`table1`.`foo`, {grouping_op}(`table1`.`bar`))"
    )

    assert found_sql == expected_sql


def test_label_compiler(faux_conn, metadata):
    class CustomLower(sqlalchemy.sql.functions.FunctionElement):
        name = "custom_lower"

    @sqlalchemy.ext.compiler.compiles(CustomLower)
    def compile_custom_intersect(element, compiler, **kwargs):
        if compiler.dialect.name != "bigquery":
            # We only test with the BigQuery dialect, so this should never happen.
            raise sqlalchemy.exc.CompileError(  # pragma: NO COVER
                f"custom_lower is not supported for dialect {compiler.dialect.name}"
            )

        clauses = list(element.clauses)
        field = compiler.process(clauses[0], **kwargs)
        return f"LOWER({field})"

    table1 = setup_table(
        faux_conn,
        "table1",
        metadata,
        sqlalchemy.Column("foo", sqlalchemy.String),
        sqlalchemy.Column("bar", sqlalchemy.Integer),
    )

    lower_foo = CustomLower(table1.c.foo).label("some_label")
    q = (
        sqlalchemy.select(lower_foo, sqlalchemy.func.max(table1.c.bar))
        .select_from(table1)
        .group_by(lower_foo)
    )
    expected_sql = (
        "SELECT LOWER(`table1`.`foo`) AS `some_label`, max(`table1`.`bar`) AS `max_1` \n"
        "FROM `table1` GROUP BY `some_label`"
    )

    found_sql = q.compile(faux_conn).string
    assert found_sql == expected_sql


def test_type_compiler_double_methods():
    from sqlalchemy_bigquery.base import BigQueryTypeCompiler

    assert BigQueryTypeCompiler.visit_DOUBLE == BigQueryTypeCompiler.visit_FLOAT
    assert (
        BigQueryTypeCompiler.visit_DOUBLE_PRECISION == BigQueryTypeCompiler.visit_FLOAT
    )


_double_types = [
    getattr(sqlalchemy, name)
    for name in ("DOUBLE", "DOUBLE_PRECISION", "Double")
    if hasattr(sqlalchemy, name)
]


@pytest.mark.skipif(
    not _double_types,
    reason="DOUBLE types not present in this SQLAlchemy version",
)
@pytest.mark.parametrize("type_cls", _double_types or [None])
def test_double_types_compile_to_float64(type_cls):
    import sqlalchemy_bigquery

    dialect = sqlalchemy_bigquery.BigQueryDialect()
    assert dialect.type_compiler.process(type_cls()) == "FLOAT64"


def test_float_literal_pyformat_bindparam():
    import sqlalchemy_bigquery

    dialect = sqlalchemy_bigquery.BigQueryDialect(paramstyle="pyformat")
    stmt = sqlalchemy.select(sqlalchemy.literal(15.7563))
    compiled = stmt.compile(dialect=dialect)
    assert "%(param_1:FLOAT64)s" in str(compiled)


def test_now_compiles_to_current_timestamp(faux_conn):
    # BigQuery has no NOW() function.
    stmt = sqlalchemy.select(sqlalchemy.func.now().label("ts"))
    found_sql = stmt.compile(faux_conn).string
    assert found_sql == "SELECT CURRENT_TIMESTAMP AS `ts`"


SAFE_CAST_TYPE_CASES = [
    pytest.param(sqlalchemy.Integer, "INT64", id="integer_class"),
    pytest.param(sqlalchemy.Integer(), "INT64", id="integer_instance"),
    pytest.param(sqlalchemy.String, "STRING", id="string"),
    pytest.param(sqlalchemy.Float, "FLOAT64", id="float"),
    pytest.param(sqlalchemy.Boolean, "BOOL", id="boolean"),
    pytest.param(sqlalchemy.Date, "DATE", id="date"),
    pytest.param(sqlalchemy.Numeric, "NUMERIC", id="numeric"),
]


@pytest.mark.parametrize("target_type,expected_bq_type", SAFE_CAST_TYPE_CASES)
def test_safe_cast_column(faux_conn, table, target_type, expected_bq_type):
    expr = safe_cast(table.c.foo, target_type)
    assert isinstance(expr, SafeCast)
    assert expr.inherit_cache is True
    expected_type_cls = (
        target_type if isinstance(target_type, type) else type(target_type)
    )
    assert isinstance(expr.type, expected_type_cls)

    stmt = sqlalchemy.select(expr.label("casted"))
    found_sql = stmt.compile(faux_conn).string
    expected_sql = (
        f"SELECT SAFE_CAST(`table1`.`foo` AS {expected_bq_type}) AS `casted` \n"
        "FROM `table1`"
    )
    assert found_sql == expected_sql


def test_safe_cast_literal(faux_conn):
    stmt = sqlalchemy.select(safe_cast(sqlalchemy.literal("123"), sqlalchemy.Integer))
    found_sql = stmt.compile(faux_conn, compile_kwargs={"literal_binds": True}).string
    assert found_sql == "SELECT SAFE_CAST('123' AS INT64) AS `anon_1`"


def test_safe_cast_null(faux_conn):
    stmt = sqlalchemy.select(
        safe_cast(sqlalchemy.null(), sqlalchemy.Integer).label("val")
    )
    found_sql = stmt.compile(faux_conn).string
    assert found_sql == "SELECT SAFE_CAST(NULL AS INT64) AS `val`"


def test_safe_cast_nested(faux_conn, table):
    inner = safe_cast(table.c.foo, sqlalchemy.String)
    outer = safe_cast(inner, sqlalchemy.Integer).label("casted")
    stmt = sqlalchemy.select(outer)
    found_sql = stmt.compile(faux_conn).string
    expected_sql = (
        "SELECT SAFE_CAST(SAFE_CAST(`table1`.`foo` AS STRING) AS INT64) AS `casted` \n"
        "FROM `table1`"
    )
    assert found_sql == expected_sql


@pytest.mark.skipif(
    not hasattr(sqlalchemy, "try_cast"),
    reason="sqlalchemy.try_cast requires SQLAlchemy 2.0.14 or higher",
)
@pytest.mark.parametrize("target_type,expected_bq_type", SAFE_CAST_TYPE_CASES)
def test_sqlalchemy_try_cast_compiles_to_safe_cast(
    faux_conn, table, target_type, expected_bq_type
):
    stmt = sqlalchemy.select(
        sqlalchemy.try_cast(table.c.foo, target_type).label("casted")
    )
    found_sql = stmt.compile(faux_conn).string
    expected_sql = (
        f"SELECT SAFE_CAST(`table1`.`foo` AS {expected_bq_type}) AS `casted` \n"
        "FROM `table1`"
    )
    assert found_sql == expected_sql


@pytest.fixture
def json_events_table(metadata):
    return sqlalchemy.Table(
        "events",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer),
        sqlalchemy.Column("payload", sqlalchemy.JSON),
        sqlalchemy.Column("k", sqlalchemy.String),
        sqlalchemy.Column("idx", sqlalchemy.Integer),
    )


def test_json_getitem_string_key(faux_conn, json_events_table):
    stmt = sqlalchemy.select(json_events_table.c.payload["key"].label("val"))
    compiled = stmt.compile(faux_conn)
    assert (
        compiled.string
        == "SELECT `events`.`payload`[%(payload_1:STRING)s] AS `val` \nFROM `events`"
    )
    assert compiled.construct_params() == {"payload_1": "key"}

    literal_sql = stmt.compile(faux_conn, compile_kwargs={"literal_binds": True}).string
    assert literal_sql == "SELECT `events`.`payload`['key'] AS `val` \nFROM `events`"


def test_json_getitem_integer_index(faux_conn, json_events_table):
    stmt = sqlalchemy.select(json_events_table.c.payload[0].label("val"))
    compiled = stmt.compile(faux_conn)
    assert (
        compiled.string
        == "SELECT `events`.`payload`[%(payload_1:INT64)s] AS `val` \nFROM `events`"
    )
    assert compiled.construct_params() == {"payload_1": 0}

    literal_sql = stmt.compile(faux_conn, compile_kwargs={"literal_binds": True}).string
    assert literal_sql == "SELECT `events`.`payload`[0] AS `val` \nFROM `events`"


def test_json_getitem_chained_subscripts(faux_conn, json_events_table):
    stmt = sqlalchemy.select(json_events_table.c.payload["a"][0]["b"].label("val"))
    compiled = stmt.compile(faux_conn)
    assert compiled.string in (
        "SELECT `events`.`payload`[%(payload_1:STRING)s]"
        "[%(param_1:INT64)s][%(param_2:STRING)s] AS `val` \n"
        "FROM `events`",
        "SELECT ((`events`.`payload`[%(payload_1:STRING)s])"
        "[%(param_1:INT64)s])[%(param_2:STRING)s] AS `val` \n"
        "FROM `events`",
    )
    assert compiled.construct_params() == {
        "payload_1": "a",
        "param_1": 0,
        "param_2": "b",
    }

    literal_sql = stmt.compile(faux_conn, compile_kwargs={"literal_binds": True}).string
    assert literal_sql in (
        "SELECT `events`.`payload`['a'][0]['b'] AS `val` \nFROM `events`",
        "SELECT ((`events`.`payload`['a'])[0])['b'] AS `val` \nFROM `events`",
    )


@pytest.mark.parametrize(
    "malicious_key",
    [
        "a` FROM `events`; DROP TABLE `x`; --",
        "a') FROM `events`; DROP TABLE `x`; --",
        'a" FROM `events`; --',
        "a\\') OR 1=1 --",
        "$[0]",
        "a.b[0]",
        "pct%s",
    ],
)
def test_json_getitem_sql_injection_prevented(
    faux_conn, json_events_table, malicious_key
):
    stmt = sqlalchemy.select(json_events_table.c.payload[malicious_key])
    compiled = stmt.compile(faux_conn)
    assert (
        compiled.string
        == "SELECT `events`.`payload`[%(payload_1:STRING)s] AS `anon_1` \nFROM `events`"
    )
    assert "DROP TABLE" not in compiled.string
    assert compiled.construct_params() == {"payload_1": malicious_key}

    literal_sql = stmt.compile(faux_conn, compile_kwargs={"literal_binds": True}).string
    expected_literal = repr(malicious_key.replace("%", "%%"))
    assert (
        literal_sql
        == f"SELECT `events`.`payload`[{expected_literal}] AS `anon_1` \nFROM `events`"
    )


def test_json_getitem_boolean_key(faux_conn, json_events_table):
    stmt = sqlalchemy.select(json_events_table.c.payload[True])
    compiled = stmt.compile(faux_conn)
    assert (
        compiled.string
        == "SELECT `events`.`payload`[%(payload_1:STRING)s] AS `anon_1` \nFROM `events`"
    )
    assert compiled.construct_params() == {"payload_1": "True"}

    literal_sql = stmt.compile(faux_conn, compile_kwargs={"literal_binds": True}).string
    assert (
        literal_sql == "SELECT `events`.`payload`['True'] AS `anon_1` \nFROM `events`"
    )


def test_json_getitem_bindparam_and_column_expressions(faux_conn, json_events_table):
    # Untyped bindparam (SQLAlchemy sets bindparam.type = JSONStrIndexType class)
    stmt_untyped = sqlalchemy.select(
        json_events_table.c.payload[sqlalchemy.bindparam("k")]
    )
    compiled_untyped = stmt_untyped.compile(faux_conn)
    assert (
        compiled_untyped.string
        == "SELECT `events`.`payload`[%(k:STRING)s] AS `anon_1` \nFROM `events`"
    )

    # JSONIndexType (base class)
    bp_idx = sqlalchemy.bindparam(
        "idx_k", "v", type_=sqlalchemy.sql.sqltypes.JSON.JSONIndexType()
    )
    assert (
        sqlalchemy.select(bp_idx).compile(faux_conn).string
        == "SELECT %(idx_k:STRING)s AS `anon_1`"
    )
    assert (
        sqlalchemy.select(bp_idx)
        .compile(faux_conn, compile_kwargs={"literal_binds": True})
        .string
        == "SELECT 'v' AS `anon_1`"
    )

    # Column expressions
    stmt_col = sqlalchemy.select(
        json_events_table.c.payload[json_events_table.c.k],
        json_events_table.c.payload[json_events_table.c.idx],
    )
    assert stmt_col.compile(faux_conn).string == (
        "SELECT `events`.`payload`[`events`.`k`] AS `anon_1`, "
        "`events`.`payload`[`events`.`idx`] AS `anon_2` \n"
        "FROM `events`"
    )


def test_json_path_getitem(faux_conn, json_events_table):
    stmt = sqlalchemy.select(
        json_events_table.c.payload[("a", 0, 'b"c\\d', True)].label("val")
    )
    compiled = stmt.compile(faux_conn)
    assert (
        compiled.string
        == "SELECT JSON_QUERY(`events`.`payload`, %(payload_1:STRING)s) AS `val` \nFROM `events`"
    )
    raw_params = compiled.construct_params()
    assert (
        compiled._bind_processors["payload_1"](raw_params["payload_1"])
        == '$."a"[0]."b\\"c\\\\d"."True"'
    )

    literal_sql = stmt.compile(faux_conn, compile_kwargs={"literal_binds": True}).string
    assert literal_sql == (
        "SELECT JSON_QUERY(`events`.`payload`, "
        + repr('$."a"[0]."b\\"c\\\\d"."True"')
        + ") AS `val` \nFROM `events`"
    )


def test_json_getitem_direct_operator_edge_cases(faux_conn, json_events_table):
    from sqlalchemy.sql import operators
    from sqlalchemy.sql.elements import BinaryExpression

    # 1. json_getitem_op with sequence value routes to json_path_getitem_op
    bp_seq = sqlalchemy.sql.elements.BindParameter(
        "p", value=["a", 1], type_=sqlalchemy.sql.sqltypes.NullType()
    )
    expr_seq = BinaryExpression(
        json_events_table.c.payload, bp_seq, operators.json_getitem_op
    )
    compiled_seq = sqlalchemy.select(expr_seq).compile(faux_conn)
    assert (
        compiled_seq.string
        == "SELECT JSON_QUERY(`events`.`payload`, %(p:STRING)s) AS `anon_1` \nFROM `events`"
    )
    raw_seq_params = compiled_seq.construct_params()
    assert compiled_seq._bind_processors["p"](raw_seq_params["p"]) == '$."a"[1]'

    # 2. json_getitem_op with NullType bindparam (int and str)
    bp_null_int = sqlalchemy.sql.elements.BindParameter(
        "p_int", value=2, type_=sqlalchemy.sql.sqltypes.NullType()
    )
    expr_null_int = BinaryExpression(
        json_events_table.c.payload, bp_null_int, operators.json_getitem_op
    )
    assert (
        sqlalchemy.select(expr_null_int).compile(faux_conn).string
        == "SELECT `events`.`payload`[%(p_int:INT64)s] AS `anon_1` \nFROM `events`"
    )

    bp_null_str = sqlalchemy.sql.elements.BindParameter(
        "p_str", value="k", type_=sqlalchemy.sql.sqltypes.NullType()
    )
    expr_null_str = BinaryExpression(
        json_events_table.c.payload, bp_null_str, operators.json_getitem_op
    )
    assert (
        sqlalchemy.select(expr_null_str).compile(faux_conn).string
        == "SELECT `events`.`payload`[%(p_str:STRING)s] AS `anon_1` \nFROM `events`"
    )

    # 3. json_path_getitem_op with non-JSONPathType BindParameter (str) and ColumnElement
    bp_str_path = sqlalchemy.bindparam("p_path", "$.a")
    expr_str_path = BinaryExpression(
        json_events_table.c.payload, bp_str_path, operators.json_path_getitem_op
    )
    assert (
        sqlalchemy.select(expr_str_path).compile(faux_conn).string
        == "SELECT JSON_QUERY(`events`.`payload`, %(p_path:STRING)s) AS `anon_1` \nFROM `events`"
    )

    expr_col_path = BinaryExpression(
        json_events_table.c.payload,
        json_events_table.c.k,
        operators.json_path_getitem_op,
    )
    assert (
        sqlalchemy.select(expr_col_path).compile(faux_conn).string
        == "SELECT JSON_QUERY(`events`.`payload`, `events`.`k`) AS `anon_1` \nFROM `events`"
    )

    # 4. Unbound bindparam with JSONPathType (both as class on .type and via subscript)
    bp_unbound_cls = sqlalchemy.bindparam("p_cls")
    bp_unbound_cls.type = sqlalchemy.sql.sqltypes.JSON.JSONPathType
    expr_unbound_cls = BinaryExpression(
        json_events_table.c.payload, bp_unbound_cls, operators.json_path_getitem_op
    )
    compiled_unbound_cls = sqlalchemy.select(expr_unbound_cls).compile(faux_conn)
    assert (
        compiled_unbound_cls.string
        == "SELECT JSON_QUERY(`events`.`payload`, %(p_cls:STRING)s) AS `anon_1` \nFROM `events`"
    )
    assert compiled_unbound_cls._bind_processors["p_cls"](("a", 0)) == '$."a"[0]'

    stmt_unbound_sub = sqlalchemy.select(
        json_events_table.c.payload[
            sqlalchemy.bindparam("p_sub", type_=sqlalchemy.JSON.JSONPathType)
        ]
    )
    compiled_unbound_sub = stmt_unbound_sub.compile(faux_conn)
    assert (
        compiled_unbound_sub.string
        == "SELECT JSON_QUERY(`events`.`payload`, %(p_sub:STRING)s) AS `anon_1` \nFROM `events`"
    )
    assert compiled_unbound_sub._bind_processors["p_sub"](("a", 0)) == '$."a"[0]'


def test_identifier_preparer_escape_unescape():
    import sqlalchemy_bigquery

    dialect_pyformat = sqlalchemy_bigquery.BigQueryDialect(paramstyle="pyformat")
    prep_pyformat = dialect_pyformat.identifier_preparer
    assert prep_pyformat.quote_identifier("a`b\\c%d") == "`a\\`b\\\\c%%d`"
    assert prep_pyformat._unescape_identifier("a\\`b\\\\c") == "a`b\\c"

    dialect_named = sqlalchemy_bigquery.BigQueryDialect(paramstyle="named")
    prep_named = dialect_named.identifier_preparer
    assert prep_named.quote_identifier("a`b\\c%d") == "`a\\`b\\\\c%d`"
