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

import types
from datetime import datetime, timezone

import mock

from tests.unit.v1._test_helpers import DEFAULT_TEST_PROJECT


def _make_collection_reference(*args, **kwargs):
    from google.cloud.firestore_v1.collection import CollectionReference

    return CollectionReference(*args, **kwargs)


def _get_public_methods(klass):
    return set().union(
        *(
            (
                name
                for name, value in class_.__dict__.items()
                if (not name.startswith("_") and isinstance(value, types.FunctionType))
            )
            for class_ in (klass,) + klass.__bases__
        )
    )


def test_query_method_matching():
    from google.cloud.firestore_v1.collection import CollectionReference
    from google.cloud.firestore_v1.query import Query

    query_methods = _get_public_methods(Query)
    collection_methods = _get_public_methods(CollectionReference)
    # Make sure every query method is present on
    # ``CollectionReference``.
    assert query_methods <= collection_methods


def test_collection_aggregation_query():
    from google.cloud.firestore_v1.aggregation import AggregationQuery

    collection_id1 = "rooms"
    document_id = "roomA"
    collection_id2 = "messages"
    client = mock.sentinel.client

    collection = _make_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )

    assert isinstance(collection._aggregation_query(), AggregationQuery)


def test_collection_count():
    collection_id1 = "rooms"
    document_id = "roomA"
    collection_id2 = "messages"
    client = mock.sentinel.client

    collection = _make_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )

    alias = "total"
    aggregation_query = collection.count(alias)

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias == alias


def test_collection_sum():
    collection_id1 = "rooms"
    document_id = "roomA"
    collection_id2 = "messages"
    client = mock.sentinel.client

    collection = _make_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )

    alias = "total"
    field_ref = "someref"
    aggregation_query = collection.sum(field_ref, alias=alias)

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias == alias
    assert aggregation_query._aggregations[0].field_ref == field_ref


def test_collection_avg():
    collection_id1 = "rooms"
    document_id = "roomA"
    collection_id2 = "messages"
    client = mock.sentinel.client

    collection = _make_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )

    alias = "total"
    field_ref = "someref"
    aggregation_query = collection.avg(field_ref, alias=alias)

    assert len(aggregation_query._aggregations) == 1
    assert aggregation_query._aggregations[0].alias == alias
    assert aggregation_query._aggregations[0].field_ref == field_ref


def test_constructor():
    collection_id1 = "rooms"
    document_id = "roomA"
    collection_id2 = "messages"
    client = mock.sentinel.client

    collection = _make_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )
    assert collection._client is client
    expected_path = (collection_id1, document_id, collection_id2)
    assert collection._path == expected_path


def test_add_auto_assigned():
    from google.cloud.firestore_v1 import SERVER_TIMESTAMP
    from google.cloud.firestore_v1._helpers import pbs_for_create
    from google.cloud.firestore_v1.document import DocumentReference
    from google.cloud.firestore_v1.types import document
    from tests.unit.v1 import _test_helpers

    # Create a minimal fake GAPIC add attach it to a real client.
    firestore_api = mock.Mock(spec=["create_document", "commit"])
    write_result = mock.Mock(
        update_time=mock.sentinel.update_time, spec=["update_time"]
    )

    commit_response = mock.Mock(
        write_results=[write_result],
        spec=["write_results", "commit_time"],
        commit_time=mock.sentinel.commit_time,
    )

    firestore_api.commit.return_value = commit_response
    create_doc_response = document.Document()
    firestore_api.create_document.return_value = create_doc_response
    client = _test_helpers.make_client()
    client._firestore_api_internal = firestore_api

    # Actually make a collection.
    collection = _make_collection_reference(
        "grand-parent", "parent", "child", client=client
    )

    # Actually call add() on our collection; include a transform to make
    # sure transforms during adds work.
    document_data = {"been": "here", "now": SERVER_TIMESTAMP}

    patch = mock.patch("google.cloud.firestore_v1.base_collection._auto_id")
    random_doc_id = "DEADBEEF"
    with patch as patched:
        patched.return_value = random_doc_id
        update_time, document_ref = collection.add(document_data)

    # Verify the response and the mocks.
    assert update_time is mock.sentinel.update_time
    assert isinstance(document_ref, DocumentReference)
    assert document_ref._client is client
    expected_path = collection._path + (random_doc_id,)
    assert document_ref._path == expected_path

    write_pbs = pbs_for_create(document_ref._document_path, document_data)
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": write_pbs,
            "transaction": None,
        },
        metadata=client._rpc_metadata,
    )
    # Since we generate the ID locally, we don't call 'create_document'.
    firestore_api.create_document.assert_not_called()


