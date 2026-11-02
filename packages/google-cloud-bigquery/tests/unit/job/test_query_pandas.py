# Copyright 2015 Google LLC
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

import concurrent.futures
import copy
import json
from unittest import mock

import pytest

from ..helpers import make_connection
from .helpers import _make_client
from .helpers import _make_job_resource
from google.cloud.bigquery.enums import DefaultPandasDTypes

try:
    from google.cloud import bigquery_storage
    import google.cloud.bigquery_storage_v1.reader
    import google.cloud.bigquery_storage_v1.services.big_query_read.client
except (ImportError, AttributeError):
    bigquery_storage = None


try:
    import shapely
except (ImportError, AttributeError):
    shapely = None
try:
    import geopandas
except (ImportError, AttributeError):
    geopandas = None
try:
    import tqdm
except (ImportError, AttributeError):
    tqdm = None

try:
    import pyarrow
    import pyarrow.types
except ImportError:
    pyarrow = None

pandas = pytest.importorskip("pandas")


@pytest.fixture
def table_read_options_kwarg():
    read_options = bigquery_storage.ReadSession.TableReadOptions(
        arrow_serialization_options=bigquery_storage.ArrowSerializationOptions(
            buffer_compression=bigquery_storage.ArrowSerializationOptions.CompressionCodec.LZ4_FRAME
        )
    )
    return {"read_options": read_options}


@pytest.mark.parametrize(
    "query,expected",
    (
        (None, False),
        ("", False),
        ("select name, age from table", False),
        ("select name, age from table LIMIT 10;", False),
        ("select name, age from table order by other_column;", True),
        ("Select name, age From table Order By other_column", True),
        ("SELECT name, age FROM table ORDER BY other_column;", True),
        ("select name, age from table order\nby other_column", True),
        ("Select name, age From table Order\nBy other_column;", True),
        ("SELECT name, age FROM table ORDER\nBY other_column", True),
        ("SelecT name, age froM table OrdeR \n\t BY other_column;", True),
    ),
)
def test__contains_order_by(query, expected):
    from google.cloud.bigquery import job as mut

    if expected:
        assert mut._contains_order_by(query)
    else:
        assert not mut._contains_order_by(query)


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
@pytest.mark.parametrize(
    "query",
    (
        "select name, age from table order by other_column;",
        "Select name, age From table Order By other_column;",
        "SELECT name, age FROM table ORDER BY other_column;",
        "select name, age from table order\nby other_column;",
        "Select name, age From table Order\nBy other_column;",
        "SELECT name, age FROM table ORDER\nBY other_column;",
        "SelecT name, age froM table OrdeR \n\t BY other_column;",
    ),
)
def test_to_dataframe_bqstorage_preserve_order(query, table_read_options_kwarg):
    from google.cloud.bigquery.job import QueryJob as target_class

    job_resource = _make_job_resource(
        project_id="test-project", job_type="query", ended=True
    )
    job_resource["configuration"]["query"]["query"] = query
    job_resource["status"] = {"state": "DONE"}
    query_resource = {
        "jobComplete": True,
        "jobReference": {"projectId": "test-project", "jobId": "test-job"},
        "schema": {
            "fields": [
                {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                {"name": "age", "type": "INTEGER", "mode": "NULLABLE"},
            ]
        },
        "totalRows": "4",
    }
    stream_id = "projects/1/locations/2/sessions/3/streams/4"
    name_array = pyarrow.array(
        ["John", "Paul", "George", "Ringo"], type=pyarrow.string()
    )
    age_array = pyarrow.array([17, 24, 21, 15], type=pyarrow.int64())
    arrow_schema = pyarrow.schema(
        [
            pyarrow.field("name", pyarrow.string(), True),
            pyarrow.field("age", pyarrow.int64(), True),
        ]
    )
    record_batch = pyarrow.RecordBatch.from_arrays(
        [name_array, age_array], schema=arrow_schema
    )
    connection = make_connection(query_resource)
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(job_resource, client)
    bqstorage_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    session = bigquery_storage.types.ReadSession()
    session.arrow_schema.serialized_schema = arrow_schema.serialize().to_pybytes()
    session.streams = [bigquery_storage.types.ReadStream(name=stream_id)]
    reader = mock.create_autospec(
        google.cloud.bigquery_storage_v1.reader.ReadRowsStream, instance=True
    )
    row_iterable = mock.create_autospec(
        google.cloud.bigquery_storage_v1.reader.ReadRowsIterable, instance=True
    )
    page = mock.create_autospec(
        google.cloud.bigquery_storage_v1.reader.ReadRowsPage, instance=True
    )
    page.to_arrow.return_value = record_batch
    type(row_iterable).pages = mock.PropertyMock(return_value=[page])
    reader.rows.return_value = row_iterable
    bqstorage_client = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_client.create_read_session.return_value = session
    bqstorage_client.read_rows.return_value = reader

    dataframe = job.to_dataframe(bqstorage_client=bqstorage_client)

    assert len(dataframe) == 4
    destination_table = (
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}".format(
            **job_resource["configuration"]["query"]["destinationTable"]
        )
    )
    expected_session = bigquery_storage.ReadSession(
        table=destination_table,
        data_format=bigquery_storage.DataFormat.ARROW,
        **table_read_options_kwarg,
    )
    bqstorage_client.create_read_session.assert_called_once_with(
        parent="projects/test-project",
        read_session=expected_session,
        max_stream_count=1,  # Use a single stream to preserve row order.
        retry=None,
        timeout=None,
    )


