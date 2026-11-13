#!/usr/bin/env python

# Copyright 2026 Google, Inc.
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

"""This application demonstrates how to do basic queue operations using
Cloud Spanner.

For more information, see the README.rst under /spanner.
"""

import argparse
import datetime

from google.api_core import exceptions
from google.cloud import spanner

OPERATION_TIMEOUT_SECONDS = 240


# [START spanner_create_database_with_queue]
def create_database_with_queue(instance_id, database_id, queue_id):
    """Creates a database and a queue."""
    from google.cloud.spanner_admin_database_v1.types import spanner_database_admin

    spanner_client = spanner.Client()
    database_admin_api = spanner_client.database_admin_api

    request = spanner_database_admin.CreateDatabaseRequest(
        parent=database_admin_api.instance_path(spanner_client.project, instance_id),
        create_statement=f"CREATE DATABASE `{database_id}`",
        extra_statements=[
            f"""CREATE QUEUE {queue_id} (
                Id INT64 NOT NULL,
                Payload STRING(MAX) NOT NULL
            ) PRIMARY KEY (Id)"""
        ],
    )

    operation = database_admin_api.create_database(request=request)

    print("Waiting for operation to complete...")
    database = operation.result(OPERATION_TIMEOUT_SECONDS)

    print(
        "Created database {} on instance {} with queue {}".format(
            database.name,
            database_admin_api.instance_path(spanner_client.project, instance_id),
            queue_id,
        )
    )


# [END spanner_create_database_with_queue]


# [START spanner_send_to_queue_with_mutation_api]
def send_to_queue_with_mutation_api(instance_id, database_id, queue_id):
    """Send to a queue with Mutation API."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.batch() as batch:
        batch.send(
            queue=queue_id,
            key=(1,),
            payload="Hello, Mutation API!",
        )
    print("Message sent to queue using Mutation API.")


# [END spanner_send_to_queue_with_mutation_api]


# [START spanner_send_to_queue_with_sql_api]
def send_to_queue_with_sql_api(instance_id, database_id, queue_id):
    """Send to a queue with SQL API (sql insert)."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_message(transaction):
        row_ct = transaction.execute_update(
            f"INSERT INTO {queue_id} (Id, Payload) VALUES (2, 'Hello, SQL API!')"
        )
        print(f"{row_ct} message(s) sent using SQL API.")

    database.run_in_transaction(insert_message)


# [END spanner_send_to_queue_with_sql_api]


# [START spanner_send_to_queue_with_mutation_api_in_future]
def send_to_queue_with_mutation_api_in_future(instance_id, database_id, queue_id):
    """Send to a queue with Mutation API in the future."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    # Deliver time 1 hour in the future
    deliver_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        hours=1
    )

    with database.batch() as batch:
        batch.send(
            queue=queue_id,
            key=(3,),
            payload="Hello, Mutation API in the future!",
            deliver_time=deliver_time,
        )
    print("Message sent to queue using Mutation API to be delivered in the future.")


# [END spanner_send_to_queue_with_mutation_api_in_future]


# [START spanner_send_to_queue_with_sql_api_in_future]
def send_to_queue_with_sql_api_in_future(instance_id, database_id, queue_id):
    """Send to a queue with SQL API in the future."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_message_in_future(transaction):
        row_ct = transaction.execute_update(
            f"INSERT INTO {queue_id} (Id, Payload, _deliver_time) VALUES (4, 'Hello, SQL API in the future!', TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR))"
        )
        print(f"{row_ct} message(s) sent using SQL API in the future.")

    try:
        database.run_in_transaction(insert_message_in_future)
    except exceptions.InvalidArgument as e:
        print(f"Failed to insert with _deliver_time: {e}")


# [END spanner_send_to_queue_with_sql_api_in_future]


# [START spanner_ack_queue_message_with_mutation_api]
def ack_queue_message_with_mutation_api(instance_id, database_id, queue_id):
    """Ack a queue message with Mutation API."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.batch() as batch:
        batch.ack(
            queue=queue_id,
            key=(1,),
        )
    print("Message acked using Mutation API.")


# [END spanner_ack_queue_message_with_mutation_api]


# [START spanner_ack_queue_message_with_sql_api]
def ack_queue_message_with_sql_api(instance_id, database_id, queue_id):
    """Ack a queue message with SQL API (DELETE ASSERT_ROWS_MODIFIED 1)."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def ack_message(transaction):
        row_ct = transaction.execute_update(
            f"DELETE FROM {queue_id} WHERE Id = 2 ASSERT_ROWS_MODIFIED 1"
        )
        print(f"{row_ct} message(s) acked using SQL API.")

    database.run_in_transaction(ack_message)


