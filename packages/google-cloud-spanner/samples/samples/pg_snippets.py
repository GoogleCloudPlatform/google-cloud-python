#!/usr/bin/env python

# Copyright 2022 Google, Inc.
#
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

"""This application demonstrates how to do basic operations using Cloud
Spanner PostgreSql dialect.

For more information, see the README.rst under /spanner.
"""

import argparse
import base64
import datetime
import decimal
import time

from google.cloud import spanner, spanner_admin_database_v1
from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect
from google.cloud.spanner_v1 import param_types
from google.cloud.spanner_v1.data_types import JsonObject

OPERATION_TIMEOUT_SECONDS = 240


# [START spanner_postgresql_create_instance]
def create_instance(instance_id):
    """Creates an instance."""
    spanner_client = spanner.Client()

    config_name = "{}/instanceConfigs/regional-us-central1".format(
        spanner_client.project_name
    )

    instance = spanner_client.instance(
        instance_id,
        configuration_name=config_name,
        display_name="This is a display name.",
        node_count=1,
        labels={
            "cloud_spanner_samples": "true",
            "sample_name": "snippets-create_instance-explicit",
            "created": str(int(time.time())),
        },
    )

    operation = instance.create()

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created instance {}".format(instance_id))


# [END spanner_postgresql_create_instance]


# [START spanner_postgresql_create_database]
def create_database(instance_id, database_id):
    """Creates a PostgreSql database and tables for sample data."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f'CREATE DATABASE "{database_id}"',
        database_dialect=DatabaseDialect.POSTGRESQL,
    )

    operation = database_admin_api.create_database(request=request)

    print("Waiting for operation to complete...")
    database = operation.result(OPERATION_TIMEOUT_SECONDS)

    create_table_using_ddl(database.name)
    print("Created database {} on instance {}".format(database_id, instance_id))


def create_table_using_ddl(database_name):
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_name,
        statements=[
            """CREATE TABLE Singers (
  SingerId   bigint NOT NULL,
  FirstName  character varying(1024),
  LastName   character varying(1024),
  SingerInfo bytea,
  FullName   character varying(2048)
    GENERATED ALWAYS AS (FirstName || ' ' || LastName) STORED,
  PRIMARY KEY (SingerId)
  )""",
            """CREATE TABLE Albums (
  SingerId     bigint NOT NULL,
  AlbumId      bigint NOT NULL,
  AlbumTitle   character varying(1024),
  PRIMARY KEY (SingerId, AlbumId)
  ) INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
        ],
    )
    operation = spanner_client.database_admin_api.update_database_ddl(request)
    operation.result(OPERATION_TIMEOUT_SECONDS)


# [END spanner_postgresql_create_database]


# [START spanner_postgresql_insert_data]
def insert_data(instance_id, database_id):
    """Inserts sample data into the given database.

    The database and table must already exist and can be created using
    `create_database`.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.batch() as batch:
        batch.insert(
            table="Singers",
            columns=("SingerId", "FirstName", "LastName"),
            values=[
                (1, "Marc", "Richards"),
                (2, "Catalina", "Smith"),
                (3, "Alice", "Trentor"),
                (4, "Lea", "Martin"),
                (5, "David", "Lomond"),
            ],
        )

        batch.insert(
            table="Albums",
            columns=("SingerId", "AlbumId", "AlbumTitle"),
            values=[
                (1, 1, "Total Junk"),
                (1, 2, "Go, Go, Go"),
                (2, 1, "Green"),
                (2, 2, "Forever Hold Your Peace"),
                (2, 3, "Terrified"),
            ],
        )

    print("Inserted data.")


# [END spanner_postgresql_insert_data]


# [START spanner_postgresql_delete_data]
def delete_data(instance_id, database_id):
    """Deletes sample data from the given database.

    The database, table, and data must already exist and can be created using
    `create_database` and `insert_data`.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Delete individual rows
    albums_to_delete = spanner.KeySet(keys=[[2, 1], [2, 3]])

    # Delete a range of rows where the column key is >=3 and <5
    singers_range = spanner.KeyRange(start_closed=[3], end_open=[5])
    singers_to_delete = spanner.KeySet(ranges=[singers_range])

    # Delete remaining Singers rows, which will also delete the remaining
    # Albums rows because Albums was defined with ON DELETE CASCADE
    remaining_singers = spanner.KeySet(all_=True)

    with database.batch() as batch:
        batch.delete("Albums", albums_to_delete)
        batch.delete("Singers", singers_to_delete)
        batch.delete("Singers", remaining_singers)

    print("Deleted data.")


# [END spanner_postgresql_delete_data]


# [START spanner_postgresql_query_data]
def query_data(instance_id, database_id):
    """Queries sample data from the database using SQL."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, AlbumTitle FROM Albums"
        )

        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))


# [END spanner_postgresql_query_data]


# [START spanner_postgresql_read_data]
def read_data(instance_id, database_id):
    """Reads sample data from the database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        keyset = spanner.KeySet(all_=True)
        results = snapshot.read(
            table="Albums", columns=("SingerId", "AlbumId", "AlbumTitle"), keyset=keyset
        )

        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))


# [END spanner_postgresql_read_data]


# [START spanner_postgresql_add_column]
def add_column(instance_id, database_id):
    """Adds a new column to the Albums table in the example database."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=["ALTER TABLE Albums ADD COLUMN MarketingBudget BIGINT"],
    )
    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the MarketingBudget column.")


# [END spanner_postgresql_add_column]


# [START spanner_postgresql_update_data]
def update_data(instance_id, database_id):
    """Updates sample data in the database.

    This updates the `MarketingBudget` column which must be created before
    running this sample. You can add the column by running the `add_column`
    sample or by running this DDL statement against your database:

        ALTER TABLE Albums ADD COLUMN MarketingBudget INT64

    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.batch() as batch:
        batch.update(
            table="Albums",
            columns=("SingerId", "AlbumId", "MarketingBudget"),
            values=[(1, 1, 100000), (2, 2, 500000)],
        )

    print("Updated data.")


# [END spanner_postgresql_update_data]


