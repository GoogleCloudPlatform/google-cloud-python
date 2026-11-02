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

import base64
from unittest import mock

import pytest
from google.cloud.datastore_v1.types import datastore as datastore_pb2
from google.cloud.datastore_v1.types import entity as entity_pb2
from google.cloud.datastore_v1.types import query as query_pb2

from google.cloud.ndb import _datastore_query, exceptions, model, tasklets
from google.cloud.ndb import context as context_module
from google.cloud.ndb import key as key_module
from google.cloud.ndb import query as query_module

from . import utils


def test_make_filter():
    expected = query_pb2.PropertyFilter(
        property=query_pb2.PropertyReference(name="harry"),
        op=query_pb2.PropertyFilter.Operator.EQUAL,
        value=entity_pb2.Value(string_value="Harold"),
    )
    assert _datastore_query.make_filter("harry", "=", "Harold") == expected


def test_make_composite_and_filter():
    filters = [
        query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="harry"),
            op=query_pb2.PropertyFilter.Operator.EQUAL,
            value=entity_pb2.Value(string_value="Harold"),
        ),
        query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="josie"),
            op=query_pb2.PropertyFilter.Operator.EQUAL,
            value=entity_pb2.Value(string_value="Josephine"),
        ),
    ]
    expected = query_pb2.CompositeFilter(
        op=query_pb2.CompositeFilter.Operator.AND,
        filters=[
            query_pb2.Filter(property_filter=sub_filter) for sub_filter in filters
        ],
    )
    assert _datastore_query.make_composite_and_filter(filters) == expected


class Test_fetch:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.iterate")
    def test_fetch(iterate):
        results = iterate.return_value
        results.has_next_async.side_effect = utils.future_results(
            True, True, True, False
        )
        results.next.side_effect = ["a", "b", "c", "d"]
        assert _datastore_query.fetch("foo").result() == ["a", "b", "c"]
        iterate.assert_called_once_with("foo")


