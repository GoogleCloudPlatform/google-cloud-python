# Copyright 2025 Google LLC
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
from datetime import datetime, timedelta
from typing import Tuple

import pytest
from google.cloud.environment_vars import BIGTABLE_EMULATOR

from google.cloud import bigtable_admin_v2 as admin_v2
from google.cloud.bigtable.data import mutations, read_rows_query
from google.cloud.bigtable.data._cross_sync import CrossSync

from .conftest import (
    BACKUP_PREFIX,
    DEFAULT_CLUSTER_LOCATIONS,
    INITIAL_CELL_VALUE,
    INSTANCE_PREFIX,
    NEW_CELL_VALUE,
    NUM_ROWS,
    REPLICATION_CLUSTER_LOCATIONS,
    ROW_PREFIX,
    TEST_BACKUP_TABLE_NAME,
    TEST_COLUMMN_FAMILY_NAME,
    TEST_COLUMN_NAME,
    TEST_TABLE_NAME,
    generate_unique_suffix,
)

if CrossSync.is_async:
    from google.api_core import operation_async as api_core_operation
else:
    from google.api_core import operation as api_core_operation


__CROSS_SYNC_OUTPUT__ = "tests.system.admin_overlay.test_system_autogen"

if os.getenv(BIGTABLE_EMULATOR):
    pytest.skip(
        allow_module_level=True,
        reason="Emulator support for admin client tests unsupported.",
    )


@CrossSync.convert
@CrossSync.pytest_fixture(scope="session")
async def data_client(admin_overlay_project_id):
    async with CrossSync.DataClient(project=admin_overlay_project_id) as client:
        yield client


@CrossSync.convert(
    replace_symbols={"BigtableTableAdminAsyncClient": "BigtableTableAdminClient"}
)
@CrossSync.pytest_fixture(scope="session")
async def table_admin_client(admin_overlay_project_id):
    async with admin_v2.BigtableTableAdminAsyncClient(
        client_options={
            "quota_project_id": admin_overlay_project_id,
        }
    ) as client:
        yield client


@CrossSync.convert(
    replace_symbols={"BigtableInstanceAdminAsyncClient": "BigtableInstanceAdminClient"}
)
@CrossSync.pytest_fixture(scope="session")
async def instance_admin_client(admin_overlay_project_id):
    async with admin_v2.BigtableInstanceAdminAsyncClient(
        client_options={
            "quota_project_id": admin_overlay_project_id,
        }
    ) as client:
        yield client


@CrossSync.convert
@CrossSync.pytest_fixture(scope="session", autouse=True)
async def cleanup_old_instances(admin_overlay_project_id):
    """
    Automatically deletes any test instances older than 1 day.

    This fixture runs once per test session and helps prevent resource leakage
    by cleaning up instances that failed to be deleted during previous test runs.
    """
    from tests.system.utils import clear_stale_instances

    from .conftest import INSTANCE_PREFIX

    clear_stale_instances(admin_overlay_project_id, INSTANCE_PREFIX, older_than_days=1)


@CrossSync.convert
@CrossSync.pytest_fixture(scope="function")
async def instances_to_delete(instance_admin_client):
    instances = []

    try:
        yield instances
    finally:
        for instance in reversed(instances):
            try:
                await instance_admin_client.delete_instance(name=instance.name)
            except Exception as e:
                print(f"Failed to delete instance {instance.name}: {e}")


@CrossSync.convert
@CrossSync.pytest_fixture(scope="function")
async def backups_to_delete(table_admin_client):
    backups = []

    try:
        yield backups
    finally:
        for backup in reversed(backups):
            try:
                await table_admin_client.delete_backup(name=backup.name)
            except Exception as e:
                print(f"Failed to delete backup {backup.name}: {e}")


