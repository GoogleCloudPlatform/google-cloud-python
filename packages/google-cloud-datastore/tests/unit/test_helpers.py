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

import pytest


def test__new_value_pb():
    from google.cloud.datastore.helpers import _new_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity_pb = entity_pb2.Entity()
    name = "foo"
    result = _new_value_pb(entity_pb, name)

    assert isinstance(result, type(entity_pb2.Value()._pb))
    assert len(entity_pb._pb.properties) == 1
    assert entity_pb._pb.properties[name] == result


def test_entity_from_protobuf_w_defaults():
    from google.cloud.datastore.helpers import _new_value_pb, entity_from_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID = 1234
    entity_pb = entity_pb2.Entity()
    entity_pb.key.partition_id.project_id = _PROJECT
    entity_pb._pb.key.path.add(kind=_KIND, id=_ID)

    value_pb = _new_value_pb(entity_pb, "foo")
    value_pb.string_value = "Foo"

    unindexed_val_pb = _new_value_pb(entity_pb, "bar")
    unindexed_val_pb.integer_value = 10
    unindexed_val_pb.exclude_from_indexes = True

    array_val_pb1 = _new_value_pb(entity_pb, "baz")
    array_pb1 = array_val_pb1.array_value.values

    unindexed_array_val_pb = array_pb1.add()
    unindexed_array_val_pb.integer_value = 11
    unindexed_array_val_pb.exclude_from_indexes = True

    array_val_pb2 = _new_value_pb(entity_pb, "qux")
    array_pb2 = array_val_pb2.array_value.values

    indexed_array_val_pb = array_pb2.add()
    indexed_array_val_pb.integer_value = 12

    entity = entity_from_protobuf(entity_pb._pb)
    assert entity.kind == _KIND
    assert entity.exclude_from_indexes == frozenset(["bar", "baz"])
    entity_props = dict(entity)
    assert entity_props == {"foo": "Foo", "bar": 10, "baz": [11], "qux": [12]}

    # Also check the key.
    key = entity.key
    assert key.project == _PROJECT
    assert key.namespace is None
    assert key.kind == _KIND
    assert key.id == _ID


def test_entity_from_protobuf_w_mismatched_value_indexed():
    from google.cloud.datastore.helpers import _new_value_pb, entity_from_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID = 1234
    entity_pb = entity_pb2.Entity()
    entity_pb.key.partition_id.project_id = _PROJECT
    entity_pb._pb.key.path.add(kind=_KIND, id=_ID)

    array_val_pb = _new_value_pb(entity_pb, "baz")
    array_pb = array_val_pb.array_value.values

    unindexed_value_pb1 = array_pb.add()
    unindexed_value_pb1.integer_value = 10
    unindexed_value_pb1.exclude_from_indexes = True

    unindexed_value_pb2 = array_pb.add()
    unindexed_value_pb2.integer_value = 11

    with pytest.raises(ValueError):
        entity_from_protobuf(entity_pb._pb)


def test_entity_from_protobuf_w_entity_no_key():
    from google.cloud.datastore.helpers import entity_from_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity_pb = entity_pb2.Entity()
    entity = entity_from_protobuf(entity_pb._pb)

    assert entity.key is None
    assert dict(entity) == {}


def test_entity_from_protobuf_w_pb2_entity_no_key():
    from google.cloud.datastore.helpers import entity_from_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity_pb = entity_pb2.Entity()
    entity = entity_from_protobuf(entity_pb)

    assert entity.key is None
    assert dict(entity) == {}


def test_entity_from_protobuf_w_entity_with_meaning():
    from google.cloud.datastore.helpers import _new_value_pb, entity_from_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity_pb = entity_pb2.Entity()
    name = "hello"
    value_pb = _new_value_pb(entity_pb, name)
    value_pb.meaning = meaning = 9
    value_pb.string_value = val = "something"

    entity = entity_from_protobuf(entity_pb)
    assert entity.key is None
    assert dict(entity) == {name: val}
    assert entity._meanings == {name: (meaning, val)}


def test_entity_from_protobuf_w_nested_entity_no_key():
    from google.cloud.datastore.helpers import _new_value_pb, entity_from_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    PROJECT = "FOO"
    KIND = "KIND"
    INSIDE_NAME = "IFOO"
    OUTSIDE_NAME = "OBAR"
    INSIDE_VALUE = 1337

    entity_inside = entity_pb2.Entity()
    inside_val_pb = _new_value_pb(entity_inside, INSIDE_NAME)
    inside_val_pb.integer_value = INSIDE_VALUE

    entity_pb = entity_pb2.Entity()
    entity_pb.key.partition_id.project_id = PROJECT
    element = entity_pb._pb.key.path.add()
    element.kind = KIND

    outside_val_pb = _new_value_pb(entity_pb, OUTSIDE_NAME)
    outside_val_pb.entity_value.CopyFrom(entity_inside._pb)

    entity = entity_from_protobuf(entity_pb._pb)
    assert entity.key.project == PROJECT
    assert entity.key.flat_path == (KIND,)
    assert len(entity) == 1

    inside_entity = entity[OUTSIDE_NAME]
    assert inside_entity.key is None
    assert len(inside_entity) == 1
    assert inside_entity[INSIDE_NAME] == INSIDE_VALUE


