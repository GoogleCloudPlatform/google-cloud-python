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

import datetime

import mock
import pytest

from google.cloud.firestore_v1 import pipeline_stages as stages
from tests.unit.v1._test_helpers import make_client


def _make_base_query(*args, **kwargs):
    from google.cloud.firestore_v1.base_query import BaseQuery

    return BaseQuery(*args, **kwargs)


def _make_base_query_all_fields(
    limit=9876,
    offset=12,
    skip_fields=(),
    parent=None,
    all_descendants=True,
):
    kwargs = {
        "projection": mock.sentinel.projection,
        "field_filters": mock.sentinel.filters,
        "orders": mock.sentinel.orders,
        "limit": limit,
        "offset": offset,
        "start_at": mock.sentinel.start_at,
        "end_at": mock.sentinel.end_at,
        "all_descendants": all_descendants,
    }

    for field in skip_fields:
        kwargs.pop(field)

    if parent is None:
        parent = mock.sentinel.parent

    return _make_base_query(parent, **kwargs)


def test_basequery_constructor_defaults():
    query = _make_base_query(mock.sentinel.parent)
    assert query._parent is mock.sentinel.parent
    assert query._projection is None
    assert query._field_filters == ()
    assert query._orders == ()
    assert query._limit is None
    assert query._offset is None
    assert query._start_at is None
    assert query._end_at is None
    assert not query._all_descendants


def test_basequery_constructor_explicit():
    limit = 234
    offset = 56
    query = _make_base_query_all_fields(limit=limit, offset=offset)
    assert query._parent is mock.sentinel.parent
    assert query._projection is mock.sentinel.projection
    assert query._field_filters is mock.sentinel.filters
    assert query._orders == mock.sentinel.orders
    assert query._limit == limit
    assert query._offset == offset
    assert query._start_at is mock.sentinel.start_at
    assert query._end_at is mock.sentinel.end_at
    assert query._all_descendants


def test_basequery__client_property():
    parent = mock.Mock(_client=mock.sentinel.client, spec=["_client"])
    query = _make_base_query(parent)
    assert query._client is mock.sentinel.client


def test_basequery___eq___other_type():
    query = _make_base_query_all_fields()
    other = object()
    assert not (query == other)


def test_basequery___eq___different_parent():
    parent = mock.sentinel.parent
    other_parent = mock.sentinel.other_parent
    query = _make_base_query_all_fields(parent=parent)
    other = _make_base_query_all_fields(parent=other_parent)
    assert not (query == other)


def test_basequery___eq___different_projection():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, skip_fields=("projection",))
    query._projection = mock.sentinel.projection
    other = _make_base_query_all_fields(parent=parent, skip_fields=("projection",))
    other._projection = mock.sentinel.other_projection
    assert not (query == other)


def test_basequery___eq___different_field_filters():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, skip_fields=("field_filters",))
    query._field_filters = mock.sentinel.field_filters
    other = _make_base_query_all_fields(parent=parent, skip_fields=("field_filters",))
    other._field_filters = mock.sentinel.other_field_filters
    assert not (query == other)


def test_basequery___eq___different_orders():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, skip_fields=("orders",))
    query._orders = mock.sentinel.orders
    other = _make_base_query_all_fields(parent=parent, skip_fields=("orders",))
    other._orders = mock.sentinel.other_orders
    assert not (query == other)


def test_basequery___eq___different_limit():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, limit=10)
    other = _make_base_query_all_fields(parent=parent, limit=20)
    assert not (query == other)


def test_basequery___eq___different_offset():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, offset=10)
    other = _make_base_query_all_fields(parent=parent, offset=20)
    assert not (query == other)


def test_basequery___eq___different_start_at():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, skip_fields=("start_at",))
    query._start_at = mock.sentinel.start_at
    other = _make_base_query_all_fields(parent=parent, skip_fields=("start_at",))
    other._start_at = mock.sentinel.other_start_at
    assert not (query == other)


def test_basequery___eq___different_end_at():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, skip_fields=("end_at",))
    query._end_at = mock.sentinel.end_at
    other = _make_base_query_all_fields(parent=parent, skip_fields=("end_at",))
    other._end_at = mock.sentinel.other_end_at
    assert not (query == other)


def test_basequery___eq___different_all_descendants():
    parent = mock.sentinel.parent
    query = _make_base_query_all_fields(parent=parent, all_descendants=True)
    other = _make_base_query_all_fields(parent=parent, all_descendants=False)
    assert not (query == other)


def test_basequery___eq___hit():
    query = _make_base_query_all_fields()
    other = _make_base_query_all_fields()
    assert query == other


def _compare_queries(query1, query2, *attr_names):
    attrs1 = query1.__dict__.copy()
    attrs2 = query2.__dict__.copy()

    assert len(attrs1) == len(attrs2)

    # The only different should be in ``attr_name``.
    for attr_name in attr_names:
        attrs1.pop(attr_name)
        attrs2.pop(attr_name)

    for key, value in attrs1.items():
        assert value is attrs2[key]


def test_basequery_select_invalid_path():
    query = _make_base_query(mock.sentinel.parent)

    with pytest.raises(ValueError):
        query.select(["*"])


