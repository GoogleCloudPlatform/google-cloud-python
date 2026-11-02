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

import warnings
from unittest import mock

import pytest

from google.cloud.ndb import _cache, tasklets


def future_result(result):
    future = tasklets.Future()
    future.set_result(result)
    return future


class TestContextCache:
    @staticmethod
    def test_get_and_validate_valid():
        cache = _cache.ContextCache()
        test_entity = mock.Mock(_key="test")
        cache["test"] = test_entity
        assert cache.get_and_validate("test") is test_entity

    @staticmethod
    def test_get_and_validate_invalid():
        cache = _cache.ContextCache()
        test_entity = mock.Mock(_key="test")
        cache["test"] = test_entity
        test_entity._key = "changed_key"
        with pytest.raises(KeyError):
            cache.get_and_validate("test")

    @staticmethod
    def test_get_and_validate_none():
        cache = _cache.ContextCache()
        cache["test"] = None
        assert cache.get_and_validate("test") is None

    @staticmethod
    def test_get_and_validate_miss():
        cache = _cache.ContextCache()
        with pytest.raises(KeyError):
            cache.get_and_validate("nonexistent_key")

    @staticmethod
    def test___repr__():
        cache = _cache.ContextCache()
        cache["hello dad"] = "i'm in jail"
        assert repr(cache) == "ContextCache()"


class Test_GlobalCacheBatch:
    @staticmethod
    def test_make_call():
        batch = _cache._GlobalCacheBatch()
        with pytest.raises(NotImplementedError):
            batch.make_call()

    @staticmethod
    def test_future_info():
        batch = _cache._GlobalCacheBatch()
        with pytest.raises(NotImplementedError):
            batch.future_info(None)

    @staticmethod
    def test_idle_callback_exception():
        class TransientError(Exception):
            pass

        error = TransientError("oops")
        batch = _cache._GlobalCacheBatch()
        batch.make_call = mock.Mock(side_effect=error)
        future1, future2 = tasklets.Future(), tasklets.Future()
        batch.futures = [future1, future2]
        batch.idle_callback()
        assert future1.exception() is error
        assert future2.exception() is error


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._cache._global_cache")
@mock.patch("google.cloud.ndb._cache._batch")
def test_global_get(_batch, _global_cache):
    batch = _batch.get_batch.return_value
    future = _future_result("hi mom!")
    batch.add.return_value = future
    _global_cache.return_value = mock.Mock(
        transient_errors=(),
        strict_read=False,
        spec=("transient_errors", "strict_read"),
    )

    assert _cache.global_get(b"foo").result() == "hi mom!"
    _batch.get_batch.assert_called_once_with(_cache._GlobalCacheGetBatch)
    batch.add.assert_called_once_with(b"foo")


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.tasklets.sleep")
@mock.patch("google.cloud.ndb._cache._global_cache")
@mock.patch("google.cloud.ndb._cache._batch")
def test_global_get_with_error_strict(_batch, _global_cache, sleep):
    class TransientError(Exception):
        pass

    sleep.return_value = future_result(None)
    batch = _batch.get_batch.return_value
    future = _future_exception(TransientError("oops"))
    batch.add.return_value = future
    _global_cache.return_value = mock.Mock(
        transient_errors=(TransientError,),
        strict_read=True,
        spec=("transient_errors", "strict_read"),
    )

    with pytest.raises(TransientError):
        _cache.global_get(b"foo").result()

    _batch.get_batch.assert_called_with(_cache._GlobalCacheGetBatch)
    batch.add.assert_called_with(b"foo")


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.tasklets.sleep")
@mock.patch("google.cloud.ndb._cache._global_cache")
@mock.patch("google.cloud.ndb._cache._batch")
def test_global_get_with_error_strict_retry(_batch, _global_cache, sleep):
    class TransientError(Exception):
        pass

    sleep.return_value = future_result(None)
    batch = _batch.get_batch.return_value
    batch.add.side_effect = [
        _future_exception(TransientError("oops")),
        future_result("hi mom!"),
    ]
    _global_cache.return_value = mock.Mock(
        transient_errors=(TransientError,),
        strict_read=True,
        spec=("transient_errors", "strict_read"),
    )

    assert _cache.global_get(b"foo").result() == "hi mom!"
    _batch.get_batch.assert_called_with(_cache._GlobalCacheGetBatch)
    batch.add.assert_called_with(b"foo")


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._cache._global_cache")
@mock.patch("google.cloud.ndb._cache._batch")
def test_global_get_with_error_not_strict(_batch, _global_cache):
    class TransientError(Exception):
        pass

    batch = _batch.get_batch.return_value
    future = _future_exception(TransientError("oops"))
    batch.add.return_value = future
    _global_cache.return_value = mock.Mock(
        transient_errors=(TransientError,),
        strict_read=False,
        spec=("transient_errors", "strict_read"),
    )

    with warnings.catch_warnings(record=True) as logged:
        assert _cache.global_get(b"foo").result() is None
        assert len(logged) in [1, 2]

    _batch.get_batch.assert_called_once_with(_cache._GlobalCacheGetBatch)
    batch.add.assert_called_once_with(b"foo")


