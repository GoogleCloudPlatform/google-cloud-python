# Copyright 2014 Google LLC
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

"""Script to populate datastore with system test data."""

from __future__ import print_function

import os
import sys

from google.cloud import datastore

FETCH_MAX = 20
ALL_KINDS = (
    "Character",
    "Company",
    "Kind",
    "Person",
    "Post",
    "uuid_key",
    "timestamp_key",
    "LargeCharacter",
    "Mergejoin",
)
TRANSACTION_MAX_GROUPS = 5
MAX_DEL_ENTITIES = 500


def get_system_test_db():
    return os.getenv("SYSTEM_TESTS_DATABASE") or "system-tests-named-db"


def print_func(message):
    if os.getenv("GOOGLE_CLOUD_NO_PRINT") != "true":
        print(message)


def get_ancestors(entities):
    # NOTE: A key will always have at least one path element.
    key_roots = [entity.key.flat_path[:2] for entity in entities]
    # Return the unique roots.
    return list(set(key_roots))


def delete_chunks(client, results):
    while results:
        chunk, results = results[:MAX_DEL_ENTITIES], results[MAX_DEL_ENTITIES:]
        client.delete_multi([result.key for result in chunk])


def remove_kind(kind, client):
    query = client.query(kind=kind)
    query.keys_only()
    results = list(query.fetch())

    if not results:
        return

    delete_outside_transaction = False
    with client.transaction():
        # Now that we have all results, we seek to delete.
        print_func("Deleting keys:")
        print_func(results)

        ancestors = get_ancestors(results)
        if len(ancestors) > TRANSACTION_MAX_GROUPS:
            delete_outside_transaction = True
        else:
            delete_chunks(client, results)

    if delete_outside_transaction:
        delete_chunks(client, results)


def remove_all_entities(client):
    query = client.query()
    results = list(query.fetch())
    keys = [entity.key for entity in results]
    client.delete_multi(keys)


def run(database):
    kinds = sys.argv[1:]

    if len(kinds) == 0:
        kinds = ALL_KINDS
    print_func(
        "This command will remove all entities from the database "
        + database
        + " for the following kinds:"
    )
    print_func("\n".join("- " + val for val in kinds))
    response = input("Is this OK [y/n]? ")

    if response.lower() == "y":
        for namespace in ["", "LargeCharacterEntity", "MergejoinNamespace"]:
            client = datastore.Client(database=database, namespace=namespace)
            for kind in kinds:
                remove_kind(kind, client)

    else:
        print_func("Doing nothing.")


def main():
    for database in ["", get_system_test_db()]:
        run(database)


if __name__ == "__main__":
    main()
