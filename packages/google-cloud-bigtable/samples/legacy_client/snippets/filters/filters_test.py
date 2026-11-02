# Copyright 2020, Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import datetime
import inspect
import os
import time
import uuid

import pytest

from ....utils import create_table_cm
from . import filter_snippets
from .snapshots.snap_filters_test import snapshots

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"mobile-time-series-filters-{str(uuid.uuid4())[:16]}"


@pytest.fixture(scope="module", autouse=True)
def table_id():
    from google.cloud.bigtable.row_set import RowSet

    table_id = TABLE_ID
    with create_table_cm(
        PROJECT, BIGTABLE_INSTANCE, table_id, {"stats_summary": None, "cell_plan": None}
    ) as table:
        timestamp = datetime.datetime(2019, 5, 1)
        timestamp_minus_hr = datetime.datetime(2019, 5, 1) - datetime.timedelta(hours=1)

        row_keys = [
            "phone#4c410523#20190501",
            "phone#4c410523#20190502",
            "phone#4c410523#20190505",
            "phone#5c10102#20190501",
            "phone#5c10102#20190502",
        ]

        rows = [table.direct_row(row_key) for row_key in row_keys]

        rows[0].set_cell("stats_summary", "connected_cell", 1, timestamp)
        rows[0].set_cell("stats_summary", "connected_wifi", 1, timestamp)
        rows[0].set_cell("stats_summary", "os_build", "PQ2A.190405.003", timestamp)
        rows[0].set_cell("cell_plan", "data_plan_01gb", "true", timestamp_minus_hr)
        rows[0].set_cell("cell_plan", "data_plan_01gb", "false", timestamp)
        rows[0].set_cell("cell_plan", "data_plan_05gb", "true", timestamp)
        rows[1].set_cell("stats_summary", "connected_cell", 1, timestamp)
        rows[1].set_cell("stats_summary", "connected_wifi", 1, timestamp)
        rows[1].set_cell("stats_summary", "os_build", "PQ2A.190405.004", timestamp)
        rows[1].set_cell("cell_plan", "data_plan_05gb", "true", timestamp)
        rows[2].set_cell("stats_summary", "connected_cell", 0, timestamp)
        rows[2].set_cell("stats_summary", "connected_wifi", 1, timestamp)
        rows[2].set_cell("stats_summary", "os_build", "PQ2A.190406.000", timestamp)
        rows[2].set_cell("cell_plan", "data_plan_05gb", "true", timestamp)
        rows[3].set_cell("stats_summary", "connected_cell", 1, timestamp)
        rows[3].set_cell("stats_summary", "connected_wifi", 1, timestamp)
        rows[3].set_cell("stats_summary", "os_build", "PQ2A.190401.002", timestamp)
        rows[3].set_cell("cell_plan", "data_plan_10gb", "true", timestamp)
        rows[4].set_cell("stats_summary", "connected_cell", 1, timestamp)
        rows[4].set_cell("stats_summary", "connected_wifi", 0, timestamp)
        rows[4].set_cell("stats_summary", "os_build", "PQ2A.190406.000", timestamp)
        rows[4].set_cell("cell_plan", "data_plan_10gb", "true", timestamp)

        table.mutate_rows(rows)

        # Ensure mutations have propagated.
        row_set = RowSet()

        for row_key in row_keys:
            row_set.add_row_key(row_key)

        fetched = list(table.read_rows(row_set=row_set))

        while len(fetched) < len(rows):
            time.sleep(5)
            fetched = list(table.read_rows(row_set=row_set))

        yield table_id


def test_filter_limit_row_sample(capsys, table_id):
    filter_snippets.filter_limit_row_sample(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    assert "Reading data for" in out


def test_filter_limit_row_regex(capsys, table_id):
    filter_snippets.filter_limit_row_regex(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_cells_per_col(capsys, table_id):
    filter_snippets.filter_limit_cells_per_col(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_cells_per_row(capsys, table_id):
    filter_snippets.filter_limit_cells_per_row(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_cells_per_row_offset(capsys, table_id):
    filter_snippets.filter_limit_cells_per_row_offset(
        PROJECT, BIGTABLE_INSTANCE, table_id
    )

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_col_family_regex(capsys, table_id):
    filter_snippets.filter_limit_col_family_regex(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_col_qualifier_regex(capsys, table_id):
    filter_snippets.filter_limit_col_qualifier_regex(
        PROJECT, BIGTABLE_INSTANCE, table_id
    )

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_col_range(capsys, table_id):
    filter_snippets.filter_limit_col_range(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_value_range(capsys, table_id):
    filter_snippets.filter_limit_value_range(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_value_regex(capsys, table_id):
    filter_snippets.filter_limit_value_regex(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_timestamp_range(capsys, table_id):
    filter_snippets.filter_limit_timestamp_range(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_block_all(capsys, table_id):
    filter_snippets.filter_limit_block_all(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_limit_pass_all(capsys, table_id):
    filter_snippets.filter_limit_pass_all(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_modify_strip_value(capsys, table_id):
    filter_snippets.filter_modify_strip_value(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_modify_apply_label(capsys, table_id):
    filter_snippets.filter_modify_apply_label(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_composing_chain(capsys, table_id):
    filter_snippets.filter_composing_chain(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_composing_interleave(capsys, table_id):
    filter_snippets.filter_composing_interleave(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected


def test_filter_composing_condition(capsys, table_id):
    filter_snippets.filter_composing_condition(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    expected = snapshots[inspect.currentframe().f_code.co_name]
    assert out == expected
