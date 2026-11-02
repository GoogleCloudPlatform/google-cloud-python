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

"""Testable usage examples for Google Cloud Bigtable API wrapper

Each example function takes a ``client`` argument (which must be an instance
of :class:`google.cloud.bigtable.client.Client`) and uses it to perform a task
with the API.

To facilitate running the examples as system tests, each example is also passed
a ``to_delete`` list;  the function adds to the list any objects created which
need to be deleted during teardown.

.. note::
    This file is under progress and will be updated with more guidance from
    the team. Unit tests will be added with guidance from the team.

"""

from datetime import datetime, timezone

import pytest
from google.api_core.exceptions import ServiceUnavailable, TooManyRequests
from test_utils.retry import RetryErrors
from test_utils.system import unique_resource_id

from google.cloud.bigtable import Client, column_family, enums

INSTANCE_ID = "snippet" + unique_resource_id("-")
CLUSTER_ID = "clus-1" + unique_resource_id("-")
TABLE_ID = "tabl-1" + unique_resource_id("-")
COLUMN_FAMILY_ID = "col_fam_id-" + unique_resource_id("-")
LOCATION_ID = "us-central1-f"
ALT_LOCATION_ID = "us-central1-a"
PRODUCTION = enums.Instance.Type.PRODUCTION
SERVER_NODES = 3
STORAGE_TYPE = enums.StorageType.SSD
LABEL_KEY = "python-snippet"
LABEL_STAMP = (
    datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dt%H-%M-%S")
)
LABELS = {LABEL_KEY: str(LABEL_STAMP)}
COLUMN_FAMILY_ID = "col_fam_id1"
COL_NAME1 = b"col-name1"
CELL_VAL1 = b"cell-val"
ROW_KEY1 = b"row_key_id1"
COLUMN_FAMILY_ID2 = "col_fam_id2"
COL_NAME2 = b"col-name2"
CELL_VAL2 = b"cell-val2"
ROW_KEY2 = b"row_key_id2"

retry_429_503 = RetryErrors((ServiceUnavailable, TooManyRequests), max_tries=9)


class Config(object):
    """Run-time configuration to be modified at set-up.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """

    CLIENT = None
    INSTANCE = None
    TABLE = None


def setup_module():
    client = Config.CLIENT = Client(admin=True)
    Config.INSTANCE = client.instance(
        INSTANCE_ID, instance_type=PRODUCTION, labels=LABELS
    )
    cluster = Config.INSTANCE.cluster(
        CLUSTER_ID,
        location_id=LOCATION_ID,
        serve_nodes=SERVER_NODES,
        default_storage_type=STORAGE_TYPE,
    )
    operation = Config.INSTANCE.create(clusters=[cluster])
    # We want to make sure the operation completes.
    operation.result(timeout=100)
    Config.TABLE = Config.INSTANCE.table(TABLE_ID)
    Config.TABLE.create()
    gc_rule = column_family.MaxVersionsGCRule(2)
    column_family1 = Config.TABLE.column_family(COLUMN_FAMILY_ID, gc_rule=gc_rule)
    column_family1.create()
    gc_rule2 = column_family.MaxVersionsGCRule(4)
    column_family2 = Config.TABLE.column_family(COLUMN_FAMILY_ID2, gc_rule=gc_rule2)
    column_family2.create()


def teardown_module():
    retry_429_503(Config.INSTANCE.delete)()


def test_bigtable_create_table():
    # [START bigtable_api_create_table]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)

    # Create table without Column families.
    table1 = instance.table("table_id1")
    table1.create()

    # Create table with Column families.
    table2 = instance.table("table_id2")
    # Define the GC policy to retain only the most recent 2 versions.
    max_versions_rule = column_family.MaxVersionsGCRule(2)
    table2.create(column_families={"cf1": max_versions_rule})

    # [END bigtable_api_create_table]
    assert table1.exists()
    assert table2.exists()
    table1.delete()
    table2.delete()