@CrossSync.convert
async def create_instance(
    instance_admin_client,
    table_admin_client,
    data_client,
    project_id,
    instances_to_delete,
    storage_type=admin_v2.StorageType.HDD,
    cluster_locations=DEFAULT_CLUSTER_LOCATIONS,
) -> Tuple[admin_v2.Instance, admin_v2.Table]:
    """
    Creates a new Bigtable instance with the specified project_id, storage type, and cluster locations.

    After creating the Bigtable instance, it will create a test table and populate it with dummy data.
    This is not defined as a fixture because the different system tests need different kinds of instances.
    """
    # Create the instance
    clusters = {}

    instance_id = generate_unique_suffix(INSTANCE_PREFIX)

    for idx, location in enumerate(cluster_locations):
        clusters[location] = admin_v2.Cluster(
            name=instance_admin_client.cluster_path(
                project_id, instance_id, f"{instance_id}-{idx}"
            ),
            location=instance_admin_client.common_location_path(project_id, location),
            default_storage_type=storage_type,
        )

    # Instance and cluster creation are currently unsupported in the Bigtable emulator
    if os.getenv(BIGTABLE_EMULATOR):
        # All we need for system tests so far is the instance name.
        instance = admin_v2.Instance(
            name=instance_admin_client.instance_path(project_id, instance_id),
        )
    else:
        create_instance_request = admin_v2.CreateInstanceRequest(
            parent=instance_admin_client.common_project_path(project_id),
            instance_id=instance_id,
            instance=admin_v2.Instance(
                display_name=instance_id[
                    :30
                ],  # truncate to 30 characters because of character limit
            ),
            clusters=clusters,
        )
        operation = await instance_admin_client.create_instance(create_instance_request)

        # add to cleanup list before waiting for result, in case of timeout
        instance_name = instance_admin_client.instance_path(project_id, instance_id)
        instance_placeholder = admin_v2.Instance(name=instance_name)
        instances_to_delete.append(instance_placeholder)

        instance = await operation.result()

        # replace with full instance object
        instances_to_delete[-1] = instance

    # Create a table within the instance
    create_table_request = admin_v2.CreateTableRequest(
        parent=instance_admin_client.instance_path(project_id, instance_id),
        table_id=TEST_TABLE_NAME,
        table=admin_v2.Table(
            column_families={
                TEST_COLUMMN_FAMILY_NAME: admin_v2.ColumnFamily(),
            }
        ),
    )

    table = await table_admin_client.create_table(create_table_request)

    # Populate with dummy data
    await populate_table(
        table_admin_client, data_client, instance, table, INITIAL_CELL_VALUE
    )

    return instance, table


@CrossSync.convert
async def populate_table(table_admin_client, data_client, instance, table, cell_value):
    """
    Populates all the test cells in the given table with the given cell value.

    This is used to populate test data when creating an instance, and for testing the
    wait_for_consistency call.
    """
    data_client_table = data_client.get_table(
        table_admin_client.parse_instance_path(instance.name)["instance"],
        table_admin_client.parse_table_path(table.name)["table"],
    )
    row_mutation_entries = []
    for i in range(0, NUM_ROWS):
        row_mutation_entries.append(
            mutations.RowMutationEntry(
                row_key=f"{ROW_PREFIX}-{i}",
                mutations=[
                    mutations.SetCell(
                        family=TEST_COLUMMN_FAMILY_NAME,
                        qualifier=TEST_COLUMN_NAME,
                        new_value=cell_value,
                        timestamp_micros=-1,
                    )
                ],
            )
        )

    await data_client_table.bulk_mutate_rows(row_mutation_entries)


@CrossSync.convert
async def create_backup(
    instance_admin_client, table_admin_client, instance, table, backups_to_delete
) -> admin_v2.Backup:
    """
    Creates a backup of the given table under the given instance.

    This will be restored to a different instance later on, to test
    optimize_restored_table.
    """
    # Get a cluster in the instance for the backup
    list_clusters_response = await instance_admin_client.list_clusters(
        parent=instance.name
    )
    cluster_name = list_clusters_response.clusters[0].name

    backup_id = generate_unique_suffix(BACKUP_PREFIX)

    # Create the backup
    operation = await table_admin_client.create_backup(
        admin_v2.CreateBackupRequest(
            parent=cluster_name,
            backup_id=backup_id,
            backup=admin_v2.Backup(
                name=f"{cluster_name}/backups/{backup_id}",
                source_table=table.name,
                expire_time=datetime.now() + timedelta(hours=7),
            ),
        )
    )

    # add to cleanup list before waiting for result, in case of timeout
    backup_name = f"{cluster_name}/backups/{backup_id}"
    backup_placeholder = admin_v2.Backup(name=backup_name)
    backups_to_delete.append(backup_placeholder)

    backup = await operation.result()

    # replace with full backup object
    backups_to_delete[-1] = backup

    return backup