def test_entity_from_protobuf_w_index_mismatch_w_empty_list():
    from google.cloud.datastore.helpers import entity_from_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID = 1234

    array_val_pb = entity_pb2.Value(array_value=entity_pb2.ArrayValue(values=[]))

    entity_pb = entity_pb2.Entity(properties={"baz": array_val_pb})
    entity_pb.key.partition_id.project_id = _PROJECT
    entity_pb.key._pb.path.add(kind=_KIND, id=_ID)

    entity = entity_from_protobuf(entity_pb._pb)
    entity_dict = dict(entity)
    assert entity_dict["baz"] == []


def _compare_entity_proto(entity_pb1, entity_pb2):
    assert entity_pb1.key == entity_pb2.key
    value_list1 = sorted(entity_pb1.properties.items())
    value_list2 = sorted(entity_pb2.properties.items())
    assert len(value_list1) == len(value_list2)
    for pair1, pair2 in zip(value_list1, value_list2):
        name1, val1 = pair1
        name2, val2 = pair2
        assert name1 == name2
        if val1._pb.HasField("entity_value"):  # Message field (Entity)
            assert val1.meaning == val2.meaning
            _compare_entity_proto(val1.entity_value, val2.entity_value)
        else:
            assert val1 == val2


def test_entity_to_protobuf_w_empty():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity = Entity()
    entity_pb = entity_to_protobuf(entity)
    _compare_entity_proto(entity_pb, entity_pb2.Entity())


def test_entity_to_protobuf_w_key_only():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import entity_to_protobuf
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import entity as entity_pb2

    kind, name = "PATH", "NAME"
    project = "PROJECT"
    key = Key(kind, name, project=project)
    entity = Entity(key=key)
    entity_pb = entity_to_protobuf(entity)

    expected_pb = entity_pb2.Entity()
    expected_pb.key.partition_id.project_id = project
    path_elt = expected_pb._pb.key.path.add()
    path_elt.kind = kind
    path_elt.name = name

    _compare_entity_proto(entity_pb, expected_pb)


def test_entity_to_protobuf_w_simple_fields():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _new_value_pb, entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity = Entity()
    name1 = "foo"
    entity[name1] = value1 = 42
    name2 = "bar"
    entity[name2] = value2 = "some-string"
    entity_pb = entity_to_protobuf(entity)

    expected_pb = entity_pb2.Entity()
    val_pb1 = _new_value_pb(expected_pb, name1)
    val_pb1.integer_value = value1
    val_pb2 = _new_value_pb(expected_pb, name2)
    val_pb2.string_value = value2

    _compare_entity_proto(entity_pb, expected_pb)


def test_entity_to_protobuf_w_with_empty_list():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity = Entity()
    entity["foo"] = []
    entity_pb = entity_to_protobuf(entity)

    expected_pb = entity_pb2.Entity()
    prop = expected_pb._pb.properties.get_or_create("foo")
    prop.array_value.CopyFrom(entity_pb2.ArrayValue(values=[])._pb)

    _compare_entity_proto(entity_pb, expected_pb)


def test_entity_to_protobuf_w_inverts_to_protobuf():
    from google.cloud.datastore.helpers import (
        _new_value_pb,
        entity_from_protobuf,
        entity_to_protobuf,
    )
    from google.cloud.datastore_v1.types import entity as entity_pb2

    original_pb = entity_pb2.Entity()
    # Add a key.
    original_pb.key.partition_id.project_id = project = "PROJECT"
    elem1 = original_pb._pb.key.path.add()
    elem1.kind = "Family"
    elem1.id = 1234
    elem2 = original_pb._pb.key.path.add()
    elem2.kind = "King"
    elem2.name = "Spades"

    # Add an integer property.
    val_pb1 = _new_value_pb(original_pb, "foo")
    val_pb1.integer_value = 1337
    val_pb1.exclude_from_indexes = True
    # Add a string property.
    val_pb2 = _new_value_pb(original_pb, "bar")
    val_pb2.string_value = "hello"

    # Add a nested (entity) property.
    val_pb3 = _new_value_pb(original_pb, "entity-baz")
    sub_pb = entity_pb2.Entity()
    sub_val_pb1 = _new_value_pb(sub_pb, "x")
    sub_val_pb1.double_value = 3.14
    sub_val_pb2 = _new_value_pb(sub_pb, "y")
    sub_val_pb2.double_value = 2.718281828
    val_pb3.meaning = 9
    val_pb3.entity_value.CopyFrom(sub_pb._pb)

    # Add a list property.
    val_pb4 = _new_value_pb(original_pb, "list-quux")
    array_val1 = val_pb4.array_value.values.add()
    array_val1.exclude_from_indexes = False
    array_val1.meaning = meaning = 22
    array_val1.blob_value = b"\xe2\x98\x83"
    array_val2 = val_pb4.array_value.values.add()
    array_val2.exclude_from_indexes = False
    array_val2.meaning = meaning
    array_val2.blob_value = b"\xe2\x98\x85"

    # Convert to the user-space Entity.
    entity = entity_from_protobuf(original_pb)
    # Convert the user-space Entity back to a protobuf.
    new_pb = entity_to_protobuf(entity)

    # NOTE: entity_to_protobuf() strips the project so we "cheat".
    new_pb.key.partition_id.project_id = project
    _compare_entity_proto(original_pb, new_pb)


def test_entity_to_protobuf_w_meaning_with_change():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _new_value_pb, entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity = Entity()
    name = "foo"
    entity[name] = value = 42
    entity._meanings[name] = (9, 1337)
    entity_pb = entity_to_protobuf(entity)

    expected_pb = entity_pb2.Entity()
    value_pb = _new_value_pb(expected_pb, name)
    value_pb.integer_value = value
    # NOTE: No meaning is used since the value differs from the
    #       value stored.
    _compare_entity_proto(entity_pb, expected_pb)


