# !/usr/bin/env python
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
import decimal

import packaging.version
import pytest
import sqlalchemy
from google.cloud.bigquery import TimePartitioning
from sqlalchemy import (
    Column,
    MetaData,
    Table,
    case,
    create_engine,
    func,
    inspect,
    literal_column,
    not_,
    select,
    types,
)
from sqlalchemy.exc import NoSuchTableError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import expression

import sqlalchemy_bigquery

SQLALCHEMY_VERSION = packaging.version.parse(sqlalchemy.__version__)

ONE_ROW_CONTENTS = [
    588,
    datetime.datetime(2013, 10, 10, 11, 27, 16, tzinfo=datetime.timezone.utc),
    "W 52 St & 11 Ave",
    40.76727216,
    decimal.Decimal("40.76727216"),
    False,
    datetime.date(2013, 10, 10),
    datetime.datetime(2013, 10, 10, 11, 27, 16),
    datetime.time(11, 27, 16),
    b"\xef",
    {"name": "John Doe", "age": 100},
    {"record": {"name": "John Doe 2", "age": 200}},
    [1, 2, 3],
]
ONE_ROW_CONTENTS_EXPANDED = [
    588,
    datetime.datetime(2013, 10, 10, 11, 27, 16, tzinfo=datetime.timezone.utc),
    "W 52 St & 11 Ave",
    40.76727216,
    decimal.Decimal("40.76727216"),
    False,
    datetime.date(2013, 10, 10),
    datetime.datetime(2013, 10, 10, 11, 27, 16),
    datetime.time(11, 27, 16),
    b"\xef",
    {"name": "John Doe", "age": 100},
    "John Doe",
    100,
    {"record": {"name": "John Doe 2", "age": 200}},
    {"name": "John Doe 2", "age": 200},
    "John Doe 2",
    200,
    [1, 2, 3],
]
ONE_ROW_CONTENTS_DML = [
    588,
    datetime.datetime(2013, 10, 10, 11, 27, 16, tzinfo=datetime.timezone.utc),
    "test",
    40.76727216,
    decimal.Decimal("40.76727216"),
    False,
    datetime.date(2013, 10, 10),
    datetime.datetime(2013, 10, 10, 11, 27, 16),
    datetime.time(11, 27, 16),
    b"\xef",
]

SAMPLE_COLUMNS = [
    {"name": "integer", "type": types.Integer(), "nullable": True, "default": None},
    {"name": "timestamp", "type": types.TIMESTAMP(), "nullable": True, "default": None},
    {"name": "string", "type": types.String(), "nullable": True, "default": None},
    {"name": "float", "type": types.Float(), "nullable": True, "default": None},
    {"name": "numeric", "type": types.Numeric(), "nullable": True, "default": None},
    {"name": "boolean", "type": types.Boolean(), "nullable": True, "default": None},
    {"name": "date", "type": types.DATE(), "nullable": True, "default": None},
    {"name": "datetime", "type": types.DATETIME(), "nullable": True, "default": None},
    {"name": "time", "type": types.TIME(), "nullable": True, "default": None},
    {"name": "bytes", "type": types.BINARY(), "nullable": True, "default": None},
    {
        "name": "record",
        "type": sqlalchemy_bigquery.STRUCT(name=types.String, age=types.Integer),
        "nullable": True,
        "default": None,
        "comment": "In Standard SQL this data type is a STRUCT<name STRING, age INT64>.",
    },
    {"name": "record.name", "type": types.String(), "nullable": True, "default": None},
    {"name": "record.age", "type": types.Integer(), "nullable": True, "default": None},
    {
        "name": "nested_record",
        "type": sqlalchemy_bigquery.STRUCT(
            record=sqlalchemy_bigquery.STRUCT(name=types.String, age=types.Integer)
        ),
        "nullable": True,
        "default": None,
    },
    {
        "name": "nested_record.record",
        "type": sqlalchemy_bigquery.STRUCT(name=types.String, age=types.Integer),
        "nullable": True,
        "default": None,
    },
    {
        "name": "nested_record.record.name",
        "type": types.String(),
        "nullable": True,
        "default": None,
    },
    {
        "name": "nested_record.record.age",
        "type": types.Integer(),
        "nullable": True,
        "default": None,
    },
    {
        "name": "array",
        "type": types.ARRAY(types.Integer()),
        "nullable": True,
        "default": None,
    },
]