class Test_count:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.iterate")
    def test_count_brute_force(iterate):
        class DummyQueryIterator:
            def __init__(self, items):
                self.items = list(items)

            def has_next_async(self):
                return utils.future_result(bool(self.items))

            def next(self):
                return self.items.pop()

        iterate.return_value = DummyQueryIterator(range(5))
        query = query_module.QueryOptions(
            filters=mock.Mock(_multiquery=True, spec=("_multiquery",))
        )

        future = _datastore_query.count(query)
        assert future.result() == 5
        iterate.assert_called_once_with(
            query_module.QueryOptions(filters=query.filters, projection=["__key__"]),
            raw=True,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.iterate")
    def test_count_brute_force_with_limit(iterate):
        class DummyQueryIterator:
            def __init__(self, items):
                self.items = list(items)

            def has_next_async(self):
                return utils.future_result(bool(self.items))

            def next(self):
                return self.items.pop()

        iterate.return_value = DummyQueryIterator(range(5))
        query = query_module.QueryOptions(
            filters=mock.Mock(
                _multiquery=False,
                _post_filters=mock.Mock(return_value=True),
                spec=("_multiquery", "_post_filters"),
            ),
            limit=3,
        )

        future = _datastore_query.count(query)
        assert future.result() == 3
        iterate.assert_called_once_with(
            query_module.QueryOptions(
                filters=query.filters, projection=["__key__"], limit=3
            ),
            raw=True,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._datastore_run_query")
    def test_count_by_skipping_w_a_result(run_query):
        # These results should technically be impossible, but better safe than sorry.
        run_query.side_effect = utils.future_results(
            mock.Mock(
                batch=mock.Mock(
                    more_results=_datastore_query.NOT_FINISHED,
                    skipped_results=1000,
                    entity_results=[],
                    end_cursor=b"himom",
                    skipped_cursor=b"dontlookatme",
                    spec=(
                        "more_results",
                        "skipped_results",
                        "entity_results",
                        "end_cursor",
                    ),
                ),
                spec=("batch",),
            ),
            mock.Mock(
                batch=mock.Mock(
                    more_results=_datastore_query.NOT_FINISHED,
                    skipped_results=0,
                    entity_results=[],
                    end_cursor=b"secondCursor",
                    spec=(
                        "more_results",
                        "skipped_results",
                        "entity_results",
                        "end_cursor",
                    ),
                ),
                spec=("batch",),
            ),
            mock.Mock(
                batch=mock.Mock(
                    more_results=_datastore_query.NO_MORE_RESULTS,
                    skipped_results=99,
                    entity_results=[object()],
                    end_cursor=b"ohhaithere",
                    skipped_cursor=b"hellodad",
                    spec=(
                        "more_results",
                        "skipped_results",
                        "entity_results",
                        "end_cursor",
                        "skipped_cursor",
                    ),
                ),
                spec=("batch",),
            ),
        )

        query = query_module.QueryOptions()
        future = _datastore_query.count(query)
        assert future.result() == 1100

        expected = [
            mock.call(
                query_module.QueryOptions(
                    limit=1,
                    offset=10000,
                    projection=["__key__"],
                )
            ),
            (
                (
                    query_module.QueryOptions(
                        limit=1,
                        offset=10000,
                        projection=["__key__"],
                        start_cursor=_datastore_query.Cursor(b"himom"),
                    ),
                ),
                {},
            ),
            (
                (
                    query_module.QueryOptions(
                        limit=1,
                        offset=10000,
                        projection=["__key__"],
                        start_cursor=_datastore_query.Cursor(b"secondCursor"),
                    ),
                ),
                {},
            ),
        ]
        assert run_query.call_args_list == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._datastore_run_query")
    def test_count_by_skipping(run_query):
        run_query.side_effect = utils.future_results(
            mock.Mock(
                batch=mock.Mock(
                    more_results=_datastore_query.NOT_FINISHED,
                    skipped_results=1000,
                    entity_results=[],
                    end_cursor=b"himom",
                    skipped_cursor=b"dontlookatme",
                    spec=(
                        "more_results",
                        "skipped_results",
                        "entity_results",
                        "end_cursor",
                    ),
                ),
                spec=("batch",),
            ),
            mock.Mock(
                batch=mock.Mock(
                    more_results=_datastore_query.NO_MORE_RESULTS,
                    skipped_results=100,
                    entity_results=[],
                    end_cursor=b"nopenuhuh",
                    skipped_cursor=b"hellodad",
                    spec=(
                        "more_results",
                        "skipped_results",
                        "entity_results",
                        "end_cursor",
                        "skipped_cursor",
                    ),
                ),
                spec=("batch",),
            ),
        )

        query = query_module.QueryOptions()
        future = _datastore_query.count(query)
        assert future.result() == 1100

        expected = [
            mock.call(
                query_module.QueryOptions(
                    limit=1,
                    offset=10000,
                    projection=["__key__"],
                )
            ),
            (
                (
                    query_module.QueryOptions(
                        limit=1,
                        offset=10000,
                        projection=["__key__"],
                        start_cursor=_datastore_query.Cursor(b"himom"),
                    ),
                ),
                {},
            ),
        ]
        assert run_query.call_args_list == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._count_brute_force")
    def test_count_by_skipping_emulator(count_brute_force):
        """Regression test for #525

        Test differences between emulator and the real Datastore.

        https://github.com/googleapis/python-ndb/issues/525
        """
        count_brute_force.return_value = utils.future_result(42)
        query = query_module.QueryOptions()
        with mock.patch.dict("os.environ", {"DATASTORE_EMULATOR_HOST": "emulator"}):
            future = _datastore_query.count(query)
            assert future.result() == 42
        assert count_brute_force.call_args_list == [mock.call(query)]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._datastore_run_query")
    def test_count_by_skipping_with_limit(run_query):
        run_query.return_value = utils.future_result(
            mock.Mock(
                batch=mock.Mock(
                    more_results=_datastore_query.MORE_RESULTS_AFTER_LIMIT,
                    skipped_results=99,
                    entity_results=[object()],
                    end_cursor=b"himom",
                    spec=(
                        "more_results",
                        "skipped_results",
                        "entity_results",
                        "end_cursor",
                    ),
                ),
                spec=("batch",),
            )
        )

        query = query_module.QueryOptions(
            filters=mock.Mock(
                _multiquery=False,
                _post_filters=mock.Mock(return_value=None),
                spec=("_multiquery", "_post_filters"),
            ),
            limit=100,
        )
        future = _datastore_query.count(query)
        assert future.result() == 100

        run_query.assert_called_once_with(
            query_module.QueryOptions(
                limit=1,
                offset=99,
                projection=["__key__"],
                filters=query.filters,
            )
        )


class Test_iterate:
    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_query._QueryIteratorImpl")
    def test_iterate_single(QueryIterator):
        query = mock.Mock(filters=None, spec=("filters"))
        iterator = QueryIterator.return_value
        assert _datastore_query.iterate(query) is iterator
        QueryIterator.assert_called_once_with(query, raw=False)

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_query._QueryIteratorImpl")
    def test_iterate_single_w_filters(QueryIterator):
        query = mock.Mock(
            filters=mock.Mock(
                _multiquery=False,
                _post_filters=mock.Mock(return_value=None),
                spec=("_multiquery", "_post_filters"),
            ),
            spec=("filters", "_post_filters"),
        )
        iterator = QueryIterator.return_value
        assert _datastore_query.iterate(query) is iterator
        QueryIterator.assert_called_once_with(query, raw=False)

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_query._PostFilterQueryIteratorImpl")
    def test_iterate_single_with_post_filter(QueryIterator):
        query = mock.Mock(
            filters=mock.Mock(_multiquery=False, spec=("_multiquery", "_post_filters")),
            spec=("filters", "_post_filters"),
        )
        iterator = QueryIterator.return_value
        post_filters = query.filters._post_filters.return_value
        predicate = post_filters._to_filter.return_value
        assert _datastore_query.iterate(query) is iterator
        QueryIterator.assert_called_once_with(query, predicate, raw=False)
        post_filters._to_filter.assert_called_once_with(post=True)

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_query._MultiQueryIteratorImpl")
    def test_iterate_multi(MultiQueryIterator):
        query = mock.Mock(
            filters=mock.Mock(_multiquery=True, spec=("_multiquery",)),
            spec=("filters",),
        )
        iterator = MultiQueryIterator.return_value
        assert _datastore_query.iterate(query) is iterator
        MultiQueryIterator.assert_called_once_with(query, raw=False)


class TestQueryIterator:
    @staticmethod
    def test_has_next():
        with pytest.raises(NotImplementedError):
            _datastore_query.QueryIterator().has_next()

    @staticmethod
    def test_has_next_async():
        with pytest.raises(NotImplementedError):
            _datastore_query.QueryIterator().has_next_async()

    @staticmethod
    def test_probably_has_next():
        with pytest.raises(NotImplementedError):
            _datastore_query.QueryIterator().probably_has_next()

    @staticmethod
    def test_next():
        with pytest.raises(NotImplementedError):
            _datastore_query.QueryIterator().next()

    @staticmethod
    def test_cursor_before():
        with pytest.raises(NotImplementedError):
            _datastore_query.QueryIterator().cursor_before()

    @staticmethod
    def test_cursor_after():
        with pytest.raises(NotImplementedError):
            _datastore_query.QueryIterator().cursor_after()

    @staticmethod
    def test_index_list():
        with pytest.raises(NotImplementedError):
            _datastore_query.QueryIterator().index_list()


class Test_QueryIteratorImpl:
    @staticmethod
    def test_constructor():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        assert iterator._query == "foo"
        assert iterator._batch is None
        assert iterator._index is None
        assert iterator._has_next_batch is None
        assert iterator._cursor_before is None
        assert iterator._cursor_after is None
        assert not iterator._raw

    @staticmethod
    def test_constructor_raw():
        iterator = _datastore_query._QueryIteratorImpl("foo", raw=True)
        assert iterator._query == "foo"
        assert iterator._batch is None
        assert iterator._index is None
        assert iterator._has_next_batch is None
        assert iterator._cursor_before is None
        assert iterator._cursor_after is None
        assert iterator._raw

    @staticmethod
    def test___iter__():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        assert iter(iterator) is iterator

    @staticmethod
    def test_has_next():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator.has_next_async = mock.Mock(return_value=utils.future_result("bar"))
        assert iterator.has_next() == "bar"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_not_started():
        iterator = _datastore_query._QueryIteratorImpl("foo")

        def dummy_next_batch():
            iterator._index = 0
            iterator._batch = ["a", "b", "c"]
            return utils.future_result(None)

        iterator._next_batch = dummy_next_batch
        assert iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_started():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._index = 0
        iterator._batch = ["a", "b", "c"]
        assert iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_finished():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._index = 3
        iterator._batch = ["a", "b", "c"]
        assert not iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_next_batch():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._index = 3
        iterator._batch = ["a", "b", "c"]
        iterator._has_next_batch = True

        def dummy_next_batch():
            iterator._index = 0
            iterator._batch = ["d", "e", "f"]
            return utils.future_result(None)

        iterator._next_batch = dummy_next_batch
        assert iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_next_batch_is_empty():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._index = 3
        iterator._batch = ["a", "b", "c"]
        iterator._has_next_batch = True

        batches = [[], ["d", "e", "f"]]

        def dummy_next_batch():
            iterator._index = 0
            iterator._batch = batches.pop(0)
            return utils.future_result(None)

        iterator._next_batch = dummy_next_batch
        assert iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_next_batch_finished():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._index = 3
        iterator._batch = ["a", "b", "c"]
        iterator._has_next_batch = True

        def dummy_next_batch():
            iterator._index = 3
            iterator._batch = ["d", "e", "f"]
            return utils.future_result(None)

        iterator._next_batch = dummy_next_batch
        assert not iterator.has_next_async().result()

    @staticmethod
    def test_probably_has_next_not_started():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        assert iterator.probably_has_next()

    @staticmethod
    def test_probably_has_next_more_batches():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._batch = "foo"
        iterator._has_next_batch = True
        assert iterator.probably_has_next()

    @staticmethod
    def test_probably_has_next_in_batch():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._batch = ["a", "b", "c"]
        iterator._index = 1
        assert iterator.probably_has_next()

    @staticmethod
    def test_probably_has_next_finished():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._batch = ["a", "b", "c"]
        iterator._index = 3
        assert not iterator.probably_has_next()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._datastore_run_query")
    def test__next_batch(_datastore_run_query):
        entity1 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
            )
        )
        entity2 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=43)],
            )
        )
        entity3 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=44)],
            )
        )
        entity_results = [
            mock.Mock(entity=entity1, cursor=b"a"),
            mock.Mock(entity=entity2, cursor=b"b"),
            mock.Mock(entity=entity3, cursor=b"c"),
        ]
        _datastore_run_query.return_value = utils.future_result(
            mock.Mock(
                batch=mock.Mock(
                    entity_result_type=query_pb2.EntityResult.ResultType.FULL,
                    entity_results=entity_results,
                    end_cursor=b"abc",
                    more_results=query_pb2.QueryResultBatch.MoreResultsType.NO_MORE_RESULTS,
                )
            )
        )

        query = query_module.QueryOptions()
        iterator = _datastore_query._QueryIteratorImpl(query)
        assert iterator._next_batch().result() is None
        assert iterator._index == 0
        assert len(iterator._batch) == 3
        assert iterator._batch[0].result_pb.entity == entity1
        assert iterator._batch[0].result_type == query_pb2.EntityResult.ResultType.FULL
        assert iterator._batch[0].order_by is None
        assert not iterator._has_next_batch

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_query._datastore_run_query")
    def test__next_batch_cached_delete(_datastore_run_query, in_context):
        entity1 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
            )
        )
        entity2 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=43)],
            )
        )
        entity3 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=44)],
            )
        )
        entity_results = [
            mock.Mock(entity=entity1, cursor=b"a"),
            mock.Mock(entity=entity2, cursor=b"b"),
            mock.Mock(entity=entity3, cursor=b"c"),
        ]
        in_context.cache[key_module.Key("ThisKind", 43)] = None
        _datastore_run_query.return_value = utils.future_result(
            mock.Mock(
                batch=mock.Mock(
                    entity_result_type=query_pb2.EntityResult.ResultType.FULL,
                    entity_results=entity_results,
                    end_cursor=b"abc",
                    more_results=query_pb2.QueryResultBatch.MoreResultsType.NO_MORE_RESULTS,
                )
            )
        )

        query = query_module.QueryOptions()
        iterator = _datastore_query._QueryIteratorImpl(query)
        assert iterator._next_batch().result() is None
        assert iterator._index == 0
        assert len(iterator._batch) == 2
        assert iterator._batch[0].result_pb.entity == entity1
        assert iterator._batch[0].result_type == query_pb2.EntityResult.ResultType.FULL
        assert iterator._batch[0].order_by is None
        assert iterator._batch[1].result_pb.entity == entity3
        assert not iterator._has_next_batch

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._datastore_run_query")
    def test__next_batch_has_more(_datastore_run_query):
        entity1 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
            )
        )
        entity2 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=43)],
            )
        )
        entity3 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=44)],
            )
        )
        entity_results = [
            mock.Mock(entity=entity1, cursor=b"a"),
            mock.Mock(entity=entity2, cursor=b"b"),
            mock.Mock(entity=entity3, cursor=b"c"),
        ]
        _datastore_run_query.return_value = utils.future_result(
            mock.Mock(
                batch=mock.Mock(
                    entity_result_type=query_pb2.EntityResult.ResultType.PROJECTION,
                    entity_results=entity_results,
                    end_cursor=b"abc",
                    more_results=query_pb2.QueryResultBatch.MoreResultsType.NOT_FINISHED,
                )
            )
        )

        query = query_module.QueryOptions()
        iterator = _datastore_query._QueryIteratorImpl(query)
        assert iterator._next_batch().result() is None
        assert iterator._index == 0
        assert len(iterator._batch) == 3
        assert iterator._batch[0].result_pb.entity == entity1
        assert (
            iterator._batch[0].result_type
            == query_pb2.EntityResult.ResultType.PROJECTION
        )
        assert iterator._batch[0].order_by is None
        assert iterator._has_next_batch
        assert iterator._query.start_cursor.cursor == b"abc"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._datastore_run_query")
    def test__next_batch_has_more_w_offset_and_limit(_datastore_run_query):
        """Regression test for Issue #236

        https://github.com/googleapis/python-ndb/issues/236
        """
        entity1 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
            )
        )
        entity2 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=43)],
            )
        )
        entity3 = mock.Mock(
            key=entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=44)],
            )
        )
        entity_results = [
            mock.Mock(entity=entity1, cursor=b"a"),
            mock.Mock(entity=entity2, cursor=b"b"),
            mock.Mock(entity=entity3, cursor=b"c"),
        ]
        _datastore_run_query.return_value = utils.future_result(
            mock.Mock(
                batch=mock.Mock(
                    entity_result_type=query_pb2.EntityResult.ResultType.FULL,
                    entity_results=entity_results,
                    end_cursor=b"abc",
                    skipped_results=5,
                    more_results=query_pb2.QueryResultBatch.MoreResultsType.NOT_FINISHED,
                )
            )
        )

        query = query_module.QueryOptions(offset=5, limit=5)
        iterator = _datastore_query._QueryIteratorImpl(query)
        assert iterator._next_batch().result() is None
        assert iterator._index == 0
        assert len(iterator._batch) == 3
        assert iterator._batch[0].result_pb.entity == entity1
        assert iterator._batch[0].result_type == query_pb2.EntityResult.ResultType.FULL
        assert iterator._batch[0].order_by is None
        assert iterator._has_next_batch
        assert iterator._query.start_cursor.cursor == b"abc"
        assert iterator._query.offset == 0
        assert iterator._query.limit == 2

    @staticmethod
    def test_next_done():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator.has_next = mock.Mock(return_value=False)
        iterator._cursor_before = b"abc"
        iterator._cursor_after = b"bcd"
        with pytest.raises(StopIteration):
            iterator.next()

        with pytest.raises(exceptions.BadArgumentError):
            iterator.cursor_before()

        assert iterator.cursor_after() == b"bcd"

    @staticmethod
    def test_next_raw():
        iterator = _datastore_query._QueryIteratorImpl("foo", raw=True)
        iterator.has_next = mock.Mock(return_value=True)
        iterator._index = 0
        result = mock.Mock(cursor=b"abc")
        iterator._batch = [result]
        assert iterator.next() is result
        assert iterator._index == 1
        assert iterator._cursor_after == b"abc"

    @staticmethod
    def test_next_entity():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator.has_next = mock.Mock(return_value=True)
        iterator._index = 1
        iterator._cursor_before = b"abc"
        result = mock.Mock(cursor=b"bcd")
        iterator._batch = [None, result]
        assert iterator.next() is result.entity.return_value
        assert iterator._index == 2
        assert iterator._cursor_after == b"bcd"

    @staticmethod
    def test__peek():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._index = 1
        iterator._batch = ["a", "b", "c"]
        assert iterator._peek() == "b"

    @staticmethod
    def test__peek_key_error():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        with pytest.raises(KeyError):
            iterator._peek()

    @staticmethod
    def test_cursor_before():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._cursor_before = "foo"
        assert iterator.cursor_before() == "foo"

    @staticmethod
    def test_cursor_before_no_cursor():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        with pytest.raises(exceptions.BadArgumentError):
            iterator.cursor_before()

    @staticmethod
    def test_cursor_after():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        iterator._cursor_after = "foo"
        assert iterator.cursor_after() == "foo"

    @staticmethod
    def test_cursor_after_no_cursor():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        with pytest.raises(exceptions.BadArgumentError):
            iterator.cursor_after()

    @staticmethod
    def test_index_list():
        iterator = _datastore_query._QueryIteratorImpl("foo")
        with pytest.raises(NotImplementedError):
            iterator.index_list()