@pytest.mark.skipif(pyarrow is None, reason="Requires `pyarrow`")
def test_to_arrow():
    from google.cloud.bigquery.job import QueryJob as target_class

    begun_resource = _make_job_resource(job_type="query")
    query_resource = {
        "jobComplete": True,
        "jobReference": begun_resource["jobReference"],
        "totalRows": "4",
        "schema": {
            "fields": [
                {
                    "name": "spouse_1",
                    "type": "RECORD",
                    "fields": [
                        {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                        {"name": "age", "type": "INTEGER", "mode": "NULLABLE"},
                    ],
                },
                {
                    "name": "spouse_2",
                    "type": "RECORD",
                    "fields": [
                        {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                        {"name": "age", "type": "INTEGER", "mode": "NULLABLE"},
                    ],
                },
            ]
        },
    }
    tabledata_resource = {
        "rows": [
            {
                "f": [
                    {"v": {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]}},
                    {"v": {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}]}},
                ]
            },
            {
                "f": [
                    {"v": {"f": [{"v": "Bhettye Rhubble"}, {"v": "27"}]}},
                    {"v": {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]}},
                ]
            },
        ]
    }
    done_resource = copy.deepcopy(begun_resource)
    done_resource["status"] = {"state": "DONE"}
    connection = make_connection(
        begun_resource, query_resource, done_resource, tabledata_resource
    )
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    tbl = job.to_arrow(create_bqstorage_client=False)

    assert isinstance(tbl, pyarrow.Table)
    assert tbl.num_rows == 2

    # Check the schema.
    assert tbl.schema[0].name == "spouse_1"
    assert tbl.schema[0].type[0].name == "name"
    assert tbl.schema[0].type[1].name == "age"
    assert pyarrow.types.is_struct(tbl.schema[0].type)
    assert pyarrow.types.is_string(tbl.schema[0].type[0].type)
    assert pyarrow.types.is_int64(tbl.schema[0].type[1].type)
    assert tbl.schema[1].name == "spouse_2"
    assert tbl.schema[1].type[0].name == "name"
    assert tbl.schema[1].type[1].name == "age"
    assert pyarrow.types.is_struct(tbl.schema[1].type)
    assert pyarrow.types.is_string(tbl.schema[1].type[0].type)
    assert pyarrow.types.is_int64(tbl.schema[1].type[1].type)

    # Check the data.
    tbl_data = tbl.to_pydict()
    spouse_1 = tbl_data["spouse_1"]
    assert spouse_1 == [
        {"name": "Phred Phlyntstone", "age": 32},
        {"name": "Bhettye Rhubble", "age": 27},
    ]
    spouse_2 = tbl_data["spouse_2"]
    assert spouse_2 == [
        {"name": "Wylma Phlyntstone", "age": 29},
        {"name": "Bharney Rhubble", "age": 33},
    ]


@pytest.mark.skipif(pyarrow is None, reason="Requires `pyarrow`")
def test_to_arrow_max_results_no_progress_bar():
    from google.cloud.bigquery import table
    from google.cloud.bigquery.job import QueryJob as target_class
    from google.cloud.bigquery.schema import SchemaField

    connection = make_connection({})
    client = _make_client(connection=connection)
    begun_resource = _make_job_resource(job_type="query")
    job = target_class.from_api_repr(begun_resource, client)

    schema = [
        SchemaField("name", "STRING", mode="REQUIRED"),
        SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    rows = [
        {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
        {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}]},
    ]
    path = "/foo"
    api_request = mock.Mock(return_value={"rows": rows})
    row_iterator = table.RowIterator(client, api_request, path, schema)

    result_patch = mock.patch(
        "google.cloud.bigquery.job.QueryJob.result",
        return_value=row_iterator,
    )
    with result_patch as result_patch_tqdm:
        tbl = job.to_arrow(create_bqstorage_client=False, max_results=123)

    result_patch_tqdm.assert_called_once_with(max_results=123)

    assert isinstance(tbl, pyarrow.Table)
    assert tbl.num_rows == 2


