#!/usr/bin/env python

# Copyright 2016 Google, Inc.
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
Spanner.

For more information, see the README.rst under /spanner.
"""

import argparse
import base64
import datetime
import decimal
import json
import logging
import time

from google.cloud import spanner
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
from google.cloud.spanner_v1 import DirectedReadOptions, param_types
from google.cloud.spanner_v1.data_types import JsonObject
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore

from testdata import singer_pb2

OPERATION_TIMEOUT_SECONDS = 240


# [START spanner_create_instance]
def create_instance(instance_id):
    """Creates an instance."""
    from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin

    spanner_client = spanner.Client()

    config_name = "{}/instanceConfigs/regional-us-central1".format(
        spanner_client.project_name
    )

    operation = spanner_client.instance_admin_api.create_instance(
        parent=spanner_client.project_name,
        instance_id=instance_id,
        instance=spanner_instance_admin.Instance(
            config=config_name,
            display_name="This is a display name.",
            node_count=1,
            labels={
                "cloud_spanner_samples": "true",
                "sample_name": "snippets-create_instance-explicit",
                "created": str(int(time.time())),
            },
            edition=spanner_instance_admin.Instance.Edition.STANDARD,  # Optional
        ),
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created instance {}".format(instance_id))


# [END spanner_create_instance]


# [START spanner_update_instance]
def update_instance(instance_id):
    """Updates an instance."""
    from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin

    spanner_client = spanner.Client()

    name = "{}/instances/{}".format(spanner_client.project_name, instance_id)

    operation = spanner_client.instance_admin_api.update_instance(
        instance=spanner_instance_admin.Instance(
            name=name,
            labels={
                "sample_name": "snippets-update_instance-explicit",
            },
            edition=spanner_instance_admin.Instance.Edition.ENTERPRISE,  # Optional
        ),
        field_mask=field_mask_pb2.FieldMask(paths=["labels", "edition"]),
    )

    print("Waiting for operation to complete...")
    operation.result(900)

    print("Updated instance {}".format(instance_id))


# [END spanner_update_instance]


# [START spanner_create_instance_with_processing_units]
def create_instance_with_processing_units(instance_id, processing_units):
    """Creates an instance."""
    from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin

    spanner_client = spanner.Client()

    config_name = "{}/instanceConfigs/regional-us-central1".format(
        spanner_client.project_name
    )

    request = spanner_instance_admin.CreateInstanceRequest(
        parent=spanner_client.project_name,
        instance_id=instance_id,
        instance=spanner_instance_admin.Instance(
            config=config_name,
            display_name="This is a display name.",
            processing_units=processing_units,
            labels={
                "cloud_spanner_samples": "true",
                "sample_name": "snippets-create_instance_with_processing_units",
                "created": str(int(time.time())),
            },
            edition=spanner_instance_admin.Instance.Edition.ENTERPRISE_PLUS,
        ),
    )

    operation = spanner_client.instance_admin_api.create_instance(request=request)

    print("Waiting for operation to complete...")
    instance = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created instance {} with {} processing units".format(
            instance_id, instance.processing_units
        )
    )


# [END spanner_create_instance_with_processing_units]


# [START spanner_get_instance_config]
def get_instance_config(instance_config):
    """Gets the leader options for the instance configuration."""
    spanner_client = spanner.Client()
    config_name = "{}/instanceConfigs/{}".format(
        spanner_client.project_name, instance_config
    )
    config = spanner_client.instance_admin_api.get_instance_config(name=config_name)
    print(
        "Available leader options for instance config {}: {}".format(
            instance_config, config.leader_options
        )
    )


# [END spanner_get_instance_config]


# [START spanner_list_instance_configs]
def list_instance_config():
    """Lists the available instance configurations."""
    from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin

    spanner_client = spanner.Client()

    request = spanner_instance_admin.ListInstanceConfigsRequest(
        parent=spanner_client.project_name
    )
    for config in spanner_client.instance_admin_api.list_instance_configs(
        request=request
    ):
        print(
            "Available leader options for instance config {}: {}".format(
                config.name, config.leader_options
            )
        )


# [END spanner_list_instance_configs]


# [START spanner_create_instance_partition]
def create_instance_partition(instance_id, instance_partition_id):
    """Creates an instance partition."""
    from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin

    spanner_client = spanner.Client()
    instance_admin_api = spanner_client.instance_admin_api

    config_name = "{}/instanceConfigs/nam3".format(spanner_client.project_name)

    operation = spanner_client.instance_admin_api.create_instance_partition(
        parent=instance_admin_api.instance_path(spanner_client.project, instance_id),
        instance_partition_id=instance_partition_id,
        instance_partition=spanner_instance_admin.InstancePartition(
            config=config_name,
            display_name="Test instance partition",
            node_count=1,
        ),
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created instance partition {}".format(instance_partition_id))


# [END spanner_create_instance_partition]


# [START spanner_list_databases]
def list_databases(instance_id):
    """Lists databases and their leader options."""
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.ListDatabasesRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id)
    )

    for database in database_admin_api.list_databases(request=request):
        print(
            "Database {} has default leader {}".format(
                database.name, database.default_leader
            )
        )


# [END spanner_list_databases]


# [START spanner_create_database]
def create_database(instance_id, database_id):
    """Creates a database and tables for sample data."""
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f"CREATE DATABASE `{database_id}`",
        extra_statements=[
            """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX),
            FullName   STRING(2048) AS (
                ARRAY_TO_STRING([FirstName, LastName], " ")
            ) STORED
        ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
        ],
    )

    operation = database_admin_api.create_database(request=request)

    print("Waiting for operation to complete...")
    database = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created database {} on instance {}".format(
            database.name,
            database_admin_api.instance_path(spanner_client.project, instance_id),
        )
    )


# [END spanner_create_database]


# [START spanner_update_database]
def update_database(instance_id, database_id):
    """Updates the drop protection setting for a database."""
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseRequest(
        database=spanner_database_admin.Database(
            name=database_admin_api.database_path(
                spanner_client.project, instance_id, database_id
            ),
            enable_drop_protection=True,
        ),
        update_mask={"paths": ["enable_drop_protection"]},
    )
    operation = database_admin_api.update_database(request=request)
    print(
        "Waiting for update operation for {}/databases/{} to complete...".format(
            database_admin_api.instance_path(spanner_client.project, instance_id),
            database_id,
        )
    )
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Updated database {}/databases/{}.".format(
            database_admin_api.instance_path(spanner_client.project, instance_id),
            database_id,
        )
    )


# [END spanner_update_database]


# [START spanner_create_database_with_encryption_key]
def create_database_with_encryption_key(instance_id, database_id, kms_key_name):
    """Creates a database with tables using a Customer Managed Encryption Key (CMEK)."""
    from google.cloud.spanner_admin_database_v1 import EncryptionConfig
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f"CREATE DATABASE `{database_id}`",
        extra_statements=[
            """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX)
        ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
        ],
        encryption_config=EncryptionConfig(kms_key_name=kms_key_name),
    )

    operation = database_admin_api.create_database(request=request)

    print("Waiting for operation to complete...")
    database = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Database {} created with encryption key {}".format(
            database.name, database.encryption_config.kms_key_name
        )
    )


# [END spanner_create_database_with_encryption_key]


# [START spanner_create_database_with_MR_CMEK]
def create_database_with_multiple_kms_keys(instance_id, database_id, kms_key_names):
    """Creates a database with tables using multiple KMS keys(CMEK)."""
    from google.cloud.spanner_admin_database_v1 import EncryptionConfig
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f"CREATE DATABASE `{database_id}`",
        extra_statements=[
            """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX)
        ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
        ],
        encryption_config=EncryptionConfig(kms_key_names=kms_key_names),
    )

    operation = database_admin_api.create_database(request=request)

    print("Waiting for operation to complete...")
    database = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Database {} created with multiple KMS keys {}".format(
            database.name, database.encryption_config.kms_key_names
        )
    )


# [END spanner_create_database_with_MR_CMEK]


# [START spanner_create_database_with_default_leader]
def create_database_with_default_leader(instance_id, database_id, default_leader):
    """Creates a database with tables with a default leader."""
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f"CREATE DATABASE `{database_id}`",
        extra_statements=[
            """CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
                SingerId     INT64 NOT NULL,
                AlbumId      INT64 NOT NULL,
                AlbumTitle   STRING(MAX)
            ) PRIMARY KEY (SingerId, AlbumId),
            INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
            "ALTER DATABASE {} SET OPTIONS (default_leader = '{}')".format(
                database_id, default_leader
            ),
        ],
    )
    operation = database_admin_api.create_database(request=request)

    print("Waiting for operation to complete...")
    database = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Database {} created with default leader {}".format(
            database.name, database.default_leader
        )
    )


# [END spanner_create_database_with_default_leader]


# [START spanner_update_database_with_default_leader]
def update_database_with_default_leader(instance_id, database_id, default_leader):
    """Updates a database with tables with a default leader."""
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "ALTER DATABASE {} SET OPTIONS (default_leader = '{}')".format(
                database_id, default_leader
            )
        ],
    )
    operation = database_admin_api.update_database_ddl(request)

    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Database {} updated with default leader {}".format(database_id, default_leader)
    )


# [END spanner_update_database_with_default_leader]


# [START spanner_get_database_ddl]
def get_database_ddl(instance_id, database_id):
    """Gets the database DDL statements."""
    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api
    ddl = database_admin_api.get_database_ddl(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        )
    )
    print("Retrieved database DDL for {}".format(database_id))
    for statement in ddl.statements:
        print(statement)


# [END spanner_get_database_ddl]


# [START spanner_query_information_schema_database_options]
def query_information_schema_database_options(instance_id, database_id):
    """Queries the default leader of a database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT OPTION_VALUE AS default_leader "
            "FROM INFORMATION_SCHEMA.DATABASE_OPTIONS "
            "WHERE SCHEMA_NAME = '' AND OPTION_NAME = 'default_leader'"
        )
        for result in results:
            print("Database {} has default leader {}".format(database_id, result[0]))


# [END spanner_query_information_schema_database_options]


# [START spanner_insert_data]
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


# [END spanner_insert_data]


