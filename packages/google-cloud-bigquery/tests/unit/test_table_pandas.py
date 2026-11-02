# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import mock
import datetime
import decimal

import pytest

from google.cloud import bigquery

pandas = pytest.importorskip("pandas")
pyarrow = pytest.importorskip("pyarrow", minversion="3.0.0")


TEST_PATH = "/v1/project/test-proj/dataset/test-dset/table/test-tbl/data"


@pytest.fixture
def class_under_test():
    from google.cloud.bigquery.table import RowIterator

    return RowIterator


def test_to_dataframe_nullable_scalars(
    monkeypatch, class_under_test
):  # pragma: NO COVER
    """See tests/system/test_arrow.py for the actual types we get from the API."""
    arrow_schema = pyarrow.schema(
        [
            pyarrow.field("bignumeric_col", pyarrow.decimal256(76, scale=38)),
            pyarrow.field("bool_col", pyarrow.bool_()),
            pyarrow.field("bytes_col", pyarrow.binary()),
            pyarrow.field("date_col", pyarrow.date32()),
            pyarrow.field("datetime_col", pyarrow.timestamp("us", tz=None)),
            pyarrow.field("float64_col", pyarrow.float64()),
            pyarrow.field("int64_col", pyarrow.int64()),
            pyarrow.field("numeric_col", pyarrow.decimal128(38, scale=9)),
            pyarrow.field("string_col", pyarrow.string()),
            pyarrow.field("time_col", pyarrow.time64("us")),
            pyarrow.field(
                "timestamp_col", pyarrow.timestamp("us", tz=datetime.timezone.utc)
            ),
            pyarrow.field("json_col", pyarrow.string()),
        ]
    )
    arrow_table = pyarrow.Table.from_pydict(
        {
            "bignumeric_col": [decimal.Decimal("123.456789101112131415")],
            "bool_col": [True],
            "bytes_col": [b"Hello,\x00World!"],
            "date_col": [datetime.date(2021, 8, 9)],
            "datetime_col": [datetime.datetime(2021, 8, 9, 13, 30, 44, 123456)],
            "float64_col": [1.25],
            "int64_col": [-7],
            "numeric_col": [decimal.Decimal("-123.456789")],
            "string_col": ["abcdefg"],
            "time_col": [datetime.time(14, 21, 17, 123456)],
            "timestamp_col": [
                datetime.datetime(
                    2021, 8, 9, 13, 30, 44, 123456, tzinfo=datetime.timezone.utc
                )
            ],
            "json_col": ["{}"],
        },
        schema=arrow_schema,
    )

    nullable_schema = [
        bigquery.SchemaField("bignumeric_col", "BIGNUMERIC"),
        bigquery.SchemaField("bool_col", "BOOLEAN"),
        bigquery.SchemaField("bytes_col", "BYTES"),
        bigquery.SchemaField("date_col", "DATE"),
        bigquery.SchemaField("datetime_col", "DATETIME"),
        bigquery.SchemaField("float64_col", "FLOAT"),
        bigquery.SchemaField("int64_col", "INT64"),
        bigquery.SchemaField("numeric_col", "NUMERIC"),
        bigquery.SchemaField("string_col", "STRING"),
        bigquery.SchemaField("time_col", "TIME"),
        bigquery.SchemaField("timestamp_col", "TIMESTAMP"),
        bigquery.SchemaField("json_col", "JSON"),
    ]
    mock_client = mock.create_autospec(bigquery.Client)
    mock_client.project = "test-proj"
    mock_api_request = mock.Mock()
    mock_to_arrow = mock.Mock()
    mock_to_arrow.return_value = arrow_table
    rows = class_under_test(mock_client, mock_api_request, TEST_PATH, nullable_schema)
    monkeypatch.setattr(rows, "to_arrow", mock_to_arrow)
    df = rows.to_dataframe()

    # Check for expected dtypes.
    # Keep these in sync with tests/system/test_pandas.py
    assert df.dtypes["bignumeric_col"].name == "object"
    assert df.dtypes["bool_col"].name == "boolean"
    assert df.dtypes["bytes_col"].name == "object"
    assert df.dtypes["date_col"].name == "dbdate"
    assert df.dtypes["float64_col"].name == "float64"
    assert df.dtypes["int64_col"].name == "Int64"
    assert df.dtypes["numeric_col"].name == "object"
    assert df.dtypes["string_col"].name in {"object", "string", "str", "O"}
    assert df.dtypes["time_col"].name == "dbtime"
    assert df.dtypes["json_col"].name in {"object", "string", "str", "O"}

    if pandas.__version__.startswith(("2.", "3.")):
        assert df.dtypes["datetime_col"].name == "datetime64[us]"
        assert df.dtypes["timestamp_col"].name == "datetime64[us, UTC]"
    else:
        assert df.dtypes["datetime_col"].name == "datetime64[ns]"
        assert df.dtypes["timestamp_col"].name == "datetime64[ns, UTC]"

    # Check for expected values.
    assert df["bignumeric_col"][0] == decimal.Decimal("123.456789101112131415")
    assert df["bool_col"][0]  # True
    assert df["bytes_col"][0] == b"Hello,\x00World!"

    # object is used by default, but we can use "datetime64[ns]" automatically
    # when data is within the supported range.
    # https://github.com/googleapis/python-bigquery/issues/861
    assert df["date_col"][0] == datetime.date(2021, 8, 9)

    assert df["datetime_col"][0] == pandas.to_datetime("2021-08-09 13:30:44.123456")
    assert df["float64_col"][0] == 1.25
    assert df["int64_col"][0] == -7
    assert df["numeric_col"][0] == decimal.Decimal("-123.456789")
    assert df["string_col"][0] == "abcdefg"
    # Pandas timedelta64 might be a better choice for pandas time columns. Then
    # they can more easily be combined with date columns to form datetimes.
    # https://github.com/googleapis/python-bigquery/issues/862
    assert df["time_col"][0] == datetime.time(14, 21, 17, 123456)
    assert df["timestamp_col"][0] == pandas.to_datetime("2021-08-09 13:30:44.123456Z")


