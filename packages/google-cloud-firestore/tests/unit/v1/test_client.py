# Copyright 2020 Google LLC All rights reserved.
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

import datetime
import types

import mock
import pytest

from google.cloud.firestore_v1.base_client import (
    _DEFAULT_EMULATOR_PROJECT,
    DEFAULT_DATABASE,
)

PROJECT = "my-prahjekt"


def _make_client(*args, **kwargs):
    from google.cloud.firestore_v1.client import Client

    return Client(*args, **kwargs)


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_default_client(*args, **kwargs):
    credentials = _make_credentials()
    database = kwargs.get("database", None)
    return _make_client(project=PROJECT, credentials=credentials, database=database)


@pytest.mark.parametrize(
    "database, expected",
    [
        (None, DEFAULT_DATABASE),
        (DEFAULT_DATABASE, DEFAULT_DATABASE),
        ("somedb", "somedb"),
    ],
)
def test_client_constructor_defaults(database, expected):
    from google.cloud.firestore_v1.client import _CLIENT_INFO

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, database=database)
    assert client.project == PROJECT
    assert client._credentials == credentials
    assert client._database == expected
    assert client._client_info is _CLIENT_INFO


def test_client_constructor_without_db():
    from google.cloud.firestore_v1.client import _CLIENT_INFO

    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials)
    assert client.project == PROJECT
    assert client._credentials == credentials
    assert client._database == DEFAULT_DATABASE
    assert client._client_info is _CLIENT_INFO


@pytest.mark.parametrize(
    "database, expected",
    [
        (None, DEFAULT_DATABASE),
        (DEFAULT_DATABASE, DEFAULT_DATABASE),
        ("somedb", "somedb"),
    ],
)
def test_client_constructor_explicit(database, expected):
    from google.api_core.client_options import ClientOptions

    credentials = _make_credentials()

    client_info = mock.Mock()
    client_options = ClientOptions("endpoint")
    client = _make_client(
        project=PROJECT,
        credentials=credentials,
        database=database,
        client_info=client_info,
        client_options=client_options,
    )
    assert client.project == PROJECT
    assert client._credentials == credentials
    assert client._database == expected
    assert client._client_info is client_info
    assert client._client_options is client_options


