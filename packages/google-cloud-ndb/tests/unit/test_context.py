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

import threading
from unittest import mock

import pytest

from google.cloud.ndb import _eventloop, _options, exceptions, model
from google.cloud.ndb import context as context_module
from google.cloud.ndb import key as key_module


class Test_get_context:
    @staticmethod
    def test_in_context(in_context):
        assert context_module.get_context() is in_context

    @staticmethod
    def test_no_context_raise():
        with pytest.raises(exceptions.ContextError):
            context_module.get_context()

    @staticmethod
    def test_no_context_dont_raise():
        assert context_module.get_context(False) is None


class Test_get_toplevel_context:
    @staticmethod
    def test_in_context(in_context):
        with in_context.new().use():
            assert context_module.get_toplevel_context() is in_context

    @staticmethod
    def test_no_context_raise():
        with pytest.raises(exceptions.ContextError):
            context_module.get_toplevel_context()

    @staticmethod
    def test_no_context_dont_raise():
        assert context_module.get_toplevel_context(False) is None


class TestContext:
    def _make_one(self, **kwargs):
        client = mock.Mock(
            namespace=None,
            project="testing",
            database="testdb",
            spec=("namespace", "project", "database"),
            stub=mock.Mock(spec=()),
        )
        return context_module.Context(client, **kwargs)

    def test_constructor_defaults(self):
        context = context_module.Context("client")
        assert context.client == "client"
        assert isinstance(context.eventloop, _eventloop.EventLoop)
        assert context.batches == {}
        assert context.transaction is None

        node1, pid1, sequence_no1 = context.id.split("-")
        node2, pid2, sequence_no2 = context_module.Context("client").id.split("-")
        assert node1 == node2
        assert pid1 == pid2
        assert int(sequence_no2) - int(sequence_no1) == 1

    def test_constructuor_concurrent_instantiation(self):
        """Regression test for #716

        This test non-deterministically tests a potential concurrency issue. Before the
        bug this is a test for was fixed, it failed most of the time.

        https://github.com/googleapis/python-ndb/issues/715
        """
        errors = []

        def make_some():
            try:
                for _ in range(10000):
                    context_module.Context("client")
            except Exception as error:  # pragma: NO COVER
                errors.append(error)

        thread1 = threading.Thread(target=make_some)
        thread2 = threading.Thread(target=make_some)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

        assert not errors

    def test_constructor_overrides(self):
        context = context_module.Context(
            client="client",
            eventloop="eventloop",
            batches="batches",
            transaction="transaction",
        )
        assert context.client == "client"
        assert context.eventloop == "eventloop"
        assert context.batches == "batches"
        assert context.transaction == "transaction"

    def test_new_transaction(self):
        context = self._make_one()
        new_context = context.new(transaction="tx123")
        assert new_context.transaction == "tx123"
        assert context.transaction is None

    def test_new_with_cache(self):
        context = self._make_one()
        context.cache["foo"] = "bar"
        new_context = context.new()
        assert context.cache is not new_context.cache
        assert context.cache == new_context.cache

    def test_use(self):
        context = self._make_one()
        with context.use():
            assert context_module.get_context() is context
        with pytest.raises(exceptions.ContextError):
            context_module.get_context()

    def test_use_nested(self):
        context = self._make_one()
        with context.use():
            assert context_module.get_context() is context
            next_context = context.new()
            with next_context.use():
                assert context_module.get_context() is next_context

            assert context_module.get_context() is context

        with pytest.raises(exceptions.ContextError):
            context_module.get_context()

    def test_clear_cache(self):
        context = self._make_one()
        context.cache["testkey"] = "testdata"
        context.clear_cache()
        assert not context.cache

    def test_flush(self):
        eventloop = mock.Mock(spec=("run",))
        context = self._make_one(eventloop=eventloop)
        context.flush()
        eventloop.run.assert_called_once_with()

    def test_get_cache_policy(self):
        context = self._make_one()
        assert context.get_cache_policy() is context_module._default_cache_policy

    def test_get_datastore_policy(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.get_datastore_policy()

    def test__use_datastore_default_policy(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one()
        with context.use():
            key = key_module.Key("SomeKind", 1)
            options = _options.Options()
            assert context._use_datastore(key, options) is True

    def test__use_datastore_from_options(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one()
        with context.use():
            key = key_module.Key("SomeKind", 1)
            options = _options.Options(use_datastore=False)
            assert context._use_datastore(key, options) is False

    def test_get_memcache_policy(self):
        context = self._make_one()
        context.get_memcache_policy()
        assert (
            context.get_memcache_policy() is context_module._default_global_cache_policy
        )

    def test_get_global_cache_policy(self):
        context = self._make_one()
        context.get_global_cache_policy()
        assert (
            context.get_memcache_policy() is context_module._default_global_cache_policy
        )

    def test_get_memcache_timeout_policy(self):
        context = self._make_one()
        assert (
            context.get_memcache_timeout_policy()
            is context_module._default_global_cache_timeout_policy
        )

    def test_get_global_cache_timeout_policy(self):
        context = self._make_one()
        assert (
            context.get_global_cache_timeout_policy()
            is context_module._default_global_cache_timeout_policy
        )

    def test_set_cache_policy(self):
        policy = object()
        context = self._make_one()
        context.set_cache_policy(policy)
        assert context.get_cache_policy() is policy

    def test_set_cache_policy_to_None(self):
        context = self._make_one()
        context.set_cache_policy(None)
        assert context.get_cache_policy() is context_module._default_cache_policy

    def test_set_cache_policy_with_bool(self):
        context = self._make_one()
        context.set_cache_policy(False)
        assert context.get_cache_policy()(None) is False

    def test__use_cache_default_policy(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one()
        with context.use():
            key = key_module.Key("SomeKind", 1)
            options = _options.Options()
            assert context._use_cache(key, options) is True

    def test__use_cache_from_options(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one()
        with context.use():
            key = "whocares"
            options = _options.Options(use_cache=False)
            assert context._use_cache(key, options) is False

    def test_set_datastore_policy(self):
        context = self._make_one()
        context.set_datastore_policy(None)
        assert context.datastore_policy is context_module._default_datastore_policy

    def test_set_datastore_policy_as_bool(self):
        context = self._make_one()
        context.set_datastore_policy(False)
        context.datastore_policy(None) is False

    def test_set_memcache_policy(self):
        context = self._make_one()
        context.set_memcache_policy(None)
        assert (
            context.global_cache_policy is context_module._default_global_cache_policy
        )

    def test_set_global_cache_policy(self):
        context = self._make_one()
        context.set_global_cache_policy(None)
        assert (
            context.global_cache_policy is context_module._default_global_cache_policy
        )

    def test_set_global_cache_policy_as_bool(self):
        context = self._make_one()
        context.set_global_cache_policy(True)
        assert context.global_cache_policy("whatever") is True

    def test__use_global_cache_no_global_cache(self):
        context = self._make_one()
        assert context._use_global_cache("key") is False

    def test__use_global_cache_default_policy(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one(global_cache="yes, there is one")
        with context.use():
            key = key_module.Key("SomeKind", 1)
            assert context._use_global_cache(key._key) is True

    def test__use_global_cache_from_options(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one(global_cache="yes, there is one")
        with context.use():
            key = "whocares"
            options = _options.Options(use_global_cache=False)
            assert context._use_global_cache(key, options=options) is False

    def test_set_memcache_timeout_policy(self):
        context = self._make_one()
        context.set_memcache_timeout_policy(None)
        assert (
            context.global_cache_timeout_policy
            is context_module._default_global_cache_timeout_policy
        )

    def test_set_global_cache_timeout_policy(self):
        context = self._make_one()
        context.set_global_cache_timeout_policy(None)
        assert (
            context.global_cache_timeout_policy
            is context_module._default_global_cache_timeout_policy
        )

    def test_set_global_cache_timeout_policy_as_int(self):
        context = self._make_one()
        context.set_global_cache_timeout_policy(14)
        assert context.global_cache_timeout_policy("whatever") == 14

    def test__global_cache_timeout_default_policy(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one()
        with context.use():
            key = key_module.Key("SomeKind", 1)
            timeout = context._global_cache_timeout(key._key, None)
            assert timeout is None

    def test__global_cache_timeout_from_options(self):
        class SomeKind(model.Model):
            pass

        context = self._make_one()
        with context.use():
            key = "whocares"
            options = _options.Options(global_cache_timeout=49)
            assert context._global_cache_timeout(key, options) == 49

    def test_call_on_commit(self):
        context = self._make_one()
        callback = mock.Mock()
        context.call_on_commit(callback)
        callback.assert_called_once_with()

    def test_call_on_commit_with_transaction(self):
        callbacks = []
        callback = "himom!"
        context = self._make_one(transaction=b"tx123", on_commit_callbacks=callbacks)
        context.call_on_commit(callback)
        assert context.on_commit_callbacks == ["himom!"]

    def test_call_on_transaction_complete(self):
        context = self._make_one()
        callback = mock.Mock()
        context.call_on_transaction_complete(callback)
        callback.assert_called_once_with()

    def test_call_on_transaction_complete_with_transaction(self):
        callbacks = []
        callback = "himom!"
        context = self._make_one(
            transaction=b"tx123", transaction_complete_callbacks=callbacks
        )
        context.call_on_transaction_complete(callback)
        assert context.transaction_complete_callbacks == ["himom!"]

    def test_in_transaction(self):
        context = self._make_one()
        assert context.in_transaction() is False

    def test_get_namespace_from_client(self):
        context = self._make_one()
        context.client.namespace = "hamburgers"
        assert context.get_namespace() == "hamburgers"

    def test_get_namespace_from_context(self):
        context = self._make_one(namespace="hotdogs")
        context.client.namespace = "hamburgers"
        assert context.get_namespace() == "hotdogs"

    def test_memcache_add(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_add()

    def test_memcache_cas(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_cas()

    def test_memcache_decr(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_decr()

    def test_memcache_replace(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_replace()

    def test_memcache_set(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_set()

    def test_memcache_delete(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_delete()

    def test_memcache_get(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_get()

    def test_memcache_gets(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_gets()

    def test_memcache_incr(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.memcache_incr()

    def test_urlfetch(self):
        context = self._make_one()
        with pytest.raises(NotImplementedError):
            context.urlfetch()


class TestAutoBatcher:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            context_module.AutoBatcher()


class TestContextOptions:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            context_module.ContextOptions()


class TestTransactionOptions:
    @staticmethod
    def test_constructor():
        assert len(context_module.TransactionOptions._PROPAGATION) == 4


class Test_default_cache_policy:
    @staticmethod
    def test_key_is_None():
        assert context_module._default_cache_policy(None) is None

    @staticmethod
    def test_no_model_class():
        key = mock.Mock(kind=mock.Mock(return_value="nokind"), spec=("kind",))
        assert context_module._default_cache_policy(key) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model():
        class ThisKind(model.Model):
            pass

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_cache_policy(key) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model_defines_policy():
        flag = object()

        class ThisKind(model.Model):
            @classmethod
            def _use_cache(cls, key):
                return flag

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_cache_policy(key) is flag

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model_defines_policy_as_bool():
        class ThisKind(model.Model):
            _use_cache = False

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_cache_policy(key) is False


class Test_default_global_cache_policy:
    @staticmethod
    def test_key_is_None():
        assert context_module._default_global_cache_policy(None) is None

    @staticmethod
    def test_no_model_class():
        key = mock.Mock(kind="nokind", spec=("kind",))
        assert context_module._default_global_cache_policy(key) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model():
        class ThisKind(model.Model):
            pass

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_global_cache_policy(key._key) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model_defines_policy():
        flag = object()

        class ThisKind(model.Model):
            @classmethod
            def _use_global_cache(cls, key):
                return flag

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_global_cache_policy(key._key) is flag

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model_defines_policy_as_bool():
        class ThisKind(model.Model):
            _use_global_cache = False

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_global_cache_policy(key._key) is False


class Test_default_global_cache_timeout_policy:
    @staticmethod
    def test_key_is_None():
        assert context_module._default_global_cache_timeout_policy(None) is None

    @staticmethod
    def test_no_model_class():
        key = mock.Mock(kind="nokind", spec=("kind",))
        assert context_module._default_global_cache_timeout_policy(key) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model():
        class ThisKind(model.Model):
            pass

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_global_cache_timeout_policy(key._key) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model_defines_policy():
        class ThisKind(model.Model):
            @classmethod
            def _global_cache_timeout(cls, key):
                return 13

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_global_cache_timeout_policy(key._key) == 13

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_model_defines_policy_as_int():
        class ThisKind(model.Model):
            _global_cache_timeout = 12

        key = key_module.Key("ThisKind", 0)
        assert context_module._default_global_cache_timeout_policy(key._key) == 12