def test_bigtable_sample_row_keys():
    table_sample = Config.INSTANCE.table("table_id1_samplerow")
    initial_split_keys = [b"split_key_1", b"split_key_10", b"split_key_20"]
    table_sample.create(initial_split_keys=initial_split_keys)
    assert table_sample.exists()

    # [START bigtable_api_sample_row_keys]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)

    table = instance.table("table_id1_samplerow")
    data = table.sample_row_keys()
    actual_keys, offset = zip(*[(rk.row_key, rk.offset_bytes) for rk in data])
    # [END bigtable_api_sample_row_keys]
    initial_split_keys.append(b"")
    assert list(actual_keys) == initial_split_keys
    table.delete()


def test_bigtable_write_read_drop_truncate():
    # [START bigtable_api_mutate_rows]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"row_key_4",
        b"row_key_20",
        b"row_key_22",
        b"row_key_200",
    ]
    col_name = b"col-name1"
    rows = []
    for i, row_key in enumerate(row_keys):
        value = "value_{}".format(i).encode()
        row = table.row(row_key)
        row.set_cell(
            COLUMN_FAMILY_ID, col_name, value, timestamp=datetime.now(timezone.utc)
        )
        rows.append(row)
    response = table.mutate_rows(rows)
    # validate that all rows written successfully
    for i, status in enumerate(response):
        if status.code != 0:
            print("Row number {} failed to write".format(i))
    # [END bigtable_api_mutate_rows]
    assert len(response) == len(rows)
    # [START bigtable_api_read_row]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = "row_key_1"
    row = table.read_row(row_key)
    # [END bigtable_api_read_row]
    assert row.row_key.decode("utf-8") == row_key
    # [START bigtable_api_read_rows]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    # Read full table
    partial_rows = table.read_rows()

    # Read row's value
    total_rows = []
    for row in partial_rows:
        cell = row.cells[COLUMN_FAMILY_ID][col_name][0]
        print(cell.value.decode("utf-8"))
        total_rows.append(cell)
    # [END bigtable_api_read_rows]
    assert len(total_rows) == len(rows)
    # [START bigtable_api_drop_by_prefix]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key_prefix = b"row_key_2"
    table.drop_by_prefix(row_key_prefix, timeout=200)
    # [END bigtable_api_drop_by_prefix]
    dropped_row_keys = [b"row_key_2", b"row_key_20", b"row_key_22", b"row_key_200"]
    for row in table.read_rows():
        assert row.row_key.decode("utf-8") not in dropped_row_keys

    # [START bigtable_api_truncate_table]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    table.truncate(timeout=200)
    # [END bigtable_api_truncate_table]
    rows_data_after_truncate = []
    for row in table.read_rows():
        rows_data_after_truncate.append(row.row_key)
    assert rows_data_after_truncate == []


def test_bigtable_mutations_batcher():
    # [START bigtable_api_mutations_batcher]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    batcher = table.mutations_batcher()
    # [END bigtable_api_mutations_batcher]

    # Below code will be used while creating batcher.py snippets.
    # So not removing this code as of now.
    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"row_key_4",
        b"row_key_20",
        b"row_key_22",
        b"row_key_200",
    ]
    column_name = "column_name".encode()
    # Add a single row
    row_key = row_keys[0]
    row = table.row(row_key)
    row.set_cell(
        COLUMN_FAMILY_ID, column_name, "value-0", timestamp=datetime.now(timezone.utc)
    )
    batcher.mutate(row)
    # Add a collections of rows
    rows = []
    for i in range(1, len(row_keys)):
        row = table.row(row_keys[i])
        value = "value_{}".format(i).encode()
        row.set_cell(
            COLUMN_FAMILY_ID, column_name, value, timestamp=datetime.now(timezone.utc)
        )
        rows.append(row)
    batcher.mutate_rows(rows)
    # batcher will flush current batch if it
    # reaches the max flush_count

    # Manually send the current batch to Cloud Bigtable
    batcher.flush()
    rows_on_table = []
    for row in table.read_rows():
        rows_on_table.append(row.row_key)
    assert len(rows_on_table) == len(row_keys)
    table.truncate(timeout=200)


def test_bigtable_table_column_family():
    # [START bigtable_api_table_column_family]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)

    table = instance.table(TABLE_ID)
    column_family_obj = table.column_family(COLUMN_FAMILY_ID)
    # [END bigtable_api_table_column_family]

    assert column_family_obj.column_family_id == COLUMN_FAMILY_ID


