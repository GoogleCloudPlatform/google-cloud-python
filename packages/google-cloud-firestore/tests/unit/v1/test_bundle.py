# -*- coding: utf-8 -*-
#
# # Copyright 2021 Google LLC All rights reserved.
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

import typing

import mock
import pytest

from google.cloud.firestore_v1 import base_query, collection
from google.cloud.firestore_v1 import query as query_mod
from tests.unit.v1 import _test_helpers
from tests.unit.v1._test_helpers import DEFAULT_TEST_PROJECT


class _CollectionQueryMixin:
    # Path to each document where we don't specify custom collection names or
    # document Ids
    doc_key: str = (
        f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc"
    )

    @staticmethod
    def build_results_iterable(items):
        raise NotImplementedError()

    @staticmethod
    def get_collection_class():
        raise NotImplementedError()

    @staticmethod
    def get_internal_client_mock():
        raise NotImplementedError()

    @staticmethod
    def get_client():
        raise NotImplementedError()

    def _bundled_collection_helper(
        self,
        document_ids: typing.Optional[typing.List[str]] = None,
        data: typing.Optional[typing.List[typing.Dict]] = None,
    ) -> collection.CollectionReference:
        """Builder of a mocked Query for the sake of testing Bundles.

        Bundling queries involves loading the actual documents for cold storage,
        and this method arranges all of the necessary mocks so that unit tests
        can think they are evaluating a live query.
        """
        from google.protobuf.timestamp_pb2 import Timestamp  # type: ignore

        from google.cloud.firestore_v1 import _helpers
        from google.cloud.firestore_v1.types.document import Document
        from google.cloud.firestore_v1.types.firestore import RunQueryResponse

        client = self.get_client()
        template = client._database_string + "/documents/col/{}"
        document_ids = document_ids or ["doc-1", "doc-2"]

        def _index_from_data(index: int):
            if data is None or len(data) < index + 1:
                return None
            return data[index]

        documents = [
            RunQueryResponse(
                transaction=b"",
                document=Document(
                    name=template.format(document_id),
                    fields=_helpers.encode_dict(
                        _index_from_data(index) or {"hello": "world"}
                    ),
                    create_time=Timestamp(seconds=1, nanos=1),
                    update_time=Timestamp(seconds=1, nanos=1),
                ),
                read_time=_test_helpers.build_timestamp(),
            )
            for index, document_id in enumerate(document_ids)
        ]
        iterator = self.build_results_iterable(documents)
        api_client = self.get_internal_client_mock()
        api_client.run_query.return_value = iterator
        client._firestore_api_internal = api_client
        return self.get_collection_class()("col", client=client)

    def _bundled_query_helper(
        self,
        document_ids: typing.Optional[typing.List[str]] = None,
        data: typing.Optional[typing.List[typing.Dict]] = None,
    ) -> base_query.BaseQuery:
        return self._bundled_collection_helper(
            document_ids=document_ids,
            data=data,
        )._query()