class Test_GlobalCacheGetBatch:
    @staticmethod
    def test_add_and_idle_and_done_callbacks(in_context):
        cache = mock.Mock()
        cache.get.return_value = future_result([b"one", b"two"])

        batch = _cache._GlobalCacheGetBatch(None)
        future1 = batch.add(b"foo")
        future2 = batch.add(b"bar")
        future3 = batch.add(b"foo")

        assert set(batch.todo.keys()) == {b"foo", b"bar"}
        assert batch.keys == [b"foo", b"bar"]

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.get.assert_called_once_with(batch.keys)
        assert future1.result() == b"one"
        assert future2.result() == b"two"
        assert future3.result() == b"one"

    @staticmethod
    def test_add_and_idle_and_done_callbacks_synchronous(in_context):
        cache = mock.Mock()
        cache.get.return_value = [b"one", b"two"]

        batch = _cache._GlobalCacheGetBatch(None)
        future1 = batch.add(b"foo")
        future2 = batch.add(b"bar")

        assert set(batch.todo.keys()) == {b"foo", b"bar"}
        assert batch.keys == [b"foo", b"bar"]

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.get.assert_called_once_with(batch.keys)
        assert future1.result() == b"one"
        assert future2.result() == b"two"

    @staticmethod
    def test_add_and_idle_and_done_callbacks_w_error(in_context):
        error = Exception("spurious error")
        cache = mock.Mock()
        cache.get.return_value = tasklets.Future()
        cache.get.return_value.set_exception(error)

        batch = _cache._GlobalCacheGetBatch(None)
        future1 = batch.add(b"foo")
        future2 = batch.add(b"bar")

        assert set(batch.todo.keys()) == {b"foo", b"bar"}
        assert batch.keys == [b"foo", b"bar"]

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.get.assert_called_once_with(batch.keys)
        assert future1.exception() is error
        assert future2.exception() is error

    @staticmethod
    def test_full():
        batch = _cache._GlobalCacheGetBatch(None)
        assert batch.full() is False