@pytest.mark.skipif(pyarrow is None, reason="Requires `pyarrow`")
@pytest.mark.skipif(tqdm is None, reason="Requires `tqdm`")
@mock.patch("google.cloud.bigquery._tqdm_helpers.tqdm")
def test_to_arrow_w_tqdm_w_query_plan(tqdm_mock):
    from google.cloud.bigquery import table
    from google.cloud.bigquery.job import QueryJob as target_class
    from google.cloud.bigquery.schema import SchemaField
    from google.cloud.bigquery._tqdm_helpers import _PROGRESS_BAR_UPDATE_INTERVAL

    begun_resource = _make_job_resource(job_type="query")
    rows = [
        {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
        {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}]},
    ]

    schema = [
        SchemaField("name", "STRING", mode="REQUIRED"),
        SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    connection = make_connection({})
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    path = "/foo"
    api_request = mock.Mock(return_value={"rows": rows})
    row_iterator = table.RowIterator(client, api_request, path, schema)

    job._properties["statistics"] = {
        "query": {
            "queryPlan": [
                {"name": "S00: Input", "id": "0", "status": "COMPLETE"},
                {"name": "S01: Output", "id": "1", "status": "COMPLETE"},
            ]
        },
    }
    reload_patch = mock.patch(
        "google.cloud.bigquery.job._AsyncJob.reload", autospec=True
    )
    result_patch = mock.patch(
        "google.cloud.bigquery.job.QueryJob.result",
        side_effect=[
            concurrent.futures.TimeoutError,
            concurrent.futures.TimeoutError,
            row_iterator,
        ],
    )
    with result_patch as tqdm_mock, reload_patch:
        tbl = job.to_arrow(progress_bar_type="tqdm", create_bqstorage_client=False)

    assert tqdm_mock.call_count == 3
    assert isinstance(tbl, pyarrow.Table)
    assert tbl.num_rows == 2
    tqdm_mock.assert_called_with(
        timeout=_PROGRESS_BAR_UPDATE_INTERVAL, max_results=None
    )


@pytest.mark.skipif(pyarrow is None, reason="Requires `pyarrow`")
@pytest.mark.skipif(tqdm is None, reason="Requires `tqdm`")
@mock.patch("google.cloud.bigquery._tqdm_helpers.tqdm")
def test_to_arrow_w_tqdm_w_pending_status(tqdm_mock):
    from google.cloud.bigquery import table
    from google.cloud.bigquery.job import QueryJob as target_class
    from google.cloud.bigquery.schema import SchemaField
    from google.cloud.bigquery._tqdm_helpers import _PROGRESS_BAR_UPDATE_INTERVAL

    begun_resource = _make_job_resource(job_type="query")
    rows = [
        {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
        {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}]},
    ]

    schema = [
        SchemaField("name", "STRING", mode="REQUIRED"),
        SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    connection = make_connection({})
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    path = "/foo"
    api_request = mock.Mock(return_value={"rows": rows})
    row_iterator = table.RowIterator(client, api_request, path, schema)

    job._properties["statistics"] = {
        "query": {
            "queryPlan": [
                {"name": "S00: Input", "id": "0", "status": "PENDING"},
                {"name": "S00: Input", "id": "1", "status": "COMPLETE"},
            ]
        },
    }
    reload_patch = mock.patch(
        "google.cloud.bigquery.job._AsyncJob.reload", autospec=True
    )
    result_patch = mock.patch(
        "google.cloud.bigquery.job.QueryJob.result",
        side_effect=[concurrent.futures.TimeoutError, row_iterator],
    )
    with result_patch as tqdm_mock, reload_patch:
        tbl = job.to_arrow(progress_bar_type="tqdm", create_bqstorage_client=False)

    assert tqdm_mock.call_count == 2
    assert isinstance(tbl, pyarrow.Table)
    assert tbl.num_rows == 2
    tqdm_mock.assert_called_with(
        timeout=_PROGRESS_BAR_UPDATE_INTERVAL, max_results=None
    )


@pytest.mark.skipif(pyarrow is None, reason="Requires `pyarrow`")
@pytest.mark.skipif(tqdm is None, reason="Requires `tqdm`")
@mock.patch("google.cloud.bigquery._tqdm_helpers.tqdm")
def test_to_arrow_w_tqdm_wo_query_plan(tqdm_mock):
    from google.cloud.bigquery import table
    from google.cloud.bigquery.job import QueryJob as target_class
    from google.cloud.bigquery.schema import SchemaField

    begun_resource = _make_job_resource(job_type="query")
    rows = [
        {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
        {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}]},
    ]

    schema = [
        SchemaField("name", "STRING", mode="REQUIRED"),
        SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    connection = make_connection({})
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    path = "/foo"
    api_request = mock.Mock(return_value={"rows": rows})
    row_iterator = table.RowIterator(client, api_request, path, schema)

    reload_patch = mock.patch(
        "google.cloud.bigquery.job._AsyncJob.reload", autospec=True
    )
    result_patch = mock.patch(
        "google.cloud.bigquery.job.QueryJob.result",
        side_effect=[concurrent.futures.TimeoutError, row_iterator],
    )
    with result_patch as tqdm_mock, reload_patch:
        tbl = job.to_arrow(progress_bar_type="tqdm", create_bqstorage_client=False)

    assert tqdm_mock.call_count == 2
    assert isinstance(tbl, pyarrow.Table)
    assert tbl.num_rows == 2
    tqdm_mock.assert_called()


def _make_job(schema=(), rows=()):
    from google.cloud.bigquery.job import QueryJob as target_class

    begun_resource = _make_job_resource(job_type="query")
    query_resource = {
        "jobComplete": True,
        "jobReference": begun_resource["jobReference"],
        "totalRows": str(len(rows)),
        "schema": {
            "fields": [
                dict(name=field[0], type=field[1], mode=field[2]) for field in schema
            ]
        },
    }
    tabledata_resource = {"rows": [{"f": [{"v": v} for v in row]} for row in rows]}
    done_resource = copy.deepcopy(begun_resource)
    done_resource["status"] = {"state": "DONE"}
    connection = make_connection(
        begun_resource, query_resource, done_resource, tabledata_resource
    )
    client = _make_client(connection=connection)
    return target_class.from_api_repr(begun_resource, client)


@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_to_dataframe():
    job = _make_job(
        (("name", "STRING", "NULLABLE"), ("age", "INTEGER", "NULLABLE")),
        (
            ("Phred Phlyntstone", "32"),
            ("Bharney Rhubble", "33"),
            ("Wylma Phlyntstone", "29"),
            ("Bhettye Rhubble", "27"),
        ),
    )
    df = job.to_dataframe(create_bqstorage_client=False)

    assert isinstance(df, pandas.DataFrame)
    assert len(df) == 4  # verify the number of rows
    assert list(df) == ["name", "age"]  # verify the column names


def test_to_dataframe_ddl_query():
    from google.cloud.bigquery.job import QueryJob as target_class

    # Destination table may have no schema for some DDL and DML queries.
    resource = _make_job_resource(job_type="query", ended=True)
    query_resource = {
        "jobComplete": True,
        "jobReference": resource["jobReference"],
        "schema": {"fields": []},
    }
    connection = make_connection(query_resource)
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(resource, client)

    df = job.to_dataframe()

    assert len(df) == 0


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_to_dataframe_bqstorage(table_read_options_kwarg):
    from google.cloud.bigquery.job import QueryJob as target_class

    resource = _make_job_resource(job_type="query", ended=True)
    query_resource = {
        "jobComplete": True,
        "jobReference": resource["jobReference"],
        "totalRows": "4",
        "schema": {
            "fields": [
                {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                {"name": "age", "type": "INTEGER", "mode": "NULLABLE"},
            ]
        },
    }
    stream_id = "projects/1/locations/2/sessions/3/streams/4"
    name_array = pyarrow.array(
        ["John", "Paul", "George", "Ringo"], type=pyarrow.string()
    )
    age_array = pyarrow.array([17, 24, 21, 15], type=pyarrow.int64())
    arrow_schema = pyarrow.schema(
        [
            pyarrow.field("name", pyarrow.string(), True),
            pyarrow.field("age", pyarrow.int64(), True),
        ]
    )
    record_batch = pyarrow.RecordBatch.from_arrays(
        [name_array, age_array], schema=arrow_schema
    )
    connection = make_connection(query_resource)
    client = _make_client(connection=connection, project="bqstorage-billing-project")
    job = target_class.from_api_repr(resource, client)
    session = bigquery_storage.types.ReadSession()
    session.arrow_schema.serialized_schema = arrow_schema.serialize().to_pybytes()
    session.streams = [bigquery_storage.types.ReadStream(name=stream_id)]
    reader = mock.create_autospec(
        google.cloud.bigquery_storage_v1.reader.ReadRowsStream, instance=True
    )
    row_iterable = mock.create_autospec(
        google.cloud.bigquery_storage_v1.reader.ReadRowsIterable, instance=True
    )
    page = mock.create_autospec(
        google.cloud.bigquery_storage_v1.reader.ReadRowsPage, instance=True
    )
    page.to_arrow.return_value = record_batch
    type(row_iterable).pages = mock.PropertyMock(return_value=[page])
    reader.rows.return_value = row_iterable
    bqstorage_client = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_client.create_read_session.return_value = session
    bqstorage_client.read_rows.return_value = reader

    dataframe = job.to_dataframe(bqstorage_client=bqstorage_client)

    assert len(dataframe) == 4
    destination_table = (
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}".format(
            **resource["configuration"]["query"]["destinationTable"]
        )
    )
    expected_session = bigquery_storage.ReadSession(
        table=destination_table,
        data_format=bigquery_storage.DataFormat.ARROW,
        **table_read_options_kwarg,
    )
    bqstorage_client.create_read_session.assert_called_once_with(
        # The billing project can differ from the data project. Make sure we
        # are charging to the billing project, not the data project.
        parent="projects/bqstorage-billing-project",
        read_session=expected_session,
        max_stream_count=0,  # Use default number of streams for best performance.
        retry=None,
        timeout=None,
    )
    bqstorage_client.read_rows.assert_called_once_with(stream_id)


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_to_dataframe_bqstorage_no_pyarrow_compression():
    from google.cloud.bigquery.job import QueryJob as target_class

    resource = _make_job_resource(job_type="query", ended=True)
    query_resource = {
        "jobComplete": True,
        "jobReference": resource["jobReference"],
        "totalRows": "4",
        "schema": {"fields": [{"name": "name", "type": "STRING", "mode": "NULLABLE"}]},
    }
    connection = make_connection(query_resource)
    client = _make_client(connection=connection, project="bqstorage-billing-project")
    job = target_class.from_api_repr(resource, client)
    bqstorage_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    session = bigquery_storage.types.ReadSession()
    session.avro_schema.schema = json.dumps(
        {
            "type": "record",
            "name": "__root__",
            "fields": [{"name": "name", "type": ["null", "string"]}],
        }
    )
    bqstorage_client.create_read_session.return_value = session

    with mock.patch(
        "google.cloud.bigquery._pandas_helpers._ARROW_COMPRESSION_SUPPORT", new=False
    ):
        job.to_dataframe(bqstorage_client=bqstorage_client)

    destination_table = (
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}".format(
            **resource["configuration"]["query"]["destinationTable"]
        )
    )
    expected_session = bigquery_storage.ReadSession(
        table=destination_table,
        data_format=bigquery_storage.DataFormat.ARROW,
    )
    bqstorage_client.create_read_session.assert_called_once_with(
        # The billing project can differ from the data project. Make sure we
        # are charging to the billing project, not the data project.
        parent="projects/bqstorage-billing-project",
        read_session=expected_session,
        max_stream_count=0,
        retry=None,
        timeout=None,
    )