def test_bigtable_list_tables():
    # [START bigtable_api_list_tables]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    tables_list = instance.list_tables()
    # [END bigtable_api_list_tables]
    assert len(tables_list) != 0


def test_bigtable_table_name():
    import re

    # [START bigtable_api_table_name]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)

    table = instance.table(TABLE_ID)
    table_name = table.name
    # [END bigtable_api_table_name]
    _table_name_re = re.compile(
        r"^projects/(?P<project>[^/]+)/"
        r"instances/(?P<instance>[^/]+)/tables/"
        r"(?P<table_id>[_a-zA-Z0-9][-_.a-zA-Z0-9]*)$"
    )
    assert _table_name_re.match(table_name)


def test_bigtable_list_column_families():
    # [START bigtable_api_list_column_families]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    column_family_list = table.list_column_families()
    # [END bigtable_api_list_column_families]

    assert len(column_family_list) > 0


def test_bigtable_get_cluster_states():
    # [START bigtable_api_get_cluster_states]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    get_cluster_states = table.get_cluster_states()
    # [END bigtable_api_get_cluster_states]

    assert CLUSTER_ID in get_cluster_states


def test_bigtable_table_test_iam_permissions():
    table_policy = Config.INSTANCE.table("table_id_iam_policy")
    table_policy.create()
    assert table_policy.exists

    # [START bigtable_api_table_test_iam_permissions]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table("table_id_iam_policy")

    permissions = ["bigtable.tables.mutateRows", "bigtable.tables.readRows"]
    permissions_allowed = table.test_iam_permissions(permissions)
    # [END bigtable_api_table_test_iam_permissions]
    assert permissions_allowed == permissions


def test_bigtable_table_set_iam_policy_then_get_iam_policy():
    table_policy = Config.INSTANCE.table("table_id_iam_policy")
    assert table_policy.exists
    service_account_email = Config.CLIENT._credentials.service_account_email

    # [START bigtable_api_table_set_iam_policy]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable.policy import BIGTABLE_ADMIN_ROLE, Policy

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table("table_id_iam_policy")
    new_policy = Policy()
    new_policy[BIGTABLE_ADMIN_ROLE] = [Policy.service_account(service_account_email)]

    policy_latest = table.set_iam_policy(new_policy)
    # [END bigtable_api_table_set_iam_policy]
    assert len(policy_latest.bigtable_admins) > 0

    # [START bigtable_api_table_get_iam_policy]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table("table_id_iam_policy")
    policy = table.get_iam_policy()
    # [END bigtable_api_table_get_iam_policy]
    assert len(policy.bigtable_admins) > 0


def test_bigtable_table_exists():
    # [START bigtable_api_check_table_exists]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    table_exists = table.exists()
    # [END bigtable_api_check_table_exists]
    assert table_exists


def test_bigtable_delete_table():
    table_del = Config.INSTANCE.table("table_id_del")
    table_del.create()
    assert table_del.exists()

    # [START bigtable_api_delete_table]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table("table_id_del")

    table.delete()
    # [END bigtable_api_delete_table]
    assert not table.exists()


def test_bigtable_table_row():
    # [START bigtable_api_table_row]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_keys = [b"row_key_1", b"row_key_2"]
    row1_obj = table.row(row_keys[0])
    row2_obj = table.row(row_keys[1])
    # [END bigtable_api_table_row]

    row1_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row1_obj.commit()
    row2_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row2_obj.commit()

    written_row_keys = []
    for row in table.read_rows():
        written_row_keys.append(row.row_key)

    assert written_row_keys == row_keys

    table.truncate(timeout=300)


