# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import copy
import datetime
import re
import warnings
from unittest import mock

import google.api_core.exceptions
import google.cloud.bigquery
import google.cloud.bigquery.table
import numpy
import packaging.version
import pandas
import pytest
from pandas import DataFrame

import pandas_gbq.constants
import pandas_gbq.core.read
import pandas_gbq.exceptions
import pandas_gbq.features
from pandas_gbq import gbq
from pandas_gbq.features import FEATURES

pytestmark = pytest.mark.filterwarnings("ignore:credentials from Google Cloud SDK")


def _make_connector(project_id="some-project", **kwargs):
    return gbq.GbqConnector(project_id, **kwargs)


def mock_get_credentials_no_project(*args, **kwargs):
    import google.auth.credentials

    mock_credentials = mock.create_autospec(google.auth.credentials.Credentials)
    return mock_credentials, None


@pytest.fixture
def mock_query_job():
    mock_query = mock.create_autospec(google.cloud.bigquery.QueryJob)
    mock_query.job_id = "some-random-id"
    mock_query.state = "DONE"
    return mock_query


@pytest.fixture
def mock_row_iterator(mock_bigquery_client):
    mock_rows = mock.create_autospec(google.cloud.bigquery.table.RowIterator)
    mock_rows.total_rows = 1
    mock_rows.__iter__.return_value = [(1,)]

    # Mock out SELECT 1 query results.
    def generate_schema():
        if mock_bigquery_client.query.call_args:
            query = mock_bigquery_client.query.call_args[0][0]
        elif (
            hasattr(mock_bigquery_client, "query_and_wait")
            and mock_bigquery_client.query_and_wait.call_args
        ):
            query = mock_bigquery_client.query_and_wait.call_args[0][0]
        else:
            query = ""
        if query == "SELECT 1 AS int_col":
            return [google.cloud.bigquery.SchemaField("int_col", "INTEGER")]
        else:
            return [google.cloud.bigquery.SchemaField("_f0", "INTEGER")]

    type(mock_rows).schema = mock.PropertyMock(side_effect=generate_schema)
    return mock_rows


@pytest.fixture(autouse=True)
def default_bigquery_client(mock_bigquery_client, mock_query_job, mock_row_iterator):
    mock_query_job.result.return_value = mock_row_iterator
    # Set up RowIterator.job to point to QueryJob for dry_run access
    mock_row_iterator.job = mock_query_job
    mock_bigquery_client.list_rows.return_value = mock_row_iterator
    mock_bigquery_client.query.return_value = mock_query_job

    if hasattr(mock_bigquery_client, "query_and_wait"):
        mock_bigquery_client.query_and_wait.return_value = mock_row_iterator

    # Mock out get_table.
    def get_table(table_ref_or_id, **kwargs):
        return google.cloud.bigquery.Table(table_ref_or_id)

    mock_bigquery_client.get_table.side_effect = get_table

    return mock_bigquery_client


@pytest.mark.parametrize(
    ("type_", "expected"),
    [
        ("SOME_NEW_UNKNOWN_TYPE", None),
        ("INTEGER", "Int64"),
        ("FLOAT", numpy.dtype(float)),
        # TIMESTAMP/DATETIME might require object dtype for out-of-bounds
        # values.
        ("TIMESTAMP", None),
        ("DATETIME", None),
    ],
)
def test__bqschema_to_nullsafe_dtypes(type_, expected):
    result = pandas_gbq.core.read._bqschema_to_nullsafe_dtypes(
        [dict(name="x", type=type_, mode="NULLABLE")]
    )
    if not expected:
        assert result == {}
    else:
        assert result == {"x": expected}


@pytest.mark.parametrize(
    ["query_or_table", "expected"],
    [
        ("SELECT 1", True),
        ("SELECT\n1", True),
        ("SELECT\t1", True),
        ("dataset.table", False),
        (" dataset.table ", False),
        ("\r\ndataset.table\r\n", False),
        ("project-id.dataset.table", False),
        (" project-id.dataset.table ", False),
        ("\r\nproject-id.dataset.table\r\n", False),
    ],
)
def test__is_query(query_or_table, expected):
    result = gbq._is_query(query_or_table)
    assert result == expected


