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
import sqlite3

import pytest
import sqlalchemy
from google.cloud.bigquery import (
    PartitionRange,
    RangePartitioning,
    TimePartitioning,
    TimePartitioningType,
)

from .conftest import setup_table


def test_table_expiration_timestamp_dialect_option(faux_conn):
    setup_table(
        faux_conn,
        "some_table",
        sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
        bigquery_expiration_timestamp=datetime.datetime.fromisoformat(
            "2038-01-01T00:00:00+00:00"
        ),
    )

    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `createdAt` DATETIME )"
        " OPTIONS(expiration_timestamp=TIMESTAMP '2038-01-01 00:00:00+00:00')"
    )


def test_table_default_rounding_mode_dialect_option(faux_conn):
    setup_table(
        faux_conn,
        "some_table",
        sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
        bigquery_default_rounding_mode="ROUND_HALF_EVEN",
    )

    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `createdAt` DATETIME )"
        " OPTIONS(default_rounding_mode='ROUND_HALF_EVEN')"
    )


def test_table_with_json_columns(faux_conn):
    setup_table(
        faux_conn,
        "some_table",
        sqlalchemy.Column("some_stuff", sqlalchemy.JSON),
    )

    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `some_stuff` JSON )"
    )


def test_table_clustering_fields_dialect_option_no_such_column(faux_conn):
    with pytest.raises(sqlalchemy.exc.NoSuchColumnError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
            bigquery_clustering_fields=["country", "unknown"],
        )


def test_table_clustering_fields_dialect_option(faux_conn):
    # expect table creation to fail as SQLite does not support clustering
    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("country", sqlalchemy.Text),
            sqlalchemy.Column("town", sqlalchemy.Text),
            bigquery_clustering_fields=["country", "town"],
        )

    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `id` INT64, `country` STRING, `town` STRING )"
        " CLUSTER BY country, town"
    )


def test_table_clustering_fields_dialect_option_type_error(faux_conn):
    # expect TypeError when bigquery_clustering_fields is not a list
    with pytest.raises(TypeError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("country", sqlalchemy.Text),
            sqlalchemy.Column("town", sqlalchemy.Text),
            bigquery_clustering_fields="country, town",
        )


@pytest.mark.parametrize(
    "column_dtype,time_partitioning_type,func_name",
    [
        # DATE dtype
        pytest.param(
            sqlalchemy.DATE,
            TimePartitioningType.HOUR,  # Only MONTH/YEAR are permitted in BigQuery
            "DATE_TRUNC",
            marks=pytest.mark.xfail,
        ),
        pytest.param(
            sqlalchemy.DATE,
            TimePartitioningType.DAY,  # Only MONTH/YEAR are permitted in BigQuery
            "DATE_TRUNC",
            marks=pytest.mark.xfail,
        ),
        (sqlalchemy.DATE, TimePartitioningType.MONTH, "DATE_TRUNC"),
        (sqlalchemy.DATE, TimePartitioningType.YEAR, "DATE_TRUNC"),
        # TIMESTAMP dtype
        (sqlalchemy.TIMESTAMP, TimePartitioningType.HOUR, "TIMESTAMP_TRUNC"),
        (sqlalchemy.TIMESTAMP, TimePartitioningType.DAY, "TIMESTAMP_TRUNC"),
        (sqlalchemy.TIMESTAMP, TimePartitioningType.MONTH, "TIMESTAMP_TRUNC"),
        (sqlalchemy.TIMESTAMP, TimePartitioningType.YEAR, "TIMESTAMP_TRUNC"),
        # DATETIME dtype
        (sqlalchemy.DATETIME, TimePartitioningType.HOUR, "DATETIME_TRUNC"),
        (sqlalchemy.DATETIME, TimePartitioningType.DAY, "DATETIME_TRUNC"),
        (sqlalchemy.DATETIME, TimePartitioningType.MONTH, "DATETIME_TRUNC"),
        (sqlalchemy.DATETIME, TimePartitioningType.YEAR, "DATETIME_TRUNC"),
        # TimePartitioning.type_ == None
        (sqlalchemy.DATETIME, None, "DATETIME_TRUNC"),
    ],
)
def test_table_time_partitioning_given_field_and_type__dialect_options(
    faux_conn, column_dtype, time_partitioning_type, func_name
):
    """NOTE: Expect table creation to fail as SQLite does not support
    partitioned tables, despite that, we are still able to test the generation
    of SQL statements.

    Each parametrization ensures that the appropriate function is generated
    depending on whether the column datatype is DATE, TIMESTAMP, DATETIME and
    whether the TimePartitioningType is HOUR, DAY, MONTH, YEAR.

    `DATE_TRUNC` only returns a result if TimePartitioningType is DAY, MONTH,
    YEAR. BigQuery cannot partition on DATE by HOUR, so that is expected to
    xfail.

    A distinguishing characteristic of this test is we provide an argument to
    the TimePartitioning class for both field and type_.

    Special case: IF time_partitioning_type is None, the __init__() in the
    TimePartitioning class will overwrite it with TimePartitioningType.DAY as
    the default.
    """

    if time_partitioning_type is None:
        time_partitioning_type = TimePartitioningType.DAY

    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("createdAt", column_dtype),
            bigquery_time_partitioning=TimePartitioning(
                field="createdAt", type_=time_partitioning_type
            ),
        )

    result = " ".join(faux_conn.test_data["execute"][-1][0].strip().split())
    expected = (
        f"CREATE TABLE `some_table` ( `id` INT64, `createdAt` {column_dtype.__visit_name__} )"
        f" PARTITION BY {func_name}(createdAt, {time_partitioning_type})"
    )
    assert result == expected