@pytest.fixture(scope="session")
def engine_using_test_dataset(bigquery_dataset):
    engine = create_engine(f"bigquery:///{bigquery_dataset}", echo=True)
    return engine


@pytest.fixture(scope="session")
def engine_with_location():
    engine = create_engine("bigquery://", echo=True, location="asia-northeast1")
    return engine


@pytest.fixture(scope="session")
def table(engine, bigquery_dataset):
    return Table(f"{bigquery_dataset}.sample", MetaData(), autoload_with=engine)


@pytest.fixture(scope="session")
def table_using_test_dataset(engine_using_test_dataset):
    return Table("sample", MetaData(), autoload_with=engine_using_test_dataset)


@pytest.fixture(scope="session")
def table_one_row(engine, bigquery_dataset):
    return Table(f"{bigquery_dataset}.sample_one_row", MetaData(), autoload_with=engine)


@pytest.fixture(scope="session")
def table_dml(engine, bigquery_empty_table):
    return Table(bigquery_empty_table, MetaData(), autoload_with=engine)


@pytest.fixture(scope="session")
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


@pytest.fixture(scope="session")
def session_using_test_dataset(engine_using_test_dataset):
    Session = sessionmaker(bind=engine_using_test_dataset)
    session = Session()
    return session


@pytest.fixture(scope="session")
def inspector(engine):
    return inspect(engine)


@pytest.fixture(scope="session")
def inspector_using_test_dataset(engine_using_test_dataset):
    return inspect(engine_using_test_dataset)


@pytest.fixture(scope="session")
def query():
    def query(table):
        col1 = literal_column("TIMESTAMP_TRUNC(timestamp, DAY)").label(
            "timestamp_label"
        )
        col2 = func.sum(table.c.integer)
        # Test rendering of nested labels. Full expression should render in SELECT, but
        # ORDER/GROUP BY should use label only.
        col3 = (
            func.sum(func.sum(table.c.integer.label("inner")).label("outer"))
            .over()
            .label("outer")
        )
        query = (
            select(col1, col2, col3)
            .where(col1 < "2017-01-01 00:00:00")
            .group_by(col1)
            .order_by(col2)
        )
        return query

    return query


def test_engine_with_dataset(engine_using_test_dataset, bigquery_dataset):
    with engine_using_test_dataset.connect() as conn:
        rows = conn.execute(sqlalchemy.text("SELECT * FROM sample_one_row")).fetchall()
        assert list(rows[0]) == ONE_ROW_CONTENTS
        table_one_row = Table(
            "sample_one_row", MetaData(), autoload_with=engine_using_test_dataset
        )
        rows = conn.execute(
            table_one_row.select().set_label_style(
                sqlalchemy.LABEL_STYLE_TABLENAME_PLUS_COL
            )
        ).fetchall()
        assert list(rows[0]) == ONE_ROW_CONTENTS_EXPANDED

        table_one_row = Table(
            f"{bigquery_dataset}.sample_one_row",
            MetaData(),
            autoload_with=engine_using_test_dataset,
        )
        rows = conn.execute(
            table_one_row.select().set_label_style(
                sqlalchemy.LABEL_STYLE_TABLENAME_PLUS_COL
            )
        ).fetchall()
        # verify that we are pulling from the specifically-named dataset,
        # instead of pulling from the default dataset of the engine (which
        # does not have this table at all)
        assert list(rows[0]) == ONE_ROW_CONTENTS_EXPANDED