@pytest.mark.usefixtures("in_context")
class Test_global_set:
    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_without_expires(_batch, _global_cache):
        batch = _batch.get_batch.return_value
        future = _future_result("hi mom!")
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        assert _cache.global_set(b"key", b"value").result() == "hi mom!"
        _batch.get_batch.assert_called_once_with(_cache._GlobalCacheSetBatch, {})
        batch.add.assert_called_once_with(b"key", b"value")

    @staticmethod
    @mock.patch("google.cloud.ndb.tasklets.sleep")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_error_strict(_batch, _global_cache, sleep):
        class TransientError(Exception):
            pass

        sleep.return_value = future_result(None)
        batch = _batch.get_batch.return_value
        future = _future_exception(TransientError("oops"))
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(TransientError,),
            spec=("transient_errors", "strict_write"),
        )

        with pytest.raises(TransientError):
            _cache.global_set(b"key", b"value").result()

        _batch.get_batch.assert_called_with(_cache._GlobalCacheSetBatch, {})
        batch.add.assert_called_with(b"key", b"value")

    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_error_not_strict_already_warned(_batch, _global_cache):
        class TransientError(Exception):
            pass

        batch = _batch.get_batch.return_value
        error = TransientError("oops")
        error._ndb_warning_logged = True
        future = _future_exception(error)
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(TransientError,),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        with warnings.catch_warnings(record=True) as logged:
            assert _cache.global_set(b"key", b"value").result() is None
            assert len(logged) in [0, 1]

        _batch.get_batch.assert_called_once_with(_cache._GlobalCacheSetBatch, {})
        batch.add.assert_called_once_with(b"key", b"value")

    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_with_expires(_batch, _global_cache):
        batch = _batch.get_batch.return_value
        future = _future_result("hi mom!")
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        future = _cache.global_set(b"key", b"value", expires=5)
        assert future.result() == "hi mom!"
        _batch.get_batch.assert_called_once_with(
            _cache._GlobalCacheSetBatch, {"expires": 5}
        )
        batch.add.assert_called_once_with(b"key", b"value")


class Test_GlobalCacheSetBatch:
    @staticmethod
    def test_add_duplicate_key_and_value():
        batch = _cache._GlobalCacheSetBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"foo", b"one")
        assert future1 is future2

    @staticmethod
    def test_add_and_idle_and_done_callbacks(in_context):
        cache = mock.Mock(spec=("set",))
        cache.set.return_value = []

        batch = _cache._GlobalCacheSetBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        assert batch.expires is None

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set.assert_called_once_with(
            {b"foo": b"one", b"bar": b"two"}, expires=None
        )
        assert future1.result() is None
        assert future2.result() is None

    @staticmethod
    def test_add_and_idle_and_done_callbacks_with_duplicate_keys(in_context):
        cache = mock.Mock(spec=("set",))
        cache.set.return_value = []

        batch = _cache._GlobalCacheSetBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"foo", b"two")

        assert batch.expires is None

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set.assert_called_once_with({b"foo": b"one"}, expires=None)
        assert future1.result() is None
        with pytest.raises(RuntimeError):
            future2.result()

    @staticmethod
    def test_add_and_idle_and_done_callbacks_with_expires(in_context):
        cache = mock.Mock(spec=("set",))
        cache.set.return_value = []

        batch = _cache._GlobalCacheSetBatch({"expires": 5})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        assert batch.expires == 5

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set.assert_called_once_with({b"foo": b"one", b"bar": b"two"}, expires=5)
        assert future1.result() is None
        assert future2.result() is None

    @staticmethod
    def test_add_and_idle_and_done_callbacks_w_error(in_context):
        error = Exception("spurious error")
        cache = mock.Mock(spec=("set",))
        cache.set.return_value = tasklets.Future()
        cache.set.return_value.set_exception(error)

        batch = _cache._GlobalCacheSetBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set.assert_called_once_with(
            {b"foo": b"one", b"bar": b"two"}, expires=None
        )
        assert future1.exception() is error
        assert future2.exception() is error

    @staticmethod
    def test_done_callbacks_with_results(in_context):
        class SpeciousError(Exception):
            pass

        cache_call = _future_result(
            {
                b"foo": "this is a result",
                b"bar": SpeciousError("this is also a kind of result"),
            }
        )

        batch = _cache._GlobalCacheSetBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        batch.done_callback(cache_call)

        assert future1.result() == "this is a result"
        with pytest.raises(SpeciousError):
            assert future2.result()