@pytest.mark.parametrize(
    ["original", "expected"],
    [
        (None, None),
        ({}, {}),
        ({"query": {"useQueryCache": False}}, {"query": {"useQueryCache": False}}),
        ({"jobTimeoutMs": "1234"}, {"jobTimeoutMs": "1234"}),
        ({"query": {"timeoutMs": "1234"}}, {"query": {}, "jobTimeoutMs": "1234"}),
    ],
)
def test__transform_read_gbq_configuration_makes_copy(original, expected):
    should_change = original == expected
    got = gbq._transform_read_gbq_configuration(original)
    assert got == expected
    # Catch if we accidentally modified the original.
    did_change = original == got
    assert did_change == should_change


def test_GbqConnector_download_results_warns_for_large_tables(default_bigquery_client):
    gbq._test_google_api_imports()
    connector = _make_connector()
    rows_iter = mock.create_autospec(
        google.cloud.bigquery.table.RowIterator, instance=True
    )
    table = google.cloud.bigquery.Table.from_api_repr(
        {
            "tableReference": {
                "projectId": "my-proj",
                "datasetId": "my-dset",
                "tableId": "my_tbl",
            },
            "numBytes": 2 * pandas_gbq.constants.BYTES_IN_GIB,
        },
    )
    rows_iter._table = table
    default_bigquery_client.get_table.reset_mock(side_effect=True)
    default_bigquery_client.get_table.return_value = table

    with pytest.warns(
        pandas_gbq.exceptions.LargeResultsWarning,
        match=re.escape("Your results are 2.0 GiB. Consider using BigQuery DataFrames"),
    ):
        connector._download_results(rows_iter)


def test_GbqConnector_download_results_doesnt_warn_for_small_tables(
    default_bigquery_client,
):
    gbq._test_google_api_imports()
    connector = _make_connector()
    rows_iter = mock.create_autospec(
        google.cloud.bigquery.table.RowIterator, instance=True
    )
    table = google.cloud.bigquery.Table.from_api_repr(
        {
            "tableReference": {
                "projectId": "my-proj",
                "datasetId": "my-dset",
                "tableId": "my_tbl",
            },
            "numBytes": 999 * pandas_gbq.constants.BYTES_IN_MIB,
        },
    )
    rows_iter._table = table
    default_bigquery_client.get_table.reset_mock(side_effect=True)
    default_bigquery_client.get_table.return_value = table

    with warnings.catch_warnings():
        warnings.simplefilter(
            "error", category=pandas_gbq.exceptions.LargeResultsWarning
        )
        connector._download_results(rows_iter)


def test_GbqConnector_get_client_w_new_bq(mock_bigquery_client):
    gbq._test_google_api_imports()
    pytest.importorskip("google.api_core.client_info")

    connector = _make_connector()
    connector.get_client()

    _, kwargs = mock_bigquery_client.call_args
    assert kwargs["client_info"].user_agent == "pandas-{}".format(pandas.__version__)


def test_GbqConnector_process_http_error_transforms_timeout():
    original = google.api_core.exceptions.GoogleAPICallError(
        "Job execution was cancelled: Job timed out after 0s"
    )
    with pytest.raises(gbq.QueryTimeout):
        gbq.GbqConnector.process_http_error(original)


def test_to_gbq_should_fail_if_invalid_table_name_passed():
    with pytest.raises(gbq.NotFoundException):
        gbq.to_gbq(DataFrame([[1]]), "invalid_table_name", project_id="1234")


def test_to_gbq_with_no_project_id_given_should_fail(monkeypatch):
    import pydata_google_auth

    monkeypatch.setattr(pydata_google_auth, "default", mock_get_credentials_no_project)

    with pytest.raises(ValueError, match="Could not determine project ID"):
        gbq.to_gbq(DataFrame([[1]]), "dataset.tablename")