@pytest.mark.skipif(pyarrow is None, reason="Requires `pyarrow`")
def test_to_dataframe_column_dtypes():
    from google.cloud.bigquery.job import QueryJob as target_class

    begun_resource = _make_job_resource(job_type="query")
    query_resource = {
        "jobComplete": True,
        "jobReference": begun_resource["jobReference"],
        "totalRows": "4",
        "schema": {
            "fields": [
                {"name": "start_timestamp", "type": "TIMESTAMP"},
                {"name": "seconds", "type": "INT64"},
                {"name": "miles", "type": "FLOAT64"},
                {"name": "km", "type": "FLOAT64"},
                {"name": "payment_type", "type": "STRING"},
                {"name": "complete", "type": "BOOL"},
                {"name": "date", "type": "DATE"},
            ]
        },
    }
    row_data = [
        [
            "1433836800000000",
            "420",
            "1.1",
            "1.77",
            "Cto_dataframeash",
            "true",
            "1999-12-01",
        ],
        ["1387811700000000", "2580", "17.7", "28.5", "Cash", "false", "1953-06-14"],
        ["1385565300000000", "2280", "4.4", "7.1", "Credit", "true", "1981-11-04"],
    ]
    rows = [{"f": [{"v": field} for field in row]} for row in row_data]
    query_resource["rows"] = rows
    done_resource = copy.deepcopy(begun_resource)
    done_resource["status"] = {"state": "DONE"}
    connection = make_connection(
        begun_resource, query_resource, done_resource, query_resource
    )
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    df = job.to_dataframe(dtypes={"km": "float16"}, create_bqstorage_client=False)

    assert isinstance(df, pandas.DataFrame)
    assert len(df) == 3  # verify the number of rows
    exp_columns = [field["name"] for field in query_resource["schema"]["fields"]]
    assert list(df) == exp_columns  # verify the column names

    assert df.seconds.dtype.name == "Int64"
    assert df.miles.dtype.name == "float64"
    assert df.km.dtype.name == "float16"
    assert df.payment_type.dtype.name in {"object", "string", "str", "O"}
    assert df.complete.dtype.name == "boolean"
    assert df.date.dtype.name == "dbdate"

    if pandas.__version__.startswith(("2.", "3.")):
        assert df.start_timestamp.dtype.name == "datetime64[us, UTC]"
    else:
        assert df.start_timestamp.dtype.name == "datetime64[ns, UTC]"