def _write_pb_for_create(document_path, document_data):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import common, document, write

    return write.Write(
        update=document.Document(
            name=document_path, fields=_helpers.encode_dict(document_data)
        ),
        current_document=common.Precondition(exists=False),
    )


def _add_helper(retry=None, timeout=None):
    from google.cloud.firestore_v1 import _helpers as _fs_v1_helpers
    from google.cloud.firestore_v1.document import DocumentReference
    from tests.unit.v1 import _test_helpers

    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = mock.Mock(spec=["commit"])
    write_result = mock.Mock(
        update_time=mock.sentinel.update_time, spec=["update_time"]
    )
    commit_response = mock.Mock(
        write_results=[write_result],
        spec=["write_results", "commit_time"],
        commit_time=mock.sentinel.commit_time,
    )
    firestore_api.commit.return_value = commit_response

    # Attach the fake GAPIC to a real client.
    client = _test_helpers.make_client()
    client._firestore_api_internal = firestore_api

    # Actually make a collection and call add().
    collection = _make_collection_reference("parent", client=client)
    document_data = {"zorp": 208.75, "i-did-not": b"know that"}
    doc_id = "child"

    kwargs = _fs_v1_helpers.make_retry_timeout_kwargs(retry, timeout)
    update_time, document_ref = collection.add(
        document_data, document_id=doc_id, **kwargs
    )

    # Verify the response and the mocks.
    assert update_time is mock.sentinel.update_time
    assert isinstance(document_ref, DocumentReference)
    assert document_ref._client is client
    assert document_ref._path == (collection.id, doc_id)

    write_pb = _write_pb_for_create(document_ref._document_path, document_data)
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": [write_pb],
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


def test_add_explicit_id():
    _add_helper()


def test_add_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _add_helper(retry=retry, timeout=timeout)


def _list_documents_helper(page_size=None, retry=None, timeout=None, read_time=None):
    from google.api_core.page_iterator import Iterator, Page

    from google.cloud.firestore_v1 import _helpers as _fs_v1_helpers
    from google.cloud.firestore_v1.document import DocumentReference
    from google.cloud.firestore_v1.services.firestore.client import FirestoreClient
    from google.cloud.firestore_v1.types.document import Document
    from tests.unit.v1 import _test_helpers

    class _Iterator(Iterator):
        def __init__(self, pages):
            super(_Iterator, self).__init__(client=None)
            self._pages = pages

        def _next_page(self):
            if self._pages:
                page, self._pages = self._pages[0], self._pages[1:]
                return Page(self, page, self.item_to_value)

    client = _test_helpers.make_client()
    template = client._database_string + "/documents/{}"
    document_ids = ["doc-1", "doc-2"]
    documents = [
        Document(name=template.format(document_id)) for document_id in document_ids
    ]
    iterator = _Iterator(pages=[documents])
    api_client = mock.create_autospec(FirestoreClient)
    api_client.list_documents.return_value = iterator
    client._firestore_api_internal = api_client
    collection = _make_collection_reference("collection", client=client)
    kwargs = _fs_v1_helpers.make_retry_timeout_kwargs(retry, timeout)

    if page_size is not None:
        documents = list(
            collection.list_documents(
                page_size=page_size,
                **kwargs,
                read_time=read_time,
            )
        )
    else:
        documents = list(collection.list_documents(**kwargs, read_time=read_time))

    # Verify the response and the mocks.
    assert len(documents) == len(document_ids)
    for document, document_id in zip(documents, document_ids):
        assert isinstance(document, DocumentReference)
        assert document.parent == collection
        assert document.id == document_id

    parent, _ = collection._parent_info()
    expected_request = {
        "parent": parent,
        "collection_id": collection.id,
        "page_size": page_size,
        "show_missing": True,
        "mask": {"field_paths": None},
    }
    if read_time is not None:
        expected_request["read_time"] = read_time

    api_client.list_documents.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


def test_list_documents_wo_page_size():
    _list_documents_helper()


def test_list_documents_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _list_documents_helper(retry=retry, timeout=timeout)


def test_list_documents_w_page_size():
    _list_documents_helper(page_size=25)