def test_entity_to_protobuf_w_variable_meanings():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _new_value_pb, entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity = Entity()
    name = "quux"
    entity[name] = values = [1, 20, 300]
    root_meaning = 31
    sub_meaning = 9
    entity._meanings[name] = ((root_meaning, [None, sub_meaning, None]), values)
    entity_pb = entity_to_protobuf(entity)

    # Construct the expected protobuf.
    expected_pb = entity_pb2.Entity()
    value_pb = _new_value_pb(expected_pb, name)
    value_pb.meaning = root_meaning
    value0 = value_pb.array_value.values.add()
    value0.integer_value = values[0]
    # The only array entry with a meaning is the middle one.
    value1 = value_pb.array_value.values.add()
    value1.integer_value = values[1]
    value1.meaning = sub_meaning
    value2 = value_pb.array_value.values.add()
    value2.integer_value = values[2]

    _compare_entity_proto(entity_pb, expected_pb)


def test_entity_to_protobuf_w_dict_to_entity():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity = Entity()
    entity["a"] = {"b": "c"}
    entity_pb = entity_to_protobuf(entity)

    expected_pb = entity_pb2.Entity(
        properties={
            "a": entity_pb2.Value(
                entity_value=entity_pb2.Entity(
                    properties={"b": entity_pb2.Value(string_value="c")}
                )
            )
        }
    )
    assert entity_pb == expected_pb


def test_entity_to_protobuf_w_dict_to_entity_recursive():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    entity = Entity()
    entity["a"] = {"b": {"c": {"d": 1.25}, "e": True}, "f": 10}
    entity_pb = entity_to_protobuf(entity)

    b_entity_pb = entity_pb2.Entity(
        properties={
            "c": entity_pb2.Value(
                entity_value=entity_pb2.Entity(
                    properties={"d": entity_pb2.Value(double_value=1.25)}
                )
            ),
            "e": entity_pb2.Value(boolean_value=True),
        }
    )
    expected_pb = entity_pb2.Entity(
        properties={
            "a": entity_pb2.Value(
                entity_value=entity_pb2.Entity(
                    properties={
                        "b": entity_pb2.Value(entity_value=b_entity_pb),
                        "f": entity_pb2.Value(integer_value=10),
                    }
                )
            )
        }
    )
    assert entity_pb == expected_pb


def _make_key_pb(project=None, namespace=None, path=(), database=None):
    from google.cloud.datastore_v1.types import entity as entity_pb2

    pb = entity_pb2.Key()
    if project is not None:
        pb.partition_id.project_id = project
    if database is not None:
        pb.partition_id.database_id = database
    if namespace is not None:
        pb.partition_id.namespace_id = namespace
    for elem in path:
        added = pb._pb.path.add()
        added.kind = elem["kind"]
        if "id" in elem:
            added.id = elem["id"]
        if "name" in elem:
            added.name = elem["name"]
    return pb


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_from_protobuf_wo_database_or_namespace_in_pb(database_id):
    from google.cloud.datastore.helpers import key_from_protobuf

    _PROJECT = "PROJECT"
    pb = _make_key_pb(path=[{"kind": "KIND"}], project=_PROJECT, database=database_id)
    key = key_from_protobuf(pb)
    assert key.project == _PROJECT
    assert key.database == database_id
    assert key.namespace is None


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_from_protobuf_w_namespace_in_pb(database_id):
    from google.cloud.datastore.helpers import key_from_protobuf

    _PROJECT = "PROJECT"
    _NAMESPACE = "NAMESPACE"
    pb = _make_key_pb(
        path=[{"kind": "KIND"}],
        namespace=_NAMESPACE,
        project=_PROJECT,
        database=database_id,
    )
    key = key_from_protobuf(pb)
    assert key.project == _PROJECT
    assert key.database == database_id
    assert key.namespace == _NAMESPACE


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_from_protobuf_w_nested_path_in_pb(database_id):
    from google.cloud.datastore.helpers import key_from_protobuf

    _PATH = [
        {"kind": "PARENT", "name": "NAME"},
        {"kind": "CHILD", "id": 1234},
        {"kind": "GRANDCHILD", "id": 5678},
    ]
    pb = _make_key_pb(path=_PATH, project="PROJECT", database=database_id)
    key = key_from_protobuf(pb)
    assert key.path == _PATH
    assert key.database == database_id


def test_w_nothing_in_pb():
    from google.cloud.datastore.helpers import key_from_protobuf

    pb = _make_key_pb()
    with pytest.raises(ValueError):
        key_from_protobuf(pb)


def test__get_read_options_w_eventual_w_txn_wo_read_time():
    from google.cloud.datastore.helpers import get_read_options

    with pytest.raises(ValueError):
        get_read_options(True, b"123", None)


def test__get_read_options_w_eventual_wo_txn_wo_read_time():
    from google.cloud.datastore.helpers import get_read_options
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    read_options = get_read_options(True, None, None)
    expected = datastore_pb2.ReadOptions(
        read_consistency=datastore_pb2.ReadOptions.ReadConsistency.EVENTUAL
    )
    assert read_options == expected


def test__get_read_options_w_evntual_w_txn_w_read_time():
    from datetime import datetime

    from google.cloud.datastore.helpers import get_read_options

    with pytest.raises(ValueError):
        get_read_options(True, b"123", datetime(2022, 1, 1, 17, 30, 0, 123456))