def test_to_dataframe_column_date_dtypes():
    from google.cloud.bigquery.job import QueryJob as target_class

    begun_resource = _make_job_resource(job_type="query")
    query_resource = {
        "jobComplete": True,
        "jobReference": begun_resource["jobReference"],
        "totalRows": "1",
        "schema": {"fields": [{"name": "date", "type": "DATE"}]},
    }
    row_data = [
        ["1999-12-01"],
    ]
    rows = [{"f": [{"v": field} for field in row]} for row in row_data]
    query_resource["rows"] = rows
    done_resource = copy.deepcopy(begun_resource)
    done_resource["status"] = {"state": "DONE"}
    connection = make_connection(
        begun_resource, query_resource, done_resource, query_resource
    )
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)
    df = job.to_dataframe(create_bqstorage_client=False)

    assert isinstance(df, pandas.DataFrame)
    assert len(df) == 1  # verify the number of rows
    exp_columns = [field["name"] for field in query_resource["schema"]["fields"]]
    assert list(df) == exp_columns  # verify the column names
    assert df.date.dtype.name == "dbdate"


@pytest.mark.skipif(tqdm is None, reason="Requires `tqdm`")
@mock.patch("google.cloud.bigquery._tqdm_helpers.tqdm")
def test_to_dataframe_with_progress_bar(tqdm_mock):
    from google.cloud.bigquery.job import QueryJob as target_class

    begun_resource = _make_job_resource(job_type="query")
    query_resource = {
        "jobComplete": True,
        "jobReference": begun_resource["jobReference"],
        "totalRows": "4",
        "schema": {"fields": [{"name": "name", "type": "STRING", "mode": "NULLABLE"}]},
    }
    done_resource = copy.deepcopy(begun_resource)
    done_resource["status"] = {"state": "DONE"}
    connection = make_connection(
        begun_resource,
        query_resource,
        done_resource,
        query_resource,
        query_resource,
    )
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    job.to_dataframe(progress_bar_type=None, create_bqstorage_client=False)
    tqdm_mock.tqdm.assert_not_called()

    job.to_dataframe(progress_bar_type="tqdm", create_bqstorage_client=False)
    tqdm_mock.tqdm.assert_called()