@pytest.mark.usefixtures("in_context")
class Test_global_set_if_not_exists:
    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_without_expires(_batch, _global_cache):
        batch = _batch.get_batch.return_value
        future = _future_result("hi mom!")
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        assert _cache.global_set_if_not_exists(b"key", b"value").result() == "hi mom!"
        _batch.get_batch.assert_called_once_with(
            _cache._GlobalCacheSetIfNotExistsBatch, {}
        )
        batch.add.assert_called_once_with(b"key", b"value")

    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_transientError(_batch, _global_cache):
        class TransientError(Exception):
            pass

        batch = _batch.get_batch.return_value
        future = _future_exception(TransientError("oops, mom!"))
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(TransientError,),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        assert _cache.global_set_if_not_exists(b"key", b"value").result() is False
        _batch.get_batch.assert_called_once_with(
            _cache._GlobalCacheSetIfNotExistsBatch, {}
        )
        batch.add.assert_called_once_with(b"key", b"value")

    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_with_expires(_batch, _global_cache):
        batch = _batch.get_batch.return_value
        future = _future_result("hi mom!")
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        assert (
            _cache.global_set_if_not_exists(b"key", b"value", expires=123).result()
            == "hi mom!"
        )
        _batch.get_batch.assert_called_once_with(
            _cache._GlobalCacheSetIfNotExistsBatch, {"expires": 123}
        )
        batch.add.assert_called_once_with(b"key", b"value")


class Test_GlobalCacheSetIfNotExistsBatch:
    @staticmethod
    def test_add_duplicate_key_and_value():
        batch = _cache._GlobalCacheSetIfNotExistsBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"foo", b"one")
        assert not future1.done()
        assert future2.result() is False

    @staticmethod
    def test_add_and_idle_and_done_callbacks(in_context):
        cache = mock.Mock(spec=("set_if_not_exists",))
        cache.set_if_not_exists.return_value = {}

        batch = _cache._GlobalCacheSetIfNotExistsBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        assert batch.expires is None

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set_if_not_exists.assert_called_once_with(
            {b"foo": b"one", b"bar": b"two"}, expires=None
        )
        assert future1.result() is None
        assert future2.result() is None

    @staticmethod
    def test_add_and_idle_and_done_callbacks_with_duplicate_keys(in_context):
        cache = mock.Mock(spec=("set_if_not_exists",))
        cache.set_if_not_exists.return_value = {b"foo": True}

        batch = _cache._GlobalCacheSetIfNotExistsBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"foo", b"two")

        assert batch.expires is None

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set_if_not_exists.assert_called_once_with({b"foo": b"one"}, expires=None)
        assert future1.result() is True
        assert future2.result() is False

    @staticmethod
    def test_add_and_idle_and_done_callbacks_with_expires(in_context):
        cache = mock.Mock(spec=("set_if_not_exists",))
        cache.set_if_not_exists.return_value = []

        batch = _cache._GlobalCacheSetIfNotExistsBatch({"expires": 5})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        assert batch.expires == 5

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set_if_not_exists.assert_called_once_with(
            {b"foo": b"one", b"bar": b"two"}, expires=5
        )
        assert future1.result() is None
        assert future2.result() is None

    @staticmethod
    def test_add_and_idle_and_done_callbacks_w_error(in_context):
        error = Exception("spurious error")
        cache = mock.Mock(spec=("set_if_not_exists",))
        cache.set_if_not_exists.return_value = tasklets.Future()
        cache.set_if_not_exists.return_value.set_exception(error)

        batch = _cache._GlobalCacheSetIfNotExistsBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.set_if_not_exists.assert_called_once_with(
            {b"foo": b"one", b"bar": b"two"}, expires=None
        )
        assert future1.exception() is error
        assert future2.exception() is error

    @staticmethod
    def test_done_callbacks_with_results(in_context):
        class SpeciousError(Exception):
            pass

        cache_call = _future_result(
            {
                b"foo": "this is a result",
                b"bar": SpeciousError("this is also a kind of result"),
            }
        )

        batch = _cache._GlobalCacheSetIfNotExistsBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        batch.done_callback(cache_call)

        assert future1.result() == "this is a result"
        with pytest.raises(SpeciousError):
            assert future2.result()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._cache._global_cache")