def test_bigtable_table_append_row():
    # [START bigtable_api_table_append_row]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_keys = [b"row_key_1", b"row_key_2"]
    row1_obj = table.append_row(row_keys[0])
    row2_obj = table.append_row(row_keys[1])
    # [END bigtable_api_table_append_row]

    row1_obj.append_cell_value(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row1_obj.commit()
    row2_obj.append_cell_value(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row2_obj.commit()

    written_row_keys = []
    for row in table.read_rows():
        written_row_keys.append(row.row_key)

    assert written_row_keys == row_keys

    table.truncate(timeout=300)


def test_bigtable_table_direct_row():
    # [START bigtable_api_table_direct_row]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_keys = [b"row_key_1", b"row_key_2"]
    row1_obj = table.direct_row(row_keys[0])
    row2_obj = table.direct_row(row_keys[1])
    # [END bigtable_api_table_direct_row]

    row1_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row1_obj.commit()
    row2_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row2_obj.commit()

    written_row_keys = []
    for row in table.read_rows():
        written_row_keys.append(row.row_key)

    assert written_row_keys == row_keys

    table.truncate(timeout=300)


def test_bigtable_table_conditional_row():
    # [START bigtable_api_table_conditional_row]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable.row_filters import PassAllFilter

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_keys = [b"row_key_1", b"row_key_2"]
    filter_ = PassAllFilter(True)
    row1_obj = table.conditional_row(row_keys[0], filter_=filter_)
    row2_obj = table.conditional_row(row_keys[1], filter_=filter_)
    # [END bigtable_api_table_conditional_row]

    row1_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1, state=False)
    row1_obj.commit()
    row2_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1, state=False)
    row2_obj.commit()

    written_row_keys = []
    for row in table.read_rows():
        written_row_keys.append(row.row_key)

    assert written_row_keys == row_keys

    table.truncate(timeout=300)


def test_bigtable_column_family_name():
    # [START bigtable_api_column_family_name]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    column_families = table.list_column_families()
    column_family_obj = column_families[COLUMN_FAMILY_ID]
    column_family_name = column_family_obj.name
    # [END bigtable_api_column_family_name]
    import re

    _cf_name_re = re.compile(
        r"^projects/(?P<project>[^/]+)/"
        r"instances/(?P<instance>[^/]+)/tables/"
        r"(?P<table>[^/]+)/columnFamilies/"
        r"(?P<cf_id>[_a-zA-Z0-9][-_.a-zA-Z0-9]*)$"
    )
    assert _cf_name_re.match(column_family_name)


def test_bigtable_create_update_delete_column_family():
    # [START bigtable_api_create_column_family]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    column_family_id = "column_family_id1"
    gc_rule = column_family.MaxVersionsGCRule(2)
    column_family_obj = table.column_family(column_family_id, gc_rule=gc_rule)
    column_family_obj.create()

    # [END bigtable_api_create_column_family]
    column_families = table.list_column_families()
    assert column_families[column_family_id].gc_rule == gc_rule

    # [START bigtable_api_update_column_family]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    # Already existing column family id
    column_family_id = "column_family_id1"
    # Define the GC rule to retain data with max age of 5 days
    max_age_rule = column_family.MaxAgeGCRule(datetime.timedelta(days=5))
    column_family_obj = table.column_family(column_family_id, gc_rule=max_age_rule)
    column_family_obj.update()
    # [END bigtable_api_update_column_family]

    updated_families = table.list_column_families()
    assert updated_families[column_family_id].gc_rule == max_age_rule

    # [START bigtable_api_delete_column_family]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    column_family_id = "column_family_id1"
    column_family_obj = table.column_family(column_family_id)
    column_family_obj.delete()
    # [END bigtable_api_delete_column_family]
    column_families = table.list_column_families()
    assert column_family_id not in column_families


