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

import mock
import pytest

from tests.unit.v1._test_helpers import DEFAULT_TEST_PROJECT


def _make_base_collection_reference(*args, **kwargs):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    return BaseCollectionReference(*args, **kwargs)


def test_basecollectionreference_ctor():
    collection_id1 = "rooms"
    document_id = "roomA"
    collection_id2 = "messages"
    client = mock.sentinel.client

    collection = _make_base_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )
    assert collection._client is client
    expected_path = (collection_id1, document_id, collection_id2)
    assert collection._path == expected_path


def test_basecollectionreference_ctor_invalid_path_empty():
    with pytest.raises(ValueError):
        _make_base_collection_reference()


def test_basecollectionreference_ctor_invalid_path_bad_collection_id():
    with pytest.raises(ValueError):
        _make_base_collection_reference(99, "doc", "bad-collection-id")


def test_basecollectionreference_ctor_invalid_path_bad_document_id():
    with pytest.raises(ValueError):
        _make_base_collection_reference("bad-document-ID", None, "sub-collection")


def test_basecollectionreference_ctor_invalid_path_bad_number_args():
    with pytest.raises(ValueError):
        _make_base_collection_reference("Just", "A-Document")


def test_basecollectionreference_ctor_invalid_kwarg():
    with pytest.raises(TypeError):
        _make_base_collection_reference("Coh-lek-shun", donut=True)


def test_basecollectionreference___eq___other_type():
    client = mock.sentinel.client
    collection = _make_base_collection_reference("name", client=client)
    other = object()
    assert not collection == other


def test_basecollectionreference___eq___different_path_same_client():
    client = mock.sentinel.client
    collection = _make_base_collection_reference("name", client=client)
    other = _make_base_collection_reference("other", client=client)
    assert not collection == other


def test_basecollectionreference___eq___same_path_different_client():
    client = mock.sentinel.client
    other_client = mock.sentinel.other_client
    collection = _make_base_collection_reference("name", client=client)
    other = _make_base_collection_reference("name", client=other_client)
    assert not collection == other


def test_basecollectionreference___eq___same_path_same_client():
    client = mock.sentinel.client
    collection = _make_base_collection_reference("name", client=client)
    other = _make_base_collection_reference("name", client=client)
    assert collection == other


def test_basecollectionreference_id_property():
    collection_id = "hi-bob"
    collection = _make_base_collection_reference(collection_id)
    assert collection.id == collection_id


def test_basecollectionreference_parent_property():
    from google.cloud.firestore_v1.document import DocumentReference

    collection_id1 = "grocery-store"
    document_id = "market"
    collection_id2 = "darth"
    client = _make_client()
    collection = _make_base_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )

    parent = collection.parent
    assert isinstance(parent, DocumentReference)
    assert parent._client is client
    assert parent._path == (collection_id1, document_id)


def test_basecollectionreference_parent_property_top_level():
    collection = _make_base_collection_reference("tahp-leh-vull")
    assert collection.parent is None


def test_basecollectionreference_document_factory_explicit_id():
    from google.cloud.firestore_v1.document import DocumentReference

    collection_id = "grocery-store"
    document_id = "market"
    client = _make_client()
    collection = _make_base_collection_reference(collection_id, client=client)

    child = collection.document(document_id)
    assert isinstance(child, DocumentReference)
    assert child._client is client
    assert child._path == (collection_id, document_id)


@mock.patch(
    "google.cloud.firestore_v1.base_collection._auto_id",
    return_value="zorpzorpthreezorp012",
)
def test_basecollectionreference_document_factory_auto_id(mock_auto_id):
    from google.cloud.firestore_v1.document import DocumentReference

    collection_name = "space-town"
    client = _make_client()
    collection = _make_base_collection_reference(collection_name, client=client)

    child = collection.document()
    assert isinstance(child, DocumentReference)
    assert child._client is client
    assert child._path == (collection_name, mock_auto_id.return_value)

    mock_auto_id.assert_called_once_with()


def test_basecollectionreference__parent_info_top_level():
    client = _make_client()
    collection_id = "soap"
    collection = _make_base_collection_reference(collection_id, client=client)

    parent_path, expected_prefix = collection._parent_info()

    expected_path = "projects/{}/databases/{}/documents".format(
        client.project, client._database
    )
    assert parent_path == expected_path
    prefix = "{}/{}".format(expected_path, collection_id)
    assert expected_prefix == prefix