@pytest.mark.parametrize(
    "extra_env,project_expected",
    [
        ({}, _DEFAULT_EMULATOR_PROJECT),
        ({"GCLOUD_PROJECT": "gcloud"}, "gcloud"),
        ({"GOOGLE_CLOUD_PROJECT": "google"}, "google"),
        ({"GCLOUD_PROJECT": "gcloud", "GOOGLE_CLOUD_PROJECT": "google"}, "google"),
    ],
)
def test_client_constructor_emulator(extra_env, project_expected):
    """
    Ensure client can be configured with FIRESOTRE_EMULATOR_HOST environment variable

    If project is not set, should be detected from GCLOUD_PROJECT or GOOGLE_CLOUD_PROJECT
    """
    expected_host = "localhost:8080"
    environment = {"FIRESTORE_EMULATOR_HOST": expected_host}
    if extra_env:
        environment.update(extra_env)

    with mock.patch("os.environ", environment):
        client = _make_client()
        assert client._emulator_host == expected_host
        assert client.project == project_expected


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client__firestore_api_property(database):
    credentials = _make_credentials()
    client = _make_client(project=PROJECT, credentials=credentials, database=database)
    helper = client._firestore_api_helper = mock.Mock()

    g_patch = mock.patch("google.cloud.firestore_v1.client.firestore_grpc_transport")
    f_patch = mock.patch("google.cloud.firestore_v1.client.firestore_client")

    with g_patch as grpc_transport:
        with f_patch as firestore_client:
            api = client._firestore_api

    assert api is helper.return_value

    helper.assert_called_once_with(
        grpc_transport.FirestoreGrpcTransport,
        firestore_client.FirestoreClient,
        firestore_client,
    )


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_constructor_w_client_options(database):
    credentials = _make_credentials()
    client = _make_client(
        project=PROJECT,
        credentials=credentials,
        client_options={"api_endpoint": "foo-firestore.googleapis.com"},
        database=database,
    )
    assert client._target == "foo-firestore.googleapis.com"


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_collection_factory(database):
    from google.cloud.firestore_v1.collection import CollectionReference

    collection_id = "users"
    client = _make_default_client(database=database)
    collection = client.collection(collection_id)

    assert collection._path == (collection_id,)
    assert collection._client is client
    assert isinstance(collection, CollectionReference)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_collection_factory_nested(database):
    from google.cloud.firestore_v1.collection import CollectionReference

    client = _make_default_client(database=database)
    parts = ("users", "alovelace", "beep")
    collection_path = "/".join(parts)
    collection1 = client.collection(collection_path)

    assert collection1._path == parts
    assert collection1._client is client
    assert isinstance(collection1, CollectionReference)

    # Make sure using segments gives the same result.
    collection2 = client.collection(*parts)
    assert collection2._path == parts
    assert collection2._client is client
    assert isinstance(collection2, CollectionReference)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client__get_collection_reference(database):
    from google.cloud.firestore_v1.collection import CollectionReference

    client = _make_default_client(database=database)
    collection = client._get_collection_reference("collectionId")

    assert collection._client is client
    assert isinstance(collection, CollectionReference)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_collection_group(database):
    client = _make_default_client(database=database)
    query = client.collection_group("collectionId").where("foo", "==", "bar")

    assert query._all_descendants
    assert query._field_filters[0].field.field_path == "foo"
    assert query._field_filters[0].value.string_value == "bar"
    assert query._field_filters[0].op == query._field_filters[0].Operator.EQUAL
    assert query._parent.id == "collectionId"


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_collection_group_no_slashes(database):
    client = _make_default_client(database=database)
    with pytest.raises(ValueError):
        client.collection_group("foo/bar")


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_document_factory(database):
    from google.cloud.firestore_v1.document import DocumentReference

    parts = ("rooms", "roomA")
    client = _make_default_client(database=database)
    doc_path = "/".join(parts)
    document1 = client.document(doc_path)

    assert document1._path == parts
    assert document1._client is client
    assert isinstance(document1, DocumentReference)

    # Make sure using segments gives the same result.
    document2 = client.document(*parts)
    assert document2._path == parts
    assert document2._client is client
    assert isinstance(document2, DocumentReference)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_document_factory_w_absolute_path(database):
    from google.cloud.firestore_v1.document import DocumentReference

    parts = ("rooms", "roomA")
    client = _make_default_client(database=database)
    doc_path = "/".join(parts)
    to_match = client.document(doc_path)
    document1 = client.document(to_match._document_path)

    assert document1._path == parts
    assert document1._client is client
    assert isinstance(document1, DocumentReference)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_document_factory_w_nested_path(database):
    from google.cloud.firestore_v1.document import DocumentReference

    client = _make_default_client(database=database)
    parts = ("rooms", "roomA", "shoes", "dressy")
    doc_path = "/".join(parts)
    document1 = client.document(doc_path)

    assert document1._path == parts
    assert document1._client is client
    assert isinstance(document1, DocumentReference)

    # Make sure using segments gives the same result.
    document2 = client.document(*parts)
    assert document2._path == parts
    assert document2._client is client
    assert isinstance(document2, DocumentReference)


def _collections_helper(retry=None, timeout=None, database=None, read_time=None):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.collection import CollectionReference

    collection_ids = ["users", "projects"]

    class Pager(object):
        def __iter__(self):
            yield from collection_ids

    firestore_api = mock.Mock(spec=["list_collection_ids"])
    firestore_api.list_collection_ids.return_value = Pager()

    client = _make_default_client(database=database)
    client._firestore_api_internal = firestore_api
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    collections = list(client.collections(read_time=read_time, **kwargs))

    assert len(collections) == len(collection_ids)
    for collection, collection_id in zip(collections, collection_ids):
        assert isinstance(collection, CollectionReference)
        assert collection.parent is None
        assert collection.id == collection_id

    base_path = client._database_string + "/documents"
    expected_request = {
        "parent": base_path,
    }
    if read_time is not None:
        expected_request["read_time"] = read_time
    firestore_api.list_collection_ids.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_collections(database):
    _collections_helper(database=database)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_collections_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _collections_helper(retry=retry, timeout=timeout, database=database)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_collections_read_time(database):
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)
    _collections_helper(database=database, read_time=read_time)


def _invoke_get_all(client, references, document_pbs, **kwargs):
    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = mock.Mock(spec=["batch_get_documents"])
    response_iterator = iter(document_pbs)
    firestore_api.batch_get_documents.return_value = response_iterator

    # Attach the fake GAPIC to a real client.
    client._firestore_api_internal = firestore_api

    # Actually call get_all().
    snapshots = client.get_all(references, **kwargs)
    assert isinstance(snapshots, types.GeneratorType)

    return list(snapshots)


