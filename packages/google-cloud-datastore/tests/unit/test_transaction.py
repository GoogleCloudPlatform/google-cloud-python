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

import mock
import pytest

from google.cloud.datastore.helpers import set_database_id_to_request


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_ctor_defaults(database_id):
    from google.cloud.datastore.transaction import Transaction

    project = "PROJECT"
    client = _Client(project, database=database_id)

    xact = _make_transaction(client)

    assert xact.project == project
    assert xact.database == database_id
    assert xact._client is client
    assert xact.id is None
    assert xact._status == Transaction._INITIAL
    assert xact._mutations == []
    assert len(xact._partial_key_entities) == 0


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_constructor_read_only(database_id):
    project = "PROJECT"
    id_ = 850302
    ds_api = _make_datastore_api(xact=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    options = _make_options(read_only=True)

    xact = _make_transaction(client, read_only=True)

    assert xact._options == options
    assert xact.database == database_id


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_constructor_w_read_time(database_id):
    from datetime import datetime

    project = "PROJECT"
    id_ = 850302
    read_time = datetime.utcfromtimestamp(1641058200.123456)
    ds_api = _make_datastore_api(xact=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    options = _make_options(read_only=True, read_time=read_time)

    xact = _make_transaction(client, read_only=True, read_time=read_time)

    assert xact._options == options
    assert xact.database == database_id


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_constructor_read_write_w_read_time(database_id):
    from datetime import datetime

    project = "PROJECT"
    id_ = 850302
    read_time = datetime.utcfromtimestamp(1641058200.123456)
    ds_api = _make_datastore_api(xact=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)

    with pytest.raises(ValueError):
        _make_transaction(client, read_only=False, read_time=read_time)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_constructor_begin_later(database_id):
    from google.cloud.datastore.transaction import Transaction

    project = "PROJECT"
    client = _Client(project, database=database_id)
    expected_id = b"1234"

    xact = _make_transaction(client, begin_later=True)
    assert xact._status == Transaction._INITIAL
    assert xact.id is None

    xact._begin_with_id(expected_id)
    assert xact._status == Transaction._IN_PROGRESS
    assert xact.id == expected_id

    # calling a second time should raise exeception
    with pytest.raises(ValueError):
        xact._begin_with_id(expected_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_current(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    id_ = 678
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, database=database_id, datastore_api=ds_api)
    xact1 = _make_transaction(client)
    xact2 = _make_transaction(client)
    assert xact1.current() is None
    assert xact2.current() is None

    with xact1:
        assert xact1.current() is xact1
        assert xact2.current() is xact1

        with _NoCommitBatch(client):
            assert xact1.current() is None
            assert xact2.current() is None

        with xact2:
            assert xact1.current() is xact2
            assert xact2.current() is xact2

            with _NoCommitBatch(client):
                assert xact1.current() is None
                assert xact2.current() is None

        assert xact1.current() is xact1
        assert xact2.current() is xact1

    assert xact1.current() is None
    assert xact2.current() is None

    begin_txn = ds_api.begin_transaction
    assert begin_txn.call_count == 2
    expected_request = _make_begin_request(project, database=database_id)
    begin_txn.assert_called_with(request=expected_request)

    commit_method = ds_api.commit
    assert commit_method.call_count == 2
    mode = datastore_pb2.CommitRequest.Mode.TRANSACTIONAL
    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": [],
        "transaction": id_,
    }
    set_database_id_to_request(expected_request, database_id)

    commit_method.assert_called_with(request=expected_request)

    ds_api.rollback.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_begin(database_id):
    project = "PROJECT"
    id_ = 889
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, database=database_id, datastore_api=ds_api)
    xact = _make_transaction(client)

    xact.begin()

    assert xact.id == id_

    expected_request = _make_begin_request(project, database=database_id)

    ds_api.begin_transaction.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_begin_w_readonly(database_id):
    project = "PROJECT"
    id_ = 889
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client, read_only=True)

    xact.begin()

    assert xact.id == id_

    expected_request = _make_begin_request(
        project, read_only=True, database=database_id
    )
    ds_api.begin_transaction.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_begin_w_read_time(database_id):
    from datetime import datetime

    project = "PROJECT"
    id_ = 889
    read_time = datetime.utcfromtimestamp(1641058200.123456)
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client, read_only=True, read_time=read_time)

    xact.begin()

    assert xact.id == id_

    expected_request = _make_begin_request(
        project, read_only=True, read_time=read_time, database=database_id
    )
    ds_api.begin_transaction.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_begin_w_retry_w_timeout(database_id):
    project = "PROJECT"
    id_ = 889
    retry = mock.Mock()
    timeout = 100000

    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)

    xact.begin(retry=retry, timeout=timeout)

    assert xact.id == id_

    expected_request = _make_begin_request(project, database=database_id)
    ds_api.begin_transaction.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_begin_tombstoned(database_id):
    project = "PROJECT"
    id_ = 1094
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)

    xact.begin()

    assert xact.id == id_

    expected_request = _make_begin_request(project, database=database_id)
    ds_api.begin_transaction.assert_called_once_with(request=expected_request)

    xact.rollback()
    expected_request = {"project_id": project, "transaction": id_}
    set_database_id_to_request(expected_request, database_id)
    client._datastore_api.rollback.assert_called_once_with(request=expected_request)
    assert xact.id is None

    with pytest.raises(ValueError):
        xact.begin()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_begin_w_begin_transaction_failure(database_id):
    project = "PROJECT"
    id_ = 712
    ds_api = _make_datastore_api(xact_id=id_)
    ds_api.begin_transaction = mock.Mock(side_effect=RuntimeError, spec=[])
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)

    with pytest.raises(RuntimeError):
        xact.begin()

    assert xact.id is None

    expected_request = _make_begin_request(project, database=database_id)
    ds_api.begin_transaction.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_rollback(database_id):
    project = "PROJECT"
    id_ = 239
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)
    xact.begin()

    xact.rollback()

    assert xact.id is None
    expected_request = {"project_id": project, "transaction": id_}
    set_database_id_to_request(expected_request, database_id)
    ds_api.rollback.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_rollback_w_retry_w_timeout(database_id):
    project = "PROJECT"
    id_ = 239
    retry = mock.Mock()
    timeout = 100000

    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)
    xact.begin()

    xact.rollback(retry=retry, timeout=timeout)

    assert xact.id is None
    expected_request = {"project_id": project, "transaction": id_}
    set_database_id_to_request(expected_request, database_id)

    ds_api.rollback.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_commit_no_partial_keys(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    id_ = 1002930
    mode = datastore_pb2.CommitRequest.Mode.TRANSACTIONAL

    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, database=database_id, datastore_api=ds_api)
    xact = _make_transaction(client)
    xact.begin()
    xact.commit()

    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": [],
        "transaction": id_,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.commit.assert_called_once_with(request=expected_request)
    assert xact.id is None


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_commit_w_partial_keys_w_retry_w_timeout(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    kind = "KIND"
    id1 = 123
    mode = datastore_pb2.CommitRequest.Mode.TRANSACTIONAL
    key = _make_key(kind, id1, project, database=database_id)
    id2 = 234
    retry = mock.Mock()
    timeout = 100000

    ds_api = _make_datastore_api(key, xact_id=id2)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)
    xact.begin()
    entity = _Entity(database=database_id)

    xact.put(entity)
    xact.commit(retry=retry, timeout=timeout)
    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": xact.mutations,
        "transaction": id2,
    }
    set_database_id_to_request(expected_request, database_id)

    ds_api.commit.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )
    assert xact.id is None
    assert entity.key.path == [{"kind": kind, "id": id1}]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_context_manager_no_raise(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    id_ = 912830
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)

    with xact:
        assert xact._status == xact._IN_PROGRESS
        # only set between begin / commit
        assert xact.id == id_

    assert xact.id is None

    expected_request = _make_begin_request(project, database=database_id)
    ds_api.begin_transaction.assert_called_once_with(request=expected_request)

    mode = datastore_pb2.CommitRequest.Mode.TRANSACTIONAL
    expected_request = {
        "project_id": project,
        "mode": mode,
        "mutations": [],
        "transaction": id_,
    }
    set_database_id_to_request(expected_request, database_id)

    client._datastore_api.commit.assert_called_once_with(
        request=expected_request,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_context_manager_w_raise(database_id):
    class Foo(Exception):
        pass

    project = "PROJECT"
    id_ = 614416
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client)
    xact._mutation = object()
    try:
        with xact:
            assert xact.id == id_
            raise Foo()
    except Foo:
        pass

    assert xact.id is None

    expected_request = _make_begin_request(project, database=database_id)
    set_database_id_to_request(expected_request, database_id)
    ds_api.begin_transaction.assert_called_once_with(request=expected_request)

    client._datastore_api.commit.assert_not_called()
    expected_request = {"project_id": project, "transaction": id_}
    set_database_id_to_request(expected_request, database_id)
    client._datastore_api.rollback.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("with_exception", [False, True])