# [END spanner_ack_queue_message_with_sql_api]


# [START spanner_delete_queue_message_with_sql_api]
def delete_queue_message_with_sql_api(instance_id, database_id, queue_id):
    """Delete a queue message with SQL API."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def delete_message(transaction):
        row_ct = transaction.execute_update(f"DELETE FROM {queue_id} WHERE Id = 4")
        print(f"{row_ct} message(s) deleted using SQL API.")

    database.run_in_transaction(delete_message)


# [END spanner_delete_queue_message_with_sql_api]


# [START spanner_send_and_receive_queue_message_with_sql_api]
def send_and_receive_queue_message_with_sql_api(instance_id, database_id, queue_id):
    """Send a message and receive it with SQL API."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    def insert_message(transaction):
        transaction.execute_update(
            f"INSERT INTO {queue_id} (Id, Payload) VALUES (5, 'Hello, SQL receive API!')"
        )

    database.run_in_transaction(insert_message)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            f"SELECT Id, Payload FROM RECEIVE_{queue_id}(max_duration => '1m')"
        )
        for row in results:
            print(f"Received message: Id={row[0]}, Payload={row[1]}")


# [END spanner_send_and_receive_queue_message_with_sql_api]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("instance_id", help="Your Cloud Spanner instance ID.")
    parser.add_argument(
        "--database-id", help="Your Cloud Spanner database ID.", default="example_db"
    )
    parser.add_argument(
        "--queue-id", help="Your Cloud Spanner queue ID.", default="example_queue"
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser(
        "create_database_with_queue", help=create_database_with_queue.__doc__
    )
    subparsers.add_parser(
        "send_to_queue_with_mutation_api", help=send_to_queue_with_mutation_api.__doc__
    )
    subparsers.add_parser(
        "send_to_queue_with_sql_api", help=send_to_queue_with_sql_api.__doc__
    )
    subparsers.add_parser(
        "send_to_queue_with_mutation_api_in_future",
        help=send_to_queue_with_mutation_api_in_future.__doc__,
    )
    subparsers.add_parser(
        "send_to_queue_with_sql_api_in_future",
        help=send_to_queue_with_sql_api_in_future.__doc__,
    )
    subparsers.add_parser(
        "ack_queue_message_with_mutation_api",
        help=ack_queue_message_with_mutation_api.__doc__,
    )
    subparsers.add_parser(
        "ack_queue_message_with_sql_api", help=ack_queue_message_with_sql_api.__doc__
    )

    subparsers.add_parser(
        "delete_queue_message_with_sql_api",
        help=delete_queue_message_with_sql_api.__doc__,
    )
    subparsers.add_parser(
        "send_and_receive_queue_message_with_sql_api",
        help=send_and_receive_queue_message_with_sql_api.__doc__,
    )

    args = parser.parse_args()

    if args.command == "create_database_with_queue":
        create_database_with_queue(args.instance_id, args.database_id, args.queue_id)
    elif args.command == "send_to_queue_with_mutation_api":
        send_to_queue_with_mutation_api(
            args.instance_id, args.database_id, args.queue_id
        )
    elif args.command == "send_to_queue_with_sql_api":
        send_to_queue_with_sql_api(args.instance_id, args.database_id, args.queue_id)
    elif args.command == "send_to_queue_with_mutation_api_in_future":
        send_to_queue_with_mutation_api_in_future(
            args.instance_id, args.database_id, args.queue_id
        )
    elif args.command == "send_to_queue_with_sql_api_in_future":
        send_to_queue_with_sql_api_in_future(
            args.instance_id, args.database_id, args.queue_id
        )
    elif args.command == "ack_queue_message_with_mutation_api":
        ack_queue_message_with_mutation_api(
            args.instance_id, args.database_id, args.queue_id
        )
    elif args.command == "ack_queue_message_with_sql_api":
        ack_queue_message_with_sql_api(
            args.instance_id, args.database_id, args.queue_id
        )

    elif args.command == "delete_queue_message_with_sql_api":
        delete_queue_message_with_sql_api(
            args.instance_id, args.database_id, args.queue_id
        )
    elif args.command == "send_and_receive_queue_message_with_sql_api":
        send_and_receive_queue_message_with_sql_api(
            args.instance_id, args.database_id, args.queue_id
        )