@pytest.mark.parametrize(
    ["api_method", "warning_message", "warning_type"],
    [
        ("load_parquet", "chunksize is ignored", DeprecationWarning),
        ("load_csv", "chunksize will be ignored", PendingDeprecationWarning),
    ],
)
def test_to_gbq_with_chunksize_warns_deprecation(
    api_method, warning_message, warning_type
):
    with pytest.warns(warning_type, match=warning_message):
        gbq.to_gbq(
            DataFrame([[1]]),
            "dataset.tablename",
            project_id="my-project",
            api_method=api_method,
            chunksize=100,
        )


@pytest.mark.parametrize(["verbose"], [(True,), (False,)])
def test_to_gbq_with_verbose_new_pandas_warns_deprecation(monkeypatch, verbose):
    monkeypatch.setattr(
        type(FEATURES),
        "pandas_has_deprecated_verbose",
        mock.PropertyMock(return_value=True),
    )
    with pytest.warns(FutureWarning, match="verbose is deprecated"):
        gbq.to_gbq(
            DataFrame([[1]]),
            "dataset.tablename",
            project_id="my-project",
            verbose=verbose,
        )


def test_to_gbq_with_private_key_raises_notimplementederror():
    with pytest.raises(NotImplementedError, match="private_key"):
        gbq.to_gbq(
            DataFrame([[1]]),
            "dataset.tablename",
            project_id="my-project",
            private_key="path/to/key.json",
        )


def test_to_gbq_doesnt_run_query(mock_bigquery_client):
    gbq.to_gbq(DataFrame([[1]]), "dataset.tablename", project_id="my-project")
    mock_bigquery_client.query.assert_not_called()


def test_to_gbq_w_empty_df(mock_bigquery_client):
    import google.api_core.exceptions

    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    gbq.to_gbq(DataFrame(), "my_dataset.my_table", project_id="1234")
    mock_bigquery_client.create_table.assert_called_with(mock.ANY)
    mock_bigquery_client.load_table_from_dataframe.assert_not_called()
    mock_bigquery_client.load_table_from_file.assert_not_called()


def test_to_gbq_w_default_project(mock_bigquery_client):
    """If no project is specified, we should be able to use project from
    default credentials.
    """
    import google.api_core.exceptions
    from google.cloud.bigquery.table import TableReference

    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    gbq.to_gbq(DataFrame(), "my_dataset.my_table")

    mock_bigquery_client.get_table.assert_called_with(
        TableReference.from_string("default-project.my_dataset.my_table")
    )
    mock_bigquery_client.create_table.assert_called_with(mock.ANY)
    table = mock_bigquery_client.create_table.call_args[0][0]
    assert table.project == "default-project"


def test_to_gbq_w_project_table(mock_bigquery_client):
    """If a project is included in the table ID, use that instead of the client
    project. See: https://github.com/pydata/pandas-gbq/issues/321
    """
    import google.api_core.exceptions
    from google.cloud.bigquery.table import TableReference

    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    gbq.to_gbq(
        DataFrame(),
        "project_table.my_dataset.my_table",
        project_id="project_client",
    )

    mock_bigquery_client.get_table.assert_called_with(
        TableReference.from_string("project_table.my_dataset.my_table")
    )
    mock_bigquery_client.create_table.assert_called_with(mock.ANY)
    table = mock_bigquery_client.create_table.call_args[0][0]
    assert table.project == "project_table"


def test_to_gbq_create_dataset(mock_bigquery_client):
    import google.api_core.exceptions

    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    mock_bigquery_client.get_dataset.side_effect = google.api_core.exceptions.NotFound(
        "my_dataset"
    )
    gbq.to_gbq(DataFrame([[1]]), "my_dataset.my_table", project_id="1234")
    mock_bigquery_client.create_dataset.assert_called_with(mock.ANY)