def test_dataset_location(
    engine_with_location, bigquery_dataset, bigquery_regional_dataset
):
    with engine_with_location.connect() as conn:
        rows = conn.execute(
            sqlalchemy.text(f"SELECT * FROM {bigquery_regional_dataset}.sample_one_row")
        ).fetchall()
        assert list(rows[0]) == ONE_ROW_CONTENTS


def test_reflect_select(table, engine_using_test_dataset, table_using_test_dataset):
    for table in [table, table_using_test_dataset]:
        assert table.comment == "A sample table containing most data types."

        assert len(table.c) == 18
        assert isinstance(table.c.integer, Column)
        assert isinstance(table.c.integer.type, types.Integer)
        assert isinstance(table.c.timestamp.type, types.TIMESTAMP)
        assert isinstance(table.c.string.type, types.String)
        assert isinstance(table.c.float.type, types.Float)
        assert isinstance(table.c.boolean.type, types.Boolean)
        assert isinstance(table.c.date.type, types.DATE)
        assert isinstance(table.c.datetime.type, types.DATETIME)
        assert isinstance(table.c.time.type, types.TIME)
        assert isinstance(table.c.bytes.type, types.BINARY)
        assert isinstance(table.c["record.age"].type, types.Integer)
        assert isinstance(table.c["record.name"].type, types.String)
        assert isinstance(table.c["nested_record.record.age"].type, types.Integer)
        assert isinstance(table.c["nested_record.record.name"].type, types.String)
        assert isinstance(table.c.array.type, types.ARRAY)

        with engine_using_test_dataset.connect() as conn:
            rows = conn.execute(
                table.select().set_label_style(
                    sqlalchemy.LABEL_STYLE_TABLENAME_PLUS_COL
                )
            ).fetchall()
            assert len(rows) == 1000


def test_content_from_raw_queries(engine, bigquery_dataset):
    with engine.connect() as conn:
        rows = conn.execute(
            sqlalchemy.text(f"SELECT * FROM {bigquery_dataset}.sample_one_row")
        ).fetchall()
        assert list(rows[0]) == ONE_ROW_CONTENTS


def test_record_content_from_raw_queries(engine, bigquery_dataset):
    with engine.connect() as conn:
        rows = conn.execute(
            sqlalchemy.text(
                f"SELECT record.name FROM {bigquery_dataset}.sample_one_row"
            )
        ).fetchall()
        assert rows[0][0] == "John Doe"


def test_content_from_reflect(engine, table_one_row):
    with engine.connect() as conn:
        rows = conn.execute(
            table_one_row.select().set_label_style(
                sqlalchemy.LABEL_STYLE_TABLENAME_PLUS_COL
            )
        ).fetchall()
        assert list(rows[0]) == ONE_ROW_CONTENTS_EXPANDED


def test_unicode(engine, table_one_row):
    unicode_str = "白人看不懂"
    with engine.connect() as conn:
        returned_str = conn.execute(
            sqlalchemy.select(expression.bindparam("好", unicode_str)).select_from(
                table_one_row
            )
        ).scalar()
    assert returned_str == unicode_str


def test_reflect_select_shared_table(engine):
    one_row = Table(
        "bigquery-public-data.samples.natality", MetaData(), autoload_with=engine
    )
    with engine.connect() as conn:
        row = conn.execute(one_row.select().limit(1)).first()
        assert len(row) >= 1


def test_reflect_table_does_not_exist(engine, bigquery_dataset):
    with pytest.raises(NoSuchTableError):
        Table(
            f"{bigquery_dataset}.table_does_not_exist",
            MetaData(),
            autoload_with=engine,
        )

    assert (
        sqlalchemy.inspect(engine).has_table(f"{bigquery_dataset}.table_does_not_exist")
        is False
    )


