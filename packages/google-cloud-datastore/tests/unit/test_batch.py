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

from typing import Any, Dict

import mock
import pytest

from google.cloud.datastore.helpers import set_database_id_to_request


def _make_batch(client):
    from google.cloud.datastore.batch import Batch

    return Batch(client)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_ctor(database_id):
    project = "PROJECT"
    namespace = "NAMESPACE"
    client = _Client(project, database=database_id, namespace=namespace)
    batch = _make_batch(client)

    assert batch.project == project
    assert batch._client is client
    assert batch.database == database_id
    assert batch.namespace == namespace
    assert batch._id is None
    assert batch._status == batch._INITIAL
    assert batch._mutations == []
    assert batch._partial_key_entities == []


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_current(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch1 = _make_batch(client)
    batch2 = _make_batch(client)

    assert batch1.current() is None
    assert batch2.current() is None

    with batch1:
        assert batch1.current() is batch1
        assert batch2.current() is batch1

        with batch2:
            assert batch1.current() is batch2
            assert batch2.current() is batch2

        assert batch1.current() is batch1
        assert batch2.current() is batch1

    assert batch1.current() is None
    assert batch2.current() is None

    commit_method = client._datastore_api.commit
    assert commit_method.call_count == 2
    mode = datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL
    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": [],
        "transaction": None,
    }
    set_database_id_to_request(expected_request, database_id)
    commit_method.assert_called_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_put_w_entity_wo_key(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    entity = _Entity()

    batch.begin()
    with pytest.raises(ValueError):
        batch.put(entity)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_put_w_wrong_status(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    entity = _Entity()
    entity.key = _Key(project=project, database=database_id)

    assert batch._status == batch._INITIAL
    with pytest.raises(ValueError):
        batch.put(entity)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_put_w_key_wrong_project(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    entity = _Entity()
    entity.key = _Key(project="OTHER", database=database_id)

    batch.begin()
    with pytest.raises(ValueError):
        batch.put(entity)


def test_batch_put_w_key_wrong_database():
    project = "PROJECT"
    client = _Client(project)
    batch = _make_batch(client)
    entity = _Entity()
    entity.key = _Key(project=project, database="somedb")

    batch.begin()
    with pytest.raises(ValueError):
        batch.put(entity)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_put_w_entity_w_partial_key(database_id):
    project = "PROJECT"
    properties = {"foo": "bar"}
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    entity = _Entity(properties)
    key = entity.key = _Key(project, database=database_id)
    key._id = None

    batch.begin()
    batch.put(entity)

    mutated_entity = _mutated_pb(batch.mutations, "insert")
    assert mutated_entity.key == key._key
    assert batch._partial_key_entities == [entity]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_put_w_entity_w_completed_key(database_id):
    project = "PROJECT"
    properties = {"foo": "bar", "baz": "qux", "spam": [1, 2, 3], "frotz": []}
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    entity = _Entity(properties)
    entity.exclude_from_indexes = ("baz", "spam")
    key = entity.key = _Key(project, database=database_id)

    batch.begin()
    batch.put(entity)

    mutated_entity = _mutated_pb(batch.mutations, "upsert")
    assert mutated_entity.key == key._key

    prop_dict = dict(mutated_entity.properties.items())
    assert len(prop_dict) == 4
    assert not prop_dict["foo"].exclude_from_indexes
    assert prop_dict["baz"].exclude_from_indexes
    assert not prop_dict["spam"].exclude_from_indexes

    spam_values = prop_dict["spam"].array_value.values
    assert spam_values[0].exclude_from_indexes
    assert spam_values[1].exclude_from_indexes
    assert spam_values[2].exclude_from_indexes
    assert "frotz" in prop_dict


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_delete_w_wrong_status(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    key = _Key(project=project, database=database_id)
    key._id = None

    assert batch._status == batch._INITIAL

    with pytest.raises(ValueError):
        batch.delete(key)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_delete_w_partial_key(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    key = _Key(project=project, database=database_id)
    key._id = None

    batch.begin()

    with pytest.raises(ValueError):
        batch.delete(key)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_delete_w_key_wrong_project(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    key = _Key(project="OTHER", database=database_id)

    batch.begin()
    with pytest.raises(ValueError):
        batch.delete(key)


def test_batch_delete_w_key_wrong_database():
    project = "PROJECT"
    database = "DATABASE"
    client = _Client(project, database=database)
    batch = _make_batch(client)
    key = _Key(project=project, database=None)

    batch.begin()
    with pytest.raises(ValueError):
        batch.delete(key)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_delete_w_completed_key(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    key = _Key(project, database=database_id)

    batch.begin()
    batch.delete(key)

    mutated_key = _mutated_pb(batch.mutations, "delete")
    assert mutated_key == key._key


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_begin_w_wrong_status(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    batch._status = batch._IN_PROGRESS

    with pytest.raises(ValueError):
        batch.begin()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_begin(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    assert batch._status == batch._INITIAL

    batch.begin()

    assert batch._status == batch._IN_PROGRESS


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_rollback_w_wrong_status(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    assert batch._status == batch._INITIAL

    with pytest.raises(ValueError):
        batch.rollback()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_rollback(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    batch.begin()
    assert batch._status == batch._IN_PROGRESS

    batch.rollback()

    assert batch._status == batch._ABORTED


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_commit_wrong_status(database_id):
    project = "PROJECT"
    client = _Client(project, database=database_id)
    batch = _make_batch(client)
    assert batch._status == batch._INITIAL

    with pytest.raises(ValueError):
        batch.commit()


def _batch_commit_helper(timeout=None, retry=None, database=None):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    client = _Client(project, database=database)
    batch = _make_batch(client)
    assert batch._status == batch._INITIAL

    batch.begin()
    assert batch._status == batch._IN_PROGRESS

    kwargs = {}

    if timeout is not None:
        kwargs["timeout"] = timeout

    if retry is not None:
        kwargs["retry"] = retry

    batch.commit(**kwargs)
    assert batch._status == batch._FINISHED

    commit_method = client._datastore_api.commit
    mode = datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL
    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": [],
        "transaction": None,
    }
    set_database_id_to_request(expected_request, database)
    commit_method.assert_called_with(request=expected_request, **kwargs)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_commit(database_id):
    _batch_commit_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_commit_w_timeout(database_id):
    timeout = 100000
    _batch_commit_helper(timeout=timeout, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_commit_w_retry(database_id):
    retry = mock.Mock(spec=[])
    _batch_commit_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_commit_w_partial_key_entity(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    new_id = 1234
    ds_api = _make_datastore_api(new_id)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    batch = _make_batch(client)
    entity = _Entity({})
    key = entity.key = _Key(project)
    key._id = None
    batch._partial_key_entities.append(entity)
    assert batch._status == batch._INITIAL

    batch.begin()
    assert batch._status == batch._IN_PROGRESS

    batch.commit()
    assert batch._status == batch._FINISHED

    mode = datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL
    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": [],
        "transaction": None,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.commit.assert_called_once_with(request=expected_request)

    assert not entity.key.is_partial
    assert entity.key._id == new_id


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_as_context_mgr_wo_error(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    properties = {"foo": "bar"}
    entity = _Entity(properties)
    key = entity.key = _Key(project, database=database_id)

    client = _Client(project, database=database_id)
    assert list(client._batches) == []

    with _make_batch(client) as batch:
        assert list(client._batches) == [batch]
        batch.put(entity)

    assert list(client._batches) == []

    mutated_entity = _mutated_pb(batch.mutations, "upsert")
    assert mutated_entity.key == key._key

    commit_method = client._datastore_api.commit
    mode = datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL
    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": batch.mutations,
        "transaction": None,
    }
    set_database_id_to_request(expected_request, database_id)
    commit_method.assert_called_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_as_context_mgr_nested(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    properties = {"foo": "bar"}
    entity1 = _Entity(properties)
    key1 = entity1.key = _Key(project, database=database_id)
    entity2 = _Entity(properties)
    key2 = entity2.key = _Key(project, database=database_id)

    client = _Client(project, database=database_id)
    assert list(client._batches) == []

    with _make_batch(client) as batch1:
        assert list(client._batches) == [batch1]
        batch1.put(entity1)

        with _make_batch(client) as batch2:
            assert list(client._batches) == [batch2, batch1]
            batch2.put(entity2)

        assert list(client._batches) == [batch1]

    assert list(client._batches) == []

    mutated_entity1 = _mutated_pb(batch1.mutations, "upsert")
    assert mutated_entity1.key == key1._key

    mutated_entity2 = _mutated_pb(batch2.mutations, "upsert")
    assert mutated_entity2.key == key2._key

    commit_method = client._datastore_api.commit
    assert commit_method.call_count == 2

    mode = datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL
    expected_request_1 = {
        "project_id": project,
        "mode": mode,
        "mutations": batch1.mutations,
        "transaction": None,
    }
    expected_request_2 = {
        "project_id": project,
        "mode": mode,
        "mutations": batch1.mutations,
        "transaction": None,
    }
    set_database_id_to_request(expected_request_1, database_id)
    set_database_id_to_request(expected_request_2, database_id)

    commit_method.assert_called_with(request=expected_request_1)
    commit_method.assert_called_with(request=expected_request_2)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_batch_as_context_mgr_w_error(database_id):
    project = "PROJECT"
    properties = {"foo": "bar"}
    entity = _Entity(properties)
    key = entity.key = _Key(project, database=database_id)

    client = _Client(project, database=database_id)
    assert list(client._batches) == []

    try:
        with _make_batch(client) as batch:
            assert list(client._batches) == [batch]
            batch.put(entity)

            raise ValueError("testing")

    except ValueError:
        pass

    assert list(client._batches) == []

    mutated_entity = _mutated_pb(batch.mutations, "upsert")
    assert mutated_entity.key == key._key

    client._datastore_api.commit.assert_not_called()


def test_batch_as_context_mgr_w_enter_fails():
    from google.cloud.datastore.batch import Batch

    class FailedBegin(Batch):
        def begin(self):
            raise RuntimeError

    client = _Client(None, None)
    assert list(client._batches) == []

    batch = FailedBegin(client)

    with pytest.raises(RuntimeError):
        # The context manager will never be entered because
        # of the failure.
        with batch:  # pragma: NO COVER
            pass

    # Make sure no batch was added.
    assert list(client._batches) == []


def test__parse_commit_response():
    from google.cloud.datastore.batch import _parse_commit_response
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2

    index_updates = 1337
    keys = [
        entity_pb2.Key(path=[entity_pb2.Key.PathElement(kind="Foo", id=1234)]),
        entity_pb2.Key(path=[entity_pb2.Key.PathElement(kind="Bar", name="baz")]),
    ]
    response = datastore_pb2.CommitResponse(
        mutation_results=[datastore_pb2.MutationResult(key=key) for key in keys],
        index_updates=index_updates,
    )

    result = _parse_commit_response(response)

    assert result == (index_updates, [i._pb for i in keys])


class _Entity(dict):
    key = None
    exclude_from_indexes = ()
    _meanings: Dict[str, Any] = {}


class _Key(object):
    _kind = "KIND"
    _key = "KEY"
    _path = None
    _id = 1234
    _stored = None

    def __init__(self, project, database=None):
        self.project = project
        self.database = database

    @property
    def is_partial(self):
        return self._id is None

    def to_protobuf(self):
        from google.cloud.datastore_v1.types import entity as entity_pb2

        key = self._key = entity_pb2.Key()
        # Don't assign it, because it will just get ripped out
        # key.partition_id.project_id = self.project

        element = key._pb.path.add()
        element.kind = self._kind
        if self._id is not None:
            element.id = self._id

        return key

    def completed_key(self, new_id):
        assert self.is_partial
        new_key = self.__class__(self.project, self.database)
        new_key._id = new_id
        return new_key


class _Client(object):
    def __init__(self, project, datastore_api=None, namespace=None, database=None):
        self.project = project
        if datastore_api is None:
            datastore_api = _make_datastore_api()
        self._datastore_api = datastore_api
        self.namespace = namespace
        self.database = database
        self._batches = []

    def _push_batch(self, batch):
        self._batches.insert(0, batch)

    def _pop_batch(self):
        return self._batches.pop(0)

    @property
    def current_batch(self):
        if self._batches:
            return self._batches[0]


def _mutated_pb(mutation_pb_list, mutation_type):
    # Make sure there is only one mutation.
    assert len(mutation_pb_list) == 1

    # We grab the only mutation.
    mutated_pb = mutation_pb_list[0]
    # Then check if it is the correct type.
    assert mutated_pb._pb.WhichOneof("operation") == mutation_type

    return getattr(mutated_pb, mutation_type)


def _make_mutation(id_):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2

    key = entity_pb2.Key()
    key.partition_id.project_id = "PROJECT"
    elem = key._pb.path.add()
    elem.kind = "Kind"
    elem.id = id_
    return datastore_pb2.MutationResult(key=key)


def _make_commit_response(*new_key_ids):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    mutation_results = [_make_mutation(key_id) for key_id in new_key_ids]
    return datastore_pb2.CommitResponse(mutation_results=mutation_results)


def _make_datastore_api(*new_key_ids):
    commit_method = mock.Mock(return_value=_make_commit_response(*new_key_ids), spec=[])
    return mock.Mock(commit=commit_method, spec=["commit"])