def test__get_read_options_w_evntual_wo_txn_w_read_time():
    from datetime import datetime

    from google.cloud.datastore.helpers import get_read_options

    with pytest.raises(ValueError):
        get_read_options(True, None, datetime(2022, 1, 1, 17, 30, 0, 123456))


def test__get_read_options_w_default_w_txn_wo_read_time():
    from google.cloud.datastore.helpers import get_read_options
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    txn_id = b"123abc-easy-as"
    read_options = get_read_options(False, txn_id, None)
    expected = datastore_pb2.ReadOptions(transaction=txn_id)
    assert read_options == expected


def test__get_read_options_w_default_wo_txn_wo_read_time():
    from google.cloud.datastore.helpers import get_read_options
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    read_options = get_read_options(False, None, None)
    expected = datastore_pb2.ReadOptions()
    assert read_options == expected


def test__get_read_options_w_default_w_txn_w_read_time():
    from datetime import datetime

    from google.cloud.datastore.helpers import get_read_options

    with pytest.raises(ValueError):
        get_read_options(False, b"123", datetime(2022, 1, 1, 17, 30, 0, 123456))


def test__get_read_options_w_default_wo_txn_w_read_time():
    from datetime import datetime

    from google.protobuf.timestamp_pb2 import Timestamp

    from google.cloud.datastore.helpers import get_read_options
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    read_time = datetime.utcfromtimestamp(1641058200.123456)
    read_time_pb = Timestamp(seconds=1641058200, nanos=123456000)
    read_options = get_read_options(False, None, read_time)
    expected = datastore_pb2.ReadOptions(read_time=read_time_pb)
    assert read_options == expected


def test__get_read_options_w_new_transaction():
    from google.cloud.datastore.helpers import get_read_options
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    input_options = datastore_pb2.TransactionOptions()
    read_options = get_read_options(False, None, new_transaction_options=input_options)
    expected = datastore_pb2.ReadOptions(new_transaction=input_options)
    assert read_options == expected


@pytest.mark.parametrize(
    "args",
    [
        (True, "id"),
        (True, "id", None),
        (True, None, "read_time"),
        (True, None, None, "new"),
        (False, "id", "read_time"),
        (False, "id", None, "new"),
        (False, None, "read_time", "new"),
    ],
)
def test__get_read_options_w_multiple_args(args):
    """
    arguments are mutually exclusive.
    Should raise ValueError if multiple are set
    """
    from google.cloud.datastore.helpers import get_read_options

    with pytest.raises(ValueError):
        get_read_options(*args)


def test__get_transaction_options_none():
    """
    test with empty transaction input
    """
    from google.cloud.datastore.helpers import get_transaction_options

    t_id, new_t = get_transaction_options(None)
    assert t_id is None
    assert new_t is None


def test__get_transaction_options_w_id():
    """
    test with transaction with id set
    """
    from google.cloud.datastore import Transaction
    from google.cloud.datastore.helpers import get_transaction_options

    expected_id = b"123abc"
    txn = Transaction(None, begin_later=True)
    txn._id = expected_id
    t_id, new_t = get_transaction_options(txn)
    assert t_id == expected_id
    assert new_t is None


def test__get_transaction_options_w_begin_later():
    """
    if begin later is set and it hasn't begun, should return new_transaction_options
    """
    from google.cloud.datastore import Transaction
    from google.cloud.datastore.helpers import get_transaction_options

    txn = Transaction(None, begin_later=True)
    t_id, new_t = get_transaction_options(txn)
    assert t_id is None
    assert new_t is txn._options


def test__get_transaction_options_not_started():
    """
    If the transaction is noet set as begin_later, but it hasn't begun, return None for both
    """
    from google.cloud.datastore import Transaction
    from google.cloud.datastore.helpers import get_transaction_options

    txn = Transaction(None, begin_later=False)
    t_id, new_t = get_transaction_options(txn)
    assert t_id is None
    assert new_t is None


def test__pb_attr_value_w_datetime_naive():
    import calendar
    import datetime

    from google.cloud._helpers import UTC

    from google.cloud.datastore.helpers import _pb_attr_value

    micros = 4375
    naive = datetime.datetime(2014, 9, 16, 10, 19, 32, micros)  # No zone.
    utc = datetime.datetime(2014, 9, 16, 10, 19, 32, micros, UTC)
    name, value = _pb_attr_value(naive)
    assert name == "timestamp_value"
    assert value.seconds == calendar.timegm(utc.timetuple())
    assert value.nanos == 1000 * micros


def test__pb_attr_value_w_datetime_w_zone():
    import calendar
    import datetime

    from google.cloud._helpers import UTC

    from google.cloud.datastore.helpers import _pb_attr_value

    micros = 4375
    utc = datetime.datetime(2014, 9, 16, 10, 19, 32, micros, UTC)
    name, value = _pb_attr_value(utc)
    assert name == "timestamp_value"
    assert value.seconds == calendar.timegm(utc.timetuple())
    assert value.nanos == 1000 * micros


def test__pb_attr_value_w_key():
    from google.cloud.datastore.helpers import _pb_attr_value
    from google.cloud.datastore.key import Key

    key = Key("PATH", 1234, project="PROJECT")
    name, value = _pb_attr_value(key)
    assert name == "key_value"
    assert value == key.to_protobuf()


def test__pb_attr_value_w_bool():
    from google.cloud.datastore.helpers import _pb_attr_value

    name, value = _pb_attr_value(False)
    assert name == "boolean_value"
    assert not value


def test__pb_attr_value_w_float():
    from google.cloud.datastore.helpers import _pb_attr_value

    name, value = _pb_attr_value(3.1415926)
    assert name == "double_value"
    assert value == 3.1415926


