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

import datetime
from decimal import Decimal

import pytest
import sqlalchemy
from sqlalchemy import not_

import sqlalchemy_bigquery

from .conftest import setup_table


def test_labels_not_forced(faux_conn):
    table = setup_table(faux_conn, "t", sqlalchemy.Column("id", sqlalchemy.Integer))
    result = faux_conn.execute(sqlalchemy.select(table.c.id))
    assert result.keys() == ["id"]  # Look! Just the column name!


def dtrepr(v):
    return f"{v.__class__.__name__.upper()} {repr(str(v))}"


@pytest.mark.parametrize(
    "type_,val,btype,vrep",
    [
        (sqlalchemy.String, "myString", "STRING", repr),
        (sqlalchemy.Text, "myText", "STRING", repr),
        (sqlalchemy.Unicode, "myUnicode", "STRING", repr),
        (sqlalchemy.UnicodeText, "myUnicodeText", "STRING", repr),
        (sqlalchemy.Integer, 424242, "INT64", repr),
        (sqlalchemy.SmallInteger, 42, "INT64", repr),
        (sqlalchemy.BigInteger, 1 << 60, "INT64", repr),
        (sqlalchemy.Numeric, Decimal(42), "NUMERIC", str),
        (sqlalchemy.Float, 4.2, "FLOAT64", repr),
        (
            sqlalchemy.DateTime,
            datetime.datetime(2021, 2, 3, 4, 5, 6, 123456),
            "DATETIME",
            dtrepr,
        ),
        (sqlalchemy.Date, datetime.date(2021, 2, 3), "DATE", dtrepr),
        (sqlalchemy.Time, datetime.time(4, 5, 6, 123456), "TIME", dtrepr),
        (sqlalchemy.Boolean, True, "BOOL", "true"),
        (sqlalchemy.REAL, 1.42, "FLOAT64", repr),
        (sqlalchemy.FLOAT, 0.42, "FLOAT64", repr),
        (sqlalchemy.NUMERIC, Decimal(4.25), "NUMERIC", str),
        (sqlalchemy.NUMERIC(39), Decimal(4.25), "BIGNUMERIC(39)", str),
        (sqlalchemy.NUMERIC(30, 10), Decimal(4.25), "BIGNUMERIC(30, 10)", str),
        (sqlalchemy.NUMERIC(39, 10), Decimal(4.25), "BIGNUMERIC(39, 10)", str),
        (sqlalchemy.DECIMAL, Decimal(0.25), "NUMERIC", str),
        (sqlalchemy.DECIMAL(39), Decimal(4.25), "BIGNUMERIC(39)", str),
        (sqlalchemy.DECIMAL(30, 10), Decimal(4.25), "BIGNUMERIC(30, 10)", str),
        (sqlalchemy.DECIMAL(39, 10), Decimal(4.25), "BIGNUMERIC(39, 10)", str),
        (sqlalchemy.INTEGER, 434343, "INT64", repr),
        (sqlalchemy.INT, 444444, "INT64", repr),
        (sqlalchemy.SMALLINT, 43, "INT64", repr),
        (sqlalchemy.BIGINT, 1 << 61, "INT64", repr),
        (
            sqlalchemy.TIMESTAMP,
            datetime.datetime(2021, 2, 3, 4, 5, 7, 123456),
            "TIMESTAMP",
            lambda v: f"TIMESTAMP {repr(str(v))}",
        ),
        (
            sqlalchemy.DATETIME,
            datetime.datetime(2021, 2, 3, 4, 5, 8, 123456),
            "DATETIME",
            dtrepr,
        ),
        (sqlalchemy.DATE, datetime.date(2021, 2, 4), "DATE", dtrepr),
        (sqlalchemy.TIME, datetime.time(4, 5, 7, 123456), "TIME", dtrepr),
        (sqlalchemy.TIME, datetime.time(4, 5, 7), "TIME", dtrepr),
        (sqlalchemy.TEXT, "myTEXT", "STRING", repr),
        (sqlalchemy.VARCHAR, "myVARCHAR", "STRING", repr),
        (sqlalchemy.NVARCHAR, "myNVARCHAR", "STRING", repr),
        (sqlalchemy.VARCHAR(42), "myVARCHAR", "STRING(42)", repr),
        (sqlalchemy.NVARCHAR(42), "myNVARCHAR", "STRING(42)", repr),
        (sqlalchemy.CHAR, "myCHAR", "STRING", repr),
        (sqlalchemy.NCHAR, "myNCHAR", "STRING", repr),
        (sqlalchemy.BINARY, b"myBINARY", "BYTES", repr),
        (sqlalchemy.VARBINARY, b"myVARBINARY", "BYTES", repr),
        (sqlalchemy.VARBINARY(42), b"myVARBINARY", "BYTES(42)", repr),
        (sqlalchemy.BOOLEAN, False, "BOOL", "false"),
        (sqlalchemy.ARRAY(sqlalchemy.Integer), [1, 2, 3], "ARRAY<INT64>", repr),
        (
            sqlalchemy.ARRAY(sqlalchemy.DATETIME),
            [
                datetime.datetime(2021, 2, 3, 4, 5, 6),
                datetime.datetime(2021, 2, 3, 4, 5, 7, 123456),
                datetime.datetime(2021, 2, 3, 4, 5, 8, 123456),
            ],
            "ARRAY<DATETIME>",
            lambda a: "[" + ", ".join(dtrepr(v) for v in a) + "]",
        ),
    ],
)
def test_typed_parameters(faux_conn, type_, val, btype, vrep):
    col_name = "foo"
    table = setup_table(faux_conn, "t", sqlalchemy.Column(col_name, type_))

    assert faux_conn.test_data["execute"].pop()[0].strip() == (
        f"CREATE TABLE `t` (\n\t`{col_name}` {btype}\n)"
    )

    faux_conn.execute(table.insert().values(**{col_name: val}))

    ptype = btype[: btype.index("(")] if "(" in btype else btype

    assert faux_conn.test_data["execute"][-1] == (
        f"INSERT INTO `t` (`{col_name}`) VALUES (%({col_name}:{ptype})s)",
        {col_name: val},
    )

    faux_conn.execute(
        table.insert()
        .values(**{col_name: sqlalchemy.literal(val, type_)})
        .compile(
            dialect=sqlalchemy_bigquery.BigQueryDialect(),
            compile_kwargs=dict(literal_binds=True),
        )
    )

    if not isinstance(vrep, str):
        vrep = vrep(val)

    assert faux_conn.test_data["execute"][-1] == (
        f"INSERT INTO `t` (`{col_name}`) VALUES ({vrep})",
        {},
    )

    assert list(map(list, faux_conn.execute(sqlalchemy.select(table)))) == [[val]] * 2
    assert faux_conn.test_data["execute"][-1][0] == "SELECT `t`.`foo` \nFROM `t`"

    assert (
        list(
            map(
                list,
                faux_conn.execute(
                    sqlalchemy.select(table.c.foo).set_label_style(
                        sqlalchemy.LABEL_STYLE_TABLENAME_PLUS_COL
                    )
                ),
            )
        )
        == [[val]] * 2
    )
    assert faux_conn.test_data["execute"][-1][0] == (
        "SELECT `t`.`foo` AS `t_foo` \nFROM `t`"
    )