def test_dataset_create_already_exists_translates_exception(mock_bigquery_client):
    connector = gbq._Dataset("my-project")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_dataset.return_value = object()
    with pytest.raises(gbq.DatasetCreationError):
        connector.create("already_exists")


def test_dataset_exists_false(mock_bigquery_client):
    connector = gbq._Dataset("my-project")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_dataset.side_effect = google.api_core.exceptions.NotFound(
        "nope"
    )
    assert not connector.exists("not_exists")


def test_dataset_exists_true(mock_bigquery_client):
    connector = gbq._Dataset("my-project")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_dataset.return_value = object()
    assert connector.exists("yes_exists")


def test_dataset_exists_translates_exception(mock_bigquery_client):
    connector = gbq._Dataset("my-project")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_dataset.side_effect = (
        google.api_core.exceptions.InternalServerError("something went wrong")
    )
    with pytest.raises(gbq.GenericGBQException):
        connector.exists("not_gonna_work")


def test_table_create_already_exists(mock_bigquery_client):
    connector = gbq._Table("my-project", "my_dataset")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_table.return_value = object()
    with pytest.raises(gbq.TableCreationError):
        connector.create(
            "already_exists", {"fields": [{"name": "f", "type": "STRING"}]}
        )


def test_table_create_translates_exception(mock_bigquery_client):
    connector = gbq._Table("my-project", "my_dataset")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "nope"
    )
    mock_bigquery_client.create_table.side_effect = (
        google.api_core.exceptions.InternalServerError("something went wrong")
    )
    with pytest.raises(gbq.GenericGBQException):
        connector.create(
            "not_gonna_work", {"fields": [{"name": "f", "type": "STRING"}]}
        )


def test_table_delete_notfound_ok(mock_bigquery_client):
    connector = gbq._Table("my-project", "my_dataset")
    connector.client = mock_bigquery_client
    mock_bigquery_client.delete_table.side_effect = google.api_core.exceptions.NotFound(
        "nope"
    )
    connector.delete("not_exists")
    mock_bigquery_client.delete_table.assert_called_once()


def test_table_delete_translates_exception(mock_bigquery_client):
    connector = gbq._Table("my-project", "my_dataset")
    connector.client = mock_bigquery_client
    mock_bigquery_client.delete_table.side_effect = (
        google.api_core.exceptions.InternalServerError("something went wrong")
    )
    with pytest.raises(gbq.GenericGBQException):
        connector.delete("not_gonna_work")


def test_table_exists_false(mock_bigquery_client):
    connector = gbq._Table("my-project", "my_dataset")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "nope"
    )
    assert not connector.exists("not_exists")


def test_table_exists_true(mock_bigquery_client):
    connector = gbq._Table("my-project", "my_dataset")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_table.return_value = object()
    assert connector.exists("yes_exists")


def test_table_exists_translates_exception(mock_bigquery_client):
    connector = gbq._Table("my-project", "my_dataset")
    connector.client = mock_bigquery_client
    mock_bigquery_client.get_table.side_effect = (
        google.api_core.exceptions.InternalServerError("something went wrong")
    )
    with pytest.raises(gbq.GenericGBQException):
        connector.exists("not_gonna_work")


def test_read_gbq_with_no_project_id_given_should_fail(monkeypatch):
    import pydata_google_auth

    monkeypatch.setattr(pydata_google_auth, "default", mock_get_credentials_no_project)

    with pytest.raises(ValueError, match="Could not determine project ID"):
        gbq.read_gbq("SELECT 1", dialect="standard")


def test_read_gbq_with_inferred_project_id_with_query(
    monkeypatch, mock_bigquery_client, mock_query_job
):
    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_MINIMUM_VERSION),
    )
    type(mock_query_job).cache_hit = mock.PropertyMock(return_value=False)
    type(mock_query_job).total_bytes_billed = mock.PropertyMock(return_value=10_000_000)
    type(mock_query_job).total_bytes_processed = mock.PropertyMock(return_value=12345)

    df = gbq.read_gbq("SELECT 1", dialect="standard")
    assert df is not None
    mock_bigquery_client.query.assert_called_once()


