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

import os
from typing import Any, Dict

import mock
import pytest

from google.cloud.datastore.helpers import set_database_id_to_request

PROJECT = "dummy-project-123"
DATABASE = "dummy-database-123"


def test__get_gcd_project_wo_value_set():
    from google.cloud.datastore.client import _get_gcd_project

    environ = {}

    with mock.patch("os.getenv", new=environ.get):
        project = _get_gcd_project()
        assert project is None


def test__get_gcd_project_w_value_set():
    from google.cloud.datastore.client import DATASTORE_DATASET, _get_gcd_project

    environ = {DATASTORE_DATASET: PROJECT}

    with mock.patch("os.getenv", new=environ.get):
        project = _get_gcd_project()
        assert project == PROJECT


def _determine_default_helper(gcd=None, fallback=None, project_called=None):
    from google.cloud.datastore.client import _determine_default_project

    _callers = []

    def gcd_mock():
        _callers.append("gcd_mock")
        return gcd

    def fallback_mock(project=None):
        _callers.append(("fallback_mock", project))
        return fallback

    patch = mock.patch.multiple(
        "google.cloud.datastore.client",
        _get_gcd_project=gcd_mock,
        _base_default_project=fallback_mock,
    )
    with patch:
        returned_project = _determine_default_project(project_called)

    return returned_project, _callers


def test__determine_default_project_wo_value():
    project, callers = _determine_default_helper()
    assert project is None
    assert callers == ["gcd_mock", ("fallback_mock", None)]


def test__determine_default_project_w_explicit():
    project, callers = _determine_default_helper(project_called=PROJECT)
    assert project == PROJECT
    assert callers == []


def test__determine_default_project_w_gcd():
    project, callers = _determine_default_helper(gcd=PROJECT)
    assert project == PROJECT
    assert callers == ["gcd_mock"]


def test__determine_default_project_w_fallback():
    project, callers = _determine_default_helper(fallback=PROJECT)
    assert project == PROJECT
    assert callers == ["gcd_mock", ("fallback_mock", None)]


def _make_client(
    project=PROJECT,
    namespace=None,
    credentials=None,
    client_info=None,
    client_options=None,
    _http=None,
    _use_grpc=None,
    database="",
):
    from google.cloud.datastore.client import Client

    return Client(
        project=project,
        database=database,
        namespace=namespace,
        credentials=credentials,
        client_info=client_info,
        client_options=client_options,
        _http=_http,
        _use_grpc=_use_grpc,
    )


@mock.patch.dict(os.environ, clear=True)
def test_client_ctor_w_project_no_environ():
    # Some environments (e.g. AppVeyor CI) run in GCE, so
    # this test would fail artificially.
    patch = mock.patch(
        "google.cloud.datastore.client._base_default_project", return_value=None
    )
    with patch:
        with pytest.raises(EnvironmentError):
            _make_client(project=None)


@pytest.mark.parametrize("database_id", [None, "somedb"])
@mock.patch.dict(os.environ, clear=True)
def test_client_ctor_w_implicit_inputs(database_id):
    from google.cloud.datastore.client import _CLIENT_INFO, _DATASTORE_BASE_URL, Client

    other = "other"
    patch1 = mock.patch(
        "google.cloud.datastore.client._determine_default_project",
        return_value=other,
    )

    creds = _make_credentials()
    patch2 = mock.patch("google.auth.default", return_value=(creds, None))

    with patch1 as _determine_default_project:
        with patch2 as default:
            client = Client(database=database_id)

    assert client.project == other
    assert client.database == database_id
    assert client.namespace is None
    assert client._credentials is creds
    assert client._client_info is _CLIENT_INFO
    assert client._http_internal is None
    assert client._client_options is None
    assert client.base_url == _DATASTORE_BASE_URL

    assert client.current_batch is None
    assert client.current_transaction is None

    default.assert_called_once_with(
        scopes=Client.SCOPE,
    )
    _determine_default_project.assert_called_once_with(None)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_ctor_w_explicit_inputs(database_id):
    from google.api_core.client_options import ClientOptions

    other = "other"
    database = "database"
    namespace = "namespace"
    creds = _make_credentials()
    client_info = mock.Mock()
    client_options = ClientOptions("endpoint")
    http = object()
    client = _make_client(
        project=other,
        database=database,
        namespace=namespace,
        credentials=creds,
        client_info=client_info,
        client_options=client_options,
        _http=http,
    )
    assert client.project == other
    assert client.database == database
    assert client.namespace == namespace
    assert client._credentials is creds
    assert client._client_info is client_info
    assert client._http_internal is http
    assert client.current_batch is None
    assert client._base_url == "endpoint"
    assert list(client._batch_stack) == []


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_ctor_use_grpc_default(database_id):
    import google.cloud.datastore.client as MUT

    project = "PROJECT"
    creds = _make_credentials()
    http = object()

    with mock.patch.object(MUT, "_USE_GRPC", new=True):
        client1 = _make_client(
            project=PROJECT, credentials=creds, _http=http, database=database_id
        )
        assert client1._use_grpc
        # Explicitly over-ride the environment.
        client2 = _make_client(
            project=project,
            credentials=creds,
            _http=http,
            _use_grpc=False,
            database=database_id,
        )
        assert not client2._use_grpc

    with mock.patch.object(MUT, "_USE_GRPC", new=False):
        client3 = _make_client(
            project=PROJECT, credentials=creds, _http=http, database=database_id
        )
        assert not client3._use_grpc
        # Explicitly over-ride the environment.
        client4 = _make_client(
            project=project,
            credentials=creds,
            _http=http,
            _use_grpc=True,
            database=database_id,
        )
        assert client4._use_grpc


def test_client_ctor_w_emulator_w_creds():
    from google.cloud.datastore.client import DATASTORE_EMULATOR_HOST

    host = "localhost:1234"
    fake_environ = {DATASTORE_EMULATOR_HOST: host}
    project = "PROJECT"
    creds = _make_credentials()
    http = object()

    with mock.patch("os.environ", new=fake_environ):
        with pytest.raises(ValueError):
            _make_client(project=project, credentials=creds, _http=http)


