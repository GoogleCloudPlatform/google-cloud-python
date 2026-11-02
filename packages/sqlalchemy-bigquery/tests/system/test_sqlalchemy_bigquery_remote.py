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

# -*- coding: utf-8 -*-

import google.api_core.exceptions as core_exceptions
import pytest
import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.schema import MetaData, Table

EXPECTED_STATES = ["AL", "CA", "FL", "KY"]

REMOTE_TESTS = [
    ("bigquery-public-data", "bigquery-public-data.usa_names.usa_1910_2013"),
    ("bigquery-public-data", "usa_names.usa_1910_2013"),
    ("bigquery-public-data/usa_names", "bigquery-public-data.usa_names.usa_1910_2013"),
    ("bigquery-public-data/usa_names", "usa_1910_2013"),
    ("bigquery-public-data/usa_names", "usa_names.usa_1910_2013"),
]


@pytest.fixture(scope="session")
def engine_using_remote_dataset(bigquery_client):
    engine = create_engine(
        "bigquery://bigquery-public-data/usa_names",
        billing_project_id=bigquery_client.project,
        echo=True,
    )
    return engine


def test_remote_tables_list(engine_using_remote_dataset):
    tables = sqlalchemy.inspect(engine_using_remote_dataset).get_table_names()
    assert "usa_1910_2013" in tables


@pytest.mark.parametrize(
    ["urlpath", "table_name"],
    REMOTE_TESTS,
    ids=[f"test_engine_remote_sql_{x}" for x in range(len(REMOTE_TESTS))],
)
def test_engine_remote_sql(bigquery_client, urlpath, table_name):
    engine = create_engine(
        f"bigquery://{urlpath}", billing_project_id=bigquery_client.project, echo=True
    )
    with engine.connect() as conn:
        rows = conn.execute(
            sqlalchemy.text(f"SELECT DISTINCT(state) FROM `{table_name}`")
        ).fetchall()
        states = set(map(lambda row: row[0], rows))
        assert set(EXPECTED_STATES).issubset(states)


@pytest.mark.parametrize(
    ["urlpath", "table_name"],
    REMOTE_TESTS,
    ids=[f"test_engine_remote_table_{x}" for x in range(len(REMOTE_TESTS))],
)
def test_engine_remote_table(bigquery_client, urlpath, table_name):
    engine = create_engine(
        f"bigquery://{urlpath}", billing_project_id=bigquery_client.project, echo=True
    )
    with engine.connect() as conn:
        table = Table(table_name, MetaData(), autoload_with=engine)
        prepared = sqlalchemy.select(
            sqlalchemy.distinct(table.c.state)
        ).set_label_style(sqlalchemy.LABEL_STYLE_TABLENAME_PLUS_COL)
        rows = conn.execute(prepared).fetchall()
        states = set(map(lambda row: row[0], rows))
        assert set(EXPECTED_STATES).issubset(states)


@pytest.mark.parametrize(
    ["urlpath", "table_name"],
    REMOTE_TESTS,
    ids=[f"test_engine_remote_table_fail_{x}" for x in range(len(REMOTE_TESTS))],
)
def test_engine_remote_table_fail(urlpath, table_name):
    engine = create_engine(f"bigquery://{urlpath}", echo=True)
    with pytest.raises(
        (DatabaseError, core_exceptions.Forbidden), match="Access Denied"
    ):
        with engine.connect() as conn:
            table = Table(table_name, MetaData(), autoload_with=engine)
            prepared = sqlalchemy.select(
                sqlalchemy.distinct(table.c.state)
            ).set_label_style(sqlalchemy.LABEL_STYLE_TABLENAME_PLUS_COL)
            conn.execute(prepared).fetchall()
