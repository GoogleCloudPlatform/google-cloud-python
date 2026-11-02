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
import string
import sys
import time
import uuid

from google.cloud import datastore

ANCESTOR = ("Book", "GoT")
RICKARD = ANCESTOR + ("Character", "Rickard")
EDDARD = RICKARD + ("Character", "Eddard")
KEY_PATHS = (
    RICKARD,
    EDDARD,
    ANCESTOR + ("Character", "Catelyn"),
    EDDARD + ("Character", "Arya"),
    EDDARD + ("Character", "Sansa"),
    EDDARD + ("Character", "Robb"),
    EDDARD + ("Character", "Bran"),
    EDDARD + ("Character", "Jon Snow"),
)
CHARACTERS = (
    {"name": "Rickard", "family": "Stark", "appearances": 0, "alive": False},
    {"name": "Eddard", "family": "Stark", "appearances": 9, "alive": False},
    {
        "name": "Catelyn",
        "family": ["Stark", "Tully"],
        "appearances": 26,
        "alive": False,
    },
    {"name": "Arya", "family": "Stark", "appearances": 33, "alive": True},
    {"name": "Sansa", "family": "Stark", "appearances": 31, "alive": True},
    {"name": "Robb", "family": "Stark", "appearances": 22, "alive": False},
    {"name": "Bran", "family": "Stark", "appearances": 25, "alive": True},
    {"name": "Jon Snow", "family": "Stark", "appearances": 32, "alive": True},
)
LARGE_CHARACTER_TOTAL_OBJECTS = 2500
LARGE_CHARACTER_NAMESPACE = "LargeCharacterEntity"
LARGE_CHARACTER_KIND = "LargeCharacter"

MERGEJOIN_QUERY_NUM_RESULTS = 7
MERGEJOIN_DATASET_INTERMEDIATE_OBJECTS = 20000
MERGEJOIN_DATASET_NAMESPACE = "MergejoinNamespace"
MERGEJOIN_DATASET_KIND = "Mergejoin"


def get_system_test_db():
    return os.getenv("SYSTEM_TESTS_DATABASE") or "system-tests-named-db"


def print_func(message):
    if os.getenv("GOOGLE_CLOUD_NO_PRINT") != "true":
        print(message)


def add_large_character_entities(client=None):
    MAX_STRING = (string.ascii_lowercase * 58)[:1500]

    client.namespace = LARGE_CHARACTER_NAMESPACE

    # Query used for all tests
    page_query = client.query(
        kind=LARGE_CHARACTER_KIND, namespace=LARGE_CHARACTER_NAMESPACE
    )

    def put_objects(count):
        current = 0

        # Can only do 500 operations in a transaction with an overall
        # size limit.
        ENTITIES_TO_BATCH = 25
        while current < count:
            start = current
            end = min(current + ENTITIES_TO_BATCH, count)
            with client.transaction() as xact:
                # The name/ID for the new entity
                for i in range(start, end):
                    name = "character{0:05d}".format(i)
                    # The Cloud Datastore key for the new entity
                    task_key = client.key(LARGE_CHARACTER_KIND, name)

                    # Prepares the new entity
                    task = datastore.Entity(key=task_key)
                    task["name"] = "{0:05d}".format(i)
                    task["family"] = "Stark"
                    task["alive"] = False

                    for i in string.ascii_lowercase:
                        task["space-{}".format(i)] = MAX_STRING

                    # Saves the entity
                    xact.put(task)
            current += ENTITIES_TO_BATCH

    # Ensure we have 1500 entities for tests. If not, clean up type and add
    # new entities equal to LARGE_CHARACTER_TOTAL_OBJECTS
    all_entities = [e for e in page_query.fetch()]
    if len(all_entities) != LARGE_CHARACTER_TOTAL_OBJECTS:
        # Cleanup Collection if not an exact match
        while all_entities:
            entities = all_entities[:500]
            all_entities = all_entities[500:]
            client.delete_multi([e.key for e in entities])
        # Put objects
        put_objects(LARGE_CHARACTER_TOTAL_OBJECTS)


def add_characters(client=None):
    if client is None:
        # Get a client that uses the test dataset.
        client = datastore.Client(database_id="mw-other-db")
    with client.transaction() as xact:
        for key_path, character in zip(KEY_PATHS, CHARACTERS):
            if key_path[-1] != character["name"]:
                raise ValueError(("Character and key don't agree", key_path, character))
            entity = datastore.Entity(key=client.key(*key_path))
            entity.update(character)
            xact.put(entity)
            print_func(
                "Adding Character %s %s" % (character["name"], character["family"])
            )


