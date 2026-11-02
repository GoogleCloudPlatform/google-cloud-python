# Copyright 2017 Google LLC All rights reserved.
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


from datetime import datetime

import mock
import pytest
from google.protobuf import timestamp_pb2

from tests.unit.v1._test_helpers import DEFAULT_TEST_PROJECT


def _make_document_reference(*args, **kwargs):
    from google.cloud.firestore_v1.document import DocumentReference

    return DocumentReference(*args, **kwargs)


def test_constructor():
    collection_id1 = "users"
    document_id1 = "alovelace"
    collection_id2 = "platform"
    document_id2 = "*nix"
    client = mock.MagicMock()
    client.__hash__.return_value = 1234

    document = _make_document_reference(
        collection_id1, document_id1, collection_id2, document_id2, client=client
    )
    assert document._client is client
    expected_path = "/".join(
        (collection_id1, document_id1, collection_id2, document_id2)
    )
    assert document.path == expected_path


def _make_commit_repsonse(write_results=None):
    from google.cloud.firestore_v1.types import firestore

    response = mock.create_autospec(firestore.CommitResponse)
    response.write_results = write_results or [mock.sentinel.write_result]
    response.commit_time = mock.sentinel.commit_time
    return response


def _write_pb_for_create(document_path, document_data):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import common, document, write

    return write.Write(
        update=document.Document(
            name=document_path, fields=_helpers.encode_dict(document_data)
        ),
        current_document=common.Precondition(exists=False),
    )