def test_basecollectionreference__parent_info_nested():
    collection_id1 = "bar"
    document_id = "baz"
    collection_id2 = "chunk"
    client = _make_client()
    collection = _make_base_collection_reference(
        collection_id1, document_id, collection_id2, client=client
    )

    parent_path, expected_prefix = collection._parent_info()

    expected_path = "projects/{}/databases/{}/documents/{}/{}".format(
        client.project, client._database, collection_id1, document_id
    )
    assert parent_path == expected_path
    prefix = "{}/{}".format(expected_path, collection_id2)
    assert expected_prefix == prefix


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_select(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        field_paths = ["a", "b"]
        query = collection.select(field_paths)

        mock_query.select.assert_called_once_with(field_paths)
        assert query == mock_query.select.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_where(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        field_path = "foo"
        op_string = "=="
        value = 45
        query = collection.where(field_path, op_string, value)

        mock_query.where.assert_called_once_with(field_path, op_string, value)
        assert query == mock_query.where.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_where_with_filter_arg(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference
    from google.cloud.firestore_v1.base_query import FieldFilter

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        field_path = "foo"
        op_string = "=="
        value = 45
        field_filter = FieldFilter(field_path, op_string, value)
        query = collection.where(filter=field_filter)

        mock_query.where.assert_called_once_with(filter=field_filter)
        assert query == mock_query.where.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_where_with_filter_arg_and_positional_args(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference
    from google.cloud.firestore_v1.base_query import FieldFilter

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        field_path = "foo"
        op_string = "=="
        value = 45
        field_filter = FieldFilter(field_path, op_string, value)
        with pytest.raises(ValueError) as exc:
            collection.where(field_path, op_string, value, filter=field_filter)

        mock_query.where.assert_not_called()
        assert (
            str(exc.value)
            == "Can't pass in both the positional arguments and 'filter' at the same time"
        )


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_where_w___name___w_value_as_list_of_str(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        client = _make_client()
        collection = _make_base_collection_reference("collection", client=client)
        field_path = "__name__"
        op_string = "in"
        names = ["hello", "world"]

        query = collection.where(field_path, op_string, names)

        expected_refs = [collection.document(name) for name in names]
        mock_query.where.assert_called_once_with(field_path, op_string, expected_refs)
        assert query == mock_query.where.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_where_w___name___w_value_as_list_of_docref(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        client = _make_client()
        collection = _make_base_collection_reference("collection", client=client)
        field_path = "__name__"
        op_string = "in"
        refs = [collection.document("hello"), collection.document("world")]

        query = collection.where(field_path, op_string, refs)

        mock_query.where.assert_called_once_with(field_path, op_string, refs)
        assert query == mock_query.where.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_order_by(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference
    from google.cloud.firestore_v1.base_query import BaseQuery

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        field_path = "foo"
        direction = BaseQuery.DESCENDING
        query = collection.order_by(field_path, direction=direction)

        mock_query.order_by.assert_called_once_with(field_path, direction=direction)
        assert query == mock_query.order_by.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_limit(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        limit = 15
        query = collection.limit(limit)

        mock_query.limit.assert_called_once_with(limit)
        assert query == mock_query.limit.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_limit_to_last(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        limit = 15
        query = collection.limit_to_last(limit)

        mock_query.limit_to_last.assert_called_once_with(limit)
        assert query == mock_query.limit_to_last.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_offset(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        offset = 113
        query = collection.offset(offset)

        mock_query.offset.assert_called_once_with(offset)
        assert query == mock_query.offset.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_start_at(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        doc_fields = {"a": "b"}
        query = collection.start_at(doc_fields)

        mock_query.start_at.assert_called_once_with(doc_fields)
        assert query == mock_query.start_at.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_start_after(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        doc_fields = {"d": "foo", "e": 10}
        query = collection.start_after(doc_fields)

        mock_query.start_after.assert_called_once_with(doc_fields)
        assert query == mock_query.start_after.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_end_before(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        doc_fields = {"bar": 10.5}
        query = collection.end_before(doc_fields)

        mock_query.end_before.assert_called_once_with(doc_fields)
        assert query == mock_query.end_before.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_end_at(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        doc_fields = {"opportunity": True, "reason": 9}
        query = collection.end_at(doc_fields)

        mock_query.end_at.assert_called_once_with(doc_fields)
        assert query == mock_query.end_at.return_value


@mock.patch("google.cloud.firestore_v1.base_query.BaseQuery", autospec=True)
def test_basecollectionreference_pipeline(mock_query):
    from google.cloud.firestore_v1.base_collection import BaseCollectionReference

    with mock.patch.object(BaseCollectionReference, "_query") as _query:
        _query.return_value = mock_query

        collection = _make_base_collection_reference("collection")
        mock_source = mock.Mock()
        pipeline = collection._build_pipeline(mock_source)

        mock_query._build_pipeline.assert_called_once_with(mock_source)
        assert pipeline == mock_query._build_pipeline.return_value


@mock.patch("random.SystemRandom.choice")
def test__auto_id(mock_rand_choice):
    from google.cloud.firestore_v1.base_collection import _AUTO_ID_CHARS, _auto_id

    mock_result = "0123456789abcdefghij"
    mock_rand_choice.side_effect = list(mock_result)
    result = _auto_id()
    assert result == mock_result

    mock_calls = [mock.call(_AUTO_ID_CHARS)] * 20
    assert mock_rand_choice.mock_calls == mock_calls


@mock.patch("random.choice")
@mock.patch("random.SystemRandom.choice")
def test__auto_id_fallback_to_random(mock_system_rand_choice, mock_rand_choice):
    from google.cloud.firestore_v1.base_collection import _AUTO_ID_CHARS, _auto_id

    mock_system_rand_choice.side_effect = NotImplementedError
    mock_result = "0123456789abcdefghij"
    mock_rand_choice.side_effect = list(mock_result)
    result = _auto_id()
    assert result == mock_result

    mock_calls = [mock.call(_AUTO_ID_CHARS)] * 20
    assert mock_rand_choice.mock_calls == mock_calls


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client():
    from google.cloud.firestore_v1.client import Client

    credentials = _make_credentials()
    return Client(project=DEFAULT_TEST_PROJECT, credentials=credentials)