# [START spanner_postgresql_read_write_transaction]
def read_write_transaction(instance_id, database_id):
    """Performs a read-write transaction to update two sample records in the
    database.

    This will transfer 200,000 from the `MarketingBudget` field for the second
    Album to the first Album. If the `MarketingBudget` is too low, it will
    raise an exception.

    Before running this sample, you will need to run the `update_data` sample
    to populate the fields.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def update_albums(transaction):
        # Read the second album budget.
        second_album_keyset = spanner.KeySet(keys=[(2, 2)])
        second_album_result = transaction.read(
            table="Albums",
            columns=("MarketingBudget",),
            keyset=second_album_keyset,
            limit=1,
        )
        second_album_row = list(second_album_result)[0]
        second_album_budget = second_album_row[0]

        transfer_amount = 200000

        if second_album_budget < transfer_amount:
            # Raising an exception will automatically roll back the
            # transaction.
            raise ValueError("The second album doesn't have enough funds to transfer")

        # Read the first album's budget.
        first_album_keyset = spanner.KeySet(keys=[(1, 1)])
        first_album_result = transaction.read(
            table="Albums",
            columns=("MarketingBudget",),
            keyset=first_album_keyset,
            limit=1,
        )
        first_album_row = list(first_album_result)[0]
        first_album_budget = first_album_row[0]

        # Update the budgets.
        second_album_budget -= transfer_amount
        first_album_budget += transfer_amount
        print(
            "Setting first album's budget to {} and the second album's "
            "budget to {}.".format(first_album_budget, second_album_budget)
        )

        # Update the rows.
        transaction.update(
            table="Albums",
            columns=("SingerId", "AlbumId", "MarketingBudget"),
            values=[(1, 1, first_album_budget), (2, 2, second_album_budget)],
        )

    database.run_in_transaction(update_albums)

    print("Transaction complete.")


# [END spanner_postgresql_read_write_transaction]


# [START spanner_postgresql_query_data_with_new_column]
def query_data_with_new_column(instance_id, database_id):
    """Queries sample data from the database using SQL.

    This sample uses the `MarketingBudget` column. You can add the column
    by running the `add_column` sample or by running this DDL statement against
    your database:

        ALTER TABLE Albums ADD COLUMN MarketingBudget INT64
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, MarketingBudget FROM Albums"
        )

        for row in results:
            print("SingerId: {}, AlbumId: {}, MarketingBudget: {}".format(*row))


# [END spanner_postgresql_query_data_with_new_column]


# [START spanner_postgresql_create_index]
def add_index(instance_id, database_id):
    """Adds a simple index to the example database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    operation = database.update_ddl(
        ["CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)"]
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the AlbumsByAlbumTitle index.")


# [END spanner_postgresql_create_index]


# [START spanner_postgresql_read_data_with_index]
def read_data_with_index(instance_id, database_id):
    """Reads sample data from the database using an index.

    The index must exist before running this sample. You can add the index
    by running the `add_index` sample or by running this DDL statement against
    your database:

        CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)

    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        keyset = spanner.KeySet(all_=True)
        results = snapshot.read(
            table="Albums",
            columns=("AlbumId", "AlbumTitle"),
            keyset=keyset,
            index="AlbumsByAlbumTitle",
        )

        for row in results:
            print("AlbumId: {}, AlbumTitle: {}".format(*row))


# [END spanner_postgresql_read_data_with_index]


# [START spanner_postgresql_create_storing_index]
def add_storing_index(instance_id, database_id):
    """Adds an storing index to the example database."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "CREATE INDEX AlbumsByAlbumTitle2 ON Albums(AlbumTitle)"
            "INCLUDE (MarketingBudget)"
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the AlbumsByAlbumTitle2 index.")


# [END spanner_postgresql_create_storing_index]


# [START spanner_postgresql_read_data_with_storing_index]
def read_data_with_storing_index(instance_id, database_id):
    """Reads sample data from the database using an index with a storing
    clause.

    The index must exist before running this sample. You can add the index
    by running the `add_scoring_index` sample or by running this DDL statement
    against your database:

        CREATE INDEX AlbumsByAlbumTitle2 ON Albums(AlbumTitle)
        INCLUDE (MarketingBudget)

    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        keyset = spanner.KeySet(all_=True)
        results = snapshot.read(
            table="Albums",
            columns=("AlbumId", "AlbumTitle", "MarketingBudget"),
            keyset=keyset,
            index="AlbumsByAlbumTitle2",
        )

        for row in results:
            print("AlbumId: {}, AlbumTitle: {}, MarketingBudget: {}".format(*row))


# [END spanner_postgresql_read_data_with_storing_index]


