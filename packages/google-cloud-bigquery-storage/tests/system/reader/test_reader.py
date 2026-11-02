# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
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
"""System tests for reading rows from tables."""

import copy
import datetime as dt
import decimal
import re
import uuid

import pytest

from google.cloud import bigquery

from .. import helpers

_TABLE_FORMAT = "projects/{}/datasets/{}/tables/{}"


@pytest.fixture
def table(project_id, dataset, bq_client):
    from google.cloud import bigquery

    schema = [
        bigquery.SchemaField("first_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("age", "INTEGER", mode="NULLABLE"),
    ]

    unique_suffix = str(uuid.uuid4()).replace("-", "_")
    table_id = "users_" + unique_suffix
    table_id_full = f"{project_id}.{dataset.dataset_id}.{table_id}"
    bq_table = bigquery.Table(table_id_full, schema=schema)
    created_table = bq_client.create_table(bq_table)

    yield created_table

    bq_client.delete_table(created_table)


def _to_bq_table_ref(table_name_string, partition_suffix=""):
    """Converts protobuf table reference to bigquery table reference.

    Args:
        table_name_string (str):
            A table name in storage API format.
            `projects/<projectid>/datasets/<datasetid>/tables/<tableid>`
        partition_suffix (str):
            An optional suffix to append to the table_id, useful for selecting
            partitions of ingestion-time partitioned tables.

    Returns:
        google.cloud.bigquery.table.TableReference
    """
    parts = table_name_string.split("/")

    return bigquery.table.TableReference.from_api_repr(
        {
            "projectId": parts[1],
            "datasetId": parts[3],
            "tableId": parts[5] + partition_suffix,
        }
    )


@pytest.mark.parametrize(
    "data_format,expected_schema_type",
    (("AVRO", "avro_schema"), ("ARROW", "arrow_schema")),
)
def test_read_rows_as_blocks_full_table(
    client_and_types,
    project_id,
    small_table_reference,
    data_format,
    expected_schema_type,
):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = small_table_reference
    read_session.data_format = data_format

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )
    stream = session.streams[0].name

    schema_type = session._pb.WhichOneof("schema")
    assert schema_type == expected_schema_type

    blocks = list(client.read_rows(stream))

    assert len(blocks) > 0


@pytest.mark.parametrize("data_format", ("AVRO", "ARROW"))
def test_read_rows_as_rows_full_table(
    client_and_types, project_id, small_table_reference, data_format
):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = small_table_reference
    read_session.data_format = data_format

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )
    stream = session.streams[0].name

    rows = list(client.read_rows(stream).rows(session))

    assert len(rows) > 0


@pytest.mark.parametrize("data_format", ("AVRO", "ARROW"))
def test_basic_nonfiltered_read(
    client_and_types, project_id, table_with_data_ref, data_format
):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = table_with_data_ref
    read_session.data_format = data_format

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )
    stream = session.streams[0].name

    rows = list(client.read_rows(stream).rows(session))

    assert len(rows) == 5  # all table rows


def test_filtered_rows_read(client_and_types, project_id, table_with_data_ref):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = table_with_data_ref
    read_session.data_format = types.DataFormat.AVRO
    read_session.read_options.row_restriction = "age >= 50"

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )
    stream = session.streams[0].name

    rows = list(client.read_rows(stream).rows(session))

    assert len(rows) == 2


@pytest.mark.parametrize("data_format", ("AVRO", "ARROW"))
def test_column_selection_read(
    client_and_types, project_id, table_with_data_ref, data_format
):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = table_with_data_ref
    read_session.data_format = data_format
    read_session.read_options.selected_fields.append("first_name")
    read_session.read_options.selected_fields.append("age")

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )
    stream = session.streams[0].name

    rows = list(client.read_rows(stream).rows(session))

    for row in rows:
        assert sorted(row.keys()) == ["age", "first_name"]


