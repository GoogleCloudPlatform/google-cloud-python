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
from google.api_core import exceptions

from google.cloud import bigtable_admin

from ...utils import create_table_cm
from .tableadmin_async import (
    create_backup,
    delete_table,
    restore_table,
    run_table_operations,
    wait_for_consistency,
)

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"table-admin-async-{str(uuid.uuid4())[:16]}"


@pytest.mark.asyncio
async def test_run_table_operations(capsys):
    await run_table_operations(PROJECT, BIGTABLE_INSTANCE, TABLE_ID)
    out, _ = capsys.readouterr()
    assert "Listing tables in current project..." in out
    assert "Created column family cf1 with MaxAge GC Rule." in out
    assert "Created column family cf2 with Max Versions GC Rule." in out
    assert "Created column family cf3 with Union GC rule" in out
    assert "Created column family cf4 with Intersection GC rule." in out
    assert "Created column family cf5 with a Nested GC rule." in out
    assert "Printing Column Family and GC Rule for all column families..." in out
    assert "Updated column family cf1 GC rule" in out
    assert "Column family cf2 deleted successfully." in out


@pytest.mark.asyncio
async def test_delete_table(capsys):
    table_id = f"table-admin-async-to-delete-{str(uuid.uuid4())[:16]}"
    with create_table_cm(PROJECT, BIGTABLE_INSTANCE, table_id, verbose=False):
        await delete_table(PROJECT, BIGTABLE_INSTANCE, table_id)
    out, _ = capsys.readouterr()
    assert f"Deleting {table_id} table." in out
    assert f"Deleted {table_id} table." in out


@pytest.mark.asyncio
async def test_wait_for_consistency(capsys):
    table_id = f"table-admin-async-consistency-{str(uuid.uuid4())[:16]}"
    with create_table_cm(PROJECT, BIGTABLE_INSTANCE, table_id, verbose=False):
        await wait_for_consistency(PROJECT, BIGTABLE_INSTANCE, table_id)
    out, _ = capsys.readouterr()
    assert f"Waiting for {table_id} to be consistent..." in out
    assert f"Table {table_id} is consistent." in out


@pytest.mark.asyncio
async def test_backup_and_restore(capsys):
    table_id = f"table-admin-async-backup-{str(uuid.uuid4())[:16]}"
    backup_id = f"backup-async-{str(uuid.uuid4())[:16]}"
    restored_table_id = f"table-admin-async-restored-{str(uuid.uuid4())[:16]}"

    instance_client = bigtable_admin.BigtableInstanceAdminClient()
    instance_path = instance_client.instance_path(PROJECT, BIGTABLE_INSTANCE)
    cluster_id = (
        instance_client.list_clusters(parent=instance_path)
        .clusters[0]
        .name.split("/")[-1]
    )

    table_client = bigtable_admin.BigtableTableAdminClient()
    backup_path = table_client.backup_path(
        PROJECT, BIGTABLE_INSTANCE, cluster_id, backup_id
    )
    restored_table_path = table_client.table_path(
        PROJECT, BIGTABLE_INSTANCE, restored_table_id
    )
    try:
        with create_table_cm(PROJECT, BIGTABLE_INSTANCE, table_id, verbose=False):
            await create_backup(
                PROJECT, BIGTABLE_INSTANCE, cluster_id, table_id, backup_id
            )
            await restore_table(
                PROJECT, BIGTABLE_INSTANCE, cluster_id, backup_id, restored_table_id
            )
        assert table_client.get_table(name=restored_table_path) is not None
    finally:
        for name, delete in (
            (restored_table_path, table_client.delete_table),
            (backup_path, table_client.delete_backup),
        ):
            try:
                delete(name=name)
            except exceptions.NotFound:
                pass

    out, _ = capsys.readouterr()
    assert f"Created backup {backup_id}." in out
    assert f"Restored table {restored_table_id}." in out
