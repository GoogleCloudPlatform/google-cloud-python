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

from unittest import mock

import grpc
import pytest
from google.api_core import client_info
from google.api_core import exceptions as core_exceptions
from google.cloud.datastore import entity, helpers
from google.cloud.datastore import key as ds_key_module
from google.cloud.datastore_v1.types import datastore as datastore_pb2
from google.cloud.datastore_v1.types import entity as entity_pb2

from google.cloud.ndb import __version__, _batch, _cache, _options, model, tasklets
from google.cloud.ndb import _datastore_api as _api
from google.cloud.ndb import context as context_module
from google.cloud.ndb import key as key_module

from . import utils


def future_result(result):
    future = tasklets.Future()
    future.set_result(result)
    return future


class TestStub:
    @staticmethod
    def test_it():
        client = mock.Mock(
            _credentials="creds",
            secure=True,
            host="thehost",
            stub=object(),
            spec=("_credentials", "secure", "host", "stub"),
            client_info=client_info.ClientInfo(
                user_agent="google-cloud-ndb/{}".format(__version__)
            ),
        )
        context = context_module.Context(client)
        with context.use():
            assert _api.stub() is client.stub


class Test_make_call:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api._retry")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_defaults(stub, _retry):
        api = stub.return_value
        future = tasklets.Future()
        api.foo.future.return_value = future
        _retry.retry_async.return_value = mock.Mock(return_value=future)
        future.set_result("bar")

        request = object()
        assert _api.make_call("foo", request).result() == "bar"
        _retry.retry_async.assert_called_once()
        tasklet = _retry.retry_async.call_args[0][0]
        assert tasklet().result() == "bar"
        retries = _retry.retry_async.call_args[1]["retries"]
        assert retries is _retry._DEFAULT_RETRIES

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api._retry")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_explicit_retries(stub, _retry):
        api = stub.return_value
        future = tasklets.Future()
        api.foo.future.return_value = future
        _retry.retry_async.return_value = mock.Mock(return_value=future)
        future.set_result("bar")

        request = object()
        assert _api.make_call("foo", request, retries=4).result() == "bar"
        _retry.retry_async.assert_called_once()
        tasklet = _retry.retry_async.call_args[0][0]
        assert tasklet().result() == "bar"
        retries = _retry.retry_async.call_args[1]["retries"]
        assert retries == 4

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api._retry")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_no_retries(stub, _retry):
        api = stub.return_value
        future = tasklets.Future()
        api.foo.future.return_value = future
        _retry.retry_async.return_value = mock.Mock(return_value=future)
        future.set_result("bar")

        request = object()
        assert _api.make_call("foo", request, retries=0).result() == "bar"
        _retry.retry_async.assert_not_called()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api._retry")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_explicit_timeout(stub, _retry):
        api = stub.return_value
        future = tasklets.Future()
        api.foo.future.return_value = future
        _retry.retry_async.return_value = mock.Mock(return_value=future)
        future.set_result("bar")

        request = object()
        metadata = object()
        call = _api.make_call("foo", request, retries=0, timeout=20, metadata=metadata)
        assert call.result() == "bar"
        api.foo.future.assert_called_once_with(request, timeout=20, metadata=metadata)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_grpc_error(stub):
        api = stub.return_value
        future = tasklets.Future()
        api.foo.future.return_value = future

        class DummyError(grpc.Call, Exception):
            def code(self):
                return grpc.StatusCode.UNAVAILABLE

            def details(self):
                return "Where is the devil in?"

        try:
            raise DummyError("Have to raise in order to get traceback")
        except Exception as error:
            future.set_exception(error)

        request = object()
        with pytest.raises(core_exceptions.ServiceUnavailable):
            _api.make_call("foo", request, retries=0).result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_other_error(stub):
        api = stub.return_value
        future = tasklets.Future()
        api.foo.future.return_value = future

        class DummyException(Exception):
            pass

        try:
            raise DummyException("Have to raise in order to get traceback")
        except Exception as error:
            future.set_exception(error)

        request = object()
        with pytest.raises(DummyException):
            _api.make_call("foo", request, retries=0).result()


def _mock_key(key_str):
    key = mock.Mock(kind="SomeKind", spec=("to_protobuf", "kind"))
    key.to_protobuf.return_value = protobuf = mock.Mock(
        _pb=mock.Mock(spec=("SerializeToString",))
    )
    protobuf._pb.SerializeToString.return_value = key_str
    return key


class Test_lookup:
    @staticmethod
    def test_it(context):
        eventloop = mock.Mock(spec=("add_idle", "run"))
        with context.new(eventloop=eventloop).use() as context:
            _api.lookup(_mock_key("foo"), _options.ReadOptions())
            _api.lookup(_mock_key("foo"), _options.ReadOptions())
            _api.lookup(_mock_key("bar"), _options.ReadOptions())

            batch = context.batches[_api._LookupBatch][()]
            assert len(batch.todo["foo"]) == 2
            assert len(batch.todo["bar"]) == 1
            assert context.eventloop.add_idle.call_count == 1

    @staticmethod
    def test_it_with_options(context):
        eventloop = mock.Mock(spec=("add_idle", "run"))
        with context.new(eventloop=eventloop).use() as context:
            _api.lookup(_mock_key("foo"), _options.ReadOptions())
            _api.lookup(
                _mock_key("foo"),
                _options.ReadOptions(read_consistency=_api.EVENTUAL),
            )
            _api.lookup(_mock_key("bar"), _options.ReadOptions())

            batches = context.batches[_api._LookupBatch]
            batch1 = batches[()]
            assert len(batch1.todo["foo"]) == 1
            assert len(batch1.todo["bar"]) == 1

            batch2 = batches[(("read_consistency", _api.EVENTUAL),)]
            assert len(batch2.todo) == 1
            assert len(batch2.todo["foo"]) == 1

            add_idle = context.eventloop.add_idle
            assert add_idle.call_count == 2

    @staticmethod
    def test_it_with_transaction(context):
        eventloop = mock.Mock(spec=("add_idle", "run"))
        new_context = context.new(eventloop=eventloop, transaction=b"tx123")
        with new_context.use():
            new_context._use_global_cache = mock.Mock(
                side_effect=Exception("Shouldn't call _use_global_cache")
            )
            _api.lookup(_mock_key("foo"), _options.ReadOptions())
            _api.lookup(_mock_key("foo"), _options.ReadOptions())
            _api.lookup(_mock_key("bar"), _options.ReadOptions())

            batch = new_context.batches[_api._LookupBatch][(("transaction", b"tx123"),)]
            assert len(batch.todo["foo"]) == 2
            assert len(batch.todo["bar"]) == 1
            assert new_context.eventloop.add_idle.call_count == 1

    @staticmethod
    def test_it_no_global_cache_or_datastore(in_context):
        with pytest.raises(TypeError):
            _api.lookup(
                _mock_key("foo"), _options.ReadOptions(use_datastore=False)
            ).result()