# [START spanner_postgresql_read_only_transaction]
def read_only_transaction(instance_id, database_id):
    """Reads data inside of a read-only transaction.

    Within the read-only transaction, or "snapshot", the application sees
    consistent view of the database at a particular timestamp.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot(multi_use=True) as snapshot:
        # Read using SQL.
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, AlbumTitle FROM Albums"
        )

        print("Results from first read:")
        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))

        # Perform another read using the `read` method. Even if the data
        # is updated in-between the reads, the snapshot ensures that both
        # return the same data.
        keyset = spanner.KeySet(all_=True)
        results = snapshot.read(
            table="Albums", columns=("SingerId", "AlbumId", "AlbumTitle"), keyset=keyset
        )

        print("Results from second read:")
        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))


# [END spanner_postgresql_read_only_transaction]


def insert_with_dml(instance_id, database_id):
    """Inserts data with a DML statement into the database."""
    # [START spanner_postgresql_dml_getting_started_insert]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_singers(transaction):
        row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) VALUES "
            "(12, 'Melissa', 'Garcia'), "
            "(13, 'Russell', 'Morales'), "
            "(14, 'Jacqueline', 'Long'), "
            "(15, 'Dylan', 'Shaw')"
        )
        print("{} record(s) inserted.".format(row_ct))

    database.run_in_transaction(insert_singers)
    # [END spanner_postgresql_dml_getting_started_insert]


def insert_with_dml_returning(instance_id, database_id):
    """Inserts sample data into the given database using a DML statement having a RETURNING clause."""
    # [START spanner_postgresql_dml_insert_returning]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Insert records into the SINGERS table and returns the
    # generated column FullName of the inserted records using
    # 'RETURNING FullName'.
    # It is also possible to return all columns of all the
    # inserted records by using 'RETURNING *'.
    def insert_singers(transaction):
        results = transaction.execute_sql(
            "INSERT INTO Singers (SingerId, FirstName, LastName) VALUES "
            "(21, 'Luann', 'Chizoba'), "
            "(22, 'Denis', 'Patricio'), "
            "(23, 'Felxi', 'Ronan'), "
            "(24, 'Dominik', 'Martyna') "
            "RETURNING FullName"
        )
        for result in results:
            print("FullName: {}".format(*result))
        print("{} record(s) inserted.".format(results.stats.row_count_exact))

    database.run_in_transaction(insert_singers)
    # [END spanner_postgresql_dml_insert_returning]


def query_data_with_parameter(instance_id, database_id):
    """Queries sample data from the database using SQL with a parameter."""
    # [START spanner_postgresql_query_with_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, FirstName, LastName FROM Singers WHERE LastName = $1",
            params={"p1": "Garcia"},
            param_types={"p1": spanner.param_types.STRING},
        )

        for row in results:
            print("SingerId: {}, FirstName: {}, LastName: {}".format(*row))
    # [END spanner_postgresql_query_with_parameter]


def write_with_dml_transaction(instance_id, database_id):
    """Transfers part of a marketing budget from one album to another."""
    # [START spanner_postgresql_dml_getting_started_update]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def transfer_budget(transaction):
        # Transfer marketing budget from one album to another. Performed in a
        # single transaction to ensure that the transfer is atomic.
        second_album_result = transaction.execute_sql(
            "SELECT MarketingBudget from Albums WHERE SingerId = 2 and AlbumId = 2"
        )
        second_album_row = list(second_album_result)[0]
        second_album_budget = second_album_row[0]

        transfer_amount = 200000

        # Transaction will only be committed if this condition still holds at
        # the time of commit. Otherwise it will be aborted and the callable
        # will be rerun by the client library
        if second_album_budget >= transfer_amount:
            first_album_result = transaction.execute_sql(
                "SELECT MarketingBudget from Albums WHERE SingerId = 1 and AlbumId = 1"
            )
            first_album_row = list(first_album_result)[0]
            first_album_budget = first_album_row[0]

            second_album_budget -= transfer_amount
            first_album_budget += transfer_amount

            # Update first album
            transaction.execute_update(
                "UPDATE Albums "
                "SET MarketingBudget = $1 "
                "WHERE SingerId = 1 and AlbumId = 1",
                params={"p1": first_album_budget},
                param_types={"p1": spanner.param_types.INT64},
            )

            # Update second album
            transaction.execute_update(
                "UPDATE Albums "
                "SET MarketingBudget = $1 "
                "WHERE SingerId = 2 and AlbumId = 2",
                params={"p1": second_album_budget},
                param_types={"p1": spanner.param_types.INT64},
            )

            print(
                "Transferred {} from Album2's budget to Album1's".format(
                    transfer_amount
                )
            )

    database.run_in_transaction(transfer_budget)
    # [END spanner_postgresql_dml_getting_started_update]


# [START spanner_postgresql_read_stale_data]
def read_stale_data(instance_id, database_id):
    """Reads sample data from the database. The data is exactly 15 seconds
    stale."""
    import datetime

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    staleness = datetime.timedelta(seconds=15)

    with database.snapshot(exact_staleness=staleness) as snapshot:
        keyset = spanner.KeySet(all_=True)
        results = snapshot.read(
            table="Albums",
            columns=("SingerId", "AlbumId", "MarketingBudget"),
            keyset=keyset,
        )

        for row in results:
            print("SingerId: {}, AlbumId: {}, MarketingBudget: {}".format(*row))


# [END spanner_postgresql_read_stale_data]


# [START spanner_postgresql_update_data_with_timestamp_column]
def update_data_with_timestamp(instance_id, database_id):
    """Updates Performances tables in the database with the COMMIT_TIMESTAMP
    column.

    This updates the `MarketingBudget` column which must be created before
    running this sample. You can add the column by running the `add_column`
    sample or by running this DDL statement against your database:

        ALTER TABLE Albums ADD COLUMN MarketingBudget BIGINT

    In addition this update expects the LastUpdateTime column added by
    applying this DDL statement against your database:

        ALTER TABLE Albums ADD COLUMN LastUpdateTime SPANNER.COMMIT_TIMESTAMP
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    with database.batch() as batch:
        batch.update(
            table="Albums",
            columns=("SingerId", "AlbumId", "MarketingBudget", "LastUpdateTime"),
            values=[
                (1, 1, 1000000, spanner.COMMIT_TIMESTAMP),
                (2, 2, 750000, spanner.COMMIT_TIMESTAMP),
            ],
        )

    print("Updated data.")


# [END spanner_postgresql_update_data_with_timestamp_column]


# [START spanner_postgresql_add_timestamp_column]
def add_timestamp_column(instance_id, database_id):
    """Adds a new TIMESTAMP column to the Albums table in the example database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    operation = database.update_ddl(
        ["ALTER TABLE Albums ADD COLUMN LastUpdateTime SPANNER.COMMIT_TIMESTAMP"]
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        'Altered table "Albums" on database {} on instance {}.'.format(
            database_id, instance_id
        )
    )


# [END spanner_postgresql_add_timestamp_column]


# [START spanner_postgresql_query_data_with_timestamp_column]
def query_data_with_timestamp(instance_id, database_id):
    """Queries sample data from the database using SQL.

    This updates the `LastUpdateTime` column which must be created before
    running this sample. You can add the column by running the
    `add_timestamp_column` sample or by running this DDL statement
    against your database:

        ALTER TABLE Performances ADD COLUMN LastUpdateTime TIMESTAMP
        OPTIONS (allow_commit_timestamp=true)

    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, MarketingBudget FROM Albums "
            "ORDER BY LastUpdateTime DESC"
        )

    for row in results:
        print("SingerId: {}, AlbumId: {}, MarketingBudget: {}".format(*row))