class Test_PostFilterQueryIteratorImpl:
    @staticmethod
    def test_constructor():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(offset=20, limit=10, filters=foo == "this")
        predicate = object()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, predicate)
        assert iterator._result_set._query == query_module.QueryOptions(
            filters=foo == "this"
        )
        assert iterator._offset == 20
        assert iterator._limit == 10
        assert iterator._predicate is predicate

    @staticmethod
    def test_has_next():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        iterator.has_next_async = mock.Mock(return_value=utils.future_result("bar"))
        assert iterator.has_next() == "bar"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_next_loaded():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        iterator._next_result = "foo"
        assert iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_iterate_async():
        def predicate(result):
            return result.result % 2 == 0

        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, predicate)
        iterator._result_set = MockResultSet([1, 2, 3, 4, 5, 6, 7])

        @tasklets.tasklet
        def iterate():
            results = []
            while (yield iterator.has_next_async()):
                results.append(iterator.next())
            raise tasklets.Return(results)

        assert iterate().result() == [2, 4, 6]

        with pytest.raises(StopIteration):
            iterator.next()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_iterate_async_raw():
        def predicate(result):
            return result.result % 2 == 0

        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(
            query, predicate, raw=True
        )
        iterator._result_set = MockResultSet([1, 2, 3, 4, 5, 6, 7])

        @tasklets.tasklet
        def iterate():
            results = []
            while (yield iterator.has_next_async()):
                results.append(iterator.next())
            raise tasklets.Return(results)

        assert iterate().result() == [
            MockResult(2),
            MockResult(4),
            MockResult(6),
        ]

        with pytest.raises(StopIteration):
            iterator.next()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_iterate_async_w_limit_and_offset():
        def predicate(result):
            return result.result % 2 == 0

        query = query_module.QueryOptions(offset=1, limit=2)
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, predicate)
        iterator._result_set = MockResultSet([1, 2, 3, 4, 5, 6, 7, 8])

        @tasklets.tasklet
        def iterate():
            results = []
            while (yield iterator.has_next_async()):
                results.append(iterator.next())
            raise tasklets.Return(results)

        assert iterate().result() == [4, 6]

        with pytest.raises(StopIteration):
            iterator.next()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_probably_has_next_next_loaded():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        iterator._next_result = "foo"
        assert iterator.probably_has_next() is True

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_probably_has_next_delegate():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        iterator._result_set._next_result = "foo"
        assert iterator.probably_has_next() is True

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_probably_has_next_doesnt():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        iterator._result_set._batch = []
        iterator._result_set._index = 0
        assert iterator.probably_has_next() is False

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_cursor_before():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        iterator._cursor_before = "himom"
        assert iterator.cursor_before() == "himom"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_cursor_before_no_cursor():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        with pytest.raises(exceptions.BadArgumentError):
            iterator.cursor_before()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_cursor_after():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        iterator._cursor_after = "himom"
        assert iterator.cursor_after() == "himom"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_cursor_after_no_cursor():
        query = query_module.QueryOptions()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, "predicate")
        with pytest.raises(exceptions.BadArgumentError):
            iterator.cursor_after()

    @staticmethod
    def test__more_results_after_limit():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(offset=20, limit=10, filters=foo == "this")
        predicate = object()
        iterator = _datastore_query._PostFilterQueryIteratorImpl(query, predicate)
        assert iterator._result_set._query == query_module.QueryOptions(
            filters=foo == "this"
        )
        assert iterator._offset == 20
        assert iterator._limit == 10
        assert iterator._predicate is predicate

        iterator._result_set._more_results_after_limit = False
        assert iterator._more_results_after_limit is False

        iterator._result_set._more_results_after_limit = True
        assert iterator._more_results_after_limit is True