# [START spanner_batch_write_at_least_once]
def batch_write(instance_id, database_id):
    """Inserts sample data into the given database via BatchWrite API.

    The database and table must already exist and can be created using
    `create_database`.
    """
    from google.rpc.code_pb2 import OK

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.mutation_groups() as groups:
        group1 = groups.group()
        group1.insert_or_update(
            table="Singers",
            columns=("SingerId", "FirstName", "LastName"),
            values=[
                (16, "Scarlet", "Terry"),
            ],
        )

        group2 = groups.group()
        group2.insert_or_update(
            table="Singers",
            columns=("SingerId", "FirstName", "LastName"),
            values=[
                (17, "Marc", ""),
                (18, "Catalina", "Smith"),
            ],
        )
        group2.insert_or_update(
            table="Albums",
            columns=("SingerId", "AlbumId", "AlbumTitle"),
            values=[
                (17, 1, "Total Junk"),
                (18, 2, "Go, Go, Go"),
            ],
        )

        for response in groups.batch_write():
            if response.status.code == OK:
                print(
                    "Mutation group indexes {} have been applied with commit timestamp {}".format(
                        response.indexes, response.commit_timestamp
                    )
                )
            else:
                print(
                    "Mutation group indexes {} could not be applied with error {}".format(
                        response.indexes, response.status
                    )
                )


# [END spanner_batch_write_at_least_once]


# [START spanner_delete_data]
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


# [END spanner_delete_data]


# [START spanner_query_data]
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


# [END spanner_query_data]


# [START spanner_read_data]
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


# [END spanner_read_data]


# [START spanner_read_stale_data]
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


# [END spanner_read_stale_data]


# [START spanner_query_data_with_new_column]
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


# [END spanner_query_data_with_new_column]


# [START spanner_create_index]
def add_index(instance_id, database_id):
    """Adds a simple index to the example database."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=["CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)"],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the AlbumsByAlbumTitle index.")


# [END spanner_create_index]


# [START spanner_query_data_with_index]
def query_data_with_index(
    instance_id, database_id, start_title="Aardvark", end_title="Goo"
):
    """Queries sample data from the database using SQL and an index.

    The index must exist before running this sample. You can add the index
    by running the `add_index` sample or by running this DDL statement against
    your database:

        CREATE INDEX AlbumsByAlbumTitle ON Albums(AlbumTitle)

    This sample also uses the `MarketingBudget` column. You can add the column
    by running the `add_column` sample or by running this DDL statement against
    your database:

        ALTER TABLE Albums ADD COLUMN MarketingBudget INT64

    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    params = {"start_title": start_title, "end_title": end_title}
    param_types = {
        "start_title": spanner.param_types.STRING,
        "end_title": spanner.param_types.STRING,
    }

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT AlbumId, AlbumTitle, MarketingBudget "
            "FROM Albums@{FORCE_INDEX=AlbumsByAlbumTitle} "
            "WHERE AlbumTitle >= @start_title AND AlbumTitle < @end_title",
            params=params,
            param_types=param_types,
        )

        for row in results:
            print("AlbumId: {}, AlbumTitle: {}, MarketingBudget: {}".format(*row))


# [END spanner_query_data_with_index]


# [START spanner_read_data_with_index]
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


# [END spanner_read_data_with_index]


# [START spanner_create_storing_index]
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
            "STORING (MarketingBudget)"
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the AlbumsByAlbumTitle2 index.")


# [END spanner_create_storing_index]


# [START spanner_read_data_with_storing_index]
def read_data_with_storing_index(instance_id, database_id):
    """Reads sample data from the database using an index with a storing
    clause.

    The index must exist before running this sample. You can add the index
    by running the `add_scoring_index` sample or by running this DDL statement
    against your database:

        CREATE INDEX AlbumsByAlbumTitle2 ON Albums(AlbumTitle)
        STORING (MarketingBudget)

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


# [END spanner_read_data_with_storing_index]


# [START spanner_add_column]
def add_column(instance_id, database_id):
    """Adds a new column to the Albums table in the example database."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "ALTER TABLE Albums ADD COLUMN MarketingBudget INT64",
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)
    print("Added the MarketingBudget column.")


# [END spanner_add_column]


# [START spanner_update_data]
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


# [END spanner_update_data]


# [START spanner_read_write_transaction]
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


# [END spanner_read_write_transaction]


# [START spanner_read_only_transaction]
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


# [END spanner_read_only_transaction]


# [START spanner_create_table_with_timestamp_column]
def create_table_with_timestamp(instance_id, database_id):
    """Creates a table with a COMMIT_TIMESTAMP column."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            """CREATE TABLE Performances (
            SingerId     INT64 NOT NULL,
            VenueId      INT64 NOT NULL,
            EventDate    Date,
            Revenue      INT64,
            LastUpdateTime TIMESTAMP NOT NULL
            OPTIONS(allow_commit_timestamp=true)
        ) PRIMARY KEY (SingerId, VenueId, EventDate),
          INTERLEAVE IN PARENT Singers ON DELETE CASCADE"""
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created Performances table on database {} on instance {}".format(
            database_id, instance_id
        )
    )


# [END spanner_create_table_with_timestamp_column]


# [START spanner_insert_data_with_timestamp_column]
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


# [END spanner_insert_data_with_timestamp_column]


# [START spanner_add_timestamp_column]
def add_timestamp_column(instance_id, database_id):
    """Adds a new TIMESTAMP column to the Albums table in the example database."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "ALTER TABLE Albums ADD COLUMN LastUpdateTime TIMESTAMP "
            "OPTIONS(allow_commit_timestamp=true)"
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        'Altered table "Albums" on database {} on instance {}.'.format(
            database_id, instance_id
        )
    )


# [END spanner_add_timestamp_column]


# [START spanner_update_data_with_timestamp_column]
def update_data_with_timestamp(instance_id, database_id):
    """Updates Performances tables in the database with the COMMIT_TIMESTAMP
    column.

    This updates the `MarketingBudget` column which must be created before
    running this sample. You can add the column by running the `add_column`
    sample or by running this DDL statement against your database:

        ALTER TABLE Albums ADD COLUMN MarketingBudget INT64

    In addition this update expects the LastUpdateTime column added by
    applying this DDL statement against your database:

        ALTER TABLE Albums ADD COLUMN LastUpdateTime TIMESTAMP
        OPTIONS(allow_commit_timestamp=true)
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


# [END spanner_update_data_with_timestamp_column]


# [START spanner_query_data_with_timestamp_column]
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


# [END spanner_query_data_with_timestamp_column]


# [START spanner_add_numeric_column]
def add_numeric_column(instance_id, database_id):
    """Adds a new NUMERIC column to the Venues table in the example database."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=["ALTER TABLE Venues ADD COLUMN Revenue NUMERIC"],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        'Altered table "Venues" on database {} on instance {}.'.format(
            database_id, instance_id
        )
    )


# [END spanner_add_numeric_column]


# [START spanner_update_data_with_numeric_column]
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


# [END spanner_update_data_with_numeric_column]


# [START spanner_add_json_column]
def add_json_column(instance_id, database_id):
    """Adds a new JSON column to the Venues table in the example database."""
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=["ALTER TABLE Venues ADD COLUMN VenueDetails JSON"],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        'Altered table "Venues" on database {} on instance {}.'.format(
            database_id, instance_id
        )
    )


# [END spanner_add_json_column]


# [START spanner_update_data_with_json_column]
def update_data_with_json(instance_id, database_id):
    """Updates Venues tables in the database with the JSON
    column.

    This updates the `VenueDetails` column which must be created before
    running this sample. You can add the column by running the
    `add_json_column` sample or by running this DDL statement
     against your database:

        ALTER TABLE Venues ADD COLUMN VenueDetails JSON
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    with database.batch() as batch:
        batch.update(
            table="Venues",
            columns=("VenueId", "VenueDetails"),
            values=[
                (
                    4,
                    JsonObject(
                        [
                            JsonObject({"name": "room 1", "open": True}),
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


# [END spanner_update_data_with_json_column]


# [START spanner_write_data_for_struct_queries]
def write_struct_data(instance_id, database_id):
    """Inserts sample data that can be used to test STRUCT parameters
    in queries.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.batch() as batch:
        batch.insert(
            table="Singers",
            columns=("SingerId", "FirstName", "LastName"),
            values=[
                (6, "Elena", "Campbell"),
                (7, "Gabriel", "Wright"),
                (8, "Benjamin", "Martinez"),
                (9, "Hannah", "Harris"),
            ],
        )

    print("Inserted sample data for STRUCT queries")


# [END spanner_write_data_for_struct_queries]


def query_with_struct(instance_id, database_id):
    """Query a table using STRUCT parameters."""
    # [START spanner_create_struct_with_data]
    record_type = param_types.Struct(
        [
            param_types.StructField("FirstName", param_types.STRING),
            param_types.StructField("LastName", param_types.STRING),
        ]
    )
    record_value = ("Elena", "Campbell")
    # [END spanner_create_struct_with_data]

    # [START spanner_query_data_with_struct]
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId FROM Singers WHERE (FirstName, LastName) = @name",
            params={"name": record_value},
            param_types={"name": record_type},
        )

    for row in results:
        print("SingerId: {}".format(*row))
    # [END spanner_query_data_with_struct]


def query_with_array_of_struct(instance_id, database_id):
    """Query a table using an array of STRUCT parameters."""
    # [START spanner_create_user_defined_struct]
    name_type = param_types.Struct(
        [
            param_types.StructField("FirstName", param_types.STRING),
            param_types.StructField("LastName", param_types.STRING),
        ]
    )
    # [END spanner_create_user_defined_struct]

    # [START spanner_create_array_of_struct_with_data]
    band_members = [
        ("Elena", "Campbell"),
        ("Gabriel", "Wright"),
        ("Benjamin", "Martinez"),
    ]
    # [END spanner_create_array_of_struct_with_data]

    # [START spanner_query_data_with_array_of_struct]
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId FROM Singers WHERE "
            "STRUCT<FirstName STRING, LastName STRING>"
            "(FirstName, LastName) IN UNNEST(@names)",
            params={"names": band_members},
            param_types={"names": param_types.Array(name_type)},
        )

    for row in results:
        print("SingerId: {}".format(*row))
    # [END spanner_query_data_with_array_of_struct]


