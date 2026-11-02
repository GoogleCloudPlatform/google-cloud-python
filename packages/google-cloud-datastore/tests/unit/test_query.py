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
import datetime

import mock
import pytest

from google.cloud.datastore.helpers import set_database_id_to_request
from google.cloud.datastore.query import (
    And,
    BaseCompositeFilter,
    Or,
    PropertyFilter,
    Query,
)

_PROJECT = "PROJECT"


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ctor_defaults(database_id):
    client = _make_client(database=database_id)
    query = _make_query(client)
    assert query._client is client
    assert query._client.database == client.database
    assert query.project == client.project
    assert query.kind is None
    assert query.namespace == client.namespace
    assert query.ancestor is None
    assert query.filters == []
    assert query.projection == []
    assert query.order == []
    assert query.distinct_on == []


@pytest.mark.parametrize(
    "filters",
    [
        [("foo", "=", "Qux"), ("bar", "<", 17)],
        [PropertyFilter("foo", "=", "Qux"), PropertyFilter("bar", "<", 17)],
        [And([PropertyFilter("foo", "=", "Qux"), PropertyFilter("bar", "<", 17)])],
        [Or([PropertyFilter("foo", "=", "Qux"), PropertyFilter("bar", "<", 17)])],
    ],
)
@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ctor_explicit(filters, database_id):
    from google.cloud.datastore.key import Key

    _PROJECT = "OTHER_PROJECT"
    _KIND = "KIND"
    _NAMESPACE = "OTHER_NAMESPACE"
    client = _make_client(database=database_id)
    ancestor = Key("ANCESTOR", 123, project=_PROJECT, database=database_id)
    FILTERS = filters
    PROJECTION = ["foo", "bar", "baz"]
    ORDER = ["foo", "bar"]
    DISTINCT_ON = ["foo"]

    query = _make_query(
        client,
        kind=_KIND,
        project=_PROJECT,
        namespace=_NAMESPACE,
        ancestor=ancestor,
        filters=FILTERS,
        projection=PROJECTION,
        order=ORDER,
        distinct_on=DISTINCT_ON,
    )
    assert query._client is client
    assert query._client.database == database_id
    assert query.project == _PROJECT
    assert query.kind == _KIND
    assert query.namespace == _NAMESPACE
    assert query.ancestor.path == ancestor.path
    assert query.filters == FILTERS
    assert query.projection == PROJECTION
    assert query.order == ORDER
    assert query.distinct_on == DISTINCT_ON


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ctor_bad_projection(database_id):
    BAD_PROJECTION = object()
    with pytest.raises(TypeError):
        _make_query(_make_client(database=database_id), projection=BAD_PROJECTION)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ctor_bad_order(database_id):
    BAD_ORDER = object()
    with pytest.raises(TypeError):
        _make_query(_make_client(database=database_id), order=BAD_ORDER)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ctor_bad_distinct_on(database_id):
    BAD_DISTINCT_ON = object()
    with pytest.raises(TypeError):
        _make_query(_make_client(database=database_id), distinct_on=BAD_DISTINCT_ON)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ctor_bad_filters(database_id):
    FILTERS_CANT_UNPACK = [("one", "two")]
    with pytest.raises(ValueError):
        _make_query(_make_client(database=database_id), filters=FILTERS_CANT_UNPACK)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_project_getter(database_id):
    PROJECT = "PROJECT"
    query = _make_query(_make_client(database=database_id), project=PROJECT)
    assert query.project == PROJECT


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_database_getter(database_id):
    query = _make_query(_make_client(database=database_id))
    assert query._client.database == database_id


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_namespace_setter_w_non_string(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.raises(ValueError):
        query.namespace = object()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_namespace_setter(database_id):
    _NAMESPACE = "OTHER_NAMESPACE"
    query = _make_query(_make_client(database=database_id))
    query.namespace = _NAMESPACE
    assert query.namespace == _NAMESPACE


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_kind_setter_w_non_string(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.raises(TypeError):
        query.kind = object()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_kind_setter_wo_existing(database_id):
    _KIND = "KIND"
    query = _make_query(_make_client(database=database_id))
    query.kind = _KIND
    assert query.kind == _KIND


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_kind_setter_w_existing(database_id):
    _KIND_BEFORE = "KIND_BEFORE"
    _KIND_AFTER = "KIND_AFTER"
    query = _make_query(_make_client(database=database_id), kind=_KIND_BEFORE)
    assert query.kind == _KIND_BEFORE
    query.kind = _KIND_AFTER
    assert query.project == _PROJECT
    assert query.kind == _KIND_AFTER


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ancestor_setter_w_non_key(database_id):
    query = _make_query(_make_client(database=database_id))

    with pytest.raises(TypeError):
        query.ancestor = object()

    with pytest.raises(TypeError):
        query.ancestor = ["KIND", "NAME"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ancestor_setter_w_key(database_id):
    from google.cloud.datastore.key import Key

    _NAME = "NAME"
    key = Key("KIND", 123, project=_PROJECT, database=database_id)
    query = _make_query(_make_client(database=database_id))
    query.add_filter("name", "=", _NAME)
    query.ancestor = key
    assert query.ancestor.path == key.path


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ancestor_setter_w_key_property_filter(database_id):
    from google.cloud.datastore.key import Key

    _NAME = "NAME"
    key = Key("KIND", 123, project=_PROJECT, database=database_id)
    query = _make_query(_make_client(database=database_id))
    query.add_filter(filter=PropertyFilter("name", "=", _NAME))
    query.ancestor = key
    assert query.ancestor.path == key.path


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_ancestor_deleter_w_key(database_id):
    from google.cloud.datastore.key import Key

    key = Key("KIND", 123, project=_PROJECT, database=database_id)
    query = _make_query(client=_make_client(database=database_id), ancestor=key)
    del query.ancestor
    assert query.ancestor is None


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter_setter_w_unknown_operator(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.raises(ValueError) as exc:
        query.add_filter("firstname", "~~", "John")
    assert "Invalid expression:" in str(exc.value)
    assert "Please use one of: =, <, <=, >, >=, !=, IN, NOT_IN." in str(exc.value)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_property_filter_setter_w_unknown_operator(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.raises(ValueError) as exc:
        query.add_filter(filter=PropertyFilter("firstname", "~~", "John"))
    assert "Invalid expression:" in str(exc.value)
    assert "Please use one of: =, <, <=, >, >=, !=, IN, NOT_IN." in str(exc.value)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter_w_known_operator(database_id):
    query = _make_query(_make_client(database=database_id))
    query.add_filter("firstname", "=", "John")
    assert query.filters == [("firstname", "=", "John")]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_property_filter_w_known_operator(database_id):
    query = _make_query(_make_client(database=database_id))
    property_filter = PropertyFilter("firstname", "=", "John")
    query.add_filter(filter=property_filter)
    assert query.filters == [property_filter]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter_w_all_operators(database_id):
    query = _make_query(_make_client(database=database_id))
    query.add_filter("leq_prop", "<=", "val1")
    query.add_filter("geq_prop", ">=", "val2")
    query.add_filter("lt_prop", "<", "val3")
    query.add_filter("gt_prop", ">", "val4")
    query.add_filter("eq_prop", "=", "val5")
    query.add_filter("in_prop", "IN", ["val6"])
    query.add_filter("neq_prop", "!=", "val9")
    query.add_filter("not_in_prop", "NOT_IN", ["val13"])
    assert len(query.filters) == 8
    assert query.filters[0] == ("leq_prop", "<=", "val1")
    assert query.filters[1] == ("geq_prop", ">=", "val2")
    assert query.filters[2] == ("lt_prop", "<", "val3")
    assert query.filters[3] == ("gt_prop", ">", "val4")
    assert query.filters[4] == ("eq_prop", "=", "val5")
    assert query.filters[5] == ("in_prop", "IN", ["val6"])
    assert query.filters[6] == ("neq_prop", "!=", "val9")
    assert query.filters[7] == ("not_in_prop", "NOT_IN", ["val13"])


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_property_filter_w_all_operators(database_id):
    query = _make_query(_make_client(database=database_id))
    filters = [
        ("leq_prop", "<=", "val1"),
        ("geq_prop", ">=", "val2"),
        ("lt_prop", "<", "val3"),
        ("gt_prop", ">", "val4"),
        ("eq_prop", "=", "val5"),
        ("in_prop", "IN", ["val6"]),
        ("neq_prop", "!=", "val9"),
        ("not_in_prop", "NOT_IN", ["val13"]),
    ]
    property_filters = [PropertyFilter(*filter) for filter in filters]

    for filter in property_filters:
        query.add_filter(filter=filter)

    assert len(query.filters) == 8

    for i in range(8):
        assert query.filters[i] == property_filters[i]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter_w_known_operator_and_entity(database_id):
    from google.cloud.datastore.entity import Entity

    query = _make_query(_make_client(database=database_id))
    other = Entity()
    other["firstname"] = "John"
    other["lastname"] = "Smith"
    query.add_filter("other", "=", other)
    assert query.filters == [("other", "=", other)]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_property_filter_w_known_operator_and_entity(database_id):
    from google.cloud.datastore.entity import Entity

    query = _make_query(_make_client(database=database_id))
    other = Entity()
    other["firstname"] = "John"
    other["lastname"] = "Smith"
    property_filter = PropertyFilter("other", "=", other)
    query.add_filter(filter=property_filter)
    assert query.filters == [property_filter]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter_w_whitespace_property_name(database_id):
    query = _make_query(_make_client(database=database_id))
    PROPERTY_NAME = "  property with lots of space "
    query.add_filter(PROPERTY_NAME, "=", "John")
    assert query.filters == [(PROPERTY_NAME, "=", "John")]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_property_filter_w_whitespace_property_name(database_id):
    query = _make_query(_make_client(database=database_id))
    PROPERTY_NAME = "  property with lots of space "
    property_filter = PropertyFilter(PROPERTY_NAME, "=", "John")
    query.add_filter(filter=property_filter)
    assert query.filters == [property_filter]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter___key__valid_key(database_id):
    from google.cloud.datastore.key import Key

    query = _make_query(_make_client(database=database_id))
    key = Key("Foo", project=_PROJECT, database=database_id)
    query.add_filter("__key__", "=", key)
    assert query.filters == [("__key__", "=", key)]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_property_filter___key__valid_key(database_id):
    from google.cloud.datastore.key import Key

    query = _make_query(_make_client(database=database_id))
    key = Key("Foo", project=_PROJECT, database=database_id)
    property_filter = PropertyFilter("__key__", "=", key)
    query.add_filter(filter=property_filter)
    assert query.filters == [property_filter]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter_return_query_obj(database_id):
    from google.cloud.datastore.query import Query

    query = _make_query(_make_client(database=database_id))
    query_obj = query.add_filter("firstname", "=", "John")
    assert isinstance(query_obj, Query)
    assert query_obj.filters == [("firstname", "=", "John")]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_property_filter_without_keyword_argument(database_id):
    query = _make_query(_make_client(database=database_id))
    property_filter = PropertyFilter("firstname", "=", "John")
    with pytest.raises(ValueError) as exc:
        query.add_filter(property_filter)

    assert (
        "PropertyFilter object must be passed using keyword argument 'filter'"
        in str(exc.value)
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_composite_filter_without_keyword_argument(database_id):
    query = _make_query(_make_client(database=database_id))
    and_filter = And(["firstname", "=", "John"])
    with pytest.raises(ValueError) as exc:
        query.add_filter(and_filter)

    assert (
        "'Or' and 'And' objects must be passed using keyword argument 'filter'"
        in str(exc.value)
    )

    or_filter = Or(["firstname", "=", "John"])
    with pytest.raises(ValueError) as exc:
        query.add_filter(or_filter)

    assert (
        "'Or' and 'And' objects must be passed using keyword argument 'filter'"
        in str(exc.value)
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_positional_args_and_property_filter(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.raises(ValueError) as exc:
        query.add_filter("firstname", "=", "John", filter=("name", "=", "Blabla"))

    assert (
        "Can't pass in both the positional arguments and 'filter' at the same time"
        in str(exc.value)
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_positional_args_and_composite_filter(database_id):
    query = _make_query(_make_client(database=database_id))
    and_filter = And(["firstname", "=", "John"])
    with pytest.raises(ValueError) as exc:
        query.add_filter("firstname", "=", "John", filter=and_filter)

    assert (
        "Can't pass in both the positional arguments and 'filter' at the same time"
        in str(exc.value)
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_add_filter_with_positional_args_raises_user_warning(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.warns(
        UserWarning,
        match="Detected filter using positional arguments",
    ):
        query.add_filter("firstname", "=", "John")

    with pytest.warns(
        UserWarning,
        match="Detected filter using positional arguments",
    ):
        _make_stub_query(filters=[("name", "=", "John")])


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_filter___key__not_equal_operator(database_id):
    from google.cloud.datastore.key import Key

    key = Key("Foo", project=_PROJECT, database=database_id)
    query = _make_query(_make_client(database=database_id))
    query.add_filter("__key__", "<", key)
    assert query.filters == [("__key__", "<", key)]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_property_filter___key__not_equal_operator(database_id):
    from google.cloud.datastore.key import Key

    key = Key("Foo", project=_PROJECT, database=database_id)
    query = _make_query(_make_client(database=database_id))
    property_filter = PropertyFilter("__key__", "<", key)
    query.add_filter(filter=property_filter)
    assert query.filters == [property_filter]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_filter___key__invalid_value(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.raises(ValueError) as exc:
        query.add_filter("__key__", "=", None)
    assert "Invalid key:" in str(exc.value)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_property_filter___key__invalid_value(database_id):
    query = _make_query(_make_client(database=database_id))
    with pytest.raises(ValueError) as exc:
        query.add_filter(filter=PropertyFilter("__key__", "=", None))
    assert "Invalid key:" in str(exc.value)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_projection_setter_empty(database_id):
    query = _make_query(_make_client(database=database_id))
    query.projection = []
    assert query.projection == []


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_projection_setter_string(database_id):
    query = _make_query(_make_client(database=database_id))
    query.projection = "field1"
    assert query.projection == ["field1"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_projection_setter_non_empty(database_id):
    query = _make_query(_make_client(database=database_id))
    query.projection = ["field1", "field2"]
    assert query.projection == ["field1", "field2"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_projection_setter_multiple_calls(database_id):
    _PROJECTION1 = ["field1", "field2"]
    _PROJECTION2 = ["field3"]
    query = _make_query(_make_client(database=database_id))
    query.projection = _PROJECTION1
    assert query.projection == _PROJECTION1
    query.projection = _PROJECTION2
    assert query.projection == _PROJECTION2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_keys_only(database_id):
    query = _make_query(_make_client(database=database_id))
    query.keys_only()
    assert query.projection == ["__key__"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_key_filter_defaults(database_id):
    from google.cloud.datastore.key import Key

    client = _make_client(database=database_id)
    query = _make_query(client)
    assert query.filters == []
    key = Key("Kind", 1234, project="project", database=database_id)
    query.key_filter(key)
    assert query.filters == [("__key__", "=", key)]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_key_filter_explicit(database_id):
    from google.cloud.datastore.key import Key

    client = _make_client(database=database_id)
    query = _make_query(client)
    assert query.filters == []
    key = Key("Kind", 1234, project="project", database=database_id)
    query.key_filter(key, operator=">")
    assert query.filters == [("__key__", ">", key)]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_order_setter_empty(database_id):
    query = _make_query(_make_client(database=database_id), order=["foo", "-bar"])
    query.order = []
    assert query.order == []


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_order_setter_string(database_id):
    query = _make_query(_make_client(database=database_id))
    query.order = "field"
    assert query.order == ["field"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_order_setter_single_item_list_desc(database_id):
    query = _make_query(_make_client(database=database_id))
    query.order = ["-field"]
    assert query.order == ["-field"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_order_setter_multiple(database_id):
    query = _make_query(_make_client(database=database_id))
    query.order = ["foo", "-bar"]
    assert query.order == ["foo", "-bar"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_distinct_on_setter_empty(database_id):
    query = _make_query(_make_client(database=database_id), distinct_on=["foo", "bar"])
    query.distinct_on = []
    assert query.distinct_on == []


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_distinct_on_setter_string(database_id):
    query = _make_query(_make_client(database=database_id))
    query.distinct_on = "field1"
    assert query.distinct_on == ["field1"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_distinct_on_setter_non_empty(database_id):
    query = _make_query(_make_client(database=database_id))
    query.distinct_on = ["field1", "field2"]
    assert query.distinct_on == ["field1", "field2"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_distinct_on_multiple_calls(database_id):
    _DISTINCT_ON1 = ["field1", "field2"]
    _DISTINCT_ON2 = ["field3"]
    query = _make_query(_make_client(database=database_id))
    query.distinct_on = _DISTINCT_ON1
    assert query.distinct_on == _DISTINCT_ON1
    query.distinct_on = _DISTINCT_ON2
    assert query.distinct_on == _DISTINCT_ON2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_fetch_defaults_w_client_attr(database_id):
    from google.cloud.datastore.query import Iterator

    client = _make_client(database=database_id)
    query = _make_query(client)

    iterator = query.fetch()

    assert isinstance(iterator, Iterator)
    assert iterator._query is query
    assert iterator.client is client
    assert iterator.max_results is None
    assert iterator._offset == 0
    assert iterator._retry is None
    assert iterator._timeout is None


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_fetch_w_explicit_client_w_retry_w_timeout(database_id):
    from google.cloud.datastore.query import Iterator

    client = _make_client(database=database_id)
    other_client = _make_client(database=database_id)
    query = _make_query(client)
    retry = mock.Mock()
    timeout = 100000

    iterator = query.fetch(
        limit=7, offset=8, client=other_client, retry=retry, timeout=timeout
    )

    assert isinstance(iterator, Iterator)
    assert iterator._query is query
    assert iterator.client is other_client
    assert iterator.max_results == 7
    assert iterator._offset == 8
    assert iterator._retry == retry
    assert iterator._timeout == timeout


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_eventual_transaction_fails(database_id):
    """
    Queries with eventual consistency cannot be used in a transaction.
    """
    import mock

    transaction = mock.Mock()
    transaction.id = b"expected_id"
    client = _Client(None, database=database_id, transaction=transaction)

    query = _make_query(client)
    with pytest.raises(ValueError):
        list(query.fetch(eventual=True))


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_transaction_id_populated(database_id):
    """
    When an query is run in the context of a transaction, the transaction
    ID should be populated in the request.
    """
    import mock

    transaction = mock.Mock()
    transaction.id = b"expected_id"
    mock_datastore_api = mock.Mock()
    mock_gapic = mock_datastore_api.run_query

    more_results_enum = 3  # NO_MORE_RESULTS
    response_pb = _make_query_response([], b"", more_results_enum, 0)
    mock_gapic.return_value = response_pb

    client = _Client(
        None,
        datastore_api=mock_datastore_api,
        database=database_id,
        transaction=transaction,
    )

    query = _make_query(client)
    # run mock query
    list(query.fetch())
    assert mock_gapic.call_count == 1
    request = mock_gapic.call_args[1]["request"]
    read_options = request["read_options"]
    # ensure transaction ID is populated
    assert read_options.transaction == client.current_transaction.id


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_query_transaction_begin_later(database_id):
    """
    When an aggregation is run in the context of a transaction with begin_later=True,
    the new_transaction field should be populated in the request read_options.
    """
    import mock

    from google.cloud.datastore_v1.types import TransactionOptions

    # make a fake begin_later transaction
    transaction = mock.Mock()
    transaction.id = None
    transaction._begin_later = True
    transaction._status = transaction._INITIAL
    transaction._options = TransactionOptions(read_only=TransactionOptions.ReadOnly())

    mock_datastore_api = mock.Mock()
    mock_gapic = mock_datastore_api.run_query

    more_results_enum = 3  # NO_MORE_RESULTS
    response_pb = _make_query_response([], b"", more_results_enum, 0)
    mock_gapic.return_value = response_pb

    client = _Client(
        None,
        datastore_api=mock_datastore_api,
        database=database_id,
        transaction=transaction,
    )

    query = _make_query(client)
    # run mock query
    list(query.fetch())
    assert mock_gapic.call_count == 1
    request = mock_gapic.call_args[1]["request"]
    read_options = request["read_options"]
    # ensure new_transaction is populated
    assert not read_options.transaction
    assert read_options.new_transaction == transaction._options


def test_iterator_constructor_defaults():
    query = object()
    client = object()

    iterator = _make_iterator(query, client)

    assert not iterator._started
    assert iterator.client is client
    assert iterator.max_results is None
    assert iterator.page_number == 0
    assert iterator.next_page_token is None
    assert iterator.num_results == 0
    assert iterator._query is query
    assert iterator._offset is None
    assert iterator._end_cursor is None
    assert iterator._more_results
    assert iterator._retry is None
    assert iterator._timeout is None


def test_iterator_constructor_explicit():
    query = object()
    client = object()
    limit = 43
    offset = 9
    start_cursor = b"8290\xff"
    end_cursor = b"so20rc\ta"
    retry = mock.Mock()
    timeout = 100000

    iterator = _make_iterator(
        query,
        client,
        limit=limit,
        offset=offset,
        start_cursor=start_cursor,
        end_cursor=end_cursor,
        retry=retry,
        timeout=timeout,
    )

    assert not iterator._started
    assert iterator.client is client
    assert iterator.max_results == limit
    assert iterator.page_number == 0
    assert iterator.next_page_token == start_cursor
    assert iterator.num_results == 0
    assert iterator._query is query
    assert iterator._offset == offset
    assert iterator._end_cursor == end_cursor
    assert iterator._more_results
    assert iterator._retry == retry
    assert iterator._timeout == timeout


def test_iterator__build_protobuf_empty():
    from google.cloud.datastore.query import Query
    from google.cloud.datastore_v1.types import query as query_pb2

    client = _Client(None)
    query = Query(client)
    iterator = _make_iterator(query, client)

    pb = iterator._build_protobuf()
    expected_pb = query_pb2.Query()
    assert pb == expected_pb


def test_iterator__build_protobuf_all_values_except_offset():
    # this test and the following (all_values_except_start_and_end_cursor)
    # test mutually exclusive states; the offset is ignored
    # if a start_cursor is supplied
    from google.cloud.datastore.query import Query
    from google.cloud.datastore_v1.types import query as query_pb2

    client = _Client(None)
    query = Query(client)
    limit = 15
    start_bytes = b"i\xb7\x1d"
    start_cursor = "abcd"
    end_bytes = b"\xc3\x1c\xb3"
    end_cursor = "wxyz"
    iterator = _make_iterator(
        query, client, limit=limit, start_cursor=start_cursor, end_cursor=end_cursor
    )
    assert iterator.max_results == limit
    iterator.num_results = 4
    iterator._skipped_results = 1

    pb = iterator._build_protobuf()
    expected_pb = query_pb2.Query(start_cursor=start_bytes, end_cursor=end_bytes)
    expected_pb._pb.limit.value = limit - iterator.num_results
    assert pb == expected_pb


def test_iterator__build_protobuf_all_values_except_start_and_end_cursor():
    # this test and the previous (all_values_except_start_offset)
    # test mutually exclusive states; the offset is ignored
    # if a start_cursor is supplied
    from google.cloud.datastore.query import Query
    from google.cloud.datastore_v1.types import query as query_pb2

    client = _Client(None)
    query = Query(client)
    limit = 15
    offset = 9
    iterator = _make_iterator(query, client, limit=limit, offset=offset)
    assert iterator.max_results == limit
    iterator.num_results = 4

    pb = iterator._build_protobuf()
    expected_pb = query_pb2.Query(offset=offset - iterator._skipped_results)
    expected_pb._pb.limit.value = limit - iterator.num_results
    assert pb == expected_pb


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__process_query_results(database_id):
    from google.cloud.datastore_v1.types import query as query_pb2

    iterator = _make_iterator(None, None, end_cursor="abcd")
    assert iterator._end_cursor is not None

    entity_pbs = [_make_entity("Hello", 9998, "PRAHJEKT", database=database_id)]
    cursor_as_bytes = b"\x9ai\xe7"
    cursor = b"mmnn"
    skipped_results = 4
    more_results_enum = query_pb2.QueryResultBatch.MoreResultsType.NOT_FINISHED
    response_pb = _make_query_response(
        entity_pbs, cursor_as_bytes, more_results_enum, skipped_results
    )
    result = iterator._process_query_results(response_pb)
    assert result == entity_pbs

    assert iterator._skipped_results == skipped_results
    assert iterator.next_page_token == cursor
    assert iterator._more_results


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__process_query_results_done(database_id):
    from google.cloud.datastore_v1.types import query as query_pb2

    iterator = _make_iterator(None, None, end_cursor="abcd")
    assert iterator._end_cursor is not None

    entity_pbs = [_make_entity("World", 1234, "PROJECT", database=database_id)]
    cursor_as_bytes = b"\x9ai\xe7"
    skipped_results = 44
    more_results_enum = query_pb2.QueryResultBatch.MoreResultsType.NO_MORE_RESULTS
    response_pb = _make_query_response(
        entity_pbs, cursor_as_bytes, more_results_enum, skipped_results
    )
    result = iterator._process_query_results(response_pb)
    assert result == entity_pbs

    assert iterator._skipped_results == skipped_results
    assert iterator.next_page_token is None
    assert not iterator._more_results


@pytest.mark.filterwarnings("ignore")
def test_iterator__process_query_results_bad_enum():
    iterator = _make_iterator(None, None)
    more_results_enum = 999
    response_pb = _make_query_response([], b"", more_results_enum, 0)
    with pytest.raises(ValueError):
        iterator._process_query_results(response_pb)


def _next_page_helper(
    txn_id=None, retry=None, timeout=None, read_time=None, database=None
):
    from google.api_core import page_iterator
    from google.protobuf.timestamp_pb2 import Timestamp

    from google.cloud.datastore.query import Query
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2
    from google.cloud.datastore_v1.types import query as query_pb2

    more_enum = query_pb2.QueryResultBatch.MoreResultsType.NOT_FINISHED
    result = _make_query_response([], b"", more_enum, 0)
    project = "prujekt"
    ds_api = _make_datastore_api(result)
    if txn_id is None:
        client = _Client(project, database=database, datastore_api=ds_api)
    else:
        transaction = mock.Mock(
            id=txn_id, _begin_later=False, spec=["id", "_begin_later"]
        )
        client = _Client(
            project, database=database, datastore_api=ds_api, transaction=transaction
        )

    query = Query(client)
    kwargs = {}

    if retry is not None:
        kwargs["retry"] = retry

    if timeout is not None:
        kwargs["timeout"] = timeout

    it_kwargs = kwargs.copy()
    if read_time is not None:
        it_kwargs["read_time"] = read_time

    iterator = _make_iterator(query, client, **it_kwargs)

    page = iterator._next_page()

    assert isinstance(page, page_iterator.Page)
    assert page._parent is iterator

    partition_id = entity_pb2.PartitionId(project_id=project, database_id=database)
    if txn_id is not None:
        read_options = datastore_pb2.ReadOptions(transaction=txn_id)
    elif read_time is not None:
        read_time_pb = Timestamp()
        read_time_pb.FromDatetime(read_time)
        read_options = datastore_pb2.ReadOptions(read_time=read_time_pb)
    else:
        read_options = datastore_pb2.ReadOptions()
    empty_query = query_pb2.Query()
    expected_request = {
        "project_id": project,
        "partition_id": partition_id,
        "read_options": read_options,
        "query": empty_query,
    }
    set_database_id_to_request(expected_request, database)
    ds_api.run_query.assert_called_once_with(
        request=expected_request,
        **kwargs,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__next_page(database_id):
    _next_page_helper(database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__next_page_w_retry(database_id):
    _next_page_helper(retry=mock.Mock(), database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__next_page_w_timeout(database_id):
    _next_page_helper(timeout=100000, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__next_page_in_transaction(database_id):
    txn_id = b"1xo1md\xe2\x98\x83"
    _next_page_helper(txn_id, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__next_page_w_read_time(database_id):
    read_time = datetime.datetime.utcfromtimestamp(1641058200.123456)
    _next_page_helper(read_time=read_time, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator__next_page_no_more(database_id):
    from google.cloud.datastore.query import Query

    ds_api = _make_datastore_api()
    client = _Client(None, datastore_api=ds_api)
    query = Query(client)
    iterator = _make_iterator(query, client)
    iterator._more_results = False

    page = iterator._next_page()
    assert page is None
    ds_api.run_query.assert_not_called()


@pytest.mark.parametrize("database_id", [None, "somedb"])
@pytest.mark.parametrize("skipped_cursor_1", [b"DEADBEEF", b""])
def test_iterator__next_page_w_skipped_lt_offset(skipped_cursor_1, database_id):
    from google.api_core import page_iterator

    from google.cloud.datastore.query import Query
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2
    from google.cloud.datastore_v1.types import query as query_pb2

    project = "prujekt"
    skipped_1 = 100
    end_cursor_1 = b"DEADBEEF"
    skipped_2 = 50
    end_cursor_2 = b"FACEDACE"

    more_enum = query_pb2.QueryResultBatch.MoreResultsType.NOT_FINISHED

    result_1 = _make_query_response([], b"", more_enum, skipped_1)
    result_1.batch.skipped_cursor = skipped_cursor_1
    result_1.batch.end_cursor = end_cursor_1
    result_2 = _make_query_response([], b"", more_enum, skipped_2)
    result_2.batch.end_cursor = end_cursor_2

    ds_api = _make_datastore_api(result_1, result_2)
    client = _Client(project, datastore_api=ds_api, database=database_id)

    query = Query(client)
    offset = 150
    iterator = _make_iterator(query, client, offset=offset)

    page = iterator._next_page()

    assert isinstance(page, page_iterator.Page)
    assert page._parent is iterator

    partition_id = entity_pb2.PartitionId(project_id=project, database_id=database_id)
    read_options = datastore_pb2.ReadOptions()

    query_1 = query_pb2.Query(offset=offset)
    query_2 = query_pb2.Query(start_cursor=end_cursor_1, offset=(offset - skipped_1))
    expected_calls = []
    for query in [query_1, query_2]:
        expected_request = {
            "project_id": project,
            "partition_id": partition_id,
            "read_options": read_options,
            "query": query,
        }
        set_database_id_to_request(expected_request, database_id)
        expected_calls.append(mock.call(request=expected_request))

    assert ds_api.run_query.call_args_list == expected_calls


@pytest.mark.parametrize("database_id", [None, "somedb"])
@pytest.mark.parametrize("analyze", [True, False])
def test_iterator_sends_explain_options_w_request(database_id, analyze):
    """
    When query has explain_options set, all requests should include
    the explain_options field.
    """
    from google.cloud.datastore.query_profile import ExplainOptions

    response_pb = _make_query_response([], b"", 0, 0)
    ds_api = _make_datastore_api(response_pb)
    client = _Client(None, datastore_api=ds_api)
    explain_options = ExplainOptions(analyze=analyze)
    query = Query(client, explain_options=explain_options)
    iterator = _make_iterator(query, client)
    iterator._next_page()
    # ensure explain_options is set in request
    assert ds_api.run_query.call_count == 1
    found_explain_options = ds_api.run_query.call_args[1]["request"]["explain_options"]
    assert found_explain_options == explain_options._to_dict()
    assert found_explain_options["analyze"] == analyze


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics(database_id):
    """
    If explain_metrics is recieved from backend, it should be set on the iterator
    """
    from google.protobuf import duration_pb2

    from google.cloud.datastore.query_profile import ExplainMetrics
    from google.cloud.datastore_v1.types import query_profile as query_profile_pb2

    expected_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=query_profile_pb2.PlanSummary(),
        execution_stats=query_profile_pb2.ExecutionStats(
            results_returned=100,
            execution_duration=duration_pb2.Duration(seconds=1),
            read_operations=10,
            debug_stats={},
        ),
    )
    response_pb = _make_query_response([], b"", 0, 0)
    response_pb.explain_metrics = expected_metrics
    ds_api = _make_datastore_api(response_pb)
    client = _Client(None, datastore_api=ds_api)
    query = Query(client)
    iterator = _make_iterator(query, client)
    assert iterator._explain_metrics is None
    iterator._next_page()
    assert isinstance(iterator._explain_metrics, ExplainMetrics)
    assert iterator._explain_metrics == ExplainMetrics._from_pb(expected_metrics)
    assert iterator.explain_metrics == ExplainMetrics._from_pb(expected_metrics)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics_no_explain(database_id):
    """
    If query has no explain_options set, iterator.explain_metrics should raise
    an exception.
    """
    from google.cloud.datastore.query_profile import QueryExplainError

    ds_api = _make_datastore_api()
    client = _Client(None, datastore_api=ds_api)
    query = Query(client, explain_options=None)
    iterator = _make_iterator(query, client)
    assert iterator._explain_metrics is None
    with pytest.raises(QueryExplainError) as exc:
        iterator.explain_metrics
    assert "explain_options not set on query" in str(exc.value)
    # should not raise error if field is set
    expected_metrics = object()
    iterator._explain_metrics = expected_metrics
    assert iterator.explain_metrics is expected_metrics


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics_no_analyze_make_call(database_id):
    """
    If query.explain_options(analyze=False), accessing iterator.explain_metrics
    should make a network call to get the data.
    """
    from google.protobuf import duration_pb2

    from google.cloud.datastore.query_profile import ExplainMetrics, ExplainOptions
    from google.cloud.datastore_v1.types import query_profile as query_profile_pb2

    response_pb = _make_query_response([], b"", 0, 0)
    expected_metrics = query_profile_pb2.ExplainMetrics(
        plan_summary=query_profile_pb2.PlanSummary(),
        execution_stats=query_profile_pb2.ExecutionStats(
            results_returned=100,
            execution_duration=duration_pb2.Duration(seconds=1),
            read_operations=10,
            debug_stats={},
        ),
    )
    response_pb.explain_metrics = expected_metrics
    ds_api = _make_datastore_api(response_pb)
    client = _Client(None, datastore_api=ds_api)
    explain_options = ExplainOptions(analyze=False)
    query = Query(client, explain_options=explain_options)
    iterator = _make_iterator(query, client)
    assert ds_api.run_query.call_count == 0
    metrics = iterator.explain_metrics
    # ensure explain_options is set in request
    assert ds_api.run_query.call_count == 1
    assert isinstance(metrics, ExplainMetrics)
    assert metrics == ExplainMetrics._from_pb(expected_metrics)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_metrics_no_analyze_make_call_failed(database_id):
    """
    If query.explain_options(analyze=False), accessing iterator.explain_metrics
    should make a network call to get the data.
    If the call does not result in explain_metrics data, it should raise a QueryExplainError.
    """
    from google.cloud.datastore.query_profile import ExplainOptions, QueryExplainError

    # mocked response does not return explain_metrics
    response_pb = _make_query_response([], b"", 0, 0)
    ds_api = _make_datastore_api(response_pb)
    client = _Client(None, datastore_api=ds_api)
    explain_options = ExplainOptions(analyze=False)
    query = Query(client, explain_options=explain_options)
    iterator = _make_iterator(query, client)
    assert ds_api.run_query.call_count == 0
    with pytest.raises(QueryExplainError):
        iterator.explain_metrics
    assert ds_api.run_query.call_count == 1


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_iterator_explain_analyze_access_before_complete(database_id):
    """
    If query.explain_options(analyze=True), accessing iterator.explain_metrics
    before the query is complete should raise an exception.
    """
    from google.cloud.datastore.query_profile import ExplainOptions, QueryExplainError

    ds_api = _make_datastore_api()
    client = _Client(None, datastore_api=ds_api)
    query = _make_query(client, explain_options=ExplainOptions(analyze=True))
    iterator = _make_iterator(query, client)
    expected_error = "explain_metrics not available until query is complete"
    with pytest.raises(QueryExplainError) as exc:
        iterator.explain_metrics
    assert expected_error in str(exc.value)


def test__item_to_entity():
    from google.cloud.datastore.query import _item_to_entity

    entity_pb = mock.Mock()
    entity_pb._pb = mock.sentinel.entity_pb
    patch = mock.patch("google.cloud.datastore.helpers.entity_from_protobuf")
    with patch as entity_from_protobuf:
        result = _item_to_entity(None, entity_pb)
        assert result is entity_from_protobuf.return_value

    entity_from_protobuf.assert_called_once_with(entity_pb)


def test_pb_from_query_empty():
    from google.cloud.datastore.query import _pb_from_query
    from google.cloud.datastore_v1.types import query as query_pb2

    pb = _pb_from_query(_make_stub_query())
    assert list(pb.projection) == []
    assert list(pb.kind) == []
    assert list(pb.order) == []
    assert list(pb.distinct_on) == []
    assert pb.filter.property_filter.property.name == ""
    cfilter = pb.filter.composite_filter
    assert cfilter.op == query_pb2.CompositeFilter.Operator.OPERATOR_UNSPECIFIED
    assert list(cfilter.filters) == []
    assert pb.start_cursor == b""
    assert pb.end_cursor == b""
    assert pb._pb.limit.value == 0
    assert pb.offset == 0


def test_pb_from_query_projection():
    from google.cloud.datastore.query import _pb_from_query

    pb = _pb_from_query(_make_stub_query(projection=["a", "b", "c"]))
    assert [item.property.name for item in pb.projection] == ["a", "b", "c"]


def test_pb_from_query_kind():
    from google.cloud.datastore.query import _pb_from_query

    pb = _pb_from_query(_make_stub_query(kind="KIND"))
    assert [item.name for item in pb.kind] == ["KIND"]


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_pb_from_query_ancestor(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore.query import _pb_from_query
    from google.cloud.datastore_v1.types import query as query_pb2

    ancestor = Key("Ancestor", 123, project="PROJECT", database=database_id)
    pb = _pb_from_query(_make_stub_query(ancestor=ancestor))
    cfilter = pb.filter.composite_filter
    assert cfilter.op == query_pb2.CompositeFilter.Operator.AND
    assert len(cfilter.filters) == 1
    pfilter = cfilter.filters[0].property_filter
    assert pfilter.property.name == "__key__"
    ancestor_pb = ancestor.to_protobuf()
    assert pfilter.value.key_value == ancestor_pb


def test_pb_from_query_filter():
    from google.cloud.datastore.query import _pb_from_query
    from google.cloud.datastore_v1.types import query as query_pb2

    query = _make_stub_query(filters=[("name", "=", "John")])
    query.OPERATORS = {"=": query_pb2.PropertyFilter.Operator.EQUAL}
    pb = _pb_from_query(query)
    cfilter = pb.filter.composite_filter
    assert cfilter.op == query_pb2.CompositeFilter.Operator.AND
    assert len(cfilter.filters) == 1
    pfilter = cfilter.filters[0].property_filter
    assert pfilter.property.name == "name"
    assert pfilter.value.string_value == "John"


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_pb_from_query_filter_key(database_id):
    from google.cloud.datastore.key import Key
    from google.cloud.datastore.query import _pb_from_query
    from google.cloud.datastore_v1.types import query as query_pb2

    key = Key("Kind", 123, project="PROJECT", database=database_id)
    query = _make_stub_query(filters=[("__key__", "=", key)])
    query.OPERATORS = {"=": query_pb2.PropertyFilter.Operator.EQUAL}
    pb = _pb_from_query(query)
    cfilter = pb.filter.composite_filter
    assert cfilter.op == query_pb2.CompositeFilter.Operator.AND
    assert len(cfilter.filters) == 1
    pfilter = cfilter.filters[0].property_filter
    assert pfilter.property.name == "__key__"
    key_pb = key.to_protobuf()
    assert pfilter.value.key_value == key_pb


def test_pb_from_complex_filter():
    from google.cloud.datastore.query import _pb_from_query
    from google.cloud.datastore_v1.types import query as query_pb2

    query = _make_stub_query(
        filters=[
            ("name", "=", "John"),
            And(
                [
                    PropertyFilter("category", "=", "Grocery"),
                    PropertyFilter("price", ">", "100"),
                ]
            ),
            Or(
                [
                    PropertyFilter("category", "=", "Stationery"),
                    PropertyFilter("price", "<", "50"),
                ]
            ),
            PropertyFilter("name", "=", "Jana"),
        ]
    )
    query.OPERATORS = {"=": query_pb2.PropertyFilter.Operator.EQUAL}
    pb = _pb_from_query(query)
    filter = pb.filter.composite_filter

    assert filter.op == query_pb2.CompositeFilter.Operator.AND
    assert len(filter.filters) == 4

    filter_1 = filter.filters[0].property_filter
    assert filter_1.property.name == "name"
    assert filter_1.value.string_value == "John"
    assert filter_1.op == Query.OPERATORS.get("=")

    filter_2 = filter.filters[1].composite_filter
    assert len(filter_2.filters) == 2
    assert filter_2.op == query_pb2.CompositeFilter.Operator.AND

    filter_2_1 = filter_2.filters[0].property_filter
    assert filter_2_1.property.name == "category"
    assert filter_2_1.op == Query.OPERATORS.get("=")
    assert filter_2_1.value.string_value == "Grocery"

    filter_2_2 = filter_2.filters[1].property_filter
    assert filter_2_2.property.name == "price"
    assert filter_2_2.op == Query.OPERATORS.get(">")
    assert filter_2_2.value.string_value == "100"

    filter_3 = filter.filters[2].composite_filter
    assert len(filter_3.filters) == 2
    assert filter_3.op == query_pb2.CompositeFilter.Operator.OR

    filter_3_1 = filter_3.filters[0].property_filter
    assert filter_3_1.property.name == "category"
    assert filter_3_1.op == Query.OPERATORS.get("=")
    assert filter_3_1.value.string_value == "Stationery"

    filter_3_2 = filter_3.filters[1].property_filter
    assert filter_3_2.property.name == "price"
    assert filter_3_2.op == Query.OPERATORS.get("<")
    assert filter_3_2.value.string_value == "50"

    filter_4 = filter.filters[3].property_filter
    assert filter_4.property.name == "name"
    assert filter_4.value.string_value == "Jana"
    assert filter_4.op == Query.OPERATORS.get("=")


def test_build_pb_for_and():
    and_filter = And(
        [
            ("name", "=", "John"),
            And(
                [
                    PropertyFilter("category", "=", "Grocery"),
                    PropertyFilter("price", ">", "100"),
                ]
            ),
            PropertyFilter("category", "=", "Grocery"),
        ]
    )
    from google.cloud.datastore_v1.types import query as query_pb2

    container_pb = (
        query_pb2.Filter().composite_filter.filters._pb.add().composite_filter
    )
    pb = and_filter.build_pb(container_pb=container_pb)

    assert pb.op == query_pb2.CompositeFilter.Operator.AND
    assert len(pb.filters) == 3


def test_base_composite_filter():
    from google.cloud.datastore_v1.types import query as query_pb2

    comp_filter = BaseCompositeFilter()
    assert len(comp_filter.filters) == 0
    assert (
        comp_filter.operation == query_pb2.CompositeFilter.Operator.OPERATOR_UNSPECIFIED
    )


def test_pb_from_query_order():
    from google.cloud.datastore.query import _pb_from_query
    from google.cloud.datastore_v1.types import query as query_pb2

    pb = _pb_from_query(_make_stub_query(order=["a", "-b", "c"]))
    assert [item.property.name for item in pb.order] == ["a", "b", "c"]
    expected_directions = [
        query_pb2.PropertyOrder.Direction.ASCENDING,
        query_pb2.PropertyOrder.Direction.DESCENDING,
        query_pb2.PropertyOrder.Direction.ASCENDING,
    ]
    assert [item.direction for item in pb.order] == expected_directions


def test_pb_from_query_distinct_on():
    from google.cloud.datastore.query import _pb_from_query

    pb = _pb_from_query(_make_stub_query(distinct_on=["a", "b", "c"]))
    assert [item.name for item in pb.distinct_on] == ["a", "b", "c"]


def _make_stub_query(
    client=object(),
    kind=None,
    project=None,
    namespace=None,
    ancestor=None,
    filters=(),
    projection=(),
    order=(),
    distinct_on=(),
):
    query = Query(
        client,
        kind=kind,
        project=project,
        namespace=namespace,
        ancestor=ancestor,
        filters=filters,
        projection=projection,
        order=order,
        distinct_on=distinct_on,
    )
    return query


class _Client(object):
    def __init__(
        self,
        project,
        datastore_api=None,
        namespace=None,
        transaction=None,
        database=None,
    ):
        self.project = project
        self._datastore_api = datastore_api
        self.database = database
        self.namespace = namespace
        self._transaction = transaction

    @property
    def current_transaction(self):
        return self._transaction


def _make_query(*args, **kw):
    from google.cloud.datastore.query import Query

    return Query(*args, **kw)


def _make_iterator(*args, **kw):
    from google.cloud.datastore.query import Iterator

    return Iterator(*args, **kw)


def _make_client(database=None):
    return _Client(_PROJECT, database=database)


def _make_entity(kind, id_, project, database=None):
    from google.cloud.datastore_v1.types import entity as entity_pb2

    key = entity_pb2.Key()
    key.partition_id.project_id = project
    key.partition_id.database_id = database
    elem = key.path._pb.add()
    elem.kind = kind
    elem.id = id_
    return entity_pb2.Entity(key=key)


def _make_query_response(
    entity_pbs, cursor_as_bytes, more_results_enum, skipped_results
):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import query as query_pb2

    return datastore_pb2.RunQueryResponse(
        batch=query_pb2.QueryResultBatch(
            skipped_results=skipped_results,
            end_cursor=cursor_as_bytes,
            more_results=more_results_enum,
            entity_results=[
                query_pb2.EntityResult(entity=entity) for entity in entity_pbs
            ],
        )
    )


def _make_datastore_api(*results):
    if len(results) == 0:
        run_query = mock.Mock(return_value=None, spec=[])
    else:
        run_query = mock.Mock(side_effect=results, spec=[])

    return mock.Mock(run_query=run_query, spec=["run_query"])