class Test_MultiQueryIteratorImpl:
    @staticmethod
    def test_constructor():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            offset=20,
            limit=10,
            filters=query_module.OR(foo == "this", foo == "that"),
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        assert iterator._result_sets[0]._query == query_module.QueryOptions(
            filters=foo == "this"
        )
        assert iterator._result_sets[1]._query == query_module.QueryOptions(
            filters=foo == "that"
        )
        assert not iterator._sortable
        assert iterator._offset == 20
        assert iterator._limit == 10

    @staticmethod
    def test_constructor_sortable():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that"),
            order_by=["foo"],
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        assert iterator._result_sets[0]._query == query_module.QueryOptions(
            filters=foo == "this", order_by=["foo"]
        )
        assert iterator._result_sets[1]._query == query_module.QueryOptions(
            filters=foo == "that", order_by=["foo"]
        )
        assert iterator._sortable

    @staticmethod
    def test_constructor_sortable_with_projection():
        foo = model.StringProperty("foo")
        order_by = [query_module.PropertyOrder("foo")]
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that"),
            order_by=order_by,
            projection=["foo"],
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        assert iterator._result_sets[0]._query == query_module.QueryOptions(
            filters=foo == "this",
            order_by=order_by,
            projection=["foo"],
        )
        assert iterator._result_sets[1]._query == query_module.QueryOptions(
            filters=foo == "that",
            order_by=order_by,
            projection=["foo"],
        )
        assert iterator._sortable

    @staticmethod
    def test_constructor_sortable_with_projection_needs_extra():
        foo = model.StringProperty("foo")
        order_by = [query_module.PropertyOrder("foo")]
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that"),
            order_by=order_by,
            projection=["bar"],
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        assert iterator._result_sets[0]._query == query_module.QueryOptions(
            filters=foo == "this",
            order_by=order_by,
            projection=["bar", "foo"],
        )
        assert iterator._result_sets[1]._query == query_module.QueryOptions(
            filters=foo == "that",
            order_by=order_by,
            projection=["bar", "foo"],
        )
        assert iterator._sortable
        assert not iterator._coerce_keys_only

    @staticmethod
    def test_constructor_sortable_with_projection_needs_extra_keys_only():
        foo = model.StringProperty("foo")
        order_by = [query_module.PropertyOrder("foo")]
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that"),
            order_by=order_by,
            projection=("__key__",),
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        assert iterator._result_sets[0]._query == query_module.QueryOptions(
            filters=foo == "this",
            order_by=order_by,
            projection=["__key__", "foo"],
        )
        assert iterator._result_sets[1]._query == query_module.QueryOptions(
            filters=foo == "that",
            order_by=order_by,
            projection=["__key__", "foo"],
        )
        assert iterator._sortable
        assert iterator._coerce_keys_only

    @staticmethod
    def test_iter():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        assert iter(iterator) is iterator

    @staticmethod
    def test_has_next():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator.has_next_async = mock.Mock(return_value=utils.future_result("bar"))
        assert iterator.has_next() == "bar"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_next_loaded():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._next_result = "foo"
        assert iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_next_async_exhausted():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._result_sets = []
        assert not iterator.has_next_async().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_next_with_extra_projections():
        foo = model.StringProperty("foo")
        order_by = [
            query_module.PropertyOrder("foo"),
            query_module.PropertyOrder("food"),
        ]
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that"),
            order_by=order_by,
            projection=["bar"],
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._next_result = next_result = mock.Mock(
            result_pb=mock.Mock(
                entity=mock.Mock(
                    properties={"foo": 1, "bar": "two"},
                    spec=("properties",),
                ),
                spec=("entity",),
            ),
            spec=("result_pb",),
        )
        iterator._raw = True

        assert iterator.next() is next_result
        assert "foo" not in next_result.result_pb.entity.properties

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_next_coerce_keys_only():
        foo = model.StringProperty("foo")
        order_by = [
            query_module.PropertyOrder("foo"),
            query_module.PropertyOrder("food"),
        ]
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that"),
            order_by=order_by,
            projection=["__key__"],
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._next_result = next_result = mock.Mock(
            result_pb=mock.Mock(
                entity=mock.Mock(
                    properties={"foo": 1, "bar": "two"},
                    spec=("properties",),
                ),
                spec=("entity",),
            ),
            entity=mock.Mock(
                return_value=mock.Mock(
                    _key="thekey",
                )
            ),
            spec=("result_pb", "entity"),
        )

        assert iterator.next() == "thekey"
        assert "foo" not in next_result.result_pb.entity.properties

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_iterate_async():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._result_sets = [
            MockResultSet(["a", "c", "e", "g", "i"]),
            MockResultSet(["b", "d", "f", "h", "j"]),
        ]

        @tasklets.tasklet
        def iterate():
            results = []
            while (yield iterator.has_next_async()):
                results.append(iterator.next())
            raise tasklets.Return(results)

        assert iterate().result() == [
            "a",
            "c",
            "e",
            "g",
            "i",
            "b",
            "d",
            "f",
            "h",
            "j",
        ]

        with pytest.raises(StopIteration):
            iterator.next()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_iterate_async_raw():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query, raw=True)
        iterator._result_sets = [
            MockResultSet(["a", "c", "e", "g", "i"]),
            MockResultSet(["b", "d", "f", "h", "j"]),
        ]

        @tasklets.tasklet
        def iterate():
            results = []
            while (yield iterator.has_next_async()):
                results.append(iterator.next())
            raise tasklets.Return(results)

        assert iterate().result() == [
            MockResult("a"),
            MockResult("c"),
            MockResult("e"),
            MockResult("g"),
            MockResult("i"),
            MockResult("b"),
            MockResult("d"),
            MockResult("f"),
            MockResult("h"),
            MockResult("j"),
        ]

        with pytest.raises(StopIteration):
            iterator.next()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_iterate_async_ordered():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._sortable = True
        iterator._result_sets = [
            MockResultSet(["a", "c", "e", "g", "i"]),
            MockResultSet(["b", "d", "f", "h", "j"]),
        ]

        @tasklets.tasklet
        def iterate():
            results = []
            while (yield iterator.has_next_async()):
                results.append(iterator.next())
            raise tasklets.Return(results)

        assert iterate().result() == [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
        ]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_iterate_async_ordered_limit_and_offset():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            offset=5,
            limit=4,
            filters=query_module.OR(foo == "this", foo == "that"),
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._sortable = True
        iterator._result_sets = [
            MockResultSet(["a", "c", "e", "g", "i"]),
            MockResultSet(["a", "b", "d", "f", "h", "j"]),
        ]

        @tasklets.tasklet
        def iterate():
            results = []
            while (yield iterator.has_next_async()):
                results.append(iterator.next())
            raise tasklets.Return(results)

        assert iterate().result() == ["f", "g", "h", "i"]

    @staticmethod
    def test_probably_has_next_loaded():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._next = "foo"
        assert iterator.probably_has_next()

    @staticmethod
    def test_probably_has_next_delegate():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._result_sets = [MockResultSet(["a"]), MockResultSet([])]
        assert iterator.probably_has_next()

    @staticmethod
    def test_probably_has_next_doesnt():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        iterator._result_sets = [MockResultSet([])]
        assert not iterator.probably_has_next()

    @staticmethod
    def test_cursor_before():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        with pytest.raises(exceptions.BadArgumentError):
            iterator.cursor_before()

    @staticmethod
    def test_cursor_after():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        with pytest.raises(exceptions.BadArgumentError):
            iterator.cursor_after()

    @staticmethod
    def test_index_list():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(
            filters=query_module.OR(foo == "this", foo == "that")
        )
        iterator = _datastore_query._MultiQueryIteratorImpl(query)
        with pytest.raises(NotImplementedError):
            iterator.index_list()