# [START spanner_field_access_on_struct_parameters]
def query_struct_field(instance_id, database_id):
    """Query a table using field access on a STRUCT parameter."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    name_type = param_types.Struct(
        [
            param_types.StructField("FirstName", param_types.STRING),
            param_types.StructField("LastName", param_types.STRING),
        ]
    )

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId FROM Singers WHERE FirstName = @name.FirstName",
            params={"name": ("Elena", "Campbell")},
            param_types={"name": name_type},
        )

    for row in results:
        print("SingerId: {}".format(*row))


# [END spanner_field_access_on_struct_parameters]


# [START spanner_field_access_on_nested_struct_parameters]
def query_nested_struct_field(instance_id, database_id):
    """Query a table using nested field access on a STRUCT parameter."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    song_info_type = param_types.Struct(
        [
            param_types.StructField("SongName", param_types.STRING),
            param_types.StructField(
                "ArtistNames",
                param_types.Array(
                    param_types.Struct(
                        [
                            param_types.StructField("FirstName", param_types.STRING),
                            param_types.StructField("LastName", param_types.STRING),
                        ]
                    )
                ),
            ),
        ]
    )

    song_info = ("Imagination", [("Elena", "Campbell"), ("Hannah", "Harris")])

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, @song_info.SongName "
            "FROM Singers WHERE "
            "STRUCT<FirstName STRING, LastName STRING>"
            "(FirstName, LastName) "
            "IN UNNEST(@song_info.ArtistNames)",
            params={"song_info": song_info},
            param_types={"song_info": song_info_type},
        )

    for row in results:
        print("SingerId: {} SongName: {}".format(*row))


# [END spanner_field_access_on_nested_struct_parameters]


def insert_data_with_dml(instance_id, database_id):
    """Inserts sample data into the given database using a DML statement."""
    # [START spanner_dml_standard_insert]
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
    # [END spanner_dml_standard_insert]


# [START spanner_get_commit_stats]
def log_commit_stats(instance_id, database_id):
    """Inserts sample data using DML and displays the commit statistics."""

    # By default, commit statistics are logged via stdout at level Info.
    # This sample uses a custom logger to access the commit statistics.
    class CommitStatsSampleLogger(logging.Logger):
        def __init__(self):
            self.last_commit_stats = None
            super().__init__("commit_stats_sample")

        def info(self, msg, *args, **kwargs):
            if (
                "extra" in kwargs
                and kwargs["extra"]
                and "commit_stats" in kwargs["extra"]
            ):
                self.last_commit_stats = kwargs["extra"]["commit_stats"]
            super().info(msg, *args, **kwargs)

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id, logger=CommitStatsSampleLogger())
    database.log_commit_stats = True

    def insert_singers(transaction):
        row_ct = transaction.execute_update(
            "INSERT Singers (SingerId, FirstName, LastName) "
            " VALUES (110, 'Virginia', 'Watson')"
        )

        print("{} record(s) inserted.".format(row_ct))

    database.run_in_transaction(insert_singers)
    commit_stats = database.logger.last_commit_stats
    print("{} mutation(s) in transaction.".format(commit_stats.mutation_count))


# [END spanner_get_commit_stats]


def set_max_commit_delay(instance_id, database_id):
    """Inserts sample data and sets a max commit delay."""
    # [START spanner_set_max_commit_delay]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_singers(transaction):
        row_ct = transaction.execute_update(
            "INSERT Singers (SingerId, FirstName, LastName) "
            " VALUES (111, 'Grace', 'Bennis')"
        )

        print("{} record(s) inserted.".format(row_ct))

    database.run_in_transaction(
        insert_singers, max_commit_delay=datetime.timedelta(milliseconds=100)
    )
    # [END spanner_set_max_commit_delay]


def update_data_with_dml(instance_id, database_id):
    """Updates sample data from the database using a DML statement."""
    # [START spanner_dml_standard_update]
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
    # [END spanner_dml_standard_update]


def update_data_with_dml_returning(instance_id, database_id):
    """Updates sample data from the database using a DML statement having a THEN RETURN clause."""
    # [START spanner_dml_update_returning]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Update MarketingBudget column for records satisfying
    # a particular condition and returns the modified
    # MarketingBudget column of the updated records using
    # 'THEN RETURN MarketingBudget'.
    # It is also possible to return all columns of all the
    # updated records by using 'THEN RETURN *'.
    def update_albums(transaction):
        results = transaction.execute_sql(
            "UPDATE Albums "
            "SET MarketingBudget = MarketingBudget * 2 "
            "WHERE SingerId = 1 and AlbumId = 1 "
            "THEN RETURN MarketingBudget"
        )
        for result in results:
            print("MarketingBudget: {}".format(*result))
        print("{} record(s) updated.".format(results.stats.row_count_exact))

    database.run_in_transaction(update_albums)
    # [END spanner_dml_update_returning]


def delete_data_with_dml(instance_id, database_id):
    """Deletes sample data from the database using a DML statement."""
    # [START spanner_dml_standard_delete]
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
    # [END spanner_dml_standard_delete]


def delete_data_with_dml_returning(instance_id, database_id):
    """Deletes sample data from the database using a DML statement having a THEN RETURN clause."""
    # [START spanner_dml_delete_returning]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Delete records from SINGERS table satisfying a
    # particular condition and returns the SingerId
    # and FullName column of the deleted records using
    # 'THEN RETURN SingerId, FullName'.
    # It is also possible to return all columns of all the
    # deleted records by using 'THEN RETURN *'.
    def delete_singers(transaction):
        results = transaction.execute_sql(
            "DELETE FROM Singers WHERE FirstName = 'David' "
            "THEN RETURN SingerId, FullName"
        )
        for result in results:
            print("SingerId: {}, FullName: {}".format(*result))
        print("{} record(s) deleted.".format(results.stats.row_count_exact))

    database.run_in_transaction(delete_singers)
    # [END spanner_dml_delete_returning]


def update_data_with_dml_timestamp(instance_id, database_id):
    """Updates data with Timestamp from the database using a DML statement."""
    # [START spanner_dml_standard_update_with_timestamp]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def update_albums(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Albums "
            "SET LastUpdateTime = PENDING_COMMIT_TIMESTAMP() "
            "WHERE SingerId = 1"
        )

        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(update_albums)
    # [END spanner_dml_standard_update_with_timestamp]


def dml_write_read_transaction(instance_id, database_id):
    """First inserts data then reads it from within a transaction using DML."""
    # [START spanner_dml_write_then_read]
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
    # [END spanner_dml_write_then_read]


def update_data_with_dml_struct(instance_id, database_id):
    """Updates data with a DML statement and STRUCT parameters."""
    # [START spanner_dml_structs]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    record_type = param_types.Struct(
        [
            param_types.StructField("FirstName", param_types.STRING),
            param_types.StructField("LastName", param_types.STRING),
        ]
    )
    record_value = ("Timothy", "Campbell")

    def write_with_struct(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Singers SET LastName = 'Grant' "
            "WHERE STRUCT<FirstName STRING, LastName STRING>"
            "(FirstName, LastName) = @name",
            params={"name": record_value},
            param_types={"name": record_type},
        )
        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(write_with_struct)
    # [END spanner_dml_structs]


def insert_with_dml(instance_id, database_id):
    """Inserts data with a DML statement into the database."""
    # [START spanner_dml_getting_started_insert]
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
    # [END spanner_dml_getting_started_insert]


def insert_with_dml_returning(instance_id, database_id):
    """Inserts sample data into the given database using a DML statement having a THEN RETURN clause."""
    # [START spanner_dml_insert_returning]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Insert records into the SINGERS table and returns the
    # generated column FullName of the inserted records using
    # 'THEN RETURN FullName'.
    # It is also possible to return all columns of all the
    # inserted records by using 'THEN RETURN *'.
    def insert_singers(transaction):
        results = transaction.execute_sql(
            "INSERT INTO Singers (SingerId, FirstName, LastName) VALUES "
            "(21, 'Luann', 'Chizoba'), "
            "(22, 'Denis', 'Patricio'), "
            "(23, 'Felxi', 'Ronan'), "
            "(24, 'Dominik', 'Martyna') "
            "THEN RETURN FullName"
        )
        for result in results:
            print("FullName: {}".format(*result))
        print("{} record(s) inserted.".format(results.stats.row_count_exact))

    database.run_in_transaction(insert_singers)
    # [END spanner_dml_insert_returning]


def query_data_with_parameter(instance_id, database_id):
    """Queries sample data from the database using SQL with a parameter."""
    # [START spanner_query_with_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, FirstName, LastName FROM Singers "
            "WHERE LastName = @lastName",
            params={"lastName": "Garcia"},
            param_types={"lastName": spanner.param_types.STRING},
        )

        for row in results:
            print("SingerId: {}, FirstName: {}, LastName: {}".format(*row))
    # [END spanner_query_with_parameter]


def write_with_dml_transaction(instance_id, database_id):
    """Transfers part of a marketing budget from one album to another."""
    # [START spanner_dml_getting_started_update]
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
                "SET MarketingBudget = @AlbumBudget "
                "WHERE SingerId = 1 and AlbumId = 1",
                params={"AlbumBudget": first_album_budget},
                param_types={"AlbumBudget": spanner.param_types.INT64},
            )

            # Update second album
            transaction.execute_update(
                "UPDATE Albums "
                "SET MarketingBudget = @AlbumBudget "
                "WHERE SingerId = 2 and AlbumId = 2",
                params={"AlbumBudget": second_album_budget},
                param_types={"AlbumBudget": spanner.param_types.INT64},
            )

            print(
                "Transferred {} from Album2's budget to Album1's".format(
                    transfer_amount
                )
            )

    database.run_in_transaction(transfer_budget)
    # [END spanner_dml_getting_started_update]


def update_data_with_partitioned_dml(instance_id, database_id):
    """Update sample data with a partitioned DML statement."""
    # [START spanner_dml_partitioned_update]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    row_ct = database.execute_partitioned_dml(
        "UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1"
    )

    print("{} records updated.".format(row_ct))
    # [END spanner_dml_partitioned_update]


def delete_data_with_partitioned_dml(instance_id, database_id):
    """Delete sample data with a partitioned DML statement."""
    # [START spanner_dml_partitioned_delete]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    row_ct = database.execute_partitioned_dml("DELETE FROM Singers WHERE SingerId > 10")

    print("{} record(s) deleted.".format(row_ct))
    # [END spanner_dml_partitioned_delete]


