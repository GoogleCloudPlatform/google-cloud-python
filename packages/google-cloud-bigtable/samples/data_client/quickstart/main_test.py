# Copyright 2026 Google LLC
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

import os
import uuid
from typing import Generator

import pytest

from google.cloud.bigtable.data import BigtableDataClient, SetCell

from ...utils import create_table_cm
from .main import main

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"quickstart-test-{str(uuid.uuid4())[:16]}"


@pytest.fixture
def table_id() -> Generator[str, None, None]:
    with create_table_cm(PROJECT, BIGTABLE_INSTANCE, TABLE_ID, {"cf1": None}):
        _populate_table(TABLE_ID)
        yield TABLE_ID


def _populate_table(table_id: str):
    with BigtableDataClient(project=PROJECT) as client:
        with client.get_table(BIGTABLE_INSTANCE, table_id) as table:
            table.mutate_row("r1", SetCell("cf1", "c1", "test-value"))


def test_main(capsys, table_id):
    main(PROJECT, BIGTABLE_INSTANCE, table_id)

    out, _ = capsys.readouterr()
    assert "Row key: r1\nData: test-value\n" in out