class MockResult:
    def __init__(self, result):
        self.result = result
        self.cursor = "cursor-" + str(result)

    def entity(self):
        return self.result

    @property
    def result_pb(self):
        return MockResultPB(self.result)

    def __eq__(self, other):
        return self.result == getattr(other, "result", object())


class MockResultPB:
    def __init__(self, result):
        self.result = result
        self.entity = self
        self.key = self
        self._pb = MockResultPB_pb(result)


class MockResultPB_pb:
    def __init__(self, result):
        self.result = result

    def SerializeToString(self):
        return self.result


class MockResultSet:
    def __init__(self, results):
        self.results = results
        self.len = len(results)
        self.index = 0

    def has_next_async(self):
        return utils.future_result(self.index < self.len)

    def next(self):
        result = self._peek()
        self.index += 1
        return MockResult(result)

    def _peek(self):
        return self.results[self.index]

    def probably_has_next(self):
        return self.index < self.len


class Test_Result:
    @staticmethod
    def test_constructor_defaults():
        result = _datastore_query._Result(
            result_type=None,
            result_pb=query_pb2.EntityResult(),
        )
        assert result.order_by is None
        assert result._query_options is None

    @staticmethod
    def test_constructor_order_by():
        order = query_module.PropertyOrder("foo")
        result = _datastore_query._Result(
            result_type=None, result_pb=query_pb2.EntityResult(), order_by=[order]
        )
        assert result.order_by == [order]

    @staticmethod
    def test_constructor_query_options():
        options = query_module.QueryOptions(use_cache=False)
        result = _datastore_query._Result(
            result_type=None, result_pb=query_pb2.EntityResult(), query_options=options
        )
        assert result._query_options == options

    @staticmethod
    def test_total_ordering():
        def result(foo, bar=0, baz=""):
            return _datastore_query._Result(
                result_type=None,
                result_pb=query_pb2.EntityResult(
                    entity=entity_pb2.Entity(
                        properties={
                            "foo": entity_pb2.Value(string_value=foo),
                            "bar": entity_pb2.Value(integer_value=bar),
                            "baz": entity_pb2.Value(string_value=baz),
                        }
                    )
                ),
                order_by=[
                    query_module.PropertyOrder("foo"),
                    query_module.PropertyOrder("bar", reverse=True),
                ],
            )

        assert result("a") < result("b")
        assert result("b") > result("a")
        assert result("a") != result("b")
        assert result("a") == result("a")

        assert result("a", 2) < result("a", 1)
        assert result("a", 1) > result("a", 2)
        assert result("a", 1) != result("a", 2)
        assert result("a", 1) == result("a", 1)

        assert result("a", 1, "femur") == result("a", 1, "patella")
        assert result("a") != "a"

    @staticmethod
    def test__compare_no_order_by():
        result = _datastore_query._Result(
            None, mock.Mock(cursor=b"123", spec=("cursor",))
        )
        with pytest.raises(NotImplementedError):
            result._compare("other")

    @staticmethod
    def test__compare_with_order_by():
        result = _datastore_query._Result(
            None,
            mock.Mock(
                cursor=b"123",
                spec=("cursor",),
            ),
            [
                query_module.PropertyOrder("foo"),
                query_module.PropertyOrder("bar", reverse=True),
            ],
        )
        assert result._compare("other") == NotImplemented

    @staticmethod
    def test__compare_with_order_by_entity_key():
        def result(key_path):
            key_pb = entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[key_path],
            )
            return _datastore_query._Result(
                result_type=None,
                result_pb=query_pb2.EntityResult(entity=entity_pb2.Entity(key=key_pb)),
                order_by=[
                    query_module.PropertyOrder("__key__"),
                ],
            )

        assert result(entity_pb2.Key.PathElement(kind="ThisKind", name="a")) < result(
            entity_pb2.Key.PathElement(kind="ThisKind", name="b")
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", name="b")) > result(
            entity_pb2.Key.PathElement(kind="ThisKind", name="a")
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", name="a")) != result(
            entity_pb2.Key.PathElement(kind="ThisKind", name="b")
        )

        assert result(entity_pb2.Key.PathElement(kind="ThisKind", id=1)) < result(
            entity_pb2.Key.PathElement(kind="ThisKind", id=2)
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", id=2)) > result(
            entity_pb2.Key.PathElement(kind="ThisKind", id=1)
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", id=1)) != result(
            entity_pb2.Key.PathElement(kind="ThisKind", id=2)
        )

    @staticmethod
    def test__compare_with_order_by_key_property():
        def result(foo_key_path):
            foo_key = entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[foo_key_path],
            )

            return _datastore_query._Result(
                result_type=None,
                result_pb=query_pb2.EntityResult(
                    entity=entity_pb2.Entity(
                        properties={
                            "foo": entity_pb2.Value(key_value=foo_key),
                        }
                    )
                ),
                order_by=[
                    query_module.PropertyOrder("foo"),
                ],
            )

        assert result(entity_pb2.Key.PathElement(kind="ThisKind", name="a")) < result(
            entity_pb2.Key.PathElement(kind="ThisKind", name="b")
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", name="b")) > result(
            entity_pb2.Key.PathElement(kind="ThisKind", name="a")
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", name="a")) != result(
            entity_pb2.Key.PathElement(kind="ThisKind", name="b")
        )

        assert result(entity_pb2.Key.PathElement(kind="ThisKind", id=1)) < result(
            entity_pb2.Key.PathElement(kind="ThisKind", id=2)
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", id=2)) > result(
            entity_pb2.Key.PathElement(kind="ThisKind", id=1)
        )
        assert result(entity_pb2.Key.PathElement(kind="ThisKind", id=1)) != result(
            entity_pb2.Key.PathElement(kind="ThisKind", id=2)
        )

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_query.model")
    def test_entity_unsupported_result_type(model):
        model._entity_from_protobuf.return_value = "bar"
        result = _datastore_query._Result(
            "foo",
            mock.Mock(entity="foo", cursor=b"123", spec=("entity", "cursor")),
        )
        with pytest.raises(NotImplementedError):
            result.entity()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.model")
    def test_entity_full_entity(model):
        key_pb = entity_pb2.Key(
            partition_id=entity_pb2.PartitionId(project_id="testing"),
            path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
        )
        entity_pb = mock.Mock(key=key_pb)
        entity = mock.Mock(key=key_module.Key("ThisKind", 42))
        model._entity_from_protobuf.return_value = entity
        result = _datastore_query._Result(
            _datastore_query.RESULT_TYPE_FULL,
            mock.Mock(entity=entity_pb, cursor=b"123", spec=("entity", "cursor")),
        )

        context = context_module.get_context()

        assert len(context.cache) == 0
        assert result.entity() is entity
        model._entity_from_protobuf.assert_called_once_with(entity_pb)

        # Regression test for #752: ensure cache is updated after querying
        assert len(context.cache) == 1

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.model")
    def test_entity_full_entity_cached(model):
        key = key_module.Key("ThisKind", 42)
        key_pb = entity_pb2.Key(
            partition_id=entity_pb2.PartitionId(project_id="testing"),
            path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
        )
        entity = mock.Mock(key=key_pb)
        cached_entity = mock.Mock(key=key_pb, _key=key)
        context = context_module.get_context()
        context.cache[key] = cached_entity
        model._entity_from_protobuf.return_value = entity
        result = _datastore_query._Result(
            _datastore_query.RESULT_TYPE_FULL,
            mock.Mock(entity=entity, cursor=b"123", spec=("entity", "cursor")),
        )

        assert result.entity() is not entity
        assert result.entity() is cached_entity

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.model")
    def test_entity_full_entity_no_cache(model):
        context = context_module.get_context()
        with context.new(cache_policy=False).use():
            key_pb = entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
            )
            entity = mock.Mock(key=key_pb)
            model._entity_from_protobuf.return_value = entity
            result = _datastore_query._Result(
                _datastore_query.RESULT_TYPE_FULL,
                mock.Mock(entity=entity, cursor=b"123", spec=("entity", "cursor")),
            )
            assert result.entity() is entity

            # Regression test for #752: ensure cache does not grow (i.e. use up memory)
            assert len(context.cache) == 0

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.model")
    def test_entity_full_entity_no_cache_via_cache_options(model):
        context = context_module.get_context()
        with context.new().use():
            key_pb = entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
            )
            entity = mock.Mock(key=key_pb)
            model._entity_from_protobuf.return_value = entity
            result = _datastore_query._Result(
                _datastore_query.RESULT_TYPE_FULL,
                mock.Mock(entity=entity, cursor=b"123", spec=("entity", "cursor")),
                query_options=query_module.QueryOptions(use_cache=False),
            )
            assert result.entity() is entity

            # Regression test for #752: ensure cache does not grow (i.e. use up memory)
            assert len(context.cache) == 0

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query.model")
    def test_entity_full_entity_cache_options_true(model):
        key_pb = entity_pb2.Key(
            partition_id=entity_pb2.PartitionId(project_id="testing"),
            path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
        )
        entity_pb = mock.Mock(key=key_pb)
        entity = mock.Mock(key=key_module.Key("ThisKind", 42))
        model._entity_from_protobuf.return_value = entity
        result = _datastore_query._Result(
            _datastore_query.RESULT_TYPE_FULL,
            mock.Mock(entity=entity_pb, cursor=b"123", spec=("entity", "cursor")),
            query_options=query_module.QueryOptions(use_cache=True),
        )

        context = context_module.get_context()

        assert len(context.cache) == 0
        assert result.entity() is entity
        model._entity_from_protobuf.assert_called_once_with(entity_pb)

        # Regression test for #752: ensure cache is updated after querying
        assert len(context.cache) == 1

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_entity_key_only():
        key_pb = entity_pb2.Key(
            partition_id=entity_pb2.PartitionId(project_id="testing"),
            path=[entity_pb2.Key.PathElement(kind="ThisKind", id=42)],
        )
        result = _datastore_query._Result(
            _datastore_query.RESULT_TYPE_KEY_ONLY,
            mock.Mock(
                entity=mock.Mock(key=key_pb, spec=("key",)),
                cursor=b"123",
                spec=("entity", "cursor"),
            ),
        )
        assert result.entity() == key_module.Key("ThisKind", 42)

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_query.model")
    def test_entity_projection(model):
        entity = mock.Mock(spec=("_set_projection",))
        entity_pb = mock.Mock(properties={"a": 0, "b": 1}, spec=("properties",))
        model._entity_from_protobuf.return_value = entity
        result = _datastore_query._Result(
            _datastore_query.RESULT_TYPE_PROJECTION,
            mock.Mock(entity=entity_pb, cursor=b"123", spec=("entity", "cursor")),
        )

        assert result.entity() is entity
        model._entity_from_protobuf.assert_called_once_with(entity_pb)
        projection = entity._set_projection.call_args[0][0]
        assert sorted(projection) == ["a", "b"]
        entity._set_projection.assert_called_once_with(projection)


