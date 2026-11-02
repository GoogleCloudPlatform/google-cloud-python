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
import sqlalchemy


def test_engine_dataset_but_no_project(faux_conn):
    engine = sqlalchemy.create_engine("bigquery:///foo")
    conn = engine.connect()
    assert conn.connection._client.project == "authproj"


def test_engine_dataset_with_billing_project(faux_conn):
    engine = sqlalchemy.create_engine("bigquery://foo", billing_project_id="bar")
    conn = engine.connect()
    assert conn.connection._client.project == "bar"


def test_engine_no_dataset_no_project(faux_conn):
    engine = sqlalchemy.create_engine("bigquery://")
    conn = engine.connect()
    assert conn.connection._client.project == "authproj"


@pytest.mark.parametrize("arraysize", [0, None])
def test_set_arraysize_not_set_if_false(faux_conn, metadata, arraysize):
    engine = sqlalchemy.create_engine("bigquery://", arraysize=arraysize)
    sqlalchemy.Table("t", metadata, sqlalchemy.Column("c", sqlalchemy.Integer))
    conn = engine.connect()
    metadata.create_all(engine)

    # Because we gave a false array size, the array size wasn't set on the cursor:
    assert "arraysize" not in conn.connection.test_data


def test_set_arraysize(faux_conn, metadata):
    engine = sqlalchemy.create_engine("bigquery://", arraysize=42)
    sqlalchemy.Table("t", metadata, sqlalchemy.Column("c", sqlalchemy.Integer))
    conn = engine.connect()
    metadata.create_all(engine)

    # Because we gave a false array size, the array size wasn't set on the cursor:
    assert conn.connection.test_data["arraysize"] == 42


def test_arraysize_querystring_takes_precedence_over_default(faux_conn, metadata):
    arraysize = 42
    engine = sqlalchemy.create_engine(
        f"bigquery://myproject/mydataset?arraysize={arraysize}"
    )
    sqlalchemy.Table("t", metadata, sqlalchemy.Column("c", sqlalchemy.Integer))
    conn = engine.connect()
    metadata.create_all(engine)

    assert conn.connection.test_data["arraysize"] == arraysize


def test_dbapi_deprecated():
    from sqlalchemy_bigquery.base import BigQueryDialect

    assert BigQueryDialect.dbapi() is BigQueryDialect.import_dbapi()