class TestBundle(_CollectionQueryMixin):
    @staticmethod
    def build_results_iterable(items):
        return iter(items)

    @staticmethod
    def get_client():
        return _test_helpers.make_client()

    @staticmethod
    def get_internal_client_mock():
        from google.cloud.firestore_v1.services.firestore import client

        return mock.create_autospec(client.FirestoreClient)

    @classmethod
    def get_collection_class(cls):
        return collection.CollectionReference

    def test_add_document(self):
        from google.cloud.firestore_bundle import FirestoreBundle

        bundle = FirestoreBundle("test")
        doc = _test_helpers.build_document_snapshot(client=_test_helpers.make_client())
        bundle.add_document(doc)
        assert bundle.documents[self.doc_key].snapshot == doc

    def test_add_newer_document(self):
        from google.protobuf.timestamp_pb2 import Timestamp  # type: ignore

        from google.cloud.firestore_bundle import FirestoreBundle

        bundle = FirestoreBundle("test")
        old_doc = _test_helpers.build_document_snapshot(
            data={"version": 1},
            client=_test_helpers.make_client(),
            read_time=Timestamp(seconds=1, nanos=1),
        )
        bundle.add_document(old_doc)
        assert bundle.documents[self.doc_key].snapshot._data["version"] == 1

        # Builds the same ID by default
        new_doc = _test_helpers.build_document_snapshot(
            data={"version": 2},
            client=_test_helpers.make_client(),
            read_time=Timestamp(seconds=1, nanos=2),
        )
        bundle.add_document(new_doc)
        assert bundle.documents[self.doc_key].snapshot._data["version"] == 2

    def test_add_older_document(self):
        from google.protobuf.timestamp_pb2 import Timestamp  # type: ignore

        from google.cloud.firestore_bundle import FirestoreBundle

        bundle = FirestoreBundle("test")
        new_doc = _test_helpers.build_document_snapshot(
            data={"version": 2},
            client=_test_helpers.make_client(),
            read_time=Timestamp(seconds=1, nanos=2),
        )
        bundle.add_document(new_doc)
        assert bundle.documents[self.doc_key].snapshot._data["version"] == 2

        # Builds the same ID by default
        old_doc = _test_helpers.build_document_snapshot(
            data={"version": 1},
            client=_test_helpers.make_client(),
            read_time=Timestamp(seconds=1, nanos=1),
        )
        bundle.add_document(old_doc)
        assert bundle.documents[self.doc_key].snapshot._data["version"] == 2

    def test_add_document_with_different_read_times(self):
        from google.cloud.firestore_bundle import FirestoreBundle

        bundle = FirestoreBundle("test")
        doc = _test_helpers.build_document_snapshot(
            client=_test_helpers.make_client(),
            data={"version": 1},
            read_time=_test_helpers.build_test_timestamp(second=1),
        )
        # Create another reference to the same document, but with new
        # data and a more recent `read_time`
        doc_refreshed = _test_helpers.build_document_snapshot(
            client=_test_helpers.make_client(),
            data={"version": 2},
            read_time=_test_helpers.build_test_timestamp(second=2),
        )

        bundle.add_document(doc)
        assert bundle.documents[self.doc_key].snapshot._data == {"version": 1}
        bundle.add_document(doc_refreshed)
        assert bundle.documents[self.doc_key].snapshot._data == {"version": 2}

    def test_add_query(self):
        from google.cloud.firestore_bundle import FirestoreBundle

        query = self._bundled_query_helper()
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", query)
        assert bundle.named_queries.get("asdf") is not None
        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-1"
            ]
            is not None
        )
        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-2"
            ]
            is not None
        )

    def test_add_query_twice(self):
        from google.cloud.firestore_bundle import FirestoreBundle

        query = self._bundled_query_helper()
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", query)
        with pytest.raises(ValueError):
            bundle.add_named_query("asdf", query)

    def test_adding_collection_raises_error(self):
        from google.cloud.firestore_bundle import FirestoreBundle

        col = self._bundled_collection_helper()
        bundle = FirestoreBundle("test")
        with pytest.raises(ValueError):
            bundle.add_named_query("asdf", col)

    def test_bundle_build(self):
        from google.cloud.firestore_bundle import FirestoreBundle

        bundle = FirestoreBundle("test")
        bundle.add_named_query("best name", self._bundled_query_helper())
        assert isinstance(bundle.build(), str)

    def test_get_documents(self):
        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        bundle = FirestoreBundle("test")
        query: query_mod.Query = self._bundled_query_helper()  # type: ignore
        bundle.add_named_query("sweet query", query)
        docs_iter = _helpers._get_documents_from_bundle(
            bundle, query_name="sweet query"
        )
        doc = next(docs_iter)
        assert doc.id == "doc-1"
        doc = next(docs_iter)
        assert doc.id == "doc-2"

        # Now an empty one
        docs_iter = _helpers._get_documents_from_bundle(
            bundle, query_name="wrong query"
        )
        doc = next(docs_iter, None)
        assert doc is None

    def test_get_documents_two_queries(self):
        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        bundle = FirestoreBundle("test")
        query: query_mod.Query = self._bundled_query_helper()  # type: ignore
        bundle.add_named_query("sweet query", query)

        query: query_mod.Query = self._bundled_query_helper(
            document_ids=["doc-3", "doc-4"]
        )  # type: ignore
        bundle.add_named_query("second query", query)

        docs_iter = _helpers._get_documents_from_bundle(
            bundle, query_name="sweet query"
        )
        doc = next(docs_iter)
        assert doc.id == "doc-1"
        doc = next(docs_iter)
        assert doc.id == "doc-2"

        docs_iter = _helpers._get_documents_from_bundle(
            bundle, query_name="second query"
        )
        doc = next(docs_iter)
        assert doc.id == "doc-3"
        doc = next(docs_iter)
        assert doc.id == "doc-4"

    def test_get_document(self):
        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        bundle = FirestoreBundle("test")
        query: query_mod.Query = self._bundled_query_helper()  # type: ignore
        bundle.add_named_query("sweet query", query)

        assert (
            _helpers._get_document_from_bundle(
                bundle,
                document_id=f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-1",
            )
            is not None
        )

        assert (
            _helpers._get_document_from_bundle(
                bundle,
                document_id=f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-0",
            )
            is None
        )