# [END spanner_postgresql_query_data_with_timestamp_column]


# [START spanner_postgresql_create_table_with_timestamp_column]
def create_table_with_timestamp(instance_id, database_id):
    """Creates a table with a COMMIT_TIMESTAMP column."""

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    request = spanner_admin_database_v1.UpdateDatabaseDdlRequest(
        database=database.name,
        statements=[
            """CREATE TABLE Performances (
  SingerId     BIGINT NOT NULL,
  VenueId      BIGINT NOT NULL,
  EventDate    Date,
  Revenue      BIGINT,
  LastUpdateTime SPANNER.COMMIT_TIMESTAMP NOT NULL,
PRIMARY KEY (SingerId, VenueId, EventDate))
INTERLEAVE IN PARENT Singers ON DELETE CASCADE"""
        ],
    )
    operation = spanner_client.database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created Performances table on database {} on instance {}".format(
            database_id, instance_id
        )
    )


# [END spanner_postgresql_create_table_with_timestamp_column]


# [START spanner_postgresql_insert_data_with_timestamp_column]
def insert_data_with_timestamp(instance_id, database_id):
    """Inserts data with a COMMIT_TIMESTAMP field into a table."""

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    with database.batch() as batch:
        batch.insert(
            table="Performances",
            columns=("SingerId", "VenueId", "EventDate", "Revenue", "LastUpdateTime"),
            values=[
                (1, 4, "2017-10-05", 11000, spanner.COMMIT_TIMESTAMP),
                (1, 19, "2017-11-02", 15000, spanner.COMMIT_TIMESTAMP),
                (2, 42, "2017-12-23", 7000, spanner.COMMIT_TIMESTAMP),
            ],
        )

    print("Inserted data.")


# [END spanner_postgresql_insert_data_with_timestamp_column]


def insert_data_with_dml(instance_id, database_id):
    """Inserts sample data into the given database using a DML statement."""
    # [START spanner_postgresql_dml_standard_insert]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_singers(transaction):
        row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            " VALUES (10, 'Virginia', 'Watson')"
        )

        print("{} record(s) inserted.".format(row_ct))

    database.run_in_transaction(insert_singers)
    # [END spanner_postgresql_dml_standard_insert]


def update_data_with_dml(instance_id, database_id):
    """Updates sample data from the database using a DML statement."""
    # [START spanner_postgresql_dml_standard_update]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def update_albums(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Albums "
            "SET MarketingBudget = MarketingBudget * 2 "
            "WHERE SingerId = 1 and AlbumId = 1"
        )

        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(update_albums)
    # [END spanner_postgresql_dml_standard_update]


def update_data_with_dml_returning(instance_id, database_id):
    """Updates sample data from the database using a DML statement having a RETURNING clause."""
    # [START spanner_postgresql_dml_update_returning]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Update MarketingBudget column for records satisfying
    # a particular condition and returns the modified
    # MarketingBudget column of the updated records using
    # 'RETURNING MarketingBudget'.
    # It is also possible to return all columns of all the
    # updated records by using 'RETURNING *'.
    def update_albums(transaction):
        results = transaction.execute_sql(
            "UPDATE Albums "
            "SET MarketingBudget = MarketingBudget * 2 "
            "WHERE SingerId = 1 and AlbumId = 1 "
            "RETURNING MarketingBudget"
        )
        for result in results:
            print("MarketingBudget: {}".format(*result))
        print("{} record(s) updated.".format(results.stats.row_count_exact))

    database.run_in_transaction(update_albums)
    # [END spanner_postgresql_dml_update_returning]


def delete_data_with_dml(instance_id, database_id):
    """Deletes sample data from the database using a DML statement."""
    # [START spanner_postgresql_dml_standard_delete]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def delete_singers(transaction):
        row_ct = transaction.execute_update(
            "DELETE FROM Singers WHERE FirstName = 'Alice'"
        )

        print("{} record(s) deleted.".format(row_ct))

    database.run_in_transaction(delete_singers)
    # [END spanner_postgresql_dml_standard_delete]


def delete_data_with_dml_returning(instance_id, database_id):
    """Deletes sample data from the database using a DML statement having a RETURNING clause."""
    # [START spanner_postgresql_dml_delete_returning]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Delete records from SINGERS table satisfying a
    # particular condition and returns the SingerId
    # and FullName column of the deleted records using
    # 'RETURNING SingerId, FullName'.
    # It is also possible to return all columns of all the
    # deleted records by using 'RETURNING *'.
    def delete_singers(transaction):
        results = transaction.execute_sql(
            "DELETE FROM Singers WHERE FirstName = 'David' RETURNING SingerId, FullName"
        )
        for result in results:
            print("SingerId: {}, FullName: {}".format(*result))
        print("{} record(s) deleted.".format(results.stats.row_count_exact))

    database.run_in_transaction(delete_singers)
    # [END spanner_postgresql_dml_delete_returning]


def dml_write_read_transaction(instance_id, database_id):
    """First inserts data then reads it from within a transaction using DML."""
    # [START spanner_postgresql_dml_write_then_read]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def write_then_read(transaction):
        # Insert record.
        row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            " VALUES (11, 'Timothy', 'Campbell')"
        )
        print("{} record(s) inserted.".format(row_ct))

        # Read newly inserted record.
        results = transaction.execute_sql(
            "SELECT FirstName, LastName FROM Singers WHERE SingerId = 11"
        )
        for result in results:
            print("FirstName: {}, LastName: {}".format(*result))

    database.run_in_transaction(write_then_read)
    # [END spanner_postgresql_dml_write_then_read]


def update_data_with_partitioned_dml(instance_id, database_id):
    """Update sample data with a partitioned DML statement."""
    # [START spanner_postgresql_dml_partitioned_update]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    row_ct = database.execute_partitioned_dml(
        "UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1"
    )

    print("{} records updated.".format(row_ct))
    # [END spanner_postgresql_dml_partitioned_update]


