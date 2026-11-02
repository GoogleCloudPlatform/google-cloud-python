# Copyright (c) 2021 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


import os
import pathlib
import tempfile
import unittest.mock as mock

import google.api_core.exceptions
import google.cloud.bigquery
import pandas as pd
import pytest
from pandas import DataFrame

from pandas_gbq import gbq

Path = pathlib.Path


class FakeDataFrame:
    """A fake bigframes DataFrame to avoid depending on bigframes."""

    def to_gbq(self):
        """Fake to_gbq() to mimic a bigframes object."""

    def to_pandas(self):
        """Fake to_pandas() to mimic a bigframes object."""


@pytest.fixture
def expected_load_method(mock_bigquery_client):
    return mock_bigquery_client.load_table_from_dataframe


def test_to_gbq_create_dataset_with_location(mock_bigquery_client):
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    mock_bigquery_client.get_dataset.side_effect = google.api_core.exceptions.NotFound(
        "my_dataset"
    )
    gbq.to_gbq(
        DataFrame([[1]]), "my_dataset.my_table", project_id="1234", location="us-west1"
    )
    assert mock_bigquery_client.create_dataset.called
    args, _ = mock_bigquery_client.create_dataset.call_args
    sent_dataset = args[0]
    assert sent_dataset.location == "us-west1"


def test_to_gbq_create_dataset_translates_exception(mock_bigquery_client):
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    mock_bigquery_client.get_dataset.side_effect = google.api_core.exceptions.NotFound(
        "my_dataset"
    )
    mock_bigquery_client.create_dataset.side_effect = (
        google.api_core.exceptions.InternalServerError("something went wrong")
    )

    with pytest.raises(gbq.GenericGBQException):
        gbq.to_gbq(DataFrame([[1]]), "my_dataset.my_table", project_id="1234")


def test_to_gbq_load_method_translates_exception(
    mock_bigquery_client, expected_load_method
):
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    expected_load_method.side_effect = google.api_core.exceptions.InternalServerError(
        "error loading data"
    )

    with pytest.raises(gbq.GenericGBQException):
        gbq.to_gbq(
            DataFrame({"int_cole": [1, 2, 3]}),
            "my_dataset.my_table",
            project_id="myproj",
        )
    expected_load_method.assert_called_once()


def test_to_gbq_with_bigframes_raises_typeerror():
    dataframe = FakeDataFrame()

    with pytest.raises(
        TypeError, match=r"Expected a pandas.DataFrame, but got .+FakeDataFrame"
    ):
        gbq.to_gbq(dataframe, "my_dataset.my_table", project_id="myproj")


def test_to_gbq_with_if_exists_append(mock_bigquery_client, expected_load_method):
    from google.cloud.bigquery import SchemaField

    mock_bigquery_client.get_table.return_value = google.cloud.bigquery.Table(
        "myproj.my_dataset.my_table",
        schema=(
            SchemaField("col_a", "FLOAT", mode="REQUIRED"),
            SchemaField("col_b", "STRING", mode="REQUIRED"),
        ),
    )
    gbq.to_gbq(
        DataFrame({"col_a": [0.25, 1.5, -1.0], "col_b": ["a", "b", "c"]}),
        "my_dataset.my_table",
        project_id="myproj",
        if_exists="append",
    )
    expected_load_method.assert_called_once()


def test_to_gbq_with_if_exists_append_mismatch(mock_bigquery_client):
    from google.cloud.bigquery import SchemaField

    mock_bigquery_client.get_table.return_value = google.cloud.bigquery.Table(
        "myproj.my_dataset.my_table",
        schema=(SchemaField("col_a", "INTEGER"), SchemaField("col_b", "STRING")),
    )
    mock_bigquery_client.side_effect = gbq.InvalidSchema(
        message=r"Provided Schema does not match Table *"
    )

    with pytest.raises((gbq.InvalidSchema)) as exception_block:
        gbq.to_gbq(
            DataFrame({"col_a": [0.25, 1.5, -1.0]}),
            "my_dataset.my_table",
            project_id="myproj",
            if_exists="append",
        )

    exc = exception_block.value
    assert exc.message == r"Provided Schema does not match Table *"


def test_to_gbq_with_if_exists_replace(mock_bigquery_client, expected_load_method):
    mock_bigquery_client.get_table.side_effect = (
        # Initial check
        google.cloud.bigquery.Table("myproj.my_dataset.my_table"),
        # Recreate check
        google.api_core.exceptions.NotFound("my_table"),
    )
    gbq.to_gbq(
        DataFrame([[1]]),
        "my_dataset.my_table",
        project_id="myproj",
        if_exists="replace",
    )
    expected_load_method.assert_called_once()


def test_to_gbq_with_if_exists_replace_cross_project(
    mock_bigquery_client, expected_load_method
):
    mock_bigquery_client.get_table.side_effect = (
        # Initial check
        google.cloud.bigquery.Table("data-project.my_dataset.my_table"),
        # Recreate check
        google.api_core.exceptions.NotFound("my_table"),
    )
    gbq.to_gbq(
        DataFrame([[1]]),
        "data-project.my_dataset.my_table",
        project_id="billing-project",
        if_exists="replace",
    )
    expected_load_method.assert_called_once()

    # Check that billing project and destination table is set correctly.
    expected_load_method.assert_called_once()
    load_args, load_kwargs = expected_load_method.call_args
    table_destination = load_args[1]
    assert table_destination.project == "data-project"
    assert table_destination.dataset_id == "my_dataset"
    assert table_destination.table_id == "my_table"
    assert load_kwargs["project"] == "billing-project"