def test_basequery_select():
    from google.cloud.firestore_v1.base_query import BaseQuery

    query1 = _make_base_query_all_fields(all_descendants=True)

    field_paths2 = ["foo", "bar"]
    query2 = query1.select(field_paths2)
    assert query2 is not query1
    assert isinstance(query2, BaseQuery)
    assert query2._projection == _make_projection_for_select(field_paths2)
    _compare_queries(query1, query2, "_projection")

    # Make sure it overrides.
    field_paths3 = ["foo.baz"]
    query3 = query2.select(field_paths3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._projection == _make_projection_for_select(field_paths3)
    _compare_queries(query2, query3, "_projection")


def test_basequery_where_invalid_path():
    query = _make_base_query(mock.sentinel.parent)

    with pytest.raises(ValueError):
        query.where("*", "==", 1)


def test_basequery_where():
    from google.cloud.firestore_v1.base_query import BaseQuery
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    query_inst = _make_base_query_all_fields(
        skip_fields=("field_filters",), all_descendants=True
    )
    new_query = query_inst.where("power.level", ">", 9000)

    assert query_inst is not new_query
    assert isinstance(new_query, BaseQuery)
    assert len(new_query._field_filters) == 1

    field_pb = new_query._field_filters[0]
    expected_pb = query.StructuredQuery.FieldFilter(
        field=query.StructuredQuery.FieldReference(field_path="power.level"),
        op=StructuredQuery.FieldFilter.Operator.GREATER_THAN,
        value=document.Value(integer_value=9000),
    )
    assert field_pb == expected_pb
    _compare_queries(query_inst, new_query, "_field_filters")


def _where_unary_helper(value, op_enum, op_string="=="):
    from google.cloud.firestore_v1.base_query import BaseQuery
    from google.cloud.firestore_v1.types import StructuredQuery

    query_inst = _make_base_query_all_fields(skip_fields=("field_filters",))
    field_path = "feeeld"
    new_query = query_inst.where(field_path, op_string, value)
    assert query_inst is not new_query
    assert isinstance(new_query, BaseQuery)
    assert len(new_query._field_filters) == 1

    field_pb = new_query._field_filters[0]
    expected_pb = StructuredQuery.UnaryFilter(
        field=StructuredQuery.FieldReference(field_path=field_path), op=op_enum
    )
    assert field_pb == expected_pb
    _compare_queries(query_inst, new_query, "_field_filters")


def _where_unary_helper_field_filter(value, op_enum, op_string="=="):
    from google.cloud.firestore_v1.base_query import BaseQuery, FieldFilter
    from google.cloud.firestore_v1.types import StructuredQuery

    query_inst = _make_base_query_all_fields(skip_fields=("field_filters",))
    field_path = "feeeld"

    filter = FieldFilter(field_path, op_string, value)
    new_query = query_inst.where(filter=filter)

    assert query_inst is not new_query
    assert isinstance(new_query, BaseQuery)
    assert len(new_query._field_filters) == 1

    field_pb = new_query._field_filters[0]
    expected_pb = StructuredQuery.UnaryFilter(
        field=StructuredQuery.FieldReference(field_path=filter.field_path), op=op_enum
    )
    assert field_pb == expected_pb
    _compare_queries(query_inst, new_query, "_field_filters")


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_eq_null(unary_helper_function):
    from google.cloud.firestore_v1.types import StructuredQuery

    op_enum = StructuredQuery.UnaryFilter.Operator.IS_NULL
    unary_helper_function(None, op_enum)


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_neq_null(unary_helper_function):
    from google.cloud.firestore_v1.types import StructuredQuery

    op_enum = StructuredQuery.UnaryFilter.Operator.IS_NOT_NULL
    unary_helper_function(None, op_enum, op_string="!=")


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_gt_null(unary_helper_function):
    from google.cloud.firestore_v1.base_query import _BAD_OP_NAN_NULL

    with pytest.raises(ValueError) as exc:
        unary_helper_function(None, 0, op_string=">")
    assert str(exc.value) == _BAD_OP_NAN_NULL


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_eq_nan(unary_helper_function):
    from google.cloud.firestore_v1.types import StructuredQuery

    op_enum = StructuredQuery.UnaryFilter.Operator.IS_NAN
    unary_helper_function(float("nan"), op_enum)


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_neq_nan(unary_helper_function):
    from google.cloud.firestore_v1.types import StructuredQuery

    op_enum = StructuredQuery.UnaryFilter.Operator.IS_NOT_NAN
    unary_helper_function(float("nan"), op_enum, op_string="!=")


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_le_nan(unary_helper_function):
    from google.cloud.firestore_v1.base_query import _BAD_OP_NAN_NULL

    with pytest.raises(ValueError) as exc:
        unary_helper_function(float("nan"), 0, op_string="<=")
    assert str(exc.value) == _BAD_OP_NAN_NULL


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_w_delete(unary_helper_function):
    from google.cloud.firestore_v1 import DELETE_FIELD
    from google.cloud.firestore_v1.base_query import _INVALID_WHERE_TRANSFORM

    with pytest.raises(ValueError) as exc:
        unary_helper_function(DELETE_FIELD, 0)
    assert str(exc.value) == _INVALID_WHERE_TRANSFORM


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_w_server_timestamp(unary_helper_function):
    from google.cloud.firestore_v1 import SERVER_TIMESTAMP
    from google.cloud.firestore_v1.base_query import _INVALID_WHERE_TRANSFORM

    with pytest.raises(ValueError) as exc:
        unary_helper_function(SERVER_TIMESTAMP, 0)
    assert str(exc.value) == _INVALID_WHERE_TRANSFORM


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_w_array_remove(unary_helper_function):
    from google.cloud.firestore_v1 import ArrayRemove
    from google.cloud.firestore_v1.base_query import _INVALID_WHERE_TRANSFORM

    with pytest.raises(ValueError) as exc:
        unary_helper_function(ArrayRemove([1, 3, 5]), 0)
    assert str(exc.value) == _INVALID_WHERE_TRANSFORM


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_w_array_union(unary_helper_function):
    from google.cloud.firestore_v1 import ArrayUnion
    from google.cloud.firestore_v1.base_query import _INVALID_WHERE_TRANSFORM

    with pytest.raises(ValueError) as exc:
        unary_helper_function(ArrayUnion([2, 4, 8]), 0)
    assert str(exc.value) == _INVALID_WHERE_TRANSFORM


@pytest.mark.parametrize(
    "unary_helper_function",
    [
        (_where_unary_helper),
        (_where_unary_helper_field_filter),
    ],
)
def test_basequery_where_filter_eq_null(unary_helper_function):
    from google.cloud.firestore_v1.types import StructuredQuery

    op_enum = StructuredQuery.UnaryFilter.Operator.IS_NULL
    unary_helper_function(None, op_enum)


def test_basequery_order_by_invalid_path():
    query = _make_base_query(mock.sentinel.parent)

    with pytest.raises(ValueError):
        query.order_by("*")


def test_basequery_order_by():
    from google.cloud.firestore_v1.base_query import BaseQuery
    from google.cloud.firestore_v1.types import StructuredQuery

    query1 = _make_base_query_all_fields(skip_fields=("orders",), all_descendants=True)

    field_path2 = "a"
    query2 = query1.order_by(field_path2)
    assert query2 is not query1
    assert isinstance(query2, BaseQuery)
    order = _make_order_pb(field_path2, StructuredQuery.Direction.ASCENDING)
    assert query2._orders == (order,)
    _compare_queries(query1, query2, "_orders")

    # Make sure it appends to the orders.
    field_path3 = "b"
    query3 = query2.order_by(field_path3, direction=BaseQuery.DESCENDING)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    order_pb3 = _make_order_pb(field_path3, StructuredQuery.Direction.DESCENDING)
    assert query3._orders == (order, order_pb3)
    _compare_queries(query2, query3, "_orders")


def test_basequery_limit():
    from google.cloud.firestore_v1.base_query import BaseQuery

    query1 = _make_base_query_all_fields(all_descendants=True)

    limit2 = 100
    query2 = query1.limit(limit2)
    assert not query2._limit_to_last
    assert query2 is not query1
    assert isinstance(query2, BaseQuery)
    assert query2._limit == limit2
    _compare_queries(query1, query2, "_limit")

    # Make sure it overrides.
    limit3 = 10
    query3 = query2.limit(limit3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._limit == limit3
    _compare_queries(query2, query3, "_limit")


def test_basequery_limit_to_last():
    from google.cloud.firestore_v1.base_query import BaseQuery

    query1 = _make_base_query_all_fields(all_descendants=True)

    limit2 = 100
    query2 = query1.limit_to_last(limit2)
    assert query2._limit_to_last
    assert query2 is not query1
    assert isinstance(query2, BaseQuery)
    assert query2._limit == limit2
    _compare_queries(query1, query2, "_limit", "_limit_to_last")

    # Make sure it overrides.
    limit3 = 10
    query3 = query2.limit(limit3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._limit == limit3
    _compare_queries(query2, query3, "_limit", "_limit_to_last")


def test_basequery__resolve_chunk_size():
    # With a global limit
    query = make_client().collection("asdf").limit(5)
    assert query._resolve_chunk_size(3, 10) == 2
    assert query._resolve_chunk_size(3, 1) == 1
    assert query._resolve_chunk_size(3, 2) == 2

    # With no limit
    query = make_client().collection("asdf")._query()
    assert query._resolve_chunk_size(3, 10) == 10
    assert query._resolve_chunk_size(3, 1) == 1
    assert query._resolve_chunk_size(3, 2) == 2


def test_basequery_offset():
    from google.cloud.firestore_v1.base_query import BaseQuery

    query1 = _make_base_query_all_fields(all_descendants=True)

    offset2 = 23
    query2 = query1.offset(offset2)
    assert query2 is not query1
    assert isinstance(query2, BaseQuery)
    assert query2._offset == offset2
    _compare_queries(query1, query2, "_offset")

    # Make sure it overrides.
    offset3 = 35
    query3 = query2.offset(offset3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._offset == offset3
    _compare_queries(query2, query3, "_offset")


def test_basequery__cursor_helper_w_dict():
    values = {"a": 7, "b": "foo"}
    query1 = _make_base_query(mock.sentinel.parent)
    query1._all_descendants = True
    query2 = query1._cursor_helper(values, True, True)

    assert query2._parent is mock.sentinel.parent
    assert query2._projection is None
    assert query2._field_filters == ()
    assert query2._orders == query1._orders
    assert query2._limit is None
    assert query2._offset is None
    assert query2._end_at is None
    assert query2._all_descendants

    cursor, before = query2._start_at

    assert cursor == values
    assert before


def test_basequery__cursor_helper_w_tuple():
    values = (7, "foo")
    query1 = _make_base_query(mock.sentinel.parent)
    query2 = query1._cursor_helper(values, False, True)

    assert query2._parent is mock.sentinel.parent
    assert query2._projection is None
    assert query2._field_filters == ()
    assert query2._orders == query1._orders
    assert query2._limit is None
    assert query2._offset is None
    assert query2._end_at is None

    cursor, before = query2._start_at

    assert cursor == list(values)
    assert not before


def test_basequery__cursor_helper_w_list():
    values = [7, "foo"]
    query1 = _make_base_query(mock.sentinel.parent)
    query2 = query1._cursor_helper(values, True, False)

    assert query2._parent is mock.sentinel.parent
    assert query2._projection is None
    assert query2._field_filters == ()
    assert query2._orders == query1._orders
    assert query2._limit is None
    assert query2._offset is None
    assert query2._start_at is None

    cursor, before = query2._end_at

    assert cursor == values
    assert cursor == values
    assert before


def test_basequery__cursor_helper_w_snapshot_wrong_collection():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("there", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query = _make_base_query(collection)

    with pytest.raises(ValueError):
        query._cursor_helper(snapshot, False, False)


def test_basequery__cursor_helper_w_snapshot_other_collection_all_descendants():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("there", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query1 = _make_base_query(collection, all_descendants=True)

    query2 = query1._cursor_helper(snapshot, False, False)

    assert query2._parent is collection
    assert query2._projection is None
    assert query2._field_filters == ()
    assert query2._orders == ()
    assert query2._limit is None
    assert query2._offset is None
    assert query2._start_at is None

    cursor, before = query2._end_at

    assert cursor is snapshot
    assert not before


def test_basequery__cursor_helper_w_snapshot():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("here", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query1 = _make_base_query(collection)

    query2 = query1._cursor_helper(snapshot, False, False)

    assert query2._parent is collection
    assert query2._projection is None
    assert query2._field_filters == ()
    assert query2._orders == ()
    assert query2._limit is None
    assert query2._offset is None
    assert query2._start_at is None

    cursor, before = query2._end_at

    assert cursor is snapshot
    assert not before


def test_basequery_start_at():
    from google.cloud.firestore_v1.base_query import BaseQuery

    collection = _make_collection("here")
    query1 = _make_base_query_all_fields(
        parent=collection, skip_fields=("orders",), all_descendants=True
    )
    query2 = query1.order_by("hi")

    document_fields3 = {"hi": "mom"}
    query3 = query2.start_at(document_fields3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._start_at == (document_fields3, True)
    _compare_queries(query2, query3, "_start_at")

    # Make sure it overrides.
    query4 = query3.order_by("bye")
    values5 = {"hi": "zap", "bye": 88}
    docref = _make_docref("here", "doc_id")
    document_fields5 = _make_snapshot(docref, values5)
    query5 = query4.start_at(document_fields5)
    assert query5 is not query4
    assert isinstance(query5, BaseQuery)
    assert query5._start_at == (document_fields5, True)
    _compare_queries(query4, query5, "_start_at")


def test_basequery_start_after():
    from google.cloud.firestore_v1.base_query import BaseQuery

    collection = _make_collection("here")
    query1 = _make_base_query_all_fields(parent=collection, skip_fields=("orders",))
    query2 = query1.order_by("down")

    document_fields3 = {"down": 99.75}
    query3 = query2.start_after(document_fields3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._start_at == (document_fields3, False)
    _compare_queries(query2, query3, "_start_at")

    # Make sure it overrides.
    query4 = query3.order_by("out")
    values5 = {"down": 100.25, "out": b"\x00\x01"}
    docref = _make_docref("here", "doc_id")
    document_fields5 = _make_snapshot(docref, values5)
    query5 = query4.start_after(document_fields5)
    assert query5 is not query4
    assert isinstance(query5, BaseQuery)
    assert query5._start_at == (document_fields5, False)
    _compare_queries(query4, query5, "_start_at")


def test_basequery_end_before():
    from google.cloud.firestore_v1.base_query import BaseQuery

    collection = _make_collection("here")
    query1 = _make_base_query_all_fields(parent=collection, skip_fields=("orders",))
    query2 = query1.order_by("down")

    document_fields3 = {"down": 99.75}
    query3 = query2.end_before(document_fields3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._end_at == (document_fields3, True)
    _compare_queries(query2, query3, "_end_at")

    # Make sure it overrides.
    query4 = query3.order_by("out")
    values5 = {"down": 100.25, "out": b"\x00\x01"}
    docref = _make_docref("here", "doc_id")
    document_fields5 = _make_snapshot(docref, values5)
    query5 = query4.end_before(document_fields5)
    assert query5 is not query4
    assert isinstance(query5, BaseQuery)
    assert query5._end_at == (document_fields5, True)
    _compare_queries(query4, query5, "_end_at")
    _compare_queries(query4, query5, "_end_at")


def test_basequery_end_at():
    from google.cloud.firestore_v1.base_query import BaseQuery

    collection = _make_collection("here")
    query1 = _make_base_query_all_fields(parent=collection, skip_fields=("orders",))
    query2 = query1.order_by("hi")

    document_fields3 = {"hi": "mom"}
    query3 = query2.end_at(document_fields3)
    assert query3 is not query2
    assert isinstance(query3, BaseQuery)
    assert query3._end_at == (document_fields3, False)
    _compare_queries(query2, query3, "_end_at")

    # Make sure it overrides.
    query4 = query3.order_by("bye")
    values5 = {"hi": "zap", "bye": 88}
    docref = _make_docref("here", "doc_id")
    document_fields5 = _make_snapshot(docref, values5)
    query5 = query4.end_at(document_fields5)
    assert query5 is not query4
    assert isinstance(query5, BaseQuery)
    assert query5._end_at == (document_fields5, False)
    _compare_queries(query4, query5, "_end_at")


def test_basequery_where_filter_keyword_arg():
    from google.cloud.firestore_v1.base_query import And, FieldFilter, Or
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    op_class = StructuredQuery.FieldFilter.Operator

    field_path_1 = "x.y"
    op_str_1 = ">"
    value_1 = 50.5

    field_path_2 = "population"
    op_str_2 = "=="
    value_2 = 60000

    field_filter_1 = FieldFilter(field_path_1, op_str_1, value_1)
    field_filter_2 = FieldFilter(field_path_2, op_str_2, value_2)

    q = _make_base_query(mock.sentinel.parent)
    q = q.where(filter=field_filter_1)

    filter_pb = q._filters_pb()
    expected_pb = query.StructuredQuery.Filter(
        field_filter=query.StructuredQuery.FieldFilter(
            field=query.StructuredQuery.FieldReference(field_path=field_path_1),
            op=StructuredQuery.FieldFilter.Operator.GREATER_THAN,
            value=document.Value(double_value=value_1),
        )
    )
    assert filter_pb == expected_pb

    or_filter = Or(filters=[field_filter_1, field_filter_2])
    q = _make_base_query(mock.sentinel.parent)
    q = q.where(filter=or_filter)

    filter_pb = q._filters_pb()
    expected_pb = query.StructuredQuery.Filter(
        query.StructuredQuery.Filter(
            composite_filter=query.StructuredQuery.CompositeFilter(
                op=StructuredQuery.CompositeFilter.Operator.OR,
                filters=[
                    query.StructuredQuery.Filter(
                        field_filter=query.StructuredQuery.FieldFilter(
                            field=query.StructuredQuery.FieldReference(
                                field_path=field_path_1
                            ),
                            op=op_class.GREATER_THAN,
                            value=document.Value(double_value=value_1),
                        )
                    ),
                    query.StructuredQuery.Filter(
                        field_filter=query.StructuredQuery.FieldFilter(
                            field=query.StructuredQuery.FieldReference(
                                field_path=field_path_2
                            ),
                            op=op_class.EQUAL,
                            value=document.Value(integer_value=value_2),
                        )
                    ),
                ],
            )
        )
    )
    assert filter_pb == expected_pb

    and_filter = And(filters=[field_filter_1, field_filter_2])
    q = _make_base_query(mock.sentinel.parent)
    q = q.where(filter=and_filter)

    filter_pb = q._filters_pb()
    expected_pb = query.StructuredQuery.Filter(
        query.StructuredQuery.Filter(
            composite_filter=query.StructuredQuery.CompositeFilter(
                op=StructuredQuery.CompositeFilter.Operator.AND,
                filters=[
                    query.StructuredQuery.Filter(
                        field_filter=query.StructuredQuery.FieldFilter(
                            field=query.StructuredQuery.FieldReference(
                                field_path=field_path_1
                            ),
                            op=op_class.GREATER_THAN,
                            value=document.Value(double_value=value_1),
                        )
                    ),
                    query.StructuredQuery.Filter(
                        field_filter=query.StructuredQuery.FieldFilter(
                            field=query.StructuredQuery.FieldReference(
                                field_path=field_path_2
                            ),
                            op=op_class.EQUAL,
                            value=document.Value(integer_value=value_2),
                        )
                    ),
                ],
            )
        )
    )
    assert filter_pb == expected_pb


def test_basequery_where_cannot_pass_both_positional_and_keyword_filter_arg():
    from google.cloud.firestore_v1.base_query import FieldFilter

    field_path_1 = "x.y"
    op_str_1 = ">"
    value_1 = 50.5
    filter = FieldFilter(field_path_1, op_str_1, value_1)
    q = _make_base_query(mock.sentinel.parent)

    with pytest.raises(
        ValueError,
        match="Can't pass in both the positional arguments and 'filter' at the same time",
    ):
        q.where(field_path_1, op_str_1, value_1, filter=filter)


def test_basequery_where_cannot_pass_filter_without_keyword_arg():
    from google.cloud.firestore_v1.base_query import And, FieldFilter

    field_path_1 = "x.y"
    op_str_1 = ">"
    value_1 = 50.5
    filter = FieldFilter(field_path_1, op_str_1, value_1)
    q = _make_base_query(mock.sentinel.parent)

    with pytest.raises(
        ValueError,
        match="FieldFilter object must be passed using keyword argument 'filter'",
    ):
        q.where(filter)

    and_filter = And(filters=[filter])
    with pytest.raises(
        ValueError,
        match="'Or' and 'And' objects must be passed using keyword argument 'filter'",
    ):
        q.where(and_filter)


def test_basequery_where_mix_of_field_and_composite():
    from google.cloud.firestore_v1.base_query import And, FieldFilter, Or
    from google.cloud.firestore_v1.types import document, query
    from google.cloud.firestore_v1.types.query import StructuredQuery

    op_class = StructuredQuery.FieldFilter.Operator

    field_path_1 = "x.y"
    op_str_1 = ">"
    value_1 = 50.5
    filter_1 = FieldFilter(field_path_1, op_str_1, value_1)

    field_path_2 = "population"
    op_str_2 = "=="
    value_2 = 60000
    filter_2 = FieldFilter(field_path_2, op_str_2, value_2)

    field_path_3 = "country"
    op_str_3 = "=="
    value_3 = "USA"
    filter_3 = FieldFilter(field_path_3, op_str_3, value_3)

    or_filter = Or(filters=[filter_2, filter_3])
    combined_filter = And(filters=[filter_1, or_filter])
    q = _make_base_query(mock.sentinel.parent)
    q = q.where(filter=filter_1).where(filter=combined_filter)

    filter_pb = q._filters_pb()

    expected_pb = query.StructuredQuery.Filter(
        composite_filter=query.StructuredQuery.CompositeFilter(
            op=StructuredQuery.CompositeFilter.Operator.AND,
            filters=[
                query.StructuredQuery.Filter(
                    field_filter=query.StructuredQuery.FieldFilter(
                        field=query.StructuredQuery.FieldReference(
                            field_path=field_path_1
                        ),
                        op=op_class.GREATER_THAN,
                        value=document.Value(double_value=value_1),
                    )
                ),
                query.StructuredQuery.Filter(
                    composite_filter=query.StructuredQuery.CompositeFilter(
                        op=StructuredQuery.CompositeFilter.Operator.AND,
                        filters=[
                            query.StructuredQuery.Filter(
                                field_filter=query.StructuredQuery.FieldFilter(
                                    field=query.StructuredQuery.FieldReference(
                                        field_path=field_path_1
                                    ),
                                    op=op_class.GREATER_THAN,
                                    value=document.Value(double_value=value_1),
                                )
                            ),
                            query.StructuredQuery.Filter(
                                composite_filter=query.StructuredQuery.CompositeFilter(
                                    op=StructuredQuery.CompositeFilter.Operator.OR,
                                    filters=[
                                        query.StructuredQuery.Filter(
                                            field_filter=query.StructuredQuery.FieldFilter(
                                                field=query.StructuredQuery.FieldReference(
                                                    field_path=field_path_2
                                                ),
                                                op=op_class.EQUAL,
                                                value=document.Value(
                                                    integer_value=value_2
                                                ),
                                            )
                                        ),
                                        query.StructuredQuery.Filter(
                                            field_filter=query.StructuredQuery.FieldFilter(
                                                field=query.StructuredQuery.FieldReference(
                                                    field_path=field_path_3
                                                ),
                                                op=op_class.EQUAL,
                                                value=document.Value(
                                                    string_value=value_3
                                                ),
                                            )
                                        ),
                                    ],
                                )
                            ),
                        ],
                    )
                ),
            ],
        )
    )

    assert filter_pb == expected_pb


def test_basequery_where_filter_as_positional_arg():
    from google.cloud.firestore_v1.base_query import FieldFilter, Or

    field_path_1 = "x.y"
    op_str_1 = ">"
    value_1 = 50.5
    filter_1 = FieldFilter(field_path_1, op_str_1, value_1)

    q = _make_base_query(mock.sentinel.parent)
    with pytest.raises(ValueError) as exc:
        q.where(filter_1)
    assert (
        str(exc.value)
        == "FieldFilter object must be passed using keyword argument 'filter'"
    )

    or_filter = Or(filters=[filter_1])
    with pytest.raises(ValueError) as exc:
        q.where(or_filter)
    assert (
        str(exc.value)
        == "'Or' and 'And' objects must be passed using keyword argument 'filter'"
    )


def test_basequery_where_requires_a_filter():
    q = _make_base_query(mock.sentinel.parent)

    with pytest.raises(
        ValueError,
        match="Filter must be provided through positional arguments or the 'filter' keyword argument.",
    ):
        q.where()


def test_query_add_filter_with_positional_args_raises_user_warning():
    q = _make_base_query(mock.sentinel.parent)

    with pytest.warns(
        UserWarning,
        match="Detected filter using positional arguments",
    ):
        q.where("x.y", "==", 50)


def test_basequery__filters_pb_empty():
    query = _make_base_query(mock.sentinel.parent)
    assert len(query._field_filters) == 0
    assert query._filters_pb() is None


def test_basequery__filters_pb_single():
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    query1 = _make_base_query(mock.sentinel.parent)
    query2 = query1.where("x.y", ">", 50.5)
    filter_pb = query2._filters_pb()
    expected_pb = query.StructuredQuery.Filter(
        field_filter=query.StructuredQuery.FieldFilter(
            field=query.StructuredQuery.FieldReference(field_path="x.y"),
            op=StructuredQuery.FieldFilter.Operator.GREATER_THAN,
            value=document.Value(double_value=50.5),
        )
    )
    assert filter_pb == expected_pb


def test_basequery__filters_pb_multi():
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    query1 = _make_base_query(mock.sentinel.parent)
    query2 = query1.where("x.y", ">", 50.5)
    query3 = query2.where("ABC", "==", 123)

    filter_pb = query3._filters_pb()
    op_class = StructuredQuery.FieldFilter.Operator
    expected_pb = query.StructuredQuery.Filter(
        composite_filter=query.StructuredQuery.CompositeFilter(
            op=StructuredQuery.CompositeFilter.Operator.AND,
            filters=[
                query.StructuredQuery.Filter(
                    field_filter=query.StructuredQuery.FieldFilter(
                        field=query.StructuredQuery.FieldReference(field_path="x.y"),
                        op=op_class.GREATER_THAN,
                        value=document.Value(double_value=50.5),
                    )
                ),
                query.StructuredQuery.Filter(
                    field_filter=query.StructuredQuery.FieldFilter(
                        field=query.StructuredQuery.FieldReference(field_path="ABC"),
                        op=op_class.EQUAL,
                        value=document.Value(integer_value=123),
                    )
                ),
            ],
        )
    )
    assert filter_pb == expected_pb


def test_basequery__normalize_projection_none():
    query = _make_base_query(mock.sentinel.parent)
    assert query._normalize_projection(None) is None


def test_basequery__normalize_projection_empty():
    projection = _make_projection_for_select([])
    query = _make_base_query(mock.sentinel.parent)
    normalized = query._normalize_projection(projection)
    field_paths = [field_ref.field_path for field_ref in normalized.fields]
    assert field_paths == ["__name__"]


def test_basequery__normalize_projection_non_empty():
    projection = _make_projection_for_select(["a", "b"])
    query = _make_base_query(mock.sentinel.parent)
    assert query._normalize_projection(projection) is projection


def test_basequery__normalize_orders_wo_orders_wo_cursors():
    query = _make_base_query(mock.sentinel.parent)
    expected = []
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_w_orders_wo_cursors():
    query = _make_base_query(mock.sentinel.parent).order_by("a")
    expected = [query._make_order("a", "ASCENDING")]
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_wo_orders_w_snapshot_cursor():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("here", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query = _make_base_query(collection).start_at(snapshot)
    expected = [query._make_order("__name__", "ASCENDING")]
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_w_name_orders_w_snapshot_cursor():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("here", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query = (
        _make_base_query(collection)
        .order_by("__name__", "DESCENDING")
        .start_at(snapshot)
    )
    expected = [query._make_order("__name__", "DESCENDING")]
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_wo_orders_w_snapshot_cursor_w_neq_exists():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("here", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query = (
        _make_base_query(collection)
        .where("c", "<=", 20)
        .order_by("c", "DESCENDING")
        .start_at(snapshot)
    )
    expected = [
        query._make_order("c", "DESCENDING"),
        query._make_order("__name__", "DESCENDING"),
    ]
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_wo_orders_w_snapshot_cursor_w_neq_where():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("here", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query = _make_base_query(collection).where("c", "<=", 20).end_at(snapshot)
    expected = [
        query._make_order("c", "ASCENDING"),
        query._make_order("__name__", "ASCENDING"),
    ]
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_wo_orders_w_snapshot_cursor_w_isnull_where():
    values = {"a": 7, "b": "foo"}
    docref = _make_docref("here", "doc_id")
    snapshot = _make_snapshot(docref, values)
    collection = _make_collection("here")
    query = _make_base_query(collection).where("c", "==", None).end_at(snapshot)
    expected = [
        query._make_order("__name__", "ASCENDING"),
    ]
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_w_name_orders_w_none_cursor():
    collection = _make_collection("here")
    query = (
        _make_base_query(collection).order_by("__name__", "DESCENDING").start_at(None)
    )
    expected = [query._make_order("__name__", "DESCENDING")]
    assert query._normalize_orders() == expected


def test_basequery__normalize_orders_w_cursor_descending():
    """
    Test case for b/306472103
    """
    from google.cloud.firestore_v1.base_query import FieldFilter

    collection = _make_collection("here")
    snapshot = _make_snapshot(_make_docref("here", "doc_id"), {"a": 1, "b": 2})
    query = (
        _make_base_query(collection)
        .where(filter=FieldFilter("a", "==", 1))
        .where(filter=FieldFilter("b", "in", [1, 2, 3]))
        .order_by("c", "DESCENDING")
    )
    query_w_snapshot = query.start_after(snapshot)

    normalized = query._normalize_orders()
    expected = [query._make_order("c", "DESCENDING")]
    assert normalized == expected

    normalized_w_snapshot = query_w_snapshot._normalize_orders()
    expected_w_snapshot = expected + [query._make_order("__name__", "DESCENDING")]
    assert normalized_w_snapshot == expected_w_snapshot


def test_basequery__normalize_orders_w_cursor_descending_w_inequality():
    """
    Test case for b/306472103, with extra ineuality filter in "where" clause
    """
    from google.cloud.firestore_v1.base_query import FieldFilter

    collection = _make_collection("here")
    snapshot = _make_snapshot(_make_docref("here", "doc_id"), {"a": 1, "b": 2})
    query = (
        _make_base_query(collection)
        .where(filter=FieldFilter("a", "==", 1))
        .where(filter=FieldFilter("b", "in", [1, 2, 3]))
        .where(filter=FieldFilter("c", "not-in", [4, 5, 6]))
        .order_by("d", "DESCENDING")
    )
    query_w_snapshot = query.start_after(snapshot)

    normalized = query._normalize_orders()
    expected = [query._make_order("d", "DESCENDING")]
    assert normalized == expected

    normalized_w_snapshot = query_w_snapshot._normalize_orders()
    expected_w_snapshot = [
        query._make_order("d", "DESCENDING"),
        query._make_order("c", "DESCENDING"),
        query._make_order("__name__", "DESCENDING"),
    ]
    assert normalized_w_snapshot == expected_w_snapshot


def test_basequery__normalize_cursor_none():
    query = _make_base_query(mock.sentinel.parent)
    assert query._normalize_cursor(None, query._orders) is None


def test_basequery__normalize_cursor_no_order():
    cursor = ([1], True)
    query = _make_base_query(mock.sentinel.parent)

    with pytest.raises(ValueError):
        query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_as_list_mismatched_order():
    cursor = ([1, 2], True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    with pytest.raises(ValueError):
        query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_as_dict_mismatched_order():
    cursor = ({"a": 1}, True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    with pytest.raises(ValueError):
        query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_as_dict_extra_orders_ok():
    cursor = ({"name": "Springfield"}, True)
    query = _make_base_query(mock.sentinel.parent).order_by("name").order_by("state")

    normalized = query._normalize_cursor(cursor, query._orders)
    assert normalized == (["Springfield"], True)


def test_basequery__normalize_cursor_extra_orders_ok():
    cursor = (["Springfield"], True)
    query = _make_base_query(mock.sentinel.parent).order_by("name").order_by("state")

    query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_w_delete():
    from google.cloud.firestore_v1 import DELETE_FIELD

    cursor = ([DELETE_FIELD], True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    with pytest.raises(ValueError):
        query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_w_server_timestamp():
    from google.cloud.firestore_v1 import SERVER_TIMESTAMP

    cursor = ([SERVER_TIMESTAMP], True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    with pytest.raises(ValueError):
        query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_w_array_remove():
    from google.cloud.firestore_v1 import ArrayRemove

    cursor = ([ArrayRemove([1, 3, 5])], True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    with pytest.raises(ValueError):
        query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_w_array_union():
    from google.cloud.firestore_v1 import ArrayUnion

    cursor = ([ArrayUnion([2, 4, 8])], True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    with pytest.raises(ValueError):
        query._normalize_cursor(cursor, query._orders)


def test_basequery__normalize_cursor_as_list_hit():
    cursor = ([1], True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    assert query._normalize_cursor(cursor, query._orders) == ([1], True)


def test_basequery__normalize_cursor_as_dict_hit():
    cursor = ({"b": 1}, True)
    query = _make_base_query(mock.sentinel.parent).order_by("b", "ASCENDING")

    assert query._normalize_cursor(cursor, query._orders) == ([1], True)


def test_basequery__normalize_cursor_as_dict_with_dot_key_hit():
    cursor = ({"b.a": 1}, True)
    query = _make_base_query(mock.sentinel.parent).order_by("b.a", "ASCENDING")
    assert query._normalize_cursor(cursor, query._orders) == ([1], True)


def test_basequery__normalize_cursor_as_dict_with_inner_data_hit():
    cursor = ({"b": {"a": 1}}, True)
    query = _make_base_query(mock.sentinel.parent).order_by("b.a", "ASCENDING")
    assert query._normalize_cursor(cursor, query._orders) == ([1], True)


def test_basequery__normalize_cursor_as_snapshot_hit():
    values = {"b": 1}
    docref = _make_docref("here", "doc_id")
    snapshot = _make_snapshot(docref, values)
    cursor = (snapshot, True)
    collection = _make_collection("here")
    query = _make_base_query(collection).order_by("b", "ASCENDING")

    assert query._normalize_cursor(cursor, query._orders) == ([1], True)


def test_basequery__normalize_cursor_non_existant_snapshot():
    from google.cloud.firestore_v1 import document

    values = {"b": 1}
    docref = _make_docref("here", "doc_id")
    snapshot = document.DocumentSnapshot(docref, values, False, None, None, None)
    cursor = (snapshot, True)
    collection = _make_collection("here")
    query = _make_base_query(collection).order_by("b", "ASCENDING")

    assert query._normalize_cursor(cursor, query._orders) == ([1], True)


def test_basequery__normalize_cursor_w___name___w_reference():
    db_string = "projects/my-project/database/(default)"
    client = mock.Mock(spec=["_database_string"])
    client._database_string = db_string
    parent = mock.Mock(spec=["_path", "_client"])
    parent._client = client
    parent._path = ["C"]
    query = _make_base_query(parent).order_by("__name__", "ASCENDING")
    docref = _make_docref("here", "doc_id")
    values = {"a": 7}
    snapshot = _make_snapshot(docref, values)
    expected = docref
    cursor = (snapshot, True)

    assert query._normalize_cursor(cursor, query._orders) == ([expected], True)


def test_basequery__normalize_cursor_w___name___wo_slash():
    db_string = "projects/my-project/database/(default)"
    client = mock.Mock(spec=["_database_string"])
    client._database_string = db_string
    parent = mock.Mock(spec=["_path", "_client", "document"])
    parent._client = client
    parent._path = ["C"]
    document = parent.document.return_value = mock.Mock(spec=[])
    query = _make_base_query(parent).order_by("__name__", "ASCENDING")
    cursor = (["b"], True)
    expected = document

    assert query._normalize_cursor(cursor, query._orders) == ([expected], True)
    parent.document.assert_called_once_with("b")


def test_basequery__to_protobuf_all_fields():
    from google.protobuf import wrappers_pb2

    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    parent = mock.Mock(id="cat", spec=["id"])
    query1 = _make_base_query(parent)
    query2 = query1.select(["X", "Y", "Z"])
    query3 = query2.where("Y", ">", 2.5)
    query4 = query3.order_by("X")
    query5 = query4.limit(17)
    query6 = query5.offset(3)
    query7 = query6.start_at({"X": 10})
    query8 = query7.end_at({"X": 25})

    structured_query_pb = query8._to_protobuf()
    query_kwargs = {
        "from_": [query.StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "select": query.StructuredQuery.Projection(
            fields=[
                query.StructuredQuery.FieldReference(field_path=field_path)
                for field_path in ["X", "Y", "Z"]
            ]
        ),
        "where": query.StructuredQuery.Filter(
            field_filter=query.StructuredQuery.FieldFilter(
                field=query.StructuredQuery.FieldReference(field_path="Y"),
                op=StructuredQuery.FieldFilter.Operator.GREATER_THAN,
                value=document.Value(double_value=2.5),
            )
        ),
        "order_by": [_make_order_pb("X", StructuredQuery.Direction.ASCENDING)],
        "start_at": query.Cursor(
            values=[document.Value(integer_value=10)], before=True
        ),
        "end_at": query.Cursor(values=[document.Value(integer_value=25)]),
        "offset": 3,
        "limit": wrappers_pb2.Int32Value(value=17),
    }
    expected_pb = query.StructuredQuery(**query_kwargs)
    assert structured_query_pb == expected_pb


def test_basequery__to_protobuf_select_only():
    from google.cloud.firestore_v1.types import query

    parent = mock.Mock(id="cat", spec=["id"])
    query1 = _make_base_query(parent)
    field_paths = ["a.b", "a.c", "d"]
    query2 = query1.select(field_paths)

    structured_query_pb = query2._to_protobuf()
    query_kwargs = {
        "from_": [query.StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "select": query.StructuredQuery.Projection(
            fields=[
                query.StructuredQuery.FieldReference(field_path=field_path)
                for field_path in field_paths
            ]
        ),
    }
    expected_pb = query.StructuredQuery(**query_kwargs)
    assert structured_query_pb == expected_pb


def test_basequery__to_protobuf_where_only():
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    parent = mock.Mock(id="dog", spec=["id"])
    query1 = _make_base_query(parent)
    query2 = query1.where("a", "==", "b")

    structured_query_pb = query2._to_protobuf()
    query_kwargs = {
        "from_": [query.StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "where": query.StructuredQuery.Filter(
            field_filter=query.StructuredQuery.FieldFilter(
                field=query.StructuredQuery.FieldReference(field_path="a"),
                op=StructuredQuery.FieldFilter.Operator.EQUAL,
                value=document.Value(string_value="b"),
            )
        ),
    }
    expected_pb = query.StructuredQuery(**query_kwargs)
    assert structured_query_pb == expected_pb


def test_basequery__to_protobuf_order_by_only():
    from google.cloud.firestore_v1.types import StructuredQuery, query

    parent = mock.Mock(id="fish", spec=["id"])
    query1 = _make_base_query(parent)
    query2 = query1.order_by("abc")

    structured_query_pb = query2._to_protobuf()
    query_kwargs = {
        "from_": [query.StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "order_by": [_make_order_pb("abc", StructuredQuery.Direction.ASCENDING)],
    }
    expected_pb = query.StructuredQuery(**query_kwargs)
    assert structured_query_pb == expected_pb


def test_basequery__to_protobuf_start_at_only():
    # NOTE: "only" is wrong since we must have ``order_by`` as well.
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    parent = mock.Mock(id="phish", spec=["id"])
    query_inst = _make_base_query(parent).order_by("X.Y").start_after({"X": {"Y": "Z"}})

    structured_query_pb = query_inst._to_protobuf()
    query_kwargs = {
        "from_": [StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "order_by": [_make_order_pb("X.Y", StructuredQuery.Direction.ASCENDING)],
        "start_at": query.Cursor(values=[document.Value(string_value="Z")]),
    }
    expected_pb = StructuredQuery(**query_kwargs)
    assert structured_query_pb == expected_pb


def test_basequery__to_protobuf_end_at_only():
    # NOTE: "only" is wrong since we must have ``order_by`` as well.
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    parent = mock.Mock(id="ghoti", spec=["id"])
    query_inst = _make_base_query(parent).order_by("a").end_at({"a": 88})

    structured_query_pb = query_inst._to_protobuf()
    query_kwargs = {
        "from_": [query.StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "order_by": [_make_order_pb("a", StructuredQuery.Direction.ASCENDING)],
        "end_at": query.Cursor(values=[document.Value(integer_value=88)]),
    }
    expected_pb = query.StructuredQuery(**query_kwargs)
    assert structured_query_pb == expected_pb


def test_basequery__to_protobuf_offset_only():
    from google.cloud.firestore_v1.types import query

    parent = mock.Mock(id="cartt", spec=["id"])
    query1 = _make_base_query(parent)
    offset = 14
    query2 = query1.offset(offset)

    structured_query_pb = query2._to_protobuf()
    query_kwargs = {
        "from_": [query.StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "offset": offset,
    }
    expected_pb = query.StructuredQuery(**query_kwargs)
    assert structured_query_pb == expected_pb


def test_basequery__to_protobuf_limit_only():
    from google.protobuf import wrappers_pb2

    from google.cloud.firestore_v1.types import query

    parent = mock.Mock(id="donut", spec=["id"])
    query1 = _make_base_query(parent)
    limit = 31
    query2 = query1.limit(limit)

    structured_query_pb = query2._to_protobuf()
    query_kwargs = {
        "from_": [query.StructuredQuery.CollectionSelector(collection_id=parent.id)],
        "limit": wrappers_pb2.Int32Value(value=limit),
    }
    expected_pb = query.StructuredQuery(**query_kwargs)

    assert structured_query_pb == expected_pb


def test_basequery_comparator_no_ordering():
    query = _make_base_query(mock.sentinel.parent)
    query._orders = []
    doc1 = mock.Mock()
    doc1.reference._path = ("col", "adocument1")

    doc2 = mock.Mock()
    doc2.reference._path = ("col", "adocument2")

    sort = query._comparator(doc1, doc2)
    assert sort == -1


def test_basequery_comparator_no_ordering_same_id():
    query = _make_base_query(mock.sentinel.parent)
    query._orders = []
    doc1 = mock.Mock()
    doc1.reference._path = ("col", "adocument1")

    doc2 = mock.Mock()
    doc2.reference._path = ("col", "adocument1")

    sort = query._comparator(doc1, doc2)
    assert sort == 0


def test_basequery_comparator_ordering():
    query = _make_base_query(mock.sentinel.parent)
    orderByMock = mock.Mock()
    orderByMock.field.field_path = "last"
    orderByMock.direction = 1  # ascending
    query._orders = [orderByMock]

    doc1 = mock.Mock()
    doc1.reference._path = ("col", "adocument1")
    doc1._data = {
        "first": {"stringValue": "Ada"},
        "last": {"stringValue": "secondlovelace"},
    }
    doc2 = mock.Mock()
    doc2.reference._path = ("col", "adocument2")
    doc2._data = {
        "first": {"stringValue": "Ada"},
        "last": {"stringValue": "lovelace"},
    }

    sort = query._comparator(doc1, doc2)
    assert sort == 1


def test_basequery_comparator_ordering_descending():
    query = _make_base_query(mock.sentinel.parent)
    orderByMock = mock.Mock()
    orderByMock.field.field_path = "last"
    orderByMock.direction = -1  # descending
    query._orders = [orderByMock]

    doc1 = mock.Mock()
    doc1.reference._path = ("col", "adocument1")
    doc1._data = {
        "first": {"stringValue": "Ada"},
        "last": {"stringValue": "secondlovelace"},
    }
    doc2 = mock.Mock()
    doc2.reference._path = ("col", "adocument2")
    doc2._data = {
        "first": {"stringValue": "Ada"},
        "last": {"stringValue": "lovelace"},
    }

    sort = query._comparator(doc1, doc2)
    assert sort == -1


def test_basequery_comparator_missing_order_by_field_in_data_raises():
    query = _make_base_query(mock.sentinel.parent)
    orderByMock = mock.Mock()
    orderByMock.field.field_path = "last"
    orderByMock.direction = 1  # ascending
    query._orders = [orderByMock]

    doc1 = mock.Mock()
    doc1.reference._path = ("col", "adocument1")
    doc1._data = {}
    doc2 = mock.Mock()
    doc2.reference._path = ("col", "adocument2")
    doc2._data = {
        "first": {"stringValue": "Ada"},
        "last": {"stringValue": "lovelace"},
    }

    with pytest.raises(ValueError) as exc_info:
        query._comparator(doc1, doc2)

    (message,) = exc_info.value.args
    assert message.startswith("Can only compare fields ")


def test_basequery_recursive_multiple():
    from google.cloud.firestore_v1.base_query import BaseQuery
    from google.cloud.firestore_v1.collection import CollectionReference

    class DerivedQuery(BaseQuery):
        @staticmethod
        def _get_collection_reference_class():
            return CollectionReference

    query = DerivedQuery(make_client().collection("asdf"))
    assert isinstance(query.recursive().recursive(), DerivedQuery)


def _get_op_class():
    from google.cloud.firestore_v1.types import StructuredQuery

    return StructuredQuery.FieldFilter.Operator


def test__enum_from_op_string_lt():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("<") == op_class.LESS_THAN


def test__enum_from_op_string_le():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("<=") == op_class.LESS_THAN_OR_EQUAL


def test__enum_from_op_string_eq():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("==") == op_class.EQUAL


def test__enum_from_op_string_ge():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string(">=") == op_class.GREATER_THAN_OR_EQUAL


def test__enum_from_op_string_gt():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string(">") == op_class.GREATER_THAN


def test__enum_from_op_string_array_contains():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("array_contains") == op_class.ARRAY_CONTAINS


def test__enum_from_op_string_in():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("in") == op_class.IN


def test__enum_from_op_string_array_contains_any():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("array_contains_any") == op_class.ARRAY_CONTAINS_ANY


def test__enum_from_op_string_not_in():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("not-in") == op_class.NOT_IN


def test__enum_from_op_string_not_eq():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    op_class = _get_op_class()
    assert _enum_from_op_string("!=") == op_class.NOT_EQUAL


def test__enum_from_op_string_invalid():
    from google.cloud.firestore_v1.base_query import _enum_from_op_string

    with pytest.raises(ValueError):
        _enum_from_op_string("?")


def test__isnan_valid():
    from google.cloud.firestore_v1.base_query import _isnan

    assert _isnan(float("nan"))


def test__isnan_invalid():
    from google.cloud.firestore_v1.base_query import _isnan

    assert not _isnan(51.5)
    assert not _isnan(None)
    assert not _isnan("str")
    assert not _isnan(int)
    assert not _isnan(1.0 + 1.0j)


def test__enum_from_direction_success():
    from google.cloud.firestore_v1.base_query import _enum_from_direction
    from google.cloud.firestore_v1.query import Query
    from google.cloud.firestore_v1.types import StructuredQuery

    dir_class = StructuredQuery.Direction
    assert _enum_from_direction(Query.ASCENDING) == dir_class.ASCENDING
    assert _enum_from_direction(Query.DESCENDING) == dir_class.DESCENDING

    # Ints pass through
    assert _enum_from_direction(dir_class.ASCENDING) == dir_class.ASCENDING
    assert _enum_from_direction(dir_class.DESCENDING) == dir_class.DESCENDING


def test__enum_from_direction_failure():
    from google.cloud.firestore_v1.base_query import _enum_from_direction

    with pytest.raises(ValueError):
        _enum_from_direction("neither-ASCENDING-nor-DESCENDING")


def test__filter_pb_unary():
    from google.cloud.firestore_v1.base_query import _filter_pb
    from google.cloud.firestore_v1.types import StructuredQuery, query

    unary_pb = query.StructuredQuery.UnaryFilter(
        field=query.StructuredQuery.FieldReference(field_path="a.b.c"),
        op=StructuredQuery.UnaryFilter.Operator.IS_NULL,
    )
    filter_pb = _filter_pb(unary_pb)
    expected_pb = query.StructuredQuery.Filter(unary_filter=unary_pb)
    assert filter_pb == expected_pb


def test__filter_pb_field():
    from google.cloud.firestore_v1.base_query import _filter_pb
    from google.cloud.firestore_v1.types import StructuredQuery, document, query

    field_filter_pb = query.StructuredQuery.FieldFilter(
        field=query.StructuredQuery.FieldReference(field_path="XYZ"),
        op=StructuredQuery.FieldFilter.Operator.GREATER_THAN,
        value=document.Value(double_value=90.75),
    )
    filter_pb = _filter_pb(field_filter_pb)
    expected_pb = query.StructuredQuery.Filter(field_filter=field_filter_pb)
    assert filter_pb == expected_pb


def test__filter_pb_bad_type():
    from google.cloud.firestore_v1.base_query import _filter_pb

    with pytest.raises(ValueError):
        _filter_pb(None)


def test__cursor_pb_no_pair():
    from google.cloud.firestore_v1.base_query import _cursor_pb

    assert _cursor_pb(None) is None


def test__cursor_pb_success():
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.base_query import _cursor_pb
    from google.cloud.firestore_v1.types import query

    data = [1.5, 10, True]
    cursor_pair = data, True

    cursor_pb = _cursor_pb(cursor_pair)

    expected_pb = query.Cursor(
        values=[_helpers.encode_value(value) for value in data], before=True
    )
    assert cursor_pb == expected_pb


def test__query_response_to_snapshot_empty():
    from google.cloud.firestore_v1.base_query import _query_response_to_snapshot

    response_pb = _make_query_response()
    snapshot = _query_response_to_snapshot(response_pb, None, None)
    assert snapshot is None


def test__query_response_to_snapshot_after_offset():
    from google.cloud.firestore_v1.base_query import _query_response_to_snapshot

    skipped_results = 410
    response_pb = _make_query_response(skipped_results=skipped_results)
    snapshot = _query_response_to_snapshot(response_pb, None, None)
    assert snapshot is None


def test__query_response_to_snapshot_response():
    from google.cloud.firestore_v1.base_query import _query_response_to_snapshot
    from google.cloud.firestore_v1.document import DocumentSnapshot

    client = make_client()
    collection = client.collection("a", "b", "c")
    _, expected_prefix = collection._parent_info()

    # Create name for the protobuf.
    doc_id = "gigantic"
    name = "{}/{}".format(expected_prefix, doc_id)
    data = {"a": 901, "b": True}
    response_pb = _make_query_response(name=name, data=data)

    snapshot = _query_response_to_snapshot(response_pb, collection, expected_prefix)
    assert isinstance(snapshot, DocumentSnapshot)
    expected_path = collection._path + (doc_id,)
    assert snapshot.reference._path == expected_path
    assert snapshot.to_dict() == data
    assert snapshot.exists
    assert snapshot.read_time == response_pb.read_time
    assert snapshot.create_time == response_pb.document.create_time
    assert snapshot.update_time == response_pb.document.update_time


def test__collection_group_query_response_to_snapshot_empty():
    from google.cloud.firestore_v1.base_query import (
        _collection_group_query_response_to_snapshot,
    )

    response_pb = _make_query_response()
    snapshot = _collection_group_query_response_to_snapshot(response_pb, None)
    assert snapshot is None


def test__collection_group_query_response_to_snapshot_after_offset():
    from google.cloud.firestore_v1.base_query import (
        _collection_group_query_response_to_snapshot,
    )

    skipped_results = 410
    response_pb = _make_query_response(skipped_results=skipped_results)
    snapshot = _collection_group_query_response_to_snapshot(response_pb, None)
    assert snapshot is None


def test__collection_group_query_response_to_snapshot_response():
    from google.cloud.firestore_v1.base_query import (
        _collection_group_query_response_to_snapshot,
    )
    from google.cloud.firestore_v1.document import DocumentSnapshot

    client = make_client()
    collection = client.collection("a", "b", "c")
    other_collection = client.collection("a", "b", "d")
    to_match = other_collection.document("gigantic")
    data = {"a": 901, "b": True}
    response_pb = _make_query_response(name=to_match._document_path, data=data)

    snapshot = _collection_group_query_response_to_snapshot(response_pb, collection)
    assert isinstance(snapshot, DocumentSnapshot)
    assert snapshot.reference._document_path == to_match._document_path
    assert snapshot.to_dict() == data
    assert snapshot.exists
    assert snapshot.read_time == response_pb._pb.read_time
    assert snapshot.create_time == response_pb._pb.document.create_time
    assert snapshot.update_time == response_pb._pb.document.update_time


def test__query_pipeline_decendants():
    client = make_client()
    query = client.collection_group("my_col")
    pipeline = query._build_pipeline(client.pipeline())

    assert len(pipeline.stages) == 1
    stage = pipeline.stages[0]
    assert isinstance(stage, stages.CollectionGroup)
    assert stage.collection_id == "my_col"


@pytest.mark.parametrize(
    "in_path,out_path",
    [
        ("my_col/doc/", "/my_col/doc/"),
        ("/my_col/doc", "/my_col/doc"),
        ("my_col/doc/sub_col", "/my_col/doc/sub_col"),
    ],
)
def test__query_pipeline_no_decendants(in_path, out_path):
    client = make_client()
    collection = client.collection(in_path)
    query = collection._query()
    pipeline = query._build_pipeline(client.pipeline())

    assert len(pipeline.stages) == 1
    stage = pipeline.stages[0]
    assert isinstance(stage, stages.Collection)
    assert stage.path == out_path


def test__query_pipeline_composite_filter():
    from google.cloud.firestore_v1 import FieldFilter
    from google.cloud.firestore_v1 import pipeline_expressions as expr

    client = make_client()
    in_filter = FieldFilter("field_a", "==", "value_a")
    query = client.collection("my_col").where(filter=in_filter)
    with mock.patch.object(
        expr.BooleanExpression, "_from_query_filter_pb"
    ) as convert_mock:
        pipeline = query._build_pipeline(client.pipeline())
        convert_mock.assert_called_once_with(in_filter._to_pb(), client)
        assert len(pipeline.stages) == 2
        stage = pipeline.stages[1]
        assert isinstance(stage, stages.Where)
        assert stage.condition == convert_mock.return_value


def test__query_pipeline_projections():
    client = make_client()
    query = client.collection("my_col").select(["field_a", "field_b.c"])
    pipeline = query._build_pipeline(client.pipeline())

    assert len(pipeline.stages) == 2
    stage = pipeline.stages[1]
    assert isinstance(stage, stages.Select)
    assert len(stage.projections) == 2
    assert stage.projections[0].path == "field_a"
    assert stage.projections[1].path == "field_b.c"


def test__query_pipeline_order_exists_multiple():
    from google.cloud.firestore_v1 import pipeline_expressions as expr

    client = make_client()
    query = client.collection("my_col").order_by("field_a").order_by("field_b")
    pipeline = query._build_pipeline(client.pipeline())

    # should have collection, where, and sort
    # we're interested in where
    assert len(pipeline.stages) == 3
    where_stage = pipeline.stages[1]
    assert isinstance(where_stage, stages.Where)
    # should have and with both orderings
    assert isinstance(where_stage.condition, expr.And)
    assert len(where_stage.condition.params) == 2
    operands = [p for p in where_stage.condition.params]
    assert operands[0].name == "exists"
    assert operands[0].params[0].path == "field_a"
    assert operands[1].name == "exists"
    assert operands[1].params[0].path == "field_b"


def test__query_pipeline_order_exists_single():
    client = make_client()
    query_single = client.collection("my_col").order_by("field_c")
    pipeline_single = query_single._build_pipeline(client.pipeline())

    # should have collection, where, and sort
    # we're interested in where
    assert len(pipeline_single.stages) == 3
    where_stage_single = pipeline_single.stages[1]
    assert isinstance(where_stage_single, stages.Where)
    assert where_stage_single.condition.name == "exists"
    assert where_stage_single.condition.params[0].path == "field_c"


def test__query_pipeline_order_sorts():
    from google.cloud.firestore_v1 import pipeline_expressions as expr
    from google.cloud.firestore_v1.base_query import BaseQuery

    client = make_client()
    query = (
        client.collection("my_col")
        .order_by("field_a", direction=BaseQuery.ASCENDING)
        .order_by("field_b", direction=BaseQuery.DESCENDING)
    )
    pipeline = query._build_pipeline(client.pipeline())

    assert len(pipeline.stages) == 3
    sort_stage = pipeline.stages[2]
    assert isinstance(sort_stage, stages.Sort)
    assert len(sort_stage.orders) == 2
    assert isinstance(sort_stage.orders[0], expr.Ordering)
    assert sort_stage.orders[0].expr.path == "field_a"
    assert sort_stage.orders[0].order_dir == expr.Ordering.Direction.ASCENDING
    assert isinstance(sort_stage.orders[1], expr.Ordering)
    assert sort_stage.orders[1].expr.path == "field_b"
    assert sort_stage.orders[1].order_dir == expr.Ordering.Direction.DESCENDING


def test__query_pipeline_cursors():
    from google.cloud.firestore_v1 import pipeline_expressions as expr

    client = make_client()
    query_start = (
        client.collection("my_col").order_by("field_a").start_at({"field_a": 10})
    )
    pipeline = query_start._build_pipeline(client.pipeline())

    # Stages:
    # 0: Collection
    # 1: Where (exists field_a) - Generated because field_a is explicitly ordered
    # 2: Where (cursor condition)
    # 3: Sort (field_a)
    assert len(pipeline.stages) == 4

    where_stage = pipeline.stages[2]
    assert isinstance(where_stage, stages.Where)
    # Expected: (field_a > 10) OR (field_a == 10)
    assert isinstance(where_stage.condition, expr.Or)
    params = where_stage.condition.params
    assert len(params) == 2
    assert params[0].name == "greater_than"
    assert params[1].name == "equal"


def test__query_pipeline_limit_to_last():
    from google.cloud.firestore_v1 import pipeline_expressions as expr

    client = make_client()
    query = client.collection("my_col").order_by("field_a").limit_to_last(5)
    pipeline = query._build_pipeline(client.pipeline())

    # Stages:
    # 0: Collection
    # 1: Where (exists field_a)
    # 2: Sort (field_a DESC) - Reversed
    # 3: Limit (5)
    # 4: Sort (field_a ASC) - Restored
    assert len(pipeline.stages) == 5

    sort_reversed = pipeline.stages[2]
    assert isinstance(sort_reversed, stages.Sort)
    assert sort_reversed.orders[0].order_dir == expr.Ordering.Direction.DESCENDING

    limit_stage = pipeline.stages[3]
    assert isinstance(limit_stage, stages.Limit)
    assert limit_stage.limit == 5

    sort_restored = pipeline.stages[4]
    assert isinstance(sort_restored, stages.Sort)
    assert sort_restored.orders[0].order_dir == expr.Ordering.Direction.ASCENDING


def test__query_pipeline_limit_to_last_descending():
    from google.cloud.firestore_v1 import pipeline_expressions as expr
    from google.cloud.firestore_v1.base_query import BaseQuery

    client = make_client()
    # User orders by field_a DESCENDING
    query = (
        client.collection("my_col")
        .order_by("field_a", direction=BaseQuery.DESCENDING)
        .limit_to_last(5)
    )
    pipeline = query._build_pipeline(client.pipeline())

    # Stages:
    # 0: Collection
    # 1: Where (exists field_a)
    # 2: Sort (field_a ASCENDING) - Reversed from DESCENDING
    # 3: Limit (5)
    # 4: Sort (field_a DESCENDING) - Restored to original
    assert len(pipeline.stages) == 5

    sort_reversed = pipeline.stages[2]
    assert isinstance(sort_reversed, stages.Sort)
    # Should be ASCENDING because original was DESCENDING
    assert sort_reversed.orders[0].order_dir == expr.Ordering.Direction.ASCENDING

    limit_stage = pipeline.stages[3]
    assert isinstance(limit_stage, stages.Limit)
    assert limit_stage.limit == 5

    sort_restored = pipeline.stages[4]
    assert isinstance(sort_restored, stages.Sort)
    # Should be DESCENDING (original)
    assert sort_restored.orders[0].order_dir == expr.Ordering.Direction.DESCENDING


def test__query_pipeline_limit():
    client = make_client()
    query = client.collection("my_col").limit(15)
    pipeline = query._build_pipeline(client.pipeline())

    assert len(pipeline.stages) == 2
    stage = pipeline.stages[1]
    assert isinstance(stage, stages.Limit)
    assert stage.limit == 15


def test__query_pipeline_offset():
    client = make_client()
    query = client.collection("my_col").offset(5)
    pipeline = query._build_pipeline(client.pipeline())

    assert len(pipeline.stages) == 2
    stage = pipeline.stages[1]
    assert isinstance(stage, stages.Offset)
    assert stage.offset == 5


def _make_order_pb(field_path, direction):
    from google.cloud.firestore_v1.types import query

    return query.StructuredQuery.Order(
        field=query.StructuredQuery.FieldReference(field_path=field_path),
        direction=direction,
    )


def _make_query_response(**kwargs):
    # kwargs supported are ``skipped_results``, ``name``, ``data``
    # and ``explain_metrics``
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import document, firestore, query_profile

    now = datetime.datetime.now(tz=datetime.timezone.utc)
    read_time = _datetime_to_pb_timestamp(now)
    kwargs["read_time"] = read_time

    name = kwargs.pop("name", None)
    data = kwargs.pop("data", None)
    if name is not None and data is not None:
        document_pb = document.Document(name=name, fields=_helpers.encode_dict(data))
        delta = datetime.timedelta(seconds=100)
        update_time = _datetime_to_pb_timestamp(now - delta)
        create_time = _datetime_to_pb_timestamp(now - 2 * delta)
        document_pb._pb.update_time.CopyFrom(update_time)
        document_pb._pb.create_time.CopyFrom(create_time)

        kwargs["document"] = document_pb

    explain_metrics = kwargs.pop("explain_metrics", None)
    if explain_metrics is not None:
        kwargs["explain_metrics"] = query_profile.ExplainMetrics(explain_metrics)

    return firestore.RunQueryResponse(**kwargs)


def _make_cursor_pb(pair):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.types import query

    values, before = pair
    value_pbs = [_helpers.encode_value(value) for value in values]
    return query.Cursor(values=value_pbs, before=before)


def _make_query_partition(*args, **kwargs):
    from google.cloud.firestore_v1.base_query import QueryPartition

    return QueryPartition(*args, **kwargs)


def test_constructor():
    partition = _make_query_partition(mock.sentinel.query, "start", "end")
    assert partition._query is mock.sentinel.query
    assert partition.start_at == "start"
    assert partition.end_at == "end"


def test_query_begin():
    partition = _make_query_partition(DummyQuery("PARENT"), None, "end")
    query = partition.query()
    assert query._parent == "PARENT"
    assert query.all_descendants == "YUP"
    assert query.orders == "ORDER"
    assert query.start_at is None
    assert query.end_at == (["end"], True)


def test_query_middle():
    partition = _make_query_partition(DummyQuery("PARENT"), "start", "end")
    query = partition.query()
    assert query._parent == "PARENT"
    assert query.all_descendants == "YUP"
    assert query.orders == "ORDER"
    assert query.start_at == (["start"], True)
    assert query.end_at == (["end"], True)


def test_query_end():
    partition = _make_query_partition(DummyQuery("PARENT"), "start", None)
    query = partition.query()
    assert query._parent == "PARENT"
    assert query.all_descendants == "YUP"
    assert query.orders == "ORDER"
    assert query.start_at == (["start"], True)
    assert query.end_at is None


def test_base_composite_filter_constructor():
    from google.cloud.firestore_v1.base_query import BaseCompositeFilter
    from google.cloud.firestore_v1.types import query

    comp_filter = BaseCompositeFilter()
    assert (
        comp_filter.operator
        == query.StructuredQuery.CompositeFilter.Operator.OPERATOR_UNSPECIFIED
    )
    assert len(comp_filter.filters) == 0


class DummyQuery:
    _all_descendants = "YUP"
    _PARTITION_QUERY_ORDER = "ORDER"

    def __init__(
        self, parent, *, all_descendants=None, orders=None, start_at=None, end_at=None
    ):
        self._parent = parent
        self.all_descendants = all_descendants
        self.orders = orders
        self.start_at = start_at
        self.end_at = end_at


def _make_projection_for_select(field_paths):
    from google.cloud.firestore_v1.types import query

    return query.StructuredQuery.Projection(
        fields=[
            query.StructuredQuery.FieldReference(field_path=field_path)
            for field_path in field_paths
        ]
    )


def _make_collection(*path, **kw):
    from google.cloud.firestore_v1 import collection

    return collection.CollectionReference(*path, **kw)


def _make_docref(*path, **kw):
    from google.cloud.firestore_v1 import document

    return document.DocumentReference(*path, **kw)


def _make_snapshot(docref, values):
    from google.cloud.firestore_v1 import document

    return document.DocumentSnapshot(docref, values, True, None, None, None)


def test__where_conditions_from_cursor_descending():
    from google.cloud.firestore_v1 import pipeline_expressions
    from google.cloud.firestore_v1.base_query import _where_conditions_from_cursor

    # Create ordering: field DESC
    field_expr = pipeline_expressions.Field.of("field")
    ordering = pipeline_expressions.Ordering(field_expr, "descending")

    # Case 1: StartAt (inclusive) -> <= 10
    cursor = ([10], True)
    condition = _where_conditions_from_cursor(cursor, [ordering], is_start_cursor=True)
    # Expected: field < 10 OR field == 10
    expected = pipeline_expressions.Or(field_expr.less_than(10), field_expr.equal(10))
    assert condition == expected

    # Case 2: StartAfter (exclusive) -> < 10
    cursor = ([10], False)
    condition = _where_conditions_from_cursor(cursor, [ordering], is_start_cursor=True)
    # Expected: field < 10
    expected = field_expr.less_than(10)
    assert condition == expected

    # Case 3: EndAt (inclusive) -> >= 10
    cursor = ([10], False)
    condition = _where_conditions_from_cursor(cursor, [ordering], is_start_cursor=False)
    # Expected: field > 10 OR field == 10
    expected = pipeline_expressions.Or(
        field_expr.greater_than(10), field_expr.equal(10)
    )
    assert condition == expected

    # Case 4: EndBefore (exclusive) -> > 10
    cursor = ([10], True)
    condition = _where_conditions_from_cursor(cursor, [ordering], is_start_cursor=False)
    # Expected: field > 10
    expected = field_expr.greater_than(10)
    assert condition == expected


def test__query_pipeline_end_at():
    from google.cloud.firestore_v1 import pipeline_expressions as expr

    client = make_client()
    query_end = client.collection("my_col").order_by("field_a").end_at({"field_a": 10})
    pipeline = query_end._build_pipeline(client.pipeline())

    # Stages:
    # 0: Collection
    # 1: Where (exists field_a)
    # 2: Where (cursor condition)
    # 3: Sort (field_a)
    assert len(pipeline.stages) == 4

    where_stage = pipeline.stages[2]
    assert isinstance(where_stage, stages.Where)
    # Expected: (field_a < 10) OR (field_a == 10)
    assert isinstance(where_stage.condition, expr.Or)
    params = where_stage.condition.params
    assert len(params) == 2
    assert params[0].name == "less_than"
    assert params[1].name == "equal"


def test__where_conditions_from_cursor_multi_field():
    from google.cloud.firestore_v1 import pipeline_expressions as expr
    from google.cloud.firestore_v1.base_query import _where_conditions_from_cursor

    # Order by: A ASC, B DESC
    field_a = expr.Field.of("A")
    field_b = expr.Field.of("B")
    ordering_a = expr.Ordering(field_a, "ascending")
    ordering_b = expr.Ordering(field_b, "descending")
    orderings = [ordering_a, ordering_b]

    # Cursor: A=1, B=2. StartAt (inclusive)
    # Logic: (A > 1) OR (A == 1 AND (B < 2 OR B == 2))
    # Note: B is DESC, so start_at means <= 2
    cursor = ([1, 2], True)

    condition = _where_conditions_from_cursor(cursor, orderings, is_start_cursor=True)

    # Verify structure: Or(A > 1, And(A == 1, Or(B < 2, B == 2)))
    assert isinstance(condition, expr.Or)
    # First term: A > 1
    term1 = condition.params[0]
    assert term1.name == "greater_than"
    assert term1.params[0] == field_a
    assert term1.params[1] == expr.Constant(1)

    # Second term: And(...)
    term2 = condition.params[1]
    assert isinstance(term2, expr.And)

    # Inside And: A == 1
    sub_term1 = term2.params[0]
    assert sub_term1.name == "equal"
    assert sub_term1.params[0] == field_a
    assert sub_term1.params[1] == expr.Constant(1)

    # Inside And: Or(B < 2, B == 2)  <-- DESCENDING logic check
    sub_term2 = term2.params[1]
    assert isinstance(sub_term2, expr.Or)

    # B < 2 (because DESC start_at)
    sub_sub_term1 = sub_term2.params[0]
    assert sub_sub_term1.name == "less_than"
    assert sub_sub_term1.params[0] == field_b
    assert sub_sub_term1.params[1] == expr.Constant(2)

    # B == 2
    sub_sub_term2 = sub_term2.params[1]
    assert sub_sub_term2.name == "equal"
    assert sub_sub_term2.params[0] == field_b
    assert sub_sub_term2.params[1] == expr.Constant(2)


def test__reverse_orderings_descending():
    from google.cloud.firestore_v1 import pipeline_expressions as expr
    from google.cloud.firestore_v1.base_query import _reverse_orderings

    # Input: A ASC, B DESC
    field_a = expr.Field.of("A")
    field_b = expr.Field.of("B")
    ord_a = expr.Ordering(field_a, "ascending")
    ord_b = expr.Ordering(field_b, "descending")

    reversed_ords = _reverse_orderings([ord_a, ord_b])

    assert len(reversed_ords) == 2
    # Expect: A DESC, B ASC
    assert reversed_ords[0].expr == field_a
    assert reversed_ords[0].order_dir == expr.Ordering.Direction.DESCENDING

    assert reversed_ords[1].expr == field_b
    assert reversed_ords[1].order_dir == expr.Ordering.Direction.ASCENDING
