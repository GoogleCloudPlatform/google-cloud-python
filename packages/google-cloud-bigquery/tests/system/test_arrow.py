# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""System tests for Arrow connector."""

import datetime
import json
import math
from typing import Optional
from unittest import mock
import uuid

import pyarrow
import pytest
from dateutil import relativedelta

from google.api_core import exceptions
from google.cloud import bigquery
from google.cloud.bigquery import enums


@pytest.mark.parametrize(
    ("max_results", "scalars_table_name"),
    (
        (None, "scalars_table"),  # Use BQ Storage API.
        (10, "scalars_table"),  # Use REST API.
        (None, "scalars_extreme_table"),  # Use BQ Storage API.
        (10, "scalars_extreme_table"),  # Use REST API.
    ),
)
def test_list_rows_nullable_scalars_dtypes(
    bigquery_client: bigquery.Client,
    scalars_table: str,
    scalars_extreme_table: str,
    max_results: Optional[int],
    scalars_table_name: str,
):
    table_id = scalars_table
    if scalars_table_name == "scalars_extreme_table":
        table_id = scalars_extreme_table

    # TODO(GH#836): Avoid INTERVAL columns until they are supported by the
    # BigQuery Storage API and pyarrow.
    schema = [
        bigquery.SchemaField("bool_col", enums.SqlTypeNames.BOOLEAN),
        bigquery.SchemaField("bignumeric_col", enums.SqlTypeNames.BIGNUMERIC),
        bigquery.SchemaField("bytes_col", enums.SqlTypeNames.BYTES),
        bigquery.SchemaField("date_col", enums.SqlTypeNames.DATE),
        bigquery.SchemaField("datetime_col", enums.SqlTypeNames.DATETIME),
        bigquery.SchemaField("float64_col", enums.SqlTypeNames.FLOAT64),
        bigquery.SchemaField("geography_col", enums.SqlTypeNames.GEOGRAPHY),
        bigquery.SchemaField("int64_col", enums.SqlTypeNames.INT64),
        bigquery.SchemaField("numeric_col", enums.SqlTypeNames.NUMERIC),
        bigquery.SchemaField("string_col", enums.SqlTypeNames.STRING),
        bigquery.SchemaField("time_col", enums.SqlTypeNames.TIME),
        bigquery.SchemaField("timestamp_col", enums.SqlTypeNames.TIMESTAMP),
    ]

    arrow_table = bigquery_client.list_rows(
        table_id,
        max_results=max_results,
        selected_fields=schema,
    ).to_arrow()

    schema = arrow_table.schema
    bignumeric_type = schema.field("bignumeric_col").type
    # 77th digit is partial.
    # https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#decimal_types
    assert bignumeric_type.precision in {76, 77}
    assert bignumeric_type.scale == 38

    bool_type = schema.field("bool_col").type
    assert bool_type.equals(pyarrow.bool_())

    bytes_type = schema.field("bytes_col").type
    assert bytes_type.equals(pyarrow.binary())

    date_type = schema.field("date_col").type
    assert date_type.equals(pyarrow.date32())

    datetime_type = schema.field("datetime_col").type
    assert datetime_type.unit == "us"
    assert datetime_type.tz is None

    float64_type = schema.field("float64_col").type
    assert float64_type.equals(pyarrow.float64())

    geography_type = schema.field("geography_col").type
    assert geography_type.equals(pyarrow.string())

    int64_type = schema.field("int64_col").type
    assert int64_type.equals(pyarrow.int64())

    numeric_type = schema.field("numeric_col").type
    assert numeric_type.precision == 38
    assert numeric_type.scale == 9

    string_type = schema.field("string_col").type
    assert string_type.equals(pyarrow.string())

    time_type = schema.field("time_col").type
    assert time_type.equals(pyarrow.time64("us"))

    timestamp_type = schema.field("timestamp_col").type
    assert timestamp_type.unit == "us"
    assert timestamp_type.tz is not None


