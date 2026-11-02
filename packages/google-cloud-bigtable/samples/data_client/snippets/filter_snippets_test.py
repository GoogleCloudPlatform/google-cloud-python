# Copyright 2026 Google LLC
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
import uuid
from typing import Generator

import pytest
from google.cloud._helpers import _microseconds_from_datetime

from ...utils import create_table_cm
from . import filter_snippets
from .snapshots.snap_filters_test import snapshots

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"mobile-time-series-filters-{str(uuid.uuid4())[:16]}"


@pytest.fixture(scope="module", autouse=True)
def table_id() -> Generator[str, None, None]:
    with create_table_cm(
        PROJECT, BIGTABLE_INSTANCE, TABLE_ID, {"stats_summary": None, "cell_plan": None}
    ):
        _populate_table(TABLE_ID)
        yield TABLE_ID


def _populate_table(table_id):
    from google.cloud.bigtable.data import (
        BigtableDataClient,
        RowMutationEntry,
        SetCell,
    )

    timestamp = datetime.datetime(2019, 5, 1)
    timestamp_minus_hr = timestamp - datetime.timedelta(hours=1)

    with BigtableDataClient(project=PROJECT) as client:
        with client.get_table(BIGTABLE_INSTANCE, table_id) as table:
            with table.mutations_batcher() as batcher:
                batcher.append(
                    RowMutationEntry(
                        "phone#4c410523#20190501",
                        [
                            SetCell(
                                "stats_summary",
                                "connected_cell",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "connected_cell",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "connected_wifi",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "os_build",
                                "PQ2A.190405.003",
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "cell_plan",
                                "data_plan_01gb",
                                "true",
                                _microseconds_from_datetime(timestamp_minus_hr),
                            ),
                            SetCell(
                                "cell_plan",
                                "data_plan_01gb",
                                "false",
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "cell_plan",
                                "data_plan_05gb",
                                "true",
                                _microseconds_from_datetime(timestamp),
                            ),
                        ],
                    )
                )
                batcher.append(
                    RowMutationEntry(
                        "phone#4c410523#20190502",
                        [
                            SetCell(
                                "stats_summary",
                                "connected_cell",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "connected_wifi",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "os_build",
                                "PQ2A.190405.004",
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "cell_plan",
                                "data_plan_05gb",
                                "true",
                                _microseconds_from_datetime(timestamp),
                            ),
                        ],
                    )
                )
                batcher.append(
                    RowMutationEntry(
                        "phone#4c410523#20190505",
                        [
                            SetCell(
                                "stats_summary",
                                "connected_cell",
                                0,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "connected_wifi",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "os_build",
                                "PQ2A.190406.000",
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "cell_plan",
                                "data_plan_05gb",
                                "true",
                                _microseconds_from_datetime(timestamp),
                            ),
                        ],
                    )
                )
                batcher.append(
                    RowMutationEntry(
                        "phone#5c10102#20190501",
                        [
                            SetCell(
                                "stats_summary",
                                "connected_cell",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "connected_wifi",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "os_build",
                                "PQ2A.190401.002",
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "cell_plan",
                                "data_plan_10gb",
                                "true",
                                _microseconds_from_datetime(timestamp),
                            ),
                        ],
                    )
                )
                batcher.append(
                    RowMutationEntry(
                        "phone#5c10102#20190502",
                        [
                            SetCell(
                                "stats_summary",
                                "connected_cell",
                                1,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "connected_wifi",
                                0,
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "stats_summary",
                                "os_build",
                                "PQ2A.190406.000",
                                _microseconds_from_datetime(timestamp),
                            ),
                            SetCell(
                                "cell_plan",
                                "data_plan_10gb",
                                "true",
                                _microseconds_from_datetime(timestamp),
                            ),
                        ],
                    )
                )


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