def test_bigtable_add_row_add_row_range_add_row_range_from_keys():
    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"row_key_4",
        b"row_key_5",
        b"row_key_6",
        b"row_key_7",
        b"row_key_8",
        b"row_key_9",
    ]

    rows = []
    for row_key in row_keys:
        row = Config.TABLE.row(row_key)
        row.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
        rows.append(row)
    Config.TABLE.mutate_rows(rows)

    # [START bigtable_api_add_row_key]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable.row_set import RowSet

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_set = RowSet()
    row_set.add_row_key(b"row_key_5")
    # [END bigtable_api_add_row_key]

    read_rows = table.read_rows(row_set=row_set)
    expected_row_keys = [b"row_key_5"]
    found_row_keys = [row.row_key for row in read_rows]
    assert found_row_keys == expected_row_keys

    # [START bigtable_api_add_row_range]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable.row_set import RowRange, RowSet

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_set = RowSet()
    row_set.add_row_range(RowRange(start_key=b"row_key_3", end_key=b"row_key_7"))
    # [END bigtable_api_add_row_range]

    read_rows = table.read_rows(row_set=row_set)
    expected_row_keys = [b"row_key_3", b"row_key_4", b"row_key_5", b"row_key_6"]
    found_row_keys = [row.row_key for row in read_rows]
    assert found_row_keys == expected_row_keys

    # [START bigtable_api_row_range_from_keys]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable.row_set import RowSet

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_set = RowSet()
    row_set.add_row_range_from_keys(start_key=b"row_key_3", end_key=b"row_key_7")
    # [END bigtable_api_row_range_from_keys]

    read_rows = table.read_rows(row_set=row_set)
    expected_row_keys = [b"row_key_3", b"row_key_4", b"row_key_5", b"row_key_6"]
    found_row_keys = [row.row_key for row in read_rows]
    assert found_row_keys == expected_row_keys
    table.truncate(timeout=200)


def test_bigtable_add_row_range_with_prefix():
    row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
        b"sample_row_key_1",
        b"sample_row_key_2",
    ]

    rows = []
    for row_key in row_keys:
        row = Config.TABLE.row(row_key)
        row.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
        rows.append(row)
    Config.TABLE.mutate_rows(rows)

    # [START bigtable_api_add_row_range_with_prefix]
    from google.cloud.bigtable import Client
    from google.cloud.bigtable.row_set import RowSet

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_set = RowSet()
    row_set.add_row_range_with_prefix("row")
    # [END bigtable_api_add_row_range_with_prefix]

    read_rows = table.read_rows(row_set=row_set)
    expected_row_keys = [
        b"row_key_1",
        b"row_key_2",
        b"row_key_3",
    ]
    found_row_keys = [row.row_key for row in read_rows]
    assert found_row_keys == expected_row_keys
    table.truncate(timeout=200)


def test_bigtable_batcher_mutate_flush_mutate_rows():
    # [START bigtable_api_batcher_mutate]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    # Batcher for max row bytes, max_row_bytes=1024 is optional.
    batcher = table.mutations_batcher(max_row_bytes=1024)

    # Add a single row
    row_key = b"row_key_1"
    row = table.row(row_key)
    row.set_cell(
        COLUMN_FAMILY_ID, COL_NAME1, "value-0", timestamp=datetime.now(timezone.utc)
    )

    # In batcher, mutate will flush current batch if it
    # reaches the max_row_bytes
    batcher.mutate(row)
    batcher.flush()
    # [END bigtable_api_batcher_mutate]

    # [START bigtable_api_batcher_flush]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    # Batcher for max row bytes, max_row_bytes=1024 is optional.
    batcher = table.mutations_batcher(max_row_bytes=1024)

    # Add a single row
    row_key = b"row_key"
    row = table.row(row_key)
    row.set_cell(COLUMN_FAMILY_ID, COL_NAME1, "value-0")

    # In batcher, mutate will flush current batch if it
    # reaches the max_row_bytes
    batcher.mutate(row)
    batcher.flush()
    # [END bigtable_api_batcher_flush]

    rows_on_table = []
    for row in table.read_rows():
        rows_on_table.append(row.row_key)
    assert len(rows_on_table) == 2
    table.truncate(timeout=200)

    # [START bigtable_api_batcher_mutate_rows]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    batcher = table.mutations_batcher()

    row1 = table.row(b"row_key_1")
    row2 = table.row(b"row_key_2")
    row3 = table.row(b"row_key_3")
    row4 = table.row(b"row_key_4")

    row1.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val1")
    row2.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val2")
    row3.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val3")
    row4.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val4")

    batcher.mutate_rows([row1, row2, row3, row4])

    # batcher will flush current batch if it
    # reaches the max flush_count
    # Manually send the current batch to Cloud Bigtable
    batcher.flush()
    # [END bigtable_api_batcher_mutate_rows]

    rows_on_table = []
    for row in table.read_rows():
        rows_on_table.append(row.row_key)
    assert len(rows_on_table) == 4
    table.truncate(timeout=200)