def test_client_ctor_w_emulator_wo_creds():
    from google.auth.credentials import AnonymousCredentials

    from google.cloud.datastore.client import DATASTORE_EMULATOR_HOST

    host = "localhost:1234"
    fake_environ = {DATASTORE_EMULATOR_HOST: host}
    project = "PROJECT"
    http = object()

    with mock.patch("os.environ", new=fake_environ):
        client = _make_client(project=project, _http=http)

    assert client.base_url == "http://" + host
    assert isinstance(client._credentials, AnonymousCredentials)


def test_client_base_url_property():
    from google.api_core.client_options import ClientOptions

    from google.cloud.datastore.client import _DATASTORE_BASE_URL

    alternate_url = "https://alias.example.com/"
    creds = _make_credentials()
    client_options = ClientOptions()

    client = _make_client(credentials=creds, client_options=client_options)
    assert client.base_url == _DATASTORE_BASE_URL

    client.base_url = alternate_url
    assert client.base_url == alternate_url


def test_client_base_url_property_w_client_options():
    alternate_url = "https://alias.example.com/"
    creds = _make_credentials()
    client_options = {"api_endpoint": "endpoint"}

    client = _make_client(
        credentials=creds,
        client_options=client_options,
    )
    assert client.base_url == "endpoint"

    client.base_url = alternate_url
    assert client.base_url == alternate_url


def test_client__datastore_api_property_already_set():
    client = _make_client(credentials=_make_credentials(), _use_grpc=True)
    already = client._datastore_api_internal = object()
    assert client._datastore_api is already


def test_client__datastore_api_property_gapic():
    client_info = mock.Mock()
    client = _make_client(
        project="prahj-ekt",
        credentials=_make_credentials(),
        client_info=client_info,
        _http=object(),
        _use_grpc=True,
    )

    assert client._datastore_api_internal is None
    patch = mock.patch(
        "google.cloud.datastore.client.make_datastore_api",
        return_value=mock.sentinel.ds_api,
    )
    with patch as make_api:
        ds_api = client._datastore_api

    assert ds_api is mock.sentinel.ds_api
    assert client._datastore_api_internal is mock.sentinel.ds_api
    make_api.assert_called_once_with(client)


def test__datastore_api_property_http():
    client_info = mock.Mock()
    client = _make_client(
        project="prahj-ekt",
        credentials=_make_credentials(),
        client_info=client_info,
        _http=object(),
        _use_grpc=False,
    )

    assert client._datastore_api_internal is None
    patch = mock.patch(
        "google.cloud.datastore.client.HTTPDatastoreAPI",
        return_value=mock.sentinel.ds_api,
    )
    with patch as make_api:
        ds_api = client._datastore_api

    assert ds_api is mock.sentinel.ds_api
    assert client._datastore_api_internal is mock.sentinel.ds_api
    make_api.assert_called_once_with(client)


def test_client__push_batch_and__pop_batch():
    creds = _make_credentials()
    client = _make_client(credentials=creds)
    batch = client.batch()
    xact = client.transaction()

    client._push_batch(batch)
    assert list(client._batch_stack) == [batch]
    assert client.current_batch is batch
    assert client.current_transaction is None

    client._push_batch(xact)
    assert client.current_batch is xact
    assert client.current_transaction is xact
    # list(_LocalStack) returns in reverse order.
    assert list(client._batch_stack) == [xact, batch]

    assert client._pop_batch() is xact
    assert list(client._batch_stack) == [batch]
    assert client.current_batch is batch
    assert client.current_transaction is None

    assert client._pop_batch() is batch
    assert list(client._batch_stack) == []


def test_client_get_miss():
    creds = _make_credentials()
    client = _make_client(credentials=creds)
    get_multi = client.get_multi = mock.Mock(return_value=[])

    key = object()

    assert client.get(key) is None

    get_multi.assert_called_once_with(
        keys=[key],
        missing=None,
        deferred=None,
        transaction=None,
        eventual=False,
        retry=None,
        timeout=None,
        read_time=None,
    )


def test_client_get_hit():
    txn_id = "123"
    _entity = object()
    creds = _make_credentials()
    client = _make_client(credentials=creds)
    get_multi = client.get_multi = mock.Mock(return_value=[_entity])

    key, missing, deferred = object(), [], []

    assert client.get(key, missing, deferred, txn_id) is _entity

    get_multi.assert_called_once_with(
        keys=[key],
        missing=missing,
        deferred=deferred,
        transaction=txn_id,
        eventual=False,
        retry=None,
        timeout=None,
        read_time=None,
    )


