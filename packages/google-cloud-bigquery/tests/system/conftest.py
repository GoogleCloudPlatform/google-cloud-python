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

import pathlib
import random
import re
from typing import Tuple

import pytest
import test_utils.prefixer

from google.cloud import bigquery
from google.cloud.bigquery import enums
from . import helpers


prefixer = test_utils.prefixer.Prefixer("python-bigquery", "tests/system")

DATA_DIR = pathlib.Path(__file__).parent.parent / "data"
TOKYO_LOCATION = "asia-northeast1"


@pytest.fixture(scope="session", autouse=True)
def cleanup_datasets(bigquery_client: bigquery.Client):
    for dataset in bigquery_client.list_datasets():
        if prefixer.should_cleanup(dataset.dataset_id):
            bigquery_client.delete_dataset(
                dataset, delete_contents=True, not_found_ok=True
            )


@pytest.fixture(scope="session")
def bigquery_client():
    return bigquery.Client()


@pytest.fixture(scope="session")
def project_id(bigquery_client: bigquery.Client):
    return bigquery_client.project


@pytest.fixture(scope="session")
def bqstorage_client(bigquery_client):
    from google.cloud import bigquery_storage

    return bigquery_storage.BigQueryReadClient(credentials=bigquery_client._credentials)


@pytest.fixture(scope="session")
def dataset_id(bigquery_client):
    dataset_id = prefixer.create_prefix()
    bigquery_client.create_dataset(dataset_id)
    yield dataset_id
    bigquery_client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)


@pytest.fixture(scope="session")
def dataset_id_tokyo(bigquery_client: bigquery.Client, project_id: str):
    dataset_id = prefixer.create_prefix() + "_tokyo"
    dataset = bigquery.Dataset(f"{project_id}.{dataset_id}")
    dataset.location = TOKYO_LOCATION
    bigquery_client.create_dataset(dataset)
    yield dataset_id
    bigquery_client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)


@pytest.fixture()
def dataset_client(bigquery_client, dataset_id):
    import google.cloud.bigquery.job

    return bigquery.Client(
        default_query_job_config=google.cloud.bigquery.job.QueryJobConfig(
            default_dataset=f"{bigquery_client.project}.{dataset_id}",
        )
    )


@pytest.fixture
def table_id(dataset_id):
    return f"{dataset_id}.table_{helpers.temp_suffix()}"


def load_scalars_table(
    bigquery_client: bigquery.Client,
    project_id: str,
    dataset_id: str,
    data_path: str = "scalars.jsonl",
    source_format=enums.SourceFormat.NEWLINE_DELIMITED_JSON,
    schema_source="scalars_schema.json",
    timestamp_target_precision=None,
) -> str:
    schema = bigquery_client.schema_from_json(DATA_DIR / schema_source)
    table_id = data_path.replace(".", "_") + hex(random.randrange(1000000))
    job_config = bigquery.LoadJobConfig()
    job_config.schema = schema
    job_config.source_format = source_format
    job_config.timestamp_target_precision = timestamp_target_precision
    full_table_id = f"{project_id}.{dataset_id}.{table_id}"
    with open(DATA_DIR / data_path, "rb") as data_file:
        job = bigquery_client.load_table_from_file(
            data_file, full_table_id, job_config=job_config
        )
    job.result()
    return full_table_id


@pytest.fixture(scope="session")
def scalars_table(bigquery_client: bigquery.Client, project_id: str, dataset_id: str):
    full_table_id = load_scalars_table(bigquery_client, project_id, dataset_id)
    yield full_table_id
    bigquery_client.delete_table(full_table_id, not_found_ok=True)


@pytest.fixture(scope="session")
def scalars_table_tokyo(
    bigquery_client: bigquery.Client, project_id: str, dataset_id_tokyo: str
):
    full_table_id = load_scalars_table(bigquery_client, project_id, dataset_id_tokyo)
    yield full_table_id
    bigquery_client.delete_table(full_table_id, not_found_ok=True)


@pytest.fixture(scope="session")
def scalars_extreme_table(
    bigquery_client: bigquery.Client, project_id: str, dataset_id: str
):
    full_table_id = load_scalars_table(
        bigquery_client, project_id, dataset_id, data_path="scalars_extreme.jsonl"
    )
    yield full_table_id
    bigquery_client.delete_table(full_table_id, not_found_ok=True)


@pytest.fixture(scope="session", params=["US", TOKYO_LOCATION])
def scalars_table_multi_location(
    request, scalars_table: str, scalars_table_tokyo: str
) -> Tuple[str, str]:
    if request.param == "US":
        full_table_id = scalars_table
    elif request.param == TOKYO_LOCATION:
        full_table_id = scalars_table_tokyo
    else:
        raise ValueError(f"got unexpected location: {request.param}")
    return request.param, full_table_id


@pytest.fixture(scope="session")
def scalars_table_csv(
    bigquery_client: bigquery.Client, project_id: str, dataset_id: str
):
    full_table_id = load_scalars_table(
        bigquery_client,
        project_id,
        dataset_id,
        data_path="scalars.csv",
        source_format=enums.SourceFormat.CSV,
        schema_source="scalars_schema_csv.json",
    )
    yield full_table_id
    bigquery_client.delete_table(full_table_id, not_found_ok=True)


@pytest.fixture(scope="session")
def scalars_table_pico(
    bigquery_client: bigquery.Client, project_id: str, dataset_id: str
):
    from google.api_core import exceptions

    try:
        full_table_id = load_scalars_table(
            bigquery_client,
            project_id,
            dataset_id,
            data_path="pico.csv",
            source_format=enums.SourceFormat.CSV,
            schema_source="pico_schema.json",
            timestamp_target_precision=[12],
        )
    except exceptions.BadRequest as exc:
        if "picosecond precision" in str(exc):
            pytest.skip("Picosecond precision not supported in this environment")
        raise exc
    yield full_table_id
    bigquery_client.delete_table(full_table_id, not_found_ok=True)


@pytest.fixture
def test_table_name(request, replace_non_anum=re.compile(r"[^a-zA-Z0-9_]").sub):
    return replace_non_anum("_", request.node.name)