@pytest.mark.parametrize("do_insert", [True, False])
def test_arrow_extension_types_same_for_storage_and_REST_APIs_894(
    dataset_client, test_table_name, do_insert
):
    types = dict(
        astring=("STRING", "'x'"),
        astring9=("STRING(9)", "'x'"),
        abytes=("BYTES", "b'x'"),
        abytes9=("BYTES(9)", "b'x'"),
        anumeric=("NUMERIC", "42"),
        anumeric9=("NUMERIC(9)", "42"),
        anumeric92=("NUMERIC(9,2)", "42"),
        abignumeric=("BIGNUMERIC", "42e30"),
        abignumeric49=("BIGNUMERIC(37)", "42e30"),
        abignumeric492=("BIGNUMERIC(37,2)", "42e30"),
        abool=("BOOL", "true"),
        adate=("DATE", "'2021-09-06'"),
        adatetime=("DATETIME", "'2021-09-06T09:57:26'"),
        ageography=("GEOGRAPHY", "ST_GEOGFROMTEXT('point(0 0)')"),
        # Can't get arrow data for interval :(
        # ainterval=('INTERVAL', "make_interval(1, 2, 3, 4, 5, 6)"),
        aint64=("INT64", "42"),
        afloat64=("FLOAT64", "42.0"),
        astruct=("STRUCT<v int64>", "struct(42)"),
        atime=("TIME", "'1:2:3'"),
        atimestamp=("TIMESTAMP", "'2021-09-06T09:57:26'"),
    )
    columns = ", ".join(f"{k} {t[0]}" for k, t in types.items())
    dataset_client.query(f"create table {test_table_name} ({columns})").result()
    if do_insert:
        names = list(types)
        values = ", ".join(types[name][1] for name in names)
        names = ", ".join(names)
        dataset_client.query(
            f"insert into {test_table_name} ({names}) values ({values})"
        ).result()
    at = dataset_client.query(f"select * from {test_table_name}").result().to_arrow()
    storage_api_metadata = {
        at.field(i).name: at.field(i).metadata for i in range(at.num_columns)
    }
    at = (
        dataset_client.query(f"select * from {test_table_name}")
        .result()
        .to_arrow(create_bqstorage_client=False)
    )
    rest_api_metadata = {
        at.field(i).name: at.field(i).metadata for i in range(at.num_columns)
    }

    assert rest_api_metadata == storage_api_metadata
    assert rest_api_metadata["adatetime"] == {
        b"ARROW:extension:name": b"google:sqlType:datetime"
    }
    assert rest_api_metadata["ageography"] == {
        b"ARROW:extension:name": b"google:sqlType:geography",
        b"ARROW:extension:metadata": b'{"encoding": "WKT"}',
    }


def test_list_rows_range_csv(
    bigquery_client: bigquery.Client,
    scalars_table_csv: str,
):
    table_id = scalars_table_csv

    schema = [
        bigquery.SchemaField(
            "range_date", enums.SqlTypeNames.RANGE, range_element_type="DATE"
        ),
    ]

    arrow_table = bigquery_client.list_rows(
        table_id,
        selected_fields=schema,
    ).to_arrow()

    schema = arrow_table.schema

    expected_type = pyarrow.struct(
        [("start", pyarrow.date32()), ("end", pyarrow.date32())]
    )

    range_type = schema.field("range_date").type
    assert range_type == expected_type


def test_to_arrow_query_with_empty_results(bigquery_client):
    """
    JSON regression test for https://github.com/googleapis/python-bigquery/issues/1580.
    """
    job = bigquery_client.query(
        """
        select
        123 as int_col,
        '' as string_col,
        to_json('{}') as json_col,
        struct(to_json('[]') as json_field, -1 as int_field) as struct_col,
        [to_json('null')] as json_array_col,
        from unnest([])
        """
    )
    table = job.to_arrow()
    assert list(table.column_names) == [
        "int_col",
        "string_col",
        "json_col",
        "struct_col",
        "json_array_col",
    ]
    assert table.shape == (0, 5)
    struct_type = table.field("struct_col").type
    assert struct_type.get_field_index("json_field") == 0
    assert struct_type.get_field_index("int_field") == 1


def test_query_and_wait_arrow_format_with_compression_codec_to_arrow_iterable(
    bigquery_client,
):
    iterator = bigquery_client.query_and_wait(
        "SELECT 1 AS num, 'hello' AS msg",
        query_results_format="ARROW",
        compression_codec=enums.QueryResultsCompressionCodec.LZ4_FRAME,
    )
    batches = list(iterator.to_arrow_iterable())
    assert len(batches) >= 1
    table = pyarrow.Table.from_batches(batches)
    assert table.column_names == ["num", "msg"]
    assert table.to_pydict() == {"num": [1], "msg": ["hello"]}