@mock.patch("google.cloud.ndb._cache._batch")
def test_global_delete(_batch, _global_cache):
    batch = _batch.get_batch.return_value
    future = _future_result("hi mom!")
    batch.add.return_value = future
    _global_cache.return_value = mock.Mock(
        transient_errors=(),
        strict_write=False,
        spec=("transient_errors", "strict_write"),
    )

    assert _cache.global_delete(b"key").result() == "hi mom!"
    _batch.get_batch.assert_called_once_with(_cache._GlobalCacheDeleteBatch)
    batch.add.assert_called_once_with(b"key")


class Test_GlobalCacheDeleteBatch:
    @staticmethod
    def test_add_and_idle_and_done_callbacks(in_context):
        cache = mock.Mock()

        batch = _cache._GlobalCacheDeleteBatch({})
        future1 = batch.add(b"foo")
        future2 = batch.add(b"bar")

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.delete.assert_called_once_with([b"foo", b"bar"])
        assert future1.result() is None
        assert future2.result() is None


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._cache._global_cache")
@mock.patch("google.cloud.ndb._cache._batch")
def test_global_watch(_batch, _global_cache):
    batch = _batch.get_batch.return_value
    future = _future_result("hi mom!")
    batch.add.return_value = future
    _global_cache.return_value = mock.Mock(
        transient_errors=(),
        strict_read=False,
        spec=("transient_errors", "strict_read"),
    )

    assert _cache.global_watch(b"key", b"value").result() == "hi mom!"
    _batch.get_batch.assert_called_once_with(_cache._GlobalCacheWatchBatch, {})
    batch.add.assert_called_once_with(b"key", b"value")


@pytest.mark.usefixtures("in_context")
class Test_GlobalCacheWatchBatch:
    @staticmethod
    def test_add_and_idle_and_done_callbacks(in_context):
        cache = mock.Mock(spec=("watch",))
        cache.watch.return_value = None

        batch = _cache._GlobalCacheWatchBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        assert batch.expires is None

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.watch.assert_called_once_with({b"foo": b"one", b"bar": b"two"})
        assert future1.result() is None
        assert future2.result() is None


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._cache._global_cache")
@mock.patch("google.cloud.ndb._cache._batch")
def test_global_unwatch(_batch, _global_cache):
    batch = _batch.get_batch.return_value
    future = _future_result("hi mom!")
    batch.add.return_value = future
    _global_cache.return_value = mock.Mock(
        transient_errors=(),
        strict_write=False,
        spec=("transient_errors", "strict_write"),
    )

    assert _cache.global_unwatch(b"key").result() == "hi mom!"
    _batch.get_batch.assert_called_once_with(_cache._GlobalCacheUnwatchBatch, {})
    batch.add.assert_called_once_with(b"key")


class Test_GlobalCacheUnwatchBatch:
    @staticmethod
    def test_add_and_idle_and_done_callbacks(in_context):
        cache = mock.Mock()

        batch = _cache._GlobalCacheUnwatchBatch({})
        future1 = batch.add(b"foo")
        future2 = batch.add(b"bar")

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.unwatch.assert_called_once_with([b"foo", b"bar"])
        assert future1.result() is None
        assert future2.result() is None


