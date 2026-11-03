#!/usr/bin/env python

# Copyright 2018, Google LLC
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

from google.api_core import exceptions
from test_utils.retry import RetryErrors

from ...utils import create_table_cm
from .tableadmin import delete_table, run_table_operations

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"tableadmin-test-{str(uuid.uuid4())[:16]}"

retry_429_503 = RetryErrors(exceptions.TooManyRequests, exceptions.ServiceUnavailable)


def test_run_table_operations(capsys):
    retry_429_503(run_table_operations)(PROJECT, BIGTABLE_INSTANCE, TABLE_ID)
    out, _ = capsys.readouterr()

    assert "Listing tables in current project." in out
    assert "Creating column family cf1 with with MaxAge GC Rule" in out
    assert "Created column family cf1 with MaxAge GC Rule." in out
    assert "Created column family cf2 with Max Versions GC Rule." in out
    assert "Created column family cf3 with Union GC rule" in out
    assert "Created column family cf4 with Intersection GC rule." in out
    assert "Created column family cf5 with a Nested GC rule." in out
    assert "Printing Column Family and GC Rule for all column families." in out
    assert "Updating column family cf1 GC rule..." in out
    assert "Updated column family cf1 GC rule" in out
    assert "Print column family cf1 GC rule after update..." in out
    assert "Column Family: cf1" in out
    assert "max_num_versions: 1" in out
    assert "Delete a column family cf2..." in out
    assert "Column family cf2 deleted successfully." in out


def test_delete_table(capsys):
    table_id = f"table-admin-to-delete-{str(uuid.uuid4())[:16]}"
    with create_table_cm(PROJECT, BIGTABLE_INSTANCE, table_id, verbose=False):
        delete_table(PROJECT, BIGTABLE_INSTANCE, table_id)
    out, _ = capsys.readouterr()

    assert "Table " + table_id + " exists." in out
    assert "Deleting " + table_id + " table." in out
    assert "Deleted " + table_id + " table." in out
