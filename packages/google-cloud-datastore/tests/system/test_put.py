# Copyright 2011 Google LLC
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

import datetime

import pytest
from google.cloud._helpers import UTC

from google.cloud import datastore
from google.cloud.datastore.helpers import GeoPoint

from . import _helpers


def parent_key(datastore_client):
    return datastore_client.key("Blog", "PizzaMan")


def _get_post(datastore_client, id_or_name=None, post_content=None):
    post_content = post_content or {
        "title": "How to make the perfect pizza in your grill",
        "tags": ["pizza", "grill"],
        "publishedAt": datetime.datetime(2001, 1, 1, tzinfo=UTC),
        "author": "Silvano",
        "isDraft": False,
        "wordCount": 400,
        "rating": 5.0,
    }
    # Create an entity with the given content.
    # NOTE: Using a parent to ensure consistency for query
    #       in `test_empty_kind`.
    key = datastore_client.key("Post", parent=parent_key(datastore_client))
    entity = datastore.Entity(key=key)
    entity.update(post_content)

    # Update the entity key.
    if id_or_name is not None:
        entity.key = entity.key.completed_key(id_or_name)

    return entity


@pytest.mark.parametrize(
    "name,key_id", [(None, None), ("post1", None), (None, 123456789)]
)
@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_put(datastore_client, entities_to_delete, name, key_id, database_id):
    entity = _get_post(datastore_client, id_or_name=(name or key_id))
    datastore_client.put(entity)
    entities_to_delete.append(entity)

    if name is not None:
        assert entity.key.name == name
    if key_id is not None:
        assert entity.key.id == key_id

    retrieved_entity = datastore_client.get(entity.key)
    # Check the given and retrieved are the same.
    assert retrieved_entity == entity


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_put_w_multiple_in_txn(
    datastore_client, entities_to_delete, database_id
):
    with datastore_client.transaction() as xact:
        entity1 = _get_post(datastore_client)
        xact.put(entity1)
        # Register entity to be deleted.
        entities_to_delete.append(entity1)

        second_post_content = {
            "title": "How to make the perfect homemade pasta",
            "tags": ["pasta", "homemade"],
            "publishedAt": datetime.datetime(2001, 1, 1),
            "author": "Silvano",
            "isDraft": False,
            "wordCount": 450,
            "rating": 4.5,
        }
        entity2 = _get_post(
            datastore_client,
            post_content=second_post_content,
        )
        xact.put(entity2)
        # Register entity to be deleted.
        entities_to_delete.append(entity2)

    keys = [entity1.key, entity2.key]
    matches = datastore_client.get_multi(keys)
    assert len(matches) == 2


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_query_w_empty_kind(datastore_client, database_id):
    query = datastore_client.query(kind="Post")
    query.ancestor = parent_key(datastore_client)
    posts = query.fetch(limit=2)
    assert list(posts) == []


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_put_w_all_value_types(
    datastore_client, entities_to_delete, database_id
):
    key = datastore_client.key("TestPanObject", 1234)
    entity = datastore.Entity(key=key)
    entity["timestamp"] = datetime.datetime(2014, 9, 9, tzinfo=UTC)
    key_stored = datastore_client.key("SavedKey", "right-here")
    entity["key"] = key_stored
    entity["truthy"] = True
    entity["float"] = 2.718281828
    entity["int"] = 3735928559
    entity["words"] = "foo"
    entity["blob"] = b"seekretz"
    entity_stored = datastore.Entity(key=key_stored)
    entity_stored["hi"] = "bye"
    entity["nested"] = entity_stored
    entity["items"] = [1, 2, 3]
    entity["geo"] = GeoPoint(1.0, 2.0)
    entity["nothing_here"] = None

    # Store the entity.
    datastore_client.put(entity)
    entities_to_delete.append(entity)

    # Check the original and retrieved are the same.
    retrieved_entity = datastore_client.get(entity.key)
    assert retrieved_entity == entity


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_put_w_entity_w_self_reference(
    datastore_client, entities_to_delete, database_id
):
    parent_key = datastore_client.key("Residence", "NewYork")
    key = datastore_client.key("Person", "name", parent=parent_key)
    entity = datastore.Entity(key=key)
    entity["fullName"] = "Full name"
    entity["linkedTo"] = key  # Self reference.

    datastore_client.put(entity)
    entities_to_delete.append(entity)

    query = datastore_client.query(kind="Person")
    # Adding ancestor to ensure consistency.
    query.ancestor = parent_key
    query.add_filter("linkedTo", "=", key)

    stored_persons = list(query.fetch(limit=2))
    assert stored_persons == [entity]


@pytest.mark.parametrize("database_id", [None, _helpers.TEST_DATABASE], indirect=True)
def test_client_put_w_empty_array(datastore_client, entities_to_delete, database_id):
    local_client = _helpers.clone_client(datastore_client)

    key = local_client.key("EmptyArray", 1234)
    local_client = datastore.Client(database=local_client.database)
    entity = datastore.Entity(key=key)
    entity["children"] = []
    local_client.put(entity)
    entities_to_delete.append(entity)

    retrieved = local_client.get(entity.key)

    assert entity["children"] == retrieved["children"]
