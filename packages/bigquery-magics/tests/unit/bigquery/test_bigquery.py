# Copyright 2018 Google LLC
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

import contextlib
import copy
import json
import os
import pathlib
import re
import sys
import tempfile
import warnings
from concurrent import futures
from unittest import mock

import google.auth.credentials
import google.cloud.bigquery._http
import google.cloud.bigquery.exceptions
import IPython
import IPython.utils.io as io
import pandas
import pytest
from google.api_core import exceptions
from google.cloud import bigquery
from google.cloud.bigquery import exceptions as bq_exceptions
from google.cloud.bigquery import job, table
from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
from IPython.testing import globalipapp

import bigquery_magics
import bigquery_magics.bigquery as magics
import bigquery_magics.graph_server as graph_server

try:
    import google.cloud.bigquery_storage as bigquery_storage
except ImportError:
    bigquery_storage = None

try:
    import bigframes.pandas as bpd
except ImportError:
    bpd = None

try:
    import spanner_graphs.graph_visualization as graph_visualization
except ImportError:
    graph_visualization = None

try:
    import geopandas as gpd
except ImportError:
    gpd = None

Path = pathlib.Path


def make_connection(*args):
    # TODO(tswast): Remove this in favor of a mock google.cloud.bigquery.Client
    # in tests.
    conn = mock.create_autospec(google.cloud.bigquery._http.Connection, instance=True)
    conn.api_request.side_effect = args
    return conn


PROJECT_ID = "its-a-project-eh"
JOB_ID = "some-random-id"
JOB_REFERENCE_RESOURCE = {"projectId": PROJECT_ID, "jobId": JOB_ID}
DATASET_ID = "dest_dataset"
TABLE_ID = "dest_table"
TABLE_REFERENCE_RESOURCE = {
    "projectId": PROJECT_ID,
    "datasetId": DATASET_ID,
    "tableId": TABLE_ID,
}
QUERY_STRING = "SELECT 42 AS the_answer FROM `life.the_universe.and_everything`;"
QUERY_RESOURCE = {
    "jobReference": JOB_REFERENCE_RESOURCE,
    "configuration": {
        "query": {
            "destinationTable": TABLE_REFERENCE_RESOURCE,
            "query": QUERY_STRING,
            "queryParameters": [],
            "useLegacySql": False,
        }
    },
    "status": {"state": "DONE"},
}
QUERY_RESULTS_RESOURCE = {
    "jobReference": JOB_REFERENCE_RESOURCE,
    "totalRows": 1,
    "jobComplete": True,
    "schema": {"fields": [{"name": "the_answer", "type": "INTEGER"}]},
}


def test_context_with_default_connection():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._credentials = None
    bigquery_magics.context._project = None
    bigquery_magics.context._connection = None

    default_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    credentials_patch = mock.patch(
        "google.auth.default", return_value=(default_credentials, "project-from-env")
    )
    default_conn = make_connection(QUERY_RESOURCE, QUERY_RESULTS_RESOURCE)
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)
    list_rows_patch = mock.patch(
        "google.cloud.bigquery.client.Client._list_rows_from_query_results",
        return_value=google.cloud.bigquery.table._EmptyRowIterator(),
    )

    with conn_patch as conn, credentials_patch, list_rows_patch as list_rows:
        conn.return_value = default_conn
        ip.run_cell_magic("bigquery", "", QUERY_STRING)

    # Check that query actually starts the job.
    conn.assert_called()
    list_rows.assert_called()
    begin_call = mock.call(
        method="POST",
        path="/projects/project-from-env/jobs",
        data=mock.ANY,
        timeout=DEFAULT_TIMEOUT,
    )
    query_results_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT_ID}/queries/{JOB_ID}",
        query_params=mock.ANY,
        timeout=mock.ANY,
        headers=mock.ANY,
    )
    default_conn.api_request.assert_has_calls([begin_call, query_results_call])


def test_context_with_custom_connection():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None
    bigquery_magics.context._credentials = None
    context_conn = bigquery_magics.context._connection = make_connection(
        QUERY_RESOURCE, QUERY_RESULTS_RESOURCE
    )

    default_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    credentials_patch = mock.patch(
        "google.auth.default", return_value=(default_credentials, "project-from-env")
    )
    default_conn = make_connection()
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)
    list_rows_patch = mock.patch(
        "google.cloud.bigquery.client.Client._list_rows_from_query_results",
        return_value=google.cloud.bigquery.table._EmptyRowIterator(),
    )

    with conn_patch as conn, credentials_patch, list_rows_patch as list_rows:
        conn.return_value = default_conn
        ip.run_cell_magic("bigquery", "", QUERY_STRING)

    list_rows.assert_called()
    default_conn.api_request.assert_not_called()
    begin_call = mock.call(
        method="POST",
        path="/projects/project-from-env/jobs",
        data=mock.ANY,
        timeout=DEFAULT_TIMEOUT,
    )
    query_results_call = mock.call(
        method="GET",
        path=f"/projects/{PROJECT_ID}/queries/{JOB_ID}",
        query_params=mock.ANY,
        timeout=mock.ANY,
        headers=mock.ANY,
    )
    context_conn.api_request.assert_has_calls([begin_call, query_results_call])


def test__run_query():
    bigquery_magics.context._credentials = None

    job_id = "job_1234"
    sql = "SELECT 17"
    responses = [
        futures.TimeoutError,
        futures.TimeoutError,
        [table.Row((17,), {"num": 0})],
    ]

    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)
    with client_patch as client_mock, io.capture_output() as captured:
        client_mock().query(sql).result.side_effect = responses
        client_mock().query(sql).job_id = job_id

        query_job = magics._run_query(client_mock(), sql)

    lines = re.split("\n|\r", captured.stdout)
    # Removes blanks & terminal code (result of display clearing)
    updates = list(filter(lambda x: bool(x) and x != "\x1b[2K", lines))

    assert query_job.job_id == job_id
    expected_first_line = "Executing query with job ID: {}".format(job_id)
    assert updates[0] == expected_first_line
    execution_updates = updates[1:-1]
    assert len(execution_updates) == 3  # one update per API response
    for line in execution_updates:
        assert re.match("Query executing: .*s", line)


def test__run_query_dry_run_without_errors_is_silent():
    bigquery_magics.context._credentials = None

    sql = "SELECT 17"

    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)

    job_config = job.QueryJobConfig()
    job_config.dry_run = True
    with client_patch as client_mock, io.capture_output() as captured:
        client_mock().query(sql).job_id = None
        magics._run_query(client_mock(), sql, job_config=job_config)

    assert len(captured.stderr) == 0
    assert len(captured.stdout) == 0


def test__get_graph_schema_exception():
    bq_client = mock.create_autospec(bigquery.Client, instance=True)
    bq_client.query.side_effect = Exception("error")
    query_text = "GRAPH foo.bar"
    query_job = mock.Mock()

    graph_ref = mock.Mock()
    graph_ref.project = "my-project"
    graph_ref.dataset_id = "dataset"
    graph_ref.property_graph_id = "graph"
    query_job.referenced_property_graphs = [graph_ref]

    assert magics._get_graph_schema(bq_client, query_text, query_job) is None


def test__get_graph_schema_zero_references():
    bq_client = mock.create_autospec(bigquery.Client, instance=True)
    query_job = mock.Mock()
    query_job.referenced_property_graphs = []

    assert magics._get_graph_schema(bq_client, "SELECT 1", query_job) is None


def test__get_graph_schema_two_references():
    bq_client = mock.create_autospec(bigquery.Client, instance=True)
    query_job = mock.Mock()

    ref1 = mock.Mock()
    ref2 = mock.Mock()
    query_job.referenced_property_graphs = [ref1, ref2]

    assert magics._get_graph_schema(bq_client, "SELECT 1", query_job) is None


def test__get_graph_schema_success():
    bq_client = mock.create_autospec(bigquery.Client, instance=True)
    query_job = mock.Mock()

    graph_ref = mock.Mock()
    graph_ref.project = "my-project"
    graph_ref.dataset_id = "dataset"
    graph_ref.property_graph_id = "graph"
    query_job.referenced_property_graphs = [graph_ref]

    mock_df = mock.MagicMock()
    mock_df.shape = (1, 1)
    mock_df.iloc.__getitem__.return_value = "schema_json"
    bq_client.query.return_value.to_dataframe.return_value = mock_df

    with mock.patch(
        "bigquery_magics.bigquery.graph_server._convert_schema"
    ) as convert_mock:
        convert_mock.return_value = {"nodes": [], "edges": []}

        result = magics._get_graph_schema(bq_client, "SELECT 1", query_job)

        assert result == {"nodes": [], "edges": []}
        convert_mock.assert_called_once_with("schema_json")

        called_query = bq_client.query.call_args[0][0]
        assert (
            "FROM `my-project.dataset`.INFORMATION_SCHEMA.PROPERTY_GRAPHS"
            in called_query
        )

        called_config = bq_client.query.call_args[1]["job_config"]
        called_params = called_config.query_parameters
        assert len(called_params) == 1
        assert called_params[0].name == "graph_id"
        assert called_params[0].value == "graph"


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test__make_bqstorage_client():
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    test_client = bigquery.Client(
        project="test_project", credentials=credentials_mock, location="test_location"
    )
    got = magics._make_bqstorage_client(test_client, {})
    assert isinstance(got, bigquery_storage.BigQueryReadClient)


def test__make_bqstorage_client_true_raises_import_error(missing_bq_storage):
    """When package `google-cloud-bigquery-storage` is not installed, reports
    ImportError.
    """
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    test_client = bigquery.Client(
        project="test_project", credentials=credentials_mock, location="test_location"
    )

    with pytest.raises(ImportError) as exc_context, missing_bq_storage:
        magics._make_bqstorage_client(test_client, {})

    error_msg = str(exc_context.value)
    assert "google-cloud-bigquery-storage" in error_msg
    assert "pyarrow" in error_msg


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test__make_bqstorage_client_true_obsolete_dependency():
    """When package `google-cloud-bigquery-storage` is installed but has outdated
    version, returns None, and raises a warning.
    """
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    test_client = bigquery.Client(
        project="test_project", credentials=credentials_mock, location="test_location"
    )

    patcher = mock.patch(
        "bigquery_magics._versions_helpers.BQ_STORAGE_VERSIONS.try_import",
        side_effect=bq_exceptions.LegacyBigQueryStorageError(
            "google-cloud-bigquery-storage is outdated"
        ),
    )
    with (
        patcher,
        pytest.raises(google.cloud.bigquery.exceptions.LegacyBigQueryStorageError),
    ):
        magics._make_bqstorage_client(test_client, {})


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test__make_bqstorage_client_true_missing_gapic(missing_grpcio_lib):
    with pytest.raises(ImportError) as exc_context, missing_grpcio_lib:
        magics._make_bqstorage_client(True, {})

    assert "grpcio" in str(exc_context.value)