def update_with_batch_dml(instance_id, database_id):
    """Updates sample data in the database using Batch DML."""
    # [START spanner_dml_batch_update]
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
    # [END spanner_dml_batch_update]


def dml_last_statement_option(instance_id, database_id):
    """Inserts and updates using DML where the update sets the last statement option."""
    # [START spanner_dml_last_statement]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_and_update_singers(transaction):
        insert_row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            "VALUES (54213, 'John', 'Do')"
        )

        print("{} record(s) inserted.".format(insert_row_ct))

        update_row_ct = transaction.execute_update(
            "UPDATE Singers SET LastName = 'Doe' WHERE SingerId = 54213",
            last_statement=True,
        )

        print("{} record(s) updated.".format(update_row_ct))

    database.run_in_transaction(insert_and_update_singers)
    # [END spanner_dml_last_statement]


def create_table_with_datatypes(instance_id, database_id):
    """Creates a table with supported datatypes."""
    # [START spanner_create_table_with_datatypes]
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
            VenueId         INT64 NOT NULL,
            VenueName       STRING(100),
            VenueInfo       BYTES(MAX),
            Capacity        INT64,
            AvailableDates  ARRAY<DATE>,
            LastContactDate DATE,
            OutdoorVenue    BOOL,
            PopularityScore FLOAT64,
            LastUpdateTime  TIMESTAMP NOT NULL
            OPTIONS(allow_commit_timestamp=true)
        ) PRIMARY KEY (VenueId)"""
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
    # [END spanner_create_table_with_datatypes]


def insert_datatypes_data(instance_id, database_id):
    """Inserts data with supported datatypes into a table."""
    # [START spanner_insert_datatypes_data]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleBytes1 = base64.b64encode("Hello World 1".encode())
    exampleBytes2 = base64.b64encode("Hello World 2".encode())
    exampleBytes3 = base64.b64encode("Hello World 3".encode())
    available_dates1 = ["2020-12-01", "2020-12-02", "2020-12-03"]
    available_dates2 = ["2020-11-01", "2020-11-05", "2020-11-15"]
    available_dates3 = ["2020-10-01", "2020-10-07"]
    with database.batch() as batch:
        batch.insert(
            table="Venues",
            columns=(
                "VenueId",
                "VenueName",
                "VenueInfo",
                "Capacity",
                "AvailableDates",
                "LastContactDate",
                "OutdoorVenue",
                "PopularityScore",
                "LastUpdateTime",
            ),
            values=[
                (
                    4,
                    "Venue 4",
                    exampleBytes1,
                    1800,
                    available_dates1,
                    "2018-09-02",
                    False,
                    0.85543,
                    spanner.COMMIT_TIMESTAMP,
                ),
                (
                    19,
                    "Venue 19",
                    exampleBytes2,
                    6300,
                    available_dates2,
                    "2019-01-15",
                    True,
                    0.98716,
                    spanner.COMMIT_TIMESTAMP,
                ),
                (
                    42,
                    "Venue 42",
                    exampleBytes3,
                    3000,
                    available_dates3,
                    "2018-10-01",
                    False,
                    0.72598,
                    spanner.COMMIT_TIMESTAMP,
                ),
            ],
        )

    print("Inserted data.")
    # [END spanner_insert_datatypes_data]


def query_data_with_array(instance_id, database_id):
    """Queries sample data using SQL with an ARRAY parameter."""
    # [START spanner_query_with_array_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleArray = ["2020-10-01", "2020-11-01"]
    param = {"available_dates": exampleArray}
    param_type = {"available_dates": param_types.Array(param_types.DATE)}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, AvailableDate FROM Venues v,"
            "UNNEST(v.AvailableDates) as AvailableDate "
            "WHERE AvailableDate in UNNEST(@available_dates)",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, AvailableDate: {}".format(*row))
    # [END spanner_query_with_array_parameter]


def query_data_with_bool(instance_id, database_id):
    """Queries sample data using SQL with a BOOL parameter."""
    # [START spanner_query_with_bool_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleBool = True
    param = {"outdoor_venue": exampleBool}
    param_type = {"outdoor_venue": param_types.BOOL}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, OutdoorVenue FROM Venues "
            "WHERE OutdoorVenue = @outdoor_venue",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, OutdoorVenue: {}".format(*row))
    # [END spanner_query_with_bool_parameter]


def query_data_with_bytes(instance_id, database_id):
    """Queries sample data using SQL with a BYTES parameter."""
    # [START spanner_query_with_bytes_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleBytes = base64.b64encode("Hello World 1".encode())
    param = {"venue_info": exampleBytes}
    param_type = {"venue_info": param_types.BYTES}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName FROM Venues WHERE VenueInfo = @venue_info",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}".format(*row))
    # [END spanner_query_with_bytes_parameter]


def query_data_with_date(instance_id, database_id):
    """Queries sample data using SQL with a DATE parameter."""
    # [START spanner_query_with_date_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleDate = "2019-01-01"
    param = {"last_contact_date": exampleDate}
    param_type = {"last_contact_date": param_types.DATE}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, LastContactDate FROM Venues "
            "WHERE LastContactDate < @last_contact_date",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, LastContactDate: {}".format(*row))
    # [END spanner_query_with_date_parameter]


def query_data_with_float(instance_id, database_id):
    """Queries sample data using SQL with a FLOAT64 parameter."""
    # [START spanner_query_with_float_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleFloat = 0.8
    param = {"popularity_score": exampleFloat}
    param_type = {"popularity_score": param_types.FLOAT64}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, PopularityScore FROM Venues "
            "WHERE PopularityScore > @popularity_score",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, PopularityScore: {}".format(*row))
    # [END spanner_query_with_float_parameter]


def query_data_with_int(instance_id, database_id):
    """Queries sample data using SQL with a INT64 parameter."""
    # [START spanner_query_with_int_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleInt = 3000
    param = {"capacity": exampleInt}
    param_type = {"capacity": param_types.INT64}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, Capacity FROM Venues "
            "WHERE Capacity >= @capacity",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, Capacity: {}".format(*row))
    # [END spanner_query_with_int_parameter]


def query_data_with_string(instance_id, database_id):
    """Queries sample data using SQL with a STRING parameter."""
    # [START spanner_query_with_string_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    exampleString = "Venue 42"
    param = {"venue_name": exampleString}
    param_type = {"venue_name": param_types.STRING}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName FROM Venues WHERE VenueName = @venue_name",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}".format(*row))
    # [END spanner_query_with_string_parameter]


def query_data_with_numeric_parameter(instance_id, database_id):
    """Queries sample data using SQL with a NUMERIC parameter."""
    # [START spanner_query_with_numeric_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    example_numeric = decimal.Decimal("100000")
    param = {"revenue": example_numeric}
    param_type = {"revenue": param_types.NUMERIC}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, Revenue FROM Venues WHERE Revenue < @revenue",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, Revenue: {}".format(*row))
    # [END spanner_query_with_numeric_parameter]


def query_data_with_json_parameter(instance_id, database_id):
    """Queries sample data using SQL with a JSON parameter."""
    # [START spanner_query_with_json_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    example_json = json.dumps({"rating": 9})
    param = {"details": example_json}
    param_type = {"details": param_types.JSON}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueDetails "
            "FROM Venues "
            "WHERE JSON_VALUE(VenueDetails, '$.rating') = "
            "JSON_VALUE(@details, '$.rating')",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueDetails: {}".format(*row))
    # [END spanner_query_with_json_parameter]


def query_data_with_timestamp_parameter(instance_id, database_id):
    """Queries sample data using SQL with a TIMESTAMP parameter."""
    # [START spanner_query_with_timestamp_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    example_timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    # [END spanner_query_with_timestamp_parameter]
    # Avoid time drift on the local machine.
    # https://github.com/GoogleCloudPlatform/python-docs-samples/issues/4197.
    example_timestamp = (
        datetime.datetime.utcnow() + datetime.timedelta(days=1)
    ).isoformat() + "Z"
    # [START spanner_query_with_timestamp_parameter]
    param = {"last_update_time": example_timestamp}
    param_type = {"last_update_time": param_types.TIMESTAMP}

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, LastUpdateTime FROM Venues "
            "WHERE LastUpdateTime < @last_update_time",
            params=param,
            param_types=param_type,
        )

        for row in results:
            print("VenueId: {}, VenueName: {}, LastUpdateTime: {}".format(*row))
    # [END spanner_query_with_timestamp_parameter]


def query_data_with_query_options(instance_id, database_id):
    """Queries sample data using SQL with query options."""
    # [START spanner_query_with_query_options]
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
    # [END spanner_query_with_query_options]


def create_client_with_query_options(instance_id, database_id):
    """Create a client with query options."""
    # [START spanner_create_client_with_query_options]
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
    # [END spanner_create_client_with_query_options]


def set_transaction_tag(instance_id, database_id):
    """Executes a transaction with a transaction tag."""
    # [START spanner_set_transaction_tag]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def update_venues(transaction):
        # Sets the request tag to "app=concert,env=dev,action=update".
        #  This request tag will only be set on this request.
        transaction.execute_update(
            "UPDATE Venues SET Capacity = CAST(Capacity/4 AS INT64) WHERE OutdoorVenue = false",
            request_options={"request_tag": "app=concert,env=dev,action=update"},
        )
        print("Venue capacities updated.")

        # Sets the request tag to "app=concert,env=dev,action=insert".
        # This request tag will only be set on this request.
        transaction.execute_update(
            "INSERT INTO Venues (VenueId, VenueName, Capacity, OutdoorVenue, LastUpdateTime) "
            "VALUES (@venueId, @venueName, @capacity, @outdoorVenue, PENDING_COMMIT_TIMESTAMP())",
            params={
                "venueId": 81,
                "venueName": "Venue 81",
                "capacity": 1440,
                "outdoorVenue": True,
            },
            param_types={
                "venueId": param_types.INT64,
                "venueName": param_types.STRING,
                "capacity": param_types.INT64,
                "outdoorVenue": param_types.BOOL,
            },
            request_options={"request_tag": "app=concert,env=dev,action=insert"},
        )
        print("New venue inserted.")

    database.run_in_transaction(update_venues, transaction_tag="app=concert,env=dev")

    # [END spanner_set_transaction_tag]


def set_transaction_timeout(instance_id, database_id):
    """Executes a transaction with a transaction timeout."""
    # [START spanner_transaction_timeout]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def read_then_write(transaction):
        # Read records.
        results = transaction.execute_sql(
            "SELECT SingerId, FirstName, LastName FROM Singers ORDER BY LastName, FirstName"
        )
        for result in results:
            print("SingerId: {}, FirstName: {}, LastName: {}".format(*result))

        # Insert a record.
        row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            " VALUES (100, 'George', 'Washington')"
        )
        print("{} record(s) inserted.".format(row_ct))

    # configure transaction timeout to 60 seconds
    database.run_in_transaction(read_then_write, timeout_secs=60)

    # [END spanner_transaction_timeout]


def set_statement_timeout(instance_id, database_id):
    """Executes a transaction with a statement timeout."""
    # [START spanner_set_statement_timeout]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def write(transaction):
        # Insert a record and configure the statement timeout to 60 seconds
        # This timeout can however ONLY BE SHORTER than the default timeout
        # for the RPC. If you set a timeout that is longer than the default timeout,
        # then the default timeout will be used.
        row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            " VALUES (110, 'George', 'Washington')",
            timeout=60,
        )
        print("{} record(s) inserted.".format(row_ct))

    database.run_in_transaction(write)

    # [END spanner_set_statement_timeout]


def set_request_tag(instance_id, database_id):
    """Executes a snapshot read with a request tag."""
    # [START spanner_set_request_tag]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, AlbumTitle FROM Albums",
            request_options={"request_tag": "app=concert,env=dev,action=select"},
        )

        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))

    # [END spanner_set_request_tag]


# [START spanner_create_instance_config]
def create_instance_config(user_config_name, base_config_id):
    """Creates the new user-managed instance configuration using base instance config."""

    # user_config_name = `custom-nam11`
    # base_config_id = `projects/<project>/instanceConfigs/nam11`
    spanner_client = spanner.Client()
    base_config = spanner_client.instance_admin_api.get_instance_config(
        name=base_config_id
    )

    # The replicas for the custom instance configuration must include all the replicas of the base
    # configuration, in addition to at least one from the list of optional replicas of the base
    # configuration.
    replicas = []
    for replica in base_config.replicas:
        replicas.append(replica)
    replicas.append(base_config.optional_replicas[0])
    operation = spanner_client.instance_admin_api.create_instance_config(
        parent=spanner_client.project_name,
        instance_config_id=user_config_name,
        instance_config=spanner_instance_admin.InstanceConfig(
            name="{}/instanceConfigs/{}".format(
                spanner_client.project_name, user_config_name
            ),
            display_name="custom-python-samples",
            config_type=spanner_instance_admin.InstanceConfig.Type.USER_MANAGED,
            replicas=replicas,
            base_config=base_config.name,
            labels={"python_cloud_spanner_samples": "true"},
        ),
    )
    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created instance configuration {}".format(user_config_name))


# [END spanner_create_instance_config]


# [START spanner_update_instance_config]
def update_instance_config(user_config_name):
    """Updates the user-managed instance configuration."""

    # user_config_name = `custom-nam11`
    spanner_client = spanner.Client()
    config = spanner_client.instance_admin_api.get_instance_config(
        name="{}/instanceConfigs/{}".format(
            spanner_client.project_name, user_config_name
        )
    )
    config.display_name = "updated custom instance config"
    config.labels["updated"] = "true"
    operation = spanner_client.instance_admin_api.update_instance_config(
        instance_config=config,
        update_mask=field_mask_pb2.FieldMask(paths=["display_name", "labels"]),
    )
    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)
    print("Updated instance configuration {}".format(user_config_name))


# [END spanner_update_instance_config]


# [START spanner_delete_instance_config]
def delete_instance_config(user_config_id):
    """Deleted the user-managed instance configuration."""
    spanner_client = spanner.Client()
    spanner_client.instance_admin_api.delete_instance_config(name=user_config_id)
    print("Instance config {} successfully deleted".format(user_config_id))


# [END spanner_delete_instance_config]


# [START spanner_list_instance_config_operations]
def list_instance_config_operations():
    """List the user-managed instance configuration operations."""
    spanner_client = spanner.Client()
    operations = spanner_client.instance_admin_api.list_instance_config_operations(
        request=spanner_instance_admin.ListInstanceConfigOperationsRequest(
            parent=spanner_client.project_name,
            filter="(metadata.@type=type.googleapis.com/google.spanner.admin.instance.v1.CreateInstanceConfigMetadata)",
        )
    )
    for op in operations:
        metadata = spanner_instance_admin.CreateInstanceConfigMetadata.pb(
            spanner_instance_admin.CreateInstanceConfigMetadata()
        )
        op.metadata.Unpack(metadata)
        print(
            "List instance config operations {} is {}% completed.".format(
                metadata.instance_config.name, metadata.progress.progress_percent
            )
        )


# [END spanner_list_instance_config_operations]


def add_and_drop_database_roles(instance_id, database_id):
    """Showcases how to manage a user defined database role."""
    # [START spanner_add_and_drop_database_role]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    role_parent = "new_parent"
    role_child = "new_child"

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "CREATE ROLE {}".format(role_parent),
            "GRANT SELECT ON TABLE Singers TO ROLE {}".format(role_parent),
            "CREATE ROLE {}".format(role_child),
            "GRANT ROLE {} TO ROLE {}".format(role_parent, role_child),
        ],
    )
    operation = database_admin_api.update_database_ddl(request)

    operation.result(OPERATION_TIMEOUT_SECONDS)
    print(
        "Created roles {} and {} and granted privileges".format(role_parent, role_child)
    )

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "REVOKE ROLE {} FROM ROLE {}".format(role_parent, role_child),
            "DROP ROLE {}".format(role_child),
        ],
    )
    operation = database_admin_api.update_database_ddl(request)

    operation.result(OPERATION_TIMEOUT_SECONDS)
    print("Revoked privileges and dropped role {}".format(role_child))

    # [END spanner_add_and_drop_database_role]


def read_data_with_database_role(instance_id, database_id):
    """Showcases how a user defined database role is used by member."""
    # [START spanner_read_data_with_database_role]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    role = "new_parent"
    database = instance.database(database_id, database_role=role)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql("SELECT * FROM Singers")
        for row in results:
            print("SingerId: {}, FirstName: {}, LastName: {}".format(*row))

    # [END spanner_read_data_with_database_role]


def list_database_roles(instance_id, database_id):
    """Showcases how to list Database Roles."""
    # [START spanner_list_database_roles]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.ListDatabaseRolesRequest(
        parent=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        )
    )
    # List database roles.
    print("Database Roles are:")
    for role in database_admin_api.list_database_roles(request):
        print(role.name.split("/")[-1])
    # [END spanner_list_database_roles]


def enable_fine_grained_access(
    instance_id,
    database_id,
    iam_member="user:alice@example.com",
    database_role="new_parent",
    title="condition title",
):
    """Showcases how to enable fine grained access control."""
    # [START spanner_enable_fine_grained_access]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    # iam_member = "user:alice@example.com"
    # database_role = "new_parent"
    # title = "condition title"

    from google.iam.v1 import iam_policy_pb2, options_pb2, policy_pb2
    from google.type import expr_pb2

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    # The policy in the response from getDatabaseIAMPolicy might use the policy version
    # that you specified, or it might use a lower policy version. For example, if you
    # specify version 3, but the policy has no conditional role bindings, the response
    # uses version 1. Valid values are 0, 1, and 3.
    request = iam_policy_pb2.GetIamPolicyRequest(
        resource=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        options=options_pb2.GetPolicyOptions(requested_policy_version=3),
    )
    policy = database_admin_api.get_iam_policy(request=request)
    if policy.version < 3:
        policy.version = 3

    new_binding = policy_pb2.Binding(
        role="roles/spanner.fineGrainedAccessUser",
        members=[iam_member],
        condition=expr_pb2.Expr(
            title=title,
            expression=f'resource.name.endsWith("/databaseRoles/{database_role}")',
        ),
    )

    policy.version = 3
    policy.bindings.append(new_binding)
    set_request = iam_policy_pb2.SetIamPolicyRequest(
        resource=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        policy=policy,
    )
    database_admin_api.set_iam_policy(set_request)

    new_policy = database_admin_api.get_iam_policy(request=request)
    print(
        f"Enabled fine-grained access in IAM. New policy has version {new_policy.version}"
    )
    # [END spanner_enable_fine_grained_access]


# [START spanner_create_table_with_foreign_key_delete_cascade]
def create_table_with_foreign_key_delete_cascade(instance_id, database_id):
    """Creates a table with foreign key delete cascade action"""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            """CREATE TABLE Customers (
               CustomerId INT64 NOT NULL,
               CustomerName STRING(62) NOT NULL,
               ) PRIMARY KEY (CustomerId)
            """,
            """
               CREATE TABLE ShoppingCarts (
               CartId INT64 NOT NULL,
               CustomerId INT64 NOT NULL,
               CustomerName STRING(62) NOT NULL,
               CONSTRAINT FKShoppingCartsCustomerId FOREIGN KEY (CustomerId)
               REFERENCES Customers (CustomerId) ON DELETE CASCADE
               ) PRIMARY KEY (CartId)
            """,
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        """Created Customers and ShoppingCarts table with FKShoppingCartsCustomerId
           foreign key constraint on database {} on instance {}""".format(
            database_id, instance_id
        )
    )


# [END spanner_create_table_with_foreign_key_delete_cascade]


# [START spanner_alter_table_with_foreign_key_delete_cascade]
def alter_table_with_foreign_key_delete_cascade(instance_id, database_id):
    """Alters a table with foreign key delete cascade action"""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            """ALTER TABLE ShoppingCarts
               ADD CONSTRAINT FKShoppingCartsCustomerName
               FOREIGN KEY (CustomerName)
               REFERENCES Customers(CustomerName)
               ON DELETE CASCADE"""
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        """Altered ShoppingCarts table with FKShoppingCartsCustomerName
           foreign key constraint on database {} on instance {}""".format(
            database_id, instance_id
        )
    )


# [END spanner_alter_table_with_foreign_key_delete_cascade]


# [START spanner_drop_foreign_key_constraint_delete_cascade]
def drop_foreign_key_constraint_delete_cascade(instance_id, database_id):
    """Alter table to drop foreign key delete cascade action"""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            """ALTER TABLE ShoppingCarts
               DROP CONSTRAINT FKShoppingCartsCustomerName"""
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        """Altered ShoppingCarts table to drop FKShoppingCartsCustomerName
           foreign key constraint on database {} on instance {}""".format(
            database_id, instance_id
        )
    )


# [END spanner_drop_foreign_key_constraint_delete_cascade]


# [START spanner_create_sequence]
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
            "CREATE SEQUENCE Seq OPTIONS (sequence_kind = 'bit_reversed_positive')",
            """CREATE TABLE Customers (
            CustomerId     INT64 DEFAULT (GET_NEXT_SEQUENCE_VALUE(Sequence Seq)),
            CustomerName      STRING(1024)
            ) PRIMARY KEY (CustomerId)""",
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
            "THEN RETURN CustomerId"
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


# [END spanner_create_sequence]


# [START spanner_alter_sequence]
def alter_sequence(instance_id, database_id):
    """Alters the Sequence and insert data"""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "ALTER SEQUENCE Seq SET OPTIONS (skip_range_min = 1000, skip_range_max = 5000000)",
        ],
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
            "THEN RETURN CustomerId"
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


# [END spanner_alter_sequence]


# [START spanner_drop_sequence]
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


# [END spanner_drop_sequence]


def directed_read_options(
    instance_id,
    database_id,
):
    """
    Shows how to run an execute sql request with directed read options.
    Only one of exclude_replicas or include_replicas can be set
    Each accepts a list of replicaSelections which contains location and type
    * `location` - The location must be one of the regions within the
        multi-region configuration of your database.
    * `type_` - The type of the replica
    Some examples of using replica_selectors are:
    * `location:us-east1` --> The "us-east1" replica(s) of any available type
                              will be used to process the request.
    * `type:READ_ONLY`    --> The "READ_ONLY" type replica(s) in nearest
                              available location will be used to process the
                              request.
    * `location:us-east1 type:READ_ONLY` --> The "READ_ONLY" type replica(s)
                              in location "us-east1" will be used to process
                              the request.
    include_replicas also contains an option for auto_failover_disabled which when set
    Spanner will not route requests to a replica outside the
    include_replicas list when all the specified replicas are unavailable
    or unhealthy. The default value is `false`
    """
    # [START spanner_directed_read]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    directed_read_options_for_client = {
        "exclude_replicas": {
            "replica_selections": [
                {
                    "location": "us-east4",
                },
            ],
        },
    }

    # directed_read_options can be set at client level and will be used in all
    # read-only transaction requests
    spanner_client = spanner.Client(
        directed_read_options=directed_read_options_for_client
    )
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    directed_read_options_for_request = {
        "include_replicas": {
            "replica_selections": [
                {
                    "type_": DirectedReadOptions.ReplicaSelection.Type.READ_ONLY,
                },
            ],
            "auto_failover_disabled": True,
        },
    }

    with database.snapshot() as snapshot:
        # Read rows while passing directed_read_options directly to the query.
        # These will override the options passed at Client level.
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, AlbumTitle FROM Albums",
            directed_read_options=directed_read_options_for_request,
        )

        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))
    # [END spanner_directed_read]


def isolation_level_options(
    instance_id,
    database_id,
):
    """
    Shows how to run a Read Write transaction with isolation level options.
    """
    # [START spanner_isolation_level]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    from google.cloud.spanner_v1 import DefaultTransactionOptions, TransactionOptions

    # The isolation level specified at the client-level will be applied to all RW transactions.
    isolation_options_for_client = TransactionOptions.IsolationLevel.SERIALIZABLE

    spanner_client = spanner.Client(
        default_transaction_options=DefaultTransactionOptions(
            isolation_level=isolation_options_for_client
        )
    )
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # The isolation level specified at the request level takes precedence over the isolation level configured at the client level.
    isolation_options_for_transaction = (
        TransactionOptions.IsolationLevel.REPEATABLE_READ
    )

    def update_albums_with_isolation(transaction):
        # Read an AlbumTitle.
        results = transaction.execute_sql(
            "SELECT AlbumTitle from Albums WHERE SingerId = 1 and AlbumId = 1"
        )
        for result in results:
            print("Current Album Title: {}".format(*result))

        # Update the AlbumTitle.
        row_ct = transaction.execute_update(
            "UPDATE Albums SET AlbumTitle = 'A New Title' WHERE SingerId = 1 and AlbumId = 1"
        )

        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(
        update_albums_with_isolation, isolation_level=isolation_options_for_transaction
    )
    # [END spanner_isolation_level]


def read_lock_mode_options(
    instance_id,
    database_id,
):
    """
    Shows how to run a Read Write transaction with read lock mode options.
    """
    # [START spanner_read_lock_mode]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    from google.cloud.spanner_v1 import DefaultTransactionOptions, TransactionOptions

    # The read lock mode specified at the client-level will be applied to all
    # RW transactions.
    read_lock_mode_options_for_client = (
        TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC
    )

    # Create a client that uses Serializable isolation (default) with
    # optimistic locking for read-write transactions.
    spanner_client = spanner.Client(
        default_transaction_options=DefaultTransactionOptions(
            read_lock_mode=read_lock_mode_options_for_client
        )
    )
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # The read lock mode specified at the request level takes precedence over
    # the read lock mode configured at the client level.
    read_lock_mode_options_for_transaction = (
        TransactionOptions.ReadWrite.ReadLockMode.PESSIMISTIC
    )

    def update_albums_with_read_lock_mode(transaction):
        # Read an AlbumTitle.
        results = transaction.execute_sql(
            "SELECT AlbumTitle from Albums WHERE SingerId = 2 and AlbumId = 1"
        )
        for result in results:
            print("Current Album Title: {}".format(*result))

        # Update the AlbumTitle.
        row_ct = transaction.execute_update(
            "UPDATE Albums SET AlbumTitle = 'A New Title' WHERE SingerId = 2 and AlbumId = 1"
        )

        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(
        update_albums_with_read_lock_mode,
        read_lock_mode=read_lock_mode_options_for_transaction,
    )
    # [END spanner_read_lock_mode]


def set_custom_timeout_and_retry(instance_id, database_id):
    """Executes a snapshot read with custom timeout and retry."""
    # [START spanner_set_custom_timeout_and_retry]
    from google.api_core import exceptions as core_exceptions
    from google.api_core import retry

    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    retry = retry.Retry(
        # Customize retry with an initial wait time of 500 milliseconds.
        initial=0.5,
        # Customize retry with a maximum wait time of 16 seconds.
        maximum=16,
        # Customize retry with a wait time multiplier per iteration of 1.5.
        multiplier=1.5,
        # Customize retry with a timeout on
        # how long a certain RPC may be retried in
        # case the server returns an error.
        timeout=60,
        # Configure which errors should be retried.
        predicate=retry.if_exception_type(
            core_exceptions.ServiceUnavailable,
        ),
    )

    # Set a custom retry and timeout setting.
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, AlbumTitle FROM Albums",
            # Set custom retry setting for this request
            retry=retry,
            # Set custom timeout of 60 seconds for this request
            timeout=60,
        )

        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))

    # [END spanner_set_custom_timeout_and_retry]


# [START spanner_create_instance_with_autoscaling_config]
def create_instance_with_autoscaling_config(instance_id):
    """Creates a Cloud Spanner instance with an autoscaling configuration."""
    from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin

    spanner_client = spanner.Client()

    config_name = "{}/instanceConfigs/regional-us-central1".format(
        spanner_client.project_name
    )

    autoscaling_config = spanner_instance_admin.AutoscalingConfig(
        # Only one of minNodes/maxNodes or minProcessingUnits/maxProcessingUnits can be set.
        autoscaling_limits=spanner_instance_admin.AutoscalingConfig.AutoscalingLimits(
            min_nodes=1,
            max_nodes=2,
        ),
        # highPriorityCpuUtilizationPercent and storageUtilizationPercent are both
        # percentages and must lie between 0 and 100.
        autoscaling_targets=spanner_instance_admin.AutoscalingConfig.AutoscalingTargets(
            high_priority_cpu_utilization_percent=65,
            storage_utilization_percent=95,
        ),
    )

    #  Creates a new instance with autoscaling configuration
    #  When autoscalingConfig is enabled, nodeCount and processingUnits fields
    #  need not be specified.
    request = spanner_instance_admin.CreateInstanceRequest(
        parent=spanner_client.project_name,
        instance_id=instance_id,
        instance=spanner_instance_admin.Instance(
            config=config_name,
            display_name="This is a display name.",
            autoscaling_config=autoscaling_config,
            labels={
                "cloud_spanner_samples": "true",
                "sample_name": "snippets-create_instance_with_autoscaling_config",
                "created": str(int(time.time())),
            },
            edition=spanner_instance_admin.Instance.Edition.ENTERPRISE,  # Optional
        ),
    )

    operation = spanner_client.instance_admin_api.create_instance(request=request)

    print("Waiting for operation to complete...")
    instance = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created instance {} with {} autoscaling config".format(
            instance_id, instance.autoscaling_config
        )
    )


# [END spanner_create_instance_with_autoscaling_config]


# [START spanner_create_instance_without_default_backup_schedule]
def create_instance_without_default_backup_schedules(instance_id):
    spanner_client = spanner.Client()
    config_name = "{}/instanceConfigs/regional-me-central2".format(
        spanner_client.project_name
    )

    operation = spanner_client.instance_admin_api.create_instance(
        parent=spanner_client.project_name,
        instance_id=instance_id,
        instance=spanner_instance_admin.Instance(
            config=config_name,
            display_name="This is a display name.",
            node_count=1,
            default_backup_schedule_type=spanner_instance_admin.Instance.DefaultBackupScheduleType.NONE,  # Optional
        ),
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created instance {} without default backup schedules".format(instance_id))


# [END spanner_create_instance_without_default_backup_schedule]


# [START spanner_update_instance_default_backup_schedule_type]
def update_instance_default_backup_schedule_type(instance_id):
    spanner_client = spanner.Client()

    name = "{}/instances/{}".format(spanner_client.project_name, instance_id)

    operation = spanner_client.instance_admin_api.update_instance(
        instance=spanner_instance_admin.Instance(
            name=name,
            default_backup_schedule_type=spanner_instance_admin.Instance.DefaultBackupScheduleType.AUTOMATIC,  # Optional
        ),
        field_mask=field_mask_pb2.FieldMask(paths=["default_backup_schedule_type"]),
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Updated instance {} to have default backup schedules".format(instance_id))


# [END spanner_update_instance_default_backup_schedule_type]


def add_proto_type_columns(instance_id, database_id):
    # [START spanner_add_proto_type_columns]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    """Adds a new Proto Message column and Proto Enum column to the Singers table."""

    import os

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "testdata/descriptors.pb")

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    proto_descriptor_file = open(filename, "rb")
    proto_descriptor = proto_descriptor_file.read()

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            """CREATE PROTO BUNDLE (
            examples.spanner.music.SingerInfo,
            examples.spanner.music.Genre,
            )""",
            "ALTER TABLE Singers ADD COLUMN SingerInfo examples.spanner.music.SingerInfo",
            "ALTER TABLE Singers ADD COLUMN SingerInfoArray ARRAY<examples.spanner.music.SingerInfo>",
            "ALTER TABLE Singers ADD COLUMN SingerGenre examples.spanner.music.Genre",
            "ALTER TABLE Singers ADD COLUMN SingerGenreArray ARRAY<examples.spanner.music.Genre>",
        ],
        proto_descriptors=proto_descriptor,
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)
    proto_descriptor_file.close()

    print(
        'Altered table "Singers" on database {} on instance {} with proto descriptors.'.format(
            database_id, instance_id
        )
    )
    # [END spanner_add_proto_type_columns]


def update_data_with_proto_types(instance_id, database_id):
    # [START spanner_update_data_with_proto_types]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    """Updates Singers tables in the database with the ProtoMessage
    and ProtoEnum column.

    This updates the `SingerInfo`, `SingerInfoArray`, `SingerGenre` and
    `SingerGenreArray` columns which must be created before
    running this sample. You can add the column by running the
    `add_proto_type_columns` sample or by running this DDL statement
     against your database:

         ALTER TABLE Singers ADD COLUMN SingerInfo examples.spanner.music.SingerInfo\n
         ALTER TABLE Singers ADD COLUMN SingerInfoArray ARRAY<examples.spanner.music.SingerInfo>\n
         ALTER TABLE Singers ADD COLUMN SingerGenre examples.spanner.music.Genre\n
         ALTER TABLE Singers ADD COLUMN SingerGenreArray ARRAY<examples.spanner.music.Genre>\n
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    singer_info = singer_pb2.SingerInfo()
    singer_info.singer_id = 2
    singer_info.birth_date = "February"
    singer_info.nationality = "Country2"
    singer_info.genre = singer_pb2.Genre.FOLK

    singer_info_array = [singer_info]

    singer_genre_array = [singer_pb2.Genre.FOLK]

    with database.batch() as batch:
        batch.update(
            table="Singers",
            columns=(
                "SingerId",
                "SingerInfo",
                "SingerInfoArray",
                "SingerGenre",
                "SingerGenreArray",
            ),
            values=[
                (
                    2,
                    singer_info,
                    singer_info_array,
                    singer_pb2.Genre.FOLK,
                    singer_genre_array,
                ),
                (3, None, None, None, None),
            ],
        )

    print("Data updated.")
    # [END spanner_update_data_with_proto_types]