def test_read_gbq_with_inferred_project_id_with_query_and_wait(
    monkeypatch, mock_bigquery_client
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_QUERY_AND_WAIT_VERSION),
    )

    df = gbq.read_gbq("SELECT 1", dialect="standard")
    assert df is not None
    mock_bigquery_client.query_and_wait.assert_called_once()


def test_read_gbq_with_inferred_project_id_from_service_account_credentials_with_query(
    monkeypatch, mock_bigquery_client, mock_service_account_credentials
):
    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_MINIMUM_VERSION),
    )

    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "SELECT 1",
        dialect="standard",
        credentials=mock_service_account_credentials,
    )
    assert df is not None
    mock_bigquery_client.query.assert_called_once_with(
        "SELECT 1",
        job_config=mock.ANY,
        location=None,
        project="service_account_project_id",
    )


def test_read_gbq_with_inferred_project_id_from_service_account_credentials_with_query_and_wait(
    monkeypatch, mock_bigquery_client, mock_service_account_credentials
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_QUERY_AND_WAIT_VERSION),
    )

    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "SELECT 1",
        dialect="standard",
        credentials=mock_service_account_credentials,
    )
    assert df is not None
    mock_bigquery_client.query_and_wait.assert_called_once_with(
        "SELECT 1",
        job_config=mock.ANY,
        location=None,
        project="service_account_project_id",
        max_results=None,
        wait_timeout=None,
    )


def test_read_gbq_without_inferred_project_id_from_compute_engine_credentials(
    mock_compute_engine_credentials,
):
    with pytest.raises(ValueError, match="Could not determine project ID"):
        gbq.read_gbq(
            "SELECT 1",
            dialect="standard",
            credentials=mock_compute_engine_credentials,
        )


def test_read_gbq_with_max_results_zero(monkeypatch):
    df = gbq.read_gbq("SELECT 1", dialect="standard", max_results=0)
    assert df is None


def test_read_gbq_with_max_results_ten_query(monkeypatch, mock_query_job):
    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_MINIMUM_VERSION),
    )
    df = gbq.read_gbq("SELECT 1", dialect="standard", max_results=10)
    assert df is not None
    mock_query_job.result.assert_called_with(max_results=10)


def test_read_gbq_with_max_results_ten_query_and_wait(
    monkeypatch, mock_bigquery_client
):
    if not hasattr(mock_bigquery_client, "query_and_wait"):
        pytest.skip(
            f"google-cloud-bigquery {google.cloud.bigquery.__version__} does not have query_and_wait"
        )

    monkeypatch.setattr(
        pandas_gbq.features.FEATURES,
        "_bigquery_installed_version",
        packaging.version.parse(pandas_gbq.features.BIGQUERY_QUERY_AND_WAIT_VERSION),
    )
    df = gbq.read_gbq("SELECT 1", dialect="standard", max_results=10)
    assert df is not None
    mock_bigquery_client.query_and_wait.assert_called_with(
        "SELECT 1",
        job_config=mock.ANY,
        location=mock.ANY,
        project=mock.ANY,
        max_results=10,
        wait_timeout=None,
    )


@pytest.mark.parametrize(["verbose"], [(True,), (False,)])
def test_read_gbq_with_verbose_new_pandas_warns_deprecation(monkeypatch, verbose):
    monkeypatch.setattr(
        type(FEATURES),
        "pandas_has_deprecated_verbose",
        mock.PropertyMock(return_value=True),
    )
    with pytest.warns(FutureWarning, match="verbose is deprecated"):
        gbq.read_gbq("SELECT 1", project_id="my-project", verbose=verbose)