def test_except(faux_conn):
    table = setup_table(
        faux_conn,
        "table",
        sqlalchemy.Column("id", sqlalchemy.Integer),
        sqlalchemy.Column("foo", sqlalchemy.Integer),
    )

    s1 = sqlalchemy.select(table.c.foo).where(table.c.id >= 2)
    s2 = sqlalchemy.select(table.c.foo).where(table.c.id >= 4)

    s3 = s1.except_(s2)

    result = s3.compile(faux_conn).string

    expected = (
        "SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_1:INT64)s EXCEPT DISTINCT SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_2:INT64)s"
    )
    assert result == expected


def test_intersect(faux_conn):
    table = setup_table(
        faux_conn,
        "table",
        sqlalchemy.Column("id", sqlalchemy.Integer),
        sqlalchemy.Column("foo", sqlalchemy.Integer),
    )

    s1 = sqlalchemy.select(table.c.foo).where(table.c.id >= 2)
    s2 = sqlalchemy.select(table.c.foo).where(table.c.id >= 4)

    s3 = s1.intersect(s2)

    result = s3.compile(faux_conn).string

    expected = (
        "SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_1:INT64)s INTERSECT DISTINCT SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_2:INT64)s"
    )
    assert result == expected


def test_union(faux_conn):
    table = setup_table(
        faux_conn,
        "table",
        sqlalchemy.Column("id", sqlalchemy.Integer),
        sqlalchemy.Column("foo", sqlalchemy.Integer),
    )

    s1 = sqlalchemy.select(table.c.foo).where(table.c.id >= 2)
    s2 = sqlalchemy.select(table.c.foo).where(table.c.id >= 4)

    s3 = s1.union(s2)

    result = s3.compile(faux_conn).string

    expected = (
        "SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_1:INT64)s UNION DISTINCT SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_2:INT64)s"
    )
    assert result == expected

    s4 = s1.union_all(s2)

    result = s4.compile(faux_conn).string

    expected = (
        "SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_1:INT64)s UNION ALL SELECT `table`.`foo` \n"
        "FROM `table` \n"
        "WHERE `table`.`id` >= %(id_2:INT64)s"
    )
    assert result == expected