def update_data_with_proto_types_with_dml(instance_id, database_id):
    # [START spanner_update_data_with_proto_types_with_dml]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    """Updates Singers tables in the database with the ProtoMessage
    and ProtoEnum column.

    This updates the `SingerInfo`, `SingerInfoArray`, `SingerGenre` and `SingerGenreArray` columns which must be created before
    running this sample. You can add the column by running the
    `add_proto_type_columns` sample or by running this DDL statement
     against your database:

         ALTER TABLE Singers ADD COLUMN SingerInfo examples.spanner.music.SingerInfo\n
         ALTER TABLE Singers ADD COLUMN SingerInfoArray ARRAY<examples.spanner.music.SingerInfo>\n
         ALTER TABLE Singers ADD COLUMN SingerGenre examples.spanner.music.Genre\n
         ALTER TABLE Singers ADD COLUMN SingerGenreArray ARRAY<examples.spanner.music.Genre>\n
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    singer_info = singer_pb2.SingerInfo()
    singer_info.singer_id = 1
    singer_info.birth_date = "January"
    singer_info.nationality = "Country1"
    singer_info.genre = singer_pb2.Genre.ROCK

    singer_info_array = [singer_info, None]

    singer_genre_array = [singer_pb2.Genre.ROCK, None]

    def update_singers_with_proto_types(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Singers "
            "SET SingerInfo = @singerInfo,  SingerInfoArray=@singerInfoArray, "
            "SingerGenre=@singerGenre, SingerGenreArray=@singerGenreArray "
            "WHERE SingerId = 1",
            params={
                "singerInfo": singer_info,
                "singerInfoArray": singer_info_array,
                "singerGenre": singer_pb2.Genre.ROCK,
                "singerGenreArray": singer_genre_array,
            },
            param_types={
                "singerInfo": param_types.ProtoMessage(singer_info),
                "singerInfoArray": param_types.Array(
                    param_types.ProtoMessage(singer_info)
                ),
                "singerGenre": param_types.ProtoEnum(singer_pb2.Genre),
                "singerGenreArray": param_types.Array(
                    param_types.ProtoEnum(singer_pb2.Genre)
                ),
            },
        )

        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(update_singers_with_proto_types)

    def update_singers_with_proto_field(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Singers "
            "SET SingerInfo.nationality = @singerNationality "
            "WHERE SingerId = 1",
            params={
                "singerNationality": "Country2",
            },
            param_types={
                "singerNationality": param_types.STRING,
            },
        )

        print("{} record(s) updated.".format(row_ct))

    database.run_in_transaction(update_singers_with_proto_field)
    # [END spanner_update_data_with_proto_types_with_dml]