def test_table_time_partitioning_given_field_but_no_type__dialect_option(faux_conn):
    """Expect table creation to fail as SQLite does not support partitioned tables

    Confirms that if the column datatype is DATETIME but no TimePartitioning.type_
    has been supplied, the system will default to DAY.

    A distinguishing characteristic of this test is we provide an argument to
    the TimePartitioning class for field but not type_.
    """

    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
            bigquery_time_partitioning=TimePartitioning(field="createdAt"),
        )
    result = " ".join(faux_conn.test_data["execute"][-1][0].strip().split())
    expected = (
        "CREATE TABLE `some_table` ( `id` INT64, `createdAt` DATETIME )"
        " PARTITION BY DATETIME_TRUNC(createdAt, DAY)"
    )
    assert result == expected


@pytest.mark.parametrize(
    "column_dtype,time_partitioning_type",
    [
        pytest.param(
            sqlalchemy.DATE,
            TimePartitioningType.HOUR,
            marks=pytest.mark.xfail,
        ),
        (sqlalchemy.DATE, TimePartitioningType.DAY),
        (sqlalchemy.DATE, TimePartitioningType.MONTH),
        (sqlalchemy.DATE, TimePartitioningType.YEAR),
    ],
)
def test_table_time_partitioning_given_type__but_no_field_dialect_option(
    faux_conn,
    column_dtype,
    time_partitioning_type,
):
    """NOTE: Expect table creation to fail as SQLite does not support
    partitioned tables, despite that, we are still able to test the generation
    of SQL statements

    If the `field` argument to TimePartitioning() is not provided, it defaults to
    None. That causes the pseudocolumn "_PARTITIONDATE" to be used by default as
    the column to partition by.

    _PARTITIONTIME only returns a result if TimePartitioningType is DAY, MONTH,
    YEAR. BigQuery cannot partition on _PARTITIONDATE by HOUR, so that is
    expected to xfail.

    A distinguishing characteristic of this test is we provide an argument to
    the TimePartitioning class for type_ but not field.
    """

    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table_2",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("createdAt", column_dtype),
            bigquery_time_partitioning=TimePartitioning(type_=time_partitioning_type),
        )

    # confirm that the following code creates the correct SQL string
    result = " ".join(faux_conn.test_data["execute"][-1][0].strip().split())

    # We need two versions of expected depending on whether we use _PARTITIONDATE
    expected = (
        f"CREATE TABLE `some_table_2` ( `id` INT64, `createdAt` {column_dtype.__visit_name__} )"
        f" PARTITION BY _PARTITIONDATE"
    )
    assert result == expected