def test__pb_attr_value_w_int():
    from google.cloud.datastore.helpers import _pb_attr_value

    name, value = _pb_attr_value(42)
    assert name == "integer_value"
    assert value == 42


def test__pb_attr_value_w_long():
    from google.cloud.datastore.helpers import _pb_attr_value

    must_be_long = (1 << 63) - 1
    name, value = _pb_attr_value(must_be_long)
    assert name == "integer_value"
    assert value == must_be_long


def test__pb_attr_value_w_native_str():
    from google.cloud.datastore.helpers import _pb_attr_value

    name, value = _pb_attr_value("str")

    assert name == "string_value"
    assert value == "str"


def test__pb_attr_value_w_bytes():
    from google.cloud.datastore.helpers import _pb_attr_value

    name, value = _pb_attr_value(b"bytes")
    assert name == "blob_value"
    assert value == b"bytes"


def test__pb_attr_value_w_unicode():
    from google.cloud.datastore.helpers import _pb_attr_value

    name, value = _pb_attr_value("str")
    assert name == "string_value"
    assert value == "str"


def test__pb_attr_value_w_entity():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _pb_attr_value

    entity = Entity()
    name, value = _pb_attr_value(entity)
    assert name == "entity_value"
    assert value is entity


def test__pb_attr_value_w_dict():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _pb_attr_value

    orig_value = {"richard": b"feynman"}
    name, value = _pb_attr_value(orig_value)
    assert name == "entity_value"
    assert isinstance(value, Entity)
    assert value.key is None
    assert value._meanings == {}
    assert value.exclude_from_indexes == set()
    assert dict(value) == orig_value


def test__pb_attr_value_w_array():
    from google.cloud.datastore.helpers import _pb_attr_value

    values = ["a", 0, 3.14]
    name, value = _pb_attr_value(values)
    assert name == "array_value"
    assert value is values


def test__pb_attr_value_w_geo_point():
    from google.type import latlng_pb2

    from google.cloud.datastore.helpers import GeoPoint, _pb_attr_value

    lat = 42.42
    lng = 99.0007
    geo_pt = GeoPoint(latitude=lat, longitude=lng)
    geo_pt_pb = latlng_pb2.LatLng(latitude=lat, longitude=lng)
    name, value = _pb_attr_value(geo_pt)
    assert name == "geo_point_value"
    assert value == geo_pt_pb


def test__pb_attr_value_w_null():
    from google.protobuf import struct_pb2

    from google.cloud.datastore.helpers import _pb_attr_value

    name, value = _pb_attr_value(None)
    assert name == "null_value"
    assert value == struct_pb2.NULL_VALUE


def test__pb_attr_value_w_object():
    from google.cloud.datastore.helpers import _pb_attr_value

    with pytest.raises(ValueError):
        _pb_attr_value(object())


def _make_value_pb(attr_name, attr_value):
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value = entity_pb2.Value()
    setattr(value._pb, attr_name, attr_value)
    return value


def test__get_value_from_value_pb_w_datetime():
    import calendar
    import datetime

    from google.cloud._helpers import UTC

    from google.cloud.datastore.helpers import _get_value_from_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    micros = 4375
    utc = datetime.datetime(2014, 9, 16, 10, 19, 32, micros, UTC)
    value = entity_pb2.Value()
    value._pb.timestamp_value.seconds = calendar.timegm(utc.timetuple())
    value._pb.timestamp_value.nanos = 1000 * micros
    assert _get_value_from_value_pb(value._pb) == utc


def test__get_value_from_value_pb_w_key():
    from google.cloud.datastore.helpers import _get_value_from_value_pb
    from google.cloud.datastore.key import Key
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value = entity_pb2.Value()
    expected = Key("KIND", 1234, project="PROJECT").to_protobuf()
    value.key_value._pb.CopyFrom(expected._pb)
    found = _get_value_from_value_pb(value._pb)
    assert found.to_protobuf() == expected


def test__get_value_from_value_pb_w_bool():
    from google.cloud.datastore.helpers import _get_value_from_value_pb

    value = _make_value_pb("boolean_value", False)
    assert not _get_value_from_value_pb(value._pb)


def test__get_value_from_value_pb_w_float():
    from google.cloud.datastore.helpers import _get_value_from_value_pb

    value = _make_value_pb("double_value", 3.1415926)
    assert _get_value_from_value_pb(value._pb) == 3.1415926


def test__get_value_from_value_pb_w_int():
    from google.cloud.datastore.helpers import _get_value_from_value_pb

    value = _make_value_pb("integer_value", 42)
    assert _get_value_from_value_pb(value._pb) == 42


def test__get_value_from_value_pb_w_bytes():
    from google.cloud.datastore.helpers import _get_value_from_value_pb

    value = _make_value_pb("blob_value", b"str")
    assert _get_value_from_value_pb(value._pb) == b"str"


def test__get_value_from_value_pb_w_unicode():
    from google.cloud.datastore.helpers import _get_value_from_value_pb

    value = _make_value_pb("string_value", "str")
    assert _get_value_from_value_pb(value._pb) == "str"


def test__get_value_from_value_pb_w_entity():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _get_value_from_value_pb, _new_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value = entity_pb2.Value()
    entity_pb = value.entity_value
    entity_pb._pb.key.path.add(kind="KIND")
    entity_pb.key.partition_id.project_id = "PROJECT"

    value_pb = _new_value_pb(entity_pb, "foo")
    value_pb.string_value = "Foo"
    entity = _get_value_from_value_pb(value._pb)
    assert isinstance(entity, Entity)
    assert entity["foo"] == "Foo"


