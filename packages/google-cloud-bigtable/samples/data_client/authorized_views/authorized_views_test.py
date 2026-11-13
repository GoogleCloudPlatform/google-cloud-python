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

from google.api_core.exceptions import NotFound

from google.cloud import bigtable_admin_v2

from . import authorized_views

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"authorized-views-{str(uuid.uuid4())[:16]}"
AUTHORIZED_VIEW_ID = f"view-{str(uuid.uuid4())[:16]}"


def test_run(capsys):
    try:
        authorized_views.run(PROJECT, BIGTABLE_INSTANCE, TABLE_ID, AUTHORIZED_VIEW_ID)
    finally:
        # the sample deletes the table itself; this only matters if it failed midway
        admin_client = bigtable_admin_v2.BigtableTableAdminClient()
        try:
            admin_client.delete_table(
                name=admin_client.table_path(PROJECT, BIGTABLE_INSTANCE, TABLE_ID)
            )
        except NotFound:
            pass

    out, _ = capsys.readouterr()
    assert f"Table does not exist, creating table: {TABLE_ID}" in out
    assert f"authorizedViews/{AUTHORIZED_VIEW_ID} created successfully" in out
    assert f"authorizedViews/{AUTHORIZED_VIEW_ID} updated successfully" in out
    assert "Column Family: cf, Qualifier Prefix: " in out
    assert f"\n{AUTHORIZED_VIEW_ID}\n" in out
    assert "Hello World!" in out
    assert "Row: rowKey0" in out
    assert "Family: cf    Qualifier: greeting    Value: Hello World!" in out
    assert "Row Key: rowKey2" in out
    assert f"AuthorizedView: {AUTHORIZED_VIEW_ID} deleted successfully" in out
    assert f"Table: {TABLE_ID} deleted successfully" in out
