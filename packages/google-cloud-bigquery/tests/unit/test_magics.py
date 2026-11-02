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

import copy
import re
import warnings
from concurrent import futures
from unittest import mock

import google.auth.credentials
import pytest
from google.api_core import exceptions
from google.cloud import bigquery
from google.cloud.bigquery import exceptions as bq_exceptions
from google.cloud.bigquery import job, table
from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
from test_utils.imports import maybe_fail_import

from tests.unit.helpers import make_connection

try:
    from google.cloud.bigquery.magics import magics
except ImportError:
    magics = None


bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
IPython = pytest.importorskip("IPython")
interactiveshell = pytest.importorskip("IPython.core.interactiveshell")
tools = pytest.importorskip("IPython.testing.tools")
io = pytest.importorskip("IPython.utils.io")
pandas = pytest.importorskip("pandas")


@pytest.fixture(autouse=True)
def use_local_magics_context(monkeypatch):
    if magics is not None:  # pragma: NO COVER
        local_context = magics.Context()
        local_context._project = "unit-test-project"
        mock_credentials = mock.create_autospec(
            google.auth.credentials.Credentials, instance=True
        )
        local_context._credentials = mock_credentials
        monkeypatch.setattr(magics, "context", local_context)


@pytest.fixture(scope="session")
def ipython():
    config = tools.default_config()
    shell = interactiveshell.InteractiveShell.instance(config=config)
    return shell


@pytest.fixture()
def ipython_interactive(request, ipython):
    """Activate IPython's builtin hooks

    for the duration of the test scope.
    """
    with ipython.builtin_trap:
        yield ipython


@pytest.fixture()
def ipython_ns_cleanup():
    """A helper to clean up user namespace after the test

    for the duration of the test scope.
    """
    names_to_clean = []  # pairs (IPython_instance, name_to_clean)

    yield names_to_clean

    for ip, name in names_to_clean:
        if name in ip.user_ns:
            del ip.user_ns[name]


@pytest.fixture(scope="session")
def missing_bq_storage():
    """Provide a patcher that can make the bigquery storage import to fail."""

    def fail_if(name, globals, locals, fromlist, level):
        # NOTE: *very* simplified, assuming a straightforward absolute import
        return "bigquery_storage" in name or (
            fromlist is not None and "bigquery_storage" in fromlist
        )

    return maybe_fail_import(predicate=fail_if)


@pytest.fixture(scope="session")
def missing_grpcio_lib():
    """Provide a patcher that can make the gapic library import to fail."""

    def fail_if(name, globals, locals, fromlist, level):
        # NOTE: *very* simplified, assuming a straightforward absolute import
        return "gapic_v1" in name or (fromlist is not None and "gapic_v1" in fromlist)

    return maybe_fail_import(predicate=fail_if)


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


def test_context_resolves_unset_credentials_and_project():
    """When context credentials and project are unset (None), accessing them
    resolves them from Application Default Credentials.
    """
    magics.context._credentials = None
    magics.context._project = None
    assert magics.context._credentials is None
    assert magics.context._project is None

    project = "prahj-ekt"
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, project)
    )
    with default_patch as default_mock:
        assert magics.context.credentials is credentials_mock
        assert magics.context.project == project

    assert default_mock.call_count == 2


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_context_with_default_connection(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._credentials = None
    magics.context._project = None
    magics.context._connection = None

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
    )
    default_conn.api_request.assert_has_calls([begin_call, query_results_call])