def delete_data_with_partitioned_dml(instance_id, database_id):
    """Delete sample data with a partitioned DML statement."""
    # [START spanner_postgresql_dml_partitioned_delete]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    row_ct = database.execute_partitioned_dml("DELETE FROM Singers WHERE SingerId > 10")

    print("{} record(s) deleted.".format(row_ct))
    # [END spanner_postgresql_dml_partitioned_delete]


def update_with_batch_dml(instance_id, database_id):
    """Updates sample data in the database using Batch DML."""
    # [START spanner_postgresql_dml_batch_update]
    from google.rpc.code_pb2 import OK

    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    insert_statement = (
        "INSERT INTO Albums "
        "(SingerId, AlbumId, AlbumTitle, MarketingBudget) "
        "VALUES (1, 3, 'Test Album Title', 10000)"
    )

    update_statement = (
        "UPDATE Albums "
        "SET MarketingBudget = MarketingBudget * 2 "
        "WHERE SingerId = 1 and AlbumId = 3"
    )

    def update_albums(transaction):
        status, row_cts = transaction.batch_update([insert_statement, update_statement])

        if status.code != OK:
            # Do handling here.
            # Note: the exception will still be raised when
            # `commit` is called by `run_in_transaction`.
            return

        print("Executed {} SQL statements using Batch DML.".format(len(row_cts)))

    database.run_in_transaction(update_albums)
    # [END spanner_postgresql_dml_batch_update]


def dml_last_statement_option(instance_id, database_id):
    """Inserts and updates using DML where the update sets the last statement option."""
    # [START spanner_postgresql_dml_last_statement]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_and_update_singers(transaction):
        insert_row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            "VALUES (54214, 'John', 'Do')"
        )

        print("{} record(s) inserted.".format(insert_row_ct))

        update_row_ct = transaction.execute_update(
            "UPDATE Singers SET LastName = 'Doe' WHERE SingerId = 54214",
            last_statement=True,
        )

        print("{} record(s) updated.".format(update_row_ct))

    database.run_in_transaction(insert_and_update_singers)
    # [END spanner_postgresql_dml_last_statement]


def create_table_with_datatypes(instance_id, database_id):
    """Creates a table with supported datatypes."""
    # [START spanner_postgresql_create_table_with_datatypes]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            """CREATE TABLE Venues (
  VenueId         BIGINT NOT NULL,
  VenueName       character varying(100),
  VenueInfo       BYTEA,
  Capacity        BIGINT,
  OutdoorVenue    BOOL,
  PopularityScore FLOAT8,
  Revenue         NUMERIC,
  LastUpdateTime  SPANNER.COMMIT_TIMESTAMP NOT NULL,
  PRIMARY KEY (VenueId))"""
        ],
    )
    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created Venues table on database {} on instance {}".format(
            database_id, instance_id
        )
    )
    # [END spanner_postgresql_create_table_with_datatypes]


def insert_datatypes_data(instance_id, database_id):
    """Inserts data with supported datatypes into a table."""
    # [START spanner_postgresql_insert_datatypes_data]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleBytes1 = base64.b64encode("Hello World 1".encode())
    exampleBytes2 = base64.b64encode("Hello World 2".encode())
    exampleBytes3 = base64.b64encode("Hello World 3".encode())
    with database.batch() as batch:
        batch.insert(
            table="Venues",
            columns=(
                "VenueId",
                "VenueName",
                "VenueInfo",
                "Capacity",
                "OutdoorVenue",
                "PopularityScore",
                "Revenue",
                "LastUpdateTime",
            ),
            values=[
                (
                    4,
                    "Venue 4",
                    exampleBytes1,
                    1800,
                    False,
                    0.85543,
                    decimal.Decimal("215100.10"),
                    spanner.COMMIT_TIMESTAMP,
                ),
                (
                    19,
                    "Venue 19",
                    exampleBytes2,
                    6300,
                    True,
                    0.98716,
                    decimal.Decimal("1200100.00"),
                    spanner.COMMIT_TIMESTAMP,
                ),
                (
                    42,
                    "Venue 42",
                    exampleBytes3,
                    3000,
                    False,
                    0.72598,
                    decimal.Decimal("390650.99"),
                    spanner.COMMIT_TIMESTAMP,
                ),
            ],
        )

    print("Inserted data.")
    # [END spanner_postgresql_insert_datatypes_data]


def query_data_with_bool(instance_id, database_id):
    """Queries sample data using SQL with a BOOL parameter."""
    # [START spanner_postgresql_query_with_bool_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleBool = True
    param = {"p1": exampleBool}
    param_type = {"p1": param_types.BOOL}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, OutdoorVenue FROM Venues "
            "WHERE OutdoorVenue = $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, OutdoorVenue: {}".format(*row))
    # [END spanner_postgresql_query_with_bool_parameter]


def query_data_with_bytes(instance_id, database_id):
    """Queries sample data using SQL with a BYTES parameter."""
    # [START spanner_postgresql_query_with_bytes_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleBytes = base64.b64encode("Hello World 1".encode())
    param = {"p1": exampleBytes}
    param_type = {"p1": param_types.BYTES}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName FROM Venues WHERE VenueInfo = $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}".format(*row))
    # [END spanner_postgresql_query_with_bytes_parameter]


def query_data_with_float(instance_id, database_id):
    """Queries sample data using SQL with a FLOAT8 parameter."""
    # [START spanner_postgresql_query_with_float_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleFloat = 0.8
    param = {"p1": exampleFloat}
    param_type = {"p1": param_types.FLOAT64}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, PopularityScore FROM Venues "
            "WHERE PopularityScore > $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, PopularityScore: {}".format(*row))
    # [END spanner_postgresql_query_with_float_parameter]


def query_data_with_int(instance_id, database_id):
    """Queries sample data using SQL with a BIGINT parameter."""
    # [START spanner_postgresql_query_with_int_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleInt = 3000
    param = {"p1": exampleInt}
    param_type = {"p1": param_types.INT64}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, Capacity FROM Venues WHERE Capacity >= $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, Capacity: {}".format(*row))
    # [END spanner_postgresql_query_with_int_parameter]


def query_data_with_string(instance_id, database_id):
    """Queries sample data using SQL with a STRING parameter."""
    # [START spanner_postgresql_query_with_string_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleString = "Venue 42"
    param = {"p1": exampleString}
    param_type = {"p1": param_types.STRING}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName FROM Venues WHERE VenueName = $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}".format(*row))
    # [END spanner_postgresql_query_with_string_parameter]


def query_data_with_timestamp_parameter(instance_id, database_id):
    """Queries sample data using SQL with a TIMESTAMPTZ parameter."""
    # [START spanner_postgresql_query_with_timestamp_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    example_timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    # [END spanner_postgresql_query_with_timestamp_parameter]
    # Avoid time drift on the local machine.
    # https://github.com/GoogleCloudPlatform/python-docs-samples/issues/4197.
    example_timestamp = (
        datetime.datetime.utcnow() + datetime.timedelta(days=1)
    ).isoformat() + "Z"
    # [START spanner_postgresql_query_with_timestamp_parameter]
    param = {"p1": example_timestamp}
    param_type = {"p1": param_types.TIMESTAMP}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, LastUpdateTime FROM Venues "
            "WHERE LastUpdateTime < $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, LastUpdateTime: {}".format(*row))
    # [END spanner_postgresql_query_with_timestamp_parameter]


# [START spanner_postgresql_update_data_with_numeric_column]
def update_data_with_numeric(instance_id, database_id):
    """Updates Venues tables in the database with the NUMERIC
    column.

    This updates the `Revenue` column which must be created before
    running this sample. You can add the column by running the
    `add_numeric_column` sample or by running this DDL statement
     against your database:

        ALTER TABLE Venues ADD COLUMN Revenue NUMERIC
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    with database.batch() as batch:
        batch.update(
            table="Venues",
            columns=("VenueId", "Revenue"),
            values=[
                (4, decimal.Decimal("35000")),
                (19, decimal.Decimal("104500")),
                (42, decimal.Decimal("99999999999999999999999999999.99")),
            ],
        )

    print("Updated data.")