def test_select_struct(faux_conn, metadata):
    from sqlalchemy_bigquery import STRUCT

    table = sqlalchemy.Table(
        "t",
        metadata,
        sqlalchemy.Column("x", STRUCT(y=sqlalchemy.Integer)),
    )

    faux_conn.ex("create table t (x RECORD)")
    faux_conn.ex("""insert into t values ('{"y": 1}')""")

    row = list(faux_conn.execute(sqlalchemy.select(table)))[0]
    # We expect the raw string, because sqlite3, unlike BigQuery
    # doesn't deserialize for us.
    assert row.x == '{"y": 1}'


def test_select_label_starts_w_digit(faux_conn):
    # Make sure label names are legal identifiers
    faux_conn.execute(sqlalchemy.select(sqlalchemy.literal(1).label("2foo")))
    assert (
        faux_conn.test_data["execute"][-1][0] == "SELECT %(param_1:INT64)s AS `_2foo`"
    )


def test_force_quote(faux_conn):
    from sqlalchemy.sql.elements import quoted_name

    table = setup_table(
        faux_conn,
        "t",
        sqlalchemy.Column(quoted_name("foo", True), sqlalchemy.Integer),
    )
    faux_conn.execute(sqlalchemy.select(table))
    assert faux_conn.test_data["execute"][-1][0] == ("SELECT `t`.`foo` \nFROM `t`")


def test_disable_quote(faux_conn):
    from sqlalchemy.sql.elements import quoted_name

    table = setup_table(
        faux_conn,
        "t",
        sqlalchemy.Column(quoted_name("foo", False), sqlalchemy.Integer),
    )
    faux_conn.execute(sqlalchemy.select(table))
    assert faux_conn.test_data["execute"][-1][0] == ("SELECT `t`.foo \nFROM `t`")


def test_select_in_lit(faux_conn, last_query):
    faux_conn.execute(sqlalchemy.select(sqlalchemy.literal(1).in_([1, 2, 3])))
    last_query(
        "SELECT %(param_1:INT64)s IN UNNEST(%(param_2:INT64)s) AS `anon_1`",
        {"param_1": 1, "param_2": [1, 2, 3]},
    )


def test_select_in_param(faux_conn, last_query):
    faux_conn.execute(
        sqlalchemy.select(
            sqlalchemy.literal(1).in_(sqlalchemy.bindparam("q", expanding=True))
        ),
        dict(q=[1, 2, 3]),
    )

    last_query(
        "SELECT %(param_1:INT64)s IN UNNEST(%(q:INT64)s) AS `anon_1`",
        {"param_1": 1, "q": [1, 2, 3]},
    )


