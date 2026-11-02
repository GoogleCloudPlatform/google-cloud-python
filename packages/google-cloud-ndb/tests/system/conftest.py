import itertools
import logging
import os
import uuid

import pytest
import requests

from google.cloud import datastore, ndb
from google.cloud.ndb import global_cache as global_cache_module

from . import KIND, OTHER_KIND, _helpers

log = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def preclean():
    """Clean out default namespace in test database."""
    _preclean(None, None)
    if _helpers.TEST_DATABASE:
        _preclean(_helpers.TEST_DATABASE, None)


def _preclean(database, namespace):
    ds_client = _make_ds_client(database, namespace)
    for kind in (KIND, OTHER_KIND):
        query = ds_client.query(kind=kind)
        query.keys_only()
        for page in query.fetch().pages:
            keys = [entity.key for entity in page]
            ds_client.delete_multi(keys)


def _make_ds_client(database, namespace):
    emulator = bool(os.environ.get("DATASTORE_EMULATOR_HOST"))
    if emulator:
        client = datastore.Client(
            database=database, namespace=namespace, _http=requests.Session
        )
    else:
        client = datastore.Client(database=database, namespace=namespace)

    assert client.database == database
    assert client.namespace == namespace

    return client


def all_entities(client, other_namespace):
    return itertools.chain(
        client.query(kind=KIND).fetch(),
        client.query(kind=OTHER_KIND).fetch(),
        client.query(namespace=other_namespace).fetch(),
    )


@pytest.fixture(scope="session")
def deleted_keys():
    return set()


@pytest.fixture
def to_delete():
    return []


@pytest.fixture
def ds_client(database_id, namespace):
    client = _make_ds_client(database_id, namespace)
    assert client.database == database_id
    assert client.namespace == namespace
    return client


@pytest.fixture
def with_ds_client(ds_client, to_delete, deleted_keys, other_namespace):
    yield ds_client

    # Clean up after ourselves
    while to_delete:
        batch = to_delete[:500]
        ds_client.delete_multi(batch)
        deleted_keys.update(batch)
        to_delete = to_delete[500:]

    not_deleted = [
        entity
        for entity in all_entities(ds_client, other_namespace)
        if fix_key_db(entity.key, ds_client) not in deleted_keys
    ]
    if not_deleted:
        log.warning("CLEAN UP: Entities not deleted from test: {}".format(not_deleted))


@pytest.fixture
def ds_entity(with_ds_client, dispose_of):
    def make_entity(*key_args, **entity_kwargs):
        key = with_ds_client.key(*key_args)
        assert with_ds_client.get(key) is None
        entity = datastore.Entity(key=key)
        entity.update(entity_kwargs)
        with_ds_client.put(entity)
        dispose_of(key)

        return entity

    yield make_entity


@pytest.fixture
def ds_entity_with_meanings(with_ds_client, dispose_of):
    def make_entity(*key_args, **entity_kwargs):
        meanings = key_args[0]
        key = with_ds_client.key(*key_args[1:])
        assert with_ds_client.get(key) is None
        entity = datastore.Entity(key=key, exclude_from_indexes=("blob",))
        entity._meanings = meanings
        entity.update(entity_kwargs)
        with_ds_client.put(entity)
        dispose_of(key)

        return entity

    yield make_entity


# Workaround: datastore batches reject if key.database is None and client.database == ""
# or vice-versa. This should be fixed, but for now just fix the keys
# See https://github.com/googleapis/python-datastore/issues/460
def fix_key_db(key, database):
    if key.database:
        return key
    else:
        fixed_key = key.__class__(
            *key.flat_path,
            project=key.project,
            database=database,
            namespace=key.namespace,
        )
        # If the current parent has already been set, we re-use
        # the same instance
        fixed_key._parent = key._parent
        return fixed_key


@pytest.fixture
def dispose_of(with_ds_client, to_delete):
    def delete_entity(*ds_keys):
        to_delete.extend(
            map(lambda key: fix_key_db(key, with_ds_client.database), ds_keys)
        )

    return delete_entity


@pytest.fixture(params=["", _helpers.TEST_DATABASE])
def database_id(request):
    return request.param


@pytest.fixture
def namespace():
    return str(uuid.uuid4())


@pytest.fixture
def other_namespace():
    return str(uuid.uuid4())


@pytest.fixture
def client_context(database_id, namespace):
    client = ndb.Client(database=database_id)
    assert client.database == database_id
    context_manager = client.context(
        cache_policy=False,
        legacy_data=False,
        namespace=namespace,
    )
    with context_manager as context:
        yield context


@pytest.fixture
def redis_context(client_context):
    global_cache = global_cache_module.RedisCache.from_environment()
    with client_context.new(global_cache=global_cache).use() as context:
        context.set_global_cache_policy(None)  # Use default
        yield context


@pytest.fixture
def memcache_context(client_context):
    global_cache = global_cache_module.MemcacheCache.from_environment()
    with client_context.new(global_cache=global_cache).use() as context:
        context.set_global_cache_policy(None)  # Use default
        yield context