# [END spanner_postgresql_update_data_with_numeric_column]


def query_data_with_numeric_parameter(instance_id, database_id):
    """Queries sample data using SQL with a NUMERIC parameter."""
    # [START spanner_postgresql_query_with_numeric_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    example_numeric = decimal.Decimal("300000")
    param = {"p1": example_numeric}
    param_type = {"p1": param_types.PG_NUMERIC}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, Revenue FROM Venues WHERE Revenue < $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, Revenue: {}".format(*row))
    # [END spanner_postgresql_query_with_numeric_parameter]


def create_client_with_query_options(instance_id, database_id):
    """Create a client with query options."""
    # [START spanner_postgresql_create_client_with_query_options]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client(
        query_options={
            "optimizer_version": "1",
            "optimizer_statistics_package": "latest",
        }
    )
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, LastUpdateTime FROM Venues"
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, LastUpdateTime: {}".format(*row))
    # [END spanner_postgresql_create_client_with_query_options]


def query_data_with_query_options(instance_id, database_id):
    """Queries sample data using SQL with query options."""
    # [START spanner_postgresql_query_with_query_options]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, LastUpdateTime FROM Venues",
            query_options={
                "optimizer_version": "1",
                "optimizer_statistics_package": "latest",
            },
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, LastUpdateTime: {}".format(*row))
    # [END spanner_postgresql_query_with_query_options]


# [START spanner_postgresql_jsonb_add_column]
def add_jsonb_column(instance_id, database_id):
    """
    Alters Venues tables in the database adding a JSONB column.
    You can create the table by running the `create_table_with_datatypes`
    sample or by running this DDL statement against your database:
    CREATE TABLE Venues (
      VenueId         BIGINT NOT NULL,
      VenueName       character varying(100),
      VenueInfo       BYTEA,
      Capacity        BIGINT,
      OutdoorVenue    BOOL,
      PopularityScore FLOAT8,
      Revenue         NUMERIC,
      LastUpdateTime  SPANNER.COMMIT_TIMESTAMP NOT NULL,
      PRIMARY KEY (VenueId))
    """
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=["ALTER TABLE Venues ADD COLUMN VenueDetails JSONB"],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        'Altered table "Venues" on database {} on instance {}.'.format(
            database_id, instance_id
        )
    )


# [END spanner_postgresql_jsonb_add_column]


# [START spanner_postgresql_jsonb_update_data]
def update_data_with_jsonb(instance_id, database_id):
    """Updates Venues tables in the database with the JSONB
    column.
    This updates the `VenueDetails` column which must be created before
    running this sample. You can add the column by running the
    `add_jsonb_column` sample or by running this DDL statement
     against your database:
        ALTER TABLE Venues ADD COLUMN VenueDetails JSONB
    """
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    """
    PG JSONB takes the last value in the case of duplicate keys.
    PG JSONB sorts first by key length and then lexicographically with
    equivalent key length.
    """

    with database.batch() as batch:
        batch.update(
            table="Venues",
            columns=("VenueId", "VenueDetails"),
            values=[
                (
                    4,
                    JsonObject(
                        [
                            JsonObject({"name": None, "open": True}),
                            JsonObject({"name": "room 2", "open": False}),
                        ]
                    ),
                ),
                (19, JsonObject(rating=9, open=True)),
                (
                    42,
                    JsonObject(
                        {
                            "name": None,
                            "open": {"Monday": True, "Tuesday": False},
                            "tags": ["large", "airy"],
                        }
                    ),
                ),
            ],
        )

    print("Updated data.")


# [END spanner_postgresql_jsonb_update_data]


# [START spanner_postgresql_jsonb_query_parameter]
def query_data_with_jsonb_parameter(instance_id, database_id):
    """Queries sample data using SQL with a JSONB parameter."""
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    param = {"p1": 2}
    param_type = {"p1": param_types.INT64}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT venueid, venuedetails FROM Venues"
            + " WHERE CAST(venuedetails ->> 'rating' AS INTEGER) > $1",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueDetails: {}".format(*row))


# [END spanner_postgresql_jsonb_query_parameter]