@CrossSync.convert
async def assert_table_cell_value_equal_to(
    table_admin_client, data_client, instance, table, value
):
    """
    Asserts that all cells in the given table have the given value.
    """
    data_client_table = data_client.get_table(
        table_admin_client.parse_instance_path(instance.name)["instance"],
        table_admin_client.parse_table_path(table.name)["table"],
    )

    # Read all the rows; there shouldn't be that many of them
    query = read_rows_query.ReadRowsQuery(limit=NUM_ROWS)
    async for row in await data_client_table.read_rows_stream(query):
        latest_cell = row[TEST_COLUMMN_FAMILY_NAME, TEST_COLUMN_NAME][0]
        assert latest_cell.value.decode("utf-8") == value


@CrossSync.convert(
    replace_symbols={
        "AsyncRestoreTableOperation": "RestoreTableOperation",
        "AsyncOperation": "Operation",
    }
)
@CrossSync.pytest
@pytest.mark.skipif(
    os.getenv(BIGTABLE_EMULATOR),
    reason="Backups are not supported in the Bigtable emulator",
)
@pytest.mark.parametrize(
    "second_instance_storage_type,expect_optimize_operation",
    [
        (admin_v2.StorageType.HDD, False),
        (admin_v2.StorageType.SSD, True),
    ],
)
async def test_optimize_restored_table(
    admin_overlay_project_id,
    instance_admin_client,
    table_admin_client,
    data_client,
    instances_to_delete,
    backups_to_delete,
    second_instance_storage_type,
    expect_optimize_operation,
):
    # Create two instances. We backup a table from the first instance to a new table in the
    # second instance. This is to test whether or not different scenarios trigger an
    # optimize_restored_table operation
    instance_with_backup, table_to_backup = await create_instance(
        instance_admin_client,
        table_admin_client,
        data_client,
        admin_overlay_project_id,
        instances_to_delete,
        admin_v2.StorageType.HDD,
    )

    if second_instance_storage_type == admin_v2.StorageType.HDD:
        instance_to_restore = instance_with_backup
    else:
        instance_to_restore, _ = await create_instance(
            instance_admin_client,
            table_admin_client,
            data_client,
            admin_overlay_project_id,
            instances_to_delete,
            second_instance_storage_type,
        )

    backup = await create_backup(
        instance_admin_client,
        table_admin_client,
        instance_with_backup,
        table_to_backup,
        backups_to_delete,
    )

    # Restore to other instance
    restore_operation = await table_admin_client.restore_table(
        admin_v2.RestoreTableRequest(
            parent=instance_to_restore.name,
            table_id=TEST_BACKUP_TABLE_NAME,
            backup=backup.name,
        )
    )

    assert isinstance(restore_operation, admin_v2.AsyncRestoreTableOperation)
    restored_table = await restore_operation.result()

    optimize_operation = await restore_operation.optimize_restored_table_operation()
    if expect_optimize_operation:
        assert isinstance(optimize_operation, api_core_operation.AsyncOperation)
        await optimize_operation.result()
    else:
        assert optimize_operation is None

    # Test that the new table exists
    assert (
        restored_table.name
        == f"{instance_to_restore.name}/tables/{TEST_BACKUP_TABLE_NAME}"
    )
    await assert_table_cell_value_equal_to(
        table_admin_client,
        data_client,
        instance_to_restore,
        restored_table,
        INITIAL_CELL_VALUE,
    )


@CrossSync.pytest
async def test_wait_for_consistency(
    instance_admin_client,
    table_admin_client,
    data_client,
    instances_to_delete,
    admin_overlay_project_id,
):
    # Create an instance and a table, then try to write NEW_CELL_VALUE
    # to each table row instead of INITIAL_CELL_VALUE.
    instance, table = await create_instance(
        instance_admin_client,
        table_admin_client,
        data_client,
        admin_overlay_project_id,
        instances_to_delete,
        cluster_locations=REPLICATION_CLUSTER_LOCATIONS,
    )

    await populate_table(
        table_admin_client, data_client, instance, table, NEW_CELL_VALUE
    )

    wait_for_consistency_request = admin_v2.WaitForConsistencyRequest(
        name=table.name,
        standard_read_remote_writes=admin_v2.StandardReadRemoteWrites(),
    )
    await table_admin_client.wait_for_consistency(wait_for_consistency_request)
    await assert_table_cell_value_equal_to(
        table_admin_client, data_client, instance, table, NEW_CELL_VALUE
    )