def test_read_gbq_wo_verbose_w_new_pandas_no_warnings(monkeypatch, recwarn):
    monkeypatch.setattr(
        type(FEATURES),
        "pandas_has_deprecated_verbose",
        mock.PropertyMock(return_value=False),
    )
    gbq.read_gbq("SELECT 1", project_id="my-project", dialect="standard")
    # This test was intended to check for warnings about the deprecation of
    # the argument `verbose` (which was removed from gbq (~v0.4.0) and
    # pandas (~v0.23.0). (See https://github.com/googleapis/python-bigquery-pandas/pull/158/files)
    # This test should not fail upon seeing a warning in regards to a pending
    # deprecation related to rfc9110 delimiters.
    # TODO this and related tests have likely outlived their usefulness,
    # consider removing.
    for warning in recwarn.list:
        assert "delimiter" in str(warning.message)


def test_read_gbq_with_old_bq_raises_importerror(monkeypatch):
    monkeypatch.setattr(google.cloud.bigquery, "__version__", "0.27.0")
    monkeypatch.setattr(FEATURES, "_bigquery_installed_version", None)
    with pytest.raises(ImportError, match="google-cloud-bigquery"):
        gbq.read_gbq(
            "SELECT 1",
            project_id="my-project",
        )


def test_read_gbq_with_verbose_old_pandas_no_warnings(monkeypatch, recwarn):
    monkeypatch.setattr(
        type(FEATURES),
        "pandas_has_deprecated_verbose",
        mock.PropertyMock(return_value=False),
    )
    gbq.read_gbq(
        "SELECT 1",
        project_id="my-project",
        dialect="standard",
        verbose=True,
    )
    # This test was intended to check for warnings about the deprecation of
    # the argument `verbose` (which was removed from gbq (~v0.4.0) and
    # pandas (~v0.23.0). (See https://github.com/googleapis/python-bigquery-pandas/pull/158/files)
    # This test should not fail upon seeing a warning in regards to a pending
    # deprecation related to rfc9110 delimiters.
    # TODO this and related tests have likely outlived their usefulness,
    # consider removing.
    for warning in recwarn.list:
        assert "delimiter" in str(warning.message)


def test_read_gbq_with_private_raises_notimplmentederror():
    with pytest.raises(NotImplementedError, match="private_key"):
        gbq.read_gbq(
            "SELECT 1", project_id="my-project", private_key="path/to/key.json"
        )


def test_read_gbq_with_invalid_dialect():
    with pytest.raises(ValueError, match="is not valid for dialect"):
        gbq.read_gbq("SELECT 1", dialect="invalid")


def test_read_gbq_with_configuration_query():
    df = gbq.read_gbq(None, configuration={"query": {"query": "SELECT 2"}})
    assert df is not None


def test_read_gbq_with_configuration_duplicate_query_raises_error():
    with pytest.raises(
        ValueError, match="Query statement can't be specified inside config"
    ):
        gbq.read_gbq("SELECT 1", configuration={"query": {"query": "SELECT 2"}})


def test_generate_bq_schema_deprecated():
    # 11121 Deprecation of generate_bq_schema
    with pytest.warns(FutureWarning):
        df = DataFrame([[1, "two"], [3, "four"]])
        gbq.generate_bq_schema(df)


def test_load_does_not_modify_schema_arg(mock_bigquery_client):
    """Test of Issue # 277."""
    from google.api_core.exceptions import NotFound

    # Create table with new schema.
    mock_bigquery_client.get_table.side_effect = NotFound("nope")
    df = DataFrame(
        {
            "field1": ["a", "b"],
            "field2": [1, 2],
            "field3": [datetime.date(2019, 1, 1), datetime.date(2019, 5, 1)],
        }
    )
    original_schema = [
        {"name": "field1", "type": "STRING", "mode": "REQUIRED"},
        {"name": "field2", "type": "INTEGER"},
        {"name": "field3", "type": "DATE"},
    ]
    original_schema_cp = copy.deepcopy(original_schema)
    gbq.to_gbq(
        df,
        "dataset.schematest",
        project_id="my-project",
        table_schema=original_schema,
        if_exists="fail",
    )
    assert original_schema == original_schema_cp

    # Test again now that table exists - behavior will differ internally
    # branch at if table.exists(table_id)
    original_schema = [
        {"name": "field1", "type": "STRING", "mode": "REQUIRED"},
        {"name": "field2", "type": "INTEGER"},
        {"name": "field3", "type": "DATE"},
    ]
    original_schema_cp = copy.deepcopy(original_schema)
    gbq.to_gbq(
        df,
        "dataset.schematest",
        project_id="my-project",
        table_schema=original_schema,
        if_exists="append",
    )
    assert original_schema == original_schema_cp