# [START spanner_postgresql_create_sequence]
def create_sequence(instance_id, database_id):
    """Creates the Sequence and insert data"""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "CREATE SEQUENCE Seq BIT_REVERSED_POSITIVE",
            """CREATE TABLE Customers (
        CustomerId  BIGINT DEFAULT nextval('Seq'),
        CustomerName  character varying(1024),
        PRIMARY KEY (CustomerId)
        )""",
        ],
    )
    operation = database_admin_api.update_database_ddl(request)
    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created Seq sequence and Customers table, where the key column CustomerId uses the sequence as a default value on database {} on instance {}".format(
            database_id, instance_id
        )
    )

    def insert_customers(transaction):
        results = transaction.execute_sql(
            "INSERT INTO Customers (CustomerName) VALUES "
            "('Alice'), "
            "('David'), "
            "('Marc') "
            "RETURNING CustomerId"
        )
        for result in results:
            print("Inserted customer record with Customer Id: {}".format(*result))
        print(
            "Number of customer records inserted is {}".format(
                results.stats.row_count_exact
            )
        )

    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    database.run_in_transaction(insert_customers)


# [END spanner_postgresql_create_sequence]


# [START spanner_postgresql_alter_sequence]
def alter_sequence(instance_id, database_id):
    """Alters the Sequence and insert data"""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=["ALTER SEQUENCE Seq SKIP RANGE 1000 5000000"],
    )
    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Altered Seq sequence to skip an inclusive range between 1000 and 5000000 on database {} on instance {}".format(
            database_id, instance_id
        )
    )

    def insert_customers(transaction):
        results = transaction.execute_sql(
            "INSERT INTO Customers (CustomerName) VALUES "
            "('Lea'), "
            "('Cataline'), "
            "('Smith') "
            "RETURNING CustomerId"
        )
        for result in results:
            print("Inserted customer record with Customer Id: {}".format(*result))
        print(
            "Number of customer records inserted is {}".format(
                results.stats.row_count_exact
            )
        )

    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    database.run_in_transaction(insert_customers)


# [END spanner_postgresql_alter_sequence]


# [START spanner_postgresql_drop_sequence]
def drop_sequence(instance_id, database_id):
    """Drops the Sequence"""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "ALTER TABLE Customers ALTER COLUMN CustomerId DROP DEFAULT",
            "DROP SEQUENCE Seq",
        ],
    )
    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Altered Customers table to drop DEFAULT from CustomerId column and dropped the Seq sequence on database {} on instance {}".format(
            database_id, instance_id
        )
    )


# [END spanner_postgresql_drop_sequence]

