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

import packaging.version
import pytest
import sqlalchemy

import sqlalchemy_bigquery


def test_struct(engine, bigquery_dataset, metadata):
    conn = engine.connect()
    table = sqlalchemy.Table(
        f"{bigquery_dataset}.test_struct",
        metadata,
        sqlalchemy.Column(
            "person",
            sqlalchemy_bigquery.STRUCT(
                name=sqlalchemy.String,
                children=sqlalchemy.ARRAY(
                    sqlalchemy_bigquery.STRUCT(
                        name=sqlalchemy.String, bdate=sqlalchemy.DATE
                    )
                ),
            ),
        ),
    )
    metadata.create_all(engine)

    conn.execute(
        table.insert().values(
            person=dict(
                name="bob",
                children=[dict(name="billy", bdate=datetime.date(2020, 1, 1))],
            )
        )
    )

    assert list(conn.execute(sqlalchemy.select(table))) == [
        (
            {
                "name": "bob",
                "children": [{"name": "billy", "bdate": datetime.date(2020, 1, 1)}],
            },
        )
    ]
    assert list(conn.execute(sqlalchemy.select(table.c.person.NAME))) == [("bob",)]
    assert list(conn.execute(sqlalchemy.select(table.c.person.children[0]))) == [
        ({"name": "billy", "bdate": datetime.date(2020, 1, 1)},)
    ]
    assert list(conn.execute(sqlalchemy.select(table.c.person.children[0].bdate))) == [
        (datetime.date(2020, 1, 1),)
    ]
    assert list(
        conn.execute(
            sqlalchemy.select(table).where(table.c.person.children[0].NAME == "billy")
        )
    ) == [
        (
            {
                "name": "bob",
                "children": [{"name": "billy", "bdate": datetime.date(2020, 1, 1)}],
            },
        )
    ]
    assert (
        list(
            conn.execute(
                sqlalchemy.select(table).where(
                    table.c.person.children[0].NAME == "sally"
                )
            )
        )
        == []
    )


def test_complex_literals_pr_67(engine, bigquery_dataset, metadata):
    # https://github.com/googleapis/python-bigquery-sqlalchemy/pull/67

    # Simple select example:

    table_name = f"{bigquery_dataset}.test_comples_literals_pr_67"
    with engine.connect() as conn:
        conn.execute(
            sqlalchemy.text(
                f"""
            create table {table_name} as (
                select 'a' as id,
                struct(1 as x__count, 2 as y__count, 3 as z__count) as dimensions
                )
            """
            )
        )

    table = sqlalchemy.Table(table_name, metadata, autoload_with=engine)

    got = str(
        sqlalchemy.select((table.c.dimensions.x__count + 5).label("c")).compile(engine)
    )
    want = (
        f"SELECT `{table_name}`.`dimensions`.x__count + %(param_1:INT64)s AS `c` \n"
        f"FROM `{table_name}`"
    )

    assert got == want

    # Hopefully, "Example doing a pivot" is addressed by
    # test_unnest_and_struct_access_233 below :)


@pytest.mark.skipif(
    packaging.version.parse(sqlalchemy.__version__) < packaging.version.parse("1.4"),
    reason="unnest (and other table-valued-function) support required version 1.4",
)
def test_unnest_and_struct_access_233(engine, bigquery_dataset, metadata):
    # https://github.com/googleapis/python-bigquery-sqlalchemy/issues/233

    from sqlalchemy import ARRAY, Column, String, Table, func, select
    from sqlalchemy.orm import sessionmaker

    from sqlalchemy_bigquery import STRUCT

    conn = engine.connect()

    mock_table = Table(f"{bigquery_dataset}.Mock", metadata, Column("mock_id", String))
    another_mock_table = Table(
        f"{bigquery_dataset}.AnotherMock",
        metadata,
        Column("objects", ARRAY(STRUCT(object_id=String))),
    )
    metadata.create_all(engine)

    conn.execute(
        mock_table.insert(),
        [
            dict(mock_id="x"),
            dict(mock_id="y"),
            dict(mock_id="z"),
        ],
    )
    conn.execute(
        another_mock_table.insert(),
        dict(objects=[dict(object_id="x"), dict(object_id="y"), dict(object_id="q")]),
    )

    subquery = select(
        func.unnest(another_mock_table.c.objects).alias("another_mock_objects").column
    ).subquery()

    join = mock_table.join(
        subquery,
        subquery.c.another_mock_objects["object_id"] == mock_table.c.mock_id,
    )

    query = select(mock_table).select_from(join)

    got = str(query.compile(engine))
    want = (
        f"SELECT `{bigquery_dataset}.Mock`.`mock_id` \n"
        f"FROM `{bigquery_dataset}.Mock` "
        f"JOIN ("
        f"SELECT `another_mock_objects` \n"
        f"FROM "
        f"`{bigquery_dataset}.AnotherMock` `{bigquery_dataset}.AnotherMock_1`, "
        f"unnest(`{bigquery_dataset}.AnotherMock_1`.`objects`)"
        f" AS `another_mock_objects`"
        f") AS `anon_1` "
        f"ON "
        f"`anon_1`.`another_mock_objects`.object_id = "
        f"`{bigquery_dataset}.Mock`.`mock_id`"
    )
    assert got == want

    Session = sessionmaker(bind=engine)
    session = Session()
    results = sorted(session.execute(query))

    assert results == [("x",), ("y",)]