@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_context_manager_w_begin_later(database_id, with_exception):
    """
    If begin_later is set, don't begin transaction when entering context manager
    """
    project = "PROJECT"
    id_ = 912830
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    xact = _make_transaction(client, begin_later=True)

    try:
        with xact:
            assert xact._status == xact._INITIAL
            assert xact.id is None
            if with_exception:
                raise RuntimeError("expected")
    except RuntimeError:
        pass
    # should be finalized after context manager block
    assert xact._status == xact._ABORTED
    assert xact.id is None
    # no need to call commit or rollback
    assert ds_api.commit.call_count == 0
    assert ds_api.rollback.call_count == 0


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_put_read_only(database_id):
    project = "PROJECT"
    id_ = 943243
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    entity = _Entity(database=database_id)
    xact = _make_transaction(client, read_only=True)
    xact.begin()

    with pytest.raises(RuntimeError):
        xact.put(entity)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_put_w_begin_later(database_id):
    """
    If begin_later is set, should be able to call put without begin first
    """
    project = "PROJECT"
    id_ = 943243
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    entity = _Entity(database=database_id)
    with _make_transaction(client, begin_later=True) as xact:
        assert xact._status == xact._INITIAL
        assert len(xact.mutations) == 0
        xact.put(entity)
        assert len(xact.mutations) == 1
        # should still be in initial state
        assert xact._status == xact._INITIAL


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_delete_w_begin_later(database_id):
    """
    If begin_later is set, should be able to call delete without begin first
    """
    project = "PROJECT"
    id_ = 943243
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    entity = _Entity(database=database_id)
    with _make_transaction(client, begin_later=True) as xact:
        assert xact._status == xact._INITIAL
        assert len(xact.mutations) == 0
        xact.delete(entity.key.completed_key("name"))
        assert len(xact.mutations) == 1
        # should still be in initial state
        assert xact._status == xact._INITIAL


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_rollback_no_begin(database_id):
    """
    If rollback is called without begin, transaciton should abort
    """
    project = "PROJECT"
    id_ = 943243
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    with _make_transaction(client, begin_later=True) as xact:
        assert xact._status == xact._INITIAL
        with mock.patch.object(xact, "begin") as begin:
            xact.rollback()
            begin.assert_not_called()
        assert xact._status == xact._ABORTED


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_commit_no_begin(database_id):
    """
    If commit is called without begin, and it has mutations staged,
    should call begin before commit
    """
    project = "PROJECT"
    id_ = 943243
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    entity = _Entity(database=database_id)
    with _make_transaction(client, begin_later=True) as xact:
        assert xact._status == xact._INITIAL
        xact.put(entity)
        assert xact._status == xact._INITIAL
        with mock.patch.object(xact, "begin") as begin:
            begin.side_effect = lambda: setattr(xact, "_status", xact._IN_PROGRESS)
            xact.commit()
            begin.assert_called_once_with()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_empty_transaction_commit(database_id):
    """
    If commit is called without begin, and it has no mutations staged,
    should abort
    """
    project = "PROJECT"
    id_ = 943243
    ds_api = _make_datastore_api(xact_id=id_)
    client = _Client(project, datastore_api=ds_api, database=database_id)
    with _make_transaction(client, begin_later=True) as xact:
        assert xact._status == xact._INITIAL
        with mock.patch.object(xact, "begin") as begin:
            xact.commit()
            begin.assert_not_called()
        assert xact._status == xact._ABORTED


