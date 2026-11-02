# Copyright 2021 Google LLC All rights reserved.
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

import pytest

from tests.system.utils import streaming_utils

_RUN_POPULATE_STREAMING = """\
Run 'tests/system/utils/populate_streaming.py' to enable these tests."""


@pytest.fixture(scope="session")
def streaming_instance(spanner_client):
    instance = spanner_client.instance(streaming_utils.INSTANCE_NAME)
    if not instance.exists():
        pytest.skip(_RUN_POPULATE_STREAMING)

    yield instance


@pytest.fixture(scope="session")
def streaming_database(streaming_instance):
    database = streaming_instance.database(streaming_utils.DATABASE_NAME)
    if not database.exists():
        pytest.skip(_RUN_POPULATE_STREAMING)

    yield database


def _verify_one_column(db, table_desc):
    sql = f"SELECT chunk_me FROM {table_desc.table}"
    with db.snapshot() as snapshot:
        rows = list(snapshot.execute_sql(sql))
    assert len(rows) == table_desc.row_count
    expected = table_desc.value()
    for row in rows:
        assert row[0] == expected


def _verify_two_columns(db, table_desc):
    sql = f"SELECT chunk_me, chunk_me_2 FROM {table_desc.table}"
    with db.snapshot() as snapshot:
        rows = list(snapshot.execute_sql(sql))
    assert len(rows) == table_desc.row_count
    expected = table_desc.value()
    for row in rows:
        assert row[0] == expected
        assert row[1] == expected


def test_four_kay(streaming_database):
    _verify_one_column(streaming_database, streaming_utils.FOUR_KAY)


def test_forty_kay(streaming_database):
    _verify_one_column(streaming_database, streaming_utils.FORTY_KAY)


def test_four_hundred_kay(streaming_database):
    _verify_one_column(streaming_database, streaming_utils.FOUR_HUNDRED_KAY)


def test_four_meg(streaming_database):
    _verify_two_columns(streaming_database, streaming_utils.FOUR_MEG)