def test_select_in_param1(faux_conn, last_query):
    faux_conn.execute(
        sqlalchemy.select(
            sqlalchemy.literal(1).in_(sqlalchemy.bindparam("q", expanding=True))
        ),
        dict(q=[1]),
    )
    last_query(
        "SELECT %(param_1:INT64)s IN UNNEST(%(q:INT64)s) AS `anon_1`",
        {"param_1": 1, "q": [1]},
    )


def test_select_in_param_empty(faux_conn, last_query):
    faux_conn.execute(
        sqlalchemy.select(
            sqlalchemy.literal(1).in_(sqlalchemy.bindparam("q", expanding=True))
        ),
        dict(q=[]),
    )
    last_query(
        "SELECT %(param_1:INT64)s IN UNNEST(%(q:INT64)s) AS `anon_1`",
        {"param_1": 1, "q": []},
    )


def test_select_notin_lit(faux_conn, last_query):
    faux_conn.execute(sqlalchemy.select(sqlalchemy.literal(0).notin_([1, 2, 3])))
    last_query(
        "SELECT (%(param_1:INT64)s NOT IN UNNEST(%(param_2:INT64)s)) AS `anon_1`",
        {"param_1": 0, "param_2": [1, 2, 3]},
    )


def test_select_notin_param(faux_conn, last_query):
    faux_conn.execute(
        sqlalchemy.select(
            sqlalchemy.literal(1).notin_(sqlalchemy.bindparam("q", expanding=True))
        ),
        dict(q=[1, 2, 3]),
    )
    last_query(
        "SELECT (%(param_1:INT64)s NOT IN UNNEST(%(q:INT64)s)) AS `anon_1`",
        {"param_1": 1, "q": [1, 2, 3]},
    )


def test_select_notin_param_empty(faux_conn, last_query):
    faux_conn.execute(
        sqlalchemy.select(
            sqlalchemy.literal(1).notin_(sqlalchemy.bindparam("q", expanding=True))
        ),
        dict(q=[]),
    )
    last_query(
        "SELECT (%(param_1:INT64)s NOT IN UNNEST(%(q:INT64)s)) AS `anon_1`",
        {"param_1": 1, "q": []},
    )


def test_literal_binds_kwarg_with_an_IN_operator_252(faux_conn):
    table = setup_table(
        faux_conn,
        "test",
        sqlalchemy.Column("val", sqlalchemy.Integer),
        initial_data=[dict(val=i) for i in range(3)],
    )
    q = sqlalchemy.select(table.c.val).where(table.c.val.in_([2]))

    def nstr(q):
        return " ".join(str(q).strip().split())

    assert (
        nstr(q.compile(faux_conn.engine, compile_kwargs={"literal_binds": True}))
        == "SELECT `test`.`val` FROM `test` WHERE `test`.`val` IN (2)"
    )


@pytest.mark.parametrize("alias", [True, False])
def test_unnest(faux_conn, alias):
    from sqlalchemy import String

    from sqlalchemy_bigquery import ARRAY

    table = setup_table(faux_conn, "t", sqlalchemy.Column("objects", ARRAY(String)))
    fcall = sqlalchemy.func.unnest(table.c.objects)
    if alias:
        query = fcall.alias("foo_objects").column
    else:
        query = fcall.column_valued("foo_objects")
    compiled = str(sqlalchemy.select(query).compile(faux_conn.engine))
    assert " ".join(compiled.strip().split()) == (
        "SELECT `foo_objects` FROM `t` `t_1`, unnest(`t_1`.`objects`) AS `foo_objects`"
    )


@pytest.mark.parametrize("alias", [True, False])
def test_table_valued_alias_w_multiple_references_to_the_same_table(faux_conn, alias):
    from sqlalchemy import String

    from sqlalchemy_bigquery import ARRAY

    table = setup_table(faux_conn, "t", sqlalchemy.Column("objects", ARRAY(String)))
    fcall = sqlalchemy.func.foo(table.c.objects, table.c.objects)
    if alias:
        query = fcall.alias("foo_objects").column
    else:
        query = fcall.column_valued("foo_objects")
    compiled = str(sqlalchemy.select(query).compile(faux_conn.engine))
    assert " ".join(compiled.strip().split()) == (
        "SELECT `foo_objects` "
        "FROM `t` `t_1`, foo(`t_1`.`objects`, `t_1`.`objects`) AS `foo_objects`"
    )