def test_reflect_dataset_does_not_exist(engine):
    with pytest.raises(NoSuchTableError):
        Table(
            "dataset_does_not_exist.table_does_not_exist",
            MetaData(),
            autoload_with=engine,
        )


def test_tables_list(engine, engine_using_test_dataset, bigquery_dataset):
    tables = sqlalchemy.inspect(engine).get_table_names()
    assert f"{bigquery_dataset}.sample" in tables
    assert f"{bigquery_dataset}.sample_one_row" in tables
    assert f"{bigquery_dataset}.sample_view" not in tables

    tables = sqlalchemy.inspect(engine_using_test_dataset).get_table_names()
    assert "sample" in tables
    assert "sample_one_row" in tables
    assert "sample_view" not in tables


def test_group_by(session, table, session_using_test_dataset, table_using_test_dataset):
    """labels in SELECT clause should be correclty formatted (dots are replaced with underscores)"""
    for session, table in [
        (session, table),
        (session_using_test_dataset, table_using_test_dataset),
    ]:
        result = (
            session.query(table.c.string, func.count(table.c.integer))
            .group_by(table.c.string)
            .all()
        )
    assert len(result) > 0


def test_nested_labels(engine, table):
    col = table.c.integer
    exprs = [
        sqlalchemy.func.sum(
            sqlalchemy.func.sum(col.label("inner")).label("outer")
        ).over(),
        sqlalchemy.func.sum(
            sqlalchemy.case((sqlalchemy.literal(True), col.label("inner"))).label(
                "outer"
            )
        ),
        sqlalchemy.func.sum(
            sqlalchemy.func.sum(
                sqlalchemy.case((sqlalchemy.literal(True), col.label("inner"))).label(
                    "middle"
                )
            ).label("outer")
        ).over(),
    ]
    for expr in exprs:
        sql = str(expr.compile(engine))
        assert "inner" not in sql
        assert "middle" not in sql
        assert "outer" not in sql


def test_session_query(
    session, table, session_using_test_dataset, table_using_test_dataset
):
    for session, table in [
        (session, table),
        (session_using_test_dataset, table_using_test_dataset),
    ]:
        col_concat = func.concat(table.c.string).label("concat")
        result = (
            session.query(
                table.c.string,
                col_concat,
                func.avg(table.c.integer),
                func.sum(
                    case((table.c.boolean == sqlalchemy.literal(True), 1), else_=0)
                ),
            )
            .group_by(table.c.string, col_concat)
            .having(func.avg(table.c.integer) > 10)
        ).all()
        assert len(result) > 0


def test_labels(session, table, session_using_test_dataset, table_using_test_dataset):
    for session, table in [
        (session, table),
        (session_using_test_dataset, table_using_test_dataset),
    ]:
        result = session.query(
            # Valid
            table.c.string.label("abc"),
            # Invalid, needs to start with underscore
            table.c.string.label("123"),
            # Valid
            table.c.string.label("_123abc"),
            # Invalid, contains illegal characters
            table.c.string.label("!@$^*()\n{};/,.~abc"),
        )
        result = result.all()
        assert len(result) > 0


def test_custom_expression(
    engine, engine_using_test_dataset, table, table_using_test_dataset, query
):
    """GROUP BY clause should use labels instead of expressions"""
    q = query(table)
    with engine.connect() as conn:
        result = conn.execute(q).fetchall()
        assert len(result) > 0

    q = query(table_using_test_dataset)
    with engine_using_test_dataset.connect() as conn:
        result = conn.execute(q).fetchall()
        assert len(result) > 0


