# Copyright 2017 Google LLC
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

"""Populate spanner databases with data for streaming system tests."""

# Import relative to the script's directory
from streaming_utils import (
    DATABASE_NAME,
    FORTY_KAY,
    FOUR_HUNDRED_KAY,
    FOUR_KAY,
    FOUR_MEG,
    INSTANCE_NAME,
    print_func,
)

from google.cloud.spanner_v1 import Client
from google.cloud.spanner_v1.keyset import KeySet
from google.cloud.spanner_v1.pool import BurstyPool

DDL = """\
CREATE TABLE {0.table} (
    pkey INT64,
    chunk_me STRING({0.value_size}) )
    PRIMARY KEY (pkey);
CREATE TABLE {1.table} (
    pkey INT64,
    chunk_me STRING({1.value_size}) )
    PRIMARY KEY (pkey);
CREATE TABLE {2.table} (
    pkey INT64,
    chunk_me STRING({2.value_size}) )
    PRIMARY KEY (pkey);
CREATE TABLE {3.table} (
    pkey INT64,
    chunk_me STRING({3.value_size}),
    chunk_me_2 STRING({3.value_size}) )
    PRIMARY KEY (pkey);
""".format(FOUR_KAY, FORTY_KAY, FOUR_HUNDRED_KAY, FOUR_MEG)


DDL_STATEMENTS = [stmt.strip() for stmt in DDL.split(";") if stmt.strip()]


def ensure_database(client):
    instance = client.instance(INSTANCE_NAME)

    if not instance.exists():
        configs = list(client.list_instance_configs())
        config_name = configs[0].name
        print_func("Creating instance: {}".format(INSTANCE_NAME))
        instance = client.instance(INSTANCE_NAME, config_name)
        operation = instance.create()
        operation.result(30)
    else:
        print_func("Instance exists: {}".format(INSTANCE_NAME))
        instance.reload()

    pool = BurstyPool()
    database = instance.database(
        DATABASE_NAME, ddl_statements=DDL_STATEMENTS, pool=pool
    )

    if not database.exists():
        print_func("Creating database: {}".format(DATABASE_NAME))
        operation = database.create()
        operation.result(30)
    else:
        print_func("Database exists: {}".format(DATABASE_NAME))
        database.reload()

    return database


def populate_table(database, table_desc):
    all_ = KeySet(all_=True)
    columns = ("pkey", "chunk_me")
    with database.snapshot() as snapshot:
        rows = list(
            snapshot.execute_sql("SELECT COUNT(*) FROM {}".format(table_desc.table))
        )
    assert len(rows) == 1
    count = rows[0][0]
    if count != table_desc.row_count:
        print_func("Repopulating table: {}".format(table_desc.table))
        chunk_me = table_desc.value()
        row_data = [(index, chunk_me) for index in range(table_desc.row_count)]
        with database.batch() as batch:
            batch.delete(table_desc.table, all_)
            batch.insert(table_desc.table, columns, row_data)
    else:
        print_func("Leaving table: {}".format(table_desc.table))


def populate_table_2_columns(database, table_desc):
    all_ = KeySet(all_=True)
    columns = ("pkey", "chunk_me", "chunk_me_2")
    with database.snapshot() as snapshot:
        rows = list(
            snapshot.execute_sql("SELECT COUNT(*) FROM {}".format(table_desc.table))
        )
    assert len(rows) == 1
    count = rows[0][0]
    if count != table_desc.row_count:
        print_func("Repopulating table: {}".format(table_desc.table))
        chunk_me = table_desc.value()
        row_data = [
            (index, chunk_me, chunk_me) for index in range(table_desc.row_count)
        ]
        with database.batch() as batch:
            batch.delete(table_desc.table, all_)
            batch.insert(table_desc.table, columns, row_data)
    else:
        print_func("Leaving table: {}".format(table_desc.table))


def populate_streaming(client):
    database = ensure_database(client)
    populate_table(database, FOUR_KAY)
    populate_table(database, FORTY_KAY)
    populate_table(database, FOUR_HUNDRED_KAY)
    # Max STRING column size is just larger than 2 Mb, so use two columns
    populate_table_2_columns(database, FOUR_MEG)


if __name__ == "__main__":
    client = Client()
    populate_streaming(client)