def test_context_credentials_and_project_can_be_set_explicitly():
    project1 = "one-project-55564"
    project2 = "other-project-52569"
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, project1)
    )
    with default_patch as default_mock:
        magics.context.credentials = credentials_mock
        magics.context.project = project2

    assert magics.context.project == project2
    assert magics.context.credentials is credentials_mock
    # default should not be called if credentials & project are explicitly set
    assert default_mock.call_count == 0


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_context_with_custom_connection(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None
    magics.context._credentials = None
    context_conn = magics.context._connection = make_connection(
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
    )
    context_conn.api_request.assert_has_calls([begin_call, query_results_call])


def test__run_query():
    magics.context._credentials = None

    job_id = "job_1234"
    sql = "SELECT 17"
    responses = [
        futures.TimeoutError,
        futures.TimeoutError,
        [table.Row((17,), {"num": 0})],
    ]

    client_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client", autospec=True
    )
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
    magics.context._credentials = None

    sql = "SELECT 17"

    client_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client", autospec=True
    )

    job_config = job.QueryJobConfig()
    job_config.dry_run = True
    with client_patch as client_mock, io.capture_output() as captured:
        client_mock().query(sql).job_id = None
        magics._run_query(client_mock(), sql, job_config=job_config)

    assert len(captured.stderr) == 0
    assert len(captured.stdout) == 0


def test__make_bqstorage_client_false():
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    test_client = bigquery.Client(
        project="test_project", credentials=credentials_mock, location="test_location"
    )
    got = magics._make_bqstorage_client(test_client, False, {})
    assert got is None


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test__make_bqstorage_client_true():
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    test_client = bigquery.Client(
        project="test_project", credentials=credentials_mock, location="test_location"
    )
    got = magics._make_bqstorage_client(test_client, True, {})
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
        magics._make_bqstorage_client(test_client, True, {})

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
        "google.cloud.bigquery._versions_helpers.BQ_STORAGE_VERSIONS.try_import",
        side_effect=bq_exceptions.LegacyBigQueryStorageError(
            "google-cloud-bigquery-storage is outdated"
        ),
    )
    with patcher, warnings.catch_warnings(record=True) as warned:
        got = magics._make_bqstorage_client(test_client, True, {})

    assert got is None

    matching_warnings = [
        warning
        for warning in warned
        if "google-cloud-bigquery-storage is outdated" in str(warning)
    ]
    assert matching_warnings, "Obsolete dependency warning not raised."


@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test__make_bqstorage_client_true_missing_gapic(missing_grpcio_lib):
    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    with pytest.raises(ImportError) as exc_context, missing_grpcio_lib:
        magics._make_bqstorage_client(True, credentials_mock, {})

    assert "grpcio" in str(exc_context.value)


def test__create_dataset_if_necessary_exists():
    project = "project_id"
    dataset_id = "dataset_id"
    dataset_reference = bigquery.dataset.DatasetReference(project, dataset_id)
    dataset = bigquery.Dataset(dataset_reference)
    client_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client", autospec=True
    )
    with client_patch as client_mock:
        client = client_mock()
        client.project = project
        client.get_dataset.result_value = dataset
        magics._create_dataset_if_necessary(client, dataset_id)
        client.create_dataset.assert_not_called()


def test__create_dataset_if_necessary_not_exist():
    project = "project_id"
    dataset_id = "dataset_id"
    client_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client", autospec=True
    )
    with client_patch as client_mock:
        client = client_mock()
        client.location = "us"
        client.project = project
        client.get_dataset.side_effect = exceptions.NotFound("dataset not found")
        magics._create_dataset_if_necessary(client, dataset_id)
        client.create_dataset.assert_called_once()