def test_query_and_wait_arrow_format_to_arrow(bigquery_client):
    iterator = bigquery_client.query_and_wait(
        "SELECT 42 AS val",
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    table = iterator.to_arrow()
    assert isinstance(table, pyarrow.Table)
    assert table.column_names == ["val"]
    assert table.to_pydict() == {"val": [42]}


def test_query_and_wait_arrow_format_to_dataframe(bigquery_client):
    pandas = pytest.importorskip("pandas")
    iterator = bigquery_client.query_and_wait(
        "SELECT 100 AS num, 'world' AS text",
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    df = iterator.to_dataframe()
    assert isinstance(df, pandas.DataFrame)
    assert df.columns.tolist() == ["num", "text"]
    assert df.to_dict(orient="records") == [{"num": 100, "text": "world"}]


def test_query_and_wait_arrow_format_to_dataframe_iterable(bigquery_client):
    pandas = pytest.importorskip("pandas")
    iterator = bigquery_client.query_and_wait(
        "SELECT 200 AS num, 'python' AS text",
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    dfs = list(iterator.to_dataframe_iterable())
    assert len(dfs) >= 1
    concat_df = pandas.concat(dfs, ignore_index=True)
    assert concat_df.columns.tolist() == ["num", "text"]
    assert concat_df.to_dict(orient="records") == [{"num": 200, "text": "python"}]


@pytest.mark.parametrize(
    "codec",
    [
        enums.QueryResultsCompressionCodec.LZ4_FRAME,
        enums.QueryResultsCompressionCodec.ZSTD,
    ],
)
@pytest.mark.parametrize(
    "page_size", [None, 100], ids=["first_page_only", "with_stream"]
)
def test_query_and_wait_arrow_compression_matches_uncompressed(
    bigquery_client, codec, page_size
):
    query = (
        "SELECT x, CAST(x AS STRING) AS s, x / 7 AS f, "
        "TIMESTAMP_ADD(TIMESTAMP '2026-01-01', INTERVAL x SECOND) AS ts "
        "FROM UNNEST(GENERATE_ARRAY(1, 1000)) AS x ORDER BY x"
    )
    job_config = bigquery.QueryJobConfig(use_query_cache=False)

    def read(**kwargs):
        rows = bigquery_client.query_and_wait(
            query,
            job_config=job_config,
            page_size=page_size,
            query_results_format=enums.QueryResultsFormat.ARROW,
            **kwargs,
        )
        return pyarrow.Table.from_batches(list(rows.to_arrow_iterable()))

    compressed = read(compression_codec=codec)

    assert compressed.num_rows == 1000
    assert compressed.equals(read())


_MICROSECOND_VALUES = [
    datetime.datetime(2025, 1, day, 0, 0, 0, 123456, tzinfo=datetime.timezone.utc)
    for day in (1, 2, 3)
]
_TIMESTAMP_PRECISIONS = pytest.mark.parametrize(
    "timestamp_precision",
    [
        None,
        enums.TimestampPrecision.MICROSECOND,
        enums.TimestampPrecision.PICOSECOND,
    ],
    ids=["default", "microsecond", "picosecond"],
)
_PAGE_SIZES = pytest.mark.parametrize(
    "page_size", [None, 1], ids=["first_page_only", "with_stream"]
)


def _read_timestamps(bigquery_client, query, timestamp_precision, page_size):
    rows = bigquery_client.query_and_wait(
        query,
        job_config=bigquery.QueryJobConfig(use_query_cache=False),
        page_size=page_size,
        query_results_format=enums.QueryResultsFormat.ARROW,
        timestamp_precision=timestamp_precision,
    )
    table = pyarrow.Table.from_batches(list(rows.to_arrow_iterable()))
    return table.column("ts").to_pylist()


@_PAGE_SIZES
@_TIMESTAMP_PRECISIONS
def test_query_and_wait_arrow_timestamp_precision_microsecond_column(
    bigquery_client, timestamp_precision, page_size
):
    values = _read_timestamps(
        bigquery_client,
        "SELECT TIMESTAMP_ADD(TIMESTAMP '2025-01-01 00:00:00.123456 UTC', "
        "INTERVAL x DAY) AS ts FROM UNNEST([0, 1, 2]) AS x ORDER BY x",
        timestamp_precision,
        page_size,
    )

    assert values == _MICROSECOND_VALUES


@_PAGE_SIZES
@_TIMESTAMP_PRECISIONS
def test_query_and_wait_arrow_timestamp_precision_picosecond_column(
    bigquery_client, timestamp_precision, page_size
):
    try:
        values = _read_timestamps(
            bigquery_client,
            "SELECT CAST(FORMAT('2025-01-0%dT00:00:00.123456789012Z', x) "
            "AS TIMESTAMP(12)) AS ts FROM UNNEST([1, 2, 3]) AS x ORDER BY x",
            timestamp_precision,
            page_size,
        )
    except exceptions.BadRequest as exc:
        # TIMESTAMP(12) is enabled per project. The test project has it, but
        # a developer's own project may not.
        if "Timestamp precision type parameter is not supported" not in str(exc):
            raise
        pytest.xfail(f"TIMESTAMP(12) isn't enabled in this project: {exc.message}")

    if timestamp_precision == enums.TimestampPrecision.PICOSECOND:
        assert [value[:10] for value in values] == [
            "2025-01-01",
            "2025-01-02",
            "2025-01-03",
        ]
        assert all(".123456789012" in value for value in values)
    else:
        assert values == _MICROSECOND_VALUES


@_PAGE_SIZES
@_TIMESTAMP_PRECISIONS
def test_query_and_wait_arrow_timestamp_precision_picosecond_table(
    bigquery_client, scalars_table_pico, timestamp_precision, page_size
):
    values = _read_timestamps(
        bigquery_client,
        f"SELECT pico_col AS ts FROM `{scalars_table_pico}` ORDER BY pico_col",
        timestamp_precision,
        page_size,
    )

    if timestamp_precision == enums.TimestampPrecision.PICOSECOND:
        assert [value[:10] for value in values] == [
            "2025-01-01",
            "2025-01-02",
            "2025-01-03",
        ]
        assert all(".123456789012" in value for value in values)
    else:
        assert values == _MICROSECOND_VALUES


@pytest.mark.parametrize(
    ("page_size", "priority", "expected_offset"),
    [
        (100, None, 100),
        # jobs.query doesn't accept a priority, so this case runs through
        # jobs.insert, which returns no rows inline.
        (None, enums.QueryPriority.INTERACTIVE, 0),
    ],
    ids=["some_rows_inline", "no_rows_inline"],
)
def test_query_and_wait_arrow_matches_struct_encoding(
    bigquery_client, bqstorage_client, page_size, priority, expected_offset
):
    query = (
        "SELECT x, CAST(x AS STRING) AS s, MOD(x, 2) = 0 AS even, "
        "DATE_ADD(DATE '2026-01-01', INTERVAL x DAY) AS d "
        "FROM UNNEST(GENERATE_ARRAY(1, 1000)) AS x ORDER BY x"
    )
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    if priority is not None:
        job_config.priority = priority
    expected = [
        dict(row.items())
        for row in bigquery_client.query_and_wait(query, job_config=job_config)
    ]
    # Wrap read_rows() to check where the stream starts.
    read_rows = mock.Mock(wraps=bqstorage_client.read_rows)

    rows = bigquery_client.query_and_wait(
        query,
        job_config=job_config,
        page_size=page_size,
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    with mock.patch.object(bqstorage_client, "read_rows", read_rows):
        batches = list(rows.to_arrow_iterable(bqstorage_client=bqstorage_client))

    assert pyarrow.Table.from_batches(batches).to_pylist() == expected
    read_rows.assert_called_once_with(
        f"projects/{bigquery_client.project}/locations/{rows.location}"
        f"/jobs/{rows.job_id}/streams/_default",
        offset=expected_offset,
        timeout=mock.ANY,
        arrow_serialization_options=mock.ANY,
    )


def _interval_to_relativedelta(value):
    return relativedelta.relativedelta(
        months=value.months, days=value.days, microseconds=value.nanoseconds // 1000
    )


def _arrow_rows(table):
    """Return the rows of an Arrow table as STRUCT_ENCODING returns them.

    Arrow has JSON values as strings and INTERVAL values as MonthDayNano,
    while STRUCT_ENCODING rows have parsed JSON and relativedelta values.
    """
    converters = {}
    for field in table.schema:
        if field.metadata == {b"ARROW:extension:name": b"google:sqlType:json"}:
            converters[field.name] = json.loads
        elif pyarrow.types.is_interval(field.type):
            converters[field.name] = _interval_to_relativedelta
    rows = table.to_pylist()
    for row in rows:
        for name, convert in converters.items():
            if row[name] is not None:
                row[name] = convert(row[name])
    return rows


@pytest.mark.parametrize(
    ("page_size", "priority", "expected_offset"),
    [
        (1, None, 1),
        # jobs.query doesn't accept a priority, so this case runs through
        # jobs.insert, which returns no rows inline.
        (None, enums.QueryPriority.INTERACTIVE, 0),
    ],
    ids=["some_rows_inline", "no_rows_inline"],
)
def test_query_and_wait_arrow_locations(
    bigquery_client,
    bqstorage_client,
    scalars_table_multi_location,
    page_size,
    priority,
    expected_offset,
):
    location, table_id = scalars_table_multi_location
    query = f"SELECT * FROM `{table_id}` ORDER BY rowindex"
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    if priority is not None:
        job_config.priority = priority
    expected = [
        dict(row.items())
        for row in bigquery_client.query_and_wait(query, job_config=job_config)
    ]
    read_rows = mock.Mock(wraps=bqstorage_client.read_rows)

    # The query doesn't name a location, so only jobReference has it.
    rows = bigquery_client.query_and_wait(
        query,
        job_config=job_config,
        page_size=page_size,
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    with mock.patch.object(bqstorage_client, "read_rows", read_rows):
        batches = list(rows.to_arrow_iterable(bqstorage_client=bqstorage_client))

    assert rows.location == location
    assert _arrow_rows(pyarrow.Table.from_batches(batches)) == expected
    read_rows.assert_called_once_with(
        f"projects/{bigquery_client.project}/locations/{location}"
        f"/jobs/{rows.job_id}/streams/_default",
        offset=expected_offset,
        timeout=mock.ANY,
        arrow_serialization_options=mock.ANY,
    )


_DATA_TYPES_QUERY = """
SELECT
  i,
  IF(i = 2, NULL, i = 1) AS bool_col,
  IF(i = 2, NULL, i * 1000000000000) AS int64_col,
  IF(i = 2, NULL, i / 3) AS float64_col,
  IF(i = 2, NULL, NUMERIC '-123456789.123456789') AS numeric_col,
  IF(i = 2, NULL, BIGNUMERIC '1.23456789012345678901234567890123456789') AS bignumeric_col,
  IF(i = 2, NULL, FORMAT('row %d', i)) AS string_col,
  IF(i = 2, NULL, CAST(FORMAT('row %d', i) AS BYTES)) AS bytes_col,
  IF(i = 2, NULL, DATE_ADD(DATE '2026-01-01', INTERVAL i DAY)) AS date_col,
  IF(i = 2, NULL, DATETIME '2026-01-01 12:34:56.789012') AS datetime_col,
  IF(i = 2, NULL, TIME '12:34:56.789012') AS time_col,
  IF(i = 2, NULL, TIMESTAMP '2026-01-01 12:34:56.789012 UTC') AS timestamp_col,
  IF(i = 2, NULL, INTERVAL '1-2 3 4:5:6.789012' YEAR TO SECOND) AS interval_col,
  IF(i = 2, NULL, ST_GEOGPOINT(-122.0838511, 37.3860517)) AS geography_col,
  IF(i = 2, NULL, JSON '{"a": [1, 2.5, "x"], "b": null, "c": {"d": true}}') AS json_col,
  IF(i = 2, NULL, RANGE(DATE '2026-01-01', DATE '2026-02-01')) AS range_date_col,
  IF(i = 2, NULL, RANGE(DATETIME '2026-01-01 00:00:00', NULL)) AS range_datetime_col,
  IF(
    i = 2,
    NULL,
    RANGE(TIMESTAMP '2026-01-01 00:00:00 UTC', TIMESTAMP '2026-01-02 00:00:00 UTC')
  ) AS range_timestamp_col,
  IF(i = 2, [], [i, i + 1]) AS array_col,
  IF(i = 2, NULL, STRUCT(i AS x, [STRUCT('a' AS s, [1.5, 2.5] AS f)] AS nested)) AS struct_col
FROM UNNEST([1, 2, 3]) AS i
ORDER BY i
"""


def test_query_and_wait_arrow_data_types(bigquery_client):
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    expected = [
        dict(row.items())
        for row in bigquery_client.query_and_wait(
            _DATA_TYPES_QUERY, job_config=job_config
        )
    ]

    rows = bigquery_client.query_and_wait(
        _DATA_TYPES_QUERY,
        job_config=job_config,
        # The first row arrives in the first page, the others in the stream.
        page_size=1,
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    batches = list(rows.to_arrow_iterable())

    assert batches[0].num_rows == 1
    assert _arrow_rows(pyarrow.Table.from_batches(batches)) == expected


@pytest.mark.parametrize(
    "priority",
    [None, enums.QueryPriority.INTERACTIVE],
    ids=["jobs_query", "jobs_insert"],
)
def test_query_and_wait_arrow_unnamed_struct_fields(bigquery_client, priority):
    query = "SELECT (1, 'a') AS s, STRUCT(2 AS x, 'b') AS p"
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    if priority is not None:
        # jobs.query doesn't accept a priority, so this runs through jobs.insert.
        job_config.priority = priority
    expected = [
        dict(row.items())
        for row in bigquery_client.query_and_wait(query, job_config=job_config)
    ]

    try:
        rows = bigquery_client.query_and_wait(
            query,
            job_config=job_config,
            # jobs.query fails with a jobInternalError, which job_retry would
            # retry until its deadline.
            job_retry=None,
            query_results_format=enums.QueryResultsFormat.ARROW,
        )
    except exceptions.BadRequest as exc:
        if not any(error.get("reason") == "jobInternalError" for error in exc.errors):
            raise
        pytest.xfail(f"jobs.query can't send unnamed STRUCT fields: {exc.message}")
    table = pyarrow.Table.from_batches(list(rows.to_arrow_iterable()))

    assert table.to_pylist() == expected


@pytest.mark.parametrize(
    "priority",
    [None, enums.QueryPriority.INTERACTIVE],
    ids=["first_page_only", "no_rows_inline"],
)
def test_query_and_wait_arrow_extreme_values(
    bigquery_client, scalars_extreme_table, priority
):
    # BigQuery fails the extreme INTERVAL values with "Out of range conversion
    # for microseconds value", since Arrow's interval type can't hold them.
    query = (
        f"SELECT * EXCEPT (interval_col) FROM `{scalars_extreme_table}` "
        "ORDER BY rowindex"
    )
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    if priority is not None:
        job_config.priority = priority
    expected = [
        dict(row.items())
        for row in bigquery_client.query_and_wait(query, job_config=job_config)
    ]

    rows = bigquery_client.query_and_wait(
        query,
        job_config=job_config,
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    actual = _arrow_rows(pyarrow.Table.from_batches(list(rows.to_arrow_iterable())))

    # NaN never equals itself, so check it on its own.
    assert math.isnan(actual[2].pop("float64_col"))
    assert math.isnan(expected[2].pop("float64_col"))
    assert actual == expected


@pytest.mark.parametrize(
    ("priority", "page_size", "num_rows", "payload_size"),
    [
        (None, 100, 1000, 0),
        # The results are too large to return inline, so the cached jobs.query
        # response has no rows and totalRows is 0.
        (None, None, 20000, 1024),
        (enums.QueryPriority.INTERACTIVE, 100, 1000, 0),
    ],
    ids=["some_rows_inline", "too_large_for_inline", "no_rows_inline"],
)
def test_query_and_wait_arrow_cached_results(
    bigquery_client, priority, page_size, num_rows, payload_size
):
    # No other query uses this literal, so only the second run can hit the
    # cache.
    query = (
        f"SELECT x, '{uuid.uuid4().hex}' AS key, REPEAT('x', {payload_size}) AS p "
        f"FROM UNNEST(GENERATE_ARRAY(1, {num_rows})) AS x ORDER BY x"
    )
    job_config = bigquery.QueryJobConfig(use_query_cache=True)
    if priority is not None:
        job_config.priority = priority

    def read():
        rows = bigquery_client.query_and_wait(
            query,
            job_config=job_config,
            page_size=page_size,
            query_results_format=enums.QueryResultsFormat.ARROW,
        )
        table = pyarrow.Table.from_batches(list(rows.to_arrow_iterable()))
        return bigquery_client.get_job(rows.job_id, location=rows.location), table

    first_job, first = read()
    cached_job, cached = read()

    assert not first_job.cache_hit
    assert cached_job.cache_hit
    assert cached.num_rows == num_rows
    assert cached.equals(first)


@pytest.mark.parametrize(
    "priority",
    [None, enums.QueryPriority.INTERACTIVE],
    ids=["jobs_query", "jobs_insert"],
)
def test_query_and_wait_arrow_failed_query(bigquery_client, priority):
    # The last row fails, so the query fails while it runs.
    query = (
        "SELECT IF(x < 1000, x, ERROR(FORMAT('failed at row %d', x))) AS x "
        "FROM UNNEST(GENERATE_ARRAY(1, 1000)) AS x"
    )
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    if priority is not None:
        job_config.priority = priority

    with pytest.raises(exceptions.GoogleAPICallError) as struct_encoding_error:
        bigquery_client.query_and_wait(query, job_config=job_config)
    with pytest.raises(exceptions.GoogleAPICallError) as arrow_error:
        rows = bigquery_client.query_and_wait(
            query,
            job_config=job_config,
            query_results_format=enums.QueryResultsFormat.ARROW,
        )
        list(rows.to_arrow_iterable())

    assert type(arrow_error.value) is type(struct_encoding_error.value)
    assert "failed at row 1000" in arrow_error.value.message


@pytest.mark.parametrize(
    ("page_size", "max_results", "expected_rows", "streamed"),
    [
        (None, 10, 10, False),
        (100, 150, 150, True),
        (100, 5000, 1000, True),
    ],
    ids=["within_first_page", "across_stream", "past_last_row"],
)
def test_query_and_wait_arrow_max_results(
    bigquery_client, bqstorage_client, page_size, max_results, expected_rows, streamed
):
    read_rows = mock.Mock(wraps=bqstorage_client.read_rows)

    rows = bigquery_client.query_and_wait(
        "SELECT x FROM UNNEST(GENERATE_ARRAY(1, 1000)) AS x ORDER BY x",
        job_config=bigquery.QueryJobConfig(use_query_cache=False),
        page_size=page_size,
        max_results=max_results,
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    with mock.patch.object(bqstorage_client, "read_rows", read_rows):
        batches = list(rows.to_arrow_iterable(bqstorage_client=bqstorage_client))

    table = pyarrow.Table.from_batches(batches)
    assert table.column("x").to_pylist() == list(range(1, expected_rows + 1))
    assert read_rows.called == streamed


def _query_arrow(client, row_count):
    return client.query_and_wait(
        f"SELECT x FROM UNNEST(GENERATE_ARRAY(1, {row_count})) AS x ORDER BY x",
        job_config=bigquery.QueryJobConfig(use_query_cache=False),
        page_size=100,
        query_results_format=enums.QueryResultsFormat.ARROW,
    )


def test_query_and_wait_arrow_queries_share_one_bqstorage_client():
    from google.cloud.bigquery import client as client_module

    with bigquery.Client() as client:
        # Wrap the client factory to count how many clients get created.
        ensure = mock.Mock(wraps=client._ensure_bqstorage_client)
        with mock.patch.object(client, "_ensure_bqstorage_client", ensure):
            tables = [
                pyarrow.Table.from_batches(
                    list(_query_arrow(client, 1000).to_arrow_iterable())
                ),
                _query_arrow(client, 1000).to_arrow(),
                pyarrow.Table.from_batches(
                    list(_query_arrow(client, 1000).to_arrow_iterable())
                ),
            ]
        shared = client._shared_bqstorage_client

    for table in tables:
        assert table.column("x").to_pylist() == list(range(1, 1001))
    ensure.assert_called_once_with(transport=client_module._create_bqstorage_transport)
    assert shared is not None
    # Leaving the with block calls close(), which closes the shared channel.
    assert client._shared_bqstorage_client is None
    with pytest.raises(ValueError, match="(?i)closed"):
        shared.read_rows("projects/p/locations/US/jobs/j/streams/_default")


def test_query_and_wait_arrow_ending_a_read_early_cancels_only_its_stream():
    from google.cloud.bigquery_storage_v1 import reader

    # Wrap ReadRowsStream.cancel() to record calls without changing it.
    cancel_stream = reader.ReadRowsStream.cancel
    cancelled_open = []

    def record_open_cancel(stream):
        # google-cloud-bigquery-storage 2.43.0's __del__ also calls cancel()
        # on finished streams, which does nothing. Count only cancels of a
        # stream that's still open.
        # TODO(https://github.com/googleapis/google-cloud-python/issues/18785):
        # Count every cancel() once the bqstorage extra requires a release
        # whose __del__ skips finished streams.
        if stream._wrapped is not None:
            cancelled_open.append(stream)
        return cancel_stream(stream)

    with bigquery.Client() as client, mock.patch.object(
        reader.ReadRowsStream, "cancel", autospec=True, side_effect=record_open_cancel
    ):
        ended_early_rows = _query_arrow(client, 100000)
        ended_early = ended_early_rows.to_arrow_iterable()
        read_fully = _query_arrow(client, 100000).to_arrow_iterable()
        # Two reads reach the stream, whether or not jobs.query returned a
        # first page.
        next(ended_early)
        next(ended_early)
        rows = [next(read_fully), next(read_fully)]

        ended_early.close()
        rows.extend(read_fully)

    (stream,) = cancelled_open
    assert stream._name.endswith(f"/jobs/{ended_early_rows.job_id}/streams/_default")
    table = pyarrow.Table.from_batches(rows)
    assert table.column("x").to_pylist() == list(range(1, 100001))


@pytest.mark.parametrize(
    "write_disposition",
    [None, enums.WriteDisposition.WRITE_TRUNCATE],
    ids=["default", "overwrite"],
)
def test_query_and_wait_arrow_explicit_destination(
    bigquery_client, bqstorage_client, dataset_id, write_disposition
):
    table_name = f"arrow_destination_{write_disposition or 'default'}".lower()
    table_id = f"{bigquery_client.project}.{dataset_id}.{table_name}"
    job_config = bigquery.QueryJobConfig(destination=table_id)
    if write_disposition is not None:
        # The rows already in the table are replaced, not read.
        bigquery_client.query_and_wait(
            f"CREATE OR REPLACE TABLE `{table_id}` AS SELECT -1 AS x"
        )
        job_config.write_disposition = write_disposition
    # Wrap create_read_session() to check how the table is read.
    create_read_session = mock.Mock(wraps=bqstorage_client.create_read_session)

    rows = bigquery_client.query_and_wait(
        "SELECT x FROM UNNEST(GENERATE_ARRAY(1, 1000)) AS x ORDER BY x",
        job_config=job_config,
        query_results_format=enums.QueryResultsFormat.ARROW,
    )
    with mock.patch.object(
        bqstorage_client, "create_read_session", create_read_session
    ):
        batches = list(rows.to_arrow_iterable(bqstorage_client=bqstorage_client))

    table = pyarrow.Table.from_batches(batches)
    assert table.column("x").to_pylist() == list(range(1, 1001))
    kwargs = create_read_session.call_args.kwargs
    assert kwargs["read_session"].table == (
        f"projects/{bigquery_client.project}/datasets/{dataset_id}/tables/{table_name}"
    )
    assert kwargs["max_stream_count"] == 1


@pytest.mark.parametrize(
    "priority",
    [None, enums.QueryPriority.INTERACTIVE],
    ids=["jobs_query", "jobs_insert"],
)
def test_query_and_wait_arrow_zero_rows_keep_the_schema(bigquery_client, priority):
    job_config = bigquery.QueryJobConfig(use_query_cache=False)
    if priority is not None:
        # jobs.query doesn't accept a priority, so this runs through jobs.insert.
        job_config.priority = priority

    def query():
        return bigquery_client.query_and_wait(
            "SELECT x, CAST(x AS STRING) AS s "
            "FROM UNNEST(CAST([] AS ARRAY<INT64>)) AS x",
            job_config=job_config,
            query_results_format=enums.QueryResultsFormat.ARROW,
        )

    batches = list(query().to_arrow_iterable())

    assert len(batches) == 1
    for table in (pyarrow.Table.from_batches(batches), query().to_arrow()):
        assert table.num_rows == 0
        assert table.schema.names == ["x", "s"]
        assert table.schema.field("x").type == pyarrow.int64()
        assert table.schema.field("s").type == pyarrow.string()


def test_query_and_wait_arrow_statements_without_results(bigquery_client, dataset_id):
    table_id = f"{bigquery_client.project}.{dataset_id}.arrow_statements"

    for statement in (
        f"CREATE OR REPLACE TABLE `{table_id}` AS SELECT 1 AS x",
        f"UPDATE `{table_id}` SET x = 2 WHERE TRUE",
    ):
        rows = bigquery_client.query_and_wait(
            statement, query_results_format=enums.QueryResultsFormat.ARROW
        )
        (batch,) = rows.to_arrow_iterable()
        assert batch.num_rows == 0

    assert rows.num_dml_affected_rows == 1
    assert [
        row.x for row in bigquery_client.query_and_wait(f"SELECT x FROM `{table_id}`")
    ] == [2]