def test_load_modifies_schema(mock_bigquery_client):
    """Test of https://github.com/googleapis/python-bigquery-pandas/issues/670"""
    from google.api_core.exceptions import NotFound

    # Create table with new schema.
    mock_bigquery_client.get_table.side_effect = NotFound("nope")
    df = DataFrame(
        {
            "field1": ["a", "b"],
            "field2": [1, 2],
            "field3": [datetime.date(2019, 1, 1), datetime.date(2019, 5, 1)],
        }
    )
    original_schema = [
        {"name": "field1", "type": "STRING", "mode": "REQUIRED"},
        {"name": "field2", "type": "INTEGER"},
        {"name": "field3", "type": "DATE"},
    ]
    original_schema_cp = copy.deepcopy(original_schema)
    gbq.to_gbq(
        df,
        "dataset.schematest",
        project_id="my-project",
        table_schema=original_schema,
        if_exists="fail",
    )
    assert original_schema == original_schema_cp

    # Test that when if_exists == "replace", the new table schema updates
    # according to the local schema.
    new_df = DataFrame(
        {
            "field1": ["a", "b"],
            "field2": ["c", "d"],
            "field3": [datetime.date(2019, 1, 1), datetime.date(2019, 5, 1)],
        }
    )
    new_schema = [
        {"name": "field1", "type": "STRING", "mode": "REQUIRED"},
        {"name": "field2", "type": "STRING"},
        {"name": "field3", "type": "DATE"},
    ]
    new_schema_cp = copy.deepcopy(new_schema)
    gbq.to_gbq(
        new_df,
        "dataset.schematest",
        project_id="my-project",
        table_schema=new_schema,
        if_exists="replace",
    )
    assert new_schema == new_schema_cp


def test_read_gbq_passes_dtypes(mock_service_account_credentials, mock_row_iterator):
    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "SELECT 1 AS int_col",
        dialect="standard",
        credentials=mock_service_account_credentials,
        dtypes={"int_col": "my-custom-dtype"},
    )
    assert df is not None

    _, to_dataframe_kwargs = mock_row_iterator.to_dataframe.call_args
    assert to_dataframe_kwargs["dtypes"] == {"int_col": "my-custom-dtype"}


def test_read_gbq_use_bqstorage_api(
    mock_service_account_credentials,
    mock_row_iterator,
):
    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "SELECT 1 AS int_col",
        dialect="standard",
        credentials=mock_service_account_credentials,
        use_bqstorage_api=True,
    )
    assert df is not None

    mock_row_iterator.to_dataframe.assert_called_once_with(
        create_bqstorage_client=True,
        dtypes=mock.ANY,
        progress_bar_type=mock.ANY,
    )


def test_read_gbq_calls_tqdm(mock_service_account_credentials, mock_row_iterator):
    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "SELECT 1",
        dialect="standard",
        credentials=mock_service_account_credentials,
        progress_bar_type="foobar",
    )
    assert df is not None

    _, to_dataframe_kwargs = mock_row_iterator.to_dataframe.call_args
    assert to_dataframe_kwargs["progress_bar_type"] == "foobar"