def test__get_value_from_value_pb_w_array():
    from google.cloud.datastore.helpers import _get_value_from_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value = entity_pb2.Value()
    array_pb = value.array_value.values
    item_pb = array_pb._pb.add()
    item_pb.string_value = "Foo"
    item_pb = array_pb._pb.add()
    item_pb.string_value = "Bar"
    items = _get_value_from_value_pb(value._pb)
    assert items == ["Foo", "Bar"]


def test__get_value_from_value_pb_w_geo_point():
    from google.type import latlng_pb2

    from google.cloud.datastore.helpers import GeoPoint, _get_value_from_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    lat = -3.14
    lng = 13.37
    geo_pt_pb = latlng_pb2.LatLng(latitude=lat, longitude=lng)
    value = entity_pb2.Value(geo_point_value=geo_pt_pb)
    result = _get_value_from_value_pb(value._pb)
    assert isinstance(result, GeoPoint)
    assert result.latitude == lat
    assert result.longitude == lng


def test__get_value_from_value_pb_w_null():
    from google.protobuf import struct_pb2

    from google.cloud.datastore.helpers import _get_value_from_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value = entity_pb2.Value(null_value=struct_pb2.NULL_VALUE)
    result = _get_value_from_value_pb(value._pb)
    assert result is None


def test__get_value_from_value_pb_w_unknown():
    from google.cloud.datastore.helpers import _get_value_from_value_pb
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value = entity_pb2.Value()
    with pytest.raises(ValueError):
        _get_value_from_value_pb(value._pb)


def _make_empty_value_pb():
    from google.cloud.datastore_v1.types import entity as entity_pb2

    return entity_pb2.Value()._pb


def test__set_protobuf_value_w_datetime():
    import calendar
    import datetime

    from google.cloud._helpers import UTC

    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    micros = 4375
    utc = datetime.datetime(2014, 9, 16, 10, 19, 32, micros, UTC)
    _set_protobuf_value(pb, utc)
    value = pb.timestamp_value
    assert value.seconds == calendar.timegm(utc.timetuple())
    assert value.nanos == 1000 * micros


def test__set_protobuf_value_w_key():
    from google.cloud.datastore.helpers import _set_protobuf_value
    from google.cloud.datastore.key import Key

    pb = _make_empty_value_pb()
    key = Key("KIND", 1234, project="PROJECT")
    _set_protobuf_value(pb, key)
    value = pb.key_value
    assert value == key.to_protobuf()._pb


def test__set_protobuf_value_w_none():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    _set_protobuf_value(pb, None)
    assert pb.WhichOneof("value_type") == "null_value"


def test__set_protobuf_value_w_bool():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    _set_protobuf_value(pb, False)
    value = pb.boolean_value
    assert not value


def test__set_protobuf_value_w_float():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    _set_protobuf_value(pb, 3.1415926)
    value = pb.double_value
    assert value == 3.1415926


def test__set_protobuf_value_w_int():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    _set_protobuf_value(pb, 42)
    value = pb.integer_value
    assert value == 42


def test__set_protobuf_value_w_long():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    must_be_long = (1 << 63) - 1
    _set_protobuf_value(pb, must_be_long)
    value = pb.integer_value
    assert value == must_be_long


def test__set_protobuf_value_w_native_str():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    _set_protobuf_value(pb, "str")

    value = pb.string_value
    assert value == "str"


def test__set_protobuf_value_w_bytes():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    _set_protobuf_value(pb, b"str")
    value = pb.blob_value
    assert value == b"str"


def test__set_protobuf_value_w_unicode():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    _set_protobuf_value(pb, "str")
    value = pb.string_value
    assert value == "str"


def test__set_protobuf_value_w_entity_empty_wo_key():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    entity = Entity()
    _set_protobuf_value(pb, entity)
    value = pb.entity_value
    assert value.key.SerializeToString() == b""
    assert len(list(value.properties.items())) == 0


def test__set_protobuf_value_w_entity_w_key():
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _set_protobuf_value
    from google.cloud.datastore.key import Key

    name = "foo"
    value = "Foo"
    pb = _make_empty_value_pb()
    key = Key("KIND", 123, project="PROJECT")
    entity = Entity(key=key)
    entity[name] = value
    _set_protobuf_value(pb, entity)
    entity_pb = pb.entity_value
    assert entity_pb.key == key.to_protobuf()._pb

    prop_dict = dict(entity_pb.properties.items())
    assert len(prop_dict) == 1
    assert list(prop_dict.keys()) == [name]
    assert prop_dict[name].string_value == value


def test__set_protobuf_value_w_array():
    from google.cloud.datastore.helpers import _set_protobuf_value

    pb = _make_empty_value_pb()
    values = ["a", 0, 3.14]
    _set_protobuf_value(pb, values)
    marshalled = pb.array_value.values
    assert len(marshalled) == len(values)
    assert marshalled[0].string_value == values[0]
    assert marshalled[1].integer_value == values[1]
    assert marshalled[2].double_value == values[2]


def test__set_protobuf_value_w_geo_point():
    from google.type import latlng_pb2

    from google.cloud.datastore.helpers import GeoPoint, _set_protobuf_value

    pb = _make_empty_value_pb()
    lat = 9.11
    lng = 3.337
    geo_pt = GeoPoint(latitude=lat, longitude=lng)
    geo_pt_pb = latlng_pb2.LatLng(latitude=lat, longitude=lng)
    _set_protobuf_value(pb, geo_pt)
    assert pb.geo_point_value == geo_pt_pb