class Test_lookup_WithGlobalCache:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._LookupBatch")
    def test_cache_miss(_LookupBatch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        entity = SomeKind(key=key)
        entity_pb = model._entity_to_protobuf(entity)
        cache_value = entity_pb._pb.SerializeToString()

        batch = _LookupBatch.return_value
        batch.add.return_value = future_result(entity_pb)

        future = _api.lookup(key._key, _options.ReadOptions())
        assert future.result() == entity_pb

        assert global_cache.get([cache_key]) == [cache_value]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._LookupBatch")
    def test_cache_miss_followed_by_lock_acquisition_failure(
        _LookupBatch, global_cache
    ):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        entity = SomeKind(key=key)
        entity_pb = model._entity_to_protobuf(entity)

        batch = _LookupBatch.return_value
        batch.add.return_value = future_result(entity_pb)

        global_cache.set_if_not_exists = mock.Mock(
            return_value=future_result({cache_key: False})
        )

        future = _api.lookup(key._key, _options.ReadOptions())
        assert future.result() == entity_pb

        assert global_cache.get([cache_key]) == [None]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._LookupBatch")
    def test_cache_miss_no_datastore(_LookupBatch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        batch = _LookupBatch.return_value
        batch.add.side_effect = Exception("Shouldn't use Datastore")

        future = _api.lookup(key._key, _options.ReadOptions(use_datastore=False))
        assert future.result() is _api._NOT_FOUND

        assert global_cache.get([cache_key]) == [None]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._LookupBatch")
    def test_cache_hit(_LookupBatch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        entity = SomeKind(key=key)
        entity_pb = model._entity_to_protobuf(entity)
        cache_value = entity_pb._pb.SerializeToString()

        global_cache.set({cache_key: cache_value})

        batch = _LookupBatch.return_value
        batch.add.side_effect = Exception("Shouldn't get called.")

        future = _api.lookup(key._key, _options.ReadOptions())
        assert future.result() == entity_pb

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._LookupBatch")
    def test_cache_locked(_LookupBatch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        entity = SomeKind(key=key)
        entity_pb = model._entity_to_protobuf(entity)

        global_cache.set({cache_key: _cache._LOCKED_FOR_READ})

        batch = _LookupBatch.return_value
        batch.add.return_value = future_result(entity_pb)

        future = _api.lookup(key._key, _options.ReadOptions())
        assert future.result() == entity_pb

        assert global_cache.get([cache_key]) == [_cache._LOCKED_FOR_READ]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._LookupBatch")
    def test_cache_not_found(_LookupBatch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        batch = _LookupBatch.return_value
        batch.add.return_value = future_result(_api._NOT_FOUND)

        future = _api.lookup(key._key, _options.ReadOptions())
        assert future.result() is _api._NOT_FOUND

        assert global_cache.get([cache_key])[0].startswith(_cache._LOCKED_FOR_READ)
        assert len(global_cache._watch_keys) == 0


class Test_LookupBatch:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api.entity_pb2")
    @mock.patch("google.cloud.ndb._datastore_api._datastore_lookup")
    def test_idle_callback(_datastore_lookup, entity_pb2, context):
        class MockKeyPb:
            def __init__(self, key=None, parent=None):
                self.key = key
                self.parent = parent

            def ParseFromString(self, key):
                self.key = key
                self.parent.key = key

        class MockKey:
            def __init__(self, key=None):
                self.key = key
                self._pb = MockKeyPb(key, self)

        rpc = tasklets.Future("_datastore_lookup")
        _datastore_lookup.return_value = rpc

        entity_pb2.Key = MockKey
        eventloop = mock.Mock(spec=("queue_rpc", "run"))
        with context.new(eventloop=eventloop).use() as context:
            batch = _api._LookupBatch(_options.ReadOptions())
            batch.lookup_callback = mock.Mock()
            batch.todo.update({"foo": ["one", "two"], "bar": ["three"]})
            batch.idle_callback()

            called_with = _datastore_lookup.call_args[0]
            called_with_keys = set((mock_key.key for mock_key in called_with[0]))
            assert called_with_keys == set(["foo", "bar"])
            called_with_options = called_with[1]
            assert called_with_options == datastore_pb2.ReadOptions()

            rpc.set_result(None)
            batch.lookup_callback.assert_called_once_with(rpc)

    @staticmethod
    def test_lookup_callback_exception():
        future1, future2, future3 = (tasklets.Future() for _ in range(3))
        batch = _api._LookupBatch(_options.ReadOptions())
        batch.todo.update({"foo": [future1, future2], "bar": [future3]})
        error = Exception("Spurious error.")

        rpc = tasklets.Future()
        rpc.set_exception(error)
        batch.lookup_callback(rpc)

        assert future1.exception() is error
        assert future2.exception() is error

    @staticmethod
    def test_found():
        def key_pb(key):
            mock_key = mock.Mock(_pb=mock.Mock(spec=("SerializeToString",)))
            mock_key._pb.SerializeToString.return_value = key
            return mock_key

        future1, future2, future3 = (tasklets.Future() for _ in range(3))
        batch = _api._LookupBatch(_options.ReadOptions())
        batch.todo.update({"foo": [future1, future2], "bar": [future3]})

        entity1 = mock.Mock(key=key_pb("foo"), spec=("key",))
        entity2 = mock.Mock(key=key_pb("bar"), spec=("key",))
        response = mock.Mock(
            found=[
                mock.Mock(entity=entity1, spec=("entity",)),
                mock.Mock(entity=entity2, spec=("entity",)),
            ],
            missing=[],
            deferred=[],
            spec=("found", "missing", "deferred"),
        )

        rpc = tasklets.Future()
        rpc.set_result(response)
        batch.lookup_callback(rpc)

        assert future1.result() is entity1
        assert future2.result() is entity1
        assert future3.result() is entity2

    @staticmethod
    def test_missing():
        def key_pb(key):
            mock_key = mock.Mock(_pb=mock.Mock(spec=("SerializeToString",)))
            mock_key._pb.SerializeToString.return_value = key
            return mock_key

        future1, future2, future3 = (tasklets.Future() for _ in range(3))
        batch = _api._LookupBatch(_options.ReadOptions())
        batch.todo.update({"foo": [future1, future2], "bar": [future3]})

        entity1 = mock.Mock(key=key_pb("foo"), spec=("key",))
        entity2 = mock.Mock(key=key_pb("bar"), spec=("key",))
        response = mock.Mock(
            missing=[
                mock.Mock(entity=entity1, spec=("entity",)),
                mock.Mock(entity=entity2, spec=("entity",)),
            ],
            found=[],
            deferred=[],
            spec=("found", "missing", "deferred"),
        )

        rpc = tasklets.Future()
        rpc.set_result(response)
        batch.lookup_callback(rpc)

        assert future1.result() is _api._NOT_FOUND
        assert future2.result() is _api._NOT_FOUND
        assert future3.result() is _api._NOT_FOUND

    @staticmethod
    def test_deferred(context):
        def key_pb(key):
            mock_key = mock.Mock(_pb=mock.Mock(spec=("SerializeToString",)))
            mock_key._pb.SerializeToString.return_value = key
            return mock_key

        eventloop = mock.Mock(spec=("add_idle", "run"))
        with context.new(eventloop=eventloop).use() as context:
            future1, future2, future3 = (tasklets.Future() for _ in range(3))
            batch = _api._LookupBatch(_options.ReadOptions())
            batch.todo.update({"foo": [future1, future2], "bar": [future3]})

            response = mock.Mock(
                missing=[],
                found=[],
                deferred=[key_pb("foo"), key_pb("bar")],
                spec=("found", "missing", "deferred"),
            )

            rpc = tasklets.Future()
            rpc.set_result(response)
            batch.lookup_callback(rpc)

            assert future1.running()
            assert future2.running()
            assert future3.running()

            next_batch = context.batches[_api._LookupBatch][()]
            assert next_batch.todo == batch.todo and next_batch is not batch
            assert context.eventloop.add_idle.call_count == 1

    @staticmethod
    def test_found_missing_deferred(context):
        def key_pb(key):
            mock_key = mock.Mock(_pb=mock.Mock(spec=("SerializeToString",)))
            mock_key._pb.SerializeToString.return_value = key
            return mock_key

        eventloop = mock.Mock(spec=("add_idle", "run"))
        with context.new(eventloop=eventloop).use() as context:
            future1, future2, future3 = (tasklets.Future() for _ in range(3))
            batch = _api._LookupBatch(_options.ReadOptions())
            batch.todo.update({"foo": [future1], "bar": [future2], "baz": [future3]})

            entity1 = mock.Mock(key=key_pb("foo"), spec=("key",))
            entity2 = mock.Mock(key=key_pb("bar"), spec=("key",))
            response = mock.Mock(
                found=[mock.Mock(entity=entity1, spec=("entity",))],
                missing=[mock.Mock(entity=entity2, spec=("entity",))],
                deferred=[key_pb("baz")],
                spec=("found", "missing", "deferred"),
            )

            rpc = tasklets.Future()
            rpc.set_result(response)
            batch.lookup_callback(rpc)

            assert future1.result() is entity1
            assert future2.result() is _api._NOT_FOUND
            assert future3.running()

            next_batch = context.batches[_api._LookupBatch][()]
            assert next_batch.todo == {"baz": [future3]}
            assert context.eventloop.add_idle.call_count == 1


@mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
def test__datastore_lookup(datastore_pb2, context):
    client = mock.Mock(
        project="theproject",
        database="testdb",
        stub=mock.Mock(spec=("lookup",)),
        spec=("project", "database", "stub"),
    )
    with context.new(client=client).use() as context:
        client.stub.lookup = lookup = mock.Mock(spec=("future",))
        future = tasklets.Future()
        future.set_result("response")
        lookup.future.return_value = future
        datastore_pb2.LookupRequest.return_value.project_id = "theproject"
        datastore_pb2.LookupRequest.return_value.database_id = "testdb"
        assert _api._datastore_lookup(["foo", "bar"], None).result() == "response"

        datastore_pb2.LookupRequest.assert_called_once_with(
            project_id="theproject",
            database_id="testdb",
            keys=["foo", "bar"],
            read_options=None,
        )
        client.stub.lookup.future.assert_called_once_with(
            datastore_pb2.LookupRequest.return_value,
            timeout=_api._DEFAULT_TIMEOUT,
            metadata=(
                ("x-goog-request-params", "project_id=theproject&database_id=testdb"),
            ),
        )


class Test_get_read_options:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_no_args_no_transaction():
        assert (
            _api.get_read_options(_options.ReadOptions()) == datastore_pb2.ReadOptions()
        )

    @staticmethod
    def test_no_args_transaction(context):
        with context.new(transaction=b"txfoo").use():
            options = _api.get_read_options(_options.ReadOptions())
            assert options == datastore_pb2.ReadOptions(transaction=b"txfoo")

    @staticmethod
    def test_args_override_transaction(context):
        with context.new(transaction=b"txfoo").use():
            options = _api.get_read_options(_options.ReadOptions(transaction=b"txbar"))
            assert options == datastore_pb2.ReadOptions(transaction=b"txbar")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_eventually_consistent():
        options = _api.get_read_options(
            _options.ReadOptions(read_consistency=_api.EVENTUAL)
        )
        assert options == datastore_pb2.ReadOptions(
            read_consistency=datastore_pb2.ReadOptions.ReadConsistency.EVENTUAL
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_eventually_consistent_with_transaction():
        with pytest.raises(ValueError):
            _api.get_read_options(
                _options.ReadOptions(
                    read_consistency=_api.EVENTUAL, transaction=b"txfoo"
                )
            )


class Test_put:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    def test_no_transaction(datastore_pb2, in_context):
        class Mutation:
            def __init__(self, upsert=None):
                self.upsert = upsert

            def __eq__(self, other):
                return self.upsert == other.upsert

        def MockEntity(*path):
            key = ds_key_module.Key(*path, project="testing")
            return entity.Entity(key=key)

        datastore_pb2.Mutation = Mutation

        entity1 = MockEntity("a", "1")
        _api.put(entity1, _options.Options())

        entity2 = MockEntity("a")
        _api.put(entity2, _options.Options())

        entity3 = MockEntity("b")
        _api.put(entity3, _options.Options())

        batch = in_context.batches[_api._NonTransactionalCommitBatch][()]
        assert batch.mutations == [
            Mutation(upsert=helpers.entity_to_protobuf(entity1)),
            Mutation(upsert=helpers.entity_to_protobuf(entity2)),
            Mutation(upsert=helpers.entity_to_protobuf(entity3)),
        ]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    def test_w_transaction(datastore_pb2, in_context):
        class Mutation:
            def __init__(self, upsert=None):
                self.upsert = upsert

            def __eq__(self, other):
                return self.upsert == other.upsert

        def MockEntity(*path):
            key = ds_key_module.Key(*path, project="testing")
            return entity.Entity(key=key)

        with in_context.new(transaction=b"123").use() as context:
            datastore_pb2.Mutation = Mutation

            entity1 = MockEntity("a", "1")
            _api.put(entity1, _options.Options())

            entity2 = MockEntity("a")
            _api.put(entity2, _options.Options())

            entity3 = MockEntity("b")
            _api.put(entity3, _options.Options())

            batch = context.commit_batches[b"123"]
            assert batch.mutations == [
                Mutation(upsert=helpers.entity_to_protobuf(entity1)),
                Mutation(upsert=helpers.entity_to_protobuf(entity2)),
                Mutation(upsert=helpers.entity_to_protobuf(entity3)),
            ]
            assert batch.transaction == b"123"
            assert batch.incomplete_mutations == [
                Mutation(upsert=helpers.entity_to_protobuf(entity2)),
                Mutation(upsert=helpers.entity_to_protobuf(entity3)),
            ]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_no_datastore_or_global_cache():
        def MockEntity(*path):
            key = ds_key_module.Key(*path, project="testing")
            return entity.Entity(key=key)

        mock_entity = MockEntity("what", "ever")
        with pytest.raises(TypeError):
            _api.put(mock_entity, _options.Options(use_datastore=False)).result()


class Test_put_WithGlobalCache:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_no_key_returned(Batch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        entity = SomeKind(key=key)
        batch = Batch.return_value
        batch.put.return_value = future_result(None)

        future = _api.put(model._entity_to_ds_entity(entity), _options.Options())
        assert future.result() is None

        assert not global_cache.get([cache_key])[0]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_key_returned(Batch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        key_pb = key._key.to_protobuf()
        cache_key = _cache.global_cache_key(key._key)

        entity = SomeKind(key=key)
        batch = Batch.return_value
        batch.put.return_value = future_result(key_pb)

        future = _api.put(model._entity_to_ds_entity(entity), _options.Options())
        assert future.result() == key._key

        assert not global_cache.get([cache_key])[0]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_w_transaction(Batch, global_cache):
        class SomeKind(model.Model):
            pass

        context = context_module.get_context()
        callbacks = []
        with context.new(
            transaction=b"abc123", transaction_complete_callbacks=callbacks
        ).use():
            key = key_module.Key("SomeKind", 1)
            cache_key = _cache.global_cache_key(key._key)

            entity = SomeKind(key=key)
            batch = Batch.return_value
            batch.put.return_value = future_result(None)

            future = _api.put(model._entity_to_ds_entity(entity), _options.Options())
            assert future.result() is None

            assert cache_key in global_cache.cache  # lock
            for callback in callbacks:
                callback()

            # lock removed by callback
            assert not global_cache.get([cache_key])[0]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_no_datastore(Batch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        entity = SomeKind(key=key)
        cache_value = model._entity_to_protobuf(entity)._pb.SerializeToString()

        batch = Batch.return_value
        batch.put.return_value = future_result(None)

        future = _api.put(
            model._entity_to_ds_entity(entity),
            _options.Options(use_datastore=False),
        )
        assert future.result() is None

        assert global_cache.get([cache_key]) == [cache_value]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_no_datastore_incomplete_key(Batch, global_cache):
        class SomeKind(model.Model):
            pass

        key = key_module.Key("SomeKind", None)
        entity = SomeKind(key=key)
        future = _api.put(
            model._entity_to_ds_entity(entity),
            _options.Options(use_datastore=False),
        )
        with pytest.raises(TypeError):
            future.result()


class Test_delete:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    def test_no_transaction(datastore_pb2, in_context):
        class Mutation:
            def __init__(self, delete=None):
                self.delete = delete

            def __eq__(self, other):
                return self.delete == other.delete

        datastore_pb2.Mutation = Mutation

        key1 = key_module.Key("SomeKind", 1)._key
        key2 = key_module.Key("SomeKind", 2)._key
        key3 = key_module.Key("SomeKind", 3)._key
        _api.delete(key1, _options.Options())
        _api.delete(key2, _options.Options())
        _api.delete(key3, _options.Options())

        batch = in_context.batches[_api._NonTransactionalCommitBatch][()]
        assert batch.mutations == [
            Mutation(delete=key1.to_protobuf()),
            Mutation(delete=key2.to_protobuf()),
            Mutation(delete=key3.to_protobuf()),
        ]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    def test_w_transaction(datastore_pb2, in_context):
        class Mutation:
            def __init__(self, delete=None):
                self.delete = delete

            def __eq__(self, other):
                return self.delete == other.delete

        with in_context.new(transaction=b"tx123").use() as context:
            datastore_pb2.Mutation = Mutation

            key1 = key_module.Key("SomeKind", 1)._key
            key2 = key_module.Key("SomeKind", 2)._key
            key3 = key_module.Key("SomeKind", 3)._key
            assert _api.delete(key1, _options.Options()).result() is None
            assert _api.delete(key2, _options.Options()).result() is None
            assert _api.delete(key3, _options.Options()).result() is None

            batch = context.commit_batches[b"tx123"]
            assert batch.mutations == [
                Mutation(delete=key1.to_protobuf()),
                Mutation(delete=key2.to_protobuf()),
                Mutation(delete=key3.to_protobuf()),
            ]


class Test_delete_WithGlobalCache:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_cache_enabled(Batch, global_cache):
        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        batch = Batch.return_value
        batch.delete.return_value = future_result(None)

        future = _api.delete(key._key, _options.Options())
        assert future.result() is None

        assert not global_cache.get([cache_key])[0]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_lock_not_acquired(Batch, global_cache):
        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)
        global_cache.set({cache_key: b"foo"})

        batch = Batch.return_value
        batch.delete.return_value = future_result(None)

        with mock.patch(
            "google.cloud.ndb._datastore_api._cache.global_lock_for_write",
            return_value=future_result(None),
        ):
            future = _api.delete(key._key, _options.Options())

        assert future.result() is None
        batch.delete.assert_called_once_with(key._key)
        assert global_cache.get([cache_key]) == [b"foo"]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_w_transaction(Batch, global_cache):
        context = context_module.get_context()
        callbacks = []
        with context.new(
            transaction=b"abc123", transaction_complete_callbacks=callbacks
        ).use():
            key = key_module.Key("SomeKind", 1)
            cache_key = _cache.global_cache_key(key._key)

            batch = Batch.return_value
            batch.delete.return_value = future_result(None)

            future = _api.delete(key._key, _options.Options())
            assert future.result() is None

            assert cache_key in global_cache.cache  # lock
            for callback in callbacks:
                callback()

            # lock removed by callback
            assert not global_cache.get([cache_key])[0]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_without_datastore(Batch, global_cache):
        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)
        global_cache.set({cache_key: b"foo"})

        batch = Batch.return_value
        batch.delete.side_effect = Exception("Shouldn't use Datastore")

        future = _api.delete(key._key, _options.Options(use_datastore=False))
        assert future.result() is None

        assert global_cache.get([cache_key]) == [None]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_without_datastore_with_transaction(Batch, global_cache):
        context = context_module.get_context()
        callbacks = []

        with context.new(
            transaction=b"abc123", transaction_complete_callbacks=callbacks
        ).use():
            key = key_module.Key("SomeKind", 1)
            cache_key = _cache.global_cache_key(key._key)
            global_cache.set({cache_key: b"foo"})

            batch = Batch.return_value
            batch.delete.side_effect = Exception("Shouldn't use Datastore")

            future = _api.delete(
                key._key,
                _options.Options(use_datastore=False),
            )
            assert future.result() is None

            assert callbacks == []
            assert global_cache.get([cache_key]) == [None]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._NonTransactionalCommitBatch")
    def test_cache_disabled(Batch, global_cache):
        key = key_module.Key("SomeKind", 1)
        cache_key = _cache.global_cache_key(key._key)

        batch = Batch.return_value
        batch.delete.return_value = future_result(None)

        future = _api.delete(key._key, _options.Options(use_global_cache=False))
        assert future.result() is None

        assert global_cache.get([cache_key]) == [None]


class Test_NonTransactionalCommitBatch:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._process_commit")
    @mock.patch("google.cloud.ndb._datastore_api._datastore_commit")
    def test_idle_callback(_datastore_commit, _process_commit, context):
        eventloop = mock.Mock(spec=("queue_rpc", "run"))

        rpc = tasklets.Future("_datastore_commit")
        _datastore_commit.return_value = rpc

        with context.new(eventloop=eventloop).use() as context:
            mutation1, mutation2 = object(), object()
            batch = _api._NonTransactionalCommitBatch(_options.Options())
            batch.mutations = [mutation1, mutation2]
            batch.idle_callback()

            _datastore_commit.assert_called_once_with(
                [mutation1, mutation2], None, retries=None, timeout=None
            )
            rpc.set_result(None)
            _process_commit.assert_called_once_with(rpc, batch.futures)


@mock.patch("google.cloud.ndb._datastore_api._get_commit_batch")
def test_prepare_to_commit(get_commit_batch):
    _api.prepare_to_commit(b"123")
    get_commit_batch.assert_called_once_with(b"123", _options.Options())
    batch = get_commit_batch.return_value
    assert batch.preparing_to_commit is True


@mock.patch("google.cloud.ndb._datastore_api._get_commit_batch")
def test_commit(get_commit_batch):
    _api.commit(b"123")
    get_commit_batch.assert_called_once_with(b"123", _options.Options())
    get_commit_batch.return_value.commit.assert_called_once_with(
        retries=None, timeout=None
    )


class Test_get_commit_batch:
    @staticmethod
    def test_create_batch(in_context):
        batch = _api._get_commit_batch(b"123", _options.Options())
        assert isinstance(batch, _api._TransactionalCommitBatch)
        assert in_context.commit_batches[b"123"] is batch
        assert batch.transaction == b"123"
        assert _api._get_commit_batch(b"123", _options.Options()) is batch
        assert _api._get_commit_batch(b"234", _options.Options()) is not batch

    @staticmethod
    def test_bad_option():
        with pytest.raises(NotImplementedError):
            _api._get_commit_batch(b"123", _options.Options(retries=5))


class Test__TransactionalCommitBatch:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_idle_callback_nothing_to_do():
        batch = _api._TransactionalCommitBatch(b"123", _options.Options())
        batch.idle_callback()
        assert not batch.allocating_ids

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._datastore_allocate_ids")
    def test_idle_callback_success(datastore_allocate_ids, in_context):
        def Mutation():
            path = [entity_pb2.Key.PathElement(kind="SomeKind")]
            return datastore_pb2.Mutation(
                upsert=entity_pb2.Entity(key=entity_pb2.Key(path=path))
            )

        mutation1, mutation2 = Mutation(), Mutation()
        batch = _api._TransactionalCommitBatch(b"123", _options.Options())
        batch.incomplete_mutations = [mutation1, mutation2]
        future1, future2 = tasklets.Future(), tasklets.Future()
        batch.incomplete_futures = [future1, future2]

        rpc = tasklets.Future("_datastore_allocate_ids")
        datastore_allocate_ids.return_value = rpc

        eventloop = mock.Mock(spec=("queue_rpc", "run"))
        with in_context.new(eventloop=eventloop).use():
            batch.idle_callback()

            rpc.set_result(
                mock.Mock(
                    keys=[
                        entity_pb2.Key(
                            path=[entity_pb2.Key.PathElement(kind="SomeKind", id=1)]
                        ),
                        entity_pb2.Key(
                            path=[entity_pb2.Key.PathElement(kind="SomeKind", id=2)]
                        ),
                    ]
                )
            )

            allocating_ids = batch.allocating_ids[0]
            assert future1.result().path[0].id == 1
            assert mutation1.upsert.key.path[0].id == 1
            assert future2.result().path[0].id == 2
            assert mutation2.upsert.key.path[0].id == 2
            assert allocating_ids.result() is None

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._datastore_allocate_ids")
    def test_idle_callback_failure(datastore_allocate_ids, in_context):
        def Mutation():
            path = [entity_pb2.Key.PathElement(kind="SomeKind")]
            return datastore_pb2.Mutation(
                upsert=entity_pb2.Entity(key=entity_pb2.Key(path=path))
            )

        mutation1, mutation2 = Mutation(), Mutation()
        batch = _api._TransactionalCommitBatch(b"123", _options.Options())
        batch.incomplete_mutations = [mutation1, mutation2]
        future1, future2 = tasklets.Future(), tasklets.Future()
        batch.incomplete_futures = [future1, future2]

        rpc = tasklets.Future("_datastore_allocate_ids")
        datastore_allocate_ids.return_value = rpc

        eventloop = mock.Mock(spec=("queue_rpc", "run"))
        with in_context.new(eventloop=eventloop).use():
            batch.idle_callback()

            error = Exception("Spurious error")
            rpc.set_exception(error)

            allocating_ids = batch.allocating_ids[0]
            assert future1.exception() is error
            assert future2.exception() is error
            assert allocating_ids.result() is None

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._process_commit")
    @mock.patch("google.cloud.ndb._datastore_api._datastore_commit")
    def test_commit(datastore_commit, process_commit, in_context):
        batch = _api._TransactionalCommitBatch(b"123", _options.Options())
        batch.futures = object()
        batch.mutations = object()
        batch.transaction = b"abc"

        rpc = tasklets.Future("_datastore_commit")
        datastore_commit.return_value = rpc

        eventloop = mock.Mock(spec=("queue_rpc", "run", "call_soon"))
        eventloop.call_soon = lambda f, *args, **kwargs: f(*args, **kwargs)
        with in_context.new(eventloop=eventloop).use():
            future = batch.commit()

            datastore_commit.assert_called_once_with(
                batch.mutations, transaction=b"abc", retries=None, timeout=None
            )
            rpc.set_result(None)
            process_commit.assert_called_once_with(rpc, batch.futures)

        assert future.result() is None

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._process_commit")
    @mock.patch("google.cloud.ndb._datastore_api._datastore_commit")
    def test_commit_error(datastore_commit, process_commit, in_context):
        batch = _api._TransactionalCommitBatch(b"123", _options.Options())
        batch.futures = object()
        batch.mutations = object()
        batch.transaction = b"abc"

        rpc = tasklets.Future("_datastore_commit")
        datastore_commit.return_value = rpc

        eventloop = mock.Mock(spec=("queue_rpc", "run", "call_soon"))
        eventloop.call_soon = lambda f, *args, **kwargs: f(*args, **kwargs)
        with in_context.new(eventloop=eventloop).use():
            future = batch.commit()

            datastore_commit.assert_called_once_with(
                batch.mutations, transaction=b"abc", retries=None, timeout=None
            )

            error = Exception("Spurious error")
            rpc.set_exception(error)

            process_commit.assert_called_once_with(rpc, batch.futures)

        assert future.exception() is error

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._process_commit")
    @mock.patch("google.cloud.ndb._datastore_api._datastore_commit")
    def test_commit_allocating_ids(datastore_commit, process_commit, in_context):
        batch = _api._TransactionalCommitBatch(b"123", _options.Options())
        batch.futures = object()
        batch.mutations = object()
        batch.transaction = b"abc"

        allocated_ids = tasklets.Future("Already allocated ids")
        allocated_ids.set_result(None)
        batch.allocating_ids.append(allocated_ids)

        allocating_ids = tasklets.Future("AllocateIds")
        batch.allocating_ids.append(allocating_ids)

        rpc = tasklets.Future("_datastore_commit")
        datastore_commit.return_value = rpc

        eventloop = mock.Mock(spec=("queue_rpc", "run", "call_soon"))
        eventloop.call_soon = lambda f, *args, **kwargs: f(*args, **kwargs)
        with in_context.new(eventloop=eventloop).use():
            future = batch.commit()

            datastore_commit.assert_not_called()
            process_commit.assert_not_called()

            allocating_ids.set_result(None)
            datastore_commit.assert_called_once_with(
                batch.mutations, transaction=b"abc", retries=None, timeout=None
            )

            rpc.set_result(None)
            process_commit.assert_called_once_with(rpc, batch.futures)

        assert future.result() is None


class Test_process_commit:
    @staticmethod
    def test_exception():
        error = Exception("Spurious error.")
        rpc = tasklets.Future()
        rpc.set_exception(error)

        future1, future2 = tasklets.Future(), tasklets.Future()
        _api._process_commit(rpc, [future1, future2])
        assert future1.exception() is error
        assert future2.exception() is error

    @staticmethod
    def test_exception_some_already_done():
        error = Exception("Spurious error.")
        rpc = tasklets.Future()
        rpc.set_exception(error)

        future1, future2 = tasklets.Future(), tasklets.Future()
        future2.set_result("hi mom")
        _api._process_commit(rpc, [future1, future2])
        assert future1.exception() is error
        assert future2.result() == "hi mom"

    @staticmethod
    def test_success():
        key1 = mock.Mock(path=["one", "two"], spec=("path",))
        mutation1 = mock.Mock(key=key1, spec=("key",))
        key2 = mock.Mock(path=[], spec=("path",))
        mutation2 = mock.Mock(key=key2, spec=("key",))
        response = mock.Mock(
            mutation_results=(mutation1, mutation2), spec=("mutation_results",)
        )

        rpc = tasklets.Future()
        rpc.set_result(response)

        future1, future2 = tasklets.Future(), tasklets.Future()
        _api._process_commit(rpc, [future1, future2])
        assert future1.result() is key1
        assert future2.result() is None

    @staticmethod
    def test_success_some_already_done():
        key1 = mock.Mock(path=["one", "two"], spec=("path",))
        mutation1 = mock.Mock(key=key1, spec=("key",))
        key2 = mock.Mock(path=[], spec=("path",))
        mutation2 = mock.Mock(key=key2, spec=("key",))
        response = mock.Mock(
            mutation_results=(mutation1, mutation2), spec=("mutation_results",)
        )

        rpc = tasklets.Future()
        rpc.set_result(response)

        future1, future2 = tasklets.Future(), tasklets.Future()
        future2.set_result(None)
        _api._process_commit(rpc, [future1, future2])
        assert future1.result() is key1
        assert future2.result() is None


class Test_datastore_commit:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_wo_transaction(stub, datastore_pb2):
        mutations = object()
        api = stub.return_value
        future = tasklets.Future()
        future.set_result("response")
        api.commit.future.return_value = future
        assert _api._datastore_commit(mutations, None).result() == "response"

        datastore_pb2.CommitRequest.assert_called_once_with(
            project_id="testing",
            database_id=None,
            mode=datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL,
            mutations=mutations,
            transaction=None,
        )

        request = datastore_pb2.CommitRequest.return_value
        api.commit.future.assert_called_once_with(
            request, metadata=mock.ANY, timeout=mock.ANY
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_w_transaction(stub, datastore_pb2):
        mutations = object()
        api = stub.return_value
        future = tasklets.Future()
        future.set_result("response")
        api.commit.future.return_value = future
        assert _api._datastore_commit(mutations, b"tx123").result() == "response"

        datastore_pb2.CommitRequest.assert_called_once_with(
            project_id="testing",
            database_id=None,
            mode=datastore_pb2.CommitRequest.Mode.TRANSACTIONAL,
            mutations=mutations,
            transaction=b"tx123",
        )

        request = datastore_pb2.CommitRequest.return_value
        api.commit.future.assert_called_once_with(
            request, metadata=mock.ANY, timeout=mock.ANY
        )


@pytest.mark.usefixtures("in_context")
def test_allocate():
    options = _options.Options()
    future = _api.allocate(["one", "two"], options)
    batch = _batch.get_batch(_api._AllocateIdsBatch, options)
    assert batch.keys == ["one", "two"]
    assert batch.futures == future._dependencies


@pytest.mark.usefixtures("in_context")
class Test_AllocateIdsBatch:
    @staticmethod
    def test_constructor():
        options = _options.Options()
        batch = _api._AllocateIdsBatch(options)
        assert batch.options is options
        assert batch.keys == []
        assert batch.futures == []

    @staticmethod
    def test_add():
        options = _options.Options()
        batch = _api._AllocateIdsBatch(options)
        futures = batch.add(["key1", "key2"])
        assert batch.keys == ["key1", "key2"]
        assert batch.futures == futures

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._datastore_allocate_ids")
    def test_idle_callback(_datastore_allocate_ids):
        options = _options.Options()
        batch = _api._AllocateIdsBatch(options)
        batch.add(
            [
                key_module.Key("SomeKind", None)._key,
                key_module.Key("SomeKind", None)._key,
            ]
        )
        key_pbs = [key.to_protobuf() for key in batch.keys]
        batch.idle_callback()
        _datastore_allocate_ids.assert_called_once_with(
            key_pbs, retries=None, timeout=None
        )
        rpc = _datastore_allocate_ids.return_value
        rpc.add_done_callback.assert_called_once_with(batch.allocate_ids_callback)

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._datastore_allocate_ids")
    def test_allocate_ids_callback(_datastore_allocate_ids):
        options = _options.Options()
        batch = _api._AllocateIdsBatch(options)
        batch.futures = futures = [tasklets.Future(), tasklets.Future()]
        rpc = utils.future_result(mock.Mock(keys=["key1", "key2"], spec=("key",)))
        batch.allocate_ids_callback(rpc)
        results = [future.result() for future in futures]
        assert results == ["key1", "key2"]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api._datastore_allocate_ids")
    def test_allocate_ids_callback_w_exception(_datastore_allocate_ids):
        options = _options.Options()
        batch = _api._AllocateIdsBatch(options)
        batch.futures = futures = [tasklets.Future(), tasklets.Future()]
        error = Exception("spurious error")
        rpc = tasklets.Future()
        rpc.set_exception(error)
        batch.allocate_ids_callback(rpc)
        assert [future.exception() for future in futures] == [error, error]


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
@mock.patch("google.cloud.ndb._datastore_api.stub")
def test__datastore_allocate_ids(stub, datastore_pb2):
    keys = object()
    api = stub.return_value
    future = tasklets.Future()
    future.set_result("response")
    api.allocate_ids.future.return_value = future
    assert _api._datastore_allocate_ids(keys).result() == "response"

    datastore_pb2.AllocateIdsRequest.assert_called_once_with(
        project_id="testing", database_id=None, keys=keys
    )

    request = datastore_pb2.AllocateIdsRequest.return_value
    api.allocate_ids.future.assert_called_once_with(
        request, metadata=mock.ANY, timeout=mock.ANY
    )


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_api._datastore_begin_transaction")
def test_begin_transaction(_datastore_begin_transaction):
    rpc = tasklets.Future("BeginTransaction()")
    _datastore_begin_transaction.return_value = rpc

    future = _api.begin_transaction("read only")
    _datastore_begin_transaction.assert_called_once_with(
        "read only", retries=None, timeout=None
    )
    rpc.set_result(mock.Mock(transaction=b"tx123", spec=("transaction")))

    assert future.result() == b"tx123"


class Test_datastore_begin_transaction:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_read_only(stub, datastore_pb2):
        api = stub.return_value
        future = tasklets.Future()
        future.set_result("response")
        api.begin_transaction.future.return_value = future
        assert _api._datastore_begin_transaction(True).result() == "response"

        datastore_pb2.TransactionOptions.assert_called_once_with(
            read_only=datastore_pb2.TransactionOptions.ReadOnly()
        )

        transaction_options = datastore_pb2.TransactionOptions.return_value
        datastore_pb2.BeginTransactionRequest.assert_called_once_with(
            project_id="testing",
            database_id=None,
            transaction_options=transaction_options,
        )

        request = datastore_pb2.BeginTransactionRequest.return_value
        api.begin_transaction.future.assert_called_once_with(
            request, metadata=mock.ANY, timeout=mock.ANY
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
    @mock.patch("google.cloud.ndb._datastore_api.stub")
    def test_read_write(stub, datastore_pb2):
        api = stub.return_value
        future = tasklets.Future()
        future.set_result("response")
        api.begin_transaction.future.return_value = future
        assert _api._datastore_begin_transaction(False).result() == "response"

        datastore_pb2.TransactionOptions.assert_called_once_with(
            read_write=datastore_pb2.TransactionOptions.ReadWrite()
        )

        transaction_options = datastore_pb2.TransactionOptions.return_value
        datastore_pb2.BeginTransactionRequest.assert_called_once_with(
            project_id="testing",
            database_id=None,
            transaction_options=transaction_options,
        )

        request = datastore_pb2.BeginTransactionRequest.return_value
        api.begin_transaction.future.assert_called_once_with(
            request, metadata=mock.ANY, timeout=mock.ANY
        )


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_api._datastore_rollback")
def test_rollback(_datastore_rollback):
    rpc = tasklets.Future("Rollback()")
    _datastore_rollback.return_value = rpc
    future = _api.rollback(b"tx123")

    _datastore_rollback.assert_called_once_with(b"tx123", retries=None, timeout=None)
    rpc.set_result(None)

    assert future.result() is None


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_api.datastore_pb2")
@mock.patch("google.cloud.ndb._datastore_api.stub")
def test__datastore_rollback(stub, datastore_pb2):
    api = stub.return_value
    future = tasklets.Future()
    future.set_result("response")
    api.rollback.future.return_value = future
    assert _api._datastore_rollback(b"tx123").result() == "response"

    datastore_pb2.RollbackRequest.assert_called_once_with(
        project_id="testing", database_id=None, transaction=b"tx123"
    )

    request = datastore_pb2.RollbackRequest.return_value
    api.rollback.future.assert_called_once_with(
        request, metadata=mock.ANY, timeout=mock.ANY
    )


def test__complete():
    class MockElement:
        def __init__(self, id=None, name=None):
            self.id = id
            self.name = name

    assert not _api._complete(mock.Mock(path=[]))
    assert not _api._complete(mock.Mock(path=[MockElement()]))
    assert _api._complete(mock.Mock(path=[MockElement(id=1)]))
    assert _api._complete(mock.Mock(path=[MockElement(name="himom")]))


@pytest.mark.parametrize(
    "project_id,database_id,expected",
    [
        ("a", "b", "project_id=a&database_id=b"),
        ("a", "", "project_id=a"),
        ("", "b", "database_id=b"),
    ],
)
def test__add_routing_info(project_id, database_id, expected):
    expected_new_metadata = ("x-goog-request-params", expected)
    request = datastore_pb2.LookupRequest(
        project_id=project_id, database_id=database_id
    )
    assert _api._add_routing_info((), request) == (expected_new_metadata,)
    assert _api._add_routing_info(("already=there",), request) == (
        "already=there",
        expected_new_metadata,
    )


def test__add_routing_info_no_request_info():
    request = datastore_pb2.LookupRequest()
    assert _api._add_routing_info((), request) == ()
