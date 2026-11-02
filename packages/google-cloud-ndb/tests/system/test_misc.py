# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Difficult to classify regression tests.
"""

import os
import pickle
import threading
import time
import traceback
from unittest import mock

import pytest
import redis
import test_utils.system
from google.api_core import exceptions as core_exceptions

from google.cloud import ndb

from . import KIND, eventually, length_equals

USE_REDIS_CACHE = bool(os.environ.get("REDIS_CACHE_URL"))


# Pickle can only pickle/unpickle global classes
class PickleOtherKind(ndb.Model):
    foo = ndb.IntegerProperty()

    @classmethod
    def _get_kind(cls):
        return "OtherKind"


class PickleSomeKind(ndb.Model):
    other = ndb.StructuredProperty(PickleOtherKind)

    @classmethod
    def _get_kind(cls):
        return "SomeKind"


@pytest.mark.usefixtures("client_context")
def test_pickle_roundtrip_structured_property(dispose_of):
    """Regression test for Issue #281.

    https://github.com/googleapis/python-ndb/issues/281
    """
    ndb.Model._kind_map["SomeKind"] = PickleSomeKind
    ndb.Model._kind_map["OtherKind"] = PickleOtherKind

    entity = PickleSomeKind(other=PickleOtherKind(foo=1))
    key = entity.put()
    dispose_of(key._key)

    entity = key.get(use_cache=False)
    assert entity.other.key is None or entity.other.key.id() is None
    entity = pickle.loads(pickle.dumps(entity))
    assert entity.other.foo == 1


@pytest.mark.usefixtures("client_context")
def test_tasklet_yield_emtpy_list():
    """Regression test for Issue #353.

    https://github.com/googleapis/python-ndb/issues/353
    """

    @ndb.tasklet
    def test_it():
        nothing = yield []
        raise ndb.Return(nothing)

    assert test_it().result() == ()


@pytest.mark.usefixtures("client_context")
def test_transactional_composable(dispose_of):
    """Regression test for Issue #366.

    https://github.com/googleapis/python-ndb/issues/366
    """

    class OtherKind(ndb.Model):
        bar = ndb.IntegerProperty()

    class SomeKind(ndb.Model):
        foos = ndb.KeyProperty(repeated=True)
        bar = ndb.IntegerProperty(default=42)

    others = [OtherKind(bar=bar) for bar in range(5)]
    other_keys = ndb.put_multi(others)
    for key in other_keys:
        dispose_of(key._key)

    entity = SomeKind(foos=other_keys[1:])
    entity_key = entity.put()
    dispose_of(entity_key._key)

    @ndb.transactional()
    def get_entities(*keys):
        entities = []
        for entity in ndb.get_multi(keys):
            entities.append(entity)
            if isinstance(entity, SomeKind):
                entities.extend(get_foos(entity))

        return entities

    @ndb.transactional()
    def get_foos(entity):
        return ndb.get_multi(entity.foos)

    results = get_entities(entity_key, other_keys[0])
    assert [result.bar for result in results] == [42, 1, 2, 3, 4, 0]


@pytest.mark.usefixtures("client_context")
def test_parallel_transactions(dispose_of):
    """Regression test for Issue #394

    https://github.com/googleapis/python-ndb/issues/394
    """

    class SomeKind(ndb.Model):
        foo = ndb.IntegerProperty()

    @ndb.transactional_tasklet()
    def update(id, add, delay=0):
        entity = yield SomeKind.get_by_id_async(id)
        foo = entity.foo
        foo += add

        yield ndb.sleep(delay)
        entity.foo = foo

        yield entity.put_async()

    @ndb.tasklet
    def concurrent_tasks(id):
        yield [
            update(id, 100),
            update(id, 100, 0.01),
        ]

    key = SomeKind(foo=42).put()
    dispose_of(key._key)
    id = key.id()

    concurrent_tasks(id).get_result()

    entity = SomeKind.get_by_id(id)
    assert entity.foo == 242


def test_parallel_transactions_w_context_cache(client_context, dispose_of):
    """Regression test for Issue #394

    https://github.com/googleapis/python-ndb/issues/394
    """

    class SomeKind(ndb.Model):
        foo = ndb.IntegerProperty()

    @ndb.transactional_tasklet()
    def update(id, add, delay=0):
        entity = yield SomeKind.get_by_id_async(id)
        foo = entity.foo
        foo += add

        yield ndb.sleep(delay)
        entity.foo = foo

        yield entity.put_async()

    @ndb.tasklet
    def concurrent_tasks(id):
        yield [
            update(id, 100),
            update(id, 100, 0.01),
        ]

    with client_context.new(cache_policy=None).use():
        key = SomeKind(foo=42).put()
        dispose_of(key._key)
        id = key.id()

        concurrent_tasks(id).get_result()

        entity = SomeKind.get_by_id(id)
        assert entity.foo == 242


@pytest.mark.skipif(not USE_REDIS_CACHE, reason="Redis is not configured")
@pytest.mark.usefixtures("redis_context")
def test_parallel_transactions_w_redis_cache(dispose_of):
    """Regression test for Issue #394

    https://github.com/googleapis/python-ndb/issues/394
    """

    class SomeKind(ndb.Model):
        foo = ndb.IntegerProperty()

    @ndb.transactional_tasklet()
    def update(id, add, delay=0):
        entity = yield SomeKind.get_by_id_async(id)
        foo = entity.foo
        foo += add

        yield ndb.sleep(delay)
        entity.foo = foo

        yield entity.put_async()

    @ndb.tasklet
    def concurrent_tasks(id):
        yield [
            update(id, 100),
            update(id, 100, 0.01),
        ]

    key = SomeKind(foo=42).put()
    dispose_of(key._key)
    id = key.id()

    SomeKind.get_by_id(id)
    concurrent_tasks(id).get_result()

    entity = SomeKind.get_by_id(id)
    assert entity.foo == 242


def test_rollback_with_context_cache(client_context, dispose_of):
    """Regression test for Issue #398

    https://github.com/googleapis/python-ndb/issues/398
    """

    class SomeKind(ndb.Model):
        foo = ndb.IntegerProperty()

    class SpuriousError(Exception):
        pass

    @ndb.transactional()
    def update(id, add, fail=False):
        entity = SomeKind.get_by_id(id)
        entity.foo = entity.foo + add
        entity.put()

        if fail:
            raise SpuriousError()

    with client_context.new(cache_policy=None).use():
        key = SomeKind(foo=42).put()
        dispose_of(key._key)
        id = key.id()

        update(id, 100)

        entity = SomeKind.get_by_id(id)
        assert entity.foo == 142

        try:
            update(id, 100, fail=True)
        except SpuriousError:
            pass

        entity = SomeKind.get_by_id(id)
        assert entity.foo == 142


@pytest.mark.usefixtures("client_context")
def test_insert_entity_in_transaction_without_preallocating_id(dispose_of):
    class SomeKind(ndb.Model):
        foo = ndb.IntegerProperty()
        bar = ndb.StringProperty()

    def save_entity():
        # By not waiting on the Future, we don't force a call to AllocateIds
        # before the transaction is committed.
        SomeKind(foo=42, bar="none").put_async()

    ndb.transaction(save_entity)

    query = SomeKind.query()
    eventually(query.fetch, length_equals(1))
    retrieved = query.fetch()[0]
    dispose_of(retrieved._key._key)

    assert retrieved.foo == 42
    assert retrieved.bar == "none"


@pytest.mark.usefixtures("client_context")
def test_crosswired_property_names(ds_entity):
    """Regression test for #461.

    https://github.com/googleapis/python-ndb/issues/461
    """
    entity_id = test_utils.system.unique_resource_id()
    ds_entity(KIND, entity_id, foo=42, bar=43)

    class SomeKind(ndb.Model):
        bar = ndb.IntegerProperty(name="foo")

    key = ndb.Key(KIND, entity_id)
    entity = key.get()

    assert entity.bar == 42


@mock.patch("google.cloud.ndb._datastore_api.begin_transaction")
def test_do_not_disclose_cache_contents(begin_transaction, client_context):
    """Regression test for #482.

    https://github.com/googleapis/python-ndb/issues/482
    """
    begin_transaction.side_effect = core_exceptions.ServiceUnavailable("Spurious Error")

    client_context.cache["hello dad"] = "i'm in jail"

    @ndb.transactional()
    def callback():
        pass

    with pytest.raises(Exception) as error_info:
        callback()

    error = error_info.value
    message = "".join(traceback.format_exception_only(type(error), error))
    assert "hello dad" not in message


@pytest.mark.skipif(not USE_REDIS_CACHE, reason="Redis is not configured")
@pytest.mark.usefixtures("client_context")
def test_parallel_threads_lookup_w_redis_cache(database_id, namespace, dispose_of):
    """Regression test for #496

    https://github.com/googleapis/python-ndb/issues/496
    """

    class MonkeyPipeline(redis.client.Pipeline):
        def mset(self, mapping):
            """Force a delay here to expose concurrency error."""
            time.sleep(0.05)
            return super(MonkeyPipeline, self).mset(mapping)

    with mock.patch("redis.client.Pipeline", MonkeyPipeline):
        client = ndb.Client(database=database_id)
        global_cache = ndb.RedisCache.from_environment()
        activity = {"calls": 0}

        class SomeKind(ndb.Model):
            foo = ndb.IntegerProperty()

        class LookupThread(threading.Thread):
            def __init__(self, id):
                super(LookupThread, self).__init__()
                self.id = id

            def run(self):
                context = client.context(
                    cache_policy=False,
                    global_cache=global_cache,
                    namespace=namespace,
                )
                with context:
                    entity = SomeKind.get_by_id(self.id)
                    assert entity.foo == 42
                    activity["calls"] += 1

        key = SomeKind(foo=42).put()
        dispose_of(key._key)
        id = key.id()

        thread1, thread2 = LookupThread(id), LookupThread(id)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

        assert activity["calls"] == 2


@pytest.mark.usefixtures("client_context")
def test_non_transactional_means_no_transaction(dispose_of):
    """Regression test for #552

    https://github.com/googleapis/python-ndb/issues/552
    """
    N = 50

    class SomeKind(ndb.Model):
        pass

    class OtherKind(ndb.Model):
        pass

    @ndb.tasklet
    def create_entities():
        parent_keys = yield [SomeKind().put_async() for _ in range(N)]

        futures = []
        for parent_key in parent_keys:
            dispose_of(parent_key._key)
            futures.append(OtherKind(parent=parent_key).put_async())
            futures.append(OtherKind(parent=parent_key).put_async())

        keys = yield futures
        for key in keys:
            dispose_of(key._key)

        raise ndb.Return(keys)

    @ndb.non_transactional()
    @ndb.tasklet
    def non_transactional_tasklet(keys):
        entities = yield ndb.get_multi_async(keys)
        raise ndb.Return(entities)

    @ndb.non_transactional()
    @ndb.tasklet
    def also_a_non_transactional_tasklet():
        entities = yield OtherKind.query().fetch_async()
        raise ndb.Return(entities)

    @ndb.transactional()
    def test_lookup(keys):
        entities = non_transactional_tasklet(keys).result()
        assert len(entities) == N * 2

    @ndb.transactional()
    def test_query():
        return also_a_non_transactional_tasklet().result()

    keys = create_entities().result()
    test_lookup(keys)
    eventually(test_query, length_equals(N * 2))


@pytest.mark.usefixtures("client_context")
def test_legacy_local_structured_property_with_boolean(ds_entity):
    """Regression test for #623, #625

    https://github.com/googleapis/python-ndb/issues/623
    https://github.com/googleapis/python-ndb/issues/625
    """
    children = [
        b"x\x9c\xab\xe2\x96bNJ,R`\xd0b\x12`\xac\x12\xe1\xe0\x97bN\xcb\xcf\x07r9\xa5"
        b"\xd832\x15r\xf3s\x15\x01u_\x07\n",
        b"x\x9c\xab\xe2\x96bNJ,R`\xd0b\x12`\xa8\x12\xe7\xe0\x97bN\xcb\xcf\x07ry\xa4"
        b"\xb82Rsr\xf2\x15R\x12S\x14\x01\x8e\xbf\x085",
    ]

    entity_id = test_utils.system.unique_resource_id()
    ds_entity(KIND, entity_id, children=children)

    class OtherKind(ndb.Model):
        foo = ndb.StringProperty()
        bar = ndb.BooleanProperty(required=True, default=True)

    class SomeKind(ndb.Model):
        children = ndb.LocalStructuredProperty(
            OtherKind, repeated=True, compressed=True
        )

    entity = SomeKind.get_by_id(entity_id)

    assert len(entity.children) == 2
    assert entity.children[0].foo == "hi mom!"
    assert entity.children[0].bar is True
    assert entity.children[1].foo == "hello dad!"
    assert entity.children[1].bar is False

    entity.children.append(OtherKind(foo="i'm in jail!", bar=False))
    entity.put()

    entity = SomeKind.get_by_id(entity_id)
    assert entity.children[0].foo == "hi mom!"
    assert entity.children[0].bar is True
    assert entity.children[1].foo == "hello dad!"
    assert entity.children[1].bar is False
    assert entity.children[2].foo == "i'm in jail!"
    assert entity.children[2].bar is False


@pytest.mark.usefixtures("client_context")
def test_parent_and_child_in_default_namespace(dispose_of):
    """Regression test for #661

    https://github.com/googleapis/python-ndb/issues/661
    """

    class SomeKind(ndb.Model):
        pass

    class OtherKind(ndb.Model):
        foo = ndb.IntegerProperty()

    parent = SomeKind(namespace="")
    parent_key = parent.put()
    dispose_of(parent_key._key)

    child = OtherKind(parent=parent_key, namespace="", foo=42)
    child_key = child.put()
    dispose_of(child_key._key)

    assert OtherKind.query(ancestor=parent_key).get().foo == 42