@pytest.mark.parametrize("data_format", ("AVRO", "ARROW"))
def test_snapshot(client_and_types, project_id, table, bq_client, data_format):
    client, types = client_and_types

    def load_json(data):
        return bq_client.load_table_from_json(data, table).result()

    # load original data into the table
    original_data = [
        {"first_name": "OGFoo", "last_name": "Smith", "age": 44},
        {"first_name": "OGBar", "last_name": "Jones", "age": 33},
    ]
    og_job = helpers.retry_403(load_json)(original_data)
    og_time = og_job.ended

    # load additional data into the table
    new_data = [
        {"first_name": "NewFoo", "last_name": "Smiff", "age": 43},
        {"first_name": "NewBar", "last_name": "Jomes", "age": 34},
    ]
    new_job = helpers.retry_403(load_json)(new_data)
    new_time = new_job.ended

    # Because we want our snapshot to be between when we loaded the original
    # data and when the new data was loaded, take the average of the two load
    # job completion times.
    before_new_data = og_time + ((new_time - og_time) / 2)

    # read data using the timestamp before the additional data load
    table_path = _TABLE_FORMAT.format(table.project, table.dataset_id, table.table_id)
    read_session = types.ReadSession()
    read_session.table = table_path
    read_session.table_modifiers.snapshot_time = before_new_data
    read_session.data_format = data_format

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )
    stream = session.streams[0].name

    rows = list(client.read_rows(stream).rows(session))

    # verify that only the data before the timestamp was returned
    assert len(rows) == 2  # all initial records

    for row in rows:
        assert "OG" in str(row["first_name"])
        assert "New" not in str(row["first_name"])


def test_column_partitioned_table(
    client_and_types, project_id, col_partition_table_ref, bq_client
):
    client, types = client_and_types
    data = [
        {"description": "Tracking established.", "occurred": "2017-02-15"},
        {"description": "Look, a solar eclipse!", "occurred": "2018-02-15"},
        {"description": "Fake solar eclipse reported.", "occurred": "2018-02-15"},
        {"description": "1 day after false eclipse report.", "occurred": "2018-02-16"},
        {"description": "1 year after false eclipse report.", "occurred": "2019-02-15"},
    ]

    destination = _to_bq_table_ref(col_partition_table_ref)
    bq_client.load_table_from_json(data, destination).result()

    # Read from the table with a partition filter specified, and verify that
    # only the expected data is returned.

    read_session = types.ReadSession()
    read_session.table = col_partition_table_ref
    read_session.data_format = types.DataFormat.AVRO
    read_session.read_options.row_restriction = "occurred = '2018-02-15'"

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )

    assert session.streams  # there should be some data to fetch

    stream = session.streams[0].name

    rows = list(client.read_rows(stream).rows(session))
    assert len(rows) == 2

    expected_descriptions = ("Look, a solar eclipse!", "Fake solar eclipse reported.")
    for row in rows:
        assert row["occurred"] == dt.date(2018, 2, 15)
        assert row["description"] in expected_descriptions


@pytest.mark.parametrize("data_format", ("AVRO", "ARROW"))
def test_ingestion_time_partitioned_table(
    client_and_types, project_id, ingest_partition_table_ref, bq_client, data_format
):
    client, types = client_and_types
    data = [{"shape": "cigar", "altitude": 1200}, {"shape": "disc", "altitude": 750}]
    destination = _to_bq_table_ref(
        ingest_partition_table_ref, partition_suffix="$20190809"
    )
    bq_client.load_table_from_json(data, destination).result()

    data = [
        {"shape": "sphere", "altitude": 3500},
        {"shape": "doughnut", "altitude": 100},
    ]
    destination = _to_bq_table_ref(
        ingest_partition_table_ref, partition_suffix="$20190810"
    )
    bq_client.load_table_from_json(data, destination).result()

    data = [
        {"shape": "elephant", "altitude": 1},
        {"shape": "rocket", "altitude": 12700},
    ]
    destination = _to_bq_table_ref(
        ingest_partition_table_ref, partition_suffix="$20190811"
    )
    bq_client.load_table_from_json(data, destination).result()

    read_session = types.ReadSession()
    read_session.table = ingest_partition_table_ref
    read_session.data_format = data_format
    read_session.read_options.row_restriction = "DATE(_PARTITIONTIME) = '2019-08-10'"

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )

    assert session.streams  # there should be some data to fetch

    stream = session.streams[0].name

    rows = list(client.read_rows(stream).rows(session))
    assert len(rows) == 2

    data_format = getattr(types.DataFormat, data_format)
    if data_format == types.DataFormat.AVRO:
        actual_items = {(row["shape"], row["altitude"]) for row in rows}
    elif data_format == types.DataFormat.ARROW:
        actual_items = {(row["shape"].as_py(), row["altitude"].as_py()) for row in rows}
    else:
        raise AssertionError(f"got unexpected data_format: {data_format}")

    expected_items = {("sphere", 3500), ("doughnut", 100)}
    assert actual_items == expected_items