def query_data_with_proto_types_parameter(instance_id, database_id):
    # [START spanner_query_with_proto_types_parameter]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, SingerInfo, SingerInfo.nationality, SingerInfoArray, "
            "SingerGenre, SingerGenreArray FROM Singers "
            "WHERE SingerInfo.Nationality=@country "
            "and SingerGenre=@singerGenre",
            params={
                "country": "Country2",
                "singerGenre": singer_pb2.Genre.FOLK,
            },
            param_types={
                "country": param_types.STRING,
                "singerGenre": param_types.ProtoEnum(singer_pb2.Genre),
            },
            # column_info is an optional parameter and is used to deserialize
            # the proto message and enum object back from bytearray and
            # int respectively.
            # If column_info is not passed for proto messages and enums, then
            # the data types for these columns will be bytes and int
            # respectively.
            column_info={
                "SingerInfo": singer_pb2.SingerInfo(),
                "SingerInfoArray": singer_pb2.SingerInfo(),
                "SingerGenre": singer_pb2.Genre,
                "SingerGenreArray": singer_pb2.Genre,
            },
        )

        for row in results:
            print(
                "SingerId: {}, SingerInfo: {}, SingerInfoNationality: {}, "
                "SingerInfoArray: {}, SingerGenre: {}, SingerGenreArray: {}".format(
                    *row
                )
            )
    # [END spanner_query_with_proto_types_parameter]


