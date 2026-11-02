# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
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
import datetime
import decimal

import pandas as pd
import pyarrow as pa
from google.cloud.bigquery import enums

from google.cloud import bigquery
from google.cloud.bigquery_storage_v1 import types as gapic_types
from google.cloud.bigquery_storage_v1.writer import AppendRowsStream

TABLE_LENGTH = 100_000

BQ_SCHEMA = [
    bigquery.SchemaField("bool_col", enums.SqlTypeNames.BOOLEAN),
    bigquery.SchemaField("int64_col", enums.SqlTypeNames.INT64),
    bigquery.SchemaField("float64_col", enums.SqlTypeNames.FLOAT64),
    bigquery.SchemaField("numeric_col", enums.SqlTypeNames.NUMERIC),
    bigquery.SchemaField("bignumeric_col", enums.SqlTypeNames.BIGNUMERIC),
    bigquery.SchemaField("string_col", enums.SqlTypeNames.STRING),
    bigquery.SchemaField("bytes_col", enums.SqlTypeNames.BYTES),
    bigquery.SchemaField("date_col", enums.SqlTypeNames.DATE),
    bigquery.SchemaField("datetime_col", enums.SqlTypeNames.DATETIME),
    bigquery.SchemaField("time_col", enums.SqlTypeNames.TIME),
    bigquery.SchemaField("timestamp_col", enums.SqlTypeNames.TIMESTAMP),
    bigquery.SchemaField("geography_col", enums.SqlTypeNames.GEOGRAPHY),
    bigquery.SchemaField(
        "range_date_col", enums.SqlTypeNames.RANGE, range_element_type="DATE"
    ),
    bigquery.SchemaField(
        "range_datetime_col",
        enums.SqlTypeNames.RANGE,
        range_element_type="DATETIME",
    ),
    bigquery.SchemaField(
        "range_timestamp_col",
        enums.SqlTypeNames.RANGE,
        range_element_type="TIMESTAMP",
    ),
]

PYARROW_SCHEMA = pa.schema(
    [
        pa.field("bool_col", pa.bool_()),
        pa.field("int64_col", pa.int64()),
        pa.field("float64_col", pa.float64()),
        pa.field("numeric_col", pa.decimal128(38, scale=9)),
        pa.field("bignumeric_col", pa.decimal256(76, scale=38)),
        pa.field("string_col", pa.string()),
        pa.field("bytes_col", pa.binary()),
        pa.field("date_col", pa.date32()),
        pa.field("datetime_col", pa.timestamp("us")),
        pa.field("time_col", pa.time64("us")),
        pa.field("timestamp_col", pa.timestamp("us")),
        pa.field("geography_col", pa.string()),
        pa.field(
            "range_date_col",
            pa.struct([("start", pa.date32()), ("end", pa.date32())]),
        ),
        pa.field(
            "range_datetime_col",
            pa.struct([("start", pa.timestamp("us")), ("end", pa.timestamp("us"))]),
        ),
        pa.field(
            "range_timestamp_col",
            pa.struct([("start", pa.timestamp("us")), ("end", pa.timestamp("us"))]),
        ),
    ]
)


def bqstorage_write_client():
    from google.cloud import bigquery_storage_v1

    return bigquery_storage_v1.BigQueryWriteClient()


def make_table(project_id, dataset_id, bq_client):
    table_id = "append_rows_w_arrow_test"
    table_id_full = f"{project_id}.{dataset_id}.{table_id}"
    bq_table = bigquery.Table(table_id_full, schema=BQ_SCHEMA)
    created_table = bq_client.create_table(bq_table)

    return created_table


def create_stream(bqstorage_write_client, table):
    stream_name = (
        f"projects/{table.project}/datasets/{table.dataset_id}/"
        f"tables/{table.table_id}/_default"
    )
    request_template = gapic_types.AppendRowsRequest()
    request_template.write_stream = stream_name

    # Add schema to the template.
    arrow_data = gapic_types.AppendRowsRequest.ArrowData()
    arrow_data.writer_schema.serialized_schema = PYARROW_SCHEMA.serialize().to_pybytes()
    request_template.arrow_rows = arrow_data

    append_rows_stream = AppendRowsStream(
        bqstorage_write_client,
        request_template,
    )
    return append_rows_stream


