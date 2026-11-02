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
import sqlalchemy.types


@pytest.mark.parametrize(
    "table,schema,expect",
    [
        ("p.s.t", None, "p.s.t"),
        ("p.s.t", "p.s", "p.s.t"),
        # Why is a single schema name a project name when a table
        # dataset id is given?  I guess to provde a missing default.
        ("p.s.t", "p", "p.s.t"),
        ("s.t", "p", "p.s.t"),
        ("s.t", "p.s", "p.s.t"),
        ("s.t", None, "myproject.s.t"),
        ("t", None, "myproject.mydataset.t"),
        ("t", "s", "myproject.s.t"),
        ("t", "q.s", "q.s.t"),
    ],
)
def test__table_reference(faux_conn, table, schema, expect):
    assert (
        str(
            faux_conn.dialect._table_reference(
                schema, table, faux_conn.connection._client.project
            )
        )
        == expect
    )


@pytest.mark.parametrize(
    "table,table_project,schema,schema_project",
    [("p.s.t", "p", "q.s", "q"), ("p.s.t", "p", "q", "q")],
)
def test__table_reference_inconsistent_project(
    faux_conn, table, table_project, schema, schema_project
):
    with pytest.raises(
        ValueError,
        match=(
            f"project_id specified in schema and table_name disagree: "
            f"got {schema_project} in schema, and {table_project} in table_name"
        ),
    ):
        faux_conn.dialect._table_reference(
            schema, table, faux_conn.connection._client.project
        )


@pytest.mark.parametrize(
    "table,table_dataset,schema,schema_dataset",
    [("s.t", "s", "p.q", "q"), ("p.s.t", "s", "p.q", "q")],
)
def test__table_reference_inconsistent_dataset_id(
    faux_conn, table, table_dataset, schema, schema_dataset
):
    with pytest.raises(
        ValueError,
        match=(
            f"dataset_id specified in schema and table_name disagree: "
            f"got {schema_dataset} in schema, and {table_dataset} in table_name"
        ),
    ):
        faux_conn.dialect._table_reference(
            schema, table, faux_conn.connection._client.project
        )


@pytest.mark.parametrize("type_", ["view", "table"])
def test_get_table_names(faux_conn, type_):
    cursor = faux_conn.connection.cursor()
    cursor.execute("create view view1 as select 1")
    cursor.execute("create view view2 as select 2")
    cursor.execute("create table table1 (x INT64)")
    cursor.execute("create table table2 (x INT64)")
    assert sorted(getattr(faux_conn.dialect, f"get_{type_}_names")(faux_conn)) == [
        f"{type_}{d}" for d in "12"
    ]

    # once more with engine:
    assert sorted(
        getattr(faux_conn.dialect, f"get_{type_}_names")(faux_conn.engine)
    ) == [f"{type_}{d}" for d in "12"]


def test_get_schema_names(faux_conn):
    assert list(faux_conn.dialect.get_schema_names(faux_conn)) == [
        "mydataset",
        "yourdataset",
    ]
    # once more with engine:
    assert list(faux_conn.dialect.get_schema_names(faux_conn.engine)) == [
        "mydataset",
        "yourdataset",
    ]


def test_get_indexes(faux_conn):
    from google.cloud.bigquery.table import TimePartitioning

    cursor = faux_conn.connection.cursor()
    cursor.execute("create table foo (x INT64)")
    assert faux_conn.dialect.get_indexes(faux_conn, "foo") == []

    client = faux_conn.connection._client
    client.tables.foo.time_partitioning = TimePartitioning(field="tm")
    client.tables.foo.clustering_fields = ["user_email", "store_code"]

    assert faux_conn.dialect.get_indexes(faux_conn, "foo") == []


def test_no_table_pk_constraint(faux_conn):
    # BigQuery doesn't do that.
    assert faux_conn.dialect.get_pk_constraint(faux_conn, "foo") == (
        dict(constrained_columns=[])
    )


def test_no_table_foreign_keys(faux_conn):
    # BigQuery doesn't do that.
    assert faux_conn.dialect.get_foreign_keys(faux_conn, "foo") == []


def test_get_table_comment(faux_conn):
    cursor = faux_conn.connection.cursor()
    cursor.execute("create table foo (x INT64)")
    assert faux_conn.dialect.get_table_comment(faux_conn, "foo") == (dict(text=None))

    client = faux_conn.connection._client
    client.tables.foo.description = "special table"
    assert faux_conn.dialect.get_table_comment(faux_conn, "foo") == (
        dict(text="special table")
    )