@pytest.mark.usefixtures("in_context")
class Test__query_to_protobuf:
    @staticmethod
    def test_no_args():
        query = query_module.QueryOptions()
        assert _datastore_query._query_to_protobuf(query) == query_pb2.Query()

    @staticmethod
    def test_kind():
        query = query_module.QueryOptions(kind="Foo")
        assert _datastore_query._query_to_protobuf(query) == query_pb2.Query(
            kind=[query_pb2.KindExpression(name="Foo")]
        )

    @staticmethod
    def test_ancestor():
        key = key_module.Key("Foo", 123)
        query = query_module.QueryOptions(ancestor=key)
        expected_pb = query_pb2.Query(
            filter=query_pb2.Filter(
                property_filter=query_pb2.PropertyFilter(
                    property=query_pb2.PropertyReference(name="__key__"),
                    op=query_pb2.PropertyFilter.Operator.HAS_ANCESTOR,
                )
            )
        )
        expected_pb.filter.property_filter.value.key_value._pb.CopyFrom(
            key._key.to_protobuf()._pb
        )
        assert _datastore_query._query_to_protobuf(query) == expected_pb

    @staticmethod
    def test_ancestor_with_property_filter():
        key = key_module.Key("Foo", 123)
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(ancestor=key, filters=foo == "bar")
        query_pb = _datastore_query._query_to_protobuf(query)

        filter_pb = query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="foo"),
            op=query_pb2.PropertyFilter.Operator.EQUAL,
            value=entity_pb2.Value(string_value="bar"),
        )
        ancestor_pb = query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="__key__"),
            op=query_pb2.PropertyFilter.Operator.HAS_ANCESTOR,
        )
        ancestor_pb.value.key_value._pb.CopyFrom(key._key.to_protobuf()._pb)
        expected_pb = query_pb2.Query(
            filter=query_pb2.Filter(
                composite_filter=query_pb2.CompositeFilter(
                    op=query_pb2.CompositeFilter.Operator.AND,
                    filters=[
                        query_pb2.Filter(property_filter=filter_pb),
                        query_pb2.Filter(property_filter=ancestor_pb),
                    ],
                )
            )
        )
        assert query_pb == expected_pb

    @staticmethod
    def test_ancestor_with_composite_filter():
        key = key_module.Key("Foo", 123)
        foo = model.StringProperty("foo")
        food = model.StringProperty("food")
        query = query_module.QueryOptions(
            ancestor=key,
            filters=query_module.AND(foo == "bar", food == "barn"),
        )
        query_pb = _datastore_query._query_to_protobuf(query)

        filter_pb1 = query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="foo"),
            op=query_pb2.PropertyFilter.Operator.EQUAL,
            value=entity_pb2.Value(string_value="bar"),
        )
        filter_pb2 = query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="food"),
            op=query_pb2.PropertyFilter.Operator.EQUAL,
            value=entity_pb2.Value(string_value="barn"),
        )
        ancestor_pb = query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="__key__"),
            op=query_pb2.PropertyFilter.Operator.HAS_ANCESTOR,
        )
        ancestor_pb.value.key_value._pb.CopyFrom(key._key.to_protobuf()._pb)
        expected_pb = query_pb2.Query(
            filter=query_pb2.Filter(
                composite_filter=query_pb2.CompositeFilter(
                    op=query_pb2.CompositeFilter.Operator.AND,
                    filters=[
                        query_pb2.Filter(property_filter=filter_pb1),
                        query_pb2.Filter(property_filter=filter_pb2),
                        query_pb2.Filter(property_filter=ancestor_pb),
                    ],
                )
            )
        )
        assert query_pb == expected_pb

    @staticmethod
    def test_projection():
        query = query_module.QueryOptions(projection=("a", "b"))
        expected_pb = query_pb2.Query(
            projection=[
                query_pb2.Projection(property=query_pb2.PropertyReference(name="a")),
                query_pb2.Projection(property=query_pb2.PropertyReference(name="b")),
            ]
        )
        assert _datastore_query._query_to_protobuf(query) == expected_pb

    @staticmethod
    def test_distinct_on():
        query = query_module.QueryOptions(distinct_on=("a", "b"))
        expected_pb = query_pb2.Query(
            distinct_on=[
                query_pb2.PropertyReference(name="a"),
                query_pb2.PropertyReference(name="b"),
            ]
        )
        assert _datastore_query._query_to_protobuf(query) == expected_pb

    @staticmethod
    def test_order_by():
        query = query_module.QueryOptions(
            order_by=[
                query_module.PropertyOrder("a"),
                query_module.PropertyOrder("b", reverse=True),
            ]
        )
        expected_pb = query_pb2.Query(
            order=[
                query_pb2.PropertyOrder(
                    property=query_pb2.PropertyReference(name="a"),
                    direction=query_pb2.PropertyOrder.Direction.ASCENDING,
                ),
                query_pb2.PropertyOrder(
                    property=query_pb2.PropertyReference(name="b"),
                    direction=query_pb2.PropertyOrder.Direction.DESCENDING,
                ),
            ]
        )
        assert _datastore_query._query_to_protobuf(query) == expected_pb

    @staticmethod
    def test_filter_pb():
        foo = model.StringProperty("foo")
        query = query_module.QueryOptions(kind="Foo", filters=(foo == "bar"))
        query_pb = _datastore_query._query_to_protobuf(query)

        filter_pb = query_pb2.PropertyFilter(
            property=query_pb2.PropertyReference(name="foo"),
            op=query_pb2.PropertyFilter.Operator.EQUAL,
            value=entity_pb2.Value(string_value="bar"),
        )
        expected_pb = query_pb2.Query(
            kind=[query_pb2.KindExpression(name="Foo")],
            filter=query_pb2.Filter(property_filter=filter_pb),
        )
        assert query_pb == expected_pb

    @staticmethod
    def test_offset():
        query = query_module.QueryOptions(offset=20)
        assert _datastore_query._query_to_protobuf(query) == query_pb2.Query(offset=20)

    @staticmethod
    def test_limit():
        query = query_module.QueryOptions(limit=20)
        expected_pb = query_pb2.Query()
        expected_pb._pb.limit.value = 20
        assert _datastore_query._query_to_protobuf(query) == expected_pb

    @staticmethod
    def test_start_cursor():
        query = query_module.QueryOptions(start_cursor=_datastore_query.Cursor(b"abc"))
        assert _datastore_query._query_to_protobuf(query) == query_pb2.Query(
            start_cursor=b"abc"
        )

    @staticmethod
    def test_end_cursor():
        query = query_module.QueryOptions(end_cursor=_datastore_query.Cursor(b"abc"))
        assert _datastore_query._query_to_protobuf(query) == query_pb2.Query(
            end_cursor=b"abc"
        )


