# Copyright (c) 2017 The sqlalchemy-bigquery Authors
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

import pytest
import sqlalchemy


def _test_struct():
    from sqlalchemy_bigquery import STRUCT

    return STRUCT(
        name=sqlalchemy.String,
        children=sqlalchemy.ARRAY(
            STRUCT(name=sqlalchemy.String, bdate=sqlalchemy.DATE)
        ),
    )


def test_struct_colspec():
    assert _test_struct().get_col_spec() == (
        "STRUCT<name STRING, children ARRAY<STRUCT<name STRING, bdate DATE>>>"
    )


def test_struct_repr():
    assert repr(_test_struct()) == (
        "STRUCT(name=String(), children=ARRAY(STRUCT(name=String(), bdate=DATE())))"
    )


def test_bind_processor():
    assert _test_struct().bind_processor(None) is dict


def _col():
    return sqlalchemy.Table(
        "t",
        sqlalchemy.MetaData(),
        sqlalchemy.Column("person", _test_struct()),
    ).c.person


@pytest.mark.parametrize(
    "expr,sql",
    [
        (_col()["name"], "`t`.`person`.name"),
        (_col()["Name"], "`t`.`person`.Name"),
        (_col().NAME, "`t`.`person`.NAME"),
        (_col().children, "`t`.`person`.children"),
        (
            # SQLAlchemy doesn't add the label in this case for some reason.
            # TODO: why?
            # https://github.com/googleapis/python-bigquery-sqlalchemy/issues/336
            _col().children[0].label("anon_1"),
            "(`t`.`person`.children)[OFFSET(%(param_1:INT64)s)]",
        ),
        (
            _col().children[0]["bdate"],
            "((`t`.`person`.children)[OFFSET(%(param_1:INT64)s)]).bdate",
        ),
        (
            _col().children[0].bdate,
            "((`t`.`person`.children)[OFFSET(%(param_1:INT64)s)]).bdate",
        ),
    ],
)
def test_struct_traversal_project(faux_conn, expr, sql):
    sql = f"SELECT {sql} AS `anon_1` \nFROM `t`"
    assert str(sqlalchemy.select(expr).compile(faux_conn.engine)) == sql


@pytest.mark.parametrize(
    "expr,sql",
    [
        (
            _col()["name"] == "bob",
            "`t`.`person`.name = %(param_1:STRING)s",
        ),
        (
            _col()["Name"] == "bob",
            "`t`.`person`.Name = %(param_1:STRING)s",
        ),
        (
            _col()["NAME"] == "bob",
            "`t`.`person`.NAME = %(param_1:STRING)s",
        ),
        (
            _col().children[0] == dict(name="foo", bdate=datetime.date(2020, 1, 1)),
            "(`t`.`person`.children)[OFFSET(%(param_1:INT64)s)]"
            " = %(param_2:STRUCT<name STRING, bdate DATE>)s",
        ),
        (
            _col().children[0] == dict(name="foo", bdate=datetime.date(2020, 1, 1)),
            "(`t`.`person`.children)[OFFSET(%(param_1:INT64)s)]"
            " = %(param_2:STRUCT<name STRING, bdate DATE>)s",
        ),
        (
            _col().children[0]["bdate"] == datetime.date(2021, 8, 30),
            "((`t`.`person`.children)[OFFSET(%(param_1:INT64)s)]).bdate"
            " = %(param_2:DATE)s",
        ),
        (
            _col().children[0].bdate == datetime.date(2021, 8, 30),
            "((`t`.`person`.children)[OFFSET(%(param_1:INT64)s)]).bdate"
            " = %(param_2:DATE)s",
        ),
    ],
)
def test_struct_traversal_filter(faux_conn, expr, sql, param=1):
    want = f"SELECT `t`.`person` \nFROM `t`, `t` \nWHERE {sql}"
    got = str(sqlalchemy.select(_col()).where(expr).compile(faux_conn.engine))
    assert got == want


def test_struct_insert_type_info(faux_conn, metadata):
    t = sqlalchemy.Table("t", metadata, sqlalchemy.Column("person", _test_struct()))
    got = str(
        t.insert()
        .values(
            person=dict(
                name="bob",
                children=[dict(name="billy", bdate=datetime.date(2020, 1, 1))],
            )
        )
        .compile(faux_conn.engine)
    )

    assert got == (
        "INSERT INTO `t` (`person`) VALUES (%(person:"
        "STRUCT<name STRING, children ARRAY<STRUCT<name STRING, bdate DATE>>>"
        ")s)"
    )


def test_struct_non_string_field_access(faux_conn):
    with pytest.raises(
        TypeError,
        match="STRUCT fields can only be accessed with strings field names, not 42",
    ):
        _col()[42]


def test_struct_bad_name(faux_conn):
    with pytest.raises(KeyError, match="42"):
        _col()["42"]