def test_compiled_query_literal_binds(
    engine, engine_using_test_dataset, table, table_using_test_dataset, query
):
    q = query(table)
    compiled = q.compile(engine, compile_kwargs={"literal_binds": True})
    with engine.connect() as conn:
        if hasattr(conn, "exec_driver_sql"):
            result = conn.exec_driver_sql(str(compiled)).fetchall()
        else:
            result = conn.execute(compiled).fetchall()
        assert len(result) > 0

    q = query(table_using_test_dataset)
    compiled = q.compile(
        engine_using_test_dataset, compile_kwargs={"literal_binds": True}
    )
    with engine_using_test_dataset.connect() as conn:
        if hasattr(conn, "exec_driver_sql"):
            result = conn.exec_driver_sql(str(compiled)).fetchall()
        else:
            result = conn.execute(compiled).fetchall()
        assert len(result) > 0


@pytest.mark.parametrize(
    ["column", "processed"],
    [
        (types.String(), "STRING"),
        (types.NUMERIC(), "NUMERIC"),
        (types.ARRAY(types.String), "ARRAY<STRING>"),
    ],
)
def test_compile_types(engine, column, processed):
    result = engine.dialect.type_compiler.process(column)
    assert result == processed


def test_joins(session, table, table_one_row):
    result = (
        session.query(table.c.string, func.count(table_one_row.c.integer))
        .join(table_one_row, table_one_row.c.string == table.c.string)
        .group_by(table.c.string)
        .all()
    )

    assert len(result) > 0


def test_querying_wildcard_tables(engine):
    table = Table(
        "bigquery-public-data.noaa_gsod.gsod*", MetaData(), autoload_with=engine
    )
    with engine.connect() as conn:
        rows = conn.execute(table.select().limit(1)).first()
        assert len(rows) > 0


def test_dml(engine, session, table_dml):
    """
    Test DML operations on a table with no data. This table is created
    in the `bigquery_empty_table` fixture.

    Modern versions of sqlalchemy does not really require setting the
    label style. This has been maintained to retain this test.
    """
    # test insert
    with engine.connect() as conn:
        conn.execute(table_dml.insert().values(ONE_ROW_CONTENTS_DML))
        result = conn.execute(
            table_dml.select().set_label_style(sqlalchemy.LABEL_STYLE_DEFAULT)
        ).fetchall()
        assert len(result) == 1

        # test update
        session.query(table_dml).filter(table_dml.c.string == "test").update(
            {"string": "updated_row"}, synchronize_session=False
        )
        updated_result = conn.execute(
            table_dml.select().set_label_style(sqlalchemy.LABEL_STYLE_DEFAULT)
        ).fetchone()
        assert updated_result._mapping[table_dml.c.string] == "updated_row"

        # test delete
        session.query(table_dml).filter(table_dml.c.string == "updated_row").delete(
            synchronize_session=False
        )
        result = conn.execute(
            table_dml.select().set_label_style(sqlalchemy.LABEL_STYLE_DEFAULT)
        ).fetchall()
        assert len(result) == 0


@pytest.mark.parametrize(
    "time_partitioning_field",
    [
        ("timestamp_c"),
        ("datetime_c"),
        # Fails because python-bigquery TimePartitioning.type_ defaults to "DAY", but
        # the DATE_TRUNC() function only allows "MONTH"/"YEAR"
        pytest.param("date_c", marks=[pytest.mark.xfail]),
    ],
)
def test_create_table(engine, bigquery_dataset, time_partitioning_field):
    meta = MetaData()
    Table(
        f"{bigquery_dataset}.test_table_create",
        meta,
        Column("integer_c", sqlalchemy.Integer, doc="column description"),
        Column("float_c", sqlalchemy.Float),
        Column("decimal_c", sqlalchemy.DECIMAL),
        Column("string_c", sqlalchemy.String),
        Column("text_c", sqlalchemy.Text),
        Column("boolean_c", sqlalchemy.Boolean),
        Column("timestamp_c", sqlalchemy.TIMESTAMP),
        Column("datetime_c", sqlalchemy.DATETIME),
        Column("date_c", sqlalchemy.DATE),
        Column("time_c", sqlalchemy.TIME),
        Column("binary_c", sqlalchemy.BINARY),
        bigquery_description="test table description",
        bigquery_friendly_name="test table name",
        bigquery_expiration_timestamp=datetime.datetime(2183, 3, 26, 8, 30, 0),
        bigquery_time_partitioning=TimePartitioning(
            field=time_partitioning_field,
            expiration_ms=1000 * 60 * 60 * 24 * 30,  # 30 days
        ),
        bigquery_require_partition_filter=True,
        bigquery_default_rounding_mode="ROUND_HALF_EVEN",
        bigquery_clustering_fields=["integer_c", "decimal_c"],
    )
    meta.create_all(engine)
    meta.drop_all(engine)

    # Test creating tables with declarative_base
    Base = declarative_base()

    class TableTest(Base):
        __tablename__ = f"{bigquery_dataset}.test_table_create2"
        integer_c = Column(sqlalchemy.Integer, primary_key=True)
        float_c = Column(sqlalchemy.Float)

    Base.metadata.create_all(engine)
    Base.metadata.drop_all(engine)