@pytest.mark.usefixtures("in_context")
class Test_global_compare_and_swap:
    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_without_expires(_batch, _global_cache):
        batch = _batch.get_batch.return_value
        future = _future_result("hi mom!")
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_read=False,
            spec=("transient_errors", "strict_read"),
        )

        future = _cache.global_compare_and_swap(b"key", b"value")
        assert future.result() == "hi mom!"
        _batch.get_batch.assert_called_once_with(
            _cache._GlobalCacheCompareAndSwapBatch, {}
        )
        batch.add.assert_called_once_with(b"key", b"value")

    @staticmethod
    @mock.patch("google.cloud.ndb._cache._global_cache")
    @mock.patch("google.cloud.ndb._cache._batch")
    def test_with_expires(_batch, _global_cache):
        batch = _batch.get_batch.return_value
        future = _future_result("hi mom!")
        batch.add.return_value = future
        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_read=False,
            spec=("transient_errors", "strict_read"),
        )

        future = _cache.global_compare_and_swap(b"key", b"value", expires=5)
        assert future.result() == "hi mom!"
        _batch.get_batch.assert_called_once_with(
            _cache._GlobalCacheCompareAndSwapBatch, {"expires": 5}
        )
        batch.add.assert_called_once_with(b"key", b"value")


class Test_GlobalCacheCompareAndSwapBatch:
    @staticmethod
    def test_add_and_idle_and_done_callbacks(in_context):
        cache = mock.Mock(spec=("compare_and_swap",))
        cache.compare_and_swap.return_value = None

        batch = _cache._GlobalCacheCompareAndSwapBatch({})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        assert batch.expires is None

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.compare_and_swap.assert_called_once_with(
            {b"foo": b"one", b"bar": b"two"}, expires=None
        )
        assert future1.result() is None
        assert future2.result() is None

    @staticmethod
    def test_add_and_idle_and_done_callbacks_with_expires(in_context):
        cache = mock.Mock(spec=("compare_and_swap",))
        cache.compare_and_swap.return_value = None

        batch = _cache._GlobalCacheCompareAndSwapBatch({"expires": 5})
        future1 = batch.add(b"foo", b"one")
        future2 = batch.add(b"bar", b"two")

        assert batch.expires == 5

        with in_context.new(global_cache=cache).use():
            batch.idle_callback()

        cache.compare_and_swap.assert_called_once_with(
            {b"foo": b"one", b"bar": b"two"}, expires=5
        )
        assert future1.result() is None
        assert future2.result() is None


@pytest.mark.usefixtures("in_context")
class Test_global_lock_for_read:
    @staticmethod
    @mock.patch("google.cloud.ndb._cache.global_set_if_not_exists")
    def test_lock_acquired(global_set_if_not_exists):
        global_set_if_not_exists.return_value = _future_result(True)
        lock = _cache.global_lock_for_read(b"key", None).result()
        assert lock.startswith(_cache._LOCKED_FOR_READ)

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.global_set_if_not_exists")
    def test_lock_not_acquired(global_set_if_not_exists):
        global_set_if_not_exists.return_value = _future_result(False)
        lock = _cache.global_lock_for_read(b"key", None).result()
        assert lock is None

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.global_compare_and_swap")
    @mock.patch("google.cloud.ndb._cache.global_watch")
    def test_recently_written_and_lock_acquired(global_watch, global_compare_and_swap):
        global_watch.return_value = _future_result(True)
        global_compare_and_swap.return_value = _future_result(True)
        lock = _cache.global_lock_for_read(b"key", _cache._LOCKED_FOR_WRITE).result()
        assert lock.startswith(_cache._LOCKED_FOR_READ)

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.global_compare_and_swap")
    @mock.patch("google.cloud.ndb._cache.global_watch")
    def test_recently_written_and_lock_not_acquired(
        global_watch, global_compare_and_swap
    ):
        global_watch.return_value = _future_result(True)
        global_compare_and_swap.return_value = _future_result(False)
        lock = _cache.global_lock_for_read(b"key", _cache._LOCKED_FOR_WRITE).result()
        assert lock is None