class TestAsyncBundle(_CollectionQueryMixin):
    @staticmethod
    def get_client():
        return _test_helpers.make_async_client()

    @staticmethod
    def build_results_iterable(items):
        from tests.unit.v1 import test__helpers

        return test__helpers.AsyncIter(items)

    @staticmethod
    def get_internal_client_mock():
        from tests.unit.v1 import test__helpers

        return test__helpers.AsyncMock(spec=["run_query"])

    @classmethod
    def get_collection_class(cls):
        from google.cloud.firestore_v1 import async_collection

        return async_collection.AsyncCollectionReference

    def test_async_query(self):
        # Create an async query, but this test does not need to be
        # marked as async by pytest because `bundle.add_named_query()`
        # seemlessly handles accepting async iterables.
        from google.cloud.firestore_bundle import FirestoreBundle

        async_query = self._bundled_query_helper()
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", async_query)
        assert bundle.named_queries.get("asdf") is not None
        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-1"
            ]
            is not None
        )
        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-2"
            ]
            is not None
        )


class TestBundleBuilder(_CollectionQueryMixin):
    @staticmethod
    def build_results_iterable(items):
        return iter(items)

    @staticmethod
    def get_client():
        return _test_helpers.make_client()

    @staticmethod
    def get_internal_client_mock():
        from google.cloud.firestore_v1.services.firestore import client

        return mock.create_autospec(client.FirestoreClient)

    @classmethod
    def get_collection_class(cls):
        return collection.CollectionReference

    def test_build_round_trip(self):
        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        query = self._bundled_query_helper()
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", query)
        serialized = bundle.build()
        assert (
            serialized == _helpers.deserialize_bundle(serialized, query._client).build()
        )

    def test_build_round_trip_emojis(self):
        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        smile = "😂"
        mermaid = "🧜🏿‍♀️"
        query = self._bundled_query_helper(
            data=[{"smile": smile}, {"compound": mermaid}],
        )
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", query)
        serialized = bundle.build()
        reserialized_bundle = _helpers.deserialize_bundle(serialized, query._client)

        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-1"
            ].snapshot._data["smile"]
            == smile
        )
        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-2"
            ].snapshot._data["compound"]
            == mermaid
        )
        assert serialized == reserialized_bundle.build()

    def test_build_round_trip_more_unicode(self):
        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        bano = "baño"
        chinese_characters = "殷周金文集成引得"
        query = self._bundled_query_helper(
            data=[{"bano": bano}, {"international": chinese_characters}],
        )
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", query)
        serialized = bundle.build()
        reserialized_bundle = _helpers.deserialize_bundle(serialized, query._client)

        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-1"
            ].snapshot._data["bano"]
            == bano
        )
        assert (
            bundle.documents[
                f"projects/{DEFAULT_TEST_PROJECT}/databases/(default)/documents/col/doc-2"
            ].snapshot._data["international"]
            == chinese_characters
        )
        assert serialized == reserialized_bundle.build()

    def test_roundtrip_binary_data(self):
        import sys

        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        query = self._bundled_query_helper(
            data=[{"binary_data": b"\x0f"}],
        )
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", query)
        serialized = bundle.build()
        reserialized_bundle = _helpers.deserialize_bundle(serialized, query._client)
        gen = _helpers._get_documents_from_bundle(reserialized_bundle)
        snapshot = next(gen)
        assert (
            int.from_bytes(snapshot._data["binary_data"], byteorder=sys.byteorder) == 15
        )

    def test_deserialize_from_seconds_nanos(self):
        """Some SDKs (Node) serialize Timestamp values to
        '{"seconds": 123, "nanos": 456}', instead of an ISO-formatted string.
        This tests deserialization from that format."""
        from google.protobuf.json_format import ParseError

        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client(project_name="fir-bundles-test")

        _serialized: str = (
            '139{"metadata":{"id":"test-bundle","createTime":'
            + '{"seconds":"1616434660","nanos":913764000},"version":1,"totalDocuments"'
            + ':1,"totalBytes":"829"}}224{"namedQuery":{"name":"self","bundledQuery":'
            + '{"parent":"projects/fir-bundles-test/databases/(default)/documents",'
            + '"structuredQuery":{"from":[{"collectionId":"bundles"}]}},"readTime":'
            + '{"seconds":"1616434660","nanos":913764000}}}194{"documentMetadata":'
            + '{"name":"projects/fir-bundles-test/databases/(default)/documents/'
            + 'bundles/test-bundle","readTime":{"seconds":"1616434660","nanos":'
            + '913764000},"exists":true,"queries":["self"]}}402{"document":{"name":'
            + '"projects/fir-bundles-test/databases/(default)/documents/bundles/'
            + 'test-bundle","fields":{"clientCache":{"stringValue":"1200"},'
            + '"serverCache":{"stringValue":"600"},"queries":{"mapValue":{"fields":'
            + '{"self":{"mapValue":{"fields":{"collection":{"stringValue":"bundles"'
            + '}}}}}}}},"createTime":{"seconds":"1615488796","nanos":163327000},'
            + '"updateTime":{"seconds":"1615492486","nanos":34157000}}}'
        )

        with pytest.raises(
            (ValueError, ParseError)
        ):  # protobuf 3.18.0 raises ParseError
            _helpers.deserialize_bundle(_serialized, client=client)

        # See https://github.com/googleapis/python-firestore/issues/505
        #
        # The following assertions would test deserialization of NodeJS bundles
        # were explicit handling of that edge case to be added.

        # First, deserialize that value into a Bundle instance. If this succeeds,
        # we're off to a good start.
        # bundle = _helpers.deserialize_bundle(_serialized, client=client)
        # Second, re-serialize it into a Python-centric format (aka, ISO timestamps)
        # instead of seconds/nanos.
        # re_serialized = bundle.build()
        # # Finally, confirm the round trip.
        # assert re_serialized == _helpers.deserialize_bundle(re_serialized, client=client).build()
        #

    def test_deserialized_bundle_cached_metadata(self):
        from google.cloud.firestore_bundle import FirestoreBundle
        from google.cloud.firestore_v1 import _helpers

        query = self._bundled_query_helper()
        bundle = FirestoreBundle("test")
        bundle.add_named_query("asdf", query)
        bundle_copy = _helpers.deserialize_bundle(bundle.build(), query._client)
        assert isinstance(bundle_copy, FirestoreBundle)
        assert bundle_copy._deserialized_metadata is not None
        bundle_copy.add_named_query("second query", query)
        assert bundle_copy._deserialized_metadata is None

    @mock.patch("google.cloud.firestore_v1._helpers._parse_bundle_elements_data")
    def test_invalid_json(self, fnc):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        fnc.return_value = iter([{}])
        with pytest.raises(ValueError):
            _helpers.deserialize_bundle("does not matter", client)

    @mock.patch("google.cloud.firestore_v1._helpers._parse_bundle_elements_data")
    def test_not_metadata_first(self, fnc):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        fnc.return_value = iter([{"document": {}}])
        with pytest.raises(ValueError):
            _helpers.deserialize_bundle("does not matter", client)

    @mock.patch("google.cloud.firestore_bundle.FirestoreBundle._add_bundle_element")
    @mock.patch("google.cloud.firestore_v1._helpers._parse_bundle_elements_data")
    def test_unexpected_termination(self, fnc, _):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        # invalid bc `document_metadata` must be followed by a `document`
        fnc.return_value = [{"metadata": {"id": "asdf"}}, {"documentMetadata": {}}]
        with pytest.raises(ValueError):
            _helpers.deserialize_bundle("does not matter", client)

    @mock.patch("google.cloud.firestore_bundle.FirestoreBundle._add_bundle_element")
    @mock.patch("google.cloud.firestore_v1._helpers._parse_bundle_elements_data")
    def test_valid_passes(self, fnc, _):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        fnc.return_value = [
            {"metadata": {"id": "asdf"}},
            {"documentMetadata": {}},
            {"document": {}},
        ]
        _helpers.deserialize_bundle("does not matter", client)

    @mock.patch("google.cloud.firestore_bundle.FirestoreBundle._add_bundle_element")
    @mock.patch("google.cloud.firestore_v1._helpers._parse_bundle_elements_data")
    def test_invalid_bundle(self, fnc, _):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        # invalid bc `document` must follow `document_metadata`
        fnc.return_value = [{"metadata": {"id": "asdf"}}, {"document": {}}]
        with pytest.raises(ValueError):
            _helpers.deserialize_bundle("does not matter", client)

    @mock.patch("google.cloud.firestore_bundle.FirestoreBundle._add_bundle_element")
    @mock.patch("google.cloud.firestore_v1._helpers._parse_bundle_elements_data")
    def test_invalid_bundle_element_type(self, fnc, _):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        # invalid bc `wtfisthis?` is obviously invalid
        fnc.return_value = [{"metadata": {"id": "asdf"}}, {"wtfisthis?": {}}]
        with pytest.raises(ValueError):
            _helpers.deserialize_bundle("does not matter", client)

    @mock.patch("google.cloud.firestore_bundle.FirestoreBundle._add_bundle_element")
    @mock.patch("google.cloud.firestore_v1._helpers._parse_bundle_elements_data")
    def test_invalid_bundle_start(self, fnc, _):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        # invalid bc first element must be of key `metadata`
        fnc.return_value = [{"document": {}}]
        with pytest.raises(ValueError):
            _helpers.deserialize_bundle("does not matter", client)

    def test_not_actually_a_bundle_at_all(self):
        from google.cloud.firestore_v1 import _helpers

        client = _test_helpers.make_client()
        with pytest.raises(ValueError):
            _helpers.deserialize_bundle("{}", client)

    def test_add_invalid_bundle_element_type(self):
        from google.cloud.firestore_bundle import BundleElement, FirestoreBundle

        client = _test_helpers.make_client()
        bundle = FirestoreBundle("asdf")
        with pytest.raises(ValueError):
            bundle._add_bundle_element(BundleElement(), client=client, type="asdf")