def test_table_time_partitioning_dialect_option_partition_expiration_days(faux_conn):
    # expect table creation to fail as SQLite does not support partitioned tables
    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
            bigquery_time_partitioning=TimePartitioning(
                field="createdAt",
                type_="DAY",
                expiration_ms=21600000,
            ),
        )

    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `createdAt` DATETIME )"
        " PARTITION BY DATETIME_TRUNC(createdAt, DAY)"
        " OPTIONS(partition_expiration_days=0.25)"
    )


def test_table_partitioning_dialect_option_type_error(faux_conn):
    # expect TypeError when bigquery_time_partitioning is not a TimePartitioning object
    with pytest.raises(TypeError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
            bigquery_time_partitioning="DATE(createdAt)",
        )


def test_table_range_partitioning_dialect_option(faux_conn):
    # expect table creation to fail as SQLite does not support partitioned tables
    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("zipcode", sqlalchemy.INT),
            bigquery_range_partitioning=RangePartitioning(
                field="zipcode",
                range_=PartitionRange(
                    start=0,
                    end=100000,
                    interval=2,
                ),
            ),
        )

    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `id` INT64, `zipcode` INT64 )"
        " PARTITION BY RANGE_BUCKET(zipcode, GENERATE_ARRAY(0, 100000, 2))"
    )


def test_table_range_partitioning_dialect_option_no_field(faux_conn):
    # expect TypeError when bigquery_range_partitioning field is not defined
    with pytest.raises(
        AttributeError,
        match="bigquery_range_partitioning expects field to be defined",
    ):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("zipcode", sqlalchemy.FLOAT),
            bigquery_range_partitioning=RangePartitioning(
                range_=PartitionRange(
                    start=0,
                    end=100000,
                    interval=10,
                ),
            ),
        )


def test_table_range_partitioning_dialect_option_bad_column_type(faux_conn):
    # expect ValueError when bigquery_range_partitioning field is not an INTEGER
    with pytest.raises(
        ValueError,
        match=r"bigquery_range_partitioning expects field \(i\.e\. column\) data type to be INTEGER",
    ):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("zipcode", sqlalchemy.FLOAT),
            bigquery_range_partitioning=RangePartitioning(
                field="zipcode",
                range_=PartitionRange(
                    start=0,
                    end=100000,
                    interval=10,
                ),
            ),
        )


def test_table_range_partitioning_dialect_option_range_missing(faux_conn):
    # expect TypeError when bigquery_range_partitioning range start or end is missing
    with pytest.raises(
        TypeError,
        match="bigquery_range_partitioning expects range_.start to be an int, provided None",
    ):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("zipcode", sqlalchemy.INT),
            bigquery_range_partitioning=RangePartitioning(field="zipcode"),
        )

    with pytest.raises(
        TypeError,
        match="bigquery_range_partitioning expects range_.end to be an int, provided None",
    ):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("zipcode", sqlalchemy.INT),
            bigquery_range_partitioning=RangePartitioning(
                field="zipcode",
                range_=PartitionRange(start=1),
            ),
        )


def test_table_range_partitioning_dialect_option_default_interval(faux_conn):
    # expect table creation to fail as SQLite does not support partitioned tables
    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("zipcode", sqlalchemy.INT),
            bigquery_range_partitioning=RangePartitioning(
                field="zipcode",
                range_=PartitionRange(
                    start=0,
                    end=100000,
                ),
            ),
        )

    assert " ".join(faux_conn.test_data["execute"][-1][0].strip().split()) == (
        "CREATE TABLE `some_table` ( `id` INT64, `zipcode` INT64 )"
        " PARTITION BY RANGE_BUCKET(zipcode, GENERATE_ARRAY(0, 100000, 1))"
    )


def test_time_and_range_partitioning_mutually_exclusive(faux_conn):
    # expect ValueError when both bigquery_time_partitioning and bigquery_range_partitioning are provided
    with pytest.raises(ValueError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
            bigquery_range_partitioning=RangePartitioning(),
            bigquery_time_partitioning=TimePartitioning(),
        )