def test_read_gbq_with_full_table_id(
    mock_bigquery_client, mock_service_account_credentials
):
    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "my-project.my_dataset.read_gbq_table",
        credentials=mock_service_account_credentials,
        project_id="param-project",
    )
    assert df is not None

    mock_bigquery_client.query.assert_not_called()
    sent_table = mock_bigquery_client.list_rows.call_args[0][0]
    assert sent_table.project == "my-project"
    assert sent_table.dataset_id == "my_dataset"
    assert sent_table.table_id == "read_gbq_table"


def test_read_gbq_with_partial_table_id(
    mock_bigquery_client, mock_service_account_credentials
):
    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "my_dataset.read_gbq_table",
        credentials=mock_service_account_credentials,
        project_id="param-project",
    )
    assert df is not None

    mock_bigquery_client.query.assert_not_called()
    sent_table = mock_bigquery_client.list_rows.call_args[0][0]
    assert sent_table.project == "param-project"
    assert sent_table.dataset_id == "my_dataset"
    assert sent_table.table_id == "read_gbq_table"


def test_read_gbq_bypasses_query_with_table_id_and_max_results(
    mock_bigquery_client, mock_service_account_credentials
):
    mock_service_account_credentials.project_id = "service_account_project_id"
    df = gbq.read_gbq(
        "my-project.my_dataset.read_gbq_table",
        credentials=mock_service_account_credentials,
        max_results=11,
    )
    assert df is not None

    mock_bigquery_client.query.assert_not_called()
    sent_table = mock_bigquery_client.list_rows.call_args[0][0]
    assert sent_table.project == "my-project"
    assert sent_table.dataset_id == "my_dataset"
    assert sent_table.table_id == "read_gbq_table"
    sent_max_results = mock_bigquery_client.list_rows.call_args[1]["max_results"]
    assert sent_max_results == 11


def test_read_gbq_with_list_rows_error_translates_exception(
    mock_bigquery_client, mock_service_account_credentials
):
    mock_bigquery_client.list_rows.side_effect = (
        google.api_core.exceptions.NotFound("table not found"),
    )

    with pytest.raises(gbq.GenericGBQException, match="table not found"):
        gbq.read_gbq(
            "my-project.my_dataset.read_gbq_table",
            credentials=mock_service_account_credentials,
        )


def test_run_query_with_dml_query(mock_bigquery_client, mock_query_job):
    """
    Don't attempt to download results from a DML query / query with no results.

    https://github.com/googleapis/python-bigquery-pandas/issues/481
    """
    connector = _make_connector()
    type(mock_query_job).destination = mock.PropertyMock(return_value=None)
    connector.run_query("UPDATE tablename SET value = '';")
    mock_bigquery_client.list_rows.assert_not_called()


def test_read_gbq_with_dry_run(mock_bigquery_client, mock_query_job):
    total_bytes_processed = 15
    type(mock_query_job)._properties = mock.PropertyMock(
        return_value={
            "statistics": {
                "creationTime": 1767037135155.0,
                "startTime": 1767037135238.0,
                "endTime": 1767037135353.0,
                "totalBytesProcessed": f"{total_bytes_processed}",
                "query": {
                    "totalBytesProcessed": f"{total_bytes_processed}",
                    "totalBytesBilled": "0",
                    "cacheHit": True,
                    "statementType": "SELECT",
                },
                "reservation_id": "reservation_id",
                "edition": "ENTERPRISE",
                "reservationGroupPath": [""],
            },
        }
    )

    dry_run_result = gbq.read_gbq("SELECT 1", project_id="my-project", dry_run=True)

    # Check which method was called based on BigQuery version
    if (
        hasattr(mock_bigquery_client, "query_and_wait")
        and mock_bigquery_client.query_and_wait.called
    ):
        _, kwargs = mock_bigquery_client.query_and_wait.call_args
        job_config = kwargs["job_config"]
    else:
        _, kwargs = mock_bigquery_client.query.call_args
        job_config = kwargs["job_config"]
    assert job_config.dry_run is True
    assert dry_run_result["totalBytesProcessed"] == total_bytes_processed