# [START spanner_database_add_split_points]
def add_split_points(instance_id, database_id):
    """Adds split points to table and index."""

    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.UpdateDatabaseDdlRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        statements=[
            "CREATE INDEX IF NOT EXISTS SingersByFirstLastName ON Singers(FirstName, LastName)"
        ],
    )

    operation = database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the SingersByFirstLastName index.")

    addSplitPointRequest = spanner_database_admin.AddSplitPointsRequest(
        database=database_admin_api.database_path(
            spanner_client.project, instance_id, database_id
        ),
        # Table split
        # Index split without table key part
        # Index split with table key part: first key is the index key and second the table key
        split_points=[
            spanner_database_admin.SplitPoints(
                table="Singers",
                keys=[
                    spanner_database_admin.SplitPoints.Key(
                        key_parts=struct_pb2.ListValue(
                            values=[struct_pb2.Value(string_value="42")]
                        )
                    )
                ],
            ),
            spanner_database_admin.SplitPoints(
                index="SingersByFirstLastName",
                keys=[
                    spanner_database_admin.SplitPoints.Key(
                        key_parts=struct_pb2.ListValue(
                            values=[
                                struct_pb2.Value(string_value="John"),
                                struct_pb2.Value(string_value="Doe"),
                            ]
                        )
                    )
                ],
            ),
            spanner_database_admin.SplitPoints(
                index="SingersByFirstLastName",
                keys=[
                    spanner_database_admin.SplitPoints.Key(
                        key_parts=struct_pb2.ListValue(
                            values=[
                                struct_pb2.Value(string_value="Jane"),
                                struct_pb2.Value(string_value="Doe"),
                            ]
                        )
                    ),
                    spanner_database_admin.SplitPoints.Key(
                        key_parts=struct_pb2.ListValue(
                            values=[struct_pb2.Value(string_value="38")]
                        )
                    ),
                ],
            ),
        ],
    )

    operation = database_admin_api.add_split_points(addSplitPointRequest)

    print("Added split points.")