@pytest.mark.usefixtures("in_context")
class Test_global_lock_for_write:
    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache.global_set_if_not_exists")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_first_time(_global_cache, _global_get, global_set_if_not_exists, uuid):
        uuid.uuid4.return_value = "arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        lock_value = _cache._LOCKED_FOR_WRITE + b".arandomuuid"
        _global_get.return_value = _future_result(None)
        global_set_if_not_exists.return_value = _future_result(True)

        assert _cache.global_lock_for_write(b"key").result() == b".arandomuuid"
        _global_get.assert_called_once_with(b"key")
        global_set_if_not_exists.assert_called_once_with(b"key", lock_value, expires=64)

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache._global_compare_and_swap")
    @mock.patch("google.cloud.ndb._cache._global_watch")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_not_first_time_fail_once(
        _global_cache, _global_get, _global_watch, _global_compare_and_swap, uuid
    ):
        uuid.uuid4.return_value = "arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        old_lock_value = _cache._LOCKED_FOR_WRITE + b".whatevs"
        new_lock_value = old_lock_value + b".arandomuuid"
        _global_get.return_value = _future_result(old_lock_value)
        _global_watch.return_value = _future_result(None)
        _global_compare_and_swap.side_effect = (
            _future_result(False),
            _future_result(True),
        )
        assert _cache.global_lock_for_write(b"key").result() == b".arandomuuid"
        _global_get.assert_has_calls(
            [
                mock.call(b"key"),
                mock.call(b"key"),
            ]
        )
        _global_watch.assert_has_calls(
            [
                mock.call(b"key", old_lock_value),
                mock.call(b"key", old_lock_value),
            ]
        )
        _global_compare_and_swap.assert_has_calls(
            [
                mock.call(b"key", new_lock_value, expires=64),
                mock.call(b"key", new_lock_value, expires=64),
            ]
        )