def test_schemas_names(inspector, inspector_using_test_dataset, bigquery_dataset):
    datasets = inspector.get_schema_names()
    assert f"{bigquery_dataset}" in datasets

    datasets = inspector_using_test_dataset.get_schema_names()
    assert f"{bigquery_dataset}" in datasets


def test_table_names_in_schema(
    inspector, inspector_using_test_dataset, bigquery_dataset
):
    tables = inspector.get_table_names(bigquery_dataset)
    assert f"{bigquery_dataset}.sample" in tables
    assert f"{bigquery_dataset}.sample_one_row" in tables
    assert f"{bigquery_dataset}.sample_dml_empty" in tables
    assert f"{bigquery_dataset}.sample_view" not in tables
    assert len(tables) == 3

    tables = inspector_using_test_dataset.get_table_names()
    assert "sample" in tables
    assert "sample_one_row" in tables
    assert "sample_dml_empty" in tables
    assert "sample_view" not in tables
    assert len(tables) == 3


def test_view_names(inspector, inspector_using_test_dataset, bigquery_dataset):
    view_names = inspector.get_view_names()
    assert f"{bigquery_dataset}.sample_view" in view_names
    assert f"{bigquery_dataset}.sample" not in view_names

    view_names = inspector_using_test_dataset.get_view_names()
    assert "sample_view" in view_names
    assert "sample" not in view_names


def test_get_indexes(inspector, inspector_using_test_dataset, bigquery_dataset):
    for _ in [f"{bigquery_dataset}.sample", f"{bigquery_dataset}.sample_one_row"]:
        indexes = inspector.get_indexes(f"{bigquery_dataset}.sample")
        assert len(indexes) == 0


def test_get_columns(inspector, inspector_using_test_dataset, bigquery_dataset):
    columns_without_schema = inspector.get_columns(f"{bigquery_dataset}.sample")
    columns_schema = inspector.get_columns("sample", bigquery_dataset)
    columns_queries = [columns_without_schema, columns_schema]
    for columns in columns_queries:
        for i, col in enumerate(columns):
            sample_col = SAMPLE_COLUMNS[i]
            assert col["comment"] == sample_col.get("comment")
            assert col["default"] == sample_col["default"]
            assert col["name"] == sample_col["name"]
            assert col["nullable"] == sample_col["nullable"]
            assert (
                col["type"].__class__.__name__ == sample_col["type"].__class__.__name__
            )

    columns_without_schema = inspector_using_test_dataset.get_columns("sample")
    columns_schema = inspector_using_test_dataset.get_columns(
        "sample", bigquery_dataset
    )
    columns_queries = [columns_without_schema, columns_schema]
    for columns in columns_queries:
        for i, col in enumerate(columns):
            sample_col = SAMPLE_COLUMNS[i]
            assert col["comment"] == sample_col.get("comment")
            assert col["default"] == sample_col["default"]
            assert col["name"] == sample_col["name"]
            assert col["nullable"] == sample_col["nullable"]
            assert (
                col["type"].__class__.__name__ == sample_col["type"].__class__.__name__
            )