def _make_key(kind, id_, project, database=None):
    from google.cloud.datastore_v1.types import entity as entity_pb2

    key = entity_pb2.Key()
    key.partition_id.project_id = project
    key.partition_id.database_id = database
    elem = key._pb.path.add()
    elem.kind = kind
    elem.id = id_
    return key


class _Entity(dict):
    def __init__(self, database=None):
        super(_Entity, self).__init__()
        from google.cloud.datastore.key import Key

        self.key = Key("KIND", project="PROJECT", database=database)


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
        return self._batches and self._batches[0] or None


class _NoCommitBatch(object):
    def __init__(self, client):
        from google.cloud.datastore.batch import Batch

        self._client = client
        self._batch = Batch(client)

    def __enter__(self):
        self._client._push_batch(self._batch)
        return self._batch

    def __exit__(self, *args):
        self._client._pop_batch()


def _make_options(read_only=False, previous_transaction=None, read_time=None):
    from google.protobuf.timestamp_pb2 import Timestamp

    from google.cloud.datastore_v1.types import TransactionOptions

    kw = {}

    if read_only:
        read_only_kw = {}
        if read_time is not None:
            read_time_pb = Timestamp()
            read_time_pb.FromDatetime(read_time)
            read_only_kw["read_time"] = read_time_pb

        kw["read_only"] = TransactionOptions.ReadOnly(**read_only_kw)

    return TransactionOptions(**kw)


def _make_transaction(client, **kw):
    from google.cloud.datastore.transaction import Transaction

    return Transaction(client, **kw)


def _make_begin_request(project, read_only=False, read_time=None, database=None):
    expected_options = _make_options(read_only=read_only, read_time=read_time)
    request = {
        "project_id": project,
        "transaction_options": expected_options,
    }
    set_database_id_to_request(request, database)
    return request


def _make_commit_response(*keys):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    mutation_results = [datastore_pb2.MutationResult(key=key)._pb for key in keys]
    return datastore_pb2.CommitResponse(mutation_results=mutation_results)


def _make_datastore_api(*keys, **kwargs):
    commit_method = mock.Mock(return_value=_make_commit_response(*keys), spec=[])

    xact_id = kwargs.pop("xact_id", 123)
    txn_pb = mock.Mock(transaction=xact_id, spec=["transaction"])
    begin_txn = mock.Mock(return_value=txn_pb, spec=[])

    return mock.Mock(
        commit=commit_method,
        begin_transaction=begin_txn,
        spec=["begin_transaction", "commit", "rollback"],
    )