def test__create_dataset_if_necessary_exists():
    project = "project_id"
    dataset_id = "dataset_id"
    dataset_reference = bigquery.dataset.DatasetReference(project, dataset_id)
    dataset = bigquery.Dataset(dataset_reference)
    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)
    with client_patch as client_mock:
        client = client_mock()
        client.project = project
        client.get_dataset.result_value = dataset
        magics._create_dataset_if_necessary(client, dataset_id)
        client.create_dataset.assert_not_called()


def test__create_dataset_if_necessary_not_exist():
    project = "project_id"
    dataset_id = "dataset_id"
    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)
    with client_patch as client_mock:
        client = client_mock()
        client.location = "us"
        client.project = project
        client.get_dataset.side_effect = exceptions.NotFound("dataset not found")
        magics._create_dataset_if_necessary(client, dataset_id)
        client.create_dataset.assert_called_once()


@pytest.mark.parametrize(
    ("magic_name",),
    (("bigquery",),),
)
def test_extension_load(magic_name):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    # verify that the magic is registered and has the correct source
    magic = ip.magics_manager.magics["cell"].get(magic_name)
    assert magic.__module__ == "bigquery_magics.bigquery"


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_without_optional_arguments(monkeypatch):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result

    with run_query_patch as run_query_mock, bqstorage_client_patch:
        run_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "", sql)

    assert bqstorage_mock.called  # BQ storage client was used
    assert isinstance(return_value, pandas.DataFrame)
    assert len(return_value) == len(result)  # verify row count
    assert list(return_value) == list(result)  # verify column names