@pytest.mark.parametrize(
    "provided_schema_name,provided_table_name,client_project",
    [
        ("dataset", "table", "project"),
        (None, "dataset.table", "project"),
        (None, "project.dataset.table", "other_project"),
        ("project", "dataset.table", "other_project"),
        ("project.dataset", "table", "other_project"),
    ],
)
def test_table_reference(
    dialect, provided_schema_name, provided_table_name, client_project
):
    ref = dialect._table_reference(
        provided_schema_name, provided_table_name, client_project
    )
    assert ref.table_id == "table"
    assert ref.dataset_id == "dataset"
    assert ref.project == "project"


@pytest.mark.parametrize(
    "provided_schema_name,provided_table_name,client_project",
    [
        ("project.dataset", "other_dataset.table", "project"),
        ("project.dataset", "other_project.dataset.table", "project"),
        ("project.dataset.something_else", "table", "project"),
        (None, "project.dataset.table.something_else", "project"),
    ],
)
def test_invalid_table_reference(
    dialect, provided_schema_name, provided_table_name, client_project
):
    with pytest.raises(ValueError):
        dialect._table_reference(
            provided_schema_name, provided_table_name, client_project
        )


def test_has_table(engine, engine_using_test_dataset, bigquery_dataset):
    assert sqlalchemy.inspect(engine).has_table("sample", bigquery_dataset) is True
    assert sqlalchemy.inspect(engine).has_table(f"{bigquery_dataset}.sample") is True
    assert (
        sqlalchemy.inspect(engine).has_table(f"{bigquery_dataset}.nonexistent_table")
        is False
    )
    assert (
        sqlalchemy.inspect(engine).has_table("nonexistent_table", "nonexistent_dataset")
        is False
    )

    assert sqlalchemy.inspect(engine_using_test_dataset).has_table("sample") is True
    assert (
        sqlalchemy.inspect(engine_using_test_dataset).has_table(
            "sample", bigquery_dataset
        )
        is True
    )
    assert (
        sqlalchemy.inspect(engine_using_test_dataset).has_table(
            f"{bigquery_dataset}.sample"
        )
        is True
    )

    assert (
        sqlalchemy.inspect(engine_using_test_dataset).has_table("sample_alt") is False
    )


def test_distinct_188(engine, bigquery_dataset):
    from sqlalchemy import Column, Integer
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    Base = declarative_base()

    class MyTable(Base):
        __tablename__ = f"{bigquery_dataset}.test_distinct_188"
        id = Column(Integer, primary_key=True)
        my_column = Column(Integer)

    MyTable.__table__.create(engine)

    Session = sessionmaker(bind=engine)
    db = Session()
    db.add_all([MyTable(id=i, my_column=i % 2) for i in range(9)])
    db.commit()

    expected = [(0,), (1,)]

    assert sorted(db.query(MyTable.my_column).distinct().all()) == expected
    assert (
        sorted(
            db.query(
                sqlalchemy.distinct(MyTable.my_column).label("just_a_random_label")
            ).all()
        )
        == expected
    )

    assert sorted(db.query(sqlalchemy.distinct(MyTable.my_column)).all()) == expected


@pytest.mark.skipif(
    packaging.version.parse(sqlalchemy.__version__) < packaging.version.parse("1.4"),
    reason="requires sqlalchemy 1.4 or higher",
)
def test_huge_in():
    engine = sqlalchemy.create_engine("bigquery://")
    conn = engine.connect()
    try:
        assert list(
            conn.execute(
                sqlalchemy.select(sqlalchemy.literal(-1).in_(list(range(99999))))
            )
        ) == [(False,)]
    except Exception:
        error = True
    else:
        error = False

    assert not error, "execution failed"