def test_table_all_dialect_option(faux_conn):
    # expect table creation to fail as SQLite does not support clustering and partitioned tables
    with pytest.raises(sqlite3.OperationalError):
        setup_table(
            faux_conn,
            "some_table",
            sqlalchemy.Column("id", sqlalchemy.Integer),
            sqlalchemy.Column("country", sqlalchemy.Text),
            sqlalchemy.Column("town", sqlalchemy.Text),
            sqlalchemy.Column("createdAt", sqlalchemy.DateTime),
            bigquery_expiration_timestamp=datetime.datetime.fromisoformat(
                "2038-01-01T00:00:00+00:00"
            ),
            bigquery_require_partition_filter=True,
            bigquery_default_rounding_mode="ROUND_HALF_EVEN",
            bigquery_clustering_fields=["country", "town"],
            bigquery_time_partitioning=TimePartitioning(
                field="createdAt",
                type_="DAY",
                expiration_ms=2592000000,
            ),
        )

    result = " ".join(faux_conn.test_data["execute"][-1][0].strip().split())
    expected = (
        "CREATE TABLE `some_table` ( `id` INT64, `country` STRING, `town` STRING, `createdAt` DATETIME )"
        " PARTITION BY DATETIME_TRUNC(createdAt, DAY)"
        " CLUSTER BY country, town"
        " OPTIONS(partition_expiration_days=30.0, expiration_timestamp=TIMESTAMP '2038-01-01 00:00:00+00:00', require_partition_filter=true, default_rounding_mode='ROUND_HALF_EVEN')"
    )

    assert result == expected


def test_validate_friendly_name_value_type(ddl_compiler):
    # expect option value to be transformed as a string expression

    assert ddl_compiler._validate_option_value_type("friendly_name", "Friendly name")

    with pytest.raises(TypeError):
        ddl_compiler._validate_option_value_type("friendly_name", 1983)


def test_validate_expiration_timestamp_value_type(ddl_compiler):
    # expect option value to be transformed as a timestamp expression

    assert ddl_compiler._validate_option_value_type(
        "expiration_timestamp",
        datetime.datetime.fromisoformat("2038-01-01T00:00:00+00:00"),
    )

    with pytest.raises(TypeError):
        ddl_compiler._validate_option_value_type("expiration_timestamp", "2038-01-01")


def test_validate_require_partition_filter_type(ddl_compiler):
    # expect option value to be transformed as a literal boolean

    assert ddl_compiler._validate_option_value_type("require_partition_filter", True)
    assert ddl_compiler._validate_option_value_type("require_partition_filter", False)

    with pytest.raises(TypeError):
        ddl_compiler._validate_option_value_type("require_partition_filter", "true")

    with pytest.raises(TypeError):
        ddl_compiler._validate_option_value_type("require_partition_filter", "false")


def test_validate_default_rounding_mode_type(ddl_compiler):
    # expect option value to be transformed as a string expression

    assert ddl_compiler._validate_option_value_type(
        "default_rounding_mode", "ROUND_HALF_EVEN"
    )

    with pytest.raises(TypeError):
        ddl_compiler._validate_option_value_type("default_rounding_mode", True)


def test_validate_unmapped_option_type(ddl_compiler):
    # expect option value with no typed specified in mapping to be transformed as a string expression

    assert ddl_compiler._validate_option_value_type("unknown", "DEFAULT_IS_STRING")


def test_process_str_option_value(ddl_compiler):
    # expect string to be transformed as a string expression
    assert ddl_compiler._process_option_value("Some text") == "'Some text'"


def test_process_datetime_value(ddl_compiler):
    # expect datetime object to be transformed as a timestamp expression
    assert (
        ddl_compiler._process_option_value(
            datetime.datetime.fromisoformat("2038-01-01T00:00:00+00:00")
        )
        == "TIMESTAMP '2038-01-01 00:00:00+00:00'"
    )


def test_process_int_option_value(ddl_compiler):
    # expect int to be unchanged
    assert ddl_compiler._process_option_value(90) == 90


def test_process_boolean_option_value(ddl_compiler):
    # expect boolean to be transformed as a literal boolean expression

    assert ddl_compiler._process_option_value(True) == "true"
    assert ddl_compiler._process_option_value(False) == "false"


def test_process_not_implementer_option_value(ddl_compiler):
    # expect to raise
    with pytest.raises(NotImplementedError):
        ddl_compiler._process_option_value(float)
