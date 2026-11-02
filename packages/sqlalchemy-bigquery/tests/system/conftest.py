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

import pathlib
from typing import List

import pytest
import sqlalchemy
import test_utils.prefixer
import test_utils.retry
from google.api_core import exceptions
from google.cloud import bigquery

from sqlalchemy_bigquery import BigQueryDialect

prefixer = test_utils.prefixer.Prefixer("python-bigquery-sqlalchemy", "tests/system")

DATA_DIR = pathlib.Path(__file__).parent / "data"


def load_sample_data(
    full_table_id: str,
    bigquery_client: bigquery.Client,
    bigquery_schema: List[bigquery.SchemaField],
    filename: str = "sample.json",
):
    sample_config = bigquery.LoadJobConfig()
    sample_config.destination_table_description = (
        "A sample table containing most data types."
    )
    sample_config.schema = bigquery_schema
    sample_config.time_partitioning = bigquery.TimePartitioning(field="timestamp")
    sample_config.clustering_fields = ["integer", "string"]
    sample_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    sample_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

    with open(DATA_DIR / filename, "rb") as data_file:
        return bigquery_client.load_table_from_file(
            data_file,
            full_table_id,
            job_config=sample_config,
        )


@pytest.fixture(scope="session")
def bigquery_client():
    return bigquery.Client()


@pytest.fixture(scope="session")
def bigquery_schema(bigquery_client: bigquery.Client):
    return bigquery_client.schema_from_json(DATA_DIR / "schema.json")


@pytest.fixture(scope="session")
def bigquery_dataset(
    bigquery_client: bigquery.Client, bigquery_schema: List[bigquery.SchemaField]
):
    project_id = bigquery_client.project
    dataset_id = prefixer.create_prefix()
    dataset = bigquery.Dataset(f"{project_id}.{dataset_id}")
    dataset = bigquery_client.create_dataset(dataset)
    sample_table_id = f"{project_id}.{dataset_id}.sample"
    job1 = load_sample_data(sample_table_id, bigquery_client, bigquery_schema)
    job1.result()
    one_row_table_id = f"{project_id}.{dataset_id}.sample_one_row"
    job2 = load_sample_data(
        one_row_table_id,
        bigquery_client,
        bigquery_schema,
        filename="sample_one_row.json",
    )
    job2.result()
    view = bigquery.Table(
        f"{project_id}.{dataset_id}.sample_view",
    )
    view.view_query = f"SELECT string FROM `{dataset_id}.sample`"
    bigquery_client.create_table(view)
    yield dataset_id
    bigquery_client.delete_dataset(dataset_id, delete_contents=True)


@pytest.fixture(scope="session", autouse=True)
def bigquery_empty_table(
    bigquery_dataset: str,
    bigquery_client: bigquery.Client,
    bigquery_schema: List[bigquery.SchemaField],
):
    project_id = bigquery_client.project
    # Create new table in its own dataset.
    dataset_id = bigquery_dataset
    table_id = f"{project_id}.{dataset_id}.sample_dml_empty"
    empty_table = bigquery.Table(table_id, schema=bigquery_schema)
    bigquery_client.create_table(empty_table)
    return table_id


@pytest.fixture(scope="session")
def bigquery_regional_dataset(bigquery_client, bigquery_schema):
    project_id = bigquery_client.project
    dataset_id = prefixer.create_prefix()
    dataset = bigquery.Dataset(f"{project_id}.{dataset_id}")
    dataset.location = "asia-northeast1"
    dataset = bigquery_client.create_dataset(dataset)
    sample_table_id = f"{project_id}.{dataset_id}.sample_one_row"
    job = load_sample_data(
        sample_table_id,
        bigquery_client,
        bigquery_schema,
        filename="sample_one_row.json",
    )
    job.result()
    yield dataset_id
    bigquery_client.delete_dataset(dataset_id, delete_contents=True)


@pytest.fixture(autouse=True)
def cleanup_extra_tables(bigquery_client, bigquery_dataset):
    common = "sample", "sample_one_row", "sample_view", "sample_dml_empty"
    # Back-end may raise 403 for a dataset not ready yet.
    retry_403 = test_utils.retry.RetryErrors(exceptions.Forbidden)
    tables = retry_403(bigquery_client.list_tables)(bigquery_dataset)
    for table in tables:
        if table.table_id not in common:
            bigquery_client.delete_table(table)


@pytest.fixture(scope="session", autouse=True)
def cleanup_datasets(bigquery_client: bigquery.Client):
    for dataset in bigquery_client.list_datasets():
        if prefixer.should_cleanup(dataset.dataset_id):
            bigquery_client.delete_dataset(
                dataset, delete_contents=True, not_found_ok=True
            )


@pytest.fixture(scope="session")
def engine():
    engine = sqlalchemy.create_engine("bigquery://", echo=True)
    return engine


@pytest.fixture(scope="session")
def dialect():
    return BigQueryDialect()


@pytest.fixture
def metadata():
    return sqlalchemy.MetaData()