def test__get_meaning_w_no_meaning():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    result = _get_meaning(value_pb)
    assert result is None


def test__get_meaning_w_single():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    value_pb.meaning = meaning = 22
    value_pb.string_value = "hi"
    result = _get_meaning(value_pb)
    assert meaning == result


def test__get_meaning_w_empty_array_value():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    value_pb._pb.array_value.values.add()
    value_pb._pb.array_value.values.pop()

    result = _get_meaning(value_pb, is_list=True)
    assert result is None


def test__get_meaning_w_array_value():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    meaning = 9
    sub_value_pb1 = value_pb._pb.array_value.values.add()
    sub_value_pb2 = value_pb._pb.array_value.values.add()

    sub_value_pb1.meaning = sub_value_pb2.meaning = meaning
    sub_value_pb1.string_value = "hi"
    sub_value_pb2.string_value = "bye"

    result = _get_meaning(value_pb, is_list=True)
    # should preserve sub-value meanings as list
    assert (None, [meaning, meaning]) == result


def test__get_meaning_w_array_value_root_meaning():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    meaning = 9
    value_pb.meaning = meaning
    sub_value_pb1 = value_pb._pb.array_value.values.add()
    sub_value_pb2 = value_pb._pb.array_value.values.add()

    sub_value_pb1.string_value = "hi"
    sub_value_pb2.string_value = "bye"

    result = _get_meaning(value_pb, is_list=True)
    # should preserve sub-value meanings as list
    assert (meaning, None) == result


def test__get_meaning_w_array_value_root_and_sub_meanings():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    root_meaning = 9
    sub_meaning = 3
    value_pb.meaning = root_meaning
    sub_value_pb1 = value_pb._pb.array_value.values.add()
    sub_value_pb2 = value_pb._pb.array_value.values.add()

    sub_value_pb1.meaning = sub_value_pb2.meaning = sub_meaning
    sub_value_pb1.string_value = "hi"
    sub_value_pb2.string_value = "bye"

    result = _get_meaning(value_pb, is_list=True)
    # should preserve sub-value meanings as list
    assert (root_meaning, [sub_meaning, sub_meaning]) == result


def test__get_meaning_w_array_value_multiple_meanings():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    meaning1 = 9
    meaning2 = 10
    sub_value_pb1 = value_pb._pb.array_value.values.add()
    sub_value_pb2 = value_pb._pb.array_value.values.add()

    sub_value_pb1.meaning = meaning1
    sub_value_pb2.meaning = meaning2
    sub_value_pb1.string_value = "hi"
    sub_value_pb2.string_value = "bye"

    result = _get_meaning(value_pb, is_list=True)
    assert result == (None, [meaning1, meaning2])


def test__get_meaning_w_array_value_meaning_partially_unset():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    meaning1 = 9
    sub_value_pb1 = value_pb._pb.array_value.values.add()
    sub_value_pb2 = value_pb._pb.array_value.values.add()

    sub_value_pb1.meaning = meaning1
    sub_value_pb1.string_value = "hi"
    sub_value_pb2.string_value = "bye"

    result = _get_meaning(value_pb, is_list=True)
    assert result == (None, [meaning1, None])


def test__get_meaning_w_array_value_meaning_fully_unset():
    from google.cloud.datastore.helpers import _get_meaning
    from google.cloud.datastore_v1.types import entity as entity_pb2

    value_pb = entity_pb2.Value()
    sub_value_pb1 = value_pb._pb.array_value.values.add()
    sub_value_pb2 = value_pb._pb.array_value.values.add()

    sub_value_pb1.string_value = "hi"
    sub_value_pb2.string_value = "bye"

    result = _get_meaning(value_pb, is_list=True)
    assert result is None


@pytest.mark.parametrize("orig_root_meaning", [0, 1])
@pytest.mark.parametrize("orig_sub_meaning", [0, 1])
def test__set_pb_meaning_w_array_value_fully_unset(orig_root_meaning, orig_sub_meaning):
    """
    call _set_pb_meaning_from_entity with meaning=None data.
    Should not touch proto's meaning field
    """
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _set_pb_meaning_from_entity
    from google.cloud.datastore_v1.types import entity as entity_pb2

    orig_pb = entity_pb2.Entity()
    value_pb = orig_pb._pb.properties.get_or_create("value")
    value_pb.meaning = orig_root_meaning
    sub_value_pb1 = value_pb.array_value.values.add()
    sub_value_pb1.meaning = orig_sub_meaning

    entity = Entity(key="key")
    entity._meanings = {"value": ((None, None), None)}
    _set_pb_meaning_from_entity(entity, "value", None, value_pb, is_list=True)
    assert value_pb.meaning == orig_root_meaning
    assert value_pb.array_value.values[0].meaning == orig_sub_meaning


@pytest.mark.parametrize("orig_meaning", [0, 1])
def test__set_pb_meaning_w_value_unset(orig_meaning):
    """
    call _set_pb_meaning_from_entity with meaning=None data.
    Should not touch proto's meaning field
    """
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _set_pb_meaning_from_entity
    from google.cloud.datastore_v1.types import entity as entity_pb2

    orig_pb = entity_pb2.Entity()
    value_pb = orig_pb._pb.properties.get_or_create("value")
    value_pb.meaning = orig_meaning

    entity = Entity(key="key")
    entity._meanings = {"value": (None, None)}
    _set_pb_meaning_from_entity(entity, "value", None, value_pb, is_list=False)
    assert value_pb.meaning == orig_meaning


