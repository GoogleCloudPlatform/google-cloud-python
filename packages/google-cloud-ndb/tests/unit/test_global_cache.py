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

import collections
from unittest import mock

import pytest
import redis as redis_module

from google.cloud.ndb import global_cache


class TestGlobalCache:
    def make_one(self):
        class MockImpl(global_cache.GlobalCache):
            def get(self, keys):
                return super(MockImpl, self).get(keys)

            def set(self, items, expires=None):
                return super(MockImpl, self).set(items, expires=expires)

            def set_if_not_exists(self, items, expires=None):
                return super(MockImpl, self).set_if_not_exists(items, expires=expires)

            def delete(self, keys):
                return super(MockImpl, self).delete(keys)

            def watch(self, keys):
                return super(MockImpl, self).watch(keys)

            def unwatch(self, keys):
                return super(MockImpl, self).unwatch(keys)

            def compare_and_swap(self, items, expires=None):
                return super(MockImpl, self).compare_and_swap(items, expires=expires)

            def clear(self):
                return super(MockImpl, self).clear()

        return MockImpl()

    def test_get(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.get(b"foo")

    def test_set(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.set({b"foo": "bar"})

    def test_set_if_not_exists(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.set_if_not_exists({b"foo": "bar"})

    def test_delete(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.delete(b"foo")

    def test_watch(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.watch(b"foo")

    def test_unwatch(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.unwatch(b"foo")

    def test_compare_and_swap(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.compare_and_swap({b"foo": "bar"})

    def test_clear(self):
        cache = self.make_one()
        with pytest.raises(NotImplementedError):
            cache.clear()


class TestInProcessGlobalCache:
    @staticmethod
    def test_set_get_delete():
        cache = global_cache._InProcessGlobalCache()
        result = cache.set({b"one": b"foo", b"two": b"bar", b"three": b"baz"})
        assert result is None

        result = cache.get([b"two", b"three", b"one"])
        assert result == [b"bar", b"baz", b"foo"]

        cache = global_cache._InProcessGlobalCache()
        result = cache.get([b"two", b"three", b"one"])
        assert result == [b"bar", b"baz", b"foo"]

        result = cache.delete([b"one", b"two", b"three"])
        assert result is None

        result = cache.get([b"two", b"three", b"one"])
        assert result == [None, None, None]

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.time")
    def test_set_get_delete_w_expires(time):
        time.time.return_value = 0

        cache = global_cache._InProcessGlobalCache()
        result = cache.set(
            {b"one": b"foo", b"two": b"bar", b"three": b"baz"}, expires=5
        )
        assert result is None

        result = cache.get([b"two", b"three", b"one"])
        assert result == [b"bar", b"baz", b"foo"]

        time.time.return_value = 10
        result = cache.get([b"two", b"three", b"one"])
        assert result == [None, None, None]

    @staticmethod
    def test_set_if_not_exists():
        cache = global_cache._InProcessGlobalCache()
        result = cache.set_if_not_exists({b"one": b"foo", b"two": b"bar"})
        assert result == {b"one": True, b"two": True}

        result = cache.set_if_not_exists({b"two": b"bar", b"three": b"baz"})
        assert result == {b"two": False, b"three": True}

        result = cache.get([b"two", b"three", b"one"])
        assert result == [b"bar", b"baz", b"foo"]

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.time")
    def test_set_if_not_exists_w_expires(time):
        time.time.return_value = 0

        cache = global_cache._InProcessGlobalCache()
        result = cache.set_if_not_exists({b"one": b"foo", b"two": b"bar"}, expires=5)
        assert result == {b"one": True, b"two": True}

        result = cache.set_if_not_exists({b"two": b"bar", b"three": b"baz"}, expires=5)
        assert result == {b"two": False, b"three": True}

        result = cache.get([b"two", b"three", b"one"])
        assert result == [b"bar", b"baz", b"foo"]

        time.time.return_value = 10
        result = cache.get([b"two", b"three", b"one"])
        assert result == [None, None, None]

    @staticmethod
    def test_watch_compare_and_swap():
        cache = global_cache._InProcessGlobalCache()
        cache.cache[b"one"] = (b"food", None)
        cache.cache[b"two"] = (b"bard", None)
        cache.cache[b"three"] = (b"bazz", None)
        result = cache.watch({b"one": b"food", b"two": b"bard", b"three": b"bazd"})
        assert result is None

        cache.cache[b"two"] = (b"hamburgers", None)

        result = cache.compare_and_swap(
            {b"one": b"foo", b"two": b"bar", b"three": b"baz"}
        )
        assert result == {b"one": True, b"two": False, b"three": False}

        result = cache.get([b"one", b"two", b"three"])
        assert result == [b"foo", b"hamburgers", b"bazz"]

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.time")
    def test_watch_compare_and_swap_with_expires(time):
        time.time.return_value = 0

        cache = global_cache._InProcessGlobalCache()
        cache.cache[b"one"] = (b"food", None)
        cache.cache[b"two"] = (b"bard", None)
        cache.cache[b"three"] = (b"bazz", None)
        result = cache.watch({b"one": b"food", b"two": b"bard", b"three": b"bazd"})
        assert result is None

        cache.cache[b"two"] = (b"hamburgers", None)

        result = cache.compare_and_swap(
            {b"one": b"foo", b"two": b"bar", b"three": b"baz"}, expires=5
        )
        assert result == {b"one": True, b"two": False, b"three": False}

        result = cache.get([b"one", b"two", b"three"])
        assert result == [b"foo", b"hamburgers", b"bazz"]

        time.time.return_value = 10

        result = cache.get([b"one", b"two", b"three"])
        assert result == [None, b"hamburgers", b"bazz"]

    @staticmethod
    def test_watch_unwatch():
        cache = global_cache._InProcessGlobalCache()
        result = cache.watch({b"one": "foo", b"two": "bar", b"three": "baz"})
        assert result is None

        result = cache.unwatch([b"one", b"two", b"three"])
        assert result is None
        assert cache._watch_keys == {}

    @staticmethod
    def test_clear():
        cache = global_cache._InProcessGlobalCache()
        cache.cache["foo"] = "bar"
        cache.clear()
        assert cache.cache == {}


class TestRedisCache:
    @staticmethod
    def test_constructor():
        redis = object()
        cache = global_cache.RedisCache(redis)
        assert cache.redis is redis

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.redis_module")
    def test_from_environment(redis_module):
        redis = redis_module.Redis.from_url.return_value
        with mock.patch.dict("os.environ", {"REDIS_CACHE_URL": "some://url"}):
            cache = global_cache.RedisCache.from_environment()
            assert cache.redis is redis
            redis_module.Redis.from_url.assert_called_once_with("some://url")

    @staticmethod
    def test_from_environment_not_configured():
        with mock.patch.dict("os.environ", {"REDIS_CACHE_URL": ""}):
            cache = global_cache.RedisCache.from_environment()
            assert cache is None

    @staticmethod
    def test_get():
        redis = mock.Mock(spec=("mget",))
        cache_keys = [object(), object()]
        cache_value = redis.mget.return_value
        cache = global_cache.RedisCache(redis)
        assert cache.get(cache_keys) is cache_value
        redis.mget.assert_called_once_with(cache_keys)

    @staticmethod
    def test_set():
        redis = mock.Mock(spec=("mset",))
        cache_items = {"a": "foo", "b": "bar"}
        cache = global_cache.RedisCache(redis)
        cache.set(cache_items)
        redis.mset.assert_called_once_with(cache_items)

    @staticmethod
    def test_set_w_expires():
        expired = {}

        def mock_expire(key, expires):
            expired[key] = expires

        redis = mock.Mock(expire=mock_expire, spec=("mset", "expire"))
        cache_items = {"a": "foo", "b": "bar"}
        cache = global_cache.RedisCache(redis)
        cache.set(cache_items, expires=32)
        redis.mset.assert_called_once_with(cache_items)
        assert expired == {"a": 32, "b": 32}

    @staticmethod
    def test_set_if_not_exists():
        redis = mock.Mock(spec=("setnx",))
        redis.setnx.side_effect = (True, False)
        cache_items = collections.OrderedDict([("a", "foo"), ("b", "bar")])
        cache = global_cache.RedisCache(redis)
        results = cache.set_if_not_exists(cache_items)
        assert results == {"a": True, "b": False}
        redis.setnx.assert_has_calls(
            [
                mock.call("a", "foo"),
                mock.call("b", "bar"),
            ]
        )

    @staticmethod
    def test_set_if_not_exists_w_expires():
        redis = mock.Mock(spec=("setnx", "expire"))
        redis.setnx.side_effect = (True, False)
        cache_items = collections.OrderedDict([("a", "foo"), ("b", "bar")])
        cache = global_cache.RedisCache(redis)
        results = cache.set_if_not_exists(cache_items, expires=123)
        assert results == {"a": True, "b": False}
        redis.setnx.assert_has_calls(
            [
                mock.call("a", "foo"),
                mock.call("b", "bar"),
            ]
        )
        redis.expire.assert_called_once_with("a", 123)

    @staticmethod
    def test_delete():
        redis = mock.Mock(spec=("delete",))
        cache_keys = [object(), object()]
        cache = global_cache.RedisCache(redis)
        cache.delete(cache_keys)
        redis.delete.assert_called_once_with(*cache_keys)

    @staticmethod
    def test_watch():
        def mock_redis_get(key):
            if key == "foo":
                return "moo"

            return "nope"

        redis = mock.Mock(
            pipeline=mock.Mock(spec=("watch", "get", "reset")), spec=("pipeline",)
        )
        pipe = redis.pipeline.return_value
        pipe.get.side_effect = mock_redis_get
        items = {"foo": "moo", "bar": "car"}
        cache = global_cache.RedisCache(redis)
        cache.watch(items)

        pipe.watch.assert_has_calls(
            [
                mock.call("foo"),
                mock.call("bar"),
            ],
            any_order=True,
        )

        pipe.get.assert_has_calls(
            [
                mock.call("foo"),
                mock.call("bar"),
            ],
            any_order=True,
        )

        assert cache.pipes == {"foo": pipe}

    @staticmethod
    def test_unwatch():
        redis = mock.Mock(spec=())
        cache = global_cache.RedisCache(redis)
        pipe = mock.Mock(spec=("reset",))
        cache._pipes.pipes = {
            "ay": pipe,
            "be": pipe,
            "see": pipe,
            "dee": pipe,
            "whatevs": "himom!",
        }

        cache.unwatch(["ay", "be", "see", "dee", "nuffin"])
        assert cache.pipes == {"whatevs": "himom!"}
        pipe.reset.assert_has_calls([mock.call()] * 4)

    @staticmethod
    def test_compare_and_swap():
        redis = mock.Mock(spec=())
        cache = global_cache.RedisCache(redis)
        pipe1 = mock.Mock(spec=("multi", "set", "execute", "reset"))
        pipe2 = mock.Mock(spec=("multi", "set", "execute", "reset"))
        pipe2.execute.side_effect = redis_module.exceptions.WatchError
        cache._pipes.pipes = {
            "foo": pipe1,
            "bar": pipe2,
        }

        result = cache.compare_and_swap(
            {
                "foo": "moo",
                "bar": "car",
                "baz": "maz",
            }
        )
        assert result == {"foo": True, "bar": False, "baz": False}

        pipe1.multi.assert_called_once_with()
        pipe1.set.assert_called_once_with("foo", "moo")
        pipe1.execute.assert_called_once_with()
        pipe1.reset.assert_called_once_with()

        pipe2.multi.assert_called_once_with()
        pipe2.set.assert_called_once_with("bar", "car")
        pipe2.execute.assert_called_once_with()
        pipe2.reset.assert_called_once_with()

    @staticmethod
    def test_compare_and_swap_w_expires():
        redis = mock.Mock(spec=())
        cache = global_cache.RedisCache(redis)
        pipe1 = mock.Mock(spec=("multi", "setex", "execute", "reset"))
        pipe2 = mock.Mock(spec=("multi", "setex", "execute", "reset"))
        pipe2.execute.side_effect = redis_module.exceptions.WatchError
        cache._pipes.pipes = {
            "foo": pipe1,
            "bar": pipe2,
        }

        result = cache.compare_and_swap(
            {
                "foo": "moo",
                "bar": "car",
                "baz": "maz",
            },
            expires=5,
        )
        assert result == {"foo": True, "bar": False, "baz": False}

        pipe1.multi.assert_called_once_with()
        pipe1.setex.assert_called_once_with("foo", 5, "moo")
        pipe1.execute.assert_called_once_with()
        pipe1.reset.assert_called_once_with()

        pipe2.multi.assert_called_once_with()
        pipe2.setex.assert_called_once_with("bar", 5, "car")
        pipe2.execute.assert_called_once_with()
        pipe2.reset.assert_called_once_with()

    @staticmethod
    def test_clear():
        redis = mock.Mock(spec=("flushdb",))
        cache = global_cache.RedisCache(redis)
        cache.clear()
        redis.flushdb.assert_called_once_with()


class TestMemcacheCache:
    @staticmethod
    def test__key_long_key():
        key = b"ou812" * 100
        encoded = global_cache.MemcacheCache._key(key)
        assert len(encoded) == 40  # sha1 hashes are 40 bytes

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_not_configured(pymemcache):
        with mock.patch.dict("os.environ", {"MEMCACHED_HOSTS": None}):
            assert global_cache.MemcacheCache.from_environment() is None

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_one_host_no_port(pymemcache):
        with mock.patch.dict("os.environ", {"MEMCACHED_HOSTS": "somehost"}):
            cache = global_cache.MemcacheCache.from_environment()
            assert cache.client is pymemcache.PooledClient.return_value
            pymemcache.PooledClient.assert_called_once_with(
                ("somehost", 11211), max_pool_size=4
            )

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_one_host_with_port(pymemcache):
        with mock.patch.dict("os.environ", {"MEMCACHED_HOSTS": "somehost:22422"}):
            cache = global_cache.MemcacheCache.from_environment()
            assert cache.client is pymemcache.PooledClient.return_value
            pymemcache.PooledClient.assert_called_once_with(
                ("somehost", 22422), max_pool_size=4
            )

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_two_hosts_with_port(pymemcache):
        with mock.patch.dict(
            "os.environ", {"MEMCACHED_HOSTS": "somehost:22422 otherhost:33633"}
        ):
            cache = global_cache.MemcacheCache.from_environment()
            assert cache.client is pymemcache.HashClient.return_value
            pymemcache.HashClient.assert_called_once_with(
                [("somehost", 22422), ("otherhost", 33633)],
                use_pooling=True,
                max_pool_size=4,
            )

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_two_hosts_no_port(pymemcache):
        with mock.patch.dict("os.environ", {"MEMCACHED_HOSTS": "somehost otherhost"}):
            cache = global_cache.MemcacheCache.from_environment()
            assert cache.client is pymemcache.HashClient.return_value
            pymemcache.HashClient.assert_called_once_with(
                [("somehost", 11211), ("otherhost", 11211)],
                use_pooling=True,
                max_pool_size=4,
            )

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_one_host_no_port_pool_size_zero(pymemcache):
        with mock.patch.dict("os.environ", {"MEMCACHED_HOSTS": "somehost"}):
            cache = global_cache.MemcacheCache.from_environment(max_pool_size=0)
            assert cache.client is pymemcache.PooledClient.return_value
            pymemcache.PooledClient.assert_called_once_with(
                ("somehost", 11211), max_pool_size=1
            )

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_bad_host_extra_colon(pymemcache):
        with mock.patch.dict("os.environ", {"MEMCACHED_HOSTS": "somehost:say:what?"}):
            with pytest.raises(ValueError):
                global_cache.MemcacheCache.from_environment()

    @staticmethod
    @mock.patch("google.cloud.ndb.global_cache.pymemcache")
    def test_from_environment_bad_host_port_not_an_integer(pymemcache):
        with mock.patch.dict("os.environ", {"MEMCACHED_HOSTS": "somehost:saywhat?"}):
            with pytest.raises(ValueError):
                global_cache.MemcacheCache.from_environment()

    @staticmethod
    def test_get():
        client = mock.Mock(spec=("get_many",))
        cache = global_cache.MemcacheCache(client)
        key1 = cache._key(b"one")
        key2 = cache._key(b"two")
        client.get_many.return_value = {key1: "bun", key2: "shoe"}
        assert cache.get((b"one", b"two")) == ["bun", "shoe"]
        client.get_many.assert_called_once_with([key1, key2])

    @staticmethod
    def test_set():
        client = mock.Mock(spec=("set_many",))
        client.set_many.return_value = []
        cache = global_cache.MemcacheCache(client)
        key1 = cache._key(b"one")
        key2 = cache._key(b"two")
        cache.set(
            {
                b"one": "bun",
                b"two": "shoe",
            }
        )
        client.set_many.assert_called_once_with(
            {
                key1: "bun",
                key2: "shoe",
            },
            expire=0,
            noreply=False,
        )

    @staticmethod
    def test_set_if_not_exists():
        client = mock.Mock(spec=("add",))
        client.add.side_effect = (True, False)
        cache_items = collections.OrderedDict([(b"a", b"foo"), (b"b", b"bar")])
        cache = global_cache.MemcacheCache(client)
        results = cache.set_if_not_exists(cache_items)
        assert results == {b"a": True, b"b": False}
        client.add.assert_has_calls(
            [
                mock.call(cache._key(b"a"), b"foo", expire=0, noreply=False),
                mock.call(cache._key(b"b"), b"bar", expire=0, noreply=False),
            ]
        )

    @staticmethod
    def test_set_if_not_exists_w_expires():
        client = mock.Mock(spec=("add",))
        client.add.side_effect = (True, False)
        cache_items = collections.OrderedDict([(b"a", b"foo"), (b"b", b"bar")])
        cache = global_cache.MemcacheCache(client)
        results = cache.set_if_not_exists(cache_items, expires=123)
        assert results == {b"a": True, b"b": False}
        client.add.assert_has_calls(
            [
                mock.call(cache._key(b"a"), b"foo", expire=123, noreply=False),
                mock.call(cache._key(b"b"), b"bar", expire=123, noreply=False),
            ]
        )

    @staticmethod
    def test_set_w_expires():
        client = mock.Mock(spec=("set_many",))
        client.set_many.return_value = []
        cache = global_cache.MemcacheCache(client)
        key1 = cache._key(b"one")
        key2 = cache._key(b"two")
        cache.set(
            {
                b"one": "bun",
                b"two": "shoe",
            },
            expires=5,
        )
        client.set_many.assert_called_once_with(
            {
                key1: "bun",
                key2: "shoe",
            },
            expire=5,
            noreply=False,
        )

    @staticmethod
    def test_set_failed_key():
        client = mock.Mock(spec=("set_many",))
        cache = global_cache.MemcacheCache(client)
        key1 = cache._key(b"one")
        key2 = cache._key(b"two")
        client.set_many.return_value = [key2]

        unset = cache.set(
            {
                b"one": "bun",
                b"two": "shoe",
            }
        )
        assert unset == {b"two": global_cache.MemcacheCache.KeyNotSet(b"two")}

        client.set_many.assert_called_once_with(
            {
                key1: "bun",
                key2: "shoe",
            },
            expire=0,
            noreply=False,
        )

    @staticmethod
    def test_KeyNotSet():
        unset = global_cache.MemcacheCache.KeyNotSet(b"foo")
        assert unset == global_cache.MemcacheCache.KeyNotSet(b"foo")
        assert not unset == global_cache.MemcacheCache.KeyNotSet(b"goo")
        assert not unset == "hamburger"

    @staticmethod
    def test_delete():
        client = mock.Mock(spec=("delete_many",))
        cache = global_cache.MemcacheCache(client)
        key1 = cache._key(b"one")
        key2 = cache._key(b"two")
        cache.delete((b"one", b"two"))
        client.delete_many.assert_called_once_with([key1, key2])

    @staticmethod
    def test_watch():
        client = mock.Mock(spec=("gets_many",))
        cache = global_cache.MemcacheCache(client)
        key1 = cache._key(b"one")
        key2 = cache._key(b"two")
        client.gets_many.return_value = {
            key1: ("bun", b"0"),
            key2: ("shoe", b"1"),
        }
        cache.watch(
            collections.OrderedDict(
                (
                    (b"one", "bun"),
                    (b"two", "shot"),
                )
            )
        )
        client.gets_many.assert_called_once_with([key1, key2])
        assert cache.caskeys == {
            key1: b"0",
        }

    @staticmethod
    def test_unwatch():
        client = mock.Mock(spec=())
        cache = global_cache.MemcacheCache(client)
        key2 = cache._key(b"two")
        cache.caskeys[key2] = b"5"
        cache.caskeys["whatevs"] = b"6"
        cache.unwatch([b"one", b"two"])

        assert cache.caskeys == {"whatevs": b"6"}

    @staticmethod
    def test_compare_and_swap():
        client = mock.Mock(spec=("cas",))
        cache = global_cache.MemcacheCache(client)
        key2 = cache._key(b"two")
        cache.caskeys[key2] = b"5"
        cache.caskeys["whatevs"] = b"6"
        result = cache.compare_and_swap(
            {
                b"one": "bun",
                b"two": "shoe",
            }
        )

        assert result == {b"two": True}
        client.cas.assert_called_once_with(key2, "shoe", b"5", expire=0, noreply=False)
        assert cache.caskeys == {"whatevs": b"6"}

    @staticmethod
    def test_compare_and_swap_and_expires():
        client = mock.Mock(spec=("cas",))
        cache = global_cache.MemcacheCache(client)
        key2 = cache._key(b"two")
        cache.caskeys[key2] = b"5"
        cache.caskeys["whatevs"] = b"6"
        result = cache.compare_and_swap(
            {
                b"one": "bun",
                b"two": "shoe",
            },
            expires=5,
        )

        assert result == {b"two": True}
        client.cas.assert_called_once_with(key2, "shoe", b"5", expire=5, noreply=False)
        assert cache.caskeys == {"whatevs": b"6"}

    @staticmethod
    def test_clear():
        client = mock.Mock(spec=("flush_all",))
        cache = global_cache.MemcacheCache(client)
        cache.clear()
        client.flush_all.assert_called_once_with()