@pytest.mark.usefixtures("ipython_interactive")
def test_extension_load():
    ip = IPython.get_ipython()

    with pytest.warns(FutureWarning, match="bigquery_magics"):
        bigquery.load_ipython_extension(ip)


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_without_optional_arguments(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(magics.context, "_credentials", mock_credentials)

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
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    magics.context.project = "unit-test-project"
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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_default_connection_user_agent(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._connection = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    conn_patch = mock.patch("google.cloud.bigquery.client.Connection", autospec=True)

    with conn_patch as conn, run_query_patch, default_patch:
        ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

    client_info_arg = conn.call_args[1].get("client_info")
    assert client_info_arg is not None
    assert client_info_arg.user_agent == "ipython-" + IPython.__version__


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_legacy_sql(monkeypatch, use_local_magics_context):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--use_legacy_sql", "SELECT 17 AS num")

        job_config_used = run_query_mock.call_args_list[0][1]["job_config"]
        assert job_config_used.use_legacy_sql is True


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_result_saved_to_variable(
    ipython_ns_cleanup, monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "df"))

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    assert "df" not in ip.user_ns

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_does_not_clear_display_in_verbose_mode(
    monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    clear_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.display.clear_output",
        autospec=True,
    )
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with clear_patch as clear_mock, run_query_patch:
        ip.run_cell_magic("bigquery", "--verbose", "SELECT 17 as num")

        assert clear_mock.call_count == 0


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_clears_display_in_non_verbose_mode(
    monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    clear_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.display.clear_output",
        autospec=True,
    )
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with clear_patch as clear_mock, run_query_patch:
        ip.run_cell_magic("bigquery", "", "SELECT 17 as num")

        assert clear_mock.call_count == 1


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_with_bqstorage_from_argument(
    monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(magics.context, "_credentials", mock_credentials)

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
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.to_dataframe.return_value = result
    with run_query_patch as run_query_mock, (
        bqstorage_client_patch
    ), warnings.catch_warnings(record=True) as warned:
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
    assert client_info.user_agent.startswith("ipython-" + IPython.__version__)
    assert "pandas-gbq" in client_info.user_agent

    query_job_mock.to_dataframe.assert_called_once_with(
        bqstorage_client=bqstorage_instance_mock,
        create_bqstorage_client=mock.ANY,
        progress_bar_type="tqdm_notebook",
    )

    assert isinstance(return_value, pandas.DataFrame)


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
def test_bigquery_magic_with_rest_client_requested(
    monkeypatch, use_local_magics_context
):
    pandas = pytest.importorskip("pandas")

    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_max_results_invalid(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_max_results_valid_calls_queryjob_result(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_max_results_query_job_results_fails(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

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
        "google.cloud.bigquery.magics.magics._close_transports",
        autospec=True,
    )

    sql = "SELECT 17 AS num"

    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    query_job_mock.result.side_effect = [[], OSError]

    with pytest.raises(
        OSError
    ), client_query_patch as client_query_mock, (
        default_patch
    ), close_transports_patch as close_transports:
        client_query_mock.return_value = query_job_mock
        ip.run_cell_magic("bigquery", "--max_results=5", sql)

    assert close_transports.called


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_table_id_invalid(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    list_rows_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client.list_rows",
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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_missing_query(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_w_table_id_and_destination_var(ipython_ns_cleanup, monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

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

    client_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client", autospec=True
    )

    table_id = "bigquery-public-data.samples.shakespeare"
    result = pandas.DataFrame([17], columns=["num"])

    with client_patch as client_mock, default_patch:
        client_mock().list_rows.return_value = row_iterator_mock
        row_iterator_mock.to_dataframe.return_value = result

        ip.run_cell_magic("bigquery", "df", table_id)

    assert "df" in ip.user_ns
    df = ip.user_ns["df"]

    assert isinstance(df, pandas.DataFrame)


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(
    bigquery_storage is None, reason="Requires `google-cloud-bigquery-storage`"
)
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_w_table_id_and_bqstorage_client(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    row_iterator_mock = mock.create_autospec(
        google.cloud.bigquery.table.RowIterator, instance=True
    )

    client_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client", autospec=True
    )

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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_dryrun_option_sets_job_config(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    magics.context.project = "project-from-context"
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

    sql = "SELECT 17 AS num"

    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--dry_run", sql)

        job_config_used = run_query_mock.call_args_list[0][1]["job_config"]
        assert job_config_used.dry_run is True


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_dryrun_option_returns_query_job(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context.project = "project-from-context"
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

    sql = "SELECT 17 AS num"

    with run_query_patch as run_query_mock, io.capture_output() as captured_io:
        run_query_mock.return_value = query_job_mock
        return_value = ip.run_cell_magic("bigquery", "--dry_run", sql)

        assert "Query validated. This query will process" in captured_io.stdout
        assert isinstance(return_value, job.QueryJob)


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_dryrun_option_variable_error_message(
    ipython_ns_cleanup, monkeypatch
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    magics.context.project = "project-from-context"
    ipython_ns_cleanup.append((ip, "q_job"))

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query",
        autospec=True,
        side_effect=exceptions.BadRequest("Syntax error in SQL query"),
    )

    sql = "SELECT SELECT 17 AS num"

    assert "q_job" not in ip.user_ns

    with run_query_patch, io.capture_output() as captured:
        ip.run_cell_magic("bigquery", "q_job --dry_run", sql)

    full_text = captured.stderr
    assert "Could not save output to variable 'q_job'." in full_text


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_dryrun_option_saves_query_job_to_variable(
    ipython_ns_cleanup, monkeypatch
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context.project = "project-from-context"
    query_job_mock = mock.create_autospec(
        google.cloud.bigquery.job.QueryJob, instance=True
    )
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_saves_query_job_to_variable_on_error(
    ipython_ns_cleanup, monkeypatch
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    magics.context.project = "project-from-context"
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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_maximum_bytes_billed_invalid(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

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
@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_w_maximum_bytes_billed_overrides_context(
    param_value, expected, monkeypatch
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    # Set the default maximum bytes billed, so we know it's overridable by the param.
    magics.context.default_query_job_config.maximum_bytes_billed = 1234567

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
    conn = magics.context._connection = make_connection(resource, query_results, data)
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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_w_maximum_bytes_billed_w_context_inplace(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    magics.context.default_query_job_config.maximum_bytes_billed = 1337

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
    conn = magics.context._connection = make_connection(resource, query_results, data)
    list_rows_patch = mock.patch(
        "google.cloud.bigquery.client.Client._list_rows_from_query_results",
        return_value=google.cloud.bigquery.table._EmptyRowIterator(),
    )
    with list_rows_patch, default_patch:
        ip.run_cell_magic("bigquery", "", query)

    _, req = conn.api_request.call_args_list[0]
    sent_config = req["data"]["configuration"]["query"]
    assert sent_config["maximumBytesBilled"] == "1337"


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_w_maximum_bytes_billed_w_context_setter(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    magics.context.default_query_job_config = job.QueryJobConfig(
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
    conn = magics.context._connection = make_connection(resource, query_results, data)
    list_rows_patch = mock.patch(
        "google.cloud.bigquery.client.Client._list_rows_from_query_results",
        return_value=google.cloud.bigquery.table._EmptyRowIterator(),
    )
    with list_rows_patch, default_patch:
        ip.run_cell_magic("bigquery", "", query)

    _, req = conn.api_request.call_args_list[0]
    sent_config = req["data"]["configuration"]["query"]
    assert sent_config["maximumBytesBilled"] == "10203"


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_no_query_cache(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    conn = make_connection()
    monkeypatch.setattr(magics.context, "_connection", conn)
    monkeypatch.setattr(
        magics.context,
        "credentials",
        mock.create_autospec(google.auth.credentials.Credentials, instance=True),
    )
    monkeypatch.setattr(magics.context, "project", "project-from-context")

    # --no_query_cache option should override context.
    monkeypatch.setattr(
        magics.context.default_query_job_config, "use_query_cache", True
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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_context_with_no_query_cache_from_context(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    context = magics.Context()
    conn = make_connection()
    context._connection = conn
    context.credentials = mock.create_autospec(google.auth.credentials.Credentials)
    context.default_query_job_config = bigquery.QueryJobConfig(use_query_cache=False)
    context.project = "project-from-context"
    monkeypatch.setattr(magics, "context", context)

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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_w_progress_bar_type_w_context_setter(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    magics.context.progress_bar_type = "tqdm_gui"

    mock_credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    # Set up the context with monkeypatch so that it's reset for subsequent
    # tests.
    monkeypatch.setattr(magics.context, "_credentials", mock_credentials)

    # Mock out the BigQuery Storage API.
    bqstorage_mock = mock.create_autospec(bigquery_storage.BigQueryReadClient)
    bqstorage_client_patch = mock.patch(
        "google.cloud.bigquery_storage.BigQueryReadClient", bqstorage_mock
    )

    sql = "SELECT 17 AS num"
    result = pandas.DataFrame([17], columns=["num"])
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    magics.context.project = "unit-test-project"

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
            progress_bar_type=magics.context.progress_bar_type,
        )

    assert isinstance(return_value, pandas.DataFrame)


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_progress_bar_type(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    context = magics.Context()
    conn = make_connection()
    context._connection = conn
    context.credentials = mock.create_autospec(google.auth.credentials.Credentials)
    context.progress_bar_type = None
    context.project = "unit-test-project"
    monkeypatch.setattr(magics, "context", context)

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery", "--progress_bar_type=tqdm_gui", "SELECT 17 as num"
        )

        progress_bar_used = run_query_mock.mock_calls[1][2]["progress_bar_type"]
        assert progress_bar_used == "tqdm_gui"
        # context progress bar type should not change
        assert magics.context.progress_bar_type is None


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_project(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with run_query_patch as run_query_mock, default_patch:
        ip.run_cell_magic("bigquery", "--project=specific-project", "SELECT 17 as num")

        client_used = run_query_mock.call_args_list[0][0][0]
        assert client_used.project == "specific-project"
        # context project should not change
        assert magics.context.project == "general-project"


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_bigquery_api_endpoint(
    ipython_ns_cleanup, monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._connection = None

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bigquery_api_endpoint=https://bigquery_api.endpoint.com",
            "SELECT 17 as num",
        )

    connection_used = run_query_mock.call_args_list[0][0][0]._connection
    assert connection_used.API_BASE_URL == "https://bigquery_api.endpoint.com"
    # context client options should not change
    assert magics.context.bigquery_client_options.api_endpoint is None


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_bigquery_api_endpoint_context_dict(
    monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._connection = None
    magics.context.bigquery_client_options = {}

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bigquery_api_endpoint=https://bigquery_api.endpoint.com",
            "SELECT 17 as num",
        )

    connection_used = run_query_mock.call_args_list[0][0][0]._connection
    assert connection_used.API_BASE_URL == "https://bigquery_api.endpoint.com"
    # context client options should not change
    assert magics.context.bigquery_client_options == {}


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_bqstorage_api_endpoint(
    ipython_ns_cleanup, monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._connection = None

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bqstorage_api_endpoint=https://bqstorage_api.endpoint.com",
            "SELECT 17 as num",
        )

    client_used = run_query_mock.mock_calls[1][2]["bqstorage_client"]
    assert client_used._transport._host == "https://bqstorage_api.endpoint.com"
    # context client options should not change
    assert magics.context.bqstorage_client_options.api_endpoint is None


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_bqstorage_api_endpoint_context_dict(
    monkeypatch, use_local_magics_context
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._connection = None
    magics.context.bqstorage_client_options = {}

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with run_query_patch as run_query_mock:
        ip.run_cell_magic(
            "bigquery",
            "--bqstorage_api_endpoint=https://bqstorage_api.endpoint.com",
            "SELECT 17 as num",
        )

    client_used = run_query_mock.mock_calls[1][2]["bqstorage_client"]
    assert client_used._transport._host == "https://bqstorage_api.endpoint.com"
    # context client options should not change
    assert magics.context.bqstorage_client_options == {}


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_multiple_options(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_string_params(ipython_ns_cleanup, monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame([17], columns=["num"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    magics.context.project = "unit-test-project"

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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_dict_params(ipython_ns_cleanup, monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num, @tricky_value as tricky_value"
    result = pandas.DataFrame(
        [(False, '--params "value"')], columns=["valid", "tricky_value"]
    )

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    magics.context.project = "unit-test-project"

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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_dict_params_nonexisting(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @foo AS foo"

    with pytest.raises(NameError, match=r".*undefined variable.*unknown_name.*"):
        ip.run_cell_magic("bigquery", "params_dict_df --params $unknown_name", sql)


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_dict_params_incorrect_syntax(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @foo AS foo"

    with pytest.raises(SyntaxError, match=r".*--params.*"):
        cell_magic_args = "params_dict_df --params {'foo': 1; 'bar': 2}"
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_dict_params_duplicate(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @foo AS foo"

    with pytest.raises(ValueError, match=r"Duplicate --params option\."):
        cell_magic_args = (
            "params_dict_df --params {'foo': 1} --verbose --params {'bar': 2} "
        )
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_option_value_incorrect(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context.project = "unit-test-project"

    sql = "SELECT @foo AS foo"

    with pytest.raises(ValueError, match=r".*invalid literal.*\[PLENTY!\].*"):
        cell_magic_args = "params_dict_df --max_results [PLENTY!]"
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_dict_params_negative_value(
    ipython_ns_cleanup, monkeypatch
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame([-17], columns=["num"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    magics.context.project = "unit-test-project"

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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_dict_params_array_value(ipython_ns_cleanup, monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame(["foo bar", "baz quux"], columns=["array_data"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    magics.context.project = "unit-test-project"

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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_dict_params_tuple_value(ipython_ns_cleanup, monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    ipython_ns_cleanup.append((ip, "params_dict_df"))

    sql = "SELECT @num AS num"
    result = pandas.DataFrame(["foo bar", "baz quux"], columns=["array_data"])

    assert "params_dict_df" not in ip.user_ns

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    magics.context.project = "unit-test-project"

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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_improperly_formatted_params(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @num AS num"

    with pytest.raises(SyntaxError):
        ip.run_cell_magic("bigquery", "--params {17}", sql)


@pytest.mark.parametrize(
    "raw_sql", ("SELECT answer AS 42", " \t   SELECT answer AS 42  \t  ")
)
@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_valid_query_in_existing_variable(
    ipython_ns_cleanup, raw_sql, monkeypatch
):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context.project = "unit-test-project"

    ipython_ns_cleanup.append((ip, "custom_query"))
    ipython_ns_cleanup.append((ip, "query_results_df"))

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
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


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_nonexisting_query_variable(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context.project = "unit-test-project"

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

    ip.user_ns.pop("custom_query", None)  # Make sure the variable does NOT exist.
    cell_body = "$custom_query"  # Referring to a non-existing variable name.

    with pytest.raises(
        NameError, match=r".*custom_query does not exist.*"
    ), run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "", cell_body)

    run_query_mock.assert_not_called()


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_empty_query_variable_name(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context.project = "unit-test-project"
    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    cell_body = "$"  # Not referring to any variable (name omitted).

    with pytest.raises(
        NameError, match=r"(?i).*missing query variable name.*"
    ), run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "", cell_body)

    run_query_mock.assert_not_called()


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_query_variable_non_string(ipython_ns_cleanup, monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context.project = "unit-test-project"

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

    ipython_ns_cleanup.append((ip, "custom_query"))

    ip.user_ns["custom_query"] = object()
    cell_body = "$custom_query"  # Referring to a non-string variable.

    with pytest.raises(
        TypeError, match=r".*must be a string or a bytes-like.*"
    ), run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "", cell_body)

    run_query_mock.assert_not_called()


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_query_variable_not_identifier(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    magics.context.project = "unit-test-project"
    cell_body = "$123foo"  # 123foo is not valid Python identifier

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

    with run_query_patch, io.capture_output() as captured_io:
        ip.run_cell_magic("bigquery", "", cell_body)

    # If "$" prefixes a string that is not a Python identifier, we do not treat such
    # cell_body as a variable reference and just treat is as any other cell body input.
    # If at the same time the cell body does not contain any whitespace, it is
    # considered a table name, thus we expect an error that the table ID is not valid.
    output = captured_io.stderr
    assert "ERROR:" in output
    assert "Could not parse table_id." in output


@pytest.mark.usefixtures("ipython_interactive")
@pytest.mark.skipif(pandas is None, reason="Requires `pandas`")
def test_bigquery_magic_with_invalid_multiple_option_values(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )

    sql = "SELECT @foo AS foo"

    exc_pattern = r".*[Uu]nrecognized input.*option values correct\?.*567.*"

    with pytest.raises(ValueError, match=exc_pattern):
        cell_magic_args = "params_dict_df --max_results 10 567"
        ip.run_cell_magic("bigquery", cell_magic_args, sql)


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_omits_tracebacks_from_error_message(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query",
        autospec=True,
        side_effect=exceptions.BadRequest("Syntax error in SQL query"),
    )

    with run_query_patch, default_patch, io.capture_output() as captured_io:
        ip.run_cell_magic("bigquery", "", "SELECT foo FROM WHERE LIMIT bar")

    output = captured_io.stderr
    assert "400 Syntax error in SQL query" in output
    assert "Traceback (most recent call last)" not in output
    assert "Syntax error" not in captured_io.stdout


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_destination_table_invalid_format(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context._project = None

    credentials_mock = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    default_patch = mock.patch(
        "google.auth.default", return_value=(credentials_mock, "general-project")
    )

    client_patch = mock.patch(
        "google.cloud.bigquery.magics.magics.bigquery.Client", autospec=True
    )

    with client_patch, default_patch, pytest.raises(ValueError) as exc_context:
        ip.run_cell_magic(
            "bigquery", "--destination_table dataset", "SELECT foo FROM WHERE LIMIT bar"
        )
    error_msg = str(exc_context.value)
    assert (
        "--destination_table should be in a "
        "<dataset_id>.<table_id> format." in error_msg
    )


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_w_destination_table(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context._project = "test-project"

    create_dataset_if_necessary_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._create_dataset_if_necessary",
        autospec=True,
    )

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )

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


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_create_dataset_fails(monkeypatch):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)
    magics.context.credentials = mock.create_autospec(
        google.auth.credentials.Credentials, instance=True
    )
    magics.context._project = "test-project"

    create_dataset_if_necessary_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._create_dataset_if_necessary",
        autospec=True,
        side_effect=OSError,
    )
    close_transports_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._close_transports",
        autospec=True,
    )

    with pytest.raises(
        OSError
    ), create_dataset_if_necessary_patch, close_transports_patch as close_transports:
        ip.run_cell_magic(
            "bigquery",
            "--destination_table dataset_id.table_id",
            "SELECT foo FROM WHERE LIMIT bar",
        )

    assert close_transports.called


@pytest.mark.usefixtures("ipython_interactive")
def test_bigquery_magic_with_location(monkeypatch, use_local_magics_context):
    ip = IPython.get_ipython()
    monkeypatch.setattr(bigquery, "bigquery_magics", None)
    bigquery.load_ipython_extension(ip)

    run_query_patch = mock.patch(
        "google.cloud.bigquery.magics.magics._run_query", autospec=True
    )
    with run_query_patch as run_query_mock:
        ip.run_cell_magic("bigquery", "--location=us-east1", "SELECT 17 AS num")

        client_options_used = run_query_mock.call_args_list[0][0][0]
        assert client_options_used.location == "us-east1"