@pytest.mark.skipif(
    packaging.version.parse(sqlalchemy.__version__) < packaging.version.parse("1.4"),
    reason="unnest (and other table-valued-function) support required version 1.4",
)
def test_unnest(engine, bigquery_dataset):
    from sqlalchemy import String, func, select

    from sqlalchemy_bigquery import ARRAY

    conn = engine.connect()
    metadata = MetaData()
    table = Table(
        f"{bigquery_dataset}.test_unnest",
        metadata,
        Column("objects", ARRAY(String)),
    )
    metadata.create_all(engine)
    conn.execute(
        table.insert(), [dict(objects=["a", "b", "c"]), dict(objects=["x", "y"])]
    )
    query = select(func.unnest(table.c.objects).alias("foo_objects").column)
    compiled = str(query.compile(engine))
    assert " ".join(compiled.strip().split()) == (
        f"SELECT `foo_objects`"
        f" FROM"
        f" `{bigquery_dataset}.test_unnest` `{bigquery_dataset}.test_unnest_1`,"
        f" unnest(`{bigquery_dataset}.test_unnest_1`.`objects`) AS `foo_objects`"
    )
    assert sorted(r[0] for r in conn.execute(query)) == ["a", "b", "c", "x", "y"]


@pytest.mark.skipif(
    packaging.version.parse(sqlalchemy.__version__) < packaging.version.parse("1.4"),
    reason="unnest (and other table-valued-function) support required version 1.4",
)
def test_unnest_with_cte(engine, bigquery_dataset):
    from sqlalchemy import String, func, select

    from sqlalchemy_bigquery import ARRAY

    conn = engine.connect()
    metadata = MetaData()
    table_name = "test_unnest_with_cte"
    table = Table(
        f"{bigquery_dataset}.{table_name}",
        metadata,
        Column("foo", String),
        Column("bars", ARRAY(String)),
    )
    metadata.create_all(engine)
    conn.execute(
        table.insert(),
        [dict(foo="first", bars=["a", "b", "c"]), dict(foo="second", bars=["x", "y"])],
    )
    selectable = select(table.c).select_from(table).cte("cte")
    query = select(
        selectable.c.foo,
        func.unnest(selectable.c.bars).column_valued("unnest_bars"),
    ).select_from(selectable)
    compiled = str(query.compile(engine))
    assert " ".join(compiled.strip().split()) == (
        f"WITH `cte` "
        f"AS (SELECT `{bigquery_dataset}.{table_name}`.`foo` AS `foo`,"
        f" `{bigquery_dataset}.{table_name}`.`bars` AS `bars`"
        f" FROM `{bigquery_dataset}.{table_name}`) "
        f"SELECT `cte`.`foo`, `unnest_bars` "
        f"FROM `cte`, unnest(`cte`.`bars`) AS `unnest_bars`"
    )

    assert sorted(r for r in conn.execute(query)) == [
        ("first", "a"),
        ("first", "b"),
        ("first", "c"),
        ("second", "x"),
        ("second", "y"),
    ]


@pytest.mark.skipif(
    packaging.version.parse(sqlalchemy.__version__) < packaging.version.parse("1.4"),
    reason="regexp_match support requires version 1.4 or higher",
)
def test_regexp_match(session, table):
    results = (
        session.query(table.c.string)
        .where(table.c.string.regexp_match(".*52 St &.*"))
        .all()
    )

    number_of_52st_records = 12
    assert len(results) == number_of_52st_records


@pytest.mark.skipif(
    packaging.version.parse(sqlalchemy.__version__) < packaging.version.parse("1.4"),
    reason="regexp_match support requires version 1.4 or higher",
)
def test_not_regexp_match(session, table):
    results = (
        session.query(table.c.string)
        .where(not_(table.c.string.regexp_match("^Barrow St & Hudson St$")))
        .all()
    )

    number_of_non_barrowst_records = 993
    assert len(results) == number_of_non_barrowst_records