def generate_pyarrow_table(num_rows=TABLE_LENGTH):
    date_1 = datetime.date(2020, 10, 1)
    date_2 = datetime.date(2021, 10, 1)

    datetime_1 = datetime.datetime(2016, 12, 3, 14, 11, 27, 123456)
    datetime_2 = datetime.datetime(2017, 12, 3, 14, 11, 27, 123456)

    timestamp_1 = datetime.datetime(
        1999, 12, 31, 23, 59, 59, 999999, tzinfo=datetime.timezone.utc
    )
    timestamp_2 = datetime.datetime(
        2000, 12, 31, 23, 59, 59, 999999, tzinfo=datetime.timezone.utc
    )

    # Pandas Dataframe.
    rows = []
    for i in range(num_rows):
        row = {
            "bool_col": True,
            "int64_col": i,
            "float64_col": float(i),
            "numeric_col": decimal.Decimal("0.000000001"),
            "bignumeric_col": decimal.Decimal("0.1234567891"),
            "string_col": "data as string",
            "bytes_col": str.encode("data in bytes"),
            "date_col": datetime.date(2019, 5, 10),
            "datetime_col": datetime_1,
            "time_col": datetime.time(23, 59, 59, 999999),
            "timestamp_col": timestamp_1,
            "geography_col": "POINT(-121 41)",
            "range_date_col": {"start": date_1, "end": date_2},
            "range_datetime_col": {"start": datetime_1, "end": datetime_2},
            "range_timestamp_col": {"start": timestamp_1, "end": timestamp_2},
        }
        rows.append(row)
    df = pd.DataFrame(rows)

    # Dataframe to PyArrow Table.
    table = pa.Table.from_pandas(df, schema=PYARROW_SCHEMA)

    return table


def generate_write_requests(pyarrow_table):
    # Maximum size for a single AppendRowsRequest is 10 MB.
    # To be safe, we'll aim for a soft limit of 7 MB.
    max_request_bytes = 7 * 1024 * 1024  # 7 MB

    def _create_request(batches):
        """Helper to create an AppendRowsRequest from a list of batches."""
        combined_table = pa.Table.from_batches(batches)
        request = gapic_types.AppendRowsRequest()
        request.arrow_rows.rows.serialized_record_batch = (
            combined_table.combine_chunks().to_batches()[0].serialize().to_pybytes()
        )
        return request

    batches = pyarrow_table.to_batches()

    current_batches = []
    current_size = 0

    while batches:
        batch = batches.pop()
        batch_size = batch.nbytes

        # If the batch is larger than max_request_bytes, split it into 2 sub batches.
        if batch_size > max_request_bytes:
            if batch.num_rows > 1:
                # Split the batch into 2 sub batches with identical chunksizes
                mid = batch.num_rows // 2
                batch_left = batch.slice(offset=0, length=mid)
                batch_right = batch.slice(offset=mid)

                # Append the new batches into the stack and continue poping.
                batches.append(batch_left)
                batches.append(batch_right)
                continue
            # If the batch is single row and still larger than max_request_bytes
            else:
                raise ValueError(
                    f"A single PyArrow batch of one row is larger than the maximum request size "
                    f"(batch size: {batch_size} > max request size: {max_request_bytes}). Cannot proceed."
                )
        # The current batches are ok to form a request when next batch will exceed the max_request_bytes.
        if current_size + batch_size > max_request_bytes:
            # Current batches can't be empty otherwise it will suffice batch_size > max_request_bytes above.
            yield _create_request(current_batches)

            current_batches = []
            current_size = 0
            batches.append(batch)

        # Otherwise, add the batch into current_batches
        else:
            current_batches.append(batch)
            current_size += batch_size

    # Flush remaining batches
    if current_batches:
        yield _create_request(current_batches)


def verify_result(client, table, futures):
    bq_table = client.get_table(table)

    # Verify table schema.
    assert bq_table.schema == BQ_SCHEMA

    # Verify table size.
    query = client.query(f"SELECT DISTINCT int64_col FROM `{bq_table}`;")
    query_result = query.result().to_dataframe()

    assert len(query_result) == TABLE_LENGTH

    # Verify that table was split into multiple requests.
    assert len(futures) == 4


def main(project_id, dataset):
    # Initialize clients.
    write_client = bqstorage_write_client()
    bq_client = bigquery.Client()

    # Create BigQuery table.
    bq_table = make_table(project_id, dataset.dataset_id, bq_client)

    # Generate local PyArrow table.
    pa_table = generate_pyarrow_table()

    # Convert PyArrow table to Protobuf requests.
    requests = generate_write_requests(pa_table)

    # Create writing stream to the BigQuery table.
    stream = create_stream(write_client, bq_table)

    # Send requests.
    futures = []
    for request in requests:
        future = stream.send(request)
        futures.append(future)
        future.result()  # Optional, will block until writing is complete.

    # Verify results.
    verify_result(bq_client, bq_table, futures)