@pytest.mark.parametrize("data_format", ("AVRO", "ARROW"))
def test_decoding_data_types(
    client_and_types, project_id, all_types_table_ref, bq_client, data_format
):
    client, types = client_and_types
    data = [
        {
            "string_field": "Price: € 9.95.",
            "bytes_field": bigquery._helpers._bytes_to_json(b"byteees"),
            "int64_field": -1085,
            "float64_field": -42.195,
            "numeric_field": "1.4142",
            "bool_field": True,
            "geography_field": '{"type": "Point", "coordinates": [-49.3028, 69.0622]}',
            "person_struct_field": {"name": "John", "age": 42},
            "timestamp_field": 1565357902.017896,  # 2019-08-09T13:38:22.017896
            "date_field": "1995-03-17",
            "time_field": "16:24:51",
            "datetime_field": "2005-10-26T19:49:41",
            "string_array_field": ["foo", "bar", "baz"],
        }
    ]

    # Explicit schema is needed to recognize bytes_field as BYTES, and not STRING.
    # Since partial schemas are not supported in load_table_from_json(), a full
    # schema needs to be specified.
    schema = [
        bigquery.SchemaField("string_field", "STRING"),
        bigquery.SchemaField("bytes_field", "BYTES"),
        bigquery.SchemaField("int64_field", "INT64"),
        bigquery.SchemaField("float64_field", "FLOAT64"),
        bigquery.SchemaField("numeric_field", "NUMERIC"),
        bigquery.SchemaField("bool_field", "BOOL"),
        bigquery.SchemaField("geography_field", "GEOGRAPHY"),
        bigquery.SchemaField(
            "person_struct_field",
            "STRUCT",
            fields=(
                bigquery.SchemaField("name", "STRING"),
                bigquery.SchemaField("age", "INT64"),
            ),
        ),
        bigquery.SchemaField("timestamp_field", "TIMESTAMP"),
        bigquery.SchemaField("date_field", "DATE"),
        bigquery.SchemaField("time_field", "TIME"),
        bigquery.SchemaField("datetime_field", "DATETIME"),
        bigquery.SchemaField("string_array_field", "STRING", mode="REPEATED"),
    ]

    job_config = bigquery.LoadJobConfig(schema=schema)
    destination = _to_bq_table_ref(all_types_table_ref)
    bq_client.load_table_from_json(data, destination, job_config=job_config).result()

    read_session = types.ReadSession()
    read_session.table = all_types_table_ref
    read_session.data_format = data_format

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )

    assert session.streams  # there should be data available

    stream = session.streams[0].name

    data_format = getattr(types.DataFormat, data_format)
    if data_format == types.DataFormat.AVRO:
        rows = list(client.read_rows(stream).rows(session))
    elif data_format == types.DataFormat.ARROW:
        rows = list(
            dict((key, value.as_py()) for key, value in row_dict.items())
            for row_dict in client.read_rows(stream).rows(session)
        )
    else:
        raise AssertionError(f"got unexpected data_format: {data_format}")

    expected_result = {
        "string_field": "Price: € 9.95.",
        "bytes_field": b"byteees",
        "int64_field": -1085,
        "float64_field": -42.195,
        "numeric_field": decimal.Decimal("1.4142"),
        "bool_field": True,
        "geography_field": "POINT(-49.3028 69.0622)",
        "person_struct_field": {"name": "John", "age": 42},
        "timestamp_field": dt.datetime(
            2019, 8, 9, 13, 38, 22, 17896, tzinfo=dt.timezone.utc
        ),
        "date_field": dt.date(1995, 3, 17),
        "time_field": dt.time(16, 24, 51),
        "string_array_field": ["foo", "bar", "baz"],
    }

    result_copy = copy.copy(rows[0])
    del result_copy["datetime_field"]
    assert result_copy == expected_result

    # Compare datetime separately, AVRO and PYARROW return different object types,
    # although they should both represent the same value.
    # TODO: when fixed, change assertion to assert a datetime instance!
    expected_pattern = re.compile(r"2005-10-26( |T)19:49:41")
    assert expected_pattern.match(str(rows[0]["datetime_field"]))