def test_bigtable_create_family_gc_max_age():
    # [START bigtable_api_create_family_gc_max_age]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    # Define the GC rule to retain data with max age of 5 days
    max_age_rule = column_family.MaxAgeGCRule(datetime.timedelta(days=5))

    column_family_obj = table.column_family("cf1", max_age_rule)
    column_family_obj.create()

    # [END bigtable_api_create_family_gc_max_age]
    rule = str(column_family_obj.to_pb())
    assert "max_age" in rule
    assert "seconds: 432000" in rule
    column_family_obj.delete()


def test_bigtable_create_family_gc_max_versions():
    # [START bigtable_api_create_family_gc_max_versions]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    # Define the GC policy to retain only the most recent 2 versions
    max_versions_rule = column_family.MaxVersionsGCRule(2)

    column_family_obj = table.column_family("cf2", max_versions_rule)
    column_family_obj.create()

    # [END bigtable_api_create_family_gc_max_versions]
    rule = str(column_family_obj.to_pb())
    assert "max_num_versions: 2" in rule
    column_family_obj.delete()


def test_bigtable_create_family_gc_union():
    # [START bigtable_api_create_family_gc_union]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    max_versions_rule = column_family.MaxVersionsGCRule(2)
    max_age_rule = column_family.MaxAgeGCRule(datetime.timedelta(days=5))

    union_rule = column_family.GCRuleUnion([max_versions_rule, max_age_rule])

    column_family_obj = table.column_family("cf3", union_rule)
    column_family_obj.create()

    # [END bigtable_api_create_family_gc_union]
    rule = str(column_family_obj.to_pb())
    assert "union" in rule
    assert "max_age" in rule
    assert "seconds: 432000" in rule
    assert "max_num_versions: 2" in rule
    column_family_obj.delete()


def test_bigtable_create_family_gc_intersection():
    # [START bigtable_api_create_family_gc_intersection]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    max_versions_rule = column_family.MaxVersionsGCRule(2)
    max_age_rule = column_family.MaxAgeGCRule(datetime.timedelta(days=5))

    intersection_rule = column_family.GCRuleIntersection(
        [max_versions_rule, max_age_rule]
    )

    column_family_obj = table.column_family("cf4", intersection_rule)
    column_family_obj.create()

    # [END bigtable_api_create_family_gc_intersection]

    rule = str(column_family_obj.to_pb())
    assert "intersection" in rule
    assert "max_num_versions: 2" in rule
    assert "max_age" in rule
    assert "seconds: 432000" in rule
    column_family_obj.delete()


def test_bigtable_create_family_gc_nested():
    # [START bigtable_api_create_family_gc_nested]
    from google.cloud.bigtable import Client, column_family

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    # Create a column family with nested GC policies.
    # Create a nested GC rule:
    # Drop cells that are either older than the 10 recent versions
    # OR
    # Drop cells that are older than a month AND older than the
    # 2 recent versions
    rule1 = column_family.MaxVersionsGCRule(10)
    rule2 = column_family.GCRuleIntersection(
        [
            column_family.MaxAgeGCRule(datetime.timedelta(days=5)),
            column_family.MaxVersionsGCRule(2),
        ]
    )

    nested_rule = column_family.GCRuleUnion([rule1, rule2])

    column_family_obj = table.column_family("cf5", nested_rule)
    column_family_obj.create()

    # [END bigtable_api_create_family_gc_nested]

    rule = str(column_family_obj.to_pb())
    assert "intersection" in rule
    assert "max_num_versions: 2" in rule
    assert "max_age" in rule
    assert "seconds: 432000" in rule
    column_family_obj.delete()