def test_to_dataframe_nullable_scalars_with_custom_dtypes(
    monkeypatch, class_under_test
):
    """Passing in explicit dtypes is merged with default behavior."""
    arrow_schema = pyarrow.schema(
        [
            pyarrow.field("int64_col", pyarrow.int64()),
            pyarrow.field("other_int_col", pyarrow.int64()),
        ]
    )
    arrow_table = pyarrow.Table.from_pydict(
        {"int64_col": [1000], "other_int_col": [-7]},
        schema=arrow_schema,
    )

    nullable_schema = [
        bigquery.SchemaField("int64_col", "INT64"),
        bigquery.SchemaField("other_int_col", "INT64"),
    ]
    mock_client = mock.create_autospec(bigquery.Client)
    mock_client.project = "test-proj"
    mock_api_request = mock.Mock()
    mock_to_arrow = mock.Mock()
    mock_to_arrow.return_value = arrow_table
    rows = class_under_test(mock_client, mock_api_request, TEST_PATH, nullable_schema)
    monkeypatch.setattr(rows, "to_arrow", mock_to_arrow)
    df = rows.to_dataframe(dtypes={"other_int_col": "int8"})

    assert df.dtypes["int64_col"].name == "Int64"
    assert df["int64_col"][0] == 1000

    assert df.dtypes["other_int_col"].name == "int8"
    assert df["other_int_col"][0] == -7


def test_to_dataframe_arrays(monkeypatch, class_under_test):
    arrow_schema = pyarrow.schema(
        [pyarrow.field("int64_repeated", pyarrow.list_(pyarrow.int64()))]
    )
    arrow_table = pyarrow.Table.from_pydict(
        {"int64_repeated": [[-1, 0, 2]]},
        schema=arrow_schema,
    )

    nullable_schema = [
        bigquery.SchemaField("int64_repeated", "INT64", mode="REPEATED"),
    ]
    mock_client = mock.create_autospec(bigquery.Client)
    mock_client.project = "test-proj"
    mock_api_request = mock.Mock()
    mock_to_arrow = mock.Mock()
    mock_to_arrow.return_value = arrow_table
    rows = class_under_test(mock_client, mock_api_request, TEST_PATH, nullable_schema)
    monkeypatch.setattr(rows, "to_arrow", mock_to_arrow)
    df = rows.to_dataframe()

    assert df.dtypes["int64_repeated"].name == "object"
    assert tuple(df["int64_repeated"][0]) == (-1, 0, 2)