def add_uid_keys(client=None):
    if client is None:
        # Get a client that uses the test dataset.
        client = datastore.Client(database_id="mw-other-db")

    num_batches = 2
    batch_size = 500

    for batch_num in range(num_batches):
        with client.batch() as batch:
            for seq_no in range(batch_size):
                uid = str(uuid.uuid4())
                key = client.key("uuid_key", uid)
                entity = datastore.Entity(key=key)
                entity["batch_num"] = batch_num
                entity["seq_no"] = seq_no
                batch.put(entity)


def add_timestamp_keys(client=None):
    if client is None:
        # Get a client that uses the test dataset.
        client = datastore.Client()

    num_batches = 20
    batch_size = 500

    timestamp_micros = set()
    for batch_num in range(num_batches):
        with client.batch() as batch:
            for seq_no in range(batch_size):
                print("time_time: batch: {}, sequence: {}".format(batch_num, seq_no))
                now_micros = int(time.time() * 1e6)
                while now_micros in timestamp_micros:
                    now_micros = int(time.time() * 1e6)
                timestamp_micros.add(now_micros)
                key = client.key("timestamp_key", now_micros)
                entity = datastore.Entity(key=key)
                entity["batch_num"] = batch_num
                entity["seq_no"] = seq_no
                batch.put(entity)


def add_mergejoin_dataset_entities(client=None):
    """
    Dataset to account for one bug that was seen in https://github.com/googleapis/python-datastore/issues/547
    The root cause of this is us setting a subsequent query's start_cursor to skipped_cursor instead of end_cursor.
    In niche scenarios involving mergejoins, skipped_cursor becomes empty and the query starts back from the beginning,
    returning duplicate items.

    This bug is able to be reproduced with a dataset shown in b/352377540, with 7 items of a=1, b=1
    followed by 20k items of alternating a=1, b=0 and a=0, b=1, then 7 more a=1, b=1, then querying for all
    items with a=1, b=1 and an offset of 8.
    """
    client.namespace = MERGEJOIN_DATASET_NAMESPACE

    # Query used for all tests
    page_query = client.query(
        kind=MERGEJOIN_DATASET_KIND, namespace=MERGEJOIN_DATASET_NAMESPACE
    )

    def create_entity(id, a, b):
        key = client.key(MERGEJOIN_DATASET_KIND, id)
        entity = datastore.Entity(key=key)
        entity["a"] = a
        entity["b"] = b
        return entity

    def put_objects(count):
        id = 1
        curr_intermediate_entries = 0

        # Can only do 500 operations in a transaction with an overall
        # size limit.
        ENTITIES_TO_BATCH = 500

        with client.transaction() as xact:
            for _ in range(0, MERGEJOIN_QUERY_NUM_RESULTS):
                entity = create_entity(id, 1, 1)
                id += 1
                xact.put(entity)

        while curr_intermediate_entries < count - MERGEJOIN_QUERY_NUM_RESULTS:
            start = curr_intermediate_entries
            end = min(curr_intermediate_entries + ENTITIES_TO_BATCH, count)
            with client.transaction() as xact:
                # The name/ID for the new entity
                for i in range(start, end):
                    if id % 2:
                        entity = create_entity(id, 0, 1)
                    else:
                        entity = create_entity(id, 1, 0)
                    id += 1

                    # Saves the entity
                    xact.put(entity)
            curr_intermediate_entries += ENTITIES_TO_BATCH

        with client.transaction() as xact:
            for _ in range(0, MERGEJOIN_QUERY_NUM_RESULTS):
                entity = create_entity(id, 1, 1)
                id += 1
                xact.put(entity)

    # If anything exists in this namespace, delete it, since we need to
    # set up something very specific.
    all_entities = [e for e in page_query.fetch()]
    if len(all_entities) > 0:
        # Cleanup Collection if not an exact match
        while all_entities:
            entities = all_entities[:500]
            all_entities = all_entities[500:]
            client.delete_multi([e.key for e in entities])
        # Put objects
    put_objects(MERGEJOIN_DATASET_INTERMEDIATE_OBJECTS)


def run(database):
    client = datastore.Client(database=database)
    flags = sys.argv[1:]

    if len(flags) == 0:
        flags = [
            "--characters",
            "--uuid",
            "--timestamps",
            "--large-characters",
            "--mergejoin",
        ]

    if "--characters" in flags:
        add_characters(client)

    if "--uuid" in flags:
        add_uid_keys(client)

    if "--timestamps" in flags:
        add_timestamp_keys(client)

    if "--large-characters" in flags:
        add_large_character_entities(client)

    if "--mergejoin" in flags:
        add_mergejoin_dataset_entities(client)


def main():
    for database in ["", get_system_test_db()]:
        run(database)


if __name__ == "__main__":
    main()