@pytest.mark.parametrize("data_format", ("AVRO", "ARROW"))
def test_resuming_read_from_offset(
    client_and_types, project_id, data_format, local_shakespeare_table_reference
):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = local_shakespeare_table_reference
    read_session.data_format = data_format

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )

    assert session.streams  # there should be data available

    stream = session.streams[0].name

    read_rows_stream = client.read_rows(stream)

    # fetch the first two batches of rows
    rows_iter = iter(read_rows_stream)
    some_rows = next(rows_iter)
    more_rows = next(rows_iter)

    # fetch the rest of the rows using the stream offset
    offset = some_rows.row_count + more_rows.row_count
    remaining_rows_count = sum(
        1 for _ in client.read_rows(stream, offset=offset).rows(session)
    )

    # verify that the counts match
    expected_len = 164656  # total rows in shakespeare table
    actual_len = remaining_rows_count + some_rows.row_count + more_rows.row_count
    assert actual_len == expected_len


def test_read_rows_to_dataframe_with_wide_table(client_and_types, project_id):
    # Use a wide table to boost the chance of getting a large message size.
    # https://github.com/googleapis/python-bigquery-storage/issues/78
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = "projects/{}/datasets/{}/tables/{}".format(
        "bigquery-public-data", "geo_census_tracts", "us_census_tracts_national"
    )
    read_session.data_format = types.DataFormat.ARROW

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )

    stream = session.streams[0].name

    read_rows_stream = client.read_rows(stream)

    # fetch the first two batches of rows
    pages_iter = iter(read_rows_stream.rows(session).pages)
    some_rows = next(pages_iter)

    assert all(len(row["tract_geom"].as_py()) > 0 for row in some_rows)


def _arrow_table(responses):
    import pyarrow

    schema, batches = None, []
    for response in responses:
        if schema is None and response.arrow_schema.serialized_schema:
            schema = pyarrow.ipc.read_schema(
                pyarrow.py_buffer(response.arrow_schema.serialized_schema)
            )
        if response.arrow_record_batch.serialized_record_batch:
            batches.append(
                pyarrow.ipc.read_record_batch(
                    pyarrow.py_buffer(
                        response.arrow_record_batch.serialized_record_batch
                    ),
                    schema,
                )
            )
    return pyarrow.Table.from_batches(batches, schema=schema)


@pytest.fixture(scope="module")
def job_default_stream(bq_client):
    job = bq_client.query(
        "SELECT x, REPEAT('A', 1000) AS repeated_str "
        "FROM UNNEST(GENERATE_ARRAY(1, 20000)) AS x ORDER BY x"
    )
    job.result()
    return (
        f"projects/{job.project}/locations/{job.location}"
        f"/jobs/{job.job_id}/streams/_default"
    )


@pytest.mark.parametrize("codec", ["LZ4_FRAME", "ZSTD"])
def test_read_rows_job_stream_with_arrow_serialization_options(
    client_v1, job_default_stream, codec
):
    plain = list(client_v1.read_rows(job_default_stream))
    compressed = list(
        client_v1.read_rows(
            job_default_stream,
            arrow_serialization_options={"buffer_compression": codec},
        )
    )

    def size(responses):
        return sum(len(r.arrow_record_batch.serialized_record_batch) for r in responses)

    assert size(compressed) < size(plain)
    assert _arrow_table(compressed).equals(_arrow_table(plain))


def test_read_rows_job_stream_cancel(client_v1, job_default_stream):
    stream = client_v1.read_rows(job_default_stream)
    messages = iter(stream)
    first = next(messages)

    stream.cancel()

    assert first.row_count > 0
    assert list(messages) == []
