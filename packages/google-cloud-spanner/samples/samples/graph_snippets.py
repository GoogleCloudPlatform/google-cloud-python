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

"""This application demonstrates how to do basic graph operations using
Cloud Spanner.

For more information, see the README.rst under /spanner.
"""

import argparse

from google.cloud import spanner

OPERATION_TIMEOUT_SECONDS = 240


# [START spanner_create_database_with_property_graph]
def create_database_with_property_graph(instance_id, database_id):
    """Creates a database, tables and a property graph for sample data."""
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f"CREATE DATABASE `{database_id}`",
        extra_statements=[
            """CREATE TABLE Person (
            id               INT64 NOT NULL,
            name             STRING(MAX),
            birthday         TIMESTAMP,
            country          STRING(MAX),
            city             STRING(MAX),
        ) PRIMARY KEY (id)""",
            """CREATE TABLE Account (
            id               INT64 NOT NULL,
            create_time      TIMESTAMP,
            is_blocked       BOOL,
            nick_name        STRING(MAX),
        ) PRIMARY KEY (id)""",
            """CREATE TABLE PersonOwnAccount (
            id               INT64 NOT NULL,
            account_id       INT64 NOT NULL,
            create_time      TIMESTAMP,
            FOREIGN KEY (account_id)
                REFERENCES Account (id)
        ) PRIMARY KEY (id, account_id),
        INTERLEAVE IN PARENT Person ON DELETE CASCADE""",
            """CREATE TABLE AccountTransferAccount (
            id               INT64 NOT NULL,
            to_id            INT64 NOT NULL,
            amount           FLOAT64,
            create_time      TIMESTAMP NOT NULL,
            order_number     STRING(MAX),
            FOREIGN KEY (to_id) REFERENCES Account (id)
        ) PRIMARY KEY (id, to_id, create_time),
        INTERLEAVE IN PARENT Account ON DELETE CASCADE""",
            """CREATE OR REPLACE PROPERTY GRAPH FinGraph
            NODE TABLES (Account, Person)
            EDGE TABLES (
                PersonOwnAccount
                    SOURCE KEY(id) REFERENCES Person(id)
                    DESTINATION KEY(account_id) REFERENCES Account(id)
                    LABEL Owns,
                AccountTransferAccount
                    SOURCE KEY(id) REFERENCES Account(id)
                    DESTINATION KEY(to_id) REFERENCES Account(id)
                    LABEL Transfers)""",
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


# [END spanner_create_database_with_property_graph]


# [START spanner_insert_graph_data]
def insert_data(instance_id, database_id):
    """Inserts sample data into the given database.

    The database and tables must already exist and can be created using
    `create_database_with_property_graph`.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.batch() as batch:
        batch.insert(
            table="Account",
            columns=("id", "create_time", "is_blocked", "nick_name"),
            values=[
                (7, "2020-01-10T06:22:20.12Z", False, "Vacation Fund"),
                (16, "2020-01-27T17:55:09.12Z", True, "Vacation Fund"),
                (20, "2020-02-18T05:44:20.12Z", False, "Rainy Day Fund"),
            ],
        )

        batch.insert(
            table="Person",
            columns=("id", "name", "birthday", "country", "city"),
            values=[
                (1, "Alex", "1991-12-21T00:00:00.12Z", "Australia", " Adelaide"),
                (2, "Dana", "1980-10-31T00:00:00.12Z", "Czech_Republic", "Moravia"),
                (3, "Lee", "1986-12-07T00:00:00.12Z", "India", "Kollam"),
            ],
        )

        batch.insert(
            table="AccountTransferAccount",
            columns=("id", "to_id", "amount", "create_time", "order_number"),
            values=[
                (7, 16, 300.0, "2020-08-29T15:28:58.12Z", "304330008004315"),
                (7, 16, 100.0, "2020-10-04T16:55:05.12Z", "304120005529714"),
                (16, 20, 300.0, "2020-09-25T02:36:14.12Z", "103650009791820"),
                (20, 7, 500.0, "2020-10-04T16:55:05.12Z", "304120005529714"),
                (20, 16, 200.0, "2020-10-17T03:59:40.12Z", "302290001255747"),
            ],
        )

        batch.insert(
            table="PersonOwnAccount",
            columns=("id", "account_id", "create_time"),
            values=[
                (1, 7, "2020-01-10T06:22:20.12Z"),
                (2, 20, "2020-01-27T17:55:09.12Z"),
                (3, 16, "2020-02-18T05:44:20.12Z"),
            ],
        )

    print("Inserted data.")


# [END spanner_insert_graph_data]


# [START spanner_insert_graph_data_with_dml]
def insert_data_with_dml(instance_id, database_id):
    """Inserts sample data into the given database using a DML statement."""

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_accounts(transaction):
        row_ct = transaction.execute_update(
            "INSERT INTO Account (id, create_time, is_blocked) "
            "  VALUES"
            "    (1, CAST('2000-08-10 08:18:48.463959-07:52' AS TIMESTAMP), false),"
            "    (2, CAST('2000-08-12 07:13:16.463959-03:41' AS TIMESTAMP), true)"
        )

        print("{} record(s) inserted into Account.".format(row_ct))

    def insert_transfers(transaction):
        row_ct = transaction.execute_update(
            "INSERT INTO AccountTransferAccount (id, to_id, create_time, amount) "
            "  VALUES"
            "    (1, 2, CAST('2000-09-11 03:11:18.463959-06:36' AS TIMESTAMP), 100),"
            "    (1, 1, CAST('2000-09-12 04:09:34.463959-05:12' AS TIMESTAMP), 200) "
        )

        print("{} record(s) inserted into AccountTransferAccount.".format(row_ct))

    database.run_in_transaction(insert_accounts)
    database.run_in_transaction(insert_transfers)


# [END spanner_insert_graph_data_with_dml]


# [START spanner_update_graph_data_with_dml]
def update_data_with_dml(instance_id, database_id):
    """Updates sample data from the database using a DML statement."""

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def update_accounts(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Account SET is_blocked = false WHERE id = 2"
        )

        print("{} Account record(s) updated.".format(row_ct))

    def update_transfers(transaction):
        row_ct = transaction.execute_update(
            "UPDATE AccountTransferAccount SET amount = 300 WHERE id = 1 AND to_id = 2"
        )

        print("{} AccountTransferAccount record(s) updated.".format(row_ct))

    database.run_in_transaction(update_accounts)
    database.run_in_transaction(update_transfers)


# [END spanner_update_graph_data_with_dml]


# [START spanner_update_graph_data_with_graph_query_in_dml]
def update_data_with_graph_query_in_dml(instance_id, database_id):
    """Updates sample data from the database using a DML statement."""

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def update_accounts(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Account SET is_blocked = true "
            "WHERE id IN {"
            "  GRAPH FinGraph"
            "  MATCH (a:Account WHERE a.id = 1)-[:TRANSFERS]->{1,2}(b:Account)"
            "  RETURN b.id}"
        )

        print("{} Account record(s) updated.".format(row_ct))

    database.run_in_transaction(update_accounts)


# [END spanner_update_graph_data_with_graph_query_in_dml]


# [START spanner_query_graph_data]
def query_data(instance_id, database_id):
    """Queries sample data from the database using GQL."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            """Graph FinGraph
            MATCH (a:Person)-[o:Owns]->()-[t:Transfers]->()<-[p:Owns]-(b:Person)
            RETURN a.name AS sender, b.name AS receiver, t.amount, t.create_time AS transfer_at"""
        )

        for row in results:
            print("sender: {}, receiver: {}, amount: {}, transfer_at: {}".format(*row))


# [END spanner_query_graph_data]


# [START spanner_query_graph_data_with_parameter]
def query_data_with_parameter(instance_id, database_id):
    """Queries sample data from the database using SQL with a parameter."""

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            """Graph FinGraph
            MATCH (a:Person)-[o:Owns]->()-[t:Transfers]->()<-[p:Owns]-(b:Person)
            WHERE t.amount >= @min
            RETURN a.name AS sender, b.name AS receiver, t.amount, t.create_time AS transfer_at""",
            params={"min": 500},
            param_types={"min": spanner.param_types.INT64},
        )

        for row in results:
            print("sender: {}, receiver: {}, amount: {}, transfer_at: {}".format(*row))


# [END spanner_query_graph_data_with_parameter]


# [START spanner_delete_graph_data_with_dml]
def delete_data_with_dml(instance_id, database_id):
    """Deletes sample data from the database using a DML statement."""

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def delete_transfers(transaction):
        row_ct = transaction.execute_update(
            "DELETE FROM AccountTransferAccount WHERE id = 1 AND to_id = 2"
        )

        print("{} AccountTransferAccount record(s) deleted.".format(row_ct))

    def delete_accounts(transaction):
        row_ct = transaction.execute_update("DELETE FROM Account WHERE id = 2")

        print("{} Account record(s) deleted.".format(row_ct))

    database.run_in_transaction(delete_transfers)
    database.run_in_transaction(delete_accounts)


# [END spanner_delete_graph_data_with_dml]


# [START spanner_delete_graph_data]
def delete_data(instance_id, database_id):
    """Deletes sample data from the given database.

    The database, table, and data must already exist and can be created using
    `create_database` and `insert_data`.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Delete individual rows
    ownerships_to_delete = spanner.KeySet(keys=[[1, 7], [2, 20]])

    # Delete a range of rows where the column key is >=1 and <8
    transfers_range = spanner.KeyRange(start_closed=[1], end_open=[8])
    transfers_to_delete = spanner.KeySet(ranges=[transfers_range])

    # Delete Account/Person rows, which will also delete the remaining
    # AccountTransferAccount and PersonOwnAccount rows because
    # AccountTransferAccount and PersonOwnAccount are defined with
    # ON DELETE CASCADE
    remaining_nodes = spanner.KeySet(all_=True)

    with database.batch() as batch:
        batch.delete("PersonOwnAccount", ownerships_to_delete)
        batch.delete("AccountTransferAccount", transfers_to_delete)
        batch.delete("Account", remaining_nodes)
        batch.delete("Person", remaining_nodes)

    print("Deleted data.")


# [END spanner_delete_graph_data]


if __name__ == "__main__":  # noqa: C901
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("instance_id", help="Your Cloud Spanner instance ID.")
    parser.add_argument(
        "--database-id", help="Your Cloud Spanner database ID.", default="example_db"
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser(
        "create_database_with_property_graph",
        help=create_database_with_property_graph.__doc__,
    )
    subparsers.add_parser("insert_data", help=insert_data.__doc__)
    subparsers.add_parser("insert_data_with_dml", help=insert_data_with_dml.__doc__)
    subparsers.add_parser("update_data_with_dml", help=update_data_with_dml.__doc__)
    subparsers.add_parser(
        "update_data_with_graph_query_in_dml",
        help=update_data_with_graph_query_in_dml.__doc__,
    )
    subparsers.add_parser("query_data", help=query_data.__doc__)
    subparsers.add_parser(
        "query_data_with_parameter", help=query_data_with_parameter.__doc__
    )
    subparsers.add_parser("delete_data", help=delete_data.__doc__)
    subparsers.add_parser("delete_data_with_dml", help=delete_data_with_dml.__doc__)

    args = parser.parse_args()

    if args.command == "create_database_with_property_graph":
        create_database_with_property_graph(args.instance_id, args.database_id)
    elif args.command == "insert_data":
        insert_data(args.instance_id, args.database_id)
    elif args.command == "insert_data_with_dml":
        insert_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "update_data_with_dml":
        update_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "update_data_with_graph_query_in_dml":
        update_data_with_graph_query_in_dml(args.instance_id, args.database_id)
    elif args.command == "query_data":
        query_data(args.instance_id, args.database_id)
    elif args.command == "query_data_with_parameter":
        query_data_with_parameter(args.instance_id, args.database_id)
    elif args.command == "delete_data_with_dml":
        delete_data_with_dml(args.instance_id, args.database_id)
    elif args.command == "delete_data":
        delete_data(args.instance_id, args.database_id)