def _get_all_helper(
    num_snapshots=2,
    txn_id=None,
    retry=None,
    timeout=None,
    database=None,
    read_time=None,
):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.async_document import DocumentSnapshot
    from google.cloud.firestore_v1.types import common

    client = _make_default_client(database=database)

    data1 = {"a": "cheese"}
    document1 = client.document("pineapple", "lamp1")
    document_pb1, doc_read_time = _doc_get_info(document1._document_path, data1)
    response1 = _make_batch_response(found=document_pb1, read_time=doc_read_time)

    data2 = {"b": True, "c": 18}
    document2 = client.document("pineapple", "lamp2")
    document, doc_read_time = _doc_get_info(document2._document_path, data2)
    response2 = _make_batch_response(found=document, read_time=doc_read_time)

    document3 = client.document("pineapple", "lamp3")
    response3 = _make_batch_response(missing=document3._document_path)

    expected_data = [data1, data2, None][:num_snapshots]
    documents = [document1, document2, document3][:num_snapshots]
    responses = [response1, response2, response3][:num_snapshots]
    field_paths = [
        field_path for field_path in ["a", "b", None][:num_snapshots] if field_path
    ]
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    if txn_id is not None:
        transaction = client.transaction()
        transaction._id = txn_id
        kwargs["transaction"] = transaction

    snapshots = _invoke_get_all(
        client,
        documents,
        responses,
        field_paths=field_paths,
        read_time=read_time,
        **kwargs,
    )

    assert len(snapshots) == num_snapshots

    for data, document, snapshot in zip(expected_data, documents, snapshots):
        assert isinstance(snapshot, DocumentSnapshot)
        assert snapshot._reference is document
        if data is None:
            assert not snapshot.exists
        else:
            assert snapshot._data == data

    # Verify the call to the mock.
    doc_paths = [document._document_path for document in documents]
    mask = common.DocumentMask(field_paths=field_paths)

    kwargs.pop("transaction", None)
    expected_request = {
        "database": client._database_string,
        "documents": doc_paths,
        "mask": mask,
        "transaction": txn_id,
    }
    if read_time is not None:
        expected_request["read_time"] = read_time

    client._firestore_api.batch_get_documents.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_get_all(database):
    _get_all_helper(database=database)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_get_all_with_transaction(database):
    txn_id = b"the-man-is-non-stop"
    _get_all_helper(num_snapshots=1, txn_id=txn_id, database=database)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_get_all_w_retry_timeout(database):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _get_all_helper(retry=retry, timeout=timeout, database=database)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_get_all_wrong_order(database):
    _get_all_helper(num_snapshots=3, database=database)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_get_all_read_time(database):
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)
    _get_all_helper(database=database, read_time=read_time)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_get_all_unknown_result(database):
    from google.cloud.firestore_v1.base_client import _BAD_DOC_TEMPLATE

    client = _make_default_client(database=database)

    expected_document = client.document("pineapple", "lamp1")

    data = {"z": 28.5}
    wrong_document = client.document("pineapple", "lamp2")
    document_pb, read_time = _doc_get_info(wrong_document._document_path, data)
    response = _make_batch_response(found=document_pb, read_time=read_time)

    # Exercise the mocked ``batch_get_documents``.
    with pytest.raises(ValueError) as exc_info:
        _invoke_get_all(client, [expected_document], [response])

    err_msg = _BAD_DOC_TEMPLATE.format(response.found.name)
    assert exc_info.value.args == (err_msg,)

    # Verify the call to the mock.
    doc_paths = [expected_document._document_path]
    client._firestore_api.batch_get_documents.assert_called_once_with(
        request={
            "database": client._database_string,
            "documents": doc_paths,
            "mask": None,
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_recursive_delete(database):
    from google.cloud.firestore_v1.types import document, firestore

    client = _make_default_client(database=database)
    client._firestore_api_internal = mock.Mock(spec=["run_query"])
    collection_ref = client.collection("my_collection")

    results = []
    for index in range(10):
        results.append(
            firestore.RunQueryResponse(
                document=document.Document(name=f"{collection_ref.id}/{index}")
            )
        )

    chunks = [
        results[:3],
        results[3:6],
        results[6:9],
        results[9:],
    ]

    def _get_chunk(*args, **kwargs):
        return iter(chunks.pop(0))

    client._firestore_api_internal.run_query.side_effect = _get_chunk

    bulk_writer = mock.MagicMock()
    bulk_writer.mock_add_spec(spec=["delete", "close"])

    num_deleted = client.recursive_delete(
        collection_ref, bulk_writer=bulk_writer, chunk_size=3
    )
    assert num_deleted == len(results)


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_recursive_delete_from_document(database):
    from google.cloud.firestore_v1.types import document, firestore

    client = _make_default_client(database=database)
    client._firestore_api_internal = mock.Mock(
        spec=["run_query", "list_collection_ids"]
    )
    collection_ref = client.collection("my_collection")

    collection_1_id: str = "collection_1_id"
    collection_2_id: str = "collection_2_id"

    parent_doc = collection_ref.document("parent")

    collection_1_results = []
    collection_2_results = []

    for index in range(10):
        collection_1_results.append(
            firestore.RunQueryResponse(
                document=document.Document(name=f"{collection_1_id}/{index}"),
            ),
        )

        collection_2_results.append(
            firestore.RunQueryResponse(
                document=document.Document(name=f"{collection_2_id}/{index}"),
            ),
        )

    col_1_chunks = [
        collection_1_results[:3],
        collection_1_results[3:6],
        collection_1_results[6:9],
        collection_1_results[9:],
    ]

    col_2_chunks = [
        collection_2_results[:3],
        collection_2_results[3:6],
        collection_2_results[6:9],
        collection_2_results[9:],
    ]

    def _get_chunk(*args, **kwargs):
        start_at = (
            kwargs["request"]["structured_query"].start_at.values[0].reference_value
        )

        if collection_1_id in start_at:
            return iter(col_1_chunks.pop(0))
        return iter(col_2_chunks.pop(0))

    client._firestore_api_internal.run_query.side_effect = _get_chunk
    client._firestore_api_internal.list_collection_ids.return_value = [
        collection_1_id,
        collection_2_id,
    ]

    bulk_writer = mock.MagicMock()
    bulk_writer.mock_add_spec(spec=["delete", "close"])

    num_deleted = client.recursive_delete(
        parent_doc, bulk_writer=bulk_writer, chunk_size=3
    )

    expected_len = len(collection_1_results) + len(collection_2_results) + 1
    assert num_deleted == expected_len


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_recursive_delete_raises(database):
    client = _make_default_client(database=database)
    with pytest.raises(TypeError):
        client.recursive_delete(object())


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_batch(database):
    from google.cloud.firestore_v1.batch import WriteBatch

    client = _make_default_client(database=database)
    batch = client.batch()
    assert isinstance(batch, WriteBatch)
    assert batch._client is client
    assert batch._write_pbs == []


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_bulk_writer(database):
    from google.cloud.firestore_v1.bulk_writer import BulkWriter

    client = _make_default_client(database=database)
    bulk_writer = client.bulk_writer()
    assert isinstance(bulk_writer, BulkWriter)
    assert bulk_writer._client is client


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_transaction(database):
    from google.cloud.firestore_v1.transaction import Transaction

    client = _make_default_client(database=database)
    transaction = client.transaction(max_attempts=3, read_only=True)
    assert isinstance(transaction, Transaction)
    assert transaction._write_pbs == []
    assert transaction._max_attempts == 3
    assert transaction._read_only
    assert transaction._id is None


@pytest.mark.parametrize("database", [None, DEFAULT_DATABASE, "somedb"])
def test_client_pipeline(database):
    from google.cloud.firestore_v1.pipeline import Pipeline
    from google.cloud.firestore_v1.pipeline_source import PipelineSource

    client = _make_default_client(database=database)
    ppl = client.pipeline()
    assert client._pipeline_cls == Pipeline
    assert isinstance(ppl, PipelineSource)
    assert ppl.client == client


def _make_batch_response(**kwargs):
    from google.cloud.firestore_v1.types import firestore

    return firestore.BatchGetDocumentsResponse(**kwargs)


def _doc_get_info(ref_string, values):
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import document

    now = datetime.datetime.now(tz=datetime.timezone.utc)
    read_time = _datetime_to_pb_timestamp(now)
    delta = datetime.timedelta(seconds=100)
    update_time = _datetime_to_pb_timestamp(now - delta)
    create_time = _datetime_to_pb_timestamp(now - 2 * delta)

    document_pb = document.Document(
        name=ref_string,
        fields=_helpers.encode_dict(values),
        create_time=create_time,
        update_time=update_time,
    )

    return document_pb, read_time