def test_to_dataframe_with_jobs_query_response(class_under_test):
    resource = {
        "kind": "bigquery#queryResponse",
        "schema": {
            "fields": [
                {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                {"name": "number", "type": "INTEGER", "mode": "NULLABLE"},
            ]
        },
        "jobReference": {
            "projectId": "test-project",
            "jobId": "job_ocd3cb-N62QIslU7R5qKKa2_427J",
            "location": "US",
        },
        "totalRows": "9",
        "rows": [
            {"f": [{"v": "Tiarra"}, {"v": "6"}]},
            {"f": [{"v": "Timothy"}, {"v": "325"}]},
            {"f": [{"v": "Tina"}, {"v": "26"}]},
            {"f": [{"v": "Tierra"}, {"v": "10"}]},
            {"f": [{"v": "Tia"}, {"v": "17"}]},
            {"f": [{"v": "Tiara"}, {"v": "22"}]},
            {"f": [{"v": "Tiana"}, {"v": "6"}]},
            {"f": [{"v": "Tiffany"}, {"v": "229"}]},
            {"f": [{"v": "Tiffani"}, {"v": "8"}]},
        ],
        "totalBytesProcessed": "154775150",
        "jobComplete": True,
        "cacheHit": False,
        "queryId": "job_ocd3cb-N62QIslU7R5qKKa2_427J",
    }

    rows = class_under_test(
        client=None,
        api_request=None,
        path=None,
        schema=[
            bigquery.SchemaField.from_api_repr(field)
            for field in resource["schema"]["fields"]
        ],
        first_page_response=resource,
    )
    df = rows.to_dataframe()

    assert list(df.columns) == ["name", "number"]
    assert list(df["name"]) == [
        "Tiarra",
        "Timothy",
        "Tina",
        "Tierra",
        "Tia",
        "Tiara",
        "Tiana",
        "Tiffany",
        "Tiffani",
    ]
    assert list(df["number"]) == [6, 325, 26, 10, 17, 22, 6, 229, 8]


@mock.patch("google.cloud.bigquery.table.geopandas")
def test_rowiterator_to_geodataframe_with_default_dtypes(
    mock_geopandas, monkeypatch, class_under_test
):
    mock_geopandas.GeoDataFrame = mock.Mock(spec=True)
    mock_client = mock.create_autospec(bigquery.Client)
    mock_client.project = "test-proj"
    mock_api_request = mock.Mock()
    schema = [
        bigquery.SchemaField("geo_col", "GEOGRAPHY"),
        bigquery.SchemaField("bool_col", "BOOLEAN"),
        bigquery.SchemaField("int_col", "INTEGER"),
        bigquery.SchemaField("float_col", "FLOAT"),
        bigquery.SchemaField("string_col", "STRING"),
    ]
    rows = class_under_test(mock_client, mock_api_request, TEST_PATH, schema)

    mock_df = pandas.DataFrame(
        {
            "geo_col": ["POINT (1 2)"],
            "bool_col": [True],
            "int_col": [123],
            "float_col": [1.23],
            "string_col": ["abc"],
        }
    )
    rows.to_dataframe = mock.Mock(return_value=mock_df)

    rows.to_geodataframe(geography_column="geo_col")

    rows.to_dataframe.assert_called_once_with(
        None,  # bqstorage_client
        None,  # dtypes
        None,  # progress_bar_type
        True,  # create_bqstorage_client
        geography_as_object=True,
        bool_dtype=bigquery.enums.DefaultPandasDTypes.BOOL_DTYPE,
        int_dtype=bigquery.enums.DefaultPandasDTypes.INT_DTYPE,
        float_dtype=None,
        string_dtype=None,
        timeout=None,
    )
    mock_geopandas.GeoDataFrame.assert_called_once_with(
        mock_df, crs="EPSG:4326", geometry="geo_col"
    )


@mock.patch("google.cloud.bigquery.table.geopandas")
def test_rowiterator_to_geodataframe_with_custom_dtypes(
    mock_geopandas, monkeypatch, class_under_test
):
    mock_geopandas.GeoDataFrame = mock.Mock(spec=True)
    mock_client = mock.create_autospec(bigquery.Client)
    mock_client.project = "test-proj"
    mock_api_request = mock.Mock()
    schema = [
        bigquery.SchemaField("geo_col", "GEOGRAPHY"),
        bigquery.SchemaField("bool_col", "BOOLEAN"),
        bigquery.SchemaField("int_col", "INTEGER"),
        bigquery.SchemaField("float_col", "FLOAT"),
        bigquery.SchemaField("string_col", "STRING"),
    ]
    rows = class_under_test(mock_client, mock_api_request, TEST_PATH, schema)

    mock_df = pandas.DataFrame(
        {
            "geo_col": ["POINT (3 4)"],
            "bool_col": [False],
            "int_col": [456],
            "float_col": [4.56],
            "string_col": ["def"],
        }
    )
    rows.to_dataframe = mock.Mock(return_value=mock_df)

    custom_bool_dtype = "bool"
    custom_int_dtype = "int32"
    custom_float_dtype = "float32"
    custom_string_dtype = "string"

    rows.to_geodataframe(
        geography_column="geo_col",
        bool_dtype=custom_bool_dtype,
        int_dtype=custom_int_dtype,
        float_dtype=custom_float_dtype,
        string_dtype=custom_string_dtype,
    )

    rows.to_dataframe.assert_called_once_with(
        None,  # bqstorage_client
        None,  # dtypes
        None,  # progress_bar_type
        True,  # create_bqstorage_client
        geography_as_object=True,
        bool_dtype=custom_bool_dtype,
        int_dtype=custom_int_dtype,
        float_dtype=custom_float_dtype,
        string_dtype=custom_string_dtype,
        timeout=None,
    )
    mock_geopandas.GeoDataFrame.assert_called_once_with(
        mock_df, crs="EPSG:4326", geometry="geo_col"
    )
