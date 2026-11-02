# Copyright 2022 Google LLC
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
import time
from datetime import datetime, timezone

import pytest

from google.cloud import datastore

from . import _helpers


def _parent_key(datastore_client):
    return datastore_client.key("Blog", "PizzaMan")


def _put_entity(datastore_client, entity_id):
    key = datastore_client.key(
        "read_time_test", entity_id, parent=_parent_key(datastore_client)
    )
    entity = datastore.Entity(key=key)
    entity["field"] = "old_value"
    datastore_client.put(entity)
    return entity


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_get_w_read_time(datastore_client, entities_to_delete, database_id):
    entity = _put_entity(datastore_client, 1)
    entities_to_delete.append(entity)

    # Add some sleep to accommodate server & client clock discrepancy.
    time.sleep(1)
    read_time = datetime.now(tz=timezone.utc)
    time.sleep(1)

    entity["field"] = "new_value"
    datastore_client.put(entity)

    # Get without read_time.
    retrieved_entity = datastore_client.get(entity.key)
    assert retrieved_entity["field"] == "new_value"

    # Directly specify read_time in get request.
    retrieved_entity_from_read_time = datastore_client.get(
        entity.key, read_time=read_time
    )
    assert retrieved_entity_from_read_time["field"] == "old_value"

    # Use read_time in a read_only transaction.
    with datastore_client.transaction(read_only=True, read_time=read_time):
        retrieved_entity_from_xact = datastore_client.get(entity.key)
        assert retrieved_entity_from_xact["field"] == "old_value"


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_query_w_read_time(datastore_client, entities_to_delete, database_id):
    entity0 = _put_entity(datastore_client, 1)
    entity1 = _put_entity(datastore_client, 2)
    entity2 = _put_entity(datastore_client, 3)

    entities_to_delete.append(entity0)
    entities_to_delete.append(entity1)
    entities_to_delete.append(entity2)

    # Add some sleep to accommodate server & client clock discrepancy.
    time.sleep(1)
    read_time = datetime.now(tz=timezone.utc)
    time.sleep(1)

    entity2["field"] = "new_value"
    datastore_client.put(entity2)

    query = datastore_client.query(
        kind="read_time_test", ancestor=_parent_key(datastore_client)
    )
    query = query.add_filter("field", "=", "old_value")

    # Query without read_time.
    iterator = query.fetch()
    page = next(iterator.pages)
    query_results = list(page)
    assert len(query_results) == 2
    assert query_results[0].key == entity0.key
    assert query_results[1].key == entity1.key

    # Directly specify read_time in query.
    iterator_read_time = query.fetch(read_time=read_time)
    page_read_time = next(iterator_read_time.pages)
    query_results_read_time = list(page_read_time)
    assert len(query_results_read_time) == 3
    assert query_results_read_time[0].key == entity0.key
    assert query_results_read_time[1].key == entity1.key
    assert query_results_read_time[2].key == entity2.key

    # Run the query in a read_only transacxtion with read_time.
    with datastore_client.transaction(read_only=True, read_time=read_time):
        iterator_from_xact = query.fetch()
        page_from_xact = next(iterator_from_xact.pages)
        query_results_from_xact = list(page_from_xact)
        assert len(query_results_from_xact) == 3
        assert query_results_from_xact[0].key == entity0.key
        assert query_results_from_xact[1].key == entity1.key
        assert query_results_from_xact[2].key == entity2.key