def test_bigtable_row_data_cells_cell_value_cell_values():
    value = b"value_in_col1"
    row = Config.TABLE.row(b"row_key_1")
    row.set_cell(
        COLUMN_FAMILY_ID, COL_NAME1, value, timestamp=datetime.now(timezone.utc)
    )
    row.commit()

    row.set_cell(
        COLUMN_FAMILY_ID, COL_NAME1, value, timestamp=datetime.now(timezone.utc)
    )
    row.commit()

    # [START bigtable_api_row_data_cells]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = "row_key_1"
    row_data = table.read_row(row_key)

    cells = row_data.cells
    # [END bigtable_api_row_data_cells]

    actual_cell_value = cells[COLUMN_FAMILY_ID][COL_NAME1][0].value
    assert actual_cell_value == value

    # [START bigtable_api_row_cell_value]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = "row_key_1"
    row_data = table.read_row(row_key)

    cell_value = row_data.cell_value(COLUMN_FAMILY_ID, COL_NAME1)
    # [END bigtable_api_row_cell_value]
    assert cell_value == value

    # [START bigtable_api_row_cell_values]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = "row_key_1"
    row_data = table.read_row(row_key)

    cell_values = row_data.cell_values(COLUMN_FAMILY_ID, COL_NAME1)
    # [END bigtable_api_row_cell_values]

    for actual_value, timestamp in cell_values:
        assert actual_value == value

    value2 = b"value_in_col2"
    row.set_cell(COLUMN_FAMILY_ID, COL_NAME2, value2)
    row.commit()

    # [START bigtable_api_row_find_cells]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row_key = "row_key_1"
    row = table.read_row(row_key)

    cells = row.find_cells(COLUMN_FAMILY_ID, COL_NAME2)
    # [END bigtable_api_row_find_cells]

    assert cells[0].value == value2
    table.truncate(timeout=200)


def test_bigtable_row_setcell_rowkey():
    # [START bigtable_api_row_set_cell]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row = table.row(ROW_KEY1)

    cell_val = b"cell-val"
    row.set_cell(
        COLUMN_FAMILY_ID, COL_NAME1, cell_val, timestamp=datetime.now(timezone.utc)
    )
    # [END bigtable_api_row_set_cell]

    response = table.mutate_rows([row])
    # validate that all rows written successfully
    for i, status in enumerate(response):
        assert status.code == 0

    # [START bigtable_api_row_row_key]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row = table.row(ROW_KEY1)
    row_key = row.row_key
    # [END bigtable_api_row_row_key]
    assert row_key == ROW_KEY1

    # [START bigtable_api_row_table]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row = table.row(ROW_KEY1)
    table1 = row.table
    # [END bigtable_api_row_table]

    assert table1 == table
    table.truncate(timeout=200)


def test_bigtable_row_delete():
    table_row_del = Config.INSTANCE.table(TABLE_ID)
    row_obj = table_row_del.row(b"row_key_1")
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val")
    row_obj.commit()
    written_row_keys = []
    for row in table_row_del.read_rows():
        written_row_keys.append(row.row_key)
    assert written_row_keys == [b"row_key_1"]

    # [START bigtable_api_row_delete]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key = b"row_key_1"
    row_obj = table.row(row_key)

    row_obj.delete()
    row_obj.commit()
    # [END bigtable_api_row_delete]

    written_row_keys = []
    for row in table.read_rows():
        written_row_keys.append(row.row_key)
    assert len(written_row_keys) == 0


def test_bigtable_row_delete_cell():
    table_row_del_cell = Config.INSTANCE.table(TABLE_ID)
    row_key1 = b"row_key_1"
    row_obj = table_row_del_cell.row(row_key1)
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row_obj.commit()

    written_row_keys = []
    for row in table_row_del_cell.read_rows():
        written_row_keys.append(row.row_key)
    assert written_row_keys == [row_key1]

    # [START bigtable_api_row_delete_cell]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key = b"row_key_1"
    row_obj = table.row(row_key)

    row_obj.delete_cell(COLUMN_FAMILY_ID, COL_NAME1)
    row_obj.commit()
    # [END bigtable_api_row_delete_cell]

    for row in table.read_rows():
        assert not row.row_key


def test_bigtable_row_delete_cells():
    table_row_del_cells = Config.INSTANCE.table(TABLE_ID)
    row_key1 = b"row_key_1"
    row_obj = table_row_del_cells.row(row_key1)

    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, CELL_VAL1)
    row_obj.commit()
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME2, CELL_VAL2)
    row_obj.commit()

    written_row_keys = []
    for row in table_row_del_cells.read_rows():
        written_row_keys.append(row.row_key)
    assert written_row_keys == [row_key1]

    # [START bigtable_api_row_delete_cells]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key = b"row_key_1"
    row_obj = table.row(row_key)

    row_obj.delete_cells(COLUMN_FAMILY_ID, [COL_NAME1, COL_NAME2])
    row_obj.commit()
    # [END bigtable_api_row_delete_cells]

    for row in table.read_rows():
        assert not row.row_key