def test_to_gbq_with_if_exists_unknown():
    with pytest.raises(ValueError):
        gbq.to_gbq(
            DataFrame([[1]]),
            "my_dataset.my_table",
            project_id="myproj",
            if_exists="unknown",
        )


@mock.patch.dict(os.environ, {}, clear=True)
@pytest.mark.parametrize(
    "user_agent,rfc9110_delimiter,expected",
    [
        (
            "test_user_agent/2.0.42",
            False,
            f"test_user_agent/2.0.42 pandas-{pd.__version__}",
        ),
        (None, False, f"pandas-{pd.__version__}"),
        (
            "test_user_agent/2.0.42",
            True,
            f"test_user_agent/2.0.42 pandas/{pd.__version__}",
        ),
        (None, True, f"pandas/{pd.__version__}"),
    ],
)
def test_create_user_agent(user_agent, rfc9110_delimiter, expected):
    from pandas_gbq.gbq_connector import create_user_agent

    result = create_user_agent(user_agent, rfc9110_delimiter)
    assert result == expected


@mock.patch.dict(os.environ, {"VSCODE_PID": "1234"}, clear=True)
def test_create_user_agent_vscode():
    from pandas_gbq.gbq_connector import create_user_agent

    result = create_user_agent()
    assert f"pandas-{pd.__version__} vscode" in result


@mock.patch.dict(os.environ, {"VSCODE_PID": "1234"}, clear=True)
def test_create_user_agent_vscode_plugin():
    from pandas_gbq.gbq_connector import create_user_agent

    with tempfile.TemporaryDirectory() as tmpdir:
        user_home = Path(tmpdir)
        plugin_dir = (
            user_home / ".vscode" / "extensions" / "googlecloudtools.cloudcode-0.12"
        )
        plugin_config = plugin_dir / "package.json"

        # originally pluging config does not exist
        assert not plugin_config.exists()

        # simulate plugin installation by creating plugin config on disk
        plugin_dir.mkdir(parents=True)
        with open(plugin_config, "w") as f:
            f.write("{}")

        with mock.patch("pathlib.Path.home", return_value=user_home):
            result = create_user_agent()
            assert (
                f"pandas-{pd.__version__} vscode googlecloudtools.cloudcode" in result
            )


@mock.patch.dict(os.environ, {"JPY_PARENT_PID": "1234"}, clear=True)
def test_create_user_agent_jupyter():
    from pandas_gbq.gbq_connector import create_user_agent

    assert create_user_agent() == f"pandas-{pd.__version__} jupyter"


@mock.patch.dict(os.environ, {"JPY_PARENT_PID": "1234"}, clear=True)
def test_create_user_agent_jupyter_extension():
    from pandas_gbq.gbq_connector import create_user_agent

    def custom_import_module_side_effect(name, package=None):
        if name == "bigquery_jupyter_plugin":
            return mock.MagicMock()
        else:
            import importlib

            return importlib.import_module(name, package)

    with mock.patch(
        "importlib.import_module", side_effect=custom_import_module_side_effect
    ):
        assert (
            create_user_agent()
            == f"pandas-{pd.__version__} jupyter bigquery_jupyter_plugin"
        )


def test_to_gbq_with_clustering(mock_bigquery_client):
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    gbq.to_gbq(
        DataFrame([[1]]),
        "my_dataset.my_table",
        project_id="1234",
        clustering_columns=["col_a", "col_b"],
    )
    mock_bigquery_client.create_table.assert_called_with(mock.ANY)
    table = mock_bigquery_client.create_table.call_args[0][0]
    assert table.clustering_fields == ["col_a", "col_b"]


def test_to_gbq_with_time_partitioning(mock_bigquery_client):
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    gbq.to_gbq(
        DataFrame([[1]]),
        "my_dataset.my_table",
        project_id="1234",
        time_partitioning_column="time_col",
        time_partitioning_type="DAY",
        time_partitioning_expiration_ms=100,
    )
    mock_bigquery_client.create_table.assert_called_with(mock.ANY)
    table = mock_bigquery_client.create_table.call_args[0][0]
    assert table.time_partitioning.type_ == "DAY"
    assert table.time_partitioning.field == "time_col"
    assert table.time_partitioning.expiration_ms == 100


def test_to_gbq_with_range_partitioning(mock_bigquery_client):
    mock_bigquery_client.get_table.side_effect = google.api_core.exceptions.NotFound(
        "my_table"
    )
    gbq.to_gbq(
        DataFrame([[1]]),
        "my_dataset.my_table",
        project_id="1234",
        range_partitioning_column="range_col",
        range_partitioning_range={"start": 0, "end": 100, "interval": 10},
    )
    mock_bigquery_client.create_table.assert_called_with(mock.ANY)
    table = mock_bigquery_client.create_table.call_args[0][0]
    assert table.range_partitioning.field == "range_col"
    assert table.range_partitioning.range_.start == 0
    assert table.range_partitioning.range_.end == 100
    assert table.range_partitioning.range_.interval == 10