@pytest.mark.skipif(tqdm is None, reason="Requires `tqdm`")
@mock.patch("google.cloud.bigquery._tqdm_helpers.tqdm")
def test_to_dataframe_w_tqdm_pending(tqdm_mock):
    from google.cloud.bigquery import table
    from google.cloud.bigquery.job import QueryJob as target_class
    from google.cloud.bigquery.schema import SchemaField
    from google.cloud.bigquery._tqdm_helpers import _PROGRESS_BAR_UPDATE_INTERVAL

    begun_resource = _make_job_resource(job_type="query")
    schema = [
        SchemaField("name", "STRING", mode="NULLABLE"),
        SchemaField("age", "INTEGER", mode="NULLABLE"),
    ]
    rows = [
        {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]},
        {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
        {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}]},
        {"f": [{"v": "Bhettye Rhubble"}, {"v": "27"}]},
    ]

    connection = make_connection({})
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    path = "/foo"
    api_request = mock.Mock(return_value={"rows": rows})
    row_iterator = table.RowIterator(client, api_request, path, schema)

    job._properties["statistics"] = {
        "query": {
            "queryPlan": [
                {"name": "S00: Input", "id": "0", "status": "PENDING"},
                {"name": "S01: Output", "id": "1", "status": "COMPLETE"},
            ]
        },
    }
    reload_patch = mock.patch(
        "google.cloud.bigquery.job._AsyncJob.reload", autospec=True
    )
    result_patch = mock.patch(
        "google.cloud.bigquery.job.QueryJob.result",
        side_effect=[concurrent.futures.TimeoutError, row_iterator],
    )
    with result_patch as tqdm_mock, reload_patch:
        df = job.to_dataframe(progress_bar_type="tqdm", create_bqstorage_client=False)

    assert tqdm_mock.call_count == 2
    assert isinstance(df, pandas.DataFrame)
    assert len(df) == 4  # verify the number of rows
    assert list(df) == ["name", "age"]  # verify the column names
    tqdm_mock.assert_called_with(
        timeout=_PROGRESS_BAR_UPDATE_INTERVAL, max_results=None
    )