def test_list_documents_w_read_time():
    _list_documents_helper(read_time=datetime.now())


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_get(query_class):
    collection = _make_collection_reference("collection")
    get_response = collection.get()

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value

    assert get_response is query_instance.get.return_value
    query_instance.get.assert_called_once_with(transaction=None)


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_get_w_retry_timeout(query_class):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    collection = _make_collection_reference("collection")
    get_response = collection.get(retry=retry, timeout=timeout)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value

    assert get_response is query_instance.get.return_value
    query_instance.get.assert_called_once_with(
        transaction=None,
        retry=retry,
        timeout=timeout,
    )


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_get_with_transaction(query_class):
    collection = _make_collection_reference("collection")
    transaction = mock.sentinel.txn
    get_response = collection.get(transaction=transaction)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value

    assert get_response is query_instance.get.return_value
    query_instance.get.assert_called_once_with(transaction=transaction)


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_get_w_explain_options(query_class):
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    collection = _make_collection_reference("collection")
    get_response = collection.get(explain_options=explain_options)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value

    assert get_response is query_instance.get.return_value
    query_instance.get.assert_called_once_with(
        transaction=None,
        explain_options=explain_options,
    )


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_get_w_read_time(query_class):
    read_time = datetime.now(tz=timezone.utc)
    collection = _make_collection_reference("collection")
    get_response = collection.get(read_time=read_time)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value

    assert get_response is query_instance.get.return_value
    query_instance.get.assert_called_once_with(
        transaction=None,
        read_time=read_time,
    )


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_stream(query_class):
    collection = _make_collection_reference("collection")
    stream_response = collection.stream()

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value
    assert stream_response is query_instance.stream.return_value
    query_instance.stream.assert_called_once_with(transaction=None)


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_stream_w_retry_timeout(query_class):
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    collection = _make_collection_reference("collection")
    stream_response = collection.stream(retry=retry, timeout=timeout)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value
    assert stream_response is query_instance.stream.return_value
    query_instance.stream.assert_called_once_with(
        transaction=None,
        retry=retry,
        timeout=timeout,
    )


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_stream_with_transaction(query_class):
    collection = _make_collection_reference("collection")
    transaction = mock.sentinel.txn
    stream_response = collection.stream(transaction=transaction)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value
    assert stream_response is query_instance.stream.return_value
    query_instance.stream.assert_called_once_with(transaction=transaction)


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_stream_w_explain_options(query_class):
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    explain_options = ExplainOptions(analyze=True)
    collection = _make_collection_reference("collection")
    get_response = collection.stream(explain_options=explain_options)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value

    assert get_response is query_instance.stream.return_value
    query_instance.stream.assert_called_once_with(
        transaction=None,
        explain_options=explain_options,
    )


@mock.patch("google.cloud.firestore_v1.query.Query", autospec=True)
def test_stream_w_read_time(query_class):
    read_time = datetime.now(tz=timezone.utc)
    collection = _make_collection_reference("collection")
    get_response = collection.stream(read_time=read_time)

    query_class.assert_called_once_with(collection)
    query_instance = query_class.return_value

    assert get_response is query_instance.stream.return_value
    query_instance.stream.assert_called_once_with(
        transaction=None,
        read_time=read_time,
    )


def test_collectionreference_pipeline():
    from google.cloud.firestore_v1.pipeline import Pipeline
    from google.cloud.firestore_v1.pipeline_stages import Collection
    from tests.unit.v1 import _test_helpers

    client = _test_helpers.make_client()
    collection = _make_collection_reference("collection", client=client)
    pipeline = collection._build_pipeline(client.pipeline())
    assert isinstance(pipeline, Pipeline)
    # should have single "Collection" stage
    assert len(pipeline.stages) == 1
    assert isinstance(pipeline.stages[0], Collection)
    assert pipeline.stages[0].path == "/collection"


@mock.patch("google.cloud.firestore_v1.collection.Watch", autospec=True)
def test_on_snapshot(watch):
    collection = _make_collection_reference("collection")
    collection.on_snapshot(None)
    watch.for_query.assert_called_once()


def test_recursive():
    from google.cloud.firestore_v1.query import Query

    col = _make_collection_reference("collection")
    assert isinstance(col.recursive(), Query)


def test_chunkify():
    from google.cloud.firestore_v1.types.document import Document
    from google.cloud.firestore_v1.types.firestore import RunQueryResponse
    from tests.unit.v1 import _test_helpers

    client = _test_helpers.make_client()
    col = client.collection("my-collection")

    client._firestore_api_internal = mock.Mock(spec=["run_query"])

    results = []
    for index in range(10):
        results.append(
            RunQueryResponse(
                document=Document(
                    name=f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/my-collection/{index}",
                ),
            ),
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

    counter = 0
    expected_lengths = [3, 3, 3, 1]
    for chunk in col._chunkify(3):
        assert len(chunk) == expected_lengths[counter]
        counter += 1