@pytest.mark.parametrize(
    "btype,atype,extra",
    [
        ("STRING", sqlalchemy.types.String(), ()),
        ("STRING(42)", sqlalchemy.types.String(42), dict(max_length=42)),
        ("BYTES", sqlalchemy.types.BINARY(), ()),
        ("BYTES(42)", sqlalchemy.types.BINARY(42), dict(max_length=42)),
        ("INT64", sqlalchemy.types.Integer(), ()),
        ("FLOAT64", sqlalchemy.types.Float(), ()),
        ("NUMERIC", sqlalchemy.types.NUMERIC(), ()),
        ("NUMERIC(4)", sqlalchemy.types.NUMERIC(4), dict(precision=4)),
        ("NUMERIC(4, 2)", sqlalchemy.types.NUMERIC(4, 2), dict(precision=4, scale=2)),
        ("BIGNUMERIC", sqlalchemy.types.NUMERIC(), ()),
        ("BIGNUMERIC(42)", sqlalchemy.types.NUMERIC(42), dict(precision=42)),
        (
            "BIGNUMERIC(42, 2)",
            sqlalchemy.types.NUMERIC(42, 2),
            dict(precision=42, scale=2),
        ),
        ("BOOL", sqlalchemy.types.Boolean(), ()),
        ("TIMESTAMP", sqlalchemy.types.TIMESTAMP(), ()),
        ("DATE", sqlalchemy.types.DATE(), ()),
        ("TIME", sqlalchemy.types.TIME(), ()),
        ("DATETIME", sqlalchemy.types.DATETIME(), ()),
        ("THURSDAY", sqlalchemy.types.NullType, ()),
    ],
)
def test_get_table_columns(faux_conn, btype, atype, extra):
    cursor = faux_conn.connection.cursor()
    cursor.execute(f"create table foo (x {btype})")

    [col] = faux_conn.dialect.get_columns(faux_conn, "foo")
    col["type"] = str(col["type"])
    assert col == dict(
        {
            "comment": None,
            "default": None,
            "max_length": None,
            "name": "x",
            "nullable": True,
            "type": str(atype),
            "precision": None,
            "scale": None,
        },
        **(extra or {}),
    )


def test_get_table_columns_special_cases(faux_conn):
    from sqlalchemy_bigquery import STRUCT

    cursor = faux_conn.connection.cursor()
    cursor.execute("create table foo (s STRING, n INT64 not null, r RECORD)")
    client = faux_conn.connection._client
    client.tables.foo.columns.s.description = "a fine column"
    client.tables.foo.columns.s.mode = "REPEATED"
    client.tables.foo.columns.r.fields = (
        dict(name="i", type="INT64"),
        dict(name="f", type="FLOAT64"),
    )

    actual = faux_conn.dialect.get_columns(faux_conn, "foo")
    for a in actual:
        a["type"] = repr(a["type"])

    expected = [
        {
            "comment": "a fine column",
            "default": None,
            "name": "s",
            "nullable": True,
            "max_length": None,
            "precision": None,
            "scale": None,
            "type": repr(sqlalchemy.types.ARRAY(sqlalchemy.types.String())),
        },
        {
            "comment": None,
            "default": None,
            "name": "n",
            "nullable": False,
            "type": repr(sqlalchemy.types.Integer()),
            "max_length": None,
            "precision": None,
            "scale": None,
        },
        {
            "comment": None,
            "default": None,
            "name": "r",
            "nullable": True,
            "type": repr(
                STRUCT(i=sqlalchemy.types.Integer(), f=sqlalchemy.types.Float())
            ),
            "max_length": None,
            "precision": None,
            "scale": None,
        },
        {
            "comment": None,
            "default": None,
            "name": "r.i",
            "nullable": True,
            "type": repr(sqlalchemy.types.Integer()),
            "max_length": None,
            "precision": None,
            "scale": None,
        },
        {
            "comment": None,
            "default": None,
            "name": "r.f",
            "nullable": True,
            "type": repr(sqlalchemy.types.Float()),
            "max_length": None,
            "precision": None,
            "scale": None,
        },
    ]
    assert actual == expected


def test_has_table(faux_conn):
    cursor = faux_conn.connection.cursor()
    assert not faux_conn.dialect.has_table(faux_conn, "foo")
    cursor.execute("create table foo (s STRING)")
    assert faux_conn.dialect.has_table(faux_conn, "foo")
    # once more with engine:
    assert faux_conn.dialect.has_table(faux_conn.engine, "foo")


def test_bad_schema_argument(faux_conn):
    # with goofy schema name, to exercise some error handling
    with pytest.raises(ValueError, match=r"Did not understand schema: a\.b\.c"):
        faux_conn.dialect.has_table(faux_conn.engine, "foo", "a.b.c")


def test_bad_table_argument(faux_conn):
    # with goofy table name, to exercise some error handling
    with pytest.raises(ValueError, match=r"Did not understand table_name: a\.b\.c\.d"):
        faux_conn.dialect.has_table(faux_conn.engine, "a.b.c.d")