@pytest.mark.skipif(tqdm is None, reason="Requires `tqdm`")
@mock.patch("google.cloud.bigquery._tqdm_helpers.tqdm")
def test_to_dataframe_w_tqdm(tqdm_mock):
    from google.cloud.bigquery import table
    from google.cloud.bigquery.job import QueryJob as target_class
    from google.cloud.bigquery.schema import SchemaField
    from google.cloud.bigquery._tqdm_helpers import _PROGRESS_BAR_UPDATE_INTERVAL

    begun_resource = _make_job_resource(job_type="query")
    schema = [
        SchemaField("name", "STRING", mode="NULLABLE"),
        SchemaField("age", "INTEGER", mode="NULLABLE"),
    ]
    rows = [
        {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]},
        {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}]},
        {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}]},
        {"f": [{"v": "Bhettye Rhubble"}, {"v": "27"}]},
    ]

    connection = make_connection({})
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    path = "/foo"
    api_request = mock.Mock(return_value={"rows": rows})
    row_iterator = table.RowIterator(client, api_request, path, schema)

    job._properties["statistics"] = {
        "query": {
            "queryPlan": [
                {"name": "S00: Input", "id": "0", "status": "COMPLETE"},
                {"name": "S01: Output", "id": "1", "status": "COMPLETE"},
            ]
        },
    }
    reload_patch = mock.patch(
        "google.cloud.bigquery.job._AsyncJob.reload", autospec=True
    )
    result_patch = mock.patch(
        "google.cloud.bigquery.job.QueryJob.result",
        side_effect=[
            concurrent.futures.TimeoutError,
            concurrent.futures.TimeoutError,
            row_iterator,
        ],
    )

    with result_patch as tqdm_mock, reload_patch:
        df = job.to_dataframe(progress_bar_type="tqdm", create_bqstorage_client=False)

    assert tqdm_mock.call_count == 3
    assert isinstance(df, pandas.DataFrame)
    assert len(df) == 4  # verify the number of rows
    assert list(df), ["name", "age"]  # verify the column names
    tqdm_mock.assert_called_with(
        timeout=_PROGRESS_BAR_UPDATE_INTERVAL, max_results=None
    )