def test__set_pb_meaning_w_list_and_single_value():
    """
    v2.20.2 uses a tuple to represent list meanings (https://github.com/googleapis/python-datastore/pull/575)

    This check ensures _set_pb_meaning_from_entity is backwards
    compatible with the old meaning style, still used by python-ndb
    """
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _set_pb_meaning_from_entity
    from google.cloud.datastore_v1.types import entity as entity_pb2

    orig_root_meaning = 1
    updated_meaning = 22
    orig_pb = entity_pb2.Entity()
    value_pb = orig_pb._pb.properties.get_or_create("value")
    value_pb.meaning = orig_root_meaning
    sub_value_pb1 = value_pb.array_value.values.add()
    sub_value_pb2 = value_pb.array_value.values.add()

    entity = Entity(key="key")
    entity._meanings = {"value": (updated_meaning, None)}
    _set_pb_meaning_from_entity(entity, "value", None, value_pb, is_list=True)
    assert value_pb.meaning == orig_root_meaning
    assert sub_value_pb1.meaning == updated_meaning
    assert sub_value_pb2.meaning == updated_meaning


def test__set_pb_meaning_w_list_and_list():
    """
    v2.20.2 uses a tuple to represent list meanings (https://github.com/googleapis/python-datastore/pull/575)

    This check ensures _set_pb_meaning_from_entity is backwards
    compatible with the old meaning style, still used by python-ndb
    """
    from google.cloud.datastore.entity import Entity
    from google.cloud.datastore.helpers import _set_pb_meaning_from_entity
    from google.cloud.datastore_v1.types import entity as entity_pb2

    orig_root_meaning = 1
    updated_meaning_1 = 12
    updated_meaning_2 = 4
    orig_pb = entity_pb2.Entity()
    value_pb = orig_pb._pb.properties.get_or_create("value")
    value_pb.meaning = orig_root_meaning
    sub_value_pb1 = value_pb.array_value.values.add()
    sub_value_pb2 = value_pb.array_value.values.add()

    entity = Entity(key="key")
    entity._meanings = {"value": ([updated_meaning_1, updated_meaning_2], None)}
    _set_pb_meaning_from_entity(entity, "value", None, value_pb, is_list=True)
    assert value_pb.meaning == orig_root_meaning
    assert sub_value_pb1.meaning == updated_meaning_1
    assert sub_value_pb2.meaning == updated_meaning_2


def test__array_w_meaning_end_to_end():
    """
    Test proto->entity->proto with an array with a meaning field
    """
    from google.cloud.datastore.helpers import entity_from_protobuf, entity_to_protobuf
    from google.cloud.datastore_v1.types import entity as entity_pb2

    orig_pb = entity_pb2.Entity()
    value_pb = orig_pb._pb.properties.get_or_create("value")
    value_pb.meaning = 31
    sub_value_pb1 = value_pb.array_value.values.add()
    sub_value_pb1.double_value = 1
    sub_value_pb1.meaning = 1
    sub_value_pb2 = value_pb.array_value.values.add()
    sub_value_pb2.double_value = 2
    sub_value_pb3 = value_pb.array_value.values.add()
    sub_value_pb3.double_value = 3
    sub_value_pb3.meaning = 3
    # convert to entity
    entity = entity_from_protobuf(orig_pb._pb)
    assert entity._meanings["value"][0] == (31, [1, None, 3])
    assert entity._meanings["value"][1] == [1, 2, 3]
    # convert back to pb
    output_entity_pb = entity_to_protobuf(entity)
    final_pb = output_entity_pb._pb.properties["value"]
    assert final_pb.meaning == 31
    assert len(final_pb.array_value.values) == 3
    assert final_pb.array_value.values[0].meaning == 1
    assert final_pb.array_value.values[0].double_value == 1
    assert final_pb.array_value.values[1].meaning == 0
    assert final_pb.array_value.values[1].double_value == 2
    assert final_pb.array_value.values[2].meaning == 3
    assert final_pb.array_value.values[2].double_value == 3


def _make_geopoint(*args, **kwargs):
    from google.cloud.datastore.helpers import GeoPoint

    return GeoPoint(*args, **kwargs)


def test_geopoint_ctor():
    lat = 81.2
    lng = 359.9999
    geo_pt = _make_geopoint(lat, lng)
    assert geo_pt.latitude == lat
    assert geo_pt.longitude == lng


def test_geopoint_to_protobuf():
    from google.type import latlng_pb2

    lat = 0.0001
    lng = 20.03
    geo_pt = _make_geopoint(lat, lng)
    result = geo_pt.to_protobuf()
    geo_pt_pb = latlng_pb2.LatLng(latitude=lat, longitude=lng)
    assert result == geo_pt_pb


def test_geopoint___eq__():
    lat = 0.0001
    lng = 20.03
    geo_pt1 = _make_geopoint(lat, lng)
    geo_pt2 = _make_geopoint(lat, lng)
    assert geo_pt1 == geo_pt2


def test_geopoint___eq__type_differ():
    lat = 0.0001
    lng = 20.03
    geo_pt1 = _make_geopoint(lat, lng)
    geo_pt2 = object()
    assert geo_pt1 != geo_pt2


def test_geopoint___ne__same_value():
    lat = 0.0001
    lng = 20.03
    geo_pt1 = _make_geopoint(lat, lng)
    geo_pt2 = _make_geopoint(lat, lng)
    assert not geo_pt1 != geo_pt2


def test_geopoint___ne__():
    geo_pt1 = _make_geopoint(0.0, 1.0)
    geo_pt2 = _make_geopoint(2.0, 3.0)
    assert geo_pt1 != geo_pt2