if __name__ == "__main__":  # noqa: C901
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("instance_id", help="Your Cloud Spanner instance ID.")
    parser.add_argument(
        "--database-id", help="Your Cloud Spanner database ID.", default="example_db"
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("create_instance", help=create_instance.__doc__)
    subparsers.add_parser("create_database", help=create_database.__doc__)
    subparsers.add_parser("insert_data", help=insert_data.__doc__)
    subparsers.add_parser("delete_data", help=delete_data.__doc__)
    subparsers.add_parser("query_data", help=query_data.__doc__)
    subparsers.add_parser("read_data", help=read_data.__doc__)
    subparsers.add_parser("read_stale_data", help=read_stale_data.__doc__)
    subparsers.add_parser("add_column", help=add_column.__doc__)
    subparsers.add_parser("update_data", help=update_data.__doc__)
    subparsers.add_parser(
        "query_data_with_new_column", help=query_data_with_new_column.__doc__
    )
    subparsers.add_parser("read_write_transaction", help=read_write_transaction.__doc__)
    subparsers.add_parser("read_only_transaction", help=read_only_transaction.__doc__)
    subparsers.add_parser("add_index", help=add_index.__doc__)
    subparsers.add_parser("read_data_with_index", help=read_data_with_index.__doc__)
    subparsers.add_parser("add_storing_index", help=add_storing_index.__doc__)
    subparsers.add_parser(
        "read_data_with_storing_index", help=read_data_with_storing_index.__doc__
    )
    subparsers.add_parser(
        "create_table_with_timestamp", help=create_table_with_timestamp.__doc__
    )
    subparsers.add_parser(
        "insert_data_with_timestamp", help=insert_data_with_timestamp.__doc__
    )
    subparsers.add_parser("add_timestamp_column", help=add_timestamp_column.__doc__)
    subparsers.add_parser(
        "update_data_with_timestamp", help=update_data_with_timestamp.__doc__
    )
    subparsers.add_parser(
        "query_data_with_timestamp", help=query_data_with_timestamp.__doc__
    )
    subparsers.add_parser("insert_data_with_dml", help=insert_data_with_dml.__doc__)
    subparsers.add_parser("update_data_with_dml", help=update_data_with_dml.__doc__)
    subparsers.add_parser(
        "update_data_with_dml_returning", help=update_data_with_dml_returning.__doc__
    )
    subparsers.add_parser("delete_data_with_dml", help=delete_data_with_dml.__doc__)
    subparsers.add_parser(
        "delete_data_with_dml_returning", help=delete_data_with_dml_returning.__doc__
    )
    subparsers.add_parser(
        "dml_write_read_transaction", help=dml_write_read_transaction.__doc__
    )
    subparsers.add_parser("insert_with_dml", help=insert_with_dml.__doc__)
    subparsers.add_parser(
        "insert_with_dml_returning", help=insert_with_dml_returning.__doc__
    )
    subparsers.add_parser(
        "query_data_with_parameter", help=query_data_with_parameter.__doc__
    )
    subparsers.add_parser(
        "write_with_dml_transaction", help=write_with_dml_transaction.__doc__
    )
    subparsers.add_parser(
        "update_data_with_partitioned_dml",
        help=update_data_with_partitioned_dml.__doc__,
    )
    subparsers.add_parser(
        "delete_data_with_partitioned_dml",
        help=delete_data_with_partitioned_dml.__doc__,
    )
    subparsers.add_parser("update_with_batch_dml", help=update_with_batch_dml.__doc__)
    subparsers.add_parser(
        "dml_last_statement_option", help=dml_last_statement_option.__doc__
    )
    subparsers.add_parser(
        "create_table_with_datatypes", help=create_table_with_datatypes.__doc__
    )
    subparsers.add_parser("insert_datatypes_data", help=insert_datatypes_data.__doc__)
    subparsers.add_parser("query_data_with_bool", help=query_data_with_bool.__doc__)
    subparsers.add_parser("query_data_with_bytes", help=query_data_with_bytes.__doc__)
    subparsers.add_parser("query_data_with_float", help=query_data_with_float.__doc__)
    subparsers.add_parser("query_data_with_int", help=query_data_with_int.__doc__)
    subparsers.add_parser("query_data_with_string", help=query_data_with_string.__doc__)
    subparsers.add_parser(
        "query_data_with_timestamp_parameter",
        help=query_data_with_timestamp_parameter.__doc__,
    )
    subparsers.add_parser(
        "update_data_with_numeric",
        help=update_data_with_numeric.__doc__,
    )
    subparsers.add_parser(
        "query_data_with_numeric_parameter",
        help=query_data_with_numeric_parameter.__doc__,
    )
    subparsers.add_parser(
        "query_data_with_query_options", help=query_data_with_query_options.__doc__
    )
    subparsers.add_parser(
        "create_client_with_query_options",
        help=create_client_with_query_options.__doc__,
    )
    subparsers.add_parser("create_sequence", help=create_sequence.__doc__)
    subparsers.add_parser("alter_sequence", help=alter_sequence.__doc__)
    subparsers.add_parser("drop_sequence", help=drop_sequence.__doc__)

    args = parser.parse_args()

    if args.command == "create_instance":
        create_instance(args.instance_id)
    elif args.command == "create_database":
        create_database(args.instance_id, args.database_id)
    elif args.command == "insert_data":
        insert_data(args.instance_id, args.database_id)
    elif args.command == "delete_data":
        delete_data(args.instance_id, args.database_id)
    elif args.command == "query_data":
        query_data(args.instance_id, args.database_id)
    elif args.command == "read_data":
        read_data(args.instance_id, args.database_id)
    elif args.command == "read_stale_data":
        read_stale_data(args.instance_id, args.database_id)
    elif args.command == "add_column":
        add_column(args.instance_id, args.database_id)
    elif args.command == "update_data":
        update_data(args.instance_id, args.database_id)
    elif args.command == "query_data_with_new_column":
        query_data_with_new_column(args.instance_id, args.database_id)
    elif args.command == "read_write_transaction":
        read_write_transaction(args.instance_id, args.database_id)
    elif args.command == "read_only_transaction":
        read_only_transaction(args.instance_id, args.database_id)
    elif args.command == "add_index":
        add_index(args.instance_id, args.database_id)
    elif args.command == "read_data_with_index":
        read_data_with_index(args.instance_id, args.database_id)
    elif args.command == "add_storing_index":
        add_storing_index(args.instance_id, args.database_id)
    elif args.command == "read_data_with_storing_index":
        read_data_with_storing_index(args.instance_id, args.database_id)
    elif args.command == "create_table_with_timestamp":
        create_table_with_timestamp(args.instance_id, args.database_id)
    elif args.command == "insert_data_with_timestamp":
        insert_data_with_timestamp(args.instance_id, args.database_id)
    elif args.command == "add_timestamp_column":
        add_timestamp_column(args.instance_id, args.database_id)
    elif args.command == "update_data_with_timestamp":
        update_data_with_timestamp(args.instance_id, args.database_id)
    elif args.command == "query_data_with_timestamp":
        query_data_with_timestamp(args.instance_id, args.database_id)
    elif args.command == "insert_data_with_dml":
        insert_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "update_data_with_dml":
        update_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "update_data_with_dml_returning":
        update_data_with_dml_returning(args.instance_id, args.database_id)
    elif args.command == "delete_data_with_dml":
        delete_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "delete_data_with_dml_returning":
        delete_data_with_dml_returning(args.instance_id, args.database_id)
    elif args.command == "dml_write_read_transaction":
        dml_write_read_transaction(args.instance_id, args.database_id)
    elif args.command == "insert_with_dml":
        insert_with_dml(args.instance_id, args.database_id)
    elif args.command == "insert_with_dml_returning":
        insert_with_dml_returning(args.instance_id, args.database_id)
    elif args.command == "query_data_with_parameter":
        query_data_with_parameter(args.instance_id, args.database_id)
    elif args.command == "write_with_dml_transaction":
        write_with_dml_transaction(args.instance_id, args.database_id)
    elif args.command == "update_data_with_partitioned_dml":
        update_data_with_partitioned_dml(args.instance_id, args.database_id)
    elif args.command == "delete_data_with_partitioned_dml":
        delete_data_with_partitioned_dml(args.instance_id, args.database_id)
    elif args.command == "update_with_batch_dml":
        update_with_batch_dml(args.instance_id, args.database_id)
    elif args.command == "dml_last_statement_option":
        dml_last_statement_option(args.instance_id, args.database_id)
    elif args.command == "create_table_with_datatypes":
        create_table_with_datatypes(args.instance_id, args.database_id)
    elif args.command == "insert_datatypes_data":
        insert_datatypes_data(args.instance_id, args.database_id)
    elif args.command == "query_data_with_bool":
        query_data_with_bool(args.instance_id, args.database_id)
    elif args.command == "query_data_with_bytes":
        query_data_with_bytes(args.instance_id, args.database_id)
    elif args.command == "query_data_with_float":
        query_data_with_float(args.instance_id, args.database_id)
    elif args.command == "query_data_with_int":
        query_data_with_int(args.instance_id, args.database_id)
    elif args.command == "query_data_with_string":
        query_data_with_string(args.instance_id, args.database_id)
    elif args.command == "query_data_with_timestamp_parameter":
        query_data_with_timestamp_parameter(args.instance_id, args.database_id)
    elif args.command == "update_data_with_numeric":
        update_data_with_numeric(args.instance_id, args.database_id)
    elif args.command == "query_data_with_numeric_parameter":
        query_data_with_numeric_parameter(args.instance_id, args.database_id)
    elif args.command == "query_data_with_query_options":
        query_data_with_query_options(args.instance_id, args.database_id)
    elif args.command == "create_client_with_query_options":
        create_client_with_query_options(args.instance_id, args.database_id)