@pytest.mark.skipif(tqdm is None, reason="Requires `tqdm`")
@mock.patch("google.cloud.bigquery._tqdm_helpers.tqdm")
def test_to_dataframe_w_tqdm_max_results(tqdm_mock):
    from google.cloud.bigquery import table
    from google.cloud.bigquery.job import QueryJob as target_class
    from google.cloud.bigquery.schema import SchemaField
    from google.cloud.bigquery._tqdm_helpers import _PROGRESS_BAR_UPDATE_INTERVAL

    begun_resource = _make_job_resource(job_type="query")
    schema = [
        SchemaField("name", "STRING", mode="NULLABLE"),
        SchemaField("age", "INTEGER", mode="NULLABLE"),
    ]
    rows = [{"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]}]

    connection = make_connection({})
    client = _make_client(connection=connection)
    job = target_class.from_api_repr(begun_resource, client)

    path = "/foo"
    api_request = mock.Mock(return_value={"rows": rows})
    row_iterator = table.RowIterator(client, api_request, path, schema)

    job._properties["statistics"] = {
        "query": {
            "queryPlan": [
                {"name": "S00: Input", "id": "0", "status": "COMPLETE"},
                {"name": "S01: Output", "id": "1", "status": "COMPLETE"},
            ]
        },
    }
    reload_patch = mock.patch(
        "google.cloud.bigquery.job._AsyncJob.reload", autospec=True
    )
    result_patch = mock.patch(
        "google.cloud.bigquery.job.QueryJob.result",
        side_effect=[concurrent.futures.TimeoutError, row_iterator],
    )
    with result_patch as tqdm_mock, reload_patch:
        job.to_dataframe(
            progress_bar_type="tqdm", create_bqstorage_client=False, max_results=3
        )

    assert tqdm_mock.call_count == 2
    tqdm_mock.assert_called_with(timeout=_PROGRESS_BAR_UPDATE_INTERVAL, max_results=3)


@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
@pytest.mark.skipif(shapely is None, reason="Requires `shapely`")
def test_to_dataframe_geography_as_object():
    job = _make_job(
        (("name", "STRING", "NULLABLE"), ("geog", "GEOGRAPHY", "NULLABLE")),
        (
            ("Phred Phlyntstone", "Point(0 0)"),
            ("Bharney Rhubble", "Point(0 1)"),
            ("Wylma Phlyntstone", None),
        ),
    )
    df = job.to_dataframe(create_bqstorage_client=False, geography_as_object=True)

    assert isinstance(df, pandas.DataFrame)
    assert len(df) == 3  # verify the number of rows
    assert list(df) == ["name", "geog"]  # verify the column names
    assert [v.__class__.__name__ for v in df.geog] == [
        "Point",
        "Point",
        "float",
    ]  # float because nan


@pytest.mark.skipif(geopandas is None, reason="Requires `geopandas`")
def test_to_geodataframe():
    job = _make_job(
        (("name", "STRING", "NULLABLE"), ("geog", "GEOGRAPHY", "NULLABLE")),
        (
            ("Phred Phlyntstone", "Point(0 0)"),
            ("Bharney Rhubble", "Point(0 1)"),
            ("Wylma Phlyntstone", None),
        ),
    )
    df = job.to_geodataframe(create_bqstorage_client=False)

    assert isinstance(df, geopandas.GeoDataFrame)
    assert len(df) == 3  # verify the number of rows
    assert list(df) == ["name", "geog"]  # verify the column names
    assert [v.__class__.__name__ for v in df.geog] == [
        "Point",
        "Point",
        "NoneType",
    ]  # float because nan
    assert isinstance(df.geog, geopandas.GeoSeries)


@pytest.mark.skipif(geopandas is None, reason="Requires `geopandas`")
@mock.patch("google.cloud.bigquery.job.query.wait_for_query")
def test_query_job_to_geodataframe_delegation(wait_for_query):
    """
    QueryJob.to_geodataframe just delegates to RowIterator.to_geodataframe.

    This test just demonstrates that. We don't need to test all the
    variations, which are tested for RowIterator.
    """
    import numpy

    job = _make_job()
    bqstorage_client = object()
    dtypes = dict(xxx=numpy.dtype("int64"))
    progress_bar_type = "normal"
    create_bqstorage_client = False
    max_results = 42
    geography_column = "g"

    df = job.to_geodataframe(
        bqstorage_client=bqstorage_client,
        dtypes=dtypes,
        progress_bar_type=progress_bar_type,
        create_bqstorage_client=create_bqstorage_client,
        max_results=max_results,
        geography_column=geography_column,
    )

    wait_for_query.assert_called_once_with(
        job, progress_bar_type, max_results=max_results
    )
    row_iterator = wait_for_query.return_value
    row_iterator.to_geodataframe.assert_called_once_with(
        bqstorage_client=bqstorage_client,
        dtypes=dtypes,
        progress_bar_type=progress_bar_type,
        create_bqstorage_client=create_bqstorage_client,
        geography_column=geography_column,
        bool_dtype=DefaultPandasDTypes.BOOL_DTYPE,
        int_dtype=DefaultPandasDTypes.INT_DTYPE,
        float_dtype=None,
        string_dtype=None,
        timeout=None,
    )
    assert df is row_iterator.to_geodataframe.return_value


@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
@mock.patch("google.cloud.bigquery.job.query.wait_for_query")
def test_query_job_to_dataframe_delegation(wait_for_query):
    job = _make_job()
    bqstorage_client = object()
    timeout = 123.45

    job.to_dataframe(bqstorage_client=bqstorage_client, timeout=timeout)

    wait_for_query.assert_called_once_with(job, None, max_results=None)
    row_iterator = wait_for_query.return_value
    row_iterator.to_dataframe.assert_called_once()
    call_args = row_iterator.to_dataframe.call_args
    assert call_args.kwargs["timeout"] == timeout


@pytest.mark.skipif(pyarrow is None, reason="Requires `pyarrow`")
@mock.patch("google.cloud.bigquery.job.query.wait_for_query")
def test_query_job_to_arrow_delegation(wait_for_query):
    job = _make_job()
    bqstorage_client = object()
    timeout = 123.45

    job.to_arrow(bqstorage_client=bqstorage_client, timeout=timeout)

    wait_for_query.assert_called_once_with(job, None, max_results=None)
    row_iterator = wait_for_query.return_value
    row_iterator.to_arrow.assert_called_once()
    call_args = row_iterator.to_arrow.call_args
    assert call_args.kwargs["timeout"] == timeout