# [END spanner_database_add_split_points]


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
    subparsers.add_parser("update_instance", help=update_instance.__doc__)
    subparsers.add_parser("create_database", help=create_database.__doc__)
    subparsers.add_parser("insert_data", help=insert_data.__doc__)
    subparsers.add_parser("batch_write", help=batch_write.__doc__)
    subparsers.add_parser("delete_data", help=delete_data.__doc__)
    subparsers.add_parser("query_data", help=query_data.__doc__)
    subparsers.add_parser("read_data", help=read_data.__doc__)
    subparsers.add_parser("read_stale_data", help=read_stale_data.__doc__)
    subparsers.add_parser("add_column", help=add_column.__doc__)
    subparsers.add_parser("update_data", help=update_data.__doc__)
    subparsers.add_parser("set_max_commit_delay", help=set_max_commit_delay.__doc__)
    subparsers.add_parser(
        "set_transaction_timeout", help=set_transaction_timeout.__doc__
    )
    subparsers.add_parser("set_statement_timeout", help=set_statement_timeout.__doc__)
    subparsers.add_parser(
        "query_data_with_new_column", help=query_data_with_new_column.__doc__
    )
    subparsers.add_parser("read_write_transaction", help=read_write_transaction.__doc__)
    subparsers.add_parser("read_only_transaction", help=read_only_transaction.__doc__)
    subparsers.add_parser("add_index", help=add_index.__doc__)
    query_data_with_index_parser = subparsers.add_parser(
        "query_data_with_index", help=query_data_with_index.__doc__
    )
    query_data_with_index_parser.add_argument("--start_title", default="Aardvark")
    query_data_with_index_parser.add_argument("--end_title", default="Goo")
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
    subparsers.add_parser("write_struct_data", help=write_struct_data.__doc__)
    subparsers.add_parser("query_with_struct", help=query_with_struct.__doc__)
    subparsers.add_parser(
        "query_with_array_of_struct", help=query_with_array_of_struct.__doc__
    )
    subparsers.add_parser("query_struct_field", help=query_struct_field.__doc__)
    subparsers.add_parser(
        "query_nested_struct_field", help=query_nested_struct_field.__doc__
    )
    subparsers.add_parser("insert_data_with_dml", help=insert_data_with_dml.__doc__)
    subparsers.add_parser("log_commit_stats", help=log_commit_stats.__doc__)
    subparsers.add_parser("update_data_with_dml", help=update_data_with_dml.__doc__)
    subparsers.add_parser(
        "update_data_with_dml_returning", help=update_data_with_dml_returning.__doc__
    )
    subparsers.add_parser("delete_data_with_dml", help=delete_data_with_dml.__doc__)
    subparsers.add_parser(
        "delete_data_with_dml_returning", help=delete_data_with_dml_returning.__doc__
    )
    subparsers.add_parser(
        "update_data_with_dml_timestamp", help=update_data_with_dml_timestamp.__doc__
    )
    subparsers.add_parser(
        "dml_write_read_transaction", help=dml_write_read_transaction.__doc__
    )
    subparsers.add_parser(
        "update_data_with_dml_struct", help=update_data_with_dml_struct.__doc__
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
    subparsers.add_parser("query_data_with_array", help=query_data_with_array.__doc__)
    subparsers.add_parser("query_data_with_bool", help=query_data_with_bool.__doc__)
    subparsers.add_parser("query_data_with_bytes", help=query_data_with_bytes.__doc__)
    subparsers.add_parser("query_data_with_date", help=query_data_with_date.__doc__)
    subparsers.add_parser("query_data_with_float", help=query_data_with_float.__doc__)
    subparsers.add_parser("query_data_with_int", help=query_data_with_int.__doc__)
    subparsers.add_parser("query_data_with_string", help=query_data_with_string.__doc__)
    subparsers.add_parser(
        "query_data_with_timestamp_parameter",
        help=query_data_with_timestamp_parameter.__doc__,
    )
    subparsers.add_parser(
        "query_data_with_query_options", help=query_data_with_query_options.__doc__
    )
    subparsers.add_parser(
        "create_client_with_query_options",
        help=create_client_with_query_options.__doc__,
    )
    subparsers.add_parser(
        "add_and_drop_database_roles", help=add_and_drop_database_roles.__doc__
    )
    subparsers.add_parser(
        "read_data_with_database_role", help=read_data_with_database_role.__doc__
    )
    subparsers.add_parser("list_database_roles", help=list_database_roles.__doc__)
    subparsers.add_parser("create_sequence", help=create_sequence.__doc__)
    subparsers.add_parser("alter_sequence", help=alter_sequence.__doc__)
    subparsers.add_parser("drop_sequence", help=drop_sequence.__doc__)

    enable_fine_grained_access_parser = subparsers.add_parser(
        "enable_fine_grained_access", help=enable_fine_grained_access.__doc__
    )
    enable_fine_grained_access_parser.add_argument(
        "--iam_member", default="user:alice@example.com"
    )
    enable_fine_grained_access_parser.add_argument(
        "--database_role", default="new_parent"
    )
    enable_fine_grained_access_parser.add_argument("--title", default="condition title")
    subparsers.add_parser("directed_read_options", help=directed_read_options.__doc__)
    subparsers.add_parser(
        "isolation_level_options", help=isolation_level_options.__doc__
    )
    subparsers.add_parser("read_lock_mode_options", help=read_lock_mode_options.__doc__)
    subparsers.add_parser(
        "set_custom_timeout_and_retry", help=set_custom_timeout_and_retry.__doc__
    )
    subparsers.add_parser("add_proto_type_columns", help=add_proto_type_columns.__doc__)
    subparsers.add_parser(
        "update_data_with_proto_types", help=update_data_with_proto_types.__doc__
    )
    subparsers.add_parser(
        "update_data_with_proto_types_with_dml",
        help=update_data_with_proto_types_with_dml.__doc__,
    )
    subparsers.add_parser(
        "query_data_with_proto_types_parameter",
        help=query_data_with_proto_types_parameter.__doc__,
    )
    subparsers.add_parser(
        "add_split_points",
        help=add_split_points.__doc__,
    )

    args = parser.parse_args()

    if args.command == "create_instance":
        create_instance(args.instance_id)
    if args.command == "update_instance":
        update_instance(args.instance_id)
    elif args.command == "create_database":
        create_database(args.instance_id, args.database_id)
    elif args.command == "insert_data":
        insert_data(args.instance_id, args.database_id)
    elif args.command == "batch_write":
        batch_write(args.instance_id, args.database_id)
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
    elif args.command == "set_max_commit_delay":
        set_max_commit_delay(args.instance_id, args.database_id)
    elif args.command == "set_transaction_timeout":
        set_transaction_timeout(args.instance_id, args.database_id)
    elif args.command == "set_statement_timeout":
        set_statement_timeout(args.instance_id, args.database_id)
    elif args.command == "query_data_with_new_column":
        query_data_with_new_column(args.instance_id, args.database_id)
    elif args.command == "read_write_transaction":
        read_write_transaction(args.instance_id, args.database_id)
    elif args.command == "read_only_transaction":
        read_only_transaction(args.instance_id, args.database_id)
    elif args.command == "add_index":
        add_index(args.instance_id, args.database_id)
    elif args.command == "query_data_with_index":
        query_data_with_index(
            args.instance_id, args.database_id, args.start_title, args.end_title
        )
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
    elif args.command == "write_struct_data":
        write_struct_data(args.instance_id, args.database_id)
    elif args.command == "query_with_struct":
        query_with_struct(args.instance_id, args.database_id)
    elif args.command == "query_with_array_of_struct":
        query_with_array_of_struct(args.instance_id, args.database_id)
    elif args.command == "query_struct_field":
        query_struct_field(args.instance_id, args.database_id)
    elif args.command == "query_nested_struct_field":
        query_nested_struct_field(args.instance_id, args.database_id)
    elif args.command == "insert_data_with_dml":
        insert_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "log_commit_stats":
        log_commit_stats(args.instance_id, args.database_id)
    elif args.command == "update_data_with_dml":
        update_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "update_data_with_dml_returning":
        update_data_with_dml_returning(args.instance_id, args.database_id)
    elif args.command == "delete_data_with_dml":
        delete_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "delete_data_with_dml_returning":
        delete_data_with_dml_returning(args.instance_id, args.database_id)
    elif args.command == "update_data_with_dml_timestamp":
        update_data_with_dml_timestamp(args.instance_id, args.database_id)
    elif args.command == "dml_write_read_transaction":
        dml_write_read_transaction(args.instance_id, args.database_id)
    elif args.command == "update_data_with_dml_struct":
        update_data_with_dml_struct(args.instance_id, args.database_id)
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
    elif args.command == "query_data_with_array":
        query_data_with_array(args.instance_id, args.database_id)
    elif args.command == "query_data_with_bool":
        query_data_with_bool(args.instance_id, args.database_id)
    elif args.command == "query_data_with_bytes":
        query_data_with_bytes(args.instance_id, args.database_id)
    elif args.command == "query_data_with_date":
        query_data_with_date(args.instance_id, args.database_id)
    elif args.command == "query_data_with_float":
        query_data_with_float(args.instance_id, args.database_id)
    elif args.command == "query_data_with_int":
        query_data_with_int(args.instance_id, args.database_id)
    elif args.command == "query_data_with_string":
        query_data_with_string(args.instance_id, args.database_id)
    elif args.command == "query_data_with_timestamp_parameter":
        query_data_with_timestamp_parameter(args.instance_id, args.database_id)
    elif args.command == "query_data_with_query_options":
        query_data_with_query_options(args.instance_id, args.database_id)
    elif args.command == "create_client_with_query_options":
        create_client_with_query_options(args.instance_id, args.database_id)
    elif args.command == "add_and_drop_database_roles":
        add_and_drop_database_roles(args.instance_id, args.database_id)
    elif args.command == "read_data_with_database_role":
        read_data_with_database_role(args.instance_id, args.database_id)
    elif args.command == "list_database_roles":
        list_database_roles(args.instance_id, args.database_id)
    elif args.command == "enable_fine_grained_access":
        enable_fine_grained_access(
            args.instance_id,
            args.database_id,
            args.iam_member,
            args.database_role,
            args.title,
        )
    elif args.command == "directed_read_options":
        directed_read_options(args.instance_id, args.database_id)
    elif args.command == "isolation_level_options":
        isolation_level_options(args.instance_id, args.database_id)
    elif args.command == "read_lock_mode_options":
        read_lock_mode_options(args.instance_id, args.database_id)
    elif args.command == "set_custom_timeout_and_retry":
        set_custom_timeout_and_retry(args.instance_id, args.database_id)
    elif args.command == "create_instance_with_autoscaling_config":
        create_instance_with_autoscaling_config(args.instance_id)
    elif args.command == "add_proto_type_columns":
        add_proto_type_columns(args.instance_id, args.database_id)
    elif args.command == "update_data_with_proto_types":
        update_data_with_proto_types(args.instance_id, args.database_id)
    elif args.command == "update_data_with_proto_types_with_dml":
        update_data_with_proto_types_with_dml(args.instance_id, args.database_id)
    elif args.command == "query_data_with_proto_types_parameter":
        query_data_with_proto_types_parameter(args.instance_id, args.database_id)
    elif args.command == "add_split_points":
        add_split_points(args.instance_id, args.database_id)