@pytest.mark.parametrize("alias", [True, False])
def test_unnest_w_no_table_references(faux_conn, alias):
    fcall = sqlalchemy.func.unnest([1, 2, 3])
    if alias:
        query = fcall.alias().column
    else:
        query = fcall.column_valued()
    compiled = str(sqlalchemy.select(query).compile(faux_conn.engine))
    assert " ".join(compiled.strip().split()) == (
        "SELECT `anon_1` FROM unnest(%(unnest_1)s) AS `anon_1`"
    )


def test_array_indexing(faux_conn, metadata):
    t = sqlalchemy.Table(
        "t",
        metadata,
        sqlalchemy.Column("a", sqlalchemy.ARRAY(sqlalchemy.String)),
    )
    got = str(sqlalchemy.select(t.c.a[0]).compile(faux_conn.engine))
    assert got == "SELECT `t`.`a`[OFFSET(%(a_1:INT64)s)] AS `anon_1` \nFROM `t`"


def test_visit_regexp_match_op_binary(faux_conn):
    table = setup_table(
        faux_conn,
        "table",
        sqlalchemy.Column("foo", sqlalchemy.String),
    )

    # NOTE: "sample_pattern" is not used in this test, we are not testing
    # the regex engine, we are testing the ability to create SQL
    sql_statement = table.c.foo.regexp_match("sample_pattern")
    result = sql_statement.compile(faux_conn).string
    expected = "REGEXP_CONTAINS(`table`.`foo`, %(foo_1:STRING)s)"

    assert result == expected


def test_visit_not_regexp_match_op_binary(faux_conn):
    table = setup_table(
        faux_conn,
        "table",
        sqlalchemy.Column("foo", sqlalchemy.String),
    )

    # NOTE: "sample_pattern" is not used in this test, we are not testing
    # the regex engine, we are testing the ability to create SQL
    sql_statement = not_(table.c.foo.regexp_match("sample_pattern"))
    result = sql_statement.compile(faux_conn).string
    expected = "NOT REGEXP_CONTAINS(`table`.`foo`, %(foo_1:STRING)s)"

    assert result == expected


def test_visit_mod_binary(faux_conn):
    table = setup_table(
        faux_conn,
        "table",
        sqlalchemy.Column("foo", sqlalchemy.Integer),
    )
    sql_statement = table.c.foo % 2
    result = sql_statement.compile(faux_conn).string
    expected = "MOD(`table`.`foo`, %(foo_1:INT64)s)"

    assert result == expected


def test_window_rows_between(faux_conn):
    """This is a replacement for the
    'test_window_rows_between'
    test in sqlalchemy's suite of compliance tests.

    Their test is expecting things in sorted order and BQ
    doesn't return sorted results the way they expect so that
    test fails.

    Note: that test only appears in:
    sqlalchemy/lib/sqlalchemy/testing/suite/test_select.py
    in version 2.0.32. It appears as though that test will be
    replaced with a similar but new test called:
    'test_window_rows_between_w_caching'
    due to the fact the rows are part of the cache key right now and
    not handled as binds.  This is related to sqlalchemy Issue #11515

    It is expected the new test will also have the same sorting failure.
    """

    table = setup_table(
        faux_conn,
        "table",
        sqlalchemy.Column("id", sqlalchemy.String),
        sqlalchemy.Column("col1", sqlalchemy.Integer),
        sqlalchemy.Column("col2", sqlalchemy.Integer),
    )

    stmt = sqlalchemy.select(
        sqlalchemy.func.max(table.c.col2).over(
            order_by=[table.c.col1],
            rows=(-5, 0),
        )
    )

    sql = stmt.compile(
        dialect=faux_conn.dialect,
        compile_kwargs={"literal_binds": True},
    )

    result = str(sql)
    expected = (
        "SELECT max(`table`.`col2`) "
        "OVER (ORDER BY `table`.`col1` "
        "ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS `anon_1` \n"  # newline character required here to match
        "FROM `table`"
    )
    assert result == expected
