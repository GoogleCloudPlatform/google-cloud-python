#!/usr/bin/env python

# Copyright 2026 Google LLC All rights reserved.
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

"""This application demonstrates how to do basic asynchronous operations using
Cloud Spanner.
"""

from google.cloud.spanner_v1 import AsyncClient, KeySet


# [START spanner_async_create_client]
async def async_create_client(instance_id, database_id):
    """Instantiates an asynchronous Spanner client."""
    spanner_client = AsyncClient()
    instance = spanner_client.instance(instance_id)
    database = await instance.database(database_id)

    print("Async Spanner client instantiated successfully.")
    return database


# [END spanner_async_create_client]


# [START spanner_async_query_data]
async def async_query_data(instance_id, database_id):
    """Queries sample data from the database using asynchronous SQL."""
    spanner_client = AsyncClient()
    instance = spanner_client.instance(instance_id)
    database = await instance.database(database_id)

    async with database.snapshot() as snapshot:
        results = await snapshot.execute_sql(
            "SELECT SingerId, AlbumId, AlbumTitle FROM Albums"
        )

        async for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))


# [END spanner_async_query_data]


# [START spanner_async_insert_data]
async def async_insert_data(instance_id, database_id):
    """Inserts sample data into the database using DML asynchronously."""
    spanner_client = AsyncClient()
    instance = spanner_client.instance(instance_id)
    database = await instance.database(database_id)

    async def insert_singers(transaction):
        dml = (
            "INSERT INTO Singers (SingerId, FirstName, LastName) VALUES "
            "(12, 'Melissa', 'Garcia'), "
            "(13, 'Russell', 'Morales')"
        )
        await transaction.execute_update(dml)

    await database.run_in_transaction(insert_singers)
    print("Async DML Insert transaction complete.")


# [END spanner_async_insert_data]


# [START spanner_async_read_write_transaction]
async def async_read_write_transaction(instance_id, database_id):
    """Performs an asynchronous read-write transaction."""
    spanner_client = AsyncClient()
    instance = spanner_client.instance(instance_id)
    database = await instance.database(database_id)

    async def update_singer_lastname(transaction):
        # Retrieve current name
        results = await transaction.execute_sql(
            "SELECT SingerId, FirstName, LastName FROM Singers WHERE SingerId = 12"
        )
        async for row in results:
            print(
                "Before Update - SingerId: {}, FirstName: {}, LastName: {}".format(*row)
            )

        # Update LastName
        await transaction.execute_update(
            "UPDATE Singers SET LastName = 'Jackson' WHERE SingerId = 12"
        )

    await database.run_in_transaction(update_singer_lastname)
    print("Async read-write transaction complete.")


# [END spanner_async_read_write_transaction]


# [START spanner_async_read_only_transaction]
async def async_read_only_transaction(instance_id, database_id):
    """Performs an asynchronous read-only transaction."""
    spanner_client = AsyncClient()
    instance = spanner_client.instance(instance_id)
    database = await instance.database(database_id)

    async with database.snapshot() as snapshot:
        # Execute a read using standard KeySet
        keyset = KeySet(all_=True)
        results = await snapshot.read(
            table="Singers",
            columns=("SingerId", "FirstName", "LastName"),
            keyset=keyset,
        )

        async for row in results:
            print("Read Row - SingerId: {}, FirstName: {}, LastName: {}".format(*row))


# [END spanner_async_read_only_transaction]
