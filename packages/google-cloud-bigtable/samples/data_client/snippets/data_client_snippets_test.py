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

import os
import uuid

import pytest

from ...utils import create_table_cm
from . import data_client_snippets as data_snippets

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"data-client-sync-{str(uuid.uuid4())[:16]}"


@pytest.fixture(scope="session")
def column_family_config():
    from google.cloud.bigtable_admin_v2 import types

    int_aggregate_type = types.Type.Aggregate(
        input_type=types.Type(int64_type={"encoding": {"big_endian_bytes": {}}}),
        sum={},
    )

    return {
        "family": types.ColumnFamily(),
        "stats_summary": types.ColumnFamily(),
        "counters": types.ColumnFamily(
            value_type=types.Type(aggregate_type=int_aggregate_type)
        ),
    }


@pytest.fixture(scope="session")
def table_id(column_family_config):
    with create_table_cm(PROJECT, BIGTABLE_INSTANCE, TABLE_ID, column_family_config):
        yield TABLE_ID


@pytest.fixture
def table(table_id):
    from google.cloud.bigtable.data import BigtableDataClient

    with BigtableDataClient(project=PROJECT) as client:
        with client.get_table(BIGTABLE_INSTANCE, table_id) as table:
            yield table


def test_write_simple(table):
    data_snippets.write_simple(table)


def test_write_batch(table):
    data_snippets.write_batch(table)


def test_write_increment(table):
    data_snippets.write_increment(table)


def test_write_conditional(table):
    data_snippets.write_conditional(table)


def test_write_aggregate(table):
    data_snippets.write_aggregate(table)


def test_read_row(table):
    data_snippets.read_row(table)


def test_read_row_partial(table):
    data_snippets.read_row_partial(table)


def test_read_rows_multiple(table):
    data_snippets.read_rows_multiple(table)


def test_read_row_range(table):
    data_snippets.read_row_range(table)


def test_read_row_ranges(table):
    data_snippets.read_row_ranges(table)


def test_read_with_prefix(table):
    data_snippets.read_with_prefix(table)


def test_read_with_filter(table):
    data_snippets.read_with_filter(table)


def test_execute_query(table):
    data_snippets.execute_query(table)