@pytest.mark.usefixtures("in_context")
class Test_global_unlock_for_write:
    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache._global_compare_and_swap")
    @mock.patch("google.cloud.ndb._cache._global_watch")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_last_time(
        _global_cache, _global_get, _global_watch, _global_compare_and_swap, uuid
    ):
        lock = b".arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        lock_value = _cache._LOCKED_FOR_WRITE + lock
        _global_get.return_value = _future_result(lock_value)
        _global_watch.return_value = _future_result(None)
        _global_compare_and_swap.return_value = _future_result(True)

        assert _cache.global_unlock_for_write(b"key", lock).result() is None
        _global_get.assert_called_once_with(b"key")
        _global_watch.assert_called_once_with(b"key", lock_value)
        _global_compare_and_swap.assert_called_once_with(b"key", b"", expires=64)

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache._global_compare_and_swap")
    @mock.patch("google.cloud.ndb._cache._global_watch")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_lock_missing(
        _global_cache, _global_get, _global_watch, _global_compare_and_swap, uuid
    ):
        lock = b".arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        lock_value = _cache._LOCKED_FOR_WRITE + b".adifferentlock"
        _global_get.return_value = _future_result(lock_value)
        _global_watch.return_value = _future_result(None)
        _global_compare_and_swap.return_value = _future_result(True)

        with warnings.catch_warnings(record=True) as logged:
            assert _cache.global_unlock_for_write(b"key", lock).result() is None
            logged = [
                warning for warning in logged if warning.category is RuntimeWarning
            ]
            assert len(logged) == 1

        _global_get.assert_called_once_with(b"key")
        _global_watch.assert_not_called()
        _global_compare_and_swap.assert_not_called()

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache.global_set_if_not_exists")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_no_value_in_cache(
        _global_cache, _global_get, global_set_if_not_exists, uuid
    ):
        lock = b".arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        _global_get.return_value = _future_result(None)
        global_set_if_not_exists.return_value = _future_result(True)

        with warnings.catch_warnings(record=True) as logged:
            assert _cache.global_unlock_for_write(b"key", lock).result() is None
            logged = [
                warning for warning in logged if warning.category is RuntimeWarning
            ]
            assert len(logged) == 1

        _global_get.assert_called_once_with(b"key")
        global_set_if_not_exists.assert_not_called()

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache._global_compare_and_swap")
    @mock.patch("google.cloud.ndb._cache._global_watch")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_lock_overwritten(
        _global_cache, _global_get, _global_watch, _global_compare_and_swap, uuid
    ):
        lock = b".arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        lock_value = b"SOMERANDOMVALUE"
        _global_get.return_value = _future_result(lock_value)
        _global_watch.return_value = _future_result(None)
        _global_compare_and_swap.return_value = _future_result(True)

        with warnings.catch_warnings(record=True) as logged:
            assert _cache.global_unlock_for_write(b"key", lock).result() is None
            logged = [
                warning for warning in logged if warning.category is RuntimeWarning
            ]
            assert len(logged) == 1

        _global_get.assert_called_once_with(b"key")
        _global_watch.assert_called_once_with(b"key", lock_value)
        _global_compare_and_swap.assert_called_once_with(b"key", b"", expires=64)

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache._global_watch")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_transient_error(_global_cache, _global_get, _global_watch, uuid):
        class TransientError(Exception):
            pass

        lock = b".arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(TransientError,),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        lock_value = _cache._LOCKED_FOR_WRITE + lock
        _global_get.return_value = _future_result(lock_value)
        _global_watch.return_value = _future_exception(TransientError())

        assert _cache.global_unlock_for_write(b"key", lock).result() is None
        _global_get.assert_called_once_with(b"key")
        _global_watch.assert_called_once_with(b"key", lock_value)

    @staticmethod
    @mock.patch("google.cloud.ndb._cache.uuid")
    @mock.patch("google.cloud.ndb._cache._global_compare_and_swap")
    @mock.patch("google.cloud.ndb._cache._global_watch")
    @mock.patch("google.cloud.ndb._cache._global_get")
    @mock.patch("google.cloud.ndb._cache._global_cache")
    def test_not_last_time_fail_once(
        _global_cache, _global_get, _global_watch, _global_compare_and_swap, uuid
    ):
        lock = b".arandomuuid"

        _global_cache.return_value = mock.Mock(
            transient_errors=(),
            strict_write=False,
            spec=("transient_errors", "strict_write"),
        )

        new_lock_value = _cache._LOCKED_FOR_WRITE + b".whatevs"
        old_lock_value = new_lock_value + lock
        _global_get.return_value = _future_result(old_lock_value)
        _global_watch.return_value = _future_result(None)
        _global_compare_and_swap.side_effect = (
            _future_result(False),
            _future_result(True),
        )

        assert _cache.global_unlock_for_write(b"key", lock).result() is None
        _global_get.assert_has_calls(
            [
                mock.call(b"key"),
                mock.call(b"key"),
            ]
        )
        _global_watch.assert_has_calls(
            [
                mock.call(b"key", old_lock_value),
                mock.call(b"key", old_lock_value),
            ]
        )
        _global_compare_and_swap.assert_has_calls(
            [
                mock.call(b"key", new_lock_value, expires=64),
                mock.call(b"key", new_lock_value, expires=64),
            ]
        )


def test_is_locked_value():
    assert _cache.is_locked_value(_cache._LOCKED_FOR_READ)
    assert _cache.is_locked_value(_cache._LOCKED_FOR_WRITE + b"whatever")
    assert not _cache.is_locked_value(b"")
    assert not _cache.is_locked_value(b"new db, who dis?")
    assert not _cache.is_locked_value(None)


def test_global_cache_key():
    key = mock.Mock()
    key.to_protobuf.return_value._pb.SerializeToString.return_value = b"himom!"
    assert _cache.global_cache_key(key) == _cache._PREFIX + b"himom!"
    key.to_protobuf.assert_called_once_with()
    key.to_protobuf.return_value._pb.SerializeToString.assert_called_once_with()


def _future_result(result):
    future = tasklets.Future()
    future.set_result(result)
    return future


def _future_exception(error):
    future = tasklets.Future()
    future.set_exception(error)
    return future