def test_bigtable_row_clear():
    table_row_clear = Config.INSTANCE.table(TABLE_ID)
    row_obj = table_row_clear.row(b"row_key_1")
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val")

    mutation_size = row_obj.get_mutations_size()
    assert mutation_size > 0

    # [START bigtable_api_row_clear]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key = b"row_key_1"
    row_obj = table.row(row_key)
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val")

    row_obj.clear()
    # [END bigtable_api_row_clear]

    mutation_size = row_obj.get_mutations_size()
    assert mutation_size == 0


def test_bigtable_row_clear_get_mutations_size():
    # [START bigtable_api_row_get_mutations_size]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key_id = b"row_key_1"
    row_obj = table.row(row_key_id)

    mutation_size = row_obj.get_mutations_size()
    # [END bigtable_api_row_get_mutations_size]
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, b"cell-val")
    mutation_size = row_obj.get_mutations_size()
    assert mutation_size > 0

    row_obj.clear()
    mutation_size = row_obj.get_mutations_size()
    assert mutation_size == 0


def test_bigtable_row_setcell_commit_rowkey():
    # [START bigtable_api_row_set_cell]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key = b"row_key_1"
    cell_val = b"cell-val"
    row_obj = table.row(row_key)
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, cell_val)
    # [END bigtable_api_row_set_cell]
    row_obj.commit()

    # [START bigtable_api_row_commit]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key = b"row_key_2"
    cell_val = b"cell-val"
    row_obj = table.row(row_key)
    row_obj.set_cell(COLUMN_FAMILY_ID, COL_NAME1, cell_val)
    row_obj.commit()
    # [END bigtable_api_row_commit]

    written_row_keys = []
    for row in table.read_rows():
        written_row_keys.append(row.row_key)

    assert written_row_keys == [b"row_key_1", b"row_key_2"]

    # [START bigtable_api_row_row_key]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)

    row_key_id = b"row_key_2"
    row_obj = table.row(row_key_id)
    row_key = row_obj.row_key
    # [END bigtable_api_row_row_key]
    assert row_key == row_key_id
    table.truncate(timeout=300)


def test_bigtable_row_append_cell_value():
    row = Config.TABLE.row(ROW_KEY1)

    cell_val1 = b"1"
    row.set_cell(COLUMN_FAMILY_ID, COL_NAME1, cell_val1)
    row.commit()

    # [START bigtable_api_row_append_cell_value]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row = table.row(ROW_KEY1, append=True)

    cell_val2 = b"2"
    row.append_cell_value(COLUMN_FAMILY_ID, COL_NAME1, cell_val2)
    # [END bigtable_api_row_append_cell_value]
    row.commit()

    row_data = table.read_row(ROW_KEY1)
    actual_value = row_data.cell_value(COLUMN_FAMILY_ID, COL_NAME1)
    assert actual_value == cell_val1 + cell_val2

    # [START bigtable_api_row_commit]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row = Config.TABLE.row(ROW_KEY2)
    cell_val = 1
    row.set_cell(COLUMN_FAMILY_ID, COL_NAME1, cell_val)
    row.commit()
    # [END bigtable_api_row_commit]

    # [START bigtable_api_row_increment_cell_value]
    from google.cloud.bigtable import Client

    client = Client(admin=True)
    instance = client.instance(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    row = table.row(ROW_KEY2, append=True)

    int_val = 3
    row.increment_cell_value(COLUMN_FAMILY_ID, COL_NAME1, int_val)
    # [END bigtable_api_row_increment_cell_value]
    row.commit()

    row_data = table.read_row(ROW_KEY2)
    actual_value = row_data.cell_value(COLUMN_FAMILY_ID, COL_NAME1)

    import struct

    _PACK_I64 = struct.Struct(">q").pack
    assert actual_value == _PACK_I64(cell_val + int_val)
    table.truncate(timeout=200)


if __name__ == "__main__":
    pytest.main()
