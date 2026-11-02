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

import contextlib
import sqlite3

import mock
import packaging.version
import pytest
import sqlalchemy
from sqlalchemy.sql.compiler import Compiled

from sqlalchemy_bigquery.base import BigQueryDDLCompiler, BigQueryDialect

from . import fauxdbi

sqlalchemy_version = packaging.version.parse(sqlalchemy.__version__)
sqlalchemy_before_2_0 = pytest.mark.skipif(
    sqlalchemy_version >= packaging.version.parse("2.0"),
    reason="requires sqlalchemy 1.3 or lower",
)
sqlalchemy_2_0_or_higher = pytest.mark.skipif(
    sqlalchemy_version < packaging.version.parse("2.0"),
    reason="requires sqlalchemy 1.4 or higher",
)


@pytest.fixture()
def faux_conn():
    test_data = dict(execute=[])
    connection = sqlite3.connect(":memory:")

    def factory(*args, **kw):
        conn = fauxdbi.Connection(connection, test_data, *args, **kw)
        return conn

    with mock.patch("google.cloud.bigquery.dbapi.connection.Connection", factory):
        # We want to bypass client creation. We don't need it and it requires creds.
        with mock.patch(
            "sqlalchemy_bigquery._helpers.create_bigquery_client", fauxdbi.FauxClient
        ):
            with mock.patch("google.auth.default", return_value=("authdb", "authproj")):
                engine = sqlalchemy.create_engine("bigquery://myproject/mydataset")
                conn = engine.connect()
                conn.test_data = test_data

                def ex(sql, *args, **kw):
                    with contextlib.closing(
                        conn.connection.connection.connection.cursor()
                    ) as cursor:
                        cursor.execute(sql, *args, **kw)

                conn.ex = ex

                ex("create table comments (key string primary key, comment string)")

                # Modernize faux_conn for SQLAlchemy 2.0+ by allowing it to execute
                # Compiled objects (common in this test suite)
                if sqlalchemy_version >= packaging.version.parse("2.0"):
                    original_execute = conn.execute

                    def execute(statement, *args, **kw):
                        if isinstance(statement, Compiled):
                            statement = sqlalchemy.text(str(statement))
                        return original_execute(statement, *args, **kw)

                    conn.execute = execute

                yield conn
                conn.close()


@pytest.fixture()
def last_query(faux_conn):
    def last_query(sql, params=None, offset=1):
        actual_sql, actual_params = faux_conn.test_data["execute"][-offset]
        assert actual_sql == sql
        if params is not None:
            assert actual_params == params

    return last_query


@pytest.fixture()
def metadata():
    return sqlalchemy.MetaData()


@pytest.fixture()
def ddl_compiler():
    return BigQueryDDLCompiler(BigQueryDialect(), None)


def setup_table(connection, name, *columns, initial_data=(), **kw):
    metadata = sqlalchemy.MetaData()
    table = sqlalchemy.Table(name, metadata, *columns, **kw)
    metadata.create_all(connection.engine)
    if initial_data:
        connection.execute(table.insert(), initial_data)
    return table
