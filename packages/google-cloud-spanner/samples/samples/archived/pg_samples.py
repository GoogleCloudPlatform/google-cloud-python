#!/usr/bin/env python

# Copyright 2024 Google, Inc.
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

from google.cloud import spanner, spanner_admin_database_v1
from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect

OPERATION_TIMEOUT_SECONDS = 240


# [START spanner_postgresql_add_column]
def add_column(instance_id, database_id):
    """Adds a new column to the Albums table in the example database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    operation = database.update_ddl(
        ["ALTER TABLE Albums ADD COLUMN MarketingBudget BIGINT"]
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the MarketingBudget column.")


# [END spanner_postgresql_add_column]


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

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    operation = database.update_ddl(
        ["ALTER TABLE Venues ADD COLUMN VenueDetails JSONB"]
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        'Altered table "Venues" on database {} on instance {}.'.format(
            database_id, instance_id
        )
    )


# [END spanner_postgresql_jsonb_add_column]


# [START spanner_postgresql_alter_sequence]
def alter_sequence(instance_id, database_id):
    """Alters the Sequence and insert data"""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    operation = database.update_ddl(["ALTER SEQUENCE Seq SKIP RANGE 1000 5000000"])

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

    database.run_in_transaction(insert_customers)


# [END spanner_postgresql_alter_sequence]


# [START spanner_postgresql_create_database]
def create_database(instance_id, database_id):
    """Creates a PostgreSql database and tables for sample data."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)

    database = instance.database(
        database_id,
        database_dialect=DatabaseDialect.POSTGRESQL,
    )

    operation = database.create()

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    create_table_using_ddl(database.name)
    print("Created database {} on instance {}".format(database_id, instance_id))


def create_table_using_ddl(database_name):
    spanner_client = spanner.Client()
    request = spanner_admin_database_v1.UpdateDatabaseDdlRequest(
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


# [START spanner_postgresql_create_sequence]
def create_sequence(instance_id, database_id):
    """Creates the Sequence and insert data"""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    request = spanner_admin_database_v1.UpdateDatabaseDdlRequest(
        database=database.name,
        statements=[
            "CREATE SEQUENCE Seq BIT_REVERSED_POSITIVE",
            """CREATE TABLE Customers (
        CustomerId  BIGINT DEFAULT nextval('Seq'),
        CustomerName  character varying(1024),
        PRIMARY KEY (CustomerId)
        )""",
        ],
    )
    operation = spanner_client.database_admin_api.update_database_ddl(request)
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

    database.run_in_transaction(insert_customers)


# [END spanner_postgresql_create_sequence]


# [START spanner_postgresql_create_storing_index]
def add_storing_index(instance_id, database_id):
    """Adds an storing index to the example database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    operation = database.update_ddl(
        [
            "CREATE INDEX AlbumsByAlbumTitle2 ON Albums(AlbumTitle)"
            "INCLUDE (MarketingBudget)"
        ]
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Added the AlbumsByAlbumTitle2 index.")


# [END spanner_postgresql_create_storing_index]


# [START spanner_postgresql_drop_sequence]
def drop_sequence(instance_id, database_id):
    """Drops the Sequence"""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    operation = database.update_ddl(
        [
            "ALTER TABLE Customers ALTER COLUMN CustomerId DROP DEFAULT",
            "DROP SEQUENCE Seq",
        ]
    )

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Altered Customers table to drop DEFAULT from CustomerId column and dropped the Seq sequence on database {} on instance {}".format(
            database_id, instance_id
        )
    )


# [END spanner_postgresql_drop_sequence]


def create_table_with_datatypes(instance_id, database_id):
    """Creates a table with supported datatypes."""
    # [START spanner_postgresql_create_table_with_datatypes]
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    request = spanner_admin_database_v1.UpdateDatabaseDdlRequest(
        database=database.name,
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
    operation = spanner_client.database_admin_api.update_database_ddl(request)

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created Venues table on database {} on instance {}".format(
            database_id, instance_id
        )
    )
    # [END spanner_postgresql_create_table_with_datatypes]