def test_client_get_multi_no_keys():
    creds = _make_credentials()
    client = _make_client(credentials=creds)
    ds_api = _make_datastore_api()
    client._datastore_api_internal = ds_api

    results = client.get_multi([])

    assert results == []

    ds_api.lookup.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_miss(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    ds_api = _make_datastore_api()
    client._datastore_api_internal = ds_api

    key = Key("Kind", 1234, project=PROJECT)
    results = client.get_multi([key])
    assert results == []

    read_options = datastore_pb2.ReadOptions()
    expected_request = {
        "project_id": PROJECT,
        "keys": [key.to_protobuf()],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.lookup.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_miss_w_missing(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2

    KIND = "Kind"
    ID = 1234

    # Make a missing entity pb to be returned from mock backend.
    missed = entity_pb2.Entity()
    missed.key.partition_id.project_id = PROJECT
    missed.key.partition_id.database_id = database_id
    path_element = missed._pb.key.path.add()
    path_element.kind = KIND
    path_element.id = ID

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    # Set missing entity on mock connection.
    lookup_response = _make_lookup_response(missing=[missed._pb])
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    key = Key(KIND, ID, project=PROJECT, database=database_id)
    missing = []
    entities = client.get_multi([key], missing=missing)
    assert entities == []
    key_pb = key.to_protobuf()
    assert [missed.key.to_protobuf() for missed in missing] == [key_pb._pb]

    read_options = datastore_pb2.ReadOptions()
    expected_request = {
        "project_id": PROJECT,
        "keys": [key_pb],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.lookup.assert_called_once_with(request=expected_request)


def test_client_get_multi_w_missing_non_empty():
    from google.cloud.datastore.key import Key

    creds = _make_credentials()
    client = _make_client(credentials=creds)
    key = Key("Kind", 1234, project=PROJECT)

    missing = ["this", "list", "is", "not", "empty"]
    with pytest.raises(ValueError):
        client.get_multi([key], missing=missing)


def test_client_get_multi_w_deferred_non_empty():
    from google.cloud.datastore.key import Key

    creds = _make_credentials()
    client = _make_client(credentials=creds)
    key = Key("Kind", 1234, project=PROJECT)

    deferred = ["this", "list", "is", "not", "empty"]
    with pytest.raises(ValueError):
        client.get_multi([key], deferred=deferred)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_miss_w_deferred(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    key = Key("Kind", 1234, project=PROJECT, database=database_id)
    key_pb = key.to_protobuf()

    # Set deferred entity on mock connection.
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    lookup_response = _make_lookup_response(deferred=[key_pb])
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    deferred = []
    entities = client.get_multi([key], deferred=deferred)
    assert entities == []
    assert [def_key.to_protobuf() for def_key in deferred] == [key_pb]
    read_options = datastore_pb2.ReadOptions()
    expected_request = {
        "project_id": PROJECT,
        "keys": [key_pb],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request, database_id)

    ds_api.lookup.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_w_deferred_from_backend_but_not_passed(database_id):
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2

    key1 = Key("Kind", project=PROJECT, database=database_id)
    key1_pb = key1.to_protobuf()
    key2 = Key("Kind", 2345, project=PROJECT, database=database_id)
    key2_pb = key2.to_protobuf()

    entity1_pb = entity_pb2.Entity()
    entity1_pb._pb.key.CopyFrom(key1_pb._pb)
    entity2_pb = entity_pb2.Entity()
    entity2_pb._pb.key.CopyFrom(key2_pb._pb)

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    # Mock up two separate requests. Using an iterable as side_effect
    # allows multiple return values.
    lookup_response1 = _make_lookup_response(results=[entity1_pb], deferred=[key2_pb])
    lookup_response2 = _make_lookup_response(results=[entity2_pb])
    ds_api = _make_datastore_api()
    ds_api.lookup = mock.Mock(side_effect=[lookup_response1, lookup_response2], spec=[])
    client._datastore_api_internal = ds_api

    missing = []
    found = client.get_multi([key1, key2], missing=missing)
    assert len(found) == 2
    assert len(missing) == 0

    # Check the actual contents on the response.
    assert isinstance(found[0], Entity)
    assert found[0].key.path == key1.path
    assert found[0].key.project == key1.project
    assert found[0].key.database == key1.database

    assert isinstance(found[1], Entity)
    assert found[1].key.path == key2.path
    assert found[1].key.project == key2.project
    assert found[1].key.database == key2.database

    assert ds_api.lookup.call_count == 2
    read_options = datastore_pb2.ReadOptions()

    expected_request_1 = {
        "project_id": PROJECT,
        "keys": [key2_pb],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request_1, database_id)
    ds_api.lookup.assert_any_call(
        request=expected_request_1,
    )

    expected_request_2 = {
        "project_id": PROJECT,
        "keys": [key1_pb, key2_pb],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request_2, database_id)
    ds_api.lookup.assert_any_call(
        request=expected_request_2,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_hit_w_retry_w_timeout(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    kind = "Kind"
    id_ = 1234
    path = [{"kind": kind, "id": id_}]
    retry = mock.Mock()
    timeout = 100000

    # Make a found entity pb to be returned from mock backend.
    entity_pb = _make_entity_pb(PROJECT, kind, id_, "foo", "Foo", database=database_id)

    # Make a connection to return the entity pb.
    creds = _make_credentials()
    client = _make_client(credentials=creds)
    lookup_response = _make_lookup_response(results=[entity_pb])
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    key = Key(kind, id_, project=PROJECT)
    (result,) = client.get_multi([key], retry=retry, timeout=timeout)
    new_key = result.key

    # Check the returned value is as expected.
    assert new_key is not key
    assert new_key.project == PROJECT
    assert new_key.path == path
    assert list(result) == ["foo"]
    assert result["foo"] == "Foo"

    read_options = datastore_pb2.ReadOptions()

    ds_api.lookup.assert_called_once_with(
        request={
            "project_id": PROJECT,
            "database_id": "",
            "keys": [key.to_protobuf()],
            "read_options": read_options,
        },
        retry=retry,
        timeout=timeout,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_hit_w_transaction(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    txn_id = b"123"
    kind = "Kind"
    id_ = 1234
    path = [{"kind": kind, "id": id_}]

    # Make a found entity pb to be returned from mock backend.
    entity_pb = _make_entity_pb(PROJECT, kind, id_, "foo", "Foo", database=database_id)

    # Make a connection to return the entity pb.
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    lookup_response = _make_lookup_response(results=[entity_pb])
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    key = Key(kind, id_, project=PROJECT, database=database_id)
    txn = client.transaction()
    txn._id = txn_id
    (result,) = client.get_multi([key], transaction=txn)
    new_key = result.key

    # Check the returned value is as expected.
    assert new_key is not key
    assert new_key.project == PROJECT
    assert new_key.path == path
    assert list(result) == ["foo"]
    assert result["foo"] == "Foo"

    read_options = datastore_pb2.ReadOptions(transaction=txn_id)
    expected_request = {
        "project_id": PROJECT,
        "keys": [key.to_protobuf()],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.lookup.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_hit_w_transaction_begin_later(database_id):
    """
    Transactions with begin_later set should begin on first read
    """
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    kind = "Kind"
    id_ = 1234
    expected_server_id = b"123"

    # Make a found entity pb to be returned from mock backend.
    entity_pb = _make_entity_pb(PROJECT, kind, id_, "foo", "Foo", database=database_id)

    # Make a connection to return the entity pb.
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    lookup_response = _make_lookup_response(
        results=[entity_pb], transaction=expected_server_id
    )
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    key = Key(kind, id_, project=PROJECT, database=database_id)
    txn = client.transaction(begin_later=True)
    assert txn._id is None
    assert txn._status == txn._INITIAL
    client.get_multi([key], transaction=txn)

    # transaction should now be started
    assert txn._id == expected_server_id
    assert txn._id is not None
    assert txn._status == txn._IN_PROGRESS

    # check rpc args
    expected_read_options = datastore_pb2.ReadOptions(new_transaction=txn._options)
    expected_request = {
        "project_id": PROJECT,
        "keys": [key.to_protobuf()],
        "read_options": expected_read_options,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.lookup.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_hit_w_read_time(database_id):
    from datetime import datetime

    from google.protobuf.timestamp_pb2 import Timestamp

    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    read_time = datetime.utcfromtimestamp(1641058200.123456)
    read_time_pb = Timestamp(seconds=1641058200, nanos=123456000)
    kind = "Kind"
    id_ = 1234
    path = [{"kind": kind, "id": id_}]

    # Make a found entity pb to be returned from mock backend.
    entity_pb = _make_entity_pb(PROJECT, kind, id_, "foo", "Foo", database=database_id)

    # Make a connection to return the entity pb.
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    lookup_response = _make_lookup_response(results=[entity_pb])
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    key = Key(kind, id_, project=PROJECT, database=database_id)
    (result,) = client.get_multi([key], read_time=read_time)
    new_key = result.key

    # Check the returned value is as expected.
    assert new_key is not key
    assert new_key.project == PROJECT
    assert new_key.path == path
    assert list(result) == ["foo"]
    assert result["foo"] == "Foo"

    read_options = datastore_pb2.ReadOptions(read_time=read_time_pb)
    expected_request = {
        "project_id": PROJECT,
        "keys": [key.to_protobuf()],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.lookup.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_hit_multiple_keys_same_project(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    kind = "Kind"
    id1 = 1234
    id2 = 2345

    # Make a found entity pb to be returned from mock backend.
    entity_pb1 = _make_entity_pb(PROJECT, kind, id1, database=database_id)
    entity_pb2 = _make_entity_pb(PROJECT, kind, id2, database=database_id)

    # Make a connection to return the entity pbs.
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    lookup_response = _make_lookup_response(results=[entity_pb1, entity_pb2])
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    key1 = Key(kind, id1, project=PROJECT, database=database_id)
    key2 = Key(kind, id2, project=PROJECT, database=database_id)
    retrieved1, retrieved2 = client.get_multi([key1, key2])

    # Check values match.
    assert retrieved1.key.path == key1.path
    assert dict(retrieved1) == {}
    assert retrieved2.key.path == key2.path
    assert dict(retrieved2) == {}

    read_options = datastore_pb2.ReadOptions()
    expected_request = {
        "project_id": PROJECT,
        "keys": [key1.to_protobuf(), key2.to_protobuf()],
        "read_options": read_options,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.lookup.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_hit_multiple_keys_different_project(database_id):
    from google.cloud.datastore.key import Key

    PROJECT1 = "PROJECT"
    PROJECT2 = "PROJECT-ALT"

    key1 = Key("KIND", 1234, project=PROJECT1, database=database_id)
    key2 = Key("KIND", 1234, project=PROJECT2, database=database_id)

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)

    with pytest.raises(ValueError):
        client.get_multi([key1, key2])


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_get_multi_max_loops(database_id):
    from google.cloud.datastore.key import Key

    kind = "Kind"
    id_ = 1234

    # Make a found entity pb to be returned from mock backend.
    entity_pb = _make_entity_pb(PROJECT, kind, id_, "foo", "Foo", database=database_id)

    # Make a connection to return the entity pb.
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    lookup_response = _make_lookup_response(results=[entity_pb])
    ds_api = _make_datastore_api(lookup_response=lookup_response)
    client._datastore_api_internal = ds_api

    key = Key(kind, id_, project=PROJECT, database=database_id)
    deferred = []
    missing = []

    patch = mock.patch("google.cloud.datastore.client._MAX_LOOPS", new=-1)
    with patch:
        result = client.get_multi([key], missing=missing, deferred=deferred)

    # Make sure we have no results, even though the connection has been
    # set up as in `test_hit` to return a single result.
    assert result == []
    assert missing == []
    assert deferred == []
    ds_api.lookup.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_put(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    put_multi = client.put_multi = mock.Mock()
    entity = mock.Mock()

    client.put(entity)

    put_multi.assert_called_once_with(entities=[entity], retry=None, timeout=None)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_put_w_retry_w_timeout(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    put_multi = client.put_multi = mock.Mock()
    entity = mock.Mock()
    retry = mock.Mock()
    timeout = 100000

    client.put(entity, retry=retry, timeout=timeout)

    put_multi.assert_called_once_with(entities=[entity], retry=retry, timeout=timeout)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_put_multi_no_entities(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    assert client.put_multi([]) is None


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_put_multi_w_single_empty_entity(database_id):
    # https://github.com/GoogleCloudPlatform/google-cloud-python/issues/649
    from google.cloud.datastore.entity import Entity

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        client.put_multi(Entity())


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_put_multi_no_batch_w_partial_key_w_retry_w_timeout(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    entity = _Entity(foo="bar")
    key = entity.key = _Key(_Key.kind, None, database=database_id)
    retry = mock.Mock()
    timeout = 100000

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    key_pb = _make_key(234)
    ds_api = _make_datastore_api(key_pb)
    client._datastore_api_internal = ds_api

    result = client.put_multi([entity], retry=retry, timeout=timeout)
    assert result is None

    expected_request = {
        "project_id": PROJECT,
        "mode": datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL,
        "mutations": mock.ANY,
        "transaction": None,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.commit.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )

    mutations = ds_api.commit.call_args[1]["request"]["mutations"]
    mutated_entity = _mutated_pb(mutations, "insert")
    assert mutated_entity.key == key.to_protobuf()

    prop_list = list(mutated_entity.properties.items())
    assert len(prop_list) == 1
    name, value_pb = prop_list[0]
    assert name == "foo"
    assert value_pb.string_value == "bar"


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_put_multi_existing_batch_w_completed_key(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    entity = _Entity(foo="bar")
    key = entity.key = _Key(database=database_id)

    with _NoCommitBatch(client) as CURR_BATCH:
        result = client.put_multi([entity])

    assert result is None
    mutated_entity = _mutated_pb(CURR_BATCH.mutations, "upsert")
    assert mutated_entity.key == key.to_protobuf()

    prop_list = list(mutated_entity.properties.items())
    assert len(prop_list) == 1
    name, value_pb = prop_list[0]
    assert name == "foo"
    assert value_pb.string_value == "bar"


def test_client_delete():
    creds = _make_credentials()
    client = _make_client(credentials=creds)
    delete_multi = client.delete_multi = mock.Mock()
    key = mock.Mock()

    client.delete(key)

    delete_multi.assert_called_once_with(keys=[key], retry=None, timeout=None)


def test_client_delete_w_retry_w_timeout():
    creds = _make_credentials()
    client = _make_client(credentials=creds)
    delete_multi = client.delete_multi = mock.Mock()
    key = mock.Mock()
    retry = mock.Mock()
    timeout = 100000

    client.delete(key, retry=retry, timeout=timeout)

    delete_multi.assert_called_once_with(keys=[key], retry=retry, timeout=timeout)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_delete_multi_no_keys(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    client._datastore_api_internal = _make_datastore_api()

    result = client.delete_multi([])
    assert result is None
    client._datastore_api_internal.commit.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_delete_multi_no_batch_w_retry_w_timeout(database_id):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    key = _Key(database=database_id)
    retry = mock.Mock()
    timeout = 100000

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    ds_api = _make_datastore_api()
    client._datastore_api_internal = ds_api

    result = client.delete_multi([key], retry=retry, timeout=timeout)
    assert result is None

    expected_request = {
        "project_id": PROJECT,
        "mode": datastore_pb2.CommitRequest.Mode.NON_TRANSACTIONAL,
        "mutations": mock.ANY,
        "transaction": None,
    }
    set_database_id_to_request(expected_request, database_id)
    ds_api.commit.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )

    mutations = ds_api.commit.call_args[1]["request"]["mutations"]
    mutated_key = _mutated_pb(mutations, "delete")
    assert mutated_key == key.to_protobuf()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_delete_multi_w_existing_batch(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    client._datastore_api_internal = _make_datastore_api()

    key = _Key(database=database_id)

    with _NoCommitBatch(client) as CURR_BATCH:
        result = client.delete_multi([key])

    assert result is None
    mutated_key = _mutated_pb(CURR_BATCH.mutations, "delete")
    assert mutated_key == key._key
    client._datastore_api_internal.commit.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_delete_multi_w_existing_transaction(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    client._datastore_api_internal = _make_datastore_api()

    key = _Key(database=database_id)

    with _NoCommitTransaction(client) as CURR_XACT:
        result = client.delete_multi([key])

    assert result is None
    mutated_key = _mutated_pb(CURR_XACT.mutations, "delete")
    assert mutated_key == key._key
    client._datastore_api_internal.commit.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_delete_multi_w_existing_transaction_entity(database_id):
    from google.cloud.datastore.entity import Entity

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    client._datastore_api_internal = _make_datastore_api()

    key = _Key(database=database_id)
    entity = Entity(key=key)

    with _NoCommitTransaction(client) as CURR_XACT:
        result = client.delete_multi([entity])

    assert result is None
    mutated_key = _mutated_pb(CURR_XACT.mutations, "delete")
    assert mutated_key == key._key
    client._datastore_api_internal.commit.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_allocate_ids_w_completed_key(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds)

    complete_key = _Key(database=database_id)
    with pytest.raises(ValueError):
        client.allocate_ids(complete_key, 2)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_allocate_ids_w_partial_key(database_id):
    num_ids = 2

    incomplete_key = _Key(_Key.kind, None, database=database_id)

    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    allocated = mock.Mock(keys=[_KeyPB(i) for i in range(num_ids)], spec=["keys"])
    alloc_ids = mock.Mock(return_value=allocated, spec=[])
    ds_api = mock.Mock(allocate_ids=alloc_ids, spec=["allocate_ids"])
    client._datastore_api_internal = ds_api

    result = client.allocate_ids(incomplete_key, num_ids)

    # Check the IDs returned.
    assert [key.id for key in result] == list(range(num_ids))

    expected_keys = [incomplete_key.to_protobuf()] * num_ids
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    alloc_ids.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_allocate_ids_w_partial_key_w_retry_w_timeout(database_id):
    num_ids = 2

    incomplete_key = _Key(_Key.kind, None, database=database_id)
    retry = mock.Mock()
    timeout = 100000

    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    allocated = mock.Mock(keys=[_KeyPB(i) for i in range(num_ids)], spec=["keys"])
    alloc_ids = mock.Mock(return_value=allocated, spec=[])
    ds_api = mock.Mock(allocate_ids=alloc_ids, spec=["allocate_ids"])
    client._datastore_api_internal = ds_api

    result = client.allocate_ids(incomplete_key, num_ids, retry=retry, timeout=timeout)

    # Check the IDs returned.
    assert [key.id for key in result] == list(range(num_ids))

    expected_keys = [incomplete_key.to_protobuf()] * num_ids
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    alloc_ids.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_sequential_w_completed_key(database_id):
    num_ids = 2
    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    complete_key = _Key()
    reserve_ids = mock.Mock()
    ds_api = mock.Mock(reserve_ids=reserve_ids, spec=["reserve_ids"])
    client._datastore_api_internal = ds_api
    assert not complete_key.is_partial

    client.reserve_ids_sequential(complete_key, num_ids)

    reserved_keys = (
        _Key(_Key.kind, id) for id in range(complete_key.id, complete_key.id + num_ids)
    )
    expected_keys = [key.to_protobuf() for key in reserved_keys]
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    reserve_ids.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_sequential_w_completed_key_w_retry_w_timeout(database_id):
    num_ids = 2
    retry = mock.Mock()
    timeout = 100000

    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    complete_key = _Key(database=database_id)
    assert not complete_key.is_partial
    reserve_ids = mock.Mock()
    ds_api = mock.Mock(reserve_ids=reserve_ids, spec=["reserve_ids"])
    client._datastore_api_internal = ds_api

    client.reserve_ids_sequential(complete_key, num_ids, retry=retry, timeout=timeout)

    reserved_keys = (
        _Key(_Key.kind, id) for id in range(complete_key.id, complete_key.id + num_ids)
    )
    expected_keys = [key.to_protobuf() for key in reserved_keys]
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    reserve_ids.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_sequential_w_completed_key_w_ancestor(database_id):
    num_ids = 2
    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    complete_key = _Key("PARENT", "SINGLETON", _Key.kind, 1234)
    reserve_ids = mock.Mock()
    ds_api = mock.Mock(reserve_ids=reserve_ids, spec=["reserve_ids"])
    client._datastore_api_internal = ds_api
    assert not complete_key.is_partial

    client.reserve_ids_sequential(complete_key, num_ids)

    reserved_keys = (
        _Key("PARENT", "SINGLETON", _Key.kind, id, database=database_id)
        for id in range(complete_key.id, complete_key.id + num_ids)
    )
    expected_keys = [key.to_protobuf() for key in reserved_keys]
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    reserve_ids.assert_called_once_with(request=expected_request)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_sequential_w_partial_key(database_id):
    num_ids = 2
    incomplete_key = _Key(_Key.kind, None, database=database_id)
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        client.reserve_ids_sequential(incomplete_key, num_ids)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_sequential_w_wrong_num_ids(database_id):
    num_ids = "2"
    complete_key = _Key(database=database_id)
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        client.reserve_ids_sequential(complete_key, num_ids)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_sequential_w_non_numeric_key_name(database_id):
    num_ids = 2
    complete_key = _Key(_Key.kind, "batman", database=database_id)
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        client.reserve_ids_sequential(complete_key, num_ids)


def _assert_reserve_ids_warning(warned):
    assert len(warned) == 1
    assert "Client.reserve_ids is deprecated." in str(warned[0].message)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_w_partial_key(database_id):
    import warnings

    num_ids = 2
    incomplete_key = _Key(_Key.kind, None)
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        with warnings.catch_warnings(record=True) as warned:
            client.reserve_ids(incomplete_key, num_ids)

    _assert_reserve_ids_warning(warned)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_w_wrong_num_ids(database_id):
    import warnings

    num_ids = "2"
    complete_key = _Key(database=database_id)
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        with warnings.catch_warnings(record=True) as warned:
            client.reserve_ids(complete_key, num_ids)

    _assert_reserve_ids_warning(warned)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_w_non_numeric_key_name(database_id):
    import warnings

    num_ids = 2
    complete_key = _Key(_Key.kind, "batman", database=database_id)
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        with warnings.catch_warnings(record=True) as warned:
            client.reserve_ids(complete_key, num_ids)

    _assert_reserve_ids_warning(warned)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_w_completed_key(database_id):
    import warnings

    num_ids = 2
    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    complete_key = _Key(database=database_id)
    reserve_ids = mock.Mock()
    ds_api = mock.Mock(reserve_ids=reserve_ids, spec=["reserve_ids"])
    client._datastore_api_internal = ds_api
    assert not complete_key.is_partial

    with warnings.catch_warnings(record=True) as warned:
        client.reserve_ids(complete_key, num_ids)

    reserved_keys = (
        _Key(_Key.kind, id, database=database_id)
        for id in range(complete_key.id, complete_key.id + num_ids)
    )
    expected_keys = [key.to_protobuf() for key in reserved_keys]
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    reserve_ids.assert_called_once_with(request=expected_request)
    _assert_reserve_ids_warning(warned)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_w_completed_key_w_retry_w_timeout(database_id):
    import warnings

    num_ids = 2
    retry = mock.Mock()
    timeout = 100000

    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    complete_key = _Key(database=database_id)
    assert not complete_key.is_partial
    reserve_ids = mock.Mock()
    ds_api = mock.Mock(reserve_ids=reserve_ids, spec=["reserve_ids"])
    client._datastore_api_internal = ds_api

    with warnings.catch_warnings(record=True) as warned:
        client.reserve_ids(complete_key, num_ids, retry=retry, timeout=timeout)

    reserved_keys = (
        _Key(_Key.kind, id, database=database_id)
        for id in range(complete_key.id, complete_key.id + num_ids)
    )
    expected_keys = [key.to_protobuf() for key in reserved_keys]
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    reserve_ids.assert_called_once_with(
        request=expected_request,
        retry=retry,
        timeout=timeout,
    )
    _assert_reserve_ids_warning(warned)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_w_completed_key_w_ancestor(database_id):
    import warnings

    num_ids = 2
    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    complete_key = _Key("PARENT", "SINGLETON", _Key.kind, 1234, database=database_id)
    reserve_ids = mock.Mock()
    ds_api = mock.Mock(reserve_ids=reserve_ids, spec=["reserve_ids"])
    client._datastore_api_internal = ds_api
    assert not complete_key.is_partial

    with warnings.catch_warnings(record=True) as warned:
        client.reserve_ids(complete_key, num_ids)

    reserved_keys = (
        _Key("PARENT", "SINGLETON", _Key.kind, id, database=database_id)
        for id in range(complete_key.id, complete_key.id + num_ids)
    )
    expected_keys = [key.to_protobuf() for key in reserved_keys]
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)

    reserve_ids.assert_called_once_with(request=expected_request)

    _assert_reserve_ids_warning(warned)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_key_w_project(database_id):
    KIND = "KIND"
    ID = 1234

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)

    with pytest.raises(TypeError):
        client.key(KIND, ID, project=PROJECT, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_key_wo_project(database_id):
    kind = "KIND"
    id_ = 1234

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Key", spec=["__call__"])
    with patch as mock_klass:
        key = client.key(kind, id_)
        assert key is mock_klass.return_value
        mock_klass.assert_called_once_with(
            kind, id_, project=PROJECT, namespace=None, database=database_id
        )


def test_client_key_w_database():
    KIND = "KIND"
    ID = 1234

    creds = _make_credentials()
    client = _make_client(credentials=creds)

    with pytest.raises(TypeError):
        client.key(KIND, ID, database="somedb")


def test_client_key_wo_database():
    kind = "KIND"
    id_ = 1234
    database = "DATABASE"

    creds = _make_credentials()
    client = _make_client(database=database, credentials=creds)

    patch = mock.patch("google.cloud.datastore.client.Key", spec=["__call__"])
    with patch as mock_klass:
        key = client.key(kind, id_)
        assert key is mock_klass.return_value
        mock_klass.assert_called_once_with(
            kind, id_, project=PROJECT, namespace=None, database=database
        )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_key_w_namespace(database_id):
    kind = "KIND"
    id_ = 1234
    namespace = object()

    creds = _make_credentials()
    client = _make_client(namespace=namespace, credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Key", spec=["__call__"])
    with patch as mock_klass:
        key = client.key(kind, id_)
        assert key is mock_klass.return_value
        mock_klass.assert_called_once_with(
            kind, id_, project=PROJECT, namespace=namespace, database=database_id
        )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_key_w_namespace_collision(database_id):
    kind = "KIND"
    id_ = 1234
    namespace1 = object()
    namespace2 = object()

    creds = _make_credentials()
    client = _make_client(namespace=namespace1, credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Key", spec=["__call__"])
    with patch as mock_klass:
        key = client.key(kind, id_, namespace=namespace2)
        assert key is mock_klass.return_value
        mock_klass.assert_called_once_with(
            kind, id_, project=PROJECT, namespace=namespace2, database=database_id
        )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_entity_w_defaults(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Entity", spec=["__call__"])
    with patch as mock_klass:
        entity = client.entity()
        assert entity is mock_klass.return_value
        mock_klass.assert_called_once_with(key=None, exclude_from_indexes=())


def test_client_entity_w_explicit():
    key = mock.Mock(spec=[])
    exclude_from_indexes = ["foo", "bar"]
    creds = _make_credentials()
    client = _make_client(credentials=creds)

    patch = mock.patch("google.cloud.datastore.client.Entity", spec=["__call__"])
    with patch as mock_klass:
        entity = client.entity(key, exclude_from_indexes)
        assert entity is mock_klass.return_value
        mock_klass.assert_called_once_with(
            key=key, exclude_from_indexes=exclude_from_indexes
        )


def test_client_batch():
    creds = _make_credentials()
    client = _make_client(credentials=creds)

    patch = mock.patch("google.cloud.datastore.client.Batch", spec=["__call__"])
    with patch as mock_klass:
        batch = client.batch()
        assert batch is mock_klass.return_value
        mock_klass.assert_called_once_with(client)


def test_client_transaction_w_defaults():
    creds = _make_credentials()
    client = _make_client(credentials=creds)

    patch = mock.patch("google.cloud.datastore.client.Transaction", spec=["__call__"])
    with patch as mock_klass:
        xact = client.transaction()
        assert xact is mock_klass.return_value
        mock_klass.assert_called_once_with(client)


def test_client_transaction_w_read_only():
    from google.cloud.datastore_v1.types import TransactionOptions

    creds = _make_credentials()
    client = _make_client(credentials=creds)
    xact = client.transaction(read_only=True)
    options = TransactionOptions(read_only=TransactionOptions.ReadOnly())
    assert xact._options == options
    assert not xact._options._pb.HasField("read_write")
    assert xact._options._pb.HasField("read_only")
    assert xact._options._pb.read_only == TransactionOptions.ReadOnly()._pb


def test_client_query_w_other_client():
    KIND = "KIND"

    creds = _make_credentials()
    client = _make_client(credentials=creds)
    other = _make_client(credentials=_make_credentials())

    with pytest.raises(TypeError):
        client.query(kind=KIND, client=other)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_query_w_project(database_id):
    KIND = "KIND"

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)

    with pytest.raises(TypeError):
        client.query(kind=KIND, project=PROJECT)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_query_w_defaults(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Query", spec=["__call__"])
    with patch as mock_klass:
        query = client.query()
        assert query is mock_klass.return_value
        mock_klass.assert_called_once_with(client, project=PROJECT, namespace=None)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_query_w_explicit(database_id):
    kind = "KIND"
    namespace = "NAMESPACE"
    ancestor = object()
    filters = [("PROPERTY", "==", "VALUE")]
    projection = ["__key__"]
    order = ["PROPERTY"]
    distinct_on = ["DISTINCT_ON"]

    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Query", spec=["__call__"])
    with patch as mock_klass:
        query = client.query(
            kind=kind,
            namespace=namespace,
            ancestor=ancestor,
            filters=filters,
            projection=projection,
            order=order,
            distinct_on=distinct_on,
        )
        assert query is mock_klass.return_value
        mock_klass.assert_called_once_with(
            client,
            project=PROJECT,
            kind=kind,
            namespace=namespace,
            ancestor=ancestor,
            filters=filters,
            projection=projection,
            order=order,
            distinct_on=distinct_on,
        )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_query_w_namespace(database_id):
    kind = "KIND"
    namespace = object()

    creds = _make_credentials()
    client = _make_client(namespace=namespace, credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Query", spec=["__call__"])
    with patch as mock_klass:
        query = client.query(kind=kind)
        assert query is mock_klass.return_value
        mock_klass.assert_called_once_with(
            client, project=PROJECT, namespace=namespace, kind=kind
        )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_query_w_namespace_collision(database_id):
    kind = "KIND"
    namespace1 = object()
    namespace2 = object()

    creds = _make_credentials()
    client = _make_client(namespace=namespace1, credentials=creds, database=database_id)

    patch = mock.patch("google.cloud.datastore.client.Query", spec=["__call__"])
    with patch as mock_klass:
        query = client.query(kind=kind, namespace=namespace2)
        assert query is mock_klass.return_value
        mock_klass.assert_called_once_with(
            client, project=PROJECT, namespace=namespace2, kind=kind
        )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_aggregation_query_w_defaults(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    query = client.query()
    patch = mock.patch(
        "google.cloud.datastore.client.AggregationQuery", spec=["__call__"]
    )
    with patch as mock_klass:
        aggregation_query = client.aggregation_query(query=query)
        assert aggregation_query is mock_klass.return_value
        mock_klass.assert_called_once_with(client, query)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_aggregation_query_w_namespace(database_id):
    namespace = object()

    creds = _make_credentials()
    client = _make_client(namespace=namespace, credentials=creds, database=database_id)
    query = client.query()

    aggregation_query = client.aggregation_query(query=query)
    assert aggregation_query.namespace == namespace


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_aggregation_query_w_namespace_collision(database_id):
    namespace1 = object()
    namespace2 = object()

    creds = _make_credentials()
    client = _make_client(namespace=namespace1, credentials=creds, database=database_id)
    query = client.query(namespace=namespace2)

    aggregation_query = client.aggregation_query(query=query)
    assert aggregation_query.namespace == namespace2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_multi_w_partial_key(database_id):
    incomplete_key = _Key(_Key.kind, None)
    creds = _make_credentials()
    client = _make_client(credentials=creds, database=database_id)
    with pytest.raises(ValueError):
        client.reserve_ids_multi([incomplete_key])


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_client_reserve_ids_multi(database_id):
    creds = _make_credentials()
    client = _make_client(credentials=creds, _use_grpc=False, database=database_id)
    key1 = _Key(_Key.kind, "one", database=database_id)
    key2 = _Key(_Key.kind, "two", database=database_id)
    reserve_ids = mock.Mock()
    ds_api = mock.Mock(reserve_ids=reserve_ids, spec=["reserve_ids"])
    client._datastore_api_internal = ds_api

    client.reserve_ids_multi([key1, key2])

    expected_keys = [key1.to_protobuf(), key2.to_protobuf()]
    expected_request = {"project_id": PROJECT, "keys": expected_keys}
    set_database_id_to_request(expected_request, database_id)
    reserve_ids.assert_called_once_with(request=expected_request)


class _NoCommitBatch(object):
    def __init__(self, client):
        from google.cloud.datastore.batch import Batch

        self._client = client
        self._batch = Batch(client)
        self._batch.begin()

    def __enter__(self):
        self._client._push_batch(self._batch)
        return self._batch

    def __exit__(self, *args):
        self._client._pop_batch()


class _NoCommitTransaction(object):
    def __init__(self, client, transaction_id="TRANSACTION"):
        from google.cloud.datastore.batch import Batch
        from google.cloud.datastore.transaction import Transaction

        self._client = client
        xact = self._transaction = Transaction(client)
        xact._id = transaction_id
        Batch.begin(xact)

    def __enter__(self):
        self._client._push_batch(self._transaction)
        return self._transaction

    def __exit__(self, *args):
        self._client._pop_batch()


class _Entity(dict):
    key = None
    exclude_from_indexes = ()
    _meanings: Dict[str, Any] = {}


class _Key(object):
    kind = "KIND"
    id = 1234
    name = None
    _project = project = PROJECT
    _database = database = None
    _namespace = None

    _key = "KEY"
    _path = None
    _stored = None

    def __init__(self, *flat_path, **kwargs):
        if flat_path:
            self._flat_path = flat_path
            self.kind = flat_path[-2]
            id_or_name = flat_path[-1]
            if isinstance(id_or_name, int):
                self.id = id_or_name
            else:
                self.id = None
                self.name = id_or_name

        else:
            self._flat_path = [self.kind, self.id]

        self.__dict__.update(kwargs)
        self._kw_args = kwargs

    @property
    def is_partial(self):
        return self.id is None and self.name is None

    def to_protobuf(self):
        from google.cloud.datastore_v1.types import entity as entity_pb2

        key = self._key = entity_pb2.Key()

        path = self._flat_path
        while path:
            element = key._pb.path.add()
            kind, id_or_name = path[:2]
            element.kind = kind
            if isinstance(id_or_name, int):
                element.id = id_or_name
            elif id_or_name is not None:
                element.name = id_or_name

            path = path[2:]

        return key

    def completed_key(self, new_id):
        assert self.is_partial

        path = list(self._flat_path)
        path[-1] = new_id

        key_class = type(self)
        new_key = key_class(*path, **self._kw_args)
        return new_key


class _PathElementPB(object):
    def __init__(self, id_):
        self.id = id_


class _KeyPB(object):
    def __init__(self, id_):
        self.path = [_PathElementPB(id_)]


def _mutated_pb(mutation_pb_list, mutation_type):
    assert len(mutation_pb_list) == 1

    # We grab the only mutation.
    mutated_pb = mutation_pb_list[0]
    # Then check if it is the correct type.
    assert mutated_pb._pb.WhichOneof("operation") == mutation_type

    return getattr(mutated_pb, mutation_type)


def _make_key(id_):
    from google.cloud.datastore_v1.types import entity as entity_pb2

    key = entity_pb2.Key()
    elem = key._pb.path.add()
    elem.id = id_
    return key


def _make_commit_response(*keys):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    mutation_results = [datastore_pb2.MutationResult(key=key) for key in keys]
    return datastore_pb2.CommitResponse(mutation_results=mutation_results)


def _make_lookup_response(results=(), missing=(), deferred=(), transaction=None):
    entity_results_found = [
        mock.Mock(entity=result, spec=["entity"]) for result in results
    ]
    entity_results_missing = [
        mock.Mock(entity=missing_entity, spec=["entity"]) for missing_entity in missing
    ]
    return mock.Mock(
        found=entity_results_found,
        missing=entity_results_missing,
        deferred=deferred,
        transaction=transaction,
        spec=["found", "missing", "deferred", "transaction"],
    )


def _make_datastore_api(*keys, **kwargs):
    commit_method = mock.Mock(return_value=_make_commit_response(*keys), spec=[])
    lookup_response = kwargs.pop("lookup_response", _make_lookup_response())
    lookup_method = mock.Mock(return_value=lookup_response, spec=[])
    return mock.Mock(
        commit=commit_method, lookup=lookup_method, spec=["commit", "lookup"]
    )


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_entity_pb(project, kind, integer_id, name=None, str_val=None, database=None):
    from google.cloud.datastore.helpers import _new_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity_pb = entity_pb2.Entity()
    entity_pb.key.partition_id.project_id = project
    entity_pb.key.partition_id.database_id = database
    path_element = entity_pb._pb.key.path.add()
    path_element.kind = kind
    path_element.id = integer_id
    if name is not None and str_val is not None:
        value_pb = _new_value_pb(entity_pb, name)
        value_pb.string_value = str_val

    return entity_pb