def _create_helper(retry=None, timeout=None, database=None):
    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = mock.Mock()
    firestore_api.commit.mock_add_spec(spec=["commit"])
    firestore_api.commit.return_value = _make_commit_repsonse()

    # Attach the fake GAPIC to a real client.
    client = _make_client("dignity", database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a document and call create().
    document = _make_document_reference("foo", "twelve", client=client)
    document_data = {"hello": "goodbye", "count": 99}
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    write_result = document.create(document_data, **kwargs)

    # Verify the response and the mocks.
    assert write_result is mock.sentinel.write_result
    write_pb = _write_pb_for_create(document._document_path, document_data)
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": [write_pb],
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_create(database):
    _create_helper(database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_create_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _create_helper(retry=retry, timeout=timeout, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_create_empty(database):
    # Create a minimal fake GAPIC with a dummy response.
    from google.cloud.firestore_v1.document import DocumentReference, DocumentSnapshot

    firestore_api = mock.Mock(spec=["commit"])
    document_reference = mock.create_autospec(DocumentReference)
    snapshot = mock.create_autospec(DocumentSnapshot)
    snapshot.exists = True
    document_reference.get.return_value = snapshot
    firestore_api.commit.return_value = _make_commit_repsonse(
        write_results=[document_reference]
    )

    # Attach the fake GAPIC to a real client.
    client = _make_client("dignity", database=database)
    client._firestore_api_internal = firestore_api
    client.get_all = mock.MagicMock()
    client.get_all.exists.return_value = True

    # Actually make a document and call create().
    document = _make_document_reference("foo", "twelve", client=client)
    document_data = {}
    write_result = document.create(document_data)
    assert write_result.get().exists


def _write_pb_for_set(document_path, document_data, merge):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import common, document, write

    write_pbs = write.Write(
        update=document.Document(
            name=document_path, fields=_helpers.encode_dict(document_data)
        )
    )
    if merge:
        field_paths = [
            field_path
            for field_path, value in _helpers.extract_fields(
                document_data, _helpers.FieldPath()
            )
        ]
        field_paths = [field_path.to_api_repr() for field_path in sorted(field_paths)]
        mask = common.DocumentMask(field_paths=sorted(field_paths))
        write_pbs._pb.update_mask.CopyFrom(mask._pb)
    return write_pbs


def _set_helper(merge=False, retry=None, timeout=None, database=None, **option_kwargs):
    from google.cloud.firestore_v1 import _helpers

    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = mock.Mock(spec=["commit"])
    firestore_api.commit.return_value = _make_commit_repsonse()

    # Attach the fake GAPIC to a real client.
    client = _make_client("db-dee-bee", database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a document and call create().
    document = _make_document_reference("User", "Interface", client=client)
    document_data = {"And": 500, "Now": b"\xba\xaa\xaa \xba\xaa\xaa"}
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    write_result = document.set(document_data, merge, **kwargs)

    # Verify the response and the mocks.
    assert write_result is mock.sentinel.write_result
    write_pb = _write_pb_for_set(document._document_path, document_data, merge)

    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": [write_pb],
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_set(database):
    _set_helper(database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_set_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _set_helper(retry=retry, timeout=timeout, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_set_merge(database):
    _set_helper(merge=True, database=database)


def _write_pb_for_update(document_path, update_values, field_paths):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import common, document, write

    return write.Write(
        update=document.Document(
            name=document_path, fields=_helpers.encode_dict(update_values)
        ),
        update_mask=common.DocumentMask(field_paths=field_paths),
        current_document=common.Precondition(exists=True),
    )


def _update_helper(retry=None, timeout=None, database=None, **option_kwargs):
    from collections import OrderedDict

    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.transforms import DELETE_FIELD

    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = mock.Mock(spec=["commit"])
    firestore_api.commit.return_value = _make_commit_repsonse()

    # Attach the fake GAPIC to a real client.
    client = _make_client("potato-chip", database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a document and call create().
    document = _make_document_reference("baked", "Alaska", client=client)
    # "Cheat" and use OrderedDict-s so that iteritems() is deterministic.
    field_updates = OrderedDict(
        (("hello", 1), ("then.do", False), ("goodbye", DELETE_FIELD))
    )
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    if option_kwargs:
        option = client.write_option(**option_kwargs)
        write_result = document.update(field_updates, option=option, **kwargs)
    else:
        option = None
        write_result = document.update(field_updates, **kwargs)

    # Verify the response and the mocks.
    assert write_result is mock.sentinel.write_result
    update_values = {
        "hello": field_updates["hello"],
        "then": {"do": field_updates["then.do"]},
    }
    field_paths = list(field_updates.keys())
    write_pb = _write_pb_for_update(
        document._document_path, update_values, sorted(field_paths)
    )
    if option is not None:
        option.modify_write(write_pb)
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": [write_pb],
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_update_with_exists(database):
    with pytest.raises(ValueError):
        _update_helper(exists=True, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_update(database):
    _update_helper(database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_update_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _update_helper(retry=retry, timeout=timeout, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_update_with_precondition(database):
    from google.protobuf import timestamp_pb2

    timestamp = timestamp_pb2.Timestamp(seconds=1058655101, nanos=100022244)
    _update_helper(last_update_time=timestamp, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_empty_update(database):
    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = mock.Mock(spec=["commit"])
    firestore_api.commit.return_value = _make_commit_repsonse()

    # Attach the fake GAPIC to a real client.
    client = _make_client("potato-chip", database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a document and call create().
    document = _make_document_reference("baked", "Alaska", client=client)
    # "Cheat" and use OrderedDict-s so that iteritems() is deterministic.
    field_updates = {}
    with pytest.raises(ValueError):
        document.update(field_updates)


def _delete_helper(retry=None, timeout=None, database=None, **option_kwargs):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import write

    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = mock.Mock(spec=["commit"])
    firestore_api.commit.return_value = _make_commit_repsonse()

    # Attach the fake GAPIC to a real client.
    client = _make_client("donut-base", database=database)
    client._firestore_api_internal = firestore_api
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Actually make a document and call delete().
    document = _make_document_reference("where", "we-are", client=client)
    if option_kwargs:
        option = client.write_option(**option_kwargs)
        delete_time = document.delete(option=option, **kwargs)
    else:
        option = None
        delete_time = document.delete(**kwargs)

    # Verify the response and the mocks.
    assert delete_time is mock.sentinel.commit_time
    write_pb = write.Write(delete=document._document_path)
    if option is not None:
        option.modify_write(write_pb)
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": [write_pb],
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_delete(database):
    _delete_helper(database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_delete_with_option(database):
    from google.protobuf import timestamp_pb2

    timestamp_pb = timestamp_pb2.Timestamp(seconds=1058655101, nanos=100022244)
    _delete_helper(last_update_time=timestamp_pb, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_delete_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _delete_helper(retry=retry, timeout=timeout, database=database)


def _get_helper(
    field_paths=None,
    use_transaction=False,
    not_found=False,
    # This should be an impossible case, but we test against it for
    # completeness
    return_empty=False,
    retry=None,
    timeout=None,
    database=None,
    read_time=None,
):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.transaction import Transaction
    from google.cloud.firestore_v1.types import common, document, firestore

    # Create a minimal fake GAPIC with a dummy response.
    create_time = 123
    update_time = 234
    if read_time:
        response_read_time = timestamp_pb2.Timestamp()
        response_read_time.FromDatetime(read_time)
    else:
        response_read_time = 345
    firestore_api = mock.Mock(spec=["batch_get_documents"])
    response = mock.create_autospec(firestore.BatchGetDocumentsResponse)
    response.read_time = response_read_time
    response.found = mock.create_autospec(document.Document)
    response.found.fields = {}
    response.found.create_time = create_time
    response.found.update_time = update_time

    client = _make_client("donut-base", database=database)
    client._firestore_api_internal = firestore_api
    document_reference = _make_document_reference("where", "we-are", client=client)

    response.found.name = None if not_found else document_reference._document_path
    response.missing = document_reference._document_path if not_found else None

    def WhichOneof(val):
        return "missing" if not_found else "found"

    response._pb = response
    response._pb.WhichOneof = WhichOneof
    firestore_api.batch_get_documents.return_value = iter(
        [response] if not return_empty else []
    )

    if use_transaction:
        transaction = Transaction(client)
        transaction_id = transaction._id = b"asking-me-2"
    else:
        transaction = None

    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    snapshot = document_reference.get(
        field_paths=field_paths,
        transaction=transaction,
        **kwargs,
        read_time=read_time,
    )

    assert snapshot.reference is document_reference
    if not_found or return_empty:
        assert snapshot._data is None
        assert not snapshot.exists
        assert snapshot.read_time is not None
        assert snapshot.create_time is None
        assert snapshot.update_time is None
    else:
        assert snapshot.to_dict() == {}
        assert snapshot.exists
        assert snapshot.read_time is response_read_time
        assert snapshot.create_time is create_time
        assert snapshot.update_time is update_time

    # Verify the request made to the API
    if field_paths is not None:
        mask = common.DocumentMask(field_paths=sorted(field_paths))
    else:
        mask = None

    if use_transaction:
        expected_transaction_id = transaction_id
    else:
        expected_transaction_id = None

    expected_request = {
        "database": client._database_string,
        "documents": [document_reference._document_path],
        "mask": mask,
        "transaction": expected_transaction_id,
    }
    if read_time is not None:
        expected_request["read_time"] = read_time

    firestore_api.batch_get_documents.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_not_found(database):
    _get_helper(not_found=True, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_default(database):
    _get_helper(database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_return_empty(database):
    _get_helper(return_empty=True, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _get_helper(retry=retry, timeout=timeout, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_w_string_field_path(database):
    with pytest.raises(ValueError):
        _get_helper(field_paths="foo", database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_with_field_path(database):
    _get_helper(field_paths=["foo"], database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_with_multiple_field_paths(database):
    _get_helper(field_paths=["foo", "bar.baz"], database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_with_transaction(database):
    _get_helper(use_transaction=True, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_get_with_read_time(database):
    _get_helper(read_time=datetime.now(), database=database)


def _collections_helper(
    page_size=None, retry=None, timeout=None, read_time=None, database=None
):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.collection import CollectionReference
    from google.cloud.firestore_v1.services.firestore.client import FirestoreClient

    collection_ids = ["coll-1", "coll-2"]

    class Pager(object):
        def __iter__(self):
            yield from collection_ids

    api_client = mock.create_autospec(FirestoreClient)
    api_client.list_collection_ids.return_value = Pager()

    client = _make_client(database=database)
    client._firestore_api_internal = api_client
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Actually make a document and call delete().
    document = _make_document_reference("where", "we-are", client=client)
    if page_size is not None:
        collections = list(
            document.collections(page_size=page_size, **kwargs, read_time=read_time)
        )
    else:
        collections = list(document.collections(**kwargs, read_time=read_time))

    # Verify the response and the mocks.
    assert len(collections) == len(collection_ids)
    for collection, collection_id in zip(collections, collection_ids):
        assert isinstance(collection, CollectionReference)
        assert collection.parent == document
        assert collection.id == collection_id

    expected_result = {
        "parent": document._document_path,
        "page_size": page_size,
    }
    if read_time is not None:
        expected_result["read_time"] = read_time

    api_client.list_collection_ids.assert_called_once_with(
        request=expected_result,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_collections_wo_page_size(database):
    _collections_helper(database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_collections_w_page_size(database):
    _collections_helper(page_size=10, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_collections_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _collections_helper(retry=retry, timeout=timeout, database=database)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_documentreference_collections_w_read_time(database):
    _collections_helper(read_time=datetime.now(), database=database)


@mock.patch("google.cloud.firestore_v1.document.Watch", autospec=True)
def test_documentreference_on_snapshot(watch):
    client = mock.Mock(_database_string="sprinklez", spec=["_database_string"])
    document = _make_document_reference("yellow", "mellow", client=client)
    document.on_snapshot(None)
    watch.for_document.assert_called_once()


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client(project=DEFAULT_TEST_PROJECT, database=None):
    from google.cloud.firestore_v1.client import Client

    credentials = _make_credentials()
    return Client(project=project, credentials=credentials, database=database)