class Test__datastore_run_query:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_query._datastore_api")
    def test_it(_datastore_api):
        query = query_module.QueryOptions(project="testing", namespace="")
        query_pb = _datastore_query._query_to_protobuf(query)
        _datastore_api.make_call.return_value = utils.future_result("foo")
        read_options = datastore_pb2.ReadOptions()
        request = datastore_pb2.RunQueryRequest(
            project_id="testing",
            database_id=None,
            partition_id=entity_pb2.PartitionId(project_id="testing", namespace_id=""),
            query=query_pb,
            read_options=read_options,
        )
        metadata = ("x-goog-request-params", "project_id=testing")
        _datastore_api._add_routing_info.return_value = metadata
        _datastore_api.get_read_options.return_value = read_options
        assert _datastore_query._datastore_run_query(query).result() == "foo"
        _datastore_api.make_call.assert_called_once_with(
            "run_query", request, timeout=None, metadata=metadata
        )
        _datastore_api.get_read_options.assert_called_once_with(query)


class TestCursor:
    @staticmethod
    def test_constructor():
        cursor = _datastore_query.Cursor(b"123")
        assert cursor.cursor == b"123"

    @staticmethod
    def test_constructor_cursor_and_urlsafe():
        with pytest.raises(TypeError):
            _datastore_query.Cursor(b"123", urlsafe="what?")

    @staticmethod
    def test_constructor_urlsafe():
        urlsafe = base64.urlsafe_b64encode(b"123")
        cursor = _datastore_query.Cursor(urlsafe=urlsafe)
        assert cursor.cursor == b"123"

    @staticmethod
    def test_from_websafe_string():
        urlsafe = base64.urlsafe_b64encode(b"123")
        cursor = _datastore_query.Cursor.from_websafe_string(urlsafe)
        assert cursor.cursor == b"123"

    @staticmethod
    def test_to_websafe_string():
        urlsafe = base64.urlsafe_b64encode(b"123")
        cursor = _datastore_query.Cursor(b"123")
        assert cursor.to_websafe_string() == urlsafe

    @staticmethod
    def test_urlsafe():
        urlsafe = base64.urlsafe_b64encode(b"123")
        cursor = _datastore_query.Cursor(b"123")
        assert cursor.urlsafe() == urlsafe

    @staticmethod
    def test__eq__same():
        assert _datastore_query.Cursor(b"123") == _datastore_query.Cursor(b"123")
        assert not _datastore_query.Cursor(b"123") != _datastore_query.Cursor(b"123")

    @staticmethod
    def test__eq__different():
        assert _datastore_query.Cursor(b"123") != _datastore_query.Cursor(b"234")
        assert not _datastore_query.Cursor(b"123") == _datastore_query.Cursor(b"234")

    @staticmethod
    def test__eq__different_type():
        assert _datastore_query.Cursor(b"123") != b"234"
        assert not _datastore_query.Cursor(b"123") == b"234"

    @staticmethod
    def test__hash__():
        assert hash(_datastore_query.Cursor(b"123")) == hash(b"123")