@pytest.mark.skipif(
    graph_visualization is not None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` to be missing and `google-cloud-bigquery-storage` to be present",
)
def test_bigquery_graph_spanner_graph_notebook_missing(monkeypatch):
    """If `spanner-graph-notebook` is not installed, the graph visualizer
    widget cannot be displayed.
    """
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )
    display_patch = mock.patch("IPython.display.display", autospec=True)

    sql = "SELECT 3 AS result"
    result = pandas.DataFrame(["abc"], columns=["s"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "--graph", sql)

        # Since the query result is not valid JSON, the visualizer should not be displayed.
        display_mock.assert_not_called()

    assert bqstorage_mock.called  # BQ storage client was used
    assert isinstance(return_value, pandas.DataFrame)
    assert len(return_value) == len(result)  # verify row count
    assert list(return_value) == list(result)  # verify column names


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_int_result(monkeypatch):
    """Graph visualization of integer scalars is supported."""
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )
    display_patch = mock.patch("IPython.display.display", autospec=True)

    sql = "SELECT 3 AS result"
    result = pandas.DataFrame(["abc"], columns=["s"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "--graph", sql)

        # Since the query result is not valid JSON, the visualizer should not be displayed.
        display_mock.assert_not_called()

    assert bqstorage_mock.called  # BQ storage client was used
    assert isinstance(return_value, pandas.DataFrame)
    assert len(return_value) == len(result)  # verify row count
    assert list(return_value) == list(result)  # verify column names


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_str_result(monkeypatch):
    """Graph visualization of string scalars is supported."""
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )
    display_patch = mock.patch("IPython.display.display", autospec=True)

    sql = "SELECT 'abc' AS s"
    result = pandas.DataFrame(["abc"], columns=["s"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "--graph", sql)

        # Since the query result is not valid JSON, the visualizer should not be displayed.
        display_mock.assert_not_called()

    assert bqstorage_mock.called  # BQ storage client was used
    assert isinstance(return_value, pandas.DataFrame)
    assert len(return_value) == len(result)  # verify row count
    assert list(return_value) == list(result)  # verify column names


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_json_json_result(monkeypatch):
    """Graph visualization of JSON objects with valid JSON string fields is supported."""
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)
    monkeypatch.setattr(bigquery_magics.context, "_project", PROJECT_ID)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )
    display_patch = mock.patch("IPython.display.display", autospec=True)

    sql = "SELECT graph_json, graph_json AS graph_json2 FROM t"
    graph_json_rows = [
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI=","kind":"node","labels":["Person"],"properties":{"birthday":"1991-12-21T08:00:00Z","city":"Adelaide","country":"Australia","id":1,"name":"Alex"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJECkQ6ZRmluR3JhcGguUGVyc29uAHiRAplGaW5HcmFwaC5BY2NvdW50AHiRDg==","kind":"edge","labels":["Owns"],"properties":{"account_id":7,"create_time":"2020-01-10T14:22:20.222Z","id":1},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-10T14:22:20.222Z","id":7,"is_blocked":false,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY=","kind":"node","labels":["Person"],"properties":{"birthday":"1986-12-07T08:00:00Z","city":"Kollam","country":"India","id":3,"name":"Lee"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEGkSCZRmluR3JhcGguUGVyc29uAHiRBplGaW5HcmFwaC5BY2NvdW50AHiRIA==","kind":"edge","labels":["Owns"],"properties":{"account_id":16,"create_time":"2020-02-18T13:44:20.655Z","id":3},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-28T01:55:09.206Z","id":16,"is_blocked":true,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ=","kind":"node","labels":["Person"],"properties":{"birthday":"1980-10-31T08:00:00Z","city":"Moravia","country":"Czech_Republic","id":2,"name":"Dana"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEEkSiZRmluR3JhcGguUGVyc29uAHiRBJlGaW5HcmFwaC5BY2NvdW50AHiRKA==","kind":"edge","labels":["Owns"],"properties":{"account_id":20,"create_time":"2020-01-28T01:55:09.206Z","id":2},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","kind":"node","labels":["Account"],"properties":{"create_time":"2020-02-18T13:44:20.655Z","id":20,"is_blocked":false,"nick_name":"Rainy Day Fund"}}]
        """,
    ]
    result = pandas.DataFrame(
        {"graph_json": graph_json_rows, "graph_json2": graph_json_rows},
        columns=["graph_json", "graph_json2"],
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    query_job_mock.configuration.destination.project = PROJECT_ID
    query_job_mock.configuration.destination.dataset_id = DATASET_ID
    query_job_mock.configuration.destination.table_id = TABLE_ID

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock
        try:
            return_value = ip.run_cell_magic("bigquery", "--graph", sql)
        finally:
            graph_server.graph_server.stop_server()

        display_mock.assert_called()

    assert bqstorage_mock.called  # BQ storage client was used
    assert return_value is None


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_json_result(monkeypatch):
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)
    monkeypatch.setattr(bigquery_magics.context, "_project", PROJECT_ID)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT graph_json FROM t"
    graph_json_rows = [
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI=","kind":"node","labels":["Person"],"properties":{"birthday":"1991-12-21T08:00:00Z","city":"Adelaide","country":"Australia","id":1,"name":"Alex"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJECkQ6ZRmluR3JhcGguUGVyc29uAHiRAplGaW5HcmFwaC5BY2NvdW50AHiRDg==","kind":"edge","labels":["Owns"],"properties":{"account_id":7,"create_time":"2020-01-10T14:22:20.222Z","id":1},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-10T14:22:20.222Z","id":7,"is_blocked":false,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY=","kind":"node","labels":["Person"],"properties":{"birthday":"1986-12-07T08:00:00Z","city":"Kollam","country":"India","id":3,"name":"Lee"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEGkSCZRmluR3JhcGguUGVyc29uAHiRBplGaW5HcmFwaC5BY2NvdW50AHiRIA==","kind":"edge","labels":["Owns"],"properties":{"account_id":16,"create_time":"2020-02-18T13:44:20.655Z","id":3},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-28T01:55:09.206Z","id":16,"is_blocked":true,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ=","kind":"node","labels":["Person"],"properties":{"birthday":"1980-10-31T08:00:00Z","city":"Moravia","country":"Czech_Republic","id":2,"name":"Dana"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEEkSiZRmluR3JhcGguUGVyc29uAHiRBJlGaW5HcmFwaC5BY2NvdW50AHiRKA==","kind":"edge","labels":["Owns"],"properties":{"account_id":20,"create_time":"2020-01-28T01:55:09.206Z","id":2},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","kind":"node","labels":["Account"],"properties":{"create_time":"2020-02-18T13:44:20.655Z","id":20,"is_blocked":false,"nick_name":"Rainy Day Fund"}}]
        """,
    ]
    result = pandas.DataFrame(graph_json_rows, columns=["graph_json"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    display_patch = mock.patch("IPython.display.display", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    query_job_mock.configuration.destination.project = PROJECT_ID
    query_job_mock.configuration.destination.dataset_id = DATASET_ID
    query_job_mock.configuration.destination.table_id = TABLE_ID

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock

        return_value = ip.run_cell_magic("bigquery", "--graph", sql)

        assert len(display_mock.call_args_list) == 1
        assert len(display_mock.call_args_list[0]) == 2

        # Sanity check that the HTML content looks like graph visualization. Minimal check
        # to allow Spanner to change its implementation without breaking this test.
        html_content = display_mock.call_args_list[0][0][0].data
        assert "<script>" in html_content
        assert "</script>" in html_content
        # Verify that the query results are embedded into the HTML, allowing them to be visualized.
        # Due to escaping, it is not possible check for graph_json_rows exactly, so we check for a few
        # sentinel strings within the query results, instead.
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQI=" in html_content
        )  # identifier in 1st row of query result
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQY=" in html_content
        )  # identifier in 2nd row of query result
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQQ=" in html_content
        )  # identifier in 3rd row of query result

        # Verify that args are present in the HTML.
        assert '\\"args\\": {' in html_content
        assert '\\"bigquery_api_endpoint\\": null' in html_content
        assert '\\"project\\": null' in html_content
        assert '\\"location\\": null' in html_content

        # Make sure we can run a second graph query, after the graph server is already running.
        try:
            return_value = ip.run_cell_magic("bigquery", "--graph", sql)
        finally:
            graph_server.graph_server.stop_server()

        # Sanity check that the HTML content looks like graph visualization. Minimal check
        # to allow Spanner to change its implementation without breaking this test.
        html_content = display_mock.call_args_list[0][0][0].data
        assert "<script>" in html_content
        assert "</script>" in html_content
        # Verify that the query results are embedded into the HTML, allowing them to be visualized.
        # Due to escaping, it is not possible check for graph_json_rows exactly, so we check for a few
        # sentinel strings within the query results, instead.
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQI=" in html_content
        )  # identifier in 1st row of query result
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQY=" in html_content
        )  # identifier in 2nd row of query result
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQQ=" in html_content
        )  # identifier in 3rd row of query result

        # Verify that args are present in the HTML.
        assert '\\"args\\": {' in html_content
        assert '\\"bigquery_api_endpoint\\": null' in html_content
        assert '\\"project\\": null' in html_content
        assert '\\"location\\": null' in html_content

    assert bqstorage_mock.called  # BQ storage client was used
    assert return_value is None


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_size_exceeds_max(monkeypatch):
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)
    monkeypatch.setattr(bigquery_magics.context, "_project", PROJECT_ID)

    # Set threshold to a very small value to trigger the error.
    monkeypatch.setattr(magics, "MAX_GRAPH_VISUALIZATION_SIZE", 5)

    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT graph_json FROM t"
    result = pandas.DataFrame(['{"id": 1}'], columns=["graph_json"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    display_patch = mock.patch("IPython.display.display", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    query_job_mock.configuration.destination.project = PROJECT_ID
    query_job_mock.configuration.destination.dataset_id = DATASET_ID
    query_job_mock.configuration.destination.table_id = TABLE_ID

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock

        ip.run_cell_magic("bigquery", "--graph", sql)

        # Should display error message
        assert display_mock.called
        html_content = display_mock.call_args[0][0].data
        assert (
            "Error:</b> The query result is too large for graph visualization."
            in html_content
        )


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_size_exceeds_query_result_max(monkeypatch):
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)
    monkeypatch.setattr(bigquery_magics.context, "_project", PROJECT_ID)

    # Set threshold to a very small value, but larger than the other one.
    # We want estimated_size > MAX_GRAPH_VISUALIZATION_QUERY_RESULT_SIZE
    # and estimated_size <= MAX_GRAPH_VISUALIZATION_SIZE
    monkeypatch.setattr(magics, "MAX_GRAPH_VISUALIZATION_SIZE", 1000000)
    monkeypatch.setattr(magics, "MAX_GRAPH_VISUALIZATION_QUERY_RESULT_SIZE", 5)

    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT graph_json FROM t"
    result = pandas.DataFrame(['{"id": 1977323800}'], columns=["graph_json"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    display_patch = mock.patch("IPython.display.display", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    query_job_mock.configuration.destination.project = PROJECT_ID
    query_job_mock.configuration.destination.dataset_id = DATASET_ID
    query_job_mock.configuration.destination.table_id = TABLE_ID

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock

        ip.run_cell_magic("bigquery", "--graph", sql)

        # Should display visualization but without query_result embedded.
        assert display_mock.called
        html_content = display_mock.call_args[0][0].data
        assert "<script>" in html_content
        assert "1977323800" not in html_content


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_with_args_serialization(monkeypatch):
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)
    monkeypatch.setattr(bigquery_magics.context, "_project", PROJECT_ID)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )
    display_patch = mock.patch("IPython.display.display", autospec=True)

    sql = "SELECT graph_json FROM t"
    graph_json_rows = [
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI=","kind":"node","labels":["Person"],"properties":{"id":1}}]
        """
    ]
    result = pandas.DataFrame(graph_json_rows, columns=["graph_json"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    query_job_mock.configuration.destination.project = PROJECT_ID
    query_job_mock.configuration.destination.dataset_id = DATASET_ID
    query_job_mock.configuration.destination.table_id = TABLE_ID

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock

        endpoint = "https://example.com"
        project = "my-project"
        location = "us-west1"
        magic_args = (
            f"--graph --bigquery_api_endpoint={endpoint} "
            f"--project={project} --location={location}"
        )
        ip.run_cell_magic("bigquery", magic_args, sql)

        assert display_mock.called
        html_content = display_mock.call_args_list[0][0][0].data

        # Verify that args are present in the HTML with their assigned values.
        assert '\\"args\\": {' in html_content
        assert f'\\"bigquery_api_endpoint\\": \\"{endpoint}\\"' in html_content
        assert f'\\"project\\": \\"{project}\\"' in html_content
        assert f'\\"location\\": \\"{location}\\"' in html_content


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_bigquery_graph_colab(monkeypatch):
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    # Mock the colab module so the code under test uses colab.register_callback(), rather than
    # GraphServer.
    sys.modules["google.colab"] = mock.Mock()

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)
    monkeypatch.setattr(bigquery_magics.context, "_project", PROJECT_ID)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT graph_json FROM t"
    graph_json_rows = [
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI=","kind":"node","labels":["Person"],"properties":{"birthday":"1991-12-21T08:00:00Z","city":"Adelaide","country":"Australia","id":1,"name":"Alex"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJECkQ6ZRmluR3JhcGguUGVyc29uAHiRAplGaW5HcmFwaC5BY2NvdW50AHiRDg==","kind":"edge","labels":["Owns"],"properties":{"account_id":7,"create_time":"2020-01-10T14:22:20.222Z","id":1},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-10T14:22:20.222Z","id":7,"is_blocked":false,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY=","kind":"node","labels":["Person"],"properties":{"birthday":"1986-12-07T08:00:00Z","city":"Kollam","country":"India","id":3,"name":"Lee"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEGkSCZRmluR3JhcGguUGVyc29uAHiRBplGaW5HcmFwaC5BY2NvdW50AHiRIA==","kind":"edge","labels":["Owns"],"properties":{"account_id":16,"create_time":"2020-02-18T13:44:20.655Z","id":3},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-28T01:55:09.206Z","id":16,"is_blocked":true,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ=","kind":"node","labels":["Person"],"properties":{"birthday":"1980-10-31T08:00:00Z","city":"Moravia","country":"Czech_Republic","id":2,"name":"Dana"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEEkSiZRmluR3JhcGguUGVyc29uAHiRBJlGaW5HcmFwaC5BY2NvdW50AHiRKA==","kind":"edge","labels":["Owns"],"properties":{"account_id":20,"create_time":"2020-01-28T01:55:09.206Z","id":2},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","kind":"node","labels":["Account"],"properties":{"create_time":"2020-02-18T13:44:20.655Z","id":20,"is_blocked":false,"nick_name":"Rainy Day Fund"}}]
        """,
    ]
    result = pandas.DataFrame(graph_json_rows, columns=["graph_json"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    display_patch = mock.patch("IPython.display.display", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    query_job_mock.configuration.destination.project = PROJECT_ID
    query_job_mock.configuration.destination.dataset_id = DATASET_ID
    query_job_mock.configuration.destination.table_id = "test_destination_table"

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock
        try:
            return_value = ip.run_cell_magic("bigquery", "--graph", sql)
        finally:
            graph_server.graph_server.stop_server()

        assert len(display_mock.call_args_list) == 1
        assert len(display_mock.call_args_list[0]) == 2

        # Sanity check that the HTML content looks like graph visualization. Minimal check
        # to allow Spanner to change its implementation without breaking this test.
        html_content = display_mock.call_args_list[0][0][0].data
        assert "<script>" in html_content
        assert "</script>" in html_content
        # Verify that the query results are embedded into the HTML, allowing them to be visualized.
        # Due to escaping, it is not possible check for graph_json_rows exactly, so we check for a few
        # sentinel strings within the query results, instead.
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQI=" in html_content
        )  # identifier in 1st row of query result
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQY=" in html_content
        )  # identifier in 2nd row of query result
        assert (
            "mUZpbkdyYXBoLlBlcnNvbgB4kQQ=" in html_content
        )  # identifier in 3rd row of query result

        # Verify that args are present in the HTML.
        assert '\\"args\\": {' in html_content
        assert '\\"bigquery_api_endpoint\\": null' in html_content
        assert '\\"project\\": null' in html_content
        assert '\\"location\\": null' in html_content

        # Make sure we actually used colab path, not GraphServer path.
        assert sys.modules["google.colab"].output.register_callback.called

    assert bqstorage_mock.called  # BQ storage client was used
    assert return_value is None


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_colab_query_callback():
    result = bigquery_magics.bigquery._colab_query_callback(
        "query", json.dumps({"query_result": {"result": {}}})
    )
    assert result.data == {
        "response": {
            "edges": [],
            "nodes": [],
            "query_result": {"result": []},
            "schema": None,
        }
    }


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_colab_node_expansion_callback():
    result = bigquery_magics.bigquery._colab_node_expansion_callback(
        request={
            "uid": "test_uid",
            "node_labels": ["label1, label2"],
            "node_properites": {},
            "direction": "INCOMING",
            "edge_label": None,
        },
        params_str="{}",
    )

    assert result.data == {"error": "Node expansion not yet implemented"}


@pytest.mark.skipif(
    graph_visualization is not None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` to be missing and `google-cloud-bigquery-storage` to be present",
)
def test_bigquery_graph_missing_spanner_deps(monkeypatch):
    monkeypatch.setattr(
        "bigquery_magics.bigquery._get_graph_schema", lambda *args: None
    )
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )
    sql = "SELECT graph_json FROM t"
    graph_json_rows = [
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI=","kind":"node","labels":["Person"],"properties":{"birthday":"1991-12-21T08:00:00Z","city":"Adelaide","country":"Australia","id":1,"name":"Alex"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJECkQ6ZRmluR3JhcGguUGVyc29uAHiRAplGaW5HcmFwaC5BY2NvdW50AHiRDg==","kind":"edge","labels":["Owns"],"properties":{"account_id":7,"create_time":"2020-01-10T14:22:20.222Z","id":1},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQI="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEO","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-10T14:22:20.222Z","id":7,"is_blocked":false,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY=","kind":"node","labels":["Person"],"properties":{"birthday":"1986-12-07T08:00:00Z","city":"Kollam","country":"India","id":3,"name":"Lee"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEGkSCZRmluR3JhcGguUGVyc29uAHiRBplGaW5HcmFwaC5BY2NvdW50AHiRIA==","kind":"edge","labels":["Owns"],"properties":{"account_id":16,"create_time":"2020-02-18T13:44:20.655Z","id":3},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQY="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEg","kind":"node","labels":["Account"],"properties":{"create_time":"2020-01-28T01:55:09.206Z","id":16,"is_blocked":true,"nick_name":"Vacation Fund"}}]
        """,
        """
        [{"identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ=","kind":"node","labels":["Person"],"properties":{"birthday":"1980-10-31T08:00:00Z","city":"Moravia","country":"Czech_Republic","id":2,"name":"Dana"}},{"destination_node_identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","identifier":"mUZpbkdyYXBoLlBlcnNvbk93bkFjY291bnQAeJEEkSiZRmluR3JhcGguUGVyc29uAHiRBJlGaW5HcmFwaC5BY2NvdW50AHiRKA==","kind":"edge","labels":["Owns"],"properties":{"account_id":20,"create_time":"2020-01-28T01:55:09.206Z","id":2},"source_node_identifier":"mUZpbkdyYXBoLlBlcnNvbgB4kQQ="},{"identifier":"mUZpbkdyYXBoLkFjY291bnQAeJEo","kind":"node","labels":["Account"],"properties":{"create_time":"2020-02-18T13:44:20.655Z","id":20,"is_blocked":false,"nick_name":"Rainy Day Fund"}}]
        """,
    ]
    result = pandas.DataFrame(graph_json_rows, columns=["graph_json"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    display_patch = mock.patch("IPython.display.display", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result

    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        display_patch as display_mock,
    ):
        run_query_mock.return_value = query_job_mock
        with pytest.raises(ImportError):
            try:
                ip.run_cell_magic("bigquery", "--graph", sql)
            finally:
                graph_server.graph_server.stop_server()
        display_mock.assert_not_called()


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_add_graph_widget_with_schema(monkeypatch):
    """Test _add_graph_widget with a valid graph query that retrieves a schema."""
    mock_display = mock.patch("IPython.display.display", autospec=True)
    mock_gen_html = mock.patch(
        "spanner_graphs.graph_visualization.generate_visualization_html",
        return_value="<html>generated_html</html>",
    )

    bq_client = mock.create_autospec(bigquery.Client, instance=True)
    query_result = pandas.DataFrame([{"id": 1}], columns=["result"])
    query_text = "GRAPH my_dataset.my_graph"

    query_job = mock.Mock()
    query_job.configuration.destination.project = "p"
    query_job.configuration.destination.dataset_id = "d"
    query_job.configuration.destination.table_id = "t"

    graph_ref = mock.Mock()
    graph_ref.project = "p"
    graph_ref.dataset_id = "my_dataset"
    graph_ref.property_graph_id = "my_graph"
    query_job.referenced_property_graphs = [graph_ref]

    args = mock.Mock()
    args.bigquery_api_endpoint = "e"
    args.project = "p"
    args.location = "l"

    # Mock INFORMATION_SCHEMA query for schema retrieval
    schema_json = '{"propertyGraphReference": {"propertyGraphId": "my_graph"}}'
    mock_schema_df = pandas.DataFrame(
        [[schema_json]], columns=["PROPERTY_GRAPH_METADATA_JSON"]
    )
    bq_client.query.return_value.to_dataframe.return_value = mock_schema_df

    with mock_display as display_mock, mock_gen_html as gen_html_mock:
        magics._add_graph_widget(bq_client, query_result, query_text, query_job, args)

        # Verify schema was retrieved and converted
        assert bq_client.query.called
        call_args, call_kwargs = bq_client.query.call_args
        query_str = call_args[0]
        assert "INFORMATION_SCHEMA.PROPERTY_GRAPHS" in query_str
        assert "PROPERTY_GRAPH_NAME = @graph_id" in query_str

        # Verify query parameter
        job_config = call_kwargs["job_config"]
        param = job_config.query_parameters[0]
        assert param.name == "graph_id"
        assert param.value == "my_graph"

        # Verify generate_visualization_html was called with the converted schema
        assert gen_html_mock.called
        params_str = gen_html_mock.call_args[1]["params"]
        params = json.loads(params_str.replace('\\"', '"').replace("\\\\", "\\"))
        assert "schema" in params
        schema_obj = json.loads(params["schema"])
        assert schema_obj["name"] == "my_graph"

        # Verify display was called
        assert display_mock.called


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_add_graph_widget_no_graph_name(monkeypatch):
    """Test _add_graph_widget with a query that is not a GRAPH query."""
    mock_display = mock.patch("IPython.display.display", autospec=True)
    mock_gen_html = mock.patch(
        "spanner_graphs.graph_visualization.generate_visualization_html",
        return_value="<html>generated_html</html>",
    )

    bq_client = mock.create_autospec(bigquery.Client, instance=True)
    query_result = pandas.DataFrame([{"id": 1}], columns=["result"])
    query_text = "SELECT * FROM my_dataset.my_table"

    query_job = mock.Mock()
    query_job.configuration.destination.project = "p"
    query_job.configuration.destination.dataset_id = "d"
    query_job.configuration.destination.table_id = "t"

    query_job.referenced_property_graphs = []

    args = mock.Mock()
    args.bigquery_api_endpoint = "e"
    args.project = "p"
    args.location = "l"

    with mock_display as display_mock, mock_gen_html as gen_html_mock:
        magics._add_graph_widget(bq_client, query_result, query_text, query_job, args)

        # Verify schema retrieval was NOT attempted since graph name couldn't be parsed
        assert not bq_client.query.called

        # Verify generate_visualization_html was called without a schema
        assert gen_html_mock.called
        params_str = gen_html_mock.call_args[1]["params"]
        params = json.loads(params_str.replace('\\"', '"').replace("\\\\", "\\"))
        assert "schema" not in params

        assert display_mock.called


@pytest.mark.skipif(
    graph_visualization is None or bigquery_storage is None,
    reason="Requires `spanner-graph-notebook` and `google-cloud-bigquery-storage`",
)
def test_add_graph_widget_schema_not_found(monkeypatch):
    """Test _add_graph_widget when the graph schema is not found in INFORMATION_SCHEMA."""
    mock_display = mock.patch("IPython.display.display", autospec=True)
    mock_gen_html = mock.patch(
        "spanner_graphs.graph_visualization.generate_visualization_html",
        return_value="<html>generated_html</html>",
    )

    bq_client = mock.create_autospec(bigquery.Client, instance=True)
    query_result = pandas.DataFrame([{"id": 1}], columns=["result"])
    query_text = "GRAPH my_dataset.my_graph"

    query_job = mock.Mock()
    query_job.configuration.destination.project = "p"
    query_job.configuration.destination.dataset_id = "d"
    query_job.configuration.destination.table_id = "t"

    graph_ref = mock.Mock()
    graph_ref.project = "p"
    graph_ref.dataset_id = "my_dataset"
    graph_ref.property_graph_id = "my_graph"
    query_job.referenced_property_graphs = [graph_ref]

    args = mock.Mock()
    args.bigquery_api_endpoint = "e"
    args.project = "p"
    args.location = "l"

    # Mock INFORMATION_SCHEMA query returning empty results
    mock_schema_df = pandas.DataFrame([], columns=["PROPERTY_GRAPH_METADATA_JSON"])
    bq_client.query.return_value.to_dataframe.return_value = mock_schema_df

    with mock_display as display_mock, mock_gen_html as gen_html_mock:
        magics._add_graph_widget(bq_client, query_result, query_text, query_job, args)

        # Verify schema retrieval was attempted
        assert bq_client.query.called

        # Verify generate_visualization_html was called without a schema
        assert gen_html_mock.called
        params_str = gen_html_mock.call_args[1]["params"]
        params = json.loads(params_str.replace('\\"', '"').replace("\\\\", "\\"))
        assert "schema" not in params

        assert display_mock.called


def test_bigquery_magic_default_connection_user_agent():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)

    with conn_patch as conn, run_query_patch, default_patch:
        ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

    client_info_arg = conn.call_args[1].get("client_info")
    assert client_info_arg is not None
    assert client_info_arg.user_agent.startswith(
        f"ipython-{IPython.__version__} bigquery-magics/{bigquery_magics.__version__}"
    )


def test_bigquery_magic_default_connection_user_agent_vscode():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)
    env_patch = mock.patch.dict(os.environ, {"VSCODE_PID": "1234"}, clear=True)

    with conn_patch as conn, run_query_patch, default_patch, env_patch:
        ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

    client_info_arg = conn.call_args[1].get("client_info")
    assert client_info_arg is not None
    assert (
        client_info_arg.user_agent
        == f"ipython-{IPython.__version__} bigquery-magics/{bigquery_magics.__version__} vscode"
    )


@pytest.mark.parametrize(
    (
        "install_dir_exists",
        "manifest_exists",
        "manifest_valid",
        "expect_extension_user_agent",
    ),
    [
        pytest.param(False, False, False, False, id="no-install"),
        pytest.param(True, False, False, False, id="no-manifest"),
        pytest.param(True, True, False, False, id="invalid-manifest"),
        pytest.param(True, True, True, True, id="good-install"),
    ],
)
def test_bigquery_magic_default_connection_user_agent_vscode_extension(
    install_dir_exists, manifest_exists, manifest_valid, expect_extension_user_agent
):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)
    env_patch = mock.patch.dict(os.environ, {"VSCODE_PID": "1234"}, clear=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        user_home = Path(tmpdir)
        extension_dir = (
            user_home / ".vscode" / "extensions" / "googlecloudtools.cloudcode-0.12"
        )
        extension_config = extension_dir / "package.json"

        # originally extension config does not exist
        assert not extension_config.exists()

        # simulate extension installation by creating extension config on disk
        if install_dir_exists:
            extension_dir.mkdir(parents=True)

        if manifest_exists:
            if manifest_valid:
                with open(extension_config, "w") as f:
                    f.write("{}")
            else:
                extension_config.touch()

        home_dir_patch = mock.patch("pathlib.Path.home", return_value=user_home)

        with (
            conn_patch as conn,
            run_query_patch,
            default_patch,
            env_patch,
            home_dir_patch,
        ):
            ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

    expected_user_agents = [
        f"ipython-{IPython.__version__}",
        f"bigquery-magics/{bigquery_magics.__version__}",
        "vscode",
    ]
    if expect_extension_user_agent:
        expected_user_agents.append("googlecloudtools.cloudcode")
    expected_user_agent = " ".join(expected_user_agents)

    client_info_arg = conn.call_args[1].get("client_info")
    assert client_info_arg is not None
    assert client_info_arg.user_agent == expected_user_agent


def test_bigquery_magic_default_connection_user_agent_jupyter():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)
    env_patch = mock.patch.dict(os.environ, {"JPY_PARENT_PID": "1234"}, clear=True)

    with conn_patch as conn, run_query_patch, default_patch, env_patch:
        ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

    client_info_arg = conn.call_args[1].get("client_info")
    assert client_info_arg is not None
    assert (
        client_info_arg.user_agent
        == f"ipython-{IPython.__version__} bigquery-magics/{bigquery_magics.__version__} jupyter"
    )


def test_bigquery_magic_default_connection_user_agent_jupyter_plugin():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)
    env_patch = mock.patch.dict(os.environ, {"JPY_PARENT_PID": "1234"}, clear=True)

    def custom_import_module_side_effect(name, package=None):
        if name == "bigquery_jupyter_plugin":
            return mock.MagicMock()
        else:
            import importlib

            return importlib.import_module(name, package)

    assert isinstance(
        custom_import_module_side_effect("bigquery_jupyter_plugin"), mock.MagicMock
    )
    assert custom_import_module_side_effect("bigquery_magics") is bigquery_magics

    extension_import_patch = mock.patch(
        "importlib.import_module", side_effect=custom_import_module_side_effect
    )

    with (
        conn_patch as conn,
        run_query_patch,
        default_patch,
        env_patch,
        extension_import_patch,
    ):
        ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

    client_info_arg = conn.call_args[1].get("client_info")
    assert client_info_arg is not None
    assert (
        client_info_arg.user_agent
        == f"ipython-{IPython.__version__} bigquery-magics/{bigquery_magics.__version__} jupyter bigquery_jupyter_plugin"
    )


def test_bigquery_magic_with_legacy_sql():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--use_legacy_sql", "SELECT 17 AS num")

        job_config_used = run_query_mock.call_args_list[0][1]["job_config"]
        assert job_config_used.use_legacy_sql is True


def test_bigquery_magic_with_result_saved_to_variable(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "df"))

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    assert "df" not in ip.user_ns

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock

        return_value = ip.run_cell_magic("bigquery", "df", sql)

    assert return_value is None
    assert "df" in ip.user_ns  # verify that variable exists
    df = ip.user_ns["df"]
    assert len(df) == len(result)  # verify row count
    assert list(df) == list(result)  # verify column names


def test_bigquery_magic_does_not_clear_display_in_verbose_mode():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    clear_patch = mock.patch(
        "bigquery_magics.bigquery.IPython.display.clear_output",
        autospec=True,
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with clear_patch as clear_mock, run_query_patch:
        ip.run_cell_magic("bigquery", "--verbose", "SELECT 17 as num")

        assert clear_mock.call_count == 0


def test_bigquery_magic_clears_display_in_non_verbose_mode():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    clear_patch = mock.patch(
        "bigquery_magics.bigquery.IPython.display.clear_output",
        autospec=True,
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with clear_patch as clear_mock, run_query_patch:
        ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

        assert clear_mock.call_count == 1


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_with_bqstorage_from_argument(monkeypatch):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with (
        run_query_patch as run_query_mock,
        bqstorage_client_patch,
        warnings.catch_warnings(record=True) as warned,
    ):
        run_query_mock.return_value = query_job_mock

        return_value = ip.run_cell_magic("bigquery", "--use_bqstorage_api", sql)

    # Deprecation warning should have been issued.
    def warning_match(warning):
        message = str(warning).lower()
        return "deprecated" in message and "use_bqstorage_api" in message

    expected_warnings = list(filter(warning_match, warned))
    assert len(expected_warnings) == 1

    assert len(bqstorage_mock.call_args_list) == 1
    kwargs = bqstorage_mock.call_args_list[0][1]
    assert kwargs.get("credentials") is mock_credentials
    client_info = kwargs.get("client_info")
    assert client_info is not None
    assert client_info.user_agent.startswith(
        f"ipython-{IPython.__version__} bigquery-magics/{bigquery_magics.__version__}"
    )

    query_job_mock.to_dataframe.assert_called_once_with(
        bqstorage_client=bqstorage_instance_mock,
        create_bqstorage_client=mock.ANY,
        progress_bar_type="tqdm_notebook",
    )

    assert isinstance(return_value, pandas.DataFrame)


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_with_rest_client_requested(monkeypatch):
    pandas = pytest.importorskip("pandas")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(bigquery_magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock, bqstorage_client_patch:
        run_query_mock.return_value = query_job_mock

        return_value = ip.run_cell_magic("bigquery", "--use_rest_api", sql)

        bqstorage_mock.assert_not_called()
        query_job_mock.to_dataframe.assert_called_once_with(
            bqstorage_client=None,
            create_bqstorage_client=False,
            progress_bar_type="tqdm_notebook",
        )

    assert isinstance(return_value, pandas.DataFrame)


def test_bigquery_magic_w_max_results_invalid():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    client_query_patch = mock.patch(
        "google.cloud.bigquery.client.Client.query", autospec=True
    )

    sql = "SELECT 17 AS num"

    with pytest.raises(ValueError), default_patch, client_query_patch:
        ip.run_cell_magic("bigquery", "--max_results=abc", sql)


def test_bigquery_magic_w_max_results_valid_calls_queryjob_result():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    client_query_patch = mock.patch(
        "google.cloud.bigquery.client.Client.query", autospec=True
    )

    sql = "SELECT 17 AS num"

    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )

    with client_query_patch as client_query_mock, default_patch:
        client_query_mock.return_value = query_job_mock
        ip.run_cell_magic("bigquery", "--max_results=5", sql)

    query_job_mock.result.assert_called_with(max_results=5)
    query_job_mock.result.return_value.to_dataframe.assert_called_once_with(
        bqstorage_client=None,
        create_bqstorage_client=False,
        progress_bar_type=mock.ANY,
    )


@pytest.mark.skipif(gpd is None, reason="Requires `geopandas`")
def test_bigquery_magic_with_use_geodataframe():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    client_query_patch = mock.patch(
        "google.cloud.bigquery.client.Client.query", autospec=True
    )

    sql = """
    SELECT
      17 AS num,
      ST_GEOGFROMTEXT('POINT(-122.083855 37.386051)') AS my_geom
    """
    result = gpd.GeoDataFrame(
        [[17, "POINT(-122.083855 37.386051)"]], columns=["num", "my_geom"]
    )

    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_geodataframe.return_value = result

    with client_query_patch as client_query_mock, default_patch:
        client_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "--use_geodataframe my_geom", sql)

    query_job_mock.to_dataframe.assert_not_called()
    query_job_mock.to_geodataframe.assert_called_once_with(
        geography_column="my_geom",
        bqstorage_client=mock.ANY,
        create_bqstorage_client=False,
        progress_bar_type="tqdm_notebook",
    )
    assert isinstance(return_value, gpd.GeoDataFrame)


def test_bigquery_magic_w_max_results_query_job_results_fails():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    client_query_patch = mock.patch(
        "google.cloud.bigquery.client.Client.query", autospec=True
    )
    close_transports_patch = mock.patch(
        "bigquery_magics.bigquery._close_transports",
        autospec=True,
    )

    sql = "SELECT 17 AS num"

    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.result.side_effect = [[], OSError]

    with (
        pytest.raises(OSError),
        client_query_patch as client_query_mock,
        default_patch,
        close_transports_patch as close_transports,
    ):
        client_query_mock.return_value = query_job_mock
        ip.run_cell_magic("bigquery", "--max_results=5", sql)

    assert close_transports.called


def test_bigquery_magic_w_table_id_invalid():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    list_rows_patch = mock.patch(
        "bigquery_magics.bigquery.bigquery.Client.list_rows",
        autospec=True,
        side_effect=exceptions.BadRequest("Not a valid table ID"),
    )

    table_id = "not-a-real-table"

    with list_rows_patch, default_patch, io.capture_output() as captured_io:
        ip.run_cell_magic("bigquery", "df", table_id)

    output = captured_io.stderr
    assert "Could not save output to variable" in output
    assert "400 Not a valid table ID" in output
    assert "Traceback (most recent call last)" not in output


def test_bigquery_magic_w_missing_query():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    cell_body = "   \n    \n   \t\t  \n  "

    with io.capture_output() as captured_io, default_patch:
        ip.run_cell_magic("bigquery", "df", cell_body)

    output = captured_io.stderr
    assert "Could not save output to variable" in output
    assert "Query is missing" in output
    assert "Traceback (most recent call last)" not in output


def test_bigquery_magic_w_table_id_and_default_variable(
    ipython_ns_cleanup, monkeypatch
):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None
    monkeypatch.setattr(bigquery_magics.context, "default_variable", "_bq_df")

    ipython_ns_cleanup.append((ip, "df"))

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    row_iterator_mock = mock.create_autospec(
        google.cloud.bigquery.table.RowIterator, instance=True
    )

    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)

    table_id = "bigquery-public-data.samples.shakespeare"
    result = pandas.DataFrame([17], columns=["num"])

    with client_patch as client_mock, default_patch:
        client_mock().list_rows.return_value = row_iterator_mock
        row_iterator_mock.to_dataframe.return_value = result

        ip.run_cell_magic("bigquery", "", table_id)

    assert "_bq_df" in ip.user_ns
    df = ip.user_ns["_bq_df"]

    assert isinstance(df, pandas.DataFrame)


def test_bigquery_magic_w_table_id_and_destination_var(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    ipython_ns_cleanup.append((ip, "df"))

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    row_iterator_mock = mock.create_autospec(
        google.cloud.bigquery.table.RowIterator, instance=True
    )

    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)

    table_id = "bigquery-public-data.samples.shakespeare"
    result = pandas.DataFrame([17], columns=["num"])

    with client_patch as client_mock, default_patch:
        client_mock().list_rows.return_value = row_iterator_mock
        row_iterator_mock.to_dataframe.return_value = result

        ip.run_cell_magic("bigquery", "df", table_id)

    assert "df" in ip.user_ns
    df = ip.user_ns["df"]

    assert isinstance(df, pandas.DataFrame)


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_w_table_id_and_bqstorage_client():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    row_iterator_mock = mock.create_autospec(
        google.cloud.bigquery.table.RowIterator, instance=True
    )

    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)

    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_instance_mock = mock.create_autospec(
        bigquery_storage.BigQueryReadClient, instance=True
    )
    bqstorage_instance_mock._transport = mock.Mock()
    bqstorage_mock.return_value = bqstorage_instance_mock
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    table_id = "bigquery-public-data.samples.shakespeare"

    with default_patch, client_patch as client_mock, bqstorage_client_patch:
        client_mock()._ensure_bqstorage_client.return_value = bqstorage_instance_mock
        client_mock().list_rows.return_value = row_iterator_mock

        ip.run_cell_magic("bigquery", "--max_results=5", table_id)
        row_iterator_mock.to_dataframe.assert_called_once_with(
            bqstorage_client=bqstorage_instance_mock,
            create_bqstorage_client=mock.ANY,
        )


def test_bigquery_magic_dryrun_option_sets_job_config():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    sql = "SELECT 17 AS num"

    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--dry_run", sql)

        job_config_used = run_query_mock.call_args_list[0][1]["job_config"]
        assert job_config_used.dry_run is True


def test_bigquery_magic_dryrun_option_returns_query_job():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    sql = "SELECT 17 AS num"

    with run_query_patch as run_query_mock, io.capture_output() as captured_io:
        run_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "--dry_run", sql)

        assert "Query validated. This query will process" in captured_io.stdout
        assert isinstance(return_value, job.QueryJob)


def test_bigquery_magic_dryrun_option_variable_error_message(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "q_job"))

    run_query_patch = mock.patch(
        "bigquery_magics.bigquery._run_query",
        autospec=True,
        side_effect=exceptions.BadRequest("Syntax error in SQL query"),
    )

    sql = "SELECT SELECT 17 AS num"

    assert "q_job" not in ip.user_ns

    with run_query_patch, io.capture_output() as captured:
        ip.run_cell_magic("bigquery", "q_job --dry_run", sql)

    full_text = captured.stderr
    assert "Could not save output to variable 'q_job'." in full_text


def test_bigquery_magic_dryrun_option_saves_query_job_to_variable(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    ipython_ns_cleanup.append((ip, "q_job"))

    sql = "SELECT 17 AS num"

    assert "q_job" not in ip.user_ns

    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "q_job --dry_run", sql)

    assert return_value is None
    assert "q_job" in ip.user_ns
    q_job = ip.user_ns["q_job"]
    assert isinstance(q_job, job.QueryJob)


def test_bigquery_magic_saves_query_job_to_variable_on_error(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "result"))

    client_query_patch = mock.patch(
        "google.cloud.bigquery.client.Client.query", autospec=True
    )

    query_job = mock.create_autospec(job.QueryJob, instance=True)
    exception = Exception("Unexpected SELECT")
    exception.query_job = query_job
    query_job.result.side_effect = exception

    sql = "SELECT SELECT 17 AS num"

    assert "result" not in ip.user_ns

    with client_query_patch as client_query_mock:
        client_query_mock.return_value = query_job
        return_value = ip.run_cell_magic("bigquery", "result", sql)

    assert return_value is None
    assert "result" in ip.user_ns
    result = ip.user_ns["result"]
    assert isinstance(result, job.QueryJob)


def test_bigquery_magic_w_maximum_bytes_billed_invalid():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    client_query_patch = mock.patch("google.cloud.bigquery.client.Client.query")

    sql = "SELECT 17 AS num"

    with pytest.raises(ValueError), default_patch, client_query_patch:
        ip.run_cell_magic("bigquery", "--maximum_bytes_billed=abc", sql)


@pytest.mark.parametrize(
    "param_value,expected", [("987654321", "987654321"), ("None", "0")]
)
def test_bigquery_magic_w_maximum_bytes_billed_overrides_context(param_value, expected):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    # Set the default maximum bytes billed, so we know it's overridable by the param.
    bigquery_magics.context.default_query_job_config.maximum_bytes_billed = 1234567

    project = "test-project"
    job_reference = copy.deepcopy(JOB_REFERENCE_RESOURCE)
    job_reference["projectId"] = project
    query = "SELECT 17 AS num"
    resource = copy.deepcopy(QUERY_RESOURCE)
    resource["jobReference"] = job_reference
    resource["configuration"]["query"]["query"] = query
    query_results = {"jobReference": job_reference, "totalRows": 0, "jobComplete": True}
    data = {"jobReference": job_reference, "totalRows": 0, "rows": []}
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    conn = bigquery_magics.context._connection = make_connection(
        resource, query_results, data
    )
    list_rows_patch = mock.patch(
        "google.cloud.bigquery.client.Client._list_rows_from_query_results",
        return_value=google.cloud.bigquery.table._EmptyRowIterator(),
    )
    with list_rows_patch, default_patch:
        ip.run_cell_magic(
            "bigquery", "--maximum_bytes_billed={}".format(param_value), query
        )

    _, req = conn.api_request.call_args_list[0]
    sent_config = req["data"]["configuration"]["query"]
    assert sent_config["maximumBytesBilled"] == expected


def test_bigquery_magic_w_maximum_bytes_billed_w_context_inplace():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    bigquery_magics.context.default_query_job_config.maximum_bytes_billed = 1337

    project = "test-project"
    job_reference = copy.deepcopy(JOB_REFERENCE_RESOURCE)
    job_reference["projectId"] = project
    query = "SELECT 17 AS num"
    resource = copy.deepcopy(QUERY_RESOURCE)
    resource["jobReference"] = job_reference
    resource["configuration"]["query"]["query"] = query
    query_results = {"jobReference": job_reference, "totalRows": 0, "jobComplete": True}
    data = {"jobReference": job_reference, "totalRows": 0, "rows": []}
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    conn = bigquery_magics.context._connection = make_connection(
        resource, query_results, data
    )
    list_rows_patch = mock.patch(
        "google.cloud.bigquery.client.Client._list_rows_from_query_results",
        return_value=google.cloud.bigquery.table._EmptyRowIterator(),
    )
    with list_rows_patch, default_patch:
        ip.run_cell_magic("bigquery", "", query)

    _, req = conn.api_request.call_args_list[0]
    sent_config = req["data"]["configuration"]["query"]
    assert sent_config["maximumBytesBilled"] == "1337"


def test_bigquery_magic_w_maximum_bytes_billed_w_context_setter():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    bigquery_magics.context.default_query_job_config = job.QueryJobConfig(
        maximum_bytes_billed=10203
    )

    project = "test-project"
    job_reference = copy.deepcopy(JOB_REFERENCE_RESOURCE)
    job_reference["projectId"] = project
    query = "SELECT 17 AS num"
    resource = copy.deepcopy(QUERY_RESOURCE)
    resource["jobReference"] = job_reference
    resource["configuration"]["query"]["query"] = query
    query_results = {"jobReference": job_reference, "totalRows": 0, "jobComplete": True}
    data = {"jobReference": job_reference, "totalRows": 0, "rows": []}
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    conn = bigquery_magics.context._connection = make_connection(
        resource, query_results, data
    )
    list_rows_patch = mock.patch(
        "google.cloud.bigquery.client.Client._list_rows_from_query_results",
        return_value=google.cloud.bigquery.table._EmptyRowIterator(),
    )
    with list_rows_patch, default_patch:
        ip.run_cell_magic("bigquery", "", query)

    _, req = conn.api_request.call_args_list[0]
    sent_config = req["data"]["configuration"]["query"]
    assert sent_config["maximumBytesBilled"] == "10203"


def test_bigquery_magic_with_no_query_cache(monkeypatch):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    conn = make_connection()
    monkeypatch.setattr(bigquery_magics.context, "_connection", conn)
    monkeypatch.setattr(bigquery_magics.context, "project", "project-from-context")

    # --no_query_cache option should override context.
    monkeypatch.setattr(
        bigquery_magics.context.default_query_job_config, "use_query_cache", True
    )

    ip.run_cell_magic("bigquery", "--no_query_cache", QUERY_STRING)

    conn.api_request.assert_called_with(
        method="POST",
        path="/projects/project-from-context/jobs",
        data=mock.ANY,
        timeout=DEFAULT_TIMEOUT,
    )
    jobs_insert_call = [
        call
        for call in conn.api_request.call_args_list
        if call[1]["path"] == "/projects/project-from-context/jobs"
    ][0]
    assert not jobs_insert_call[1]["data"]["configuration"]["query"]["useQueryCache"]


def test_context_with_no_query_cache_from_context(monkeypatch):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    conn = make_connection()
    monkeypatch.setattr(bigquery_magics.context, "_connection", conn)
    monkeypatch.setattr(bigquery_magics.context, "project", "project-from-context")
    monkeypatch.setattr(
        bigquery_magics.context.default_query_job_config, "use_query_cache", False
    )

    ip.run_cell_magic("bigquery", "", QUERY_STRING)

    conn.api_request.assert_called_with(
        method="POST",
        path="/projects/project-from-context/jobs",
        data=mock.ANY,
        timeout=DEFAULT_TIMEOUT,
    )
    jobs_insert_call = [
        call
        for call in conn.api_request.call_args_list
        if call[1]["path"] == "/projects/project-from-context/jobs"
    ][0]
    assert not jobs_insert_call[1]["data"]["configuration"]["query"]["useQueryCache"]


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_w_progress_bar_type_w_context_setter():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    bigquery_magics.context.progress_bar_type = "tqdm_gui"

    # Mock out the BigQuery Storage API.
    if bigquery_storage is not None:
        bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        bqstorage_client_patch = mock.patch(
            "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
        )
    else:
        bqstorage_mock = mock.MagicMock()
        bqstorage_client_patch = contextlib.nullcontext()

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock, bqstorage_client_patch:
        run_query_mock.return_value = query_job_mock

        return_value = ip.run_cell_magic("bigquery", "--use_rest_api", sql)

        bqstorage_mock.assert_not_called()
        query_job_mock.to_dataframe.assert_called_once_with(
            bqstorage_client=None,
            create_bqstorage_client=False,
            progress_bar_type=bigquery_magics.context.progress_bar_type,
        )

    assert isinstance(return_value, pandas.DataFrame)


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_progress_bar_type():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.progress_bar_type = None

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery", "--progress_bar_type=tqdm_gui", "SELECT 17 as num"
        )

        progress_bar_used = run_query_mock.mock_calls[1][2]["progress_bar_type"]
        assert progress_bar_used == "tqdm_gui"
        # context progress bar type should not change
        assert bigquery_magics.context.progress_bar_type is None


def test_bigquery_magic_with_project():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock, default_patch:
        ip.run_cell_magic("bigquery", "--project=specific-project", "SELECT 17 as num")

        client_used = run_query_mock.call_args_list[0][0][0]
        assert client_used.project == "specific-project"
        # context project should not change
        assert bigquery_magics.context.project == "general-project"


def test_bigquery_magic_with_bigquery_api_endpoint(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bigquery_api_endpoint=https://bigquery_api.endpoint.com",
            "SELECT 17 as num",
        )

    connection_used = run_query_mock.call_args_list[0][0][0]._connection
    assert connection_used.API_BASE_URL == "https://bigquery_api.endpoint.com"
    # context client options should not change
    assert bigquery_magics.context.bigquery_client_options.api_endpoint is None


def test_bigquery_magic_with_bigquery_api_endpoint_context_dict():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None
    bigquery_magics.context.bigquery_client_options = {}

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bigquery_api_endpoint=https://bigquery_api.endpoint.com",
            "SELECT 17 as num",
        )

    connection_used = run_query_mock.call_args_list[0][0][0]._connection
    assert connection_used.API_BASE_URL == "https://bigquery_api.endpoint.com"
    # context client options should not change
    assert bigquery_magics.context.bigquery_client_options == {}


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_with_bqstorage_api_endpoint(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bqstorage_api_endpoint=https://bqstorage_api.endpoint.com",
            "SELECT 17 as num",
        )

    client_used = run_query_mock.mock_calls[1][2]["bqstorage_client"]
    assert client_used._transport._host == "https://bqstorage_api.endpoint.com"
    # context client options should not change
    assert bigquery_magics.context.bqstorage_client_options.api_endpoint is None


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_with_bqstorage_api_endpoint_context_dict():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._connection = None
    bigquery_magics.context.bqstorage_client_options = {}

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bqstorage_api_endpoint=https://bqstorage_api.endpoint.com",
            "SELECT 17 as num",
        )

    client_used = run_query_mock.mock_calls[1][2]["bqstorage_client"]
    assert client_used._transport._host == "https://bqstorage_api.endpoint.com"
    # context client options should not change
    assert bigquery_magics.context.bqstorage_client_options == {}


def test_bigquery_magic_with_multiple_options():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock, default_patch:
        ip.run_cell_magic(
            "bigquery",
            "--project=specific-project --use_legacy_sql --maximum_bytes_billed 1024",
            "SELECT 17 as num",
        )

    args, kwargs = run_query_mock.call_args
    client_used = args[0]
    assert client_used.project == "specific-project"

    job_config_used = kwargs["job_config"]
    assert job_config_used.use_legacy_sql
    assert job_config_used.maximum_bytes_billed == 1024


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_string_params(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame([17], columns=["num"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result

    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock

        ip.run_cell_magic("bigquery", "params_string_df --params='{\"num\":17}'", sql)

        run_query_mock.assert_called_once_with(mock.ANY, sql.format(num=17), mock.ANY)

    assert "params_string_df" in ip.user_ns  # verify that the variable exists
    df = ip.user_ns["params_string_df"]
    assert len(df) == len(result)  # verify row count
    assert list(df) == list(result)  # verify column names


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_dict_params(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num, @tricky_value as tricky_value"
    result = pandas.DataFrame(
        [(False, '--params "value"')], columns=["valid", "tricky_value"]
    )

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock

        params = {"valid": False, "tricky_value": '--params "value"'}
        # Insert dictionary into user namespace so that it can be expanded
        ip.user_ns["params"] = params
        ip.run_cell_magic("bigquery", "params_dict_df --params $params", sql)

        run_query_mock.assert_called_once_with(mock.ANY, sql.format(num=17), mock.ANY)

    assert "params_dict_df" in ip.user_ns  # verify that the variable exists
    df = ip.user_ns["params_dict_df"]
    assert len(df) == len(result)  # verify row count
    assert list(df) == list(result)  # verify column names

    assert not df["valid"][0]
    assert df["tricky_value"][0] == '--params "value"'


def test_bigquery_magic_with_dict_params_nonexisting():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @foo AS foo"

    with pytest.raises(NameError, match=r".*undefined variable.*unknown_name.*"):
        ip.run_cell_magic("bigquery", "params_dict_df --params $unknown_name", sql)


def test_bigquery_magic_with_dict_params_incorrect_syntax():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @foo AS foo"

    with pytest.raises(SyntaxError, match=r".*--params.*"):
        cell_magic_args = "params_dict_df --params {'foo': 1; 'bar': 2}"
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


def test_bigquery_magic_with_dict_params_duplicate():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    sql = "SELECT @foo AS foo"

    with pytest.raises(ValueError, match=r"Duplicate --params option\."):
        cell_magic_args = (
            "params_dict_df --params {'foo': 1} --verbose --params {'bar': 2} "
        )
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_option_value_incorrect():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    sql = "SELECT @foo AS foo"

    with pytest.raises(ValueError, match=r".*invalid literal.*\[PLENTY!\].*"):
        cell_magic_args = "params_dict_df --max_results [PLENTY!]"
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_dict_params_negative_value(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame([-17], columns=["num"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock

        params = {"num": -17}
        # Insert dictionary into user namespace so that it can be expanded
        ip.user_ns["params"] = params
        ip.run_cell_magic("bigquery", "params_dict_df --params $params", sql)

        run_query_mock.assert_called_once_with(mock.ANY, sql.format(num=-17), mock.ANY)

    assert "params_dict_df" in ip.user_ns  # verify that the variable exists
    df = ip.user_ns["params_dict_df"]
    assert len(df) == len(result)  # verify row count
    assert list(df) == list(result)  # verify column names
    assert df["num"][0] == -17


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_dict_params_array_value(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame(["foo bar", "baz quux"], columns=["array_data"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock

        params = {"array_data": ["foo bar", "baz quux"]}
        # Insert dictionary into user namespace so that it can be expanded
        ip.user_ns["params"] = params
        ip.run_cell_magic("bigquery", "params_dict_df --params $params", sql)

        run_query_mock.assert_called_once_with(mock.ANY, sql.format(num=-17), mock.ANY)

    assert "params_dict_df" in ip.user_ns  # verify that the variable exists
    df = ip.user_ns["params_dict_df"]
    assert len(df) == len(result)  # verify row count
    assert list(df) == list(result)  # verify column names
    assert list(df["array_data"]) == ["foo bar", "baz quux"]


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_dict_params_tuple_value(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame(["foo bar", "baz quux"], columns=["array_data"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock

        params = {"array_data": ("foo bar", "baz quux")}
        # Insert dictionary into user namespace so that it can be expanded
        ip.user_ns["params"] = params
        ip.run_cell_magic("bigquery", "params_dict_df --params $params", sql)

        run_query_mock.assert_called_once_with(mock.ANY, sql.format(num=-17), mock.ANY)

    assert "params_dict_df" in ip.user_ns  # verify that the variable exists
    df = ip.user_ns["params_dict_df"]
    assert len(df) == len(result)  # verify row count
    assert list(df) == list(result)  # verify column names
    assert list(df["array_data"]) == ["foo bar", "baz quux"]


def test_bigquery_magic_with_improperly_formatted_params():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    bigquery_magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @num AS num"

    with pytest.raises(SyntaxError):
        ip.run_cell_magic("bigquery", "--params {17}", sql)


@pytest.mark.parametrize(
    "raw_sql", ("SELECT answer AS 42", " \t   SELECT answer AS 42  \t  ")
)
@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_valid_query_in_existing_variable(ipython_ns_cleanup, raw_sql):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    ipython_ns_cleanup.append((ip, "custom_query"))
    ipython_ns_cleanup.append((ip, "query_results_df"))

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    mock_result = pandas.DataFrame([42], columns=["answer"])
    query_job_mock.to_dataframe.return_value = mock_result

    ip.user_ns["custom_query"] = raw_sql
    cell_body = "$custom_query"  # Referring to an existing variable name (custom_query)
    assert "query_results_df" not in ip.user_ns

    with run_query_patch as run_query_mock:
        run_query_mock.return_value = query_job_mock

        ip.run_cell_magic("bigquery", "query_results_df", cell_body)

        run_query_mock.assert_called_once_with(mock.ANY, raw_sql, mock.ANY)

    assert "query_results_df" in ip.user_ns  # verify that the variable exists
    df = ip.user_ns["query_results_df"]
    assert len(df) == len(mock_result)  # verify row count
    assert list(df) == list(mock_result)  # verify column names
    assert list(df["answer"]) == [42]


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_nonexisting_query_variable():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    ip.user_ns.pop("custom_query", None)  # Make sure the variable does NOT exist.
    cell_body = "$custom_query"  # Referring to a non-existing variable name.

    with (
        pytest.raises(NameError, match=r".*custom_query does not exist.*"),
        run_query_patch as run_query_mock,
    ):
        ip.run_cell_magic("bigquery", "", cell_body)

    run_query_mock.assert_not_called()


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_empty_query_variable_name():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    cell_body = "$"  # Not referring to any variable (name omitted).

    with (
        pytest.raises(NameError, match=r"(?i).*missing query variable name.*"),
        run_query_patch as run_query_mock,
    ):
        ip.run_cell_magic("bigquery", "", cell_body)

    run_query_mock.assert_not_called()


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_query_variable_non_string(ipython_ns_cleanup):
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    ipython_ns_cleanup.append((ip, "custom_query"))

    ip.user_ns["custom_query"] = object()
    cell_body = "$custom_query"  # Referring to a non-string variable.

    with (
        pytest.raises(TypeError, match=r".*must be a string or a bytes-like.*"),
        run_query_patch as run_query_mock,
    ):
        ip.run_cell_magic("bigquery", "", cell_body)

    run_query_mock.assert_not_called()


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_query_variable_not_identifier():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    cell_body = "$123foo"  # 123foo is not valid Python identifier

    with io.capture_output() as captured_io:
        ip.run_cell_magic("bigquery", "", cell_body)

    # If "$" prefixes a string that is not a Python identifier, we do not treat such
    # cell_body as a variable reference and just treat is as any other cell body input.
    # If at the same time the cell body does not contain any whitespace, it is
    # considered a table name, thus we expect an error that the table ID is not valid.
    output = captured_io.stderr
    assert "ERROR:" in output
    assert "table_id" in output


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_invalid_multiple_option_values():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    sql = "SELECT @foo AS foo"

    exc_pattern = r".*[Uu]nrecognized input.*option values correct\?.*567.*"

    with pytest.raises(ValueError, match=exc_pattern):
        cell_magic_args = "params_dict_df --max_results 10 567"
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_omits_tracebacks_from_error_message():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    run_query_patch = mock.patch(
        "bigquery_magics.bigquery._run_query",
        autospec=True,
        side_effect=exceptions.BadRequest("Syntax error in SQL query"),
    )

    with run_query_patch, io.capture_output() as captured_io:
        ip.run_cell_magic("bigquery", "", "SELECT foo FROM WHERE LIMIT bar")

    output = captured_io.stderr
    assert "400 Syntax error in SQL query" in output
    assert "Traceback (most recent call last)" not in output
    assert "Syntax error" not in captured_io.stdout


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_w_destination_table_invalid_format():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    client_patch = mock.patch("bigquery_magics.bigquery.bigquery.Client", autospec=True)

    with client_patch, pytest.raises(ValueError) as exc_context:
        ip.run_cell_magic(
            "bigquery", "--destination_table dataset", "SELECT foo FROM WHERE LIMIT bar"
        )
    error_msg = str(exc_context.value)
    assert (
        "--destination_table should be in a "
        "<dataset_id>.<table_id> format." in error_msg
    )


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_w_destination_table():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    create_dataset_if_necessary_patch = mock.patch(
        "bigquery_magics.bigquery._create_dataset_if_necessary",
        autospec=True,
    )

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)

    with create_dataset_if_necessary_patch, run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--destination_table dataset_id.table_id",
            "SELECT foo FROM WHERE LIMIT bar",
        )

        job_config_used = run_query_mock.call_args_list[0][1]["job_config"]
        assert job_config_used.allow_large_results is True
        assert job_config_used.create_disposition == "CREATE_IF_NEEDED"
        assert job_config_used.write_disposition == "WRITE_TRUNCATE"
        assert job_config_used.destination.dataset_id == "dataset_id"
        assert job_config_used.destination.table_id == "table_id"


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_create_dataset_fails():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    create_dataset_if_necessary_patch = mock.patch(
        "bigquery_magics.bigquery._create_dataset_if_necessary",
        autospec=True,
        side_effect=OSError,
    )
    close_transports_patch = mock.patch(
        "bigquery_magics.bigquery._close_transports",
        autospec=True,
    )

    with (
        pytest.raises(OSError),
        create_dataset_if_necessary_patch,
        close_transports_patch as close_transports,
    ):
        ip.run_cell_magic(
            "bigquery",
            "--destination_table dataset_id.table_id",
            "SELECT foo FROM WHERE LIMIT bar",
        )

    assert close_transports.called


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_with_location():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    run_query_patch = mock.patch("bigquery_magics.bigquery._run_query", autospec=True)
    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--location=us-east1", "SELECT 17 AS num")

        client_options_used = run_query_mock.call_args_list[0][0][0]
        assert client_options_used.location == "us-east1"


def test_bigquery_magic_with_invalid_engine_raises_error():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    engine = "whatever"

    with pytest.raises(ValueError, match=f"Invalid engine: {engine}"):
        ip.run_cell_magic("bigquery", f"--engine {engine}", "SELECT 17 AS num")


@pytest.mark.usefixtures("mock_credentials", "set_bigframes_engine_in_context")
def test_bigquery_magic_bigframes_set_in_context():
    if bpd is None:
        pytest.skip("BigFrames not installed")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS something"
    expected_configuration = {
        "query": {"queryParameters": [], "useLegacySql": False},
        "dryRun": False,
    }
    bf_patch = mock.patch("bigframes.pandas.read_gbq_query", autospec=True)

    with bf_patch as bf_mock:
        ip.run_cell_magic("bigquery", "", sql)

        bf_mock.assert_called_once_with(
            sql, max_results=None, configuration=expected_configuration
        )
        assert bpd.options.bigquery.credentials is bigquery_magics.context.credentials
        assert bpd.options.bigquery.project == bigquery_magics.context.project


@pytest.mark.usefixtures("mock_credentials")
def test_bigquery_magic_bigframes_set_in_args():
    if bpd is None:
        pytest.skip("BigFrames not installed")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS something"
    expected_configuration = {
        "query": {"queryParameters": [], "useLegacySql": False},
        "dryRun": False,
    }
    bf_patch = mock.patch("bigframes.pandas.read_gbq_query", autospec=True)

    with bf_patch as bf_mock:
        ip.run_cell_magic("bigquery", "--engine bigframes", sql)

        bf_mock.assert_called_once_with(
            sql, max_results=None, configuration=expected_configuration
        )
        assert bpd.options.bigquery.credentials is bigquery_magics.context.credentials
        assert bpd.options.bigquery.project == bigquery_magics.context.project


@pytest.mark.usefixtures("mock_credentials", "set_bigframes_engine_in_context")
def test_bigquery_magic_bigframes__bigframes_is_not_installed__should_raise_error():
    if bpd is not None:
        pytest.skip("BigFrames is installed")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS something"

    with pytest.raises(ValueError, match="Bigframes package is not installed."):
        ip.run_cell_magic("bigquery", "", sql)


@pytest.mark.usefixtures("mock_credentials", "set_bigframes_engine_in_context")
def test_bigquery_magic_bigframes_with_params():
    if bpd is None:
        pytest.skip("BigFrames not installed")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS @p"
    expected_configuration = {
        "query": {
            "queryParameters": [
                {
                    "name": "p",
                    "parameterType": {"type": "STRING"},
                    "parameterValue": {"value": "num"},
                },
            ],
            "useLegacySql": False,
            "parameterMode": "NAMED",
        },
        "dryRun": False,
    }
    bf_patch = mock.patch("bigframes.pandas.read_gbq_query", autospec=True)

    with bf_patch as bf_mock:
        ip.run_cell_magic("bigquery", '--params {"p":"num"}', sql)

        bf_mock.assert_called_once_with(
            sql, max_results=None, configuration=expected_configuration
        )


@pytest.mark.usefixtures("mock_credentials", "set_bigframes_engine_in_context")
def test_bigquery_magic_bigframes_with_max_results():
    if bpd is None:
        pytest.skip("BigFrames not installed")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS something"
    expected_configuration = {
        "query": {"queryParameters": [], "useLegacySql": False},
        "dryRun": False,
    }
    bf_patch = mock.patch("bigframes.pandas.read_gbq_query", autospec=True)

    with bf_patch as bf_mock:
        ip.run_cell_magic("bigquery", "--max_results 10", sql)

        bf_mock.assert_called_once_with(
            sql, max_results=10, configuration=expected_configuration
        )


@pytest.mark.usefixtures("mock_credentials", "set_bigframes_engine_in_context")
def test_bigquery_magic_bigframes_with_destination_var(ipython_ns_cleanup):
    if bpd is None:
        pytest.skip("BigFrames not installed")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS something"

    bf_patch = mock.patch("bigframes.pandas.read_gbq_query", autospec=True)
    ipython_ns_cleanup.append((ip, "df"))

    with bf_patch as bf_mock:
        ip.run_cell_magic("bigquery", "df", sql)

        assert "df" in ip.user_ns
        df = ip.user_ns["df"]
        assert df is bf_mock.return_value


@pytest.mark.usefixtures("mock_credentials", "set_bigframes_engine_in_context")
def test_bigquery_magic_bigframes_with_default_variable(
    ipython_ns_cleanup, monkeypatch
):
    if bpd is None:
        pytest.skip("BigFrames not installed")

    monkeypatch.setattr(bigquery_magics.context, "default_variable", "_bq_df")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS something"

    bf_patch = mock.patch("bigframes.pandas.read_gbq_query", autospec=True)
    ipython_ns_cleanup.append((ip, "_bq_df"))

    with bf_patch as bf_mock:
        ip.run_cell_magic("bigquery", "", sql)

        assert "_bq_df" in ip.user_ns
        df = ip.user_ns["_bq_df"]
        assert df is bf_mock.return_value


@pytest.mark.usefixtures("mock_credentials", "set_bigframes_engine_in_context")
def test_bigquery_magic_bigframes_with_dry_run__should_fail():
    if bpd is None:
        pytest.skip("BigFrames not installed")

    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")
    sql = "SELECT 0 AS @p"

    bf_patch = mock.patch("bigframes.pandas.read_gbq_query", autospec=True)

    with bf_patch, pytest.raises(ValueError):
        ip.run_cell_magic("bigquery", "--dry_run", sql)


def test_test_bigquery_magic__extension_not_loaded__is_registered():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.unload_extension("bigquery_magics")
    assert bigquery_magics.is_registered is False


def test_test_bigquery_magic__extension_loaded__is_registered_set_to_true():
    globalipapp.start_ipython()
    ip = globalipapp.get_ipython()
    ip.extension_manager.load_extension("bigquery_magics")

    assert bigquery_magics.is_registered is True
