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

import datetime
import pickle
import types
import zlib
from unittest import mock

import pytest
import pytz
from google.cloud.datastore import entity as entity_module
from google.cloud.datastore import helpers
from google.cloud.datastore import key as ds_key_module
from google.cloud.datastore_v1 import types as ds_types
from google.cloud.datastore_v1.types import entity as entity_pb2

from google.cloud import datastore
from google.cloud.ndb import (
    _datastore_types,
    _legacy_entity_pb,
    _options,
    exceptions,
    model,
    polymodel,
    tasklets,
)
from google.cloud.ndb import key as key_module
from google.cloud.ndb import query as query_module
from google.cloud.ndb import utils as ndb_utils

from . import utils


class timezone(datetime.tzinfo):
    def __init__(self, offset):
        self.offset = datetime.timedelta(hours=offset)

    def utcoffset(self, dt):
        return self.offset

    def dst(self, dt):
        return datetime.timedelta(0)

    def __eq__(self, other):
        return self.offset == other.offset


def test___all__():
    utils.verify___all__(model)


def test_Key():
    assert model.Key is key_module.Key


def test_BlobKey():
    assert model.BlobKey is _datastore_types.BlobKey


def test_GeoPt():
    assert model.GeoPt is helpers.GeoPoint


class TestIndexProperty:
    @staticmethod
    def test_constructor():
        index_prop = model.IndexProperty(name="a", direction="asc")
        assert index_prop._name == "a"
        assert index_prop._direction == "asc"

    @staticmethod
    def test_name():
        index_prop = model.IndexProperty(name="b", direction="asc")
        assert index_prop.name == "b"

    @staticmethod
    def test_direction():
        index_prop = model.IndexProperty(name="a", direction="desc")
        assert index_prop.direction == "desc"

    @staticmethod
    def test___repr__():
        index_prop = model.IndexProperty(name="c", direction="asc")
        assert repr(index_prop) == "IndexProperty(name='c', direction='asc')"

    @staticmethod
    def test___eq__():
        index_prop1 = model.IndexProperty(name="d", direction="asc")
        index_prop2 = model.IndexProperty(name="d", direction="desc")
        index_prop3 = mock.sentinel.index_prop
        assert index_prop1 == index_prop1
        assert not index_prop1 == index_prop2
        assert not index_prop1 == index_prop3

    @staticmethod
    def test___ne__():
        index_prop1 = model.IndexProperty(name="d", direction="asc")
        index_prop2 = model.IndexProperty(name="d", direction="desc")
        index_prop3 = mock.sentinel.index_prop
        index_prop4 = model.IndexProperty(name="d", direction="asc")
        assert not index_prop1 != index_prop1
        assert index_prop1 != index_prop2
        assert index_prop1 != index_prop3
        assert not index_prop1 != index_prop4

    @staticmethod
    def test___hash__():
        index_prop1 = model.IndexProperty(name="zip", direction="asc")
        index_prop2 = model.IndexProperty(name="zip", direction="asc")
        assert index_prop1 is not index_prop2
        assert hash(index_prop1) == hash(index_prop2)
        assert hash(index_prop1) == hash(("zip", "asc"))


class TestIndex:
    @staticmethod
    def test_constructor():
        index_prop = model.IndexProperty(name="a", direction="asc")
        index = model.Index(kind="IndK", properties=(index_prop,), ancestor=False)
        assert index._kind == "IndK"
        assert index._properties == (index_prop,)
        assert not index._ancestor

    @staticmethod
    def test_kind():
        index = model.Index(kind="OK", properties=(), ancestor=False)
        assert index.kind == "OK"

    @staticmethod
    def test_properties():
        index_prop1 = model.IndexProperty(name="a", direction="asc")
        index_prop2 = model.IndexProperty(name="b", direction="desc")
        index = model.Index(
            kind="F", properties=(index_prop1, index_prop2), ancestor=False
        )
        assert index.properties == (index_prop1, index_prop2)

    @staticmethod
    def test_ancestor():
        index = model.Index(kind="LK", properties=(), ancestor=True)
        assert index.ancestor

    @staticmethod
    def test___repr__():
        index_prop = model.IndexProperty(name="a", direction="asc")
        index = model.Index(kind="IndK", properties=[index_prop], ancestor=False)
        expected = "Index(kind='IndK', properties=[{!r}], ancestor=False)"
        expected = expected.format(index_prop)
        assert repr(index) == expected

    @staticmethod
    def test___eq__():
        index_props = (model.IndexProperty(name="a", direction="asc"),)
        index1 = model.Index(kind="d", properties=index_props, ancestor=False)
        index2 = model.Index(kind="d", properties=(), ancestor=False)
        index3 = model.Index(kind="d", properties=index_props, ancestor=True)
        index4 = model.Index(kind="e", properties=index_props, ancestor=False)
        index5 = mock.sentinel.index
        assert index1 == index1
        assert not index1 == index2
        assert not index1 == index3
        assert not index1 == index4
        assert not index1 == index5

    @staticmethod
    def test___ne__():
        index_props = (model.IndexProperty(name="a", direction="asc"),)
        index1 = model.Index(kind="d", properties=index_props, ancestor=False)
        index2 = model.Index(kind="d", properties=(), ancestor=False)
        index3 = model.Index(kind="d", properties=index_props, ancestor=True)
        index4 = model.Index(kind="e", properties=index_props, ancestor=False)
        index5 = mock.sentinel.index
        index6 = model.Index(kind="d", properties=index_props, ancestor=False)
        assert not index1 != index1
        assert index1 != index2
        assert index1 != index3
        assert index1 != index4
        assert index1 != index5
        assert not index1 != index6

    @staticmethod
    def test___hash__():
        index_props = (model.IndexProperty(name="a", direction="asc"),)
        index1 = model.Index(kind="d", properties=index_props, ancestor=False)
        index2 = model.Index(kind="d", properties=index_props, ancestor=False)
        assert index1 is not index2
        assert hash(index1) == hash(index2)
        assert hash(index1) == hash(("d", index_props, False))


class TestIndexState:
    INDEX = mock.sentinel.index

    def test_constructor(self):
        index_state = model.IndexState(definition=self.INDEX, state="error", id=42)
        assert index_state._definition is self.INDEX
        assert index_state._state == "error"
        assert index_state._id == 42

    def test_definition(self):
        index_state = model.IndexState(definition=self.INDEX, state="serving", id=1)
        assert index_state.definition is self.INDEX

    @staticmethod
    def test_state():
        index_state = model.IndexState(definition=None, state="deleting", id=1)
        assert index_state.state == "deleting"

    @staticmethod
    def test_id():
        index_state = model.IndexState(definition=None, state="error", id=1001)
        assert index_state.id == 1001

    @staticmethod
    def test___repr__():
        index_prop = model.IndexProperty(name="a", direction="asc")
        index = model.Index(kind="IndK", properties=[index_prop], ancestor=False)
        index_state = model.IndexState(definition=index, state="building", id=1337)
        expected = (
            "IndexState(definition=Index(kind='IndK', properties=["
            "IndexProperty(name='a', direction='asc')], ancestor=False), "
            "state='building', id=1337)"
        )
        assert repr(index_state) == expected

    def test___eq__(self):
        index_state1 = model.IndexState(definition=self.INDEX, state="error", id=20)
        index_state2 = model.IndexState(
            definition=mock.sentinel.not_index, state="error", id=20
        )
        index_state3 = model.IndexState(definition=self.INDEX, state="serving", id=20)
        index_state4 = model.IndexState(definition=self.INDEX, state="error", id=80)
        index_state5 = mock.sentinel.index_state
        assert index_state1 == index_state1
        assert not index_state1 == index_state2
        assert not index_state1 == index_state3
        assert not index_state1 == index_state4
        assert not index_state1 == index_state5

    def test___ne__(self):
        index_state1 = model.IndexState(definition=self.INDEX, state="error", id=20)
        index_state2 = model.IndexState(
            definition=mock.sentinel.not_index, state="error", id=20
        )
        index_state3 = model.IndexState(definition=self.INDEX, state="serving", id=20)
        index_state4 = model.IndexState(definition=self.INDEX, state="error", id=80)
        index_state5 = mock.sentinel.index_state
        index_state6 = model.IndexState(definition=self.INDEX, state="error", id=20)
        assert not index_state1 != index_state1
        assert index_state1 != index_state2
        assert index_state1 != index_state3
        assert index_state1 != index_state4
        assert index_state1 != index_state5
        assert not index_state1 != index_state6

    def test___hash__(self):
        index_state1 = model.IndexState(definition=self.INDEX, state="error", id=88)
        index_state2 = model.IndexState(definition=self.INDEX, state="error", id=88)
        assert index_state1 is not index_state2
        assert hash(index_state1) == hash(index_state2)
        assert hash(index_state1) == hash((self.INDEX, "error", 88))


class TestModelAdapter:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            model.ModelAdapter()


def test_make_connection():
    with pytest.raises(NotImplementedError):
        model.make_connection()


class TestModelAttribute:
    @staticmethod
    def test_constructor():
        attr = model.ModelAttribute()
        assert isinstance(attr, model.ModelAttribute)

    @staticmethod
    def test__fix_up():
        attr = model.ModelAttribute()
        assert attr._fix_up(model.Model, "birthdate") is None


class Test_BaseValue:
    @staticmethod
    def test_constructor():
        wrapped = model._BaseValue(17)
        assert wrapped.b_val == 17

    @staticmethod
    def test_constructor_invalid_input():
        with pytest.raises(TypeError):
            model._BaseValue(None)
        with pytest.raises(TypeError):
            model._BaseValue([1, 2])

    @staticmethod
    def test___repr__():
        wrapped = model._BaseValue("abc")
        assert repr(wrapped) == "_BaseValue('abc')"

    @staticmethod
    def test___eq__():
        wrapped1 = model._BaseValue("one val")
        wrapped2 = model._BaseValue(25.5)
        wrapped3 = mock.sentinel.base_value
        assert wrapped1 == wrapped1
        assert not wrapped1 == wrapped2
        assert not wrapped1 == wrapped3

    @staticmethod
    def test___ne__():
        wrapped1 = model._BaseValue("one val")
        wrapped2 = model._BaseValue(25.5)
        wrapped3 = mock.sentinel.base_value
        wrapped4 = model._BaseValue("one val")
        assert not wrapped1 != wrapped1
        assert wrapped1 != wrapped2
        assert wrapped1 != wrapped3
        assert not wrapped1 != wrapped4

    @staticmethod
    def test___hash__():
        wrapped = model._BaseValue((11, 12, 88))
        with pytest.raises(TypeError):
            hash(wrapped)


class TestProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.Property()
        # Check that none of the constructor defaults were used.
        assert prop.__dict__ == {}

    @staticmethod
    def _example_validator(prop, value):
        return value.lower()

    def test__example_validator(self):
        value = "AbCde"
        validated = self._example_validator(None, value)
        assert validated == "abcde"
        assert self._example_validator(None, validated) == "abcde"

    def test_constructor_explicit(self):
        prop = model.Property(
            name="val",
            indexed=False,
            repeated=False,
            required=True,
            default="zorp",
            choices=("zorp", "zap", "zip"),
            validator=self._example_validator,
            verbose_name="VALUE FOR READING",
            write_empty_list=False,
        )
        assert prop._name == "val"
        assert not prop._indexed
        assert not prop._repeated
        assert prop._required
        assert prop._default == "zorp"
        assert prop._choices == frozenset(("zorp", "zap", "zip"))
        assert prop._validator is self._example_validator
        assert prop._verbose_name == "VALUE FOR READING"
        assert not prop._write_empty_list

    @staticmethod
    def test_constructor_invalid_name():
        with pytest.raises(TypeError):
            model.Property(name=["not", "a", "string"])
        with pytest.raises(ValueError):
            model.Property(name="has.a.dot")

    @staticmethod
    def test_constructor_repeated_not_allowed():
        with pytest.raises(ValueError):
            model.Property(name="a", repeated=True, required=True)
        with pytest.raises(ValueError):
            model.Property(name="b", repeated=True, default="zim")

    @staticmethod
    def test_constructor_invalid_choices():
        with pytest.raises(TypeError):
            model.Property(name="a", choices={"wrong": "container"})

    @staticmethod
    def test_constructor_invalid_validator():
        with pytest.raises(TypeError):
            model.Property(name="a", validator=mock.sentinel.validator)

    def test_repr(self):
        prop = model.Property(
            "val",
            indexed=False,
            repeated=False,
            required=True,
            default="zorp",
            choices=("zorp", "zap", "zip"),
            validator=self._example_validator,
            verbose_name="VALUE FOR READING",
            write_empty_list=False,
        )
        expected = (
            "Property('val', indexed=False, required=True, "
            "default='zorp', choices={}, validator={}, "
            "verbose_name='VALUE FOR READING')".format(prop._choices, prop._validator)
        )
        assert repr(prop) == expected

    @staticmethod
    def test_repr_subclass():
        class SimpleProperty(model.Property):
            _foo_type = None
            _bar = "eleventy"

            @ndb_utils.positional(1)
            def __init__(self, foo_type, bar):
                self._foo_type = foo_type
                self._bar = bar

        prop = SimpleProperty(foo_type=list, bar="nope")
        assert repr(prop) == "SimpleProperty(foo_type=list, bar='nope')"

    @staticmethod
    def test__datastore_type():
        prop = model.Property("foo")
        value = mock.sentinel.value
        assert prop._datastore_type(value) is value

    @staticmethod
    def test__comparison_indexed():
        prop = model.Property("color", indexed=False)
        with pytest.raises(exceptions.BadFilterError):
            prop._comparison("!=", "red")

    @staticmethod
    def test__comparison():
        prop = model.Property("sentiment", indexed=True)
        filter_node = prop._comparison(">=", 0.0)
        assert filter_node == query_module.FilterNode("sentiment", ">=", 0.0)

    @staticmethod
    def test__comparison_empty_value():
        prop = model.Property("height", indexed=True)
        filter_node = prop._comparison("=", None)
        assert filter_node == query_module.FilterNode("height", "=", None)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test___eq__():
        prop = model.Property("name", indexed=True)
        value = 1337
        expected = query_module.FilterNode("name", "=", value)

        filter_node_left = prop == value
        assert filter_node_left == expected
        filter_node_right = value == prop
        assert filter_node_right == expected

    @staticmethod
    def test___ne__():
        prop = model.Property("name", indexed=True)
        value = 7.0
        expected = query_module.FilterNode("name", "!=", value)

        ne_node_left = prop != value
        assert ne_node_left == expected
        ne_node_right = value != prop
        assert ne_node_right == expected

    @staticmethod
    def test___lt__():
        prop = model.Property("name", indexed=True)
        value = 2.0
        expected = query_module.FilterNode("name", "<", value)

        filter_node_left = prop < value
        assert filter_node_left == expected
        filter_node_right = value > prop
        assert filter_node_right == expected

    @staticmethod
    def test___le__():
        prop = model.Property("name", indexed=True)
        value = 20.0
        expected = query_module.FilterNode("name", "<=", value)

        filter_node_left = prop <= value
        assert filter_node_left == expected
        filter_node_right = value >= prop
        assert filter_node_right == expected

    @staticmethod
    def test___gt__():
        prop = model.Property("name", indexed=True)
        value = "new"
        expected = query_module.FilterNode("name", ">", value)

        filter_node_left = prop > value
        assert filter_node_left == expected
        filter_node_right = value < prop
        assert filter_node_right == expected

    @staticmethod
    def test___ge__():
        prop = model.Property("name", indexed=True)
        value = "old"
        expected = query_module.FilterNode("name", ">=", value)

        filter_node_left = prop >= value
        assert filter_node_left == expected
        filter_node_right = value <= prop
        assert filter_node_right == expected

    @staticmethod
    def test__IN_not_indexed():
        prop = model.Property("name", indexed=False)
        with pytest.raises(exceptions.BadFilterError):
            prop._IN([10, 20, 81])

        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__IN_wrong_container():
        prop = model.Property("name", indexed=True)
        with pytest.raises(exceptions.BadArgumentError):
            prop._IN({1: "a", 11: "b"})

        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__IN_default():
        prop = model.Property("name", indexed=True)
        or_node = prop._IN(["a", None, "xy"])
        expected = query_module.DisjunctionNode(
            query_module.FilterNode("name", "=", "a"),
            query_module.FilterNode("name", "=", None),
            query_module.FilterNode("name", "=", "xy"),
        )
        assert or_node == expected
        # Also verify the alias
        assert or_node == prop.IN(["a", None, "xy"])

    @staticmethod
    def test__IN_client():
        prop = model.Property("name", indexed=True)
        or_node = prop._IN(["a", None, "xy"], server_op=False)
        expected = query_module.DisjunctionNode(
            query_module.FilterNode("name", "=", "a"),
            query_module.FilterNode("name", "=", None),
            query_module.FilterNode("name", "=", "xy"),
        )
        assert or_node == expected
        # Also verify the alias
        assert or_node == prop.IN(["a", None, "xy"])

    @staticmethod
    def test__IN_server():
        prop = model.Property("name", indexed=True)
        in_node = prop._IN(["a", None, "xy"], server_op=True)
        assert in_node == prop.IN(["a", None, "xy"], server_op=True)
        assert in_node != query_module.DisjunctionNode(
            query_module.FilterNode("name", "=", "a"),
            query_module.FilterNode("name", "=", None),
            query_module.FilterNode("name", "=", "xy"),
        )
        assert in_node == query_module.FilterNode(
            "name", "in", ["a", None, "xy"], server_op=True
        )

    @staticmethod
    def test__NOT_IN():
        prop = model.Property("name", indexed=True)
        not_in_node = prop._NOT_IN(["a", None, "xy"])
        assert not_in_node == prop.NOT_IN(["a", None, "xy"])
        assert not_in_node == query_module.FilterNode(
            "name", "not_in", ["a", None, "xy"]
        )

    @staticmethod
    def test___neg__():
        prop = model.Property("name")
        order = -prop
        assert isinstance(order, query_module.PropertyOrder)
        assert order.name == "name"
        assert order.reverse is True
        order = -order
        assert order.reverse is False

    @staticmethod
    def test___pos__():
        prop = model.Property("name")
        order = +prop
        assert isinstance(order, query_module.PropertyOrder)
        assert order.name == "name"
        assert order.reverse is False

    @staticmethod
    def test__do_validate():
        validator = mock.Mock(spec=())
        value = 18
        choices = (1, 2, validator.return_value)

        prop = model.Property(name="foo", validator=validator, choices=choices)
        result = prop._do_validate(value)
        assert result is validator.return_value
        # Check validator call.
        validator.assert_called_once_with(prop, value)

    @staticmethod
    def test__do_validate_base_value():
        value = model._BaseValue(b"\x00\x01")

        prop = model.Property(name="foo")
        result = prop._do_validate(value)
        assert result is value
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__do_validate_validator_none():
        validator = mock.Mock(spec=(), return_value=None)
        value = 18

        prop = model.Property(name="foo", validator=validator)
        result = prop._do_validate(value)
        assert result == value
        # Check validator call.
        validator.assert_called_once_with(prop, value)

    @staticmethod
    def test__do_validate_not_in_choices():
        value = 18
        prop = model.Property(name="foo", choices=(1, 2))

        with pytest.raises(exceptions.BadValueError):
            prop._do_validate(value)

    @staticmethod
    def test__do_validate_call_validation():
        class SimpleProperty(model.Property):
            def _validate(self, value):
                value.append("SimpleProperty._validate")
                return value

        value = []
        prop = SimpleProperty(name="foo")
        result = prop._do_validate(value)
        assert result is value
        assert value == ["SimpleProperty._validate"]

    @staticmethod
    def test__fix_up():
        prop = model.Property(name="foo")
        assert prop._code_name is None
        prop._fix_up(None, "bar")
        assert prop._code_name == "bar"

    @staticmethod
    def test__fix_up_no_name():
        prop = model.Property()
        assert prop._name is None
        assert prop._code_name is None

        prop._fix_up(None, "both")
        assert prop._code_name == "both"
        assert prop._name == "both"

    @staticmethod
    def test__store_value():
        entity = mock.Mock(_values={}, spec=("_values",))
        prop = model.Property(name="foo")
        prop._store_value(entity, mock.sentinel.value)
        assert entity._values == {prop._name: mock.sentinel.value}

    @staticmethod
    def test__set_value():
        entity = mock.Mock(
            _projection=None, _values={}, spec=("_projection", "_values")
        )
        prop = model.Property(name="foo", repeated=False)
        prop._set_value(entity, 19)
        assert entity._values == {prop._name: 19}

    @staticmethod
    def test__set_value_none():
        entity = mock.Mock(
            _projection=None, _values={}, spec=("_projection", "_values")
        )
        prop = model.Property(name="foo", repeated=False)
        prop._set_value(entity, None)
        assert entity._values == {prop._name: None}
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__set_value_repeated():
        entity = mock.Mock(
            _projection=None, _values={}, spec=("_projection", "_values")
        )
        prop = model.Property(name="foo", repeated=True)
        prop._set_value(entity, (11, 12, 13))
        assert entity._values == {prop._name: [11, 12, 13]}

    @staticmethod
    def test__set_value_repeated_bad_container():
        entity = mock.Mock(
            _projection=None, _values={}, spec=("_projection", "_values")
        )
        prop = model.Property(name="foo", repeated=True)
        with pytest.raises(exceptions.BadValueError):
            prop._set_value(entity, None)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__set_value_projection():
        entity = mock.Mock(_projection=("a", "b"), spec=("_projection",))
        prop = model.Property(name="foo", repeated=True)
        with pytest.raises(model.ReadonlyPropertyError):
            prop._set_value(entity, None)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__has_value():
        prop = model.Property(name="foo")
        values = {prop._name: 88}
        entity1 = mock.Mock(_values=values, spec=("_values",))
        entity2 = mock.Mock(_values={}, spec=("_values",))

        assert prop._has_value(entity1)
        assert not prop._has_value(entity2)

    @staticmethod
    def test__retrieve_value():
        prop = model.Property(name="foo")
        values = {prop._name: b"\x00\x01"}
        entity1 = mock.Mock(_values=values, spec=("_values",))
        entity2 = mock.Mock(_values={}, spec=("_values",))

        assert prop._retrieve_value(entity1) == b"\x00\x01"
        assert prop._retrieve_value(entity2) is None
        assert prop._retrieve_value(entity2, default=b"zip") == b"zip"

    @staticmethod
    def test__get_user_value():
        prop = model.Property(name="prop")
        value = b"\x00\x01"
        values = {prop._name: value}
        entity = mock.Mock(_values=values, spec=("_values",))
        assert value is prop._get_user_value(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__get_user_value_wrapped():
        class SimpleProperty(model.Property):
            def _from_base_type(self, value):
                return value * 2.0

        prop = SimpleProperty(name="prop")
        values = {prop._name: model._BaseValue(9.5)}
        entity = mock.Mock(_values=values, spec=("_values",))
        assert prop._get_user_value(entity) == 19.0

    @staticmethod
    def test__get_base_value():
        class SimpleProperty(model.Property):
            def _validate(self, value):
                return value + 1

        prop = SimpleProperty(name="prop")
        values = {prop._name: 20}
        entity = mock.Mock(_values=values, spec=("_values",))
        assert prop._get_base_value(entity) == model._BaseValue(21)

    @staticmethod
    def test__get_base_value_wrapped():
        prop = model.Property(name="prop")
        value = model._BaseValue(b"\x00\x01")
        values = {prop._name: value}
        entity = mock.Mock(_values=values, spec=("_values",))
        assert value is prop._get_base_value(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__get_base_value_unwrapped_as_list():
        class SimpleProperty(model.Property):
            def _validate(self, value):
                return value + 11

        prop = SimpleProperty(name="prop", repeated=False)
        values = {prop._name: 20}
        entity = mock.Mock(_values=values, spec=("_values",))
        assert prop._get_base_value_unwrapped_as_list(entity) == [31]

    @staticmethod
    def test__get_base_value_unwrapped_as_list_empty():
        prop = model.Property(name="prop", repeated=False)
        entity = mock.Mock(_values={}, spec=("_values",))
        assert prop._get_base_value_unwrapped_as_list(entity) == [None]
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__get_base_value_unwrapped_as_list_repeated():
        class SimpleProperty(model.Property):
            def _validate(self, value):
                return value / 10.0

        prop = SimpleProperty(name="prop", repeated=True)
        values = {prop._name: [20, 30, 40]}
        entity = mock.Mock(_values=values, spec=("_values",))
        expected = [2.0, 3.0, 4.0]
        assert prop._get_base_value_unwrapped_as_list(entity) == expected

    @staticmethod
    def test__opt_call_from_base_type():
        prop = model.Property(name="prop")
        value = b"\x00\x01"
        assert value is prop._opt_call_from_base_type(value)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__opt_call_from_base_type_wrapped():
        class SimpleProperty(model.Property):
            def _from_base_type(self, value):
                return value * 2.0

        prop = SimpleProperty(name="prop")
        value = model._BaseValue(8.5)
        assert prop._opt_call_from_base_type(value) == 17.0

    @staticmethod
    def test__value_to_repr():
        class SimpleProperty(model.Property):
            def _from_base_type(self, value):
                return value * 3.0

        prop = SimpleProperty(name="prop")
        value = model._BaseValue(9.25)
        assert prop._value_to_repr(value) == "27.75"

    @staticmethod
    def test__opt_call_to_base_type():
        class SimpleProperty(model.Property):
            def _validate(self, value):
                return value + 1

        prop = SimpleProperty(name="prop")
        value = 17
        result = prop._opt_call_to_base_type(value)
        assert result == model._BaseValue(value + 1)

    @staticmethod
    def test__opt_call_to_base_type_wrapped():
        prop = model.Property(name="prop")
        value = model._BaseValue(b"\x00\x01")
        assert value is prop._opt_call_to_base_type(value)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__call_from_base_type():
        class SimpleProperty(model.Property):
            def _from_base_type(self, value):
                value.append("SimpleProperty._from_base_type")
                return value

        prop = SimpleProperty(name="prop")
        value = []
        assert value is prop._call_from_base_type(value)
        assert value == ["SimpleProperty._from_base_type"]

    @staticmethod
    def _property_subtype_chain():
        class A(model.Property):
            def _validate(self, value):
                value.append("A._validate")
                return value

            def _to_base_type(self, value):
                value.append("A._to_base_type")
                return value

        class B(A):
            def _validate(self, value):
                value.append("B._validate")
                return value

            def _to_base_type(self, value):
                value.append("B._to_base_type")
                return value

        class C(B):
            def _validate(self, value):
                value.append("C._validate")
                return value

        value = []

        prop_a = A(name="name-a")
        assert value is prop_a._validate(value)
        assert value == ["A._validate"]
        assert value is prop_a._to_base_type(value)
        assert value == ["A._validate", "A._to_base_type"]
        prop_b = B(name="name-b")
        assert value is prop_b._validate(value)
        assert value == ["A._validate", "A._to_base_type", "B._validate"]
        assert value is prop_b._to_base_type(value)
        assert value == [
            "A._validate",
            "A._to_base_type",
            "B._validate",
            "B._to_base_type",
        ]
        prop_c = C(name="name-c")
        assert value is prop_c._validate(value)
        assert value == [
            "A._validate",
            "A._to_base_type",
            "B._validate",
            "B._to_base_type",
            "C._validate",
        ]

        return A, B, C

    def test__call_to_base_type(self):
        _, _, PropertySubclass = self._property_subtype_chain()
        prop = PropertySubclass(name="prop")
        value = []
        assert value is prop._call_to_base_type(value)
        assert value == [
            "C._validate",
            "B._validate",
            "B._to_base_type",
            "A._validate",
            "A._to_base_type",
        ]

    def test__call_shallow_validation(self):
        _, _, PropertySubclass = self._property_subtype_chain()
        prop = PropertySubclass(name="prop")
        value = []
        assert value is prop._call_shallow_validation(value)
        assert value == ["C._validate", "B._validate"]

    @staticmethod
    def test__call_shallow_validation_no_break():
        class SimpleProperty(model.Property):
            def _validate(self, value):
                value.append("SimpleProperty._validate")
                return value

        prop = SimpleProperty(name="simple")
        value = []
        assert value is prop._call_shallow_validation(value)
        assert value == ["SimpleProperty._validate"]

    @staticmethod
    def _property_subtype():
        class SomeProperty(model.Property):
            def find_me(self):
                return self._name

            def IN(self):
                return len(self._name) < 20

        prop = SomeProperty(name="hi")
        assert prop.find_me() == "hi"
        assert prop.IN()

        return SomeProperty

    def test__find_methods(self):
        SomeProperty = self._property_subtype()
        # Make sure cache is empty.
        assert model.Property._FIND_METHODS_CACHE == {}

        methods = SomeProperty._find_methods("IN", "find_me")
        expected = [SomeProperty.IN, SomeProperty.find_me, model.Property.IN]
        assert methods == expected
        # Check cache
        key = "{}.{}".format(SomeProperty.__module__, SomeProperty.__name__)
        assert model.Property._FIND_METHODS_CACHE == {key: {("IN", "find_me"): methods}}

    def test__find_methods_reverse(self):
        SomeProperty = self._property_subtype()
        # Make sure cache is empty.
        assert model.Property._FIND_METHODS_CACHE == {}

        methods = SomeProperty._find_methods("IN", "find_me", reverse=True)
        expected = [model.Property.IN, SomeProperty.find_me, SomeProperty.IN]
        assert methods == expected
        # Check cache
        key = "{}.{}".format(SomeProperty.__module__, SomeProperty.__name__)
        assert model.Property._FIND_METHODS_CACHE == {
            key: {("IN", "find_me"): list(reversed(methods))}
        }

    def test__find_methods_cached(self):
        SomeProperty = self._property_subtype()
        # Set cache
        methods = mock.sentinel.methods
        key = "{}.{}".format(SomeProperty.__module__, SomeProperty.__name__)
        model.Property._FIND_METHODS_CACHE = {key: {("IN", "find_me"): methods}}
        assert SomeProperty._find_methods("IN", "find_me") is methods

    def test__find_methods_cached_reverse(self):
        SomeProperty = self._property_subtype()
        # Set cache
        methods = ["a", "b"]
        key = "{}.{}".format(SomeProperty.__module__, SomeProperty.__name__)
        model.Property._FIND_METHODS_CACHE = {key: {("IN", "find_me"): methods}}
        assert SomeProperty._find_methods("IN", "find_me", reverse=True) == [
            "b",
            "a",
        ]

    @staticmethod
    def test__apply_list():
        method1 = mock.Mock(spec=())
        method2 = mock.Mock(spec=(), return_value=None)
        method3 = mock.Mock(spec=())

        prop = model.Property(name="benji")
        to_call = prop._apply_list([method1, method2, method3])
        assert isinstance(to_call, types.FunctionType)

        value = mock.sentinel.value
        result = to_call(value)
        assert result is method3.return_value

        # Check mocks.
        method1.assert_called_once_with(prop, value)
        method2.assert_called_once_with(prop, method1.return_value)
        method3.assert_called_once_with(prop, method1.return_value)

    @staticmethod
    def test__apply_to_values():
        value = "foo"
        prop = model.Property(name="bar", repeated=False)
        entity = mock.Mock(_values={prop._name: value}, spec=("_values",))
        function = mock.Mock(spec=(), return_value="foo2")

        result = prop._apply_to_values(entity, function)
        assert result == function.return_value
        assert entity._values == {prop._name: result}
        # Check mocks.
        function.assert_called_once_with(value)

    @staticmethod
    def test__apply_to_values_when_none():
        prop = model.Property(name="bar", repeated=False, default=None)
        entity = mock.Mock(_values={}, spec=("_values",))
        function = mock.Mock(spec=())

        result = prop._apply_to_values(entity, function)
        assert result is None
        assert entity._values == {}
        # Check mocks.
        function.assert_not_called()

    @staticmethod
    def test__apply_to_values_transformed_none():
        value = 7.5
        prop = model.Property(name="bar", repeated=False)
        entity = mock.Mock(_values={prop._name: value}, spec=("_values",))
        function = mock.Mock(spec=(), return_value=None)

        result = prop._apply_to_values(entity, function)
        assert result == value
        assert entity._values == {prop._name: result}
        # Check mocks.
        function.assert_called_once_with(value)

    @staticmethod
    def test__apply_to_values_transformed_unchanged():
        value = mock.sentinel.value
        prop = model.Property(name="bar", repeated=False)
        entity = mock.Mock(_values={prop._name: value}, spec=("_values",))
        function = mock.Mock(spec=(), return_value=value)

        result = prop._apply_to_values(entity, function)
        assert result == value
        assert entity._values == {prop._name: result}
        # Check mocks.
        function.assert_called_once_with(value)

    @staticmethod
    def test__apply_to_values_repeated():
        value = [1, 2, 3]
        prop = model.Property(name="bar", repeated=True)
        entity = mock.Mock(_values={prop._name: value}, spec=("_values",))
        function = mock.Mock(spec=(), return_value=42)

        result = prop._apply_to_values(entity, function)
        assert result == [
            function.return_value,
            function.return_value,
            function.return_value,
        ]
        assert result is value  # Check modify in-place.
        assert entity._values == {prop._name: result}
        # Check mocks.
        assert function.call_count == 3
        calls = [mock.call(1), mock.call(2), mock.call(3)]
        function.assert_has_calls(calls)

    @staticmethod
    def test__apply_to_values_repeated_when_none():
        prop = model.Property(name="bar", repeated=True, default=None)
        entity = mock.Mock(_values={}, spec=("_values",))
        function = mock.Mock(spec=())

        result = prop._apply_to_values(entity, function)
        assert result == []
        assert entity._values == {prop._name: result}
        # Check mocks.
        function.assert_not_called()

    @staticmethod
    def test__get_value():
        prop = model.Property(name="prop")
        value = b"\x00\x01"
        values = {prop._name: value}
        entity = mock.Mock(
            _projection=None, _values=values, spec=("_projection", "_values")
        )
        assert value is prop._get_value(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__get_value_projected_present():
        prop = model.Property(name="prop")
        value = 92.5
        values = {prop._name: value}
        entity = mock.Mock(
            _projection=(prop._name,),
            _values=values,
            spec=("_projection", "_values"),
        )
        assert value is prop._get_value(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__get_value_projected_absent():
        prop = model.Property(name="prop")
        entity = mock.Mock(_projection=("nope",), spec=("_projection",))
        with pytest.raises(model.UnprojectedPropertyError):
            prop._get_value(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__delete_value():
        prop = model.Property(name="prop")
        value = b"\x00\x01"
        values = {prop._name: value}
        entity = mock.Mock(_values=values, spec=("_values",))
        prop._delete_value(entity)
        assert values == {}

    @staticmethod
    def test__delete_value_no_op():
        prop = model.Property(name="prop")
        values = {}
        entity = mock.Mock(_values=values, spec=("_values",))
        prop._delete_value(entity)
        assert values == {}

    @staticmethod
    def test__is_initialized_not_required():
        prop = model.Property(name="prop", required=False)
        entity = mock.sentinel.entity
        assert prop._is_initialized(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__is_initialized_default_fallback():
        prop = model.Property(name="prop", required=True, default=11111)
        values = {}
        entity = mock.Mock(
            _projection=None, _values=values, spec=("_projection", "_values")
        )
        assert prop._is_initialized(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__is_initialized_set_to_none():
        prop = model.Property(name="prop", required=True)
        values = {prop._name: None}
        entity = mock.Mock(
            _projection=None, _values=values, spec=("_projection", "_values")
        )
        assert not prop._is_initialized(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test_instance_descriptors():
        class Model(object):
            prop = model.Property(name="prop", required=True)

            def __init__(self):
                self._projection = None
                self._values = {}

        m = Model()
        value = 1234.5
        # __set__
        m.prop = value
        assert m._values == {"prop": value}
        # __get__
        assert m.prop == value
        # __delete__
        del m.prop
        assert m._values == {}

    @staticmethod
    def test_class_descriptors():
        prop = model.Property(name="prop", required=True)

        class Model:
            prop2 = prop

        assert Model.prop2 is prop

    @staticmethod
    def test__serialize():
        prop = model.Property(name="prop")
        with pytest.raises(NotImplementedError):
            prop._serialize(None, None)

    @staticmethod
    def test__deserialize():
        prop = model.Property(name="prop")
        with pytest.raises(NotImplementedError):
            prop._deserialize(None, None)

    @staticmethod
    def test__prepare_for_put():
        prop = model.Property(name="prop")
        assert prop._prepare_for_put(None) is None

    @staticmethod
    def test__check_property():
        prop = model.Property(name="prop")
        assert prop._check_property() is None

    @staticmethod
    def test__check_property_not_indexed():
        prop = model.Property(name="prop", indexed=False)
        with pytest.raises(model.InvalidPropertyError):
            prop._check_property(require_indexed=True)

    @staticmethod
    def test__check_property_with_subproperty():
        prop = model.Property(name="prop", indexed=True)
        with pytest.raises(model.InvalidPropertyError):
            prop._check_property(rest="a.b.c")

    @staticmethod
    def test__get_for_dict():
        prop = model.Property(name="prop")
        value = b"\x00\x01"
        values = {prop._name: value}
        entity = mock.Mock(
            _projection=None, _values=values, spec=("_projection", "_values")
        )
        assert value is prop._get_for_dict(entity)
        # Cache is untouched.
        assert model.Property._FIND_METHODS_CACHE == {}

    @staticmethod
    def test__to_datastore():
        class SomeKind(model.Model):
            prop = model.Property()

        entity = SomeKind(prop="foo")
        data = {}
        assert SomeKind.prop._to_datastore(entity, data) == ("prop",)
        assert data == {"prop": "foo"}

    @staticmethod
    def test__to_datastore_prop_is_repeated():
        class SomeKind(model.Model):
            prop = model.Property(repeated=True)

        entity = SomeKind(prop=["foo", "bar"])
        data = {}
        assert SomeKind.prop._to_datastore(entity, data) == ("prop",)
        assert data == {"prop": ["foo", "bar"]}

    @staticmethod
    def test__to_datastore_w_prefix():
        class SomeKind(model.Model):
            prop = model.Property()

        entity = SomeKind(prop="foo")
        data = {}
        assert SomeKind.prop._to_datastore(entity, data, prefix="pre.") == ("pre.prop",)
        assert data == {"pre.prop": "foo"}

    @staticmethod
    def test__to_datastore_w_prefix_ancestor_repeated():
        class SomeKind(model.Model):
            prop = model.Property()

        entity = SomeKind(prop="foo")
        data = {}
        assert SomeKind.prop._to_datastore(
            entity, data, prefix="pre.", repeated=True
        ) == ("pre.prop",)
        assert data == {"pre.prop": ["foo"]}


class Test__validate_key:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_valid_value():
        value = model.Key("This", 1)
        result = model._validate_key(value)
        assert result is value

    @staticmethod
    def test_invalid_value():
        with pytest.raises(exceptions.BadValueError):
            model._validate_key(None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_unchecked_model_type():
        value = model.Key("This", 1)
        entity = model.Model()

        result = model._validate_key(value, entity=entity)
        assert result is value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_unchecked_expando_type():
        value = model.Key("This", 1)
        entity = model.Expando()

        result = model._validate_key(value, entity=entity)
        assert result is value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_same_kind():
        class Mine(model.Model):
            pass

        value = model.Key(Mine, "yours")
        entity = mock.Mock(spec=Mine)
        entity._get_kind.return_value = "Mine"

        result = model._validate_key(value, entity=entity)
        assert result is value
        entity._get_kind.assert_called_once_with()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_different_kind():
        class Mine(model.Model):
            pass

        value = model.Key(Mine, "yours")
        entity = mock.Mock(spec=Mine)
        entity._get_kind.return_value = "NotMine"

        with pytest.raises(model.KindError):
            model._validate_key(value, entity=entity)

        calls = [mock.call(), mock.call()]
        entity._get_kind.assert_has_calls(calls)


class TestModelKey:
    @staticmethod
    def test_constructor():
        prop = model.ModelKey()
        assert prop._name == "__key__"
        assert prop.__dict__ == {"_name": "__key__"}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_compare_valid():
        prop = model.ModelKey()
        value = key_module.Key("say", "quay")
        filter_node = prop._comparison(">=", value)
        assert filter_node == query_module.FilterNode("__key__", ">=", value)

    @staticmethod
    def test_compare_invalid():
        prop = model.ModelKey()
        with pytest.raises(exceptions.BadValueError):
            prop == None  # noqa: E711

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__validate():
        prop = model.ModelKey()
        value = key_module.Key("Up", 909)
        assert prop._validate(value) is value

    @staticmethod
    def test__validate_wrong_type():
        prop = model.ModelKey()
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__set_value():
        entity = model.Model()
        value = key_module.Key("Map", 8898)

        model.ModelKey._set_value(entity, value)
        assert entity._entity_key is value

    @staticmethod
    def test__set_value_none():
        entity = mock.Mock(spec=("_entity_key",))

        assert entity._entity_key is not None
        model.ModelKey._set_value(entity, None)
        assert entity._entity_key is None

    @staticmethod
    def test__get_value():
        entity = mock.Mock(spec=("_entity_key",))

        result = model.ModelKey._get_value(entity)
        assert result is entity._entity_key

    @staticmethod
    def test__delete_value():
        entity = mock.Mock(spec=("_entity_key",))

        assert entity._entity_key is not None
        model.ModelKey._delete_value(entity)
        assert entity._entity_key is None


class TestBooleanProperty:
    @staticmethod
    def test__validate():
        prop = model.BooleanProperty(name="certify")
        value = True
        assert prop._validate(value) is value

    @staticmethod
    def test__validate_bad_value():
        prop = model.BooleanProperty(name="certify")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__db_set_value():
        prop = model.BooleanProperty(name="certify")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.BooleanProperty(name="certify")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)

    @staticmethod
    def test__from_base_type_bool():
        prop = model.BooleanProperty(name="certify")
        assert prop._from_base_type(True) is None

    @staticmethod
    def test__from_base_type_int():
        prop = model.BooleanProperty(name="certify")
        assert prop._from_base_type(1) is True


class TestIntegerProperty:
    @staticmethod
    def test__validate():
        prop = model.IntegerProperty(name="count")
        value = 829038402384
        assert prop._validate(value) is value

    @staticmethod
    def test__validate_bool():
        prop = model.IntegerProperty(name="count")
        value = True
        assert prop._validate(value) == 1

    @staticmethod
    def test__validate_bad_value():
        prop = model.IntegerProperty(name="count")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__db_set_value():
        prop = model.IntegerProperty(name="count")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.IntegerProperty(name="count")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)


class TestFloatProperty:
    @staticmethod
    def test__validate():
        prop = model.FloatProperty(name="continuous")
        value = 7.25
        assert prop._validate(value) is value

    @staticmethod
    def test__validate_int():
        prop = model.FloatProperty(name="continuous")
        value = 1015
        assert prop._validate(value) == 1015.0

    @staticmethod
    def test__validate_bool():
        prop = model.FloatProperty(name="continuous")
        value = True
        assert prop._validate(value) == 1.0

    @staticmethod
    def test__validate_bad_value():
        prop = model.FloatProperty(name="continuous")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__db_set_value():
        prop = model.FloatProperty(name="continuous")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.FloatProperty(name="continuous")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)


class Test_CompressedValue:
    @staticmethod
    def test_constructor():
        value = b"abc" * 1000
        z_val = zlib.compress(value)
        compressed_value = model._CompressedValue(z_val)

        assert compressed_value.z_val == z_val

    @staticmethod
    def test___repr__():
        z_val = zlib.compress(b"12345678901234567890")
        compressed_value = model._CompressedValue(z_val)
        expected = "_CompressedValue(" + repr(z_val) + ")"
        assert repr(compressed_value) == expected

    @staticmethod
    def test___eq__():
        z_val1 = zlib.compress(b"12345678901234567890")
        compressed_value1 = model._CompressedValue(z_val1)
        z_val2 = zlib.compress(b"12345678901234567890abcde\x00")
        compressed_value2 = model._CompressedValue(z_val2)
        compressed_value3 = mock.sentinel.compressed_value
        assert compressed_value1 == compressed_value1
        assert not compressed_value1 == compressed_value2
        assert not compressed_value1 == compressed_value3

    @staticmethod
    def test___ne__():
        z_val1 = zlib.compress(b"12345678901234567890")
        compressed_value1 = model._CompressedValue(z_val1)
        z_val2 = zlib.compress(b"12345678901234567890abcde\x00")
        compressed_value2 = model._CompressedValue(z_val2)
        compressed_value3 = mock.sentinel.compressed_value
        compressed_value4 = model._CompressedValue(z_val1)
        assert not compressed_value1 != compressed_value1
        assert compressed_value1 != compressed_value2
        assert compressed_value1 != compressed_value3
        assert not compressed_value1 != compressed_value4

    @staticmethod
    def test___hash__():
        z_val = zlib.compress(b"12345678901234567890")
        compressed_value = model._CompressedValue(z_val)
        with pytest.raises(TypeError):
            hash(compressed_value)


class TestBlobProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.BlobProperty()
        # Check that none of the constructor defaults were used.
        assert prop.__dict__ == {}

    @staticmethod
    def test_constructor_explicit():
        prop = model.BlobProperty(
            name="blob_val",
            compressed=True,
            indexed=False,
            repeated=False,
            required=True,
            default=b"eleven\x11",
            choices=(b"a", b"b", b"c", b"eleven\x11"),
            validator=TestProperty._example_validator,
            verbose_name="VALUE FOR READING",
            write_empty_list=False,
        )
        assert prop._name == "blob_val"
        assert prop._compressed
        assert not prop._indexed
        assert not prop._repeated
        assert prop._required
        assert prop._default == b"eleven\x11"
        assert prop._choices == frozenset((b"a", b"b", b"c", b"eleven\x11"))
        assert prop._validator is TestProperty._example_validator
        assert prop._verbose_name == "VALUE FOR READING"
        assert not prop._write_empty_list

    @staticmethod
    def test_constructor_compressed_and_indexed():
        with pytest.raises(NotImplementedError):
            model.BlobProperty(name="foo", compressed=True, indexed=True)

    @staticmethod
    def test__value_to_repr():
        prop = model.BlobProperty(name="blob")
        as_repr = prop._value_to_repr("abc")
        assert as_repr == "'abc'"

    @staticmethod
    def test__value_to_repr_truncated():
        prop = model.BlobProperty(name="blob")
        value = bytes(range(256)) * 5
        as_repr = prop._value_to_repr(value)
        expected = repr(value)[: model._MAX_STRING_LENGTH] + "...'"
        assert as_repr == expected

    @staticmethod
    def test__validate():
        prop = model.BlobProperty(name="blob")
        assert prop._validate(b"abc") is None

    @staticmethod
    def test__validate_wrong_type():
        prop = model.BlobProperty(name="blob")
        values = (48, {"a": "c"})
        for value in values:
            with pytest.raises(exceptions.BadValueError):
                prop._validate(value)

    @staticmethod
    def test__validate_indexed_too_long():
        prop = model.BlobProperty(name="blob", indexed=True)
        value = b"\x00" * 2000
        with pytest.raises(exceptions.BadValueError):
            prop._validate(value)

    @staticmethod
    def test__to_base_type():
        prop = model.BlobProperty(name="blob", compressed=True)
        value = b"abc" * 10
        converted = prop._to_base_type(value)

        assert isinstance(converted, model._CompressedValue)
        assert converted.z_val == zlib.compress(value)

    @staticmethod
    def test__to_base_type_no_convert():
        prop = model.BlobProperty(name="blob", compressed=False)
        value = b"abc" * 10
        converted = prop._to_base_type(value)
        assert converted is None

    @staticmethod
    def test__from_base_type():
        prop = model.BlobProperty(name="blob")
        original = b"abc" * 10
        z_val = zlib.compress(original)
        value = model._CompressedValue(z_val)
        converted = prop._from_base_type(value)

        assert converted == original

    @staticmethod
    def test__from_base_type_no_compressed_value_uncompressed():
        prop = model.BlobProperty(name="blob", compressed=True)
        original = b"abc" * 10
        converted = prop._from_base_type(original)

        assert converted == original

    @staticmethod
    def test__from_base_type_no_compressed_value_compressed():
        prop = model.BlobProperty(name="blob", compressed=True)
        original = b"abc" * 10
        z_val = zlib.compress(original)
        converted = prop._from_base_type(z_val)

        assert converted == original

    @staticmethod
    def test__from_base_type_no_convert():
        prop = model.BlobProperty(name="blob")
        converted = prop._from_base_type(b"abc")
        assert converted is None

    @staticmethod
    def test__db_set_value():
        prop = model.BlobProperty(name="blob")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_set_compressed_meaning():
        prop = model.BlobProperty(name="blob")
        with pytest.raises(NotImplementedError):
            prop._db_set_compressed_meaning(None)

    @staticmethod
    def test__db_set_uncompressed_meaning():
        prop = model.BlobProperty(name="blob")
        with pytest.raises(NotImplementedError):
            prop._db_set_uncompressed_meaning(None)

    @staticmethod
    def test__db_get_value():
        prop = model.BlobProperty(name="blob")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_datastore_compressed():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True)

        uncompressed_value = b"abc" * 1000
        compressed_value = zlib.compress(uncompressed_value)
        entity = ThisKind(foo=uncompressed_value)
        ds_entity = model._entity_to_ds_entity(entity)
        assert "foo" in ds_entity._meanings
        assert ds_entity._meanings["foo"][0] == model._MEANING_COMPRESSED
        assert ds_entity._meanings["foo"][1] == compressed_value

    @staticmethod
    def test__to_datastore_legacy_compressed_with_prefix(in_context):
        """Regression test for #602

        https://github.com/googleapis/python-ndb/issues/602
        """

        class ThisKind(model.Model):
            bar = model.BlobProperty(compressed=True)

        class ParentKind(model.Model):
            foo = model.StructuredProperty(ThisKind)

        with in_context.new(legacy_data=True).use():
            uncompressed_value = b"abc" * 1000
            compressed_value = zlib.compress(uncompressed_value)
            entity = ParentKind(foo=ThisKind(bar=uncompressed_value))
            ds_entity = model._entity_to_ds_entity(entity)
            assert "foo.bar" in ds_entity._meanings
            assert ds_entity._meanings["foo.bar"][0] == model._MEANING_COMPRESSED
            assert ds_entity._meanings["foo.bar"][1] == compressed_value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_datastore_compressed_repeated():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True, repeated=True)

        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        entity = ThisKind(foo=[uncompressed_value_one, uncompressed_value_two])
        ds_entity = model._entity_to_ds_entity(entity)
        assert "foo" in ds_entity._meanings
        assert ds_entity._meanings["foo"][0] == model._MEANING_COMPRESSED
        assert ds_entity._meanings["foo"][1] == [
            compressed_value_one,
            compressed_value_two,
        ]

    @staticmethod
    def test__to_datastore_legacy_compressed_repeated_in_parent(in_context):
        class ThisKind(model.Model):
            bar = model.BlobProperty(compressed=True, repeated=False)

        class ParentKind(model.Model):
            foo = model.StructuredProperty(ThisKind, repeated=True)

        with in_context.new(legacy_data=True).use():
            uncompressed_value_one = b"abc" * 1000
            compressed_value_one = zlib.compress(uncompressed_value_one)
            uncompressed_value_two = b"xyz" * 1000
            compressed_value_two = zlib.compress(uncompressed_value_two)
            entity = ParentKind(
                foo=[
                    ThisKind(bar=uncompressed_value_one),
                    ThisKind(bar=uncompressed_value_two),
                ]
            )
            ds_entity = model._entity_to_ds_entity(entity)
            assert "foo.bar" not in ds_entity._meanings
            assert "foo.bar" in ds_entity.keys()
            assert ds_entity.get("foo.bar") == [
                compressed_value_one,
                compressed_value_two,
            ]

    @staticmethod
    def test__to_datastore_legacy_compressed_repeated_in_parent_uninitialized(
        in_context,
    ):
        class ThisKind(model.Model):
            bar = model.BlobProperty(compressed=True, repeated=False)

        class ParentKind(model.Model):
            foo = model.StructuredProperty(ThisKind, repeated=True)

        with in_context.new(legacy_data=True).use():
            uncompressed_value = b"abc" * 1000
            compressed_value = zlib.compress(uncompressed_value)
            entity = ParentKind(foo=[ThisKind(), ThisKind(bar=uncompressed_value)])
            ds_entity = model._entity_to_ds_entity(entity)
            assert "foo.bar" not in ds_entity._meanings
            assert "foo.bar" in ds_entity.keys()
            assert ds_entity.get("foo.bar") == [None, compressed_value]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_datastore_compressed_uninitialized():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True)

        entity = ThisKind()
        ds_entity = model._entity_to_ds_entity(entity)
        assert "foo" not in ds_entity._meanings

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_datastore_uncompressed():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=False)

        uncompressed_value = b"abc"
        entity = ThisKind(foo=uncompressed_value)
        ds_entity = model._entity_to_ds_entity(entity)
        assert "foo" not in ds_entity._meanings

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_to_uncompressed():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=False)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value = b"abc" * 1000
        compressed_value = zlib.compress(uncompressed_value)
        datastore_entity.update({"foo": compressed_value})
        meanings = {"foo": (model._MEANING_COMPRESSED, compressed_value)}
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert entity.foo == uncompressed_value
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == uncompressed_value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_to_compressed():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value = b"abc" * 1000
        compressed_value = zlib.compress(uncompressed_value)
        datastore_entity.update({"foo": compressed_value})
        meanings = {"foo": (model._MEANING_COMPRESSED, compressed_value)}
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == compressed_value

    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_repeated_to_compressed(self):
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        compressed_value = [compressed_value_one, compressed_value_two]
        datastore_entity.update({"foo": compressed_value})
        meanings = {
            "foo": (
                model._MEANING_COMPRESSED,
                compressed_value,
            )
        }
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == [compressed_value_one, compressed_value_two]

    @pytest.mark.skipif(
        [int(v) for v in datastore.__version__.split(".")] < [2, 20, 2],
        reason="uses meanings semantics from datastore v2.20.2 and later",
    )
    @pytest.mark.parametrize(
        "meaning",
        [
            (model._MEANING_COMPRESSED, None),  # set root meaning
            (model._MEANING_COMPRESSED, []),
            (model._MEANING_COMPRESSED, [1, 1]),
            (None, [model._MEANING_COMPRESSED] * 2),  # set sub-meanings
        ],
    )
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_repeated_to_compressed_tuple_meaning(
        self, meaning
    ):
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        compressed_value = [compressed_value_one, compressed_value_two]
        datastore_entity.update({"foo": compressed_value})
        meanings = {
            "foo": (
                meaning,
                compressed_value,
            )
        }
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == [compressed_value_one, compressed_value_two]

    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_repeated_to_uncompressed(self):
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=False, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        compressed_value = [compressed_value_one, compressed_value_two]
        datastore_entity.update({"foo": compressed_value})
        meanings = {
            "foo": (
                model._MEANING_COMPRESSED,
                compressed_value,
            )
        }
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == [uncompressed_value_one, uncompressed_value_two]

    @pytest.mark.skipif(
        [int(v) for v in datastore.__version__.split(".")] < [2, 20, 2],
        reason="uses meanings semantics from datastore v2.20.2 and later",
    )
    @pytest.mark.parametrize(
        "meaning",
        [
            (model._MEANING_COMPRESSED, None),  # set root meaning
            (model._MEANING_COMPRESSED, []),
            (model._MEANING_COMPRESSED, [1, 1]),
            (None, [model._MEANING_COMPRESSED] * 2),  # set sub-meanings
        ],
    )
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_repeated_to_uncompressed_tuple_meaning(
        self, meaning
    ):
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=False, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        compressed_value = [compressed_value_one, compressed_value_two]
        datastore_entity.update({"foo": compressed_value})
        meanings = {
            "foo": (
                meaning,
                compressed_value,
            )
        }
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == [uncompressed_value_one, uncompressed_value_two]

    @pytest.mark.skipif(
        [int(v) for v in datastore.__version__.split(".")] < [2, 20, 2],
        reason="uses meanings semantics from datastore v2.20.2 and later",
    )
    @pytest.mark.parametrize(
        "meaning",
        [
            (None, [model._MEANING_COMPRESSED, None]),
            (None, [model._MEANING_COMPRESSED, None, None]),
            (1, [model._MEANING_COMPRESSED, 1]),
            (None, [model._MEANING_COMPRESSED]),
        ],
    )
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_repeated_to_uncompressed_mixed_meaning(
        self, meaning
    ):
        """
        One item is compressed, one uncompressed
        """

        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=False, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        compressed_value = [compressed_value_one, compressed_value_two]
        datastore_entity.update({"foo": compressed_value})
        meanings = {
            "foo": (
                meaning,
                compressed_value,
            )
        }
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == [uncompressed_value_one, compressed_value_two]

    @pytest.mark.skipif(
        [int(v) for v in datastore.__version__.split(".")] < [2, 20, 2],
        reason="uses meanings semantics from datastore v2.20.2 and later",
    )
    @pytest.mark.parametrize(
        "meaning",
        [
            (None, None),
            (None, []),
            (None, [None]),
            (None, [None, None]),
            (1, []),
            (1, [1]),
            (1, [1, 1]),
        ],
    )
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_compressed_repeated_no_meaning(self, meaning):
        """
        could be uncompressed, but meaning not set
        """

        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=False, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        compressed_value = [compressed_value_one, compressed_value_two]
        datastore_entity.update({"foo": compressed_value})
        meanings = {
            "foo": (
                meaning,
                compressed_value,
            )
        }
        datastore_entity._meanings = meanings
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == [compressed_value_one, compressed_value_two]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_large_value_list():
        """
        try calling _from_datastore with a meaning list smaller than the value list
        """

        prop = model.BlobProperty(compressed=False, repeated=True, name="foo")

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        compressed_value = [
            model._BaseValue(compressed_value_one),
            model._BaseValue(compressed_value_two),
        ]
        datastore_entity.update({"foo": compressed_value})
        meanings = {
            "foo": (
                (None, [model._MEANING_COMPRESSED]),
                compressed_value,
            )
        }

        datastore_entity._meanings = meanings

        updated_value = prop._from_datastore(datastore_entity, compressed_value)
        assert len(updated_value) == 2
        assert updated_value[0].b_val == uncompressed_value_one
        # second value should remain compressed
        assert updated_value[1].b_val == compressed_value_two

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_uncompressed_to_uncompressed():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=False)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value = b"abc" * 1000
        datastore_entity.update({"foo": uncompressed_value})
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert entity.foo == uncompressed_value
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == uncompressed_value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_uncompressed_to_compressed():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value = b"abc" * 1000
        compressed_value = zlib.compress(uncompressed_value)
        datastore_entity.update({"foo": uncompressed_value})
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == compressed_value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__from_datastore_uncompressed_repeated_to_compressed():
        class ThisKind(model.Model):
            foo = model.BlobProperty(compressed=True, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        uncompressed_value_one = b"abc" * 1000
        compressed_value_one = zlib.compress(uncompressed_value_one)
        uncompressed_value_two = b"xyz" * 1000
        compressed_value_two = zlib.compress(uncompressed_value_two)
        datastore_entity.update(
            {"foo": [uncompressed_value_one, uncompressed_value_two]}
        )
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        ds_entity = model._entity_to_ds_entity(entity)
        assert ds_entity["foo"] == [compressed_value_one, compressed_value_two]


class TestCompressedTextProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.CompressedTextProperty()
        assert not prop._indexed
        assert prop._compressed

    @staticmethod
    def test_constructor_explicit():
        prop = model.CompressedTextProperty(name="text", indexed=False)
        assert prop._name == "text"
        assert not prop._indexed

    @staticmethod
    def test_constructor_not_allowed():
        with pytest.raises(NotImplementedError):
            model.CompressedTextProperty(indexed=True)

    @staticmethod
    def test_repr():
        prop = model.CompressedTextProperty(name="text")
        expected = "CompressedTextProperty('text')"
        assert repr(prop) == expected

    @staticmethod
    def test__validate():
        prop = model.CompressedTextProperty(name="text")
        assert prop._validate("abc") is None

    @staticmethod
    def test__validate_bad_bytes():
        prop = model.CompressedTextProperty(name="text")
        value = b"\x80abc"
        with pytest.raises(exceptions.BadValueError):
            prop._validate(value)

    @staticmethod
    def test__validate_bad_type():
        prop = model.CompressedTextProperty(name="text")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__to_base_type():
        prop = model.CompressedTextProperty(name="text")
        assert prop._to_base_type(b"abc") is None

    @staticmethod
    def test__to_base_type_converted():
        prop = model.CompressedTextProperty(name="text")
        value = b"\xe2\x98\x83"
        assert prop._to_base_type("\N{SNOWMAN}") == value

    @staticmethod
    def test__from_base_type():
        prop = model.CompressedTextProperty(name="text")
        assert prop._from_base_type("abc") is None

    @staticmethod
    def test__from_base_type_converted():
        prop = model.CompressedTextProperty(name="text")
        value = b"\xe2\x98\x83"
        assert prop._from_base_type(value) == "\N{SNOWMAN}"

    @staticmethod
    def test__from_base_type_cannot_convert():
        prop = model.CompressedTextProperty(name="text")
        value = b"\x80abc"
        assert prop._from_base_type(value) is None

    @staticmethod
    def test__db_set_uncompressed_meaning():
        prop = model.CompressedTextProperty(name="text")
        with pytest.raises(NotImplementedError):
            prop._db_set_uncompressed_meaning(None)


class TestTextProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.TextProperty()
        assert not prop._indexed

    @staticmethod
    def test_constructor_explicit():
        prop = model.TextProperty(name="text", indexed=False)
        assert prop._name == "text"
        assert not prop._indexed

    @staticmethod
    def test_constructor_not_allowed():
        with pytest.raises(NotImplementedError):
            model.TextProperty(indexed=True)

    @staticmethod
    def test_constructor_compressed():
        prop = model.TextProperty(compressed=True)
        assert isinstance(prop, model.CompressedTextProperty)

    @staticmethod
    def test_repr():
        prop = model.TextProperty(name="text")
        expected = "TextProperty('text')"
        assert repr(prop) == expected

    @staticmethod
    def test__validate():
        prop = model.TextProperty(name="text")
        assert prop._validate("abc") is None

    @staticmethod
    def test__validate_bad_bytes():
        prop = model.TextProperty(name="text")
        value = b"\x80abc"
        with pytest.raises(exceptions.BadValueError):
            prop._validate(value)

    @staticmethod
    def test__validate_bad_type():
        prop = model.TextProperty(name="text")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__to_base_type():
        prop = model.TextProperty(name="text")
        assert prop._to_base_type("abc") is None

    @staticmethod
    def test__to_base_type_converted():
        prop = model.TextProperty(name="text")
        value = "\N{SNOWMAN}"
        assert prop._to_base_type(b"\xe2\x98\x83") == value

    @staticmethod
    def test__from_base_type():
        prop = model.TextProperty(name="text")
        assert prop._from_base_type("abc") is None

    @staticmethod
    def test__from_base_type_converted():
        prop = model.TextProperty(name="text")
        value = b"\xe2\x98\x83"
        assert prop._from_base_type(value) == "\N{SNOWMAN}"

    @staticmethod
    def test__from_base_type_cannot_convert():
        prop = model.TextProperty(name="text")
        value = b"\x80abc"
        assert prop._from_base_type(value) is None

    @staticmethod
    def test__db_set_uncompressed_meaning():
        prop = model.TextProperty(name="text")
        with pytest.raises(NotImplementedError):
            prop._db_set_uncompressed_meaning(None)


class TestStringProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.StringProperty()
        assert prop._indexed

    @staticmethod
    def test_constructor_explicit():
        prop = model.StringProperty(name="limited-text", indexed=True)
        assert prop._name == "limited-text"
        assert prop._indexed

    @staticmethod
    def test_constructor_not_allowed():
        with pytest.raises(NotImplementedError):
            model.StringProperty(indexed=False)

    @staticmethod
    def test_repr():
        prop = model.StringProperty(name="limited-text")
        expected = "StringProperty('limited-text')"
        assert repr(prop) == expected

    @staticmethod
    def test__validate_bad_length():
        prop = model.StringProperty(name="limited-text")
        value = b"1" * 2000
        with pytest.raises(exceptions.BadValueError):
            prop._validate(value)


class TestGeoPtProperty:
    @staticmethod
    def test__validate():
        prop = model.GeoPtProperty(name="cartesian")
        value = model.GeoPt(0.0, 0.0)
        assert prop._validate(value) is None

    @staticmethod
    def test__validate_invalid():
        prop = model.GeoPtProperty(name="cartesian")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__db_set_value():
        prop = model.GeoPtProperty(name="cartesian")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.GeoPtProperty(name="cartesian")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)


class TestPickleProperty:
    UNPICKLED = ["a", {"b": "c"}, {"d", "e"}, (0xF, 0x10), 0x11]
    PICKLED = pickle.dumps(UNPICKLED, pickle.HIGHEST_PROTOCOL)

    def test__to_base_type(self):
        prop = model.PickleProperty(name="pkl")
        assert prop._to_base_type(self.UNPICKLED) == self.PICKLED

    def test__from_base_type(self):
        prop = model.PickleProperty(name="pkl")
        assert prop._from_base_type(self.PICKLED) == self.UNPICKLED

    @pytest.mark.usefixtures("in_context")
    def test__legacy_from_base_type(self):
        # GAE NDB stores pickled properties as bytes and with GAE NDB structures.
        # Validate we can unpickle to a Cloud NDB structure.
        # See https://github.com/googleapis/python-ndb/issues/587
        # TODO: This test fails as code will raise "_pickle.UnpicklingError: state is not a dictionary"
        gae_ndb_stored_value = b"\x80\x02cunit.models\nA\nq\x01)\x81q\x02URj#j\x0fs~crwilcox-testr\x05\x0b\x12\x01A\x0c\xa2\x01\x08UnitTestr\x11\x1a\tsome_prop \x00*\x02\x08\x01r\x15\x1a\x06source \x00*\t\x1a\x07gae 2.7\x82\x01\x00b."
        prop = model.PickleProperty(repeated=True)
        val = prop._from_base_type(gae_ndb_stored_value)
        expected = {"some_prop": 1, "source": "gae 2.7"}
        actual = val.to_dict()
        assert expected == actual


class TestJsonProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.JsonProperty()
        # Check that none of the constructor defaults were used.
        assert prop.__dict__ == {}

    @staticmethod
    def test_constructor_explicit():
        prop = model.JsonProperty(
            name="json-val",
            compressed=True,
            json_type=tuple,
            indexed=False,
            repeated=False,
            required=True,
            default=(),
            choices=((), ("b",), ("c", "d")),
            validator=TestProperty._example_validator,
            verbose_name="VALUE FOR READING",
            write_empty_list=False,
        )
        assert prop._name == "json-val"
        assert prop._compressed
        assert prop._json_type is tuple
        assert not prop._indexed
        assert not prop._repeated
        assert prop._required
        assert prop._default == ()
        assert prop._choices == frozenset([(), ("b",), ("c", "d")])
        assert prop._validator is TestProperty._example_validator
        assert prop._verbose_name == "VALUE FOR READING"
        assert not prop._write_empty_list

    @staticmethod
    def test__validate_no_type():
        prop = model.JsonProperty(name="json-val")
        assert prop._validate(b"any") is None

    @staticmethod
    def test__validate_correct_type():
        prop = model.JsonProperty(name="json-val", json_type=list)
        assert prop._validate([b"any", b"mini"]) is None

    @staticmethod
    def test__validate_incorrect_type():
        prop = model.JsonProperty(name="json-val", json_type=dict)
        with pytest.raises(TypeError):
            prop._validate(14)

    @staticmethod
    def test__to_base_type():
        prop = model.JsonProperty(name="json-val")
        value = [14, [15, 16], {"seventeen": 18}, "\N{SNOWMAN}"]
        expected = b'[14,[15,16],{"seventeen":18},"\\u2603"]'
        assert prop._to_base_type(value) == expected

    @staticmethod
    def test__from_base_type():
        prop = model.JsonProperty(name="json-val")
        value = b'[14,true,{"a":null,"b":"\\u2603"}]'
        expected = [14, True, {"a": None, "b": "\N{SNOWMAN}"}]
        assert prop._from_base_type(value) == expected

    @staticmethod
    def test__from_base_type_str():
        prop = model.JsonProperty(name="json-val")
        value = '[14,true,{"a":null,"b":"\\u2603"}]'
        expected = [14, True, {"a": None, "b": "\N{SNOWMAN}"}]
        assert prop._from_base_type(value) == expected


class TestUser:
    @staticmethod
    def test_constructor_defaults():
        with pytest.raises(ValueError):
            model.User()

    @staticmethod
    def _make_default():
        return model.User(email="foo@example.com", _auth_domain="example.com")

    def test_constructor_explicit(self):
        user_value = self._make_default()
        assert user_value._auth_domain == "example.com"
        assert user_value._email == "foo@example.com"
        assert user_value._user_id is None

    @staticmethod
    def test_constructor_no_email():
        with pytest.raises(model.UserNotFoundError):
            model.User(_auth_domain="example.com")
        with pytest.raises(model.UserNotFoundError):
            model.User(email="", _auth_domain="example.com")

    def test_nickname(self):
        user_value = self._make_default()
        assert user_value.nickname() == "foo"

    @staticmethod
    def test_nickname_mismatch_domain():
        user_value = model.User(email="foo@example.org", _auth_domain="example.com")
        assert user_value.nickname() == "foo@example.org"

    def test_email(self):
        user_value = self._make_default()
        assert user_value.email() == "foo@example.com"

    @staticmethod
    def test_user_id():
        user_value = model.User(
            email="foo@example.com", _auth_domain="example.com", _user_id="123"
        )
        assert user_value.user_id() == "123"

    def test_auth_domain(self):
        user_value = self._make_default()
        assert user_value.auth_domain() == "example.com"

    def test___str__(self):
        user_value = self._make_default()
        assert str(user_value) == "foo"

    def test___repr__(self):
        user_value = self._make_default()
        assert repr(user_value) == "users.User(email='foo@example.com')"

    @staticmethod
    def test___repr__with_user_id():
        user_value = model.User(
            email="foo@example.com", _auth_domain="example.com", _user_id="123"
        )
        expected = "users.User(email='foo@example.com', _user_id='123')"
        assert repr(user_value) == expected

    def test___hash__(self):
        user_value = self._make_default()
        expected = hash((user_value._email, user_value._auth_domain))
        assert hash(user_value) == expected

    def test___eq__(self):
        user_value1 = self._make_default()
        user_value2 = model.User(email="foo@example.org", _auth_domain="example.com")
        user_value3 = model.User(email="foo@example.com", _auth_domain="example.org")
        user_value4 = mock.sentinel.blob_key
        assert user_value1 == user_value1
        assert not user_value1 == user_value2
        assert not user_value1 == user_value3
        assert not user_value1 == user_value4

    def test___lt__(self):
        user_value1 = self._make_default()
        user_value2 = model.User(email="foo@example.org", _auth_domain="example.com")
        user_value3 = model.User(email="foo@example.com", _auth_domain="example.org")
        user_value4 = mock.sentinel.blob_key
        assert not user_value1 < user_value1
        assert user_value1 < user_value2
        assert user_value1 < user_value3
        with pytest.raises(TypeError):
            user_value1 < user_value4

    @staticmethod
    def test__from_ds_entity():
        assert model.User._from_ds_entity(
            {"email": "foo@example.com", "auth_domain": "gmail.com"}
        ) == model.User("foo@example.com", "gmail.com")

    @staticmethod
    def test__from_ds_entity_with_user_id():
        assert model.User._from_ds_entity(
            {
                "email": "foo@example.com",
                "auth_domain": "gmail.com",
                "user_id": "12345",
            }
        ) == model.User("foo@example.com", "gmail.com", "12345")


class TestUserProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.UserProperty()
        # Check that none of the constructor defaults were used.
        assert prop.__dict__ == {}

    @staticmethod
    def test_constructor_auto_current_user():
        with pytest.raises(NotImplementedError):
            model.UserProperty(auto_current_user=True)

    @staticmethod
    def test_constructor_auto_current_user_add():
        with pytest.raises(NotImplementedError):
            model.UserProperty(auto_current_user_add=True)

    @staticmethod
    def test__validate():
        prop = model.UserProperty(name="u")
        user_value = model.User(email="foo@example.com", _auth_domain="example.com")
        assert prop._validate(user_value) is None

    @staticmethod
    def test__validate_invalid():
        prop = model.UserProperty(name="u")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__prepare_for_put():
        prop = model.UserProperty(name="u")
        assert prop._prepare_for_put(None) is None

    @staticmethod
    def test__db_set_value():
        prop = model.UserProperty(name="u")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.UserProperty(name="u")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)

    @staticmethod
    def test__to_base_type():
        prop = model.UserProperty(name="u")
        entity = prop._to_base_type(
            model.User(
                "email",
                "auth_domain",
            )
        )
        assert entity["email"] == "email"
        assert "email" in entity.exclude_from_indexes
        assert entity["auth_domain"] == "auth_domain"
        assert "auth_domain" in entity.exclude_from_indexes
        assert "user_id" not in entity

    @staticmethod
    def test__to_base_type_w_user_id():
        prop = model.UserProperty(name="u")
        entity = prop._to_base_type(model.User("email", "auth_domain", "user_id"))
        assert entity["email"] == "email"
        assert "email" in entity.exclude_from_indexes
        assert entity["auth_domain"] == "auth_domain"
        assert "auth_domain" in entity.exclude_from_indexes
        assert entity["user_id"] == "user_id"
        assert "user_id" in entity.exclude_from_indexes

    @staticmethod
    def test__from_base_type():
        prop = model.UserProperty(name="u")
        assert prop._from_base_type(
            {"email": "email", "auth_domain": "auth_domain"}
        ) == model.User("email", "auth_domain")

    @staticmethod
    def test__to_datastore():
        class SomeKind(model.Model):
            u = model.UserProperty()

        entity = SomeKind(u=model.User("email", "auth_domain"))
        data = {}
        SomeKind.u._to_datastore(entity, data)
        meaning, ds_entity = data["_meanings"]["u"]
        assert meaning == model._MEANING_PREDEFINED_ENTITY_USER
        assert data["u"] == ds_entity

    @staticmethod
    def test__to_datastore_no_value():
        class SomeKind(model.Model):
            u = model.UserProperty()

        entity = SomeKind()
        data = {}
        SomeKind.u._to_datastore(entity, data)
        assert data == {"u": None}


class TestKeyProperty:
    @staticmethod
    def test_constructor_defaults():
        prop = model.KeyProperty()
        # Check that none of the constructor defaults were used.
        assert prop.__dict__ == {}

    @staticmethod
    def test_constructor_too_many_positional():
        with pytest.raises(TypeError):
            model.KeyProperty("a", None, None)

    @staticmethod
    def test_constructor_positional_name_twice():
        with pytest.raises(TypeError):
            model.KeyProperty("a", "b")

    @staticmethod
    def test_constructor_positional_kind_twice():
        class Simple(model.Model):
            pass

        with pytest.raises(TypeError):
            model.KeyProperty(Simple, Simple)

    @staticmethod
    def test_constructor_positional_bad_type():
        with pytest.raises(TypeError):
            model.KeyProperty("a", mock.sentinel.bad)

    @staticmethod
    def test_constructor_name_both_ways():
        with pytest.raises(TypeError):
            model.KeyProperty("a", name="b")

    @staticmethod
    def test_constructor_kind_both_ways():
        class Simple(model.Model):
            pass

        with pytest.raises(TypeError):
            model.KeyProperty(Simple, kind="Simple")

    @staticmethod
    def test_constructor_bad_kind():
        with pytest.raises(TypeError):
            model.KeyProperty(kind=mock.sentinel.bad)

    @staticmethod
    def test_constructor_positional():
        class Simple(model.Model):
            pass

        prop = model.KeyProperty(None, None)
        assert prop._name is None
        assert prop._kind is None

        name_only_args = [("keyp",), (None, "keyp"), ("keyp", None)]
        for args in name_only_args:
            prop = model.KeyProperty(*args)
            assert prop._name == "keyp"
            assert prop._kind is None

        kind_only_args = [(Simple,), (None, Simple), (Simple, None)]
        for args in kind_only_args:
            prop = model.KeyProperty(*args)
            assert prop._name is None
            assert prop._kind == "Simple"

        both_args = [("keyp", Simple), (Simple, "keyp")]
        for args in both_args:
            prop = model.KeyProperty(*args)
            assert prop._name == "keyp"
            assert prop._kind == "Simple"

    @staticmethod
    def test_constructor_hybrid():
        class Simple(model.Model):
            pass

        # prop1 will get a TypeError due to Python 2.7 compatibility
        # prop1 = model.KeyProperty(Simple, name="keyp")
        prop2 = model.KeyProperty("keyp", kind=Simple)
        prop3 = model.KeyProperty("keyp", kind="Simple")
        for prop in (prop2, prop3):
            assert prop._name == "keyp"
            assert prop._kind == "Simple"

    @staticmethod
    def test_repr():
        prop = model.KeyProperty("keyp", kind="Simple", repeated=True)
        expected = "KeyProperty('keyp', kind='Simple', repeated=True)"
        assert repr(prop) == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__validate():
        kind = "Simple"
        prop = model.KeyProperty("keyp", kind=kind)
        value = key_module.Key(kind, 182983)
        assert prop._validate(value) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__validate_without_kind():
        prop = model.KeyProperty("keyp")
        value = key_module.Key("Foo", "Bar")
        assert prop._validate(value) is None

    @staticmethod
    def test__validate_non_key():
        prop = model.KeyProperty("keyp")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__validate_partial_key():
        prop = model.KeyProperty("keyp")
        value = key_module.Key("Kynd", None)
        with pytest.raises(exceptions.BadValueError):
            prop._validate(value)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__validate_wrong_kind():
        prop = model.KeyProperty("keyp", kind="Simple")
        value = key_module.Key("Kynd", 184939)
        with pytest.raises(exceptions.BadValueError):
            prop._validate(value)

    @staticmethod
    def test__db_set_value():
        prop = model.KeyProperty("keyp", kind="Simple")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.KeyProperty("keyp", kind="Simple")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_base_type():
        prop = model.KeyProperty("keyp")
        value = key_module.Key("Kynd", 123)
        assert prop._to_base_type(value) is value._key

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_base_type_wrong_type():
        prop = model.KeyProperty("keyp")
        value = ("Kynd", 123)
        with pytest.raises(TypeError):
            assert prop._to_base_type(value) is value._key

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__from_base_type():
        prop = model.KeyProperty("keyp")
        ds_value = ds_key_module.Key("Kynd", 123, project="testing")
        value = prop._from_base_type(ds_value)
        assert value.kind() == "Kynd"
        assert value.id() == 123

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_equality():
        class KeyPropTestModel(model.Model):
            k = model.KeyProperty()

        kptm1 = KeyPropTestModel(k=key_module.Key("k", 1))
        kptm2 = KeyPropTestModel(k=key_module.Key("k", 1, database=""))
        assert kptm1 == kptm2


class TestBlobKeyProperty:
    @staticmethod
    def test__validate():
        prop = model.BlobKeyProperty(name="object-gcs")
        value = model.BlobKey(b"abc")
        assert prop._validate(value) is None

    @staticmethod
    def test__validate_invalid():
        prop = model.BlobKeyProperty(name="object-gcs")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__db_set_value():
        prop = model.BlobKeyProperty(name="object-gcs")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.BlobKeyProperty(name="object-gcs")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)


class TestDateTimeProperty:
    @staticmethod
    def _string_validator(prop, value):
        return datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def test_constructor_defaults():
        prop = model.DateTimeProperty()
        # Check that none of the constructor defaults were used.
        assert prop.__dict__ == {}

    @staticmethod
    def test_constructor_explicit():
        now = datetime.datetime.utcnow()
        prop = model.DateTimeProperty(
            name="dt_val",
            auto_now=True,
            auto_now_add=False,
            tzinfo=timezone(-4),
            indexed=False,
            repeated=False,
            required=True,
            default=now,
            validator=TestDateTimeProperty._string_validator,
            verbose_name="VALUE FOR READING",
            write_empty_list=False,
        )
        assert prop._name == "dt_val"
        assert prop._auto_now
        assert not prop._auto_now_add
        assert prop._tzinfo == timezone(-4)
        assert not prop._indexed
        assert not prop._repeated
        assert prop._required
        assert prop._default == now
        assert prop._choices is None
        assert prop._validator is TestDateTimeProperty._string_validator
        assert prop._verbose_name == "VALUE FOR READING"
        assert not prop._write_empty_list

    @staticmethod
    def test_constructor_repeated():
        with pytest.raises(ValueError):
            model.DateTimeProperty(name="dt_val", auto_now=True, repeated=True)
        with pytest.raises(ValueError):
            model.DateTimeProperty(name="dt_val", auto_now_add=True, repeated=True)

        prop = model.DateTimeProperty(name="dt_val", repeated=True)
        assert prop._repeated

    @staticmethod
    def test__validate():
        prop = model.DateTimeProperty(name="dt_val")
        value = datetime.datetime.utcnow()
        assert prop._validate(value) is None

    @staticmethod
    def test__do_validate_with_validator():
        prop = model.DateTimeProperty(
            name="dt_val", validator=TestDateTimeProperty._string_validator
        )
        value = "2020-08-08 12:53:54"
        # validator must be called first to convert to datetime
        assert prop._do_validate(value) == datetime.datetime(2020, 8, 8, 12, 53, 54)

    @staticmethod
    def test__validate_invalid():
        prop = model.DateTimeProperty(name="dt_val")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__validate_with_tz():
        prop = model.DateTimeProperty(name="dt_val")
        value = datetime.datetime.now(tz=pytz.utc)
        with pytest.raises(exceptions.BadValueError):
            prop._validate(value)

    @staticmethod
    def test__now():
        dt_val = model.DateTimeProperty._now()
        assert isinstance(dt_val, datetime.datetime)

    @staticmethod
    def test__prepare_for_put():
        prop = model.DateTimeProperty(name="dt_val")
        entity = mock.Mock(_values={}, spec=("_values",))

        with mock.patch.object(prop, "_now") as _now:
            prop._prepare_for_put(entity)
        assert entity._values == {}
        _now.assert_not_called()

    @staticmethod
    def test__prepare_for_put_auto_now():
        prop = model.DateTimeProperty(name="dt_val", auto_now=True)
        values1 = {}
        values2 = {prop._name: mock.sentinel.dt}
        for values in (values1, values2):
            entity = mock.Mock(_values=values, spec=("_values",))

            with mock.patch.object(prop, "_now") as _now:
                prop._prepare_for_put(entity)
            assert entity._values == {prop._name: _now.return_value}
            _now.assert_called_once_with()

    @staticmethod
    def test__prepare_for_put_auto_now_add():
        prop = model.DateTimeProperty(name="dt_val", auto_now_add=True)
        values1 = {}
        values2 = {prop._name: mock.sentinel.dt}
        for values in (values1, values2):
            entity = mock.Mock(_values=values.copy(), spec=("_values",))

            with mock.patch.object(prop, "_now") as _now:
                prop._prepare_for_put(entity)
            if values:
                assert entity._values == values
                _now.assert_not_called()
            else:
                assert entity._values != values
                assert entity._values == {prop._name: _now.return_value}
                _now.assert_called_once_with()

    @staticmethod
    def test__db_set_value():
        prop = model.DateTimeProperty(name="dt_val")
        with pytest.raises(NotImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__db_get_value():
        prop = model.DateTimeProperty(name="dt_val")
        with pytest.raises(NotImplementedError):
            prop._db_get_value(None, None)

    @staticmethod
    def test__from_base_type_no_timezone():
        prop = model.DateTimeProperty(name="dt_val")
        value = datetime.datetime.now()
        assert prop._from_base_type(value) is None

    @staticmethod
    def test__from_base_type_timezone():
        prop = model.DateTimeProperty(name="dt_val")
        value = datetime.datetime(2010, 5, 12, tzinfo=pytz.utc)
        assert prop._from_base_type(value) == datetime.datetime(2010, 5, 12)

    @staticmethod
    def test__from_base_type_convert_timezone():
        prop = model.DateTimeProperty(name="dt_val", tzinfo=timezone(-4))
        value = datetime.datetime(2010, 5, 12, tzinfo=pytz.utc)
        assert prop._from_base_type(value) == datetime.datetime(
            2010, 5, 11, 20, tzinfo=timezone(-4)
        )

    @staticmethod
    def test__from_base_type_naive_with_timezone():
        prop = model.DateTimeProperty(name="dt_val", tzinfo=timezone(-4))
        value = datetime.datetime(2010, 5, 12)
        assert prop._from_base_type(value) == datetime.datetime(
            2010, 5, 11, 20, tzinfo=timezone(-4)
        )

    @staticmethod
    def test__from_base_type_int():
        prop = model.DateTimeProperty(name="dt_val")
        value = 1273632120000000
        assert prop._from_base_type(value) == datetime.datetime(2010, 5, 12, 2, 42)

    @staticmethod
    def test__to_base_type_noop():
        prop = model.DateTimeProperty(name="dt_val", tzinfo=timezone(-4))
        value = datetime.datetime(2010, 5, 12)
        assert prop._to_base_type(value) is None

    @staticmethod
    def test__to_base_type_convert_to_utc():
        prop = model.DateTimeProperty(name="dt_val", tzinfo=timezone(-4))
        value = datetime.datetime(2010, 5, 12, tzinfo=timezone(-4))
        assert prop._to_base_type(value) == datetime.datetime(
            2010, 5, 12, 4, tzinfo=pytz.utc
        )


class TestDateProperty:
    @staticmethod
    def test__validate():
        prop = model.DateProperty(name="d_val")
        value = datetime.datetime.utcnow().date()
        assert prop._validate(value) is None

    @staticmethod
    def test__validate_invalid():
        prop = model.DateProperty(name="d_val")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__now():
        d_val = model.DateProperty._now()
        assert isinstance(d_val, datetime.date)

    def test__to_base_type(self):
        prop = model.DateProperty(name="d_val")
        value = datetime.date(2014, 10, 7)
        expected = datetime.datetime(2014, 10, 7)
        assert prop._to_base_type(value) == expected

    def test__to_base_type_invalid(self):
        prop = model.DateProperty(name="d_val")
        with pytest.raises(TypeError):
            prop._to_base_type(None)

    def test__from_base_type(self):
        prop = model.DateProperty(name="d_val")
        value = datetime.datetime(2014, 10, 7)
        expected = datetime.date(2014, 10, 7)
        assert prop._from_base_type(value) == expected


class TestTimeProperty:
    @staticmethod
    def test__validate():
        prop = model.TimeProperty(name="t_val")
        value = datetime.datetime.utcnow().time()
        assert prop._validate(value) is None

    @staticmethod
    def test__validate_invalid():
        prop = model.TimeProperty(name="t_val")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__now():
        t_val = model.TimeProperty._now()
        assert isinstance(t_val, datetime.time)

    def test__to_base_type(self):
        prop = model.TimeProperty(name="t_val")
        value = datetime.time(17, 57, 18, 453529)
        expected = datetime.datetime(1970, 1, 1, 17, 57, 18, 453529)
        assert prop._to_base_type(value) == expected

    def test__to_base_type_invalid(self):
        prop = model.TimeProperty(name="t_val")
        with pytest.raises(TypeError):
            prop._to_base_type(None)

    def test__from_base_type(self):
        prop = model.TimeProperty(name="t_val")
        value = datetime.datetime(1970, 1, 1, 1, 15, 59, 900101)
        expected = datetime.time(1, 15, 59, 900101)
        assert prop._from_base_type(value) == expected


class TestStructuredProperty:
    @staticmethod
    def test_constructor():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        assert prop._model_class == Mine

    @staticmethod
    def test_constructor_with_repeated():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine, repeated=True)
        assert prop._model_class == Mine

    @staticmethod
    def test_constructor_with_repeated_prop():
        class Mine(model.Model):
            foo = model.StringProperty(repeated=True)

        with pytest.raises(TypeError):
            model.StructuredProperty(Mine, repeated=True)

    @staticmethod
    def test__validate():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        instance = Mine()
        assert prop._validate(instance) is None

    @staticmethod
    def test__validate_with_dict():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        assert isinstance(prop._validate({}), Mine)

    @staticmethod
    def test__validate_invalid():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        with pytest.raises(exceptions.BadValueError):
            prop._validate(None)

    @staticmethod
    def test__get_value():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        mine = Mine()
        minetoo = MineToo()
        minetoo.bar = mine
        assert MineToo.bar._get_value(minetoo) == mine

    @staticmethod
    def test__get_value_unprojected():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        minetoo = MineToo(projection=("saywhat",))
        with pytest.raises(model.UnprojectedPropertyError):
            MineToo.bar._get_value(minetoo)

    @staticmethod
    def test__get_for_dict():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        mine = Mine(foo="Foo")
        minetoo = MineToo()
        minetoo.bar = mine
        assert MineToo.bar._get_for_dict(minetoo) == {"foo": "Foo"}

    @staticmethod
    def test__get_for_dict_repeated():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine, repeated=True)

        mine = Mine(foo="Foo")
        minetoo = MineToo()
        minetoo.bar = [mine, mine]
        assert MineToo.bar._get_for_dict(minetoo) == [
            {"foo": "Foo"},
            {"foo": "Foo"},
        ]

    @staticmethod
    def test__get_for_dict_no_value():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        minetoo = MineToo()
        minetoo.bar = None
        assert MineToo.bar._get_for_dict(minetoo) is None

    @staticmethod
    def test___getattr__():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "bar"
        assert isinstance(prop.foo, model.StringProperty)
        assert prop.foo._name == "bar.foo"

    @staticmethod
    def test___getattr__use_codename():
        class Mine(model.Model):
            foo = model.StringProperty("notfoo")

        prop = model.StructuredProperty(Mine)
        prop._name = "bar"
        assert isinstance(prop.foo, model.StringProperty)
        assert prop.foo._name == "bar.notfoo"

    @staticmethod
    def test___getattr___bad_prop():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        with pytest.raises(AttributeError):
            prop.baz

    @staticmethod
    def test__comparison_eq():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "bar"
        mine = Mine(foo="baz")
        assert prop._comparison("=", mine) == query_module.FilterNode(
            "bar.foo", "=", "baz"
        )

    @staticmethod
    def test__comparison_other():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        mine = Mine(foo="baz")
        with pytest.raises(exceptions.BadFilterError):
            prop._comparison(">", mine)

    @staticmethod
    def test__comparison_not_indexed():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine, indexed=False)
        mine = Mine(foo="baz")
        with pytest.raises(exceptions.BadFilterError):
            prop._comparison("=", mine)

    @staticmethod
    def test__comparison_value_none():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "bar"
        assert prop._comparison("=", None) == query_module.FilterNode("bar", "=", None)

    @staticmethod
    def test__comparison_repeated():
        class Mine(model.Model):
            foo = model.StringProperty(repeated=True)
            bar = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "baz"
        mine = Mine(bar="x")
        assert prop._comparison("=", mine) == query_module.FilterNode(
            "baz.bar", "=", "x"
        )

    @staticmethod
    def test__comparison_repeated_no_filters():
        class Mine(model.Model):
            foo = model.StringProperty(repeated=True)

        prop = model.StructuredProperty(Mine)
        prop._name = "bar"
        mine = Mine(foo=[])
        with pytest.raises(exceptions.BadFilterError):
            prop._comparison("=", mine)

    @staticmethod
    def test__comparison_repeated_non_empty():
        class Mine(model.Model):
            foo = model.StringProperty(repeated=True)

        prop = model.StructuredProperty(Mine)
        prop._name = "bar"
        mine = Mine(foo=["baz"])
        with pytest.raises(exceptions.BadFilterError):
            prop._comparison("=", mine)

    @staticmethod
    def test__comparison_repeated_empty():
        class Mine(model.Model):
            foo = model.StringProperty(repeated=True)

        prop = model.StructuredProperty(Mine)
        prop._name = "bar"
        mine = Mine(foo=[])
        with pytest.raises(exceptions.BadFilterError):
            prop._comparison("=", mine)

    @staticmethod
    def test__comparison_multiple():
        class Mine(model.Model):
            foo = model.StringProperty()
            bar = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "baz"
        mine = Mine(foo="x", bar="y")
        comparison = prop._comparison("=", mine)
        compared = query_module.AND(
            query_module.FilterNode("baz.bar", "=", "y"),
            query_module.FilterNode("baz.foo", "=", "x"),
        )
        # Sort them and test each one is in both lists.
        assert all(  # pragma: NO BRANCH
            [
                a == b
                for a, b in zip(
                    sorted(comparison._nodes, key=lambda a: a._name),
                    sorted(compared._nodes, key=lambda a: a._name),
                )
            ]
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__comparison_repeated_structured():
        class Mine(model.Model):
            foo = model.StringProperty()
            bar = model.StringProperty()

        prop = model.StructuredProperty(Mine, repeated=True)
        prop._name = "bar"
        mine = Mine(foo="x", bar="y")
        conjunction = prop._comparison("=", mine)
        # Sort them before making any comparisons.
        conjunction_nodes = sorted(
            conjunction._nodes, key=lambda a: getattr(a, "_name", "z")
        )
        assert conjunction_nodes[0] == query_module.FilterNode("bar.bar", "=", "y")
        assert conjunction_nodes[1] == query_module.FilterNode("bar.foo", "=", "x")
        assert conjunction_nodes[2].predicate.name == "bar"
        assert sorted(conjunction_nodes[2].predicate.match_keys) == [
            "bar",
            "foo",
        ]
        match_values = sorted(
            conjunction_nodes[2].predicate.match_values,
            key=lambda a: a.string_value,
        )
        assert match_values[0].string_value == "x"
        assert match_values[1].string_value == "y"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_IN():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "baz"
        mine = Mine(foo="x")
        minetoo = Mine(foo="y")
        assert prop.IN([mine, minetoo]) == query_module.OR(
            query_module.FilterNode("baz.foo", "=", "x"),
            query_module.FilterNode("baz.foo", "=", "y"),
        )

    @staticmethod
    def test_IN_no_value():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "baz"
        assert prop.IN([]) == query_module.FalseNode()

    @staticmethod
    def test_IN_bad_value():
        class Mine(model.Model):
            foo = model.StringProperty()

        prop = model.StructuredProperty(Mine)
        prop._name = "baz"
        with pytest.raises(exceptions.BadArgumentError):
            prop.IN(None)

    @staticmethod
    def test__has_value():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        mine = Mine(foo="Foo")
        minetoo = MineToo(bar=mine)
        assert MineToo.bar._has_value(minetoo) is True

    @staticmethod
    def test__has_value_with_rest():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        mine = Mine(foo="Foo")
        minetoo = MineToo(bar=mine)
        assert MineToo.bar._has_value(minetoo, rest=["foo"]) is True

    @staticmethod
    def test__has_value_with_rest_subent_none():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        minetoo = MineToo(bar=None)
        assert MineToo.bar._has_value(minetoo, rest=["foo"]) is True

    @staticmethod
    def test__has_value_with_rest_repeated_one():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine, repeated=True)

        mine = Mine(foo="x")
        minetoo = MineToo(bar=[mine])
        assert MineToo.bar._has_value(minetoo, rest=["foo"]) is True

    @staticmethod
    def test__has_value_with_rest_repeated_two():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine, repeated=True)

        mine = Mine(foo="x")
        mine2 = Mine(foo="y")
        minetoo = MineToo(bar=[mine, mine2])
        with pytest.raises(RuntimeError):
            MineToo.bar._has_value(minetoo, rest=["foo"])

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__has_value_with_rest_subprop_none():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        mine = Mine(foo="Foo")
        minetoo = MineToo(bar=mine)
        assert MineToo.bar._has_value(minetoo, rest=[None]) is False

    @staticmethod
    def test__check_property():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        assert MineToo.bar._check_property("foo") is None

    @staticmethod
    def test__check_property_with_sub():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        class MineThree(model.Model):
            baz = model.StructuredProperty(MineToo)

        assert MineThree.baz._check_property("bar.foo") is None

    @staticmethod
    def test__check_property_invalid():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        with pytest.raises(model.InvalidPropertyError):
            MineToo.bar._check_property("baz")

    @staticmethod
    def test__check_property_no_rest():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        with pytest.raises(model.InvalidPropertyError):
            MineToo.bar._check_property()

    @staticmethod
    def test__get_value_size():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        mine = Mine(foo="Foo")
        minetoo = MineToo(bar=mine)
        assert MineToo.bar._get_value_size(minetoo) == 1

    @staticmethod
    def test__get_value_size_list():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine, repeated=True)

        mine = Mine(foo="Foo")
        minetoo = MineToo(bar=[mine])
        assert MineToo.bar._get_value_size(minetoo) == 1

    @staticmethod
    def test__get_value_size_none():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        minetoo = MineToo(bar=None)
        assert MineToo.bar._get_value_size(minetoo) == 0

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_base_type():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        minetoo = MineToo(bar=Mine(foo="bar"))
        ds_bar = MineToo.bar._to_base_type(minetoo.bar)
        assert isinstance(ds_bar, entity_module.Entity)
        assert ds_bar["foo"] == "bar"
        assert ds_bar.key is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_base_type_bad_value():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.StructuredProperty(Mine)

        with pytest.raises(TypeError):
            MineToo.bar._to_base_type("badvalue")

    def test__from_base_type(self):
        class Simple(model.Model):
            pass

        prop = model.StructuredProperty(Simple, name="ent")
        entity = entity_module.Entity()
        expected = Simple()
        assert prop._from_base_type(entity) == expected

    def test__from_base_type_noop(self):
        class Simple(model.Model):
            pass

        prop = model.StructuredProperty(Simple, name="ent")
        value = object()
        assert prop._from_base_type(value) is value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__to_datastore_non_legacy():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind)

        entity = SomeKind(foo=SubKind(bar="baz"))
        data = {}
        assert SomeKind.foo._to_datastore(entity, data) == ("foo",)
        assert len(data) == 1
        assert dict(data["foo"]) == {"bar": "baz"}

    @staticmethod
    def test__to_datastore_legacy(in_context):
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind)

        with in_context.new(legacy_data=True).use():
            entity = SomeKind(foo=SubKind(bar="baz"))
            data = {}
            assert SomeKind.foo._to_datastore(entity, data) == {"foo.bar"}
            assert data == {"foo.bar": "baz"}

    @staticmethod
    def test__to_datastore_legacy_subentity_is_None(in_context):
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind)

        with in_context.new(legacy_data=True).use():
            entity = SomeKind()
            data = {}
            assert SomeKind.foo._to_datastore(entity, data) == {"foo"}
            assert data == {"foo": None}

    @staticmethod
    def test__to_datastore_legacy_subentity_is_unindexed(in_context):
        class SubKind(model.Model):
            bar = model.BlobProperty(indexed=False)

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind)

        with in_context.new(legacy_data=True).use():
            entity = SomeKind(foo=SubKind())
            data = {"_exclude_from_indexes": []}
            assert SomeKind.foo._to_datastore(entity, data) == {"foo.bar"}
            assert data.pop("_exclude_from_indexes") == ["foo.bar"]
            assert data == {"foo.bar": None}

    @staticmethod
    def test__to_datastore_legacy_repeated(in_context):
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind, repeated=True)

        with in_context.new(legacy_data=True).use():
            entity = SomeKind(foo=[SubKind(bar="baz"), SubKind(bar="boz")])
            data = {}
            assert SomeKind.foo._to_datastore(entity, data) == {"foo.bar"}
            assert data == {"foo.bar": ["baz", "boz"]}

    @staticmethod
    def test__to_datastore_legacy_repeated_empty_value(in_context):
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind, repeated=True)

        with in_context.new(legacy_data=True).use():
            entity = SomeKind(foo=[])
            data = {}
            assert SomeKind.foo._to_datastore(entity, data) == set()
            assert data == {}

    @staticmethod
    def test__prepare_for_put():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind)

        entity = SomeKind(foo=SubKind())
        entity.foo._prepare_for_put = mock.Mock()
        SomeKind.foo._prepare_for_put(entity)
        entity.foo._prepare_for_put.assert_called_once_with()

    @staticmethod
    def test__prepare_for_put_repeated():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind, repeated=True)

        entity = SomeKind(foo=[SubKind(), SubKind()])
        entity.foo[0]._prepare_for_put = mock.Mock()
        entity.foo[1]._prepare_for_put = mock.Mock()
        SomeKind.foo._prepare_for_put(entity)
        entity.foo[0]._prepare_for_put.assert_called_once_with()
        entity.foo[1]._prepare_for_put.assert_called_once_with()

    @staticmethod
    def test__prepare_for_put_repeated_None():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(SubKind)

        entity = SomeKind()
        SomeKind.foo._prepare_for_put(entity)  # noop


class TestLocalStructuredProperty:
    @staticmethod
    def test_constructor_indexed():
        class Simple(model.Model):
            pass

        with pytest.raises(NotImplementedError):
            model.LocalStructuredProperty(Simple, name="ent", indexed=True)

    @staticmethod
    def test__validate():
        class Simple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        value = Simple()
        assert prop._validate(value) is None

    @staticmethod
    def test__validate_invalid():
        class Simple(model.Model):
            pass

        class NotSimple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        with pytest.raises(exceptions.BadValueError):
            prop._validate(NotSimple())

    @staticmethod
    def test__validate_dict():
        class Simple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        value = {}
        assert isinstance(prop._validate(value), Simple)

    @staticmethod
    def test__validate_dict_invalid():
        class Simple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        with pytest.raises(exceptions.BadValueError):
            prop._validate({"key": "value"})

    @pytest.mark.usefixtures("in_context")
    def test__to_base_type(self):
        class Simple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        value = Simple()
        entity = entity_module.Entity()
        pb = helpers.entity_to_protobuf(entity)._pb
        expected = pb.SerializePartialToString()
        assert prop._to_base_type(value) == expected

    @pytest.mark.usefixtures("in_context")
    def test__to_base_type_invalid(self):
        class Simple(model.Model):
            pass

        class NotSimple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        with pytest.raises(TypeError):
            prop._to_base_type(NotSimple())

    def test__from_base_type(self):
        class Simple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        entity = entity_module.Entity()
        expected = Simple()
        assert prop._from_base_type(entity) == expected

    def test__from_base_type_bytes(self):
        class Simple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        pb = helpers.entity_to_protobuf(entity_module.Entity())._pb
        value = pb.SerializePartialToString()
        expected = Simple()
        assert prop._from_base_type(value) == expected

    def test__from_base_type_keep_keys(self):
        class Simple(model.Model):
            pass

        prop = model.LocalStructuredProperty(Simple, name="ent")
        entity = entity_module.Entity()
        entity.key = "key"
        expected = Simple()
        assert prop._from_base_type(entity) == expected

    @staticmethod
    def test__prepare_for_put():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.LocalStructuredProperty(SubKind)

        entity = SomeKind(foo=SubKind())
        entity.foo._prepare_for_put = mock.Mock()
        SomeKind.foo._prepare_for_put(entity)
        entity.foo._prepare_for_put.assert_called_once_with()

    @staticmethod
    def test__prepare_for_put_repeated():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.LocalStructuredProperty(SubKind, repeated=True)

        entity = SomeKind(foo=[SubKind(), SubKind()])
        entity.foo[0]._prepare_for_put = mock.Mock()
        entity.foo[1]._prepare_for_put = mock.Mock()
        SomeKind.foo._prepare_for_put(entity)
        entity.foo[0]._prepare_for_put.assert_called_once_with()
        entity.foo[1]._prepare_for_put.assert_called_once_with()

    @staticmethod
    def test__prepare_for_put_repeated_None():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.LocalStructuredProperty(SubKind)

        entity = SomeKind()
        SomeKind.foo._prepare_for_put(entity)  # noop

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_repeated_local_structured_property():
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.LocalStructuredProperty(SubKind, repeated=True, indexed=False)

        entity = SomeKind(foo=[SubKind(bar="baz")])
        data = {"_exclude_from_indexes": []}
        protobuf = model._entity_to_protobuf(entity.foo[0], set_key=False)._pb
        protobuf = protobuf.SerializePartialToString()
        assert SomeKind.foo._to_datastore(entity, data, repeated=True) == ("foo",)
        assert data.pop("_exclude_from_indexes") == ["foo"]
        assert data == {"foo": [[protobuf]]}

    @staticmethod
    def test_legacy_repeated_local_structured_property(in_context):
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.LocalStructuredProperty(SubKind, repeated=True, indexed=False)

        with in_context.new(legacy_data=True).use():
            entity = SomeKind(foo=[SubKind(bar="baz")])
            data = {"_exclude_from_indexes": []}
            ds_entity = model._entity_to_ds_entity(entity.foo[0], set_key=False)
            assert SomeKind.foo._to_datastore(entity, data, repeated=True) == ("foo",)
            assert data.pop("_exclude_from_indexes") == ["foo"]
            assert data == {"foo": [ds_entity]}

    @staticmethod
    def test_legacy_non_repeated_local_structured_property(in_context):
        class SubKind(model.Model):
            bar = model.Property()

        class SomeKind(model.Model):
            foo = model.LocalStructuredProperty(SubKind)

        with in_context.new(legacy_data=True).use():
            entity = SomeKind(foo=SubKind(bar="baz"))
            data = {"_exclude_from_indexes": []}
            assert SomeKind.foo._to_datastore(entity, data) == ("foo",)
            assert data.pop("_exclude_from_indexes") == ["foo"]
            ds_entity = model._entity_to_ds_entity(entity.foo, set_key=False)
            assert data == {"foo": ds_entity}

    @staticmethod
    def test_legacy_repeated_compressed_local_structured_property():
        class SubKind(model.Model):
            bar = model.TextProperty()

        prop = model.LocalStructuredProperty(SubKind, repeated=True, compressed=True)
        entity = SubKind(bar="baz")
        ds_entity = model._entity_to_ds_entity(entity, set_key=False)
        assert prop._call_from_base_type(ds_entity) == entity

    @staticmethod
    def test_legacy_compressed_entity_local_structured_property():
        class SubKind(model.Model):
            foo = model.StringProperty()
            bar = model.StringProperty()
            baz = model.StringProperty()

        prop = model.LocalStructuredProperty(SubKind, repeated=True, compressed=True)
        entity = SubKind(foo="so", bar="much", baz="code")
        compressed = b"".join(
            [
                b"x\x9c+\xe2\x95bN\xcb\xcfW`\xd0b\x91b*\xce",
                b"/\xe2\x97bNJ,\x02r\xd9\xa4XrK\x933 \x02U\x10",
                b"\x81\xe4\xfc\x94T\x00\x08\xe1\n\xff",
            ]
        )

        assert prop._call_from_base_type(compressed) == entity

    @staticmethod
    def test__get_for_dict():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.LocalStructuredProperty(Mine)

        mine = Mine(foo="Foo")
        minetoo = MineToo()
        minetoo.bar = mine
        assert MineToo.bar._get_for_dict(minetoo) == {"foo": "Foo"}

    @staticmethod
    def test__get_for_dict_repeated():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.LocalStructuredProperty(Mine, repeated=True)

        mine = Mine(foo="Foo")
        minetoo = MineToo()
        minetoo.bar = [mine, mine]
        assert MineToo.bar._get_for_dict(minetoo) == [
            {"foo": "Foo"},
            {"foo": "Foo"},
        ]

    @staticmethod
    def test__get_for_dict_no_value():
        class Mine(model.Model):
            foo = model.StringProperty()

        class MineToo(model.Model):
            bar = model.LocalStructuredProperty(Mine)

        minetoo = MineToo()
        minetoo.bar = None
        assert MineToo.bar._get_for_dict(minetoo) is None

    @staticmethod
    def test_legacy_optional_local_structured_property(in_context):
        class SubKind(model.Model):
            foo = model.Property()

        class ContainerB(model.Model):
            child_b = model.LocalStructuredProperty(SubKind)

        class ContainerA(model.Model):
            child_a = model.LocalStructuredProperty(ContainerB)

        with in_context.new(legacy_data=True).use():
            entity = ContainerA(child_a=ContainerB())
            data = {"_exclude_from_indexes": []}
            assert ContainerA.child_a._to_datastore(entity, data) == ("child_a",)
            assert data.pop("_exclude_from_indexes") == ["child_a"]
            assert data["child_a"]["child_b"] is None

    @staticmethod
    def test_local_structured_property_with_polymodel(in_context):
        class Base(polymodel.PolyModel):
            pass

        class SubKind(Base):
            foo = model.StringProperty()

        class Container(model.Model):
            child = model.LocalStructuredProperty(Base)

        entity = Container(child=SubKind(foo="bar"))
        value = b"".join(
            [
                b"\x1a \n\x05class\x12\x17J\x15\n\x07\x8a\x01\x04Base\n\n",
                b"\x8a\x01\x07SubKind\x1a\r\n\x03foo\x12\x06\x8a\x01\x03bar",
            ]
        )

        child = entity._properties["child"]._from_base_type(value)
        assert child.foo == "bar"

        pb = entity_pb2.Entity()
        pb._pb.MergeFromString(value)
        value = helpers.entity_from_protobuf(pb)
        child = model._entity_from_ds_entity(value, model_class=Base)
        assert child._values["foo"].b_val == "bar"


class TestGenericProperty:
    @staticmethod
    def test_constructor():
        prop = model.GenericProperty(name="generic")
        assert prop._name == "generic"

    @staticmethod
    def test_constructor_compressed():
        prop = model.GenericProperty(name="generic", compressed=True)
        assert prop._compressed is True

    @staticmethod
    def test_constructor_compressed_and_indexed():
        with pytest.raises(NotImplementedError):
            model.GenericProperty(name="generic", compressed=True, indexed=True)

    @staticmethod
    def test__db_get_value():
        prop = model.GenericProperty()

        with pytest.raises(exceptions.NoLongerImplementedError):
            prop._db_get_value(None, None)

    @staticmethod
    def test__db_set_value():
        prop = model.GenericProperty()

        with pytest.raises(exceptions.NoLongerImplementedError):
            prop._db_set_value(None, None, None)

    @staticmethod
    def test__to_base_type():
        prop = model.GenericProperty(name="generic", compressed=True)
        value = b"abc" * 10
        converted = prop._to_base_type(value)

        assert isinstance(converted, model._CompressedValue)
        assert converted.z_val == zlib.compress(value)

    @staticmethod
    def test__to_base_type_no_convert():
        prop = model.GenericProperty(name="generic")
        value = b"abc" * 10
        converted = prop._to_base_type(value)
        assert converted is None

    @staticmethod
    def test__from_base_type():
        prop = model.GenericProperty(name="generic")
        original = b"abc" * 10
        z_val = zlib.compress(original)
        value = model._CompressedValue(z_val)
        converted = prop._from_base_type(value)

        assert converted == original

    @staticmethod
    def test__from_base_type_no_convert():
        prop = model.GenericProperty(name="generic")
        converted = prop._from_base_type(b"abc")
        assert converted is None

    @staticmethod
    def test__validate():
        prop = model.GenericProperty(name="generic", indexed=False)
        assert prop._validate(b"abc") is None

    @staticmethod
    def test__validate_indexed():
        prop = model.GenericProperty(name="generic", indexed=True)
        assert prop._validate(42) is None

    @staticmethod
    def test__validate_indexed_bytes():
        prop = model.GenericProperty(name="generic", indexed=True)
        assert prop._validate(b"abc") is None

    @staticmethod
    def test__validate_indexed_unicode():
        prop = model.GenericProperty(name="generic", indexed=True)
        assert prop._validate("abc") is None

    @staticmethod
    def test__validate_indexed_bad_length():
        prop = model.GenericProperty(name="generic", indexed=True)
        with pytest.raises(exceptions.BadValueError):
            prop._validate(b"ab" * model._MAX_STRING_LENGTH)


class TestComputedProperty:
    @staticmethod
    def test_constructor():
        def lower_name(self):
            return self.lower()  # pragma: NO COVER

        prop = model.ComputedProperty(lower_name)
        assert prop._func == lower_name

    @staticmethod
    def test_repr():
        """Regression test for #256

        https://github.com/googleapis/python-ndb/issues/256
        """

        def lower_name(self):
            return self.lower()  # pragma: NO COVER

        prop = model.ComputedProperty(lower_name)
        assert "lower_name" in repr(prop)

    @staticmethod
    def test__set_value():
        prop = model.ComputedProperty(lambda self: self)  # pragma: NO COVER
        with pytest.raises(model.ComputedPropertyError):
            prop._set_value(None, None)

    @staticmethod
    def test__delete_value():
        prop = model.ComputedProperty(lambda self: self)  # pragma: NO COVER
        with pytest.raises(model.ComputedPropertyError):
            prop._delete_value(None)

    @staticmethod
    def test__get_value():
        prop = model.ComputedProperty(lambda self: 42)
        entity = mock.Mock(_projection=None, _values={}, spec=("_projection"))
        assert prop._get_value(entity) == 42

    @staticmethod
    def test__get_value_with_projection():
        prop = model.ComputedProperty(
            lambda self: 42, name="computed"
        )  # pragma: NO COVER
        entity = mock.Mock(
            _projection=["computed"],
            _values={"computed": 84},
            spec=("_projection", "_values"),
        )
        assert prop._get_value(entity) == 84

    @staticmethod
    def test__get_value_empty_projection():
        prop = model.ComputedProperty(lambda self: 42)
        entity = mock.Mock(_projection=None, _values={}, spec=("_projection"))
        prop._prepare_for_put(entity)
        assert entity._values == {prop._name: 42}


class TestMetaModel:
    @staticmethod
    def test___repr__():
        expected = "Model<>"
        assert repr(model.Model) == expected

    @staticmethod
    def test___repr__extended():
        class Mine(model.Model):
            first = model.IntegerProperty()
            second = model.StringProperty()

        expected = (
            "Mine<first=IntegerProperty('first'), second=StringProperty('second')>"
        )
        assert repr(Mine) == expected

    @staticmethod
    def test_bad_kind():
        with pytest.raises(model.KindError):

            class Mine(model.Model):
                @classmethod
                def _get_kind(cls):
                    return 525600

    @staticmethod
    def test_invalid_property_name():
        with pytest.raises(TypeError):

            class Mine(model.Model):
                _foo = model.StringProperty()

    @staticmethod
    def test_repeated_property():
        class Mine(model.Model):
            foo = model.StringProperty(repeated=True)

        assert Mine._has_repeated

    @staticmethod
    def test_non_property_attribute():
        model_attr = mock.Mock(spec=model.ModelAttribute)

        class Mine(model.Model):
            baz = model_attr

        model_attr._fix_up.assert_called_once_with(Mine, "baz")


class TestModel:
    @staticmethod
    def test_constructor_defaults():
        entity = model.Model()
        assert entity.__dict__ == {"_values": {}}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_key():
        key = key_module.Key("Foo", "bar")
        entity = model.Model(key=key)
        assert entity.__dict__ == {"_values": {}, "_entity_key": key}

        entity = model.Model(_key=key)
        assert entity.__dict__ == {"_values": {}, "_entity_key": key}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_key_parts():
        entity = model.Model(id=124)
        key = key_module.Key("Model", 124)
        assert entity.__dict__ == {"_values": {}, "_entity_key": key}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_namespace_no_key_parts():
        entity = model.Model(namespace="myspace")
        key = key_module.Key("Model", None, namespace="myspace")
        assert entity.__dict__ == {"_entity_key": key, "_values": {}}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_app():
        entity = model.Model(app="thisproject")
        key = key_module.Key("Model", None, project="thisproject")
        assert entity.__dict__ == {"_values": {}, "_entity_key": key}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_project():
        entity = model.Model(project="thisproject")
        key = key_module.Key("Model", None, project="thisproject")
        assert entity.__dict__ == {"_values": {}, "_entity_key": key}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_app_and_project():
        with pytest.raises(exceptions.BadArgumentError):
            model.Model(app="foo", project="bar")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_key_and_key_parts():
        key = key_module.Key("Foo", "bar")
        with pytest.raises(exceptions.BadArgumentError):
            model.Model(key=key, id=124)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_key_and_key_parts_with_namespace():
        key = key_module.Key("Foo", "bar")
        with pytest.raises(exceptions.BadArgumentError):
            model.Model(key=key, namespace="myspace")

    @staticmethod
    def test_constructor_user_property_collision():
        class SecretMap(model.Model):
            key = model.IntegerProperty()

        entity = SecretMap(key=1001)
        assert entity.__dict__ == {"_values": {"key": 1001}}

    @staticmethod
    def test_constructor_with_projection():
        class Book(model.Model):
            pages = model.IntegerProperty()
            author = model.StringProperty()
            publisher = model.StringProperty()

        entity = Book(pages=287, author="Tim Robert", projection=("pages", "author"))
        assert entity.__dict__ == {
            "_values": {"pages": 287, "author": "Tim Robert"},
            "_projection": ("pages", "author"),
        }

    @staticmethod
    def test_constructor_with_structured_property_projection():
        class Author(model.Model):
            first_name = model.StringProperty()
            last_name = model.StringProperty()

        class Book(model.Model):
            pages = model.IntegerProperty()
            author = model.StructuredProperty(Author)
            publisher = model.StringProperty()

        entity = Book(
            pages=287,
            author=Author(first_name="Tim", last_name="Robert"),
            projection=("author.first_name", "author.last_name"),
        )
        assert entity._projection == ("author.first_name", "author.last_name")
        assert entity.author._projection == ("first_name", "last_name")

    @staticmethod
    def test_constructor_with_repeated_structured_property_projection():
        class Author(model.Model):
            first_name = model.StringProperty()
            last_name = model.StringProperty()

        class Book(model.Model):
            pages = model.IntegerProperty()
            authors = model.StructuredProperty(Author, repeated=True)
            publisher = model.StringProperty()

        entity = Book(
            pages=287,
            authors=[
                Author(first_name="Tim", last_name="Robert"),
                Author(first_name="Jim", last_name="Bobert"),
            ],
            projection=("authors.first_name", "authors.last_name"),
        )
        assert entity._projection == (
            "authors.first_name",
            "authors.last_name",
        )
        assert entity.authors[0]._projection == ("first_name", "last_name")

    @staticmethod
    def test_constructor_non_existent_property():
        with pytest.raises(AttributeError):
            model.Model(pages=287)

    @staticmethod
    def test_constructor_non_property():
        class TimeTravelVehicle(model.Model):
            speed = 88

        with pytest.raises(TypeError):
            TimeTravelVehicle(speed=28)

    @staticmethod
    def test_repr():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=909, id="hi", key=[88.5, 0.0], value=None)
        expected = "ManyFields(id='hi', key=[88.5, 0.0], self=909, value=None)"
        assert repr(entity) == expected

    @staticmethod
    def test_repr_with_projection():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(
            self=909,
            id="hi",
            key=[88.5, 0.0],
            value=None,
            projection=("self", "id"),
        )
        expected = (
            "ManyFields(id='hi', key=[88.5, 0.0], self=909, value=None, "
            "_projection=('self', 'id'))"
        )
        assert repr(entity) == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_repr_with_property_named_key():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=909, id="hi", key=[88.5, 0.0], value=None, _id=78)
        expected = (
            "ManyFields(_key=Key('ManyFields', 78), id='hi', key=[88.5, 0.0], "
            "self=909, value=None)"
        )
        assert repr(entity) == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_repr_with_property_named_key_not_set():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=909, id="hi", value=None, _id=78)
        expected = (
            "ManyFields(_key=Key('ManyFields', 78), id='hi', self=909, value=None)"
        )
        assert repr(entity) == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_repr_no_property_named_key():
        class NoKeyCollision(model.Model):
            word = model.StringProperty()

        entity = NoKeyCollision(word="one", id=801)
        expected = "NoKeyCollision(key=Key('NoKeyCollision', 801), word='one')"
        assert repr(entity) == expected

    @staticmethod
    def test__get_kind():
        assert model.Model._get_kind() == "Model"

        class Simple(model.Model):
            pass

        assert Simple._get_kind() == "Simple"

    @staticmethod
    def test__class_name():
        assert model.Model._class_name() == "Model"

        class Simple(model.Model):
            pass

        assert Simple._class_name() == "Simple"

    @staticmethod
    def test__default_filters():
        assert model.Model._default_filters() == ()

        class Simple(model.Model):
            pass

        assert Simple._default_filters() == ()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___hash__():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=909, id="hi", value=None, _id=78)
        with pytest.raises(TypeError):
            hash(entity)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___eq__wrong_type():
        class Simple(model.Model):
            pass

        ManyFields = ManyFieldsFactory()
        entity1 = ManyFields(self=909, id="hi", value=None, _id=78)
        entity2 = Simple()
        assert not entity1 == entity2

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___eq__wrong_key():
        ManyFields = ManyFieldsFactory()
        entity1 = ManyFields(_id=78)
        entity2 = ManyFields(_id="seventy-eight")
        assert not entity1 == entity2

    @staticmethod
    def test___eq__wrong_projection():
        ManyFields = ManyFieldsFactory()
        entity1 = ManyFields(self=90, projection=("self",))
        entity2 = ManyFields(value="a", unused=0.0, projection=("value", "unused"))
        assert not entity1 == entity2

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___eq__same_type_same_key():
        ManyFields = ManyFieldsFactory()
        entity1 = ManyFields(self=909, id="hi", _id=78)
        entity2 = ManyFields(self=909, id="bye", _id=78)
        assert entity1 == entity1
        assert not entity1 == entity2

    @staticmethod
    def test___eq__same_type_same_key_same_projection():
        ManyFields = ManyFieldsFactory()
        entity1 = ManyFields(self=-9, id="hi", projection=("self", "id"))
        entity2 = ManyFields(self=-9, id="bye", projection=("self", "id"))
        assert entity1 == entity1
        assert not entity1 == entity2

    @staticmethod
    def test__eq__expando_w_different_number_of_properties():
        class SomeKind(model.Expando):
            foo = model.IntegerProperty()

        entity1 = SomeKind(foo=1)
        entity2 = SomeKind(foo=1, bar=2)

        assert not entity1 == entity2

    @staticmethod
    def test__eq__expando_w_different_properties():
        class SomeKind(model.Expando):
            foo = model.IntegerProperty()

        entity1 = SomeKind(foo=1, bar=2)
        entity2 = SomeKind(foo=1, baz=3)

        assert not entity1 == entity2

    @staticmethod
    def test__eq__expando():
        class SomeKind(model.Expando):
            foo = model.IntegerProperty()

        entity1 = SomeKind(foo=1, bar=2)
        entity2 = SomeKind(foo=1, bar=2)

        assert entity1 == entity2

    @staticmethod
    def test__eq__structured_property():
        class OtherKind(model.Model):
            bar = model.IntegerProperty()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(OtherKind)
            hi = model.StringProperty()

        entity1 = SomeKind(hi="mom", foo=OtherKind(bar=42))
        entity2 = SomeKind(hi="mom", foo=OtherKind(bar=42))

        assert entity1 == entity2

    @staticmethod
    def test__eq__structured_property_differs():
        class OtherKind(model.Model):
            bar = model.IntegerProperty()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(OtherKind)
            hi = model.StringProperty()

        entity1 = SomeKind(hi="mom", foo=OtherKind(bar=42))
        entity2 = SomeKind(hi="mom", foo=OtherKind(bar=43))

        assert not entity1 == entity2

    @staticmethod
    def test__eq__repeated_structured_property():
        class OtherKind(model.Model):
            bar = model.IntegerProperty()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(OtherKind, repeated=True)
            hi = model.StringProperty()

        entity1 = SomeKind(hi="mom", foo=[OtherKind(bar=42)])
        entity2 = SomeKind(hi="mom", foo=[OtherKind(bar=42)])

        assert entity1 == entity2

    @staticmethod
    def test__eq__repeated_structured_property_differs():
        class OtherKind(model.Model):
            bar = model.IntegerProperty()

        class SomeKind(model.Model):
            foo = model.StructuredProperty(OtherKind, repeated=True)
            hi = model.StringProperty()

        entity1 = SomeKind(hi="mom", foo=[OtherKind(bar=42)])
        entity2 = SomeKind(hi="mom", foo=[OtherKind(bar=42), OtherKind(bar=43)])

        assert not entity1 == entity2

    @staticmethod
    def test___ne__():
        class Simple(model.Model):
            pass

        ManyFields = ManyFieldsFactory()
        entity1 = ManyFields(self=-9, id="hi")
        entity2 = Simple()
        entity3 = ManyFields(self=-9, id="bye")
        entity4 = ManyFields(self=-9, id="bye", projection=("self", "id"))
        entity5 = None
        entity6 = ManyFields(self=-9, id="hi")
        assert not entity1 != entity1
        assert entity1 != entity2
        assert entity1 != entity3
        assert entity1 != entity4
        assert entity1 != entity5
        assert not entity1 != entity6

    @staticmethod
    def test___lt__():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=-9, id="hi")
        with pytest.raises(TypeError):
            entity < entity

    @staticmethod
    def test___le__():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=-9, id="hi")
        with pytest.raises(TypeError):
            entity <= entity

    @staticmethod
    def test___gt__():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=-9, id="hi")
        with pytest.raises(TypeError):
            entity > entity

    @staticmethod
    def test___ge__():
        ManyFields = ManyFieldsFactory()
        entity = ManyFields(self=-9, id="hi")
        with pytest.raises(TypeError):
            entity >= entity

    @staticmethod
    def test__validate_key():
        value = mock.sentinel.value
        assert model.Model._validate_key(value) is value

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test__put_no_key(_datastore_api):
        entity = model.Model()
        _datastore_api.put.return_value = future = tasklets.Future()
        future.set_result(None)

        ds_entity = model._entity_to_ds_entity(entity)
        assert entity._put() == entity.key

        # Can't do a simple "assert_called_once_with" here because entities'
        # keys will fail test for equality because Datastore's Key.__eq__
        # method returns False if either key is partial, regardless of whether
        # they're effectively equal or not. Have to do this more complicated
        # unpacking instead.
        assert _datastore_api.put.call_count == 1
        call_ds_entity, call_options = _datastore_api.put.call_args[0]
        assert call_ds_entity.key.path == ds_entity.key.path
        assert call_ds_entity.items() == ds_entity.items()
        assert call_options == _options.Options()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test__put_w_key_no_cache(_datastore_api, in_context):
        entity = model.Model()
        _datastore_api.put.return_value = future = tasklets.Future()

        key = key_module.Key("SomeKind", 123)
        future.set_result(key._key)

        ds_entity = model._entity_to_ds_entity(entity)
        assert entity._put(use_cache=False) == key
        assert not in_context.cache

        # Can't do a simple "assert_called_once_with" here because entities'
        # keys will fail test for equality because Datastore's Key.__eq__
        # method returns False if either key is partial, regardless of whether
        # they're effectively equal or not. Have to do this more complicated
        # unpacking instead.
        assert _datastore_api.put.call_count == 1
        call_ds_entity, call_options = _datastore_api.put.call_args[0]
        assert call_ds_entity.key.path == ds_entity.key.path
        assert call_ds_entity.items() == ds_entity.items()
        assert call_options == _options.Options(use_cache=False)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test__put_w_key_with_cache(_datastore_api, in_context):
        entity = model.Model()
        _datastore_api.put.return_value = future = tasklets.Future()

        key = key_module.Key("SomeKind", 123)
        future.set_result(key._key)

        ds_entity = model._entity_to_ds_entity(entity)
        assert entity._put(use_cache=True) == key
        assert in_context.cache[key] == entity
        assert in_context.cache.get_and_validate(key) == entity

        # Can't do a simple "assert_called_once_with" here because entities'
        # keys will fail test for equality because Datastore's Key.__eq__
        # method returns False if either key is partial, regardless of whether
        # they're effectively equal or not. Have to do this more complicated
        # unpacking instead.
        assert _datastore_api.put.call_count == 1
        call_ds_entity, call_options = _datastore_api.put.call_args[0]
        assert call_ds_entity.key.path == ds_entity.key.path
        assert call_ds_entity.items() == ds_entity.items()
        assert call_options == _options.Options(use_cache=True)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test__put_w_key(_datastore_api):
        entity = model.Model()
        _datastore_api.put.return_value = future = tasklets.Future()

        key = key_module.Key("SomeKind", 123)
        future.set_result(key._key)

        ds_entity = model._entity_to_ds_entity(entity)
        assert entity._put() == key

        # Can't do a simple "assert_called_once_with" here because entities'
        # keys will fail test for equality because Datastore's Key.__eq__
        # method returns False if either key is partial, regardless of whether
        # they're effectively equal or not. Have to do this more complicated
        # unpacking instead.
        assert _datastore_api.put.call_count == 1
        call_ds_entity, call_options = _datastore_api.put.call_args[0]
        assert call_ds_entity.key.path == ds_entity.key.path
        assert call_ds_entity.items() == ds_entity.items()
        assert call_options == _options.Options()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test__put_async(_datastore_api):
        entity = model.Model()
        _datastore_api.put.return_value = future = tasklets.Future()

        key = key_module.Key("SomeKind", 123)
        future.set_result(key._key)

        ds_entity = model._entity_to_ds_entity(entity)
        tasklet_future = entity._put_async()
        assert tasklet_future.result() == key

        # Can't do a simple "assert_called_once_with" here because entities'
        # keys will fail test for equality because Datastore's Key.__eq__
        # method returns False if either key is partial, regardless of whether
        # they're effectively equal or not. Have to do this more complicated
        # unpacking instead.
        assert _datastore_api.put.call_count == 1
        call_ds_entity, call_options = _datastore_api.put.call_args[0]
        assert call_ds_entity.key.path == ds_entity.key.path
        assert call_ds_entity.items() == ds_entity.items()
        assert call_options == _options.Options()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__prepare_for_put():
        class Simple(model.Model):
            foo = model.DateTimeProperty()

        entity = Simple(foo=datetime.datetime.now())
        with mock.patch.object(
            entity._properties["foo"], "_prepare_for_put"
        ) as patched:
            entity._prepare_for_put()
            patched.assert_called_once()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test__put_w_hooks(_datastore_api):
        class Simple(model.Model):
            def __init__(self):
                super(Simple, self).__init__()
                self.pre_put_calls = []
                self.post_put_calls = []

            def _pre_put_hook(self, *args, **kwargs):
                self.pre_put_calls.append((args, kwargs))

            def _post_put_hook(self, future, *args, **kwargs):
                assert isinstance(future, tasklets.Future)
                self.post_put_calls.append((args, kwargs))

        entity = Simple()
        _datastore_api.put.return_value = future = tasklets.Future()
        future.set_result(None)

        ds_entity = model._entity_to_ds_entity(entity)
        assert entity._put() == entity.key

        # Can't do a simple "assert_called_once_with" here because entities'
        # keys will fail test for equality because Datastore's Key.__eq__
        # method returns False if either key is partial, regardless of whether
        # they're effectively equal or not. Have to do this more complicated
        # unpacking instead.
        assert _datastore_api.put.call_count == 1
        call_ds_entity, call_options = _datastore_api.put.call_args[0]
        assert call_ds_entity.key.path == ds_entity.key.path
        assert call_ds_entity.items() == ds_entity.items()
        assert call_options == _options.Options()

        assert entity.pre_put_calls == [((), {})]
        assert entity.post_put_calls == [((), {})]

    @staticmethod
    def test__lookup_model():
        class ThisKind(model.Model):
            pass

        assert model.Model._lookup_model("ThisKind") is ThisKind

    @staticmethod
    def test__lookup_model_use_default():
        sentinel = object()
        assert model.Model._lookup_model("NoKind", sentinel) is sentinel

    @staticmethod
    def test__lookup_model_not_found():
        with pytest.raises(model.KindError):
            model.Model._lookup_model("NoKind")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__check_properties():
        class XModel(model.Model):
            x = model.IntegerProperty()

        properties = ["x"]
        assert XModel._check_properties(properties) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__check_properties_with_sub():
        class XModel(model.Model):
            x = model.IntegerProperty()

        properties = ["x.x"]
        # Will raise error until model.StructuredProperty is implemented
        with pytest.raises(model.InvalidPropertyError):
            XModel._check_properties(properties)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test__check_properties_not_found():
        properties = ["x"]
        with pytest.raises(model.InvalidPropertyError):
            model.Model._check_properties(properties)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_query():
        class XModel(model.Model):
            x = model.IntegerProperty()

        query = XModel.query(XModel.x == 42)
        assert query.kind == "XModel"
        assert query.filters == (XModel.x == 42)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_query_distinct():
        class XModel(model.Model):
            x = model.IntegerProperty()

        query = XModel.query(distinct=True, projection=("x",))
        assert query.distinct_on == ("x",)

    @staticmethod
    def test_query_distinct_no_projection():
        class XModel(model.Model):
            x = model.IntegerProperty()

        with pytest.raises(TypeError):
            XModel.query(distinct=True)

    @staticmethod
    def test_query_distinct_w_distinct_on():
        class XModel(model.Model):
            x = model.IntegerProperty()

        with pytest.raises(TypeError):
            XModel.query(distinct=True, distinct_on=("x",))

    @staticmethod
    def test_query_distinct_w_group_by():
        class XModel(model.Model):
            x = model.IntegerProperty()

        with pytest.raises(TypeError):
            XModel.query(distinct=True, group_by=("x",))

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_query_projection_of_unindexed_attribute():
        class XModel(model.Model):
            x = model.IntegerProperty(indexed=False)

        with pytest.raises(model.InvalidPropertyError):
            XModel.query(projection=["x"])

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_gql():
        class Simple(model.Model):
            x = model.IntegerProperty()

        query = Simple.gql("WHERE x=1")
        assert isinstance(query, query_module.Query)
        assert query.kind == "Simple"
        assert query.filters == query_module.FilterNode("x", "=", 1)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_gql_binding():
        class Simple(model.Model):
            x = model.IntegerProperty()
            y = model.StringProperty()

        query = Simple.gql("WHERE x=:1 and y=:foo", 2, foo="bar")
        assert isinstance(query, query_module.Query)
        assert query.kind == "Simple"
        assert query.filters == query_module.AND(
            query_module.FilterNode("x", "=", 2),
            query_module.FilterNode("y", "=", "bar"),
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_allocate_ids(_datastore_api):
        completed = [
            entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="Simple", id=21)],
            ),
            entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="Simple", id=42)],
            ),
        ]
        _datastore_api.allocate.return_value = utils.future_result(completed)

        class Simple(model.Model):
            pass

        keys = Simple.allocate_ids(2)
        assert keys == (
            key_module.Key("Simple", 21),
            key_module.Key("Simple", 42),
        )

        call_keys, call_options = _datastore_api.allocate.call_args[0]
        call_keys = [key_module.Key._from_ds_key(key) for key in call_keys]
        assert call_keys == [
            key_module.Key("Simple", None),
            key_module.Key("Simple", None),
        ]
        assert call_options == _options.Options()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_allocate_ids_w_hooks(_datastore_api):
        completed = [
            entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="Simple", id=21)],
            ),
            entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="Simple", id=42)],
            ),
        ]
        _datastore_api.allocate.return_value = utils.future_result(completed)

        class Simple(model.Model):
            pre_allocate_id_calls = []
            post_allocate_id_calls = []

            @classmethod
            def _pre_allocate_ids_hook(cls, *args, **kwargs):
                cls.pre_allocate_id_calls.append((args, kwargs))

            @classmethod
            def _post_allocate_ids_hook(
                cls, size, max, parent, future, *args, **kwargs
            ):
                assert isinstance(future, tasklets.Future)
                cls.post_allocate_id_calls.append(((size, max, parent) + args, kwargs))

        keys = Simple.allocate_ids(2)
        assert keys == (
            key_module.Key("Simple", 21),
            key_module.Key("Simple", 42),
        )

        call_keys, call_options = _datastore_api.allocate.call_args[0]
        call_keys = [key_module.Key._from_ds_key(key) for key in call_keys]
        assert call_keys == [
            key_module.Key("Simple", None),
            key_module.Key("Simple", None),
        ]
        assert call_options == _options.Options()

        assert Simple.pre_allocate_id_calls == [((2, None, None), {})]
        assert Simple.post_allocate_id_calls == [((2, None, None), {})]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_allocate_ids_with_max():
        class Simple(model.Model):
            pass

        with pytest.raises(NotImplementedError):
            Simple.allocate_ids(max=6)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_allocate_ids_no_args():
        class Simple(model.Model):
            pass

        with pytest.raises(TypeError):
            Simple.allocate_ids()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_allocate_ids_async(_datastore_api):
        completed = [
            entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="Simple", id=21)],
            ),
            entity_pb2.Key(
                partition_id=entity_pb2.PartitionId(project_id="testing"),
                path=[entity_pb2.Key.PathElement(kind="Simple", id=42)],
            ),
        ]
        _datastore_api.allocate.return_value = utils.future_result(completed)

        class Simple(model.Model):
            pass

        future = Simple.allocate_ids_async(2)
        keys = future.result()
        assert keys == (
            key_module.Key("Simple", 21),
            key_module.Key("Simple", 42),
        )

        call_keys, call_options = _datastore_api.allocate.call_args[0]
        call_keys = [key_module.Key._from_ds_key(key) for key in call_keys]
        assert call_keys == [
            key_module.Key("Simple", None),
            key_module.Key("Simple", None),
        ]
        assert call_options == _options.Options()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_by_id(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            pass

        assert Simple.get_by_id(1) is entity
        key_module.Key.assert_called_once_with("Simple", 1, parent=None)
        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_by_id_w_parent_project_namespace(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            pass

        assert (
            Simple.get_by_id(1, parent="foo", project="baz", namespace="bar") is entity
        )

        key_module.Key.assert_called_once_with(
            "Simple", 1, parent="foo", namespace="bar", app="baz"
        )

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_by_id_w_default_namespace(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            pass

        assert Simple.get_by_id(1, namespace="") is entity

        key_module.Key.assert_called_once_with("Simple", 1, namespace="", parent=None)

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_by_id_w_app(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            pass

        assert Simple.get_by_id(1, app="baz") is entity

        key_module.Key.assert_called_once_with("Simple", 1, parent=None, app="baz")

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_by_id_w_app_and_project():
        class Simple(model.Model):
            pass

        with pytest.raises(TypeError):
            Simple.get_by_id(1, app="baz", project="bar")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_by_id_async(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            pass

        future = Simple.get_by_id_async(1)
        assert future.result() is entity

        key_module.Key.assert_called_once_with("Simple", 1, parent=None)

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_get(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            foo = model.IntegerProperty()

        assert Simple.get_or_insert("one", foo=42) is entity

        key_module.Key.assert_called_once_with("Simple", "one", parent=None)

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_get_w_app(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            foo = model.IntegerProperty()

        assert Simple.get_or_insert("one", foo=42, app="himom") is entity

        key_module.Key.assert_called_once_with(
            "Simple", "one", parent=None, app="himom"
        )

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_get_w_namespace(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            foo = model.IntegerProperty()

        assert Simple.get_or_insert("one", foo=42, namespace="himom") is entity

        key_module.Key.assert_called_once_with(
            "Simple", "one", parent=None, namespace="himom"
        )

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_get_w_default_namespace(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            foo = model.IntegerProperty()

        assert Simple.get_or_insert("one", foo=0, namespace="") is entity

        key_module.Key.assert_called_once_with(
            "Simple", "one", parent=None, namespace=""
        )

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_or_insert_get_w_app_and_project():
        class Simple(model.Model):
            foo = model.IntegerProperty()

        with pytest.raises(TypeError):
            Simple.get_or_insert("one", foo=42, app="himom", project="hidad")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_or_insert_get_w_id_instead_of_name():
        class Simple(model.Model):
            foo = model.IntegerProperty()

        with pytest.raises(TypeError):
            Simple.get_or_insert(1, foo=42)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_get_or_insert_get_w_empty_name():
        class Simple(model.Model):
            foo = model.IntegerProperty()

        with pytest.raises(TypeError):
            Simple.get_or_insert("", foo=42)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model._transaction")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_insert_in_transaction(patched_key_module, _transaction):
        class MockKey(key_module.Key):
            get_async = mock.Mock(return_value=utils.future_result(None))

        patched_key_module.Key = MockKey

        class Simple(model.Model):
            foo = model.IntegerProperty()

            put_async = mock.Mock(return_value=utils.future_result(None))

        _transaction.in_transaction.return_value = True

        entity = Simple.get_or_insert("one", foo=42)
        assert entity.foo == 42
        assert entity._key == MockKey("Simple", "one")
        entity.put_async.assert_called_once_with(_options=_options.ReadOptions())

        entity._key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model._transaction")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_insert_not_in_transaction(patched_key_module, _transaction):
        class MockKey(key_module.Key):
            get_async = mock.Mock(return_value=utils.future_result(None))

        patched_key_module.Key = MockKey

        class Simple(model.Model):
            foo = model.IntegerProperty()

            put_async = mock.Mock(return_value=utils.future_result(None))

        _transaction.in_transaction.return_value = False
        _transaction.transaction_async = lambda f: f()

        entity = Simple.get_or_insert("one", foo=42)
        assert entity.foo == 42
        assert entity._key == MockKey("Simple", "one")
        entity.put_async.assert_called_once_with(_options=_options.ReadOptions())

        entity._key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model._transaction")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_insert_model_has_name_and_parent_properties(
        patched_key_module, _transaction
    ):
        class MockKey(key_module.Key):
            get_async = mock.Mock(return_value=utils.future_result(None))

        patched_key_module.Key = MockKey

        class Simple(model.Model):
            parent = model.IntegerProperty()
            name = model.StringProperty()

            put_async = mock.Mock(return_value=utils.future_result(None))

        _transaction.in_transaction.return_value = False
        _transaction.transaction_async = lambda f: f()

        entity = Simple.get_or_insert("one", parent=42, name="Priscilla")
        assert entity.parent == 42
        assert entity.name == "Priscilla"
        assert entity._key == MockKey("Simple", "one")
        entity.put_async.assert_called_once_with(_options=_options.ReadOptions())

        entity._key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model._transaction")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_w_parent_insert_model_has_name_and_parent_properties(
        patched_key_module, _transaction
    ):
        parent_key = key_module.Key("SomeKind", "parent_name")

        class MockKey(key_module.Key):
            get_async = mock.Mock(return_value=utils.future_result(None))

        patched_key_module.Key = MockKey

        class Simple(model.Model):
            parent = model.IntegerProperty()
            name = model.StringProperty()

            put_async = mock.Mock(return_value=utils.future_result(None))

        _transaction.in_transaction.return_value = False
        _transaction.transaction_async = lambda f: f()

        entity = Simple.get_or_insert(
            "one", _parent=parent_key, parent=42, name="Priscilla"
        )
        assert entity.parent == 42
        assert entity.name == "Priscilla"
        assert entity._key == MockKey("SomeKind", "parent_name", "Simple", "one")
        entity.put_async.assert_called_once_with(_options=_options.ReadOptions())

        entity._key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model._transaction")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_insert_model_has_timeout_property(
        patched_key_module, _transaction
    ):
        class MockKey(key_module.Key):
            get_async = mock.Mock(return_value=utils.future_result(None))

        patched_key_module.Key = MockKey

        class Simple(model.Model):
            timeout = model.IntegerProperty()

            put_async = mock.Mock(return_value=utils.future_result(None))

        _transaction.in_transaction.return_value = False
        _transaction.transaction_async = lambda f: f()

        entity = Simple.get_or_insert("one", timeout=42)
        assert entity.timeout == 42
        assert entity._key == MockKey("Simple", "one")
        entity.put_async.assert_called_once_with(_options=_options.ReadOptions())

        entity._key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model._transaction")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_insert_with_timeout_model_has_timeout_property(
        patched_key_module, _transaction
    ):
        class MockKey(key_module.Key):
            get_async = mock.Mock(return_value=utils.future_result(None))

        patched_key_module.Key = MockKey

        class Simple(model.Model):
            timeout = model.IntegerProperty()

            put_async = mock.Mock(return_value=utils.future_result(None))

        _transaction.in_transaction.return_value = False
        _transaction.transaction_async = lambda f: f()

        entity = Simple.get_or_insert("one", _timeout=60, timeout=42)
        assert entity.timeout == 42
        assert entity._key == MockKey("Simple", "one")
        entity.put_async.assert_called_once_with(
            _options=_options.ReadOptions(timeout=60)
        )
        entity._key.get_async.assert_called_once_with(
            _options=_options.ReadOptions(timeout=60)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.model.key_module")
    def test_get_or_insert_async(key_module):
        entity = object()
        key = key_module.Key.return_value
        key.get_async.return_value = utils.future_result(entity)

        class Simple(model.Model):
            foo = model.IntegerProperty()

        future = Simple.get_or_insert_async("one", foo=42)
        assert future.result() is entity

        key_module.Key.assert_called_once_with("Simple", "one", parent=None)

        key.get_async.assert_called_once_with(_options=_options.ReadOptions())

    @staticmethod
    def test_populate():
        class Simple(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        entity = Simple()
        entity.populate(foo=3, bar="baz")

        assert entity.foo == 3
        assert entity.bar == "baz"

    @staticmethod
    def test_has_complete_key_no_key():
        class Simple(model.Model):
            pass

        entity = Simple()
        assert not entity.has_complete_key()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_complete_key_incomplete_key():
        class Simple(model.Model):
            pass

        entity = Simple(key=key_module.Key("Simple", None))
        assert not entity.has_complete_key()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_has_complete_key_complete_with_id():
        class Simple(model.Model):
            pass

        entity = Simple(id="happiness")
        assert entity.has_complete_key()

    @staticmethod
    def test_to_dict():
        class Simple(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        entity = Simple(foo=3, bar="baz")
        assert entity.to_dict() == {"foo": 3, "bar": "baz"}

    @staticmethod
    def test_to_dict_with_include():
        class Simple(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        entity = Simple(foo=3, bar="baz")
        assert entity.to_dict(include={"foo"}) == {"foo": 3}

    @staticmethod
    def test_to_dict_with_exclude():
        class Simple(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        entity = Simple(foo=3, bar="baz")
        assert entity.to_dict(exclude=("bar",)) == {"foo": 3}

    @staticmethod
    def test_to_dict_with_projection():
        class Simple(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        entity = Simple(foo=3, bar="baz", projection=("foo",))
        assert entity.to_dict() == {"foo": 3}

    @staticmethod
    def test__code_name_from_stored_name():
        class Simple(model.Model):
            foo = model.StringProperty()
            bar = model.StringProperty(name="notbar")

        assert Simple._code_name_from_stored_name("foo") == "foo"
        assert Simple._code_name_from_stored_name("notbar") == "bar"


class Test_entity_from_protobuf:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_case():
        class ThisKind(model.Model):
            a = model.IntegerProperty()
            b = model.BooleanProperty()
            c = model.PickleProperty()
            d = model.StringProperty(repeated=True)
            e = model.PickleProperty(repeated=True)
            notaproperty = True

        dill = {"sandwiches": ["turkey", "reuben"], "not_sandwiches": "tacos"}
        gherkin = [{"a": {"b": "c"}, "d": 0}, [1, 2, 3], "himom"]
        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update(
            {
                "a": 42,
                "b": None,
                "c": pickle.dumps(gherkin, pickle.HIGHEST_PROTOCOL),
                "d": ["foo", "bar", "baz"],
                "e": [
                    pickle.dumps(gherkin, pickle.HIGHEST_PROTOCOL),
                    pickle.dumps(dill, pickle.HIGHEST_PROTOCOL),
                ],
                "notused": 32,
                "notaproperty": None,
            }
        )
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.a == 42
        assert entity.b is None
        assert entity.c == gherkin
        assert entity.d == ["foo", "bar", "baz"]
        assert entity.e == [gherkin, dill]
        assert entity._key == key_module.Key("ThisKind", 123, app="testing")
        assert entity.notaproperty is True

    @staticmethod
    def test_property_named_key():
        class ThisKind(model.Model):
            key = model.StringProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update({"key": "luck"})
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.key == "luck"
        assert entity._key.kind() == "ThisKind"
        assert entity._key.id() == 123

    @staticmethod
    def test_expando_property():
        class ThisKind(model.Expando):
            key = model.StringProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update({"key": "luck", "expando_prop": "good"})
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.key == "luck"
        assert entity._key.kind() == "ThisKind"
        assert entity._key.id() == 123
        assert entity.expando_prop == "good"

    @staticmethod
    def test_expando_property_list_value():
        class ThisKind(model.Expando):
            key = model.StringProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update({"key": "luck", "expando_prop": ["good"]})
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.key == "luck"
        assert entity._key.kind() == "ThisKind"
        assert entity._key.id() == 123
        assert entity.expando_prop == ["good"]

    @staticmethod
    def test_value_but_non_expando_property():
        class ThisKind(model.Model):
            key = model.StringProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update({"key": "luck", "expando_prop": None})
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.key == "luck"
        assert entity._key.kind() == "ThisKind"
        assert entity._key.id() == 123

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_legacy_structured_property():
        class OtherKind(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        class ThisKind(model.Model):
            baz = model.StructuredProperty(OtherKind)
            copacetic = model.BooleanProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update(
            {
                "baz.foo": 42,
                "baz.bar": "himom",
                "copacetic": True,
                "super.fluous": "whocares?",
            }
        )
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.baz.foo == 42
        assert entity.baz.bar == "himom"
        assert entity.copacetic is True

        assert not hasattr(entity, "super")
        assert not hasattr(entity, "super.fluous")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_repeated_structured_property():
        class OtherKind(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        class ThisKind(model.Model):
            baz = model.StructuredProperty(OtherKind, repeated=True)
            copacetic = model.BooleanProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update(
            {
                "baz.foo": [42, 144],
                "baz.bar": ["himom", "hellodad"],
                "copacetic": True,
            }
        )
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.baz[0].foo == 42
        assert entity.baz[0].bar == "himom"
        assert entity.baz[1].foo == 144
        assert entity.baz[1].bar == "hellodad"
        assert entity.copacetic is True

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_legacy_repeated_structured_property_projection():
        class OtherKind(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        class ThisKind(model.Model):
            baz = model.StructuredProperty(OtherKind, repeated=True)
            copacetic = model.BooleanProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update({"baz.foo": 42, "baz.bar": "himom", "copacetic": True})
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, ThisKind)
        assert entity.baz[0].foo == 42
        assert entity.baz[0].bar == "himom"
        assert entity.copacetic is True


class Test_entity_from_ds_entity:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_legacy_repeated_structured_property_uneven():
        class OtherKind(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        class ThisKind(model.Model):
            baz = model.StructuredProperty(OtherKind, repeated=True)
            copacetic = model.BooleanProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.items = mock.Mock(
            return_value=(
                # Order counts for coverage
                ("baz.foo", [42, 144]),
                ("baz.bar", ["himom", "hellodad", "iminjail"]),
                ("copacetic", True),
            )
        )

        entity = model._entity_from_ds_entity(datastore_entity)
        assert isinstance(entity, ThisKind)
        assert entity.baz[0].foo == 42
        assert entity.baz[0].bar == "himom"
        assert entity.baz[1].foo == 144
        assert entity.baz[1].bar == "hellodad"
        assert entity.baz[2].foo is None
        assert entity.baz[2].bar == "iminjail"
        assert entity.copacetic is True

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_legacy_repeated_structured_property_uneven_expandos():
        class Expando1(model.Expando):
            bar = model.StringProperty()

        class Expando2(model.Expando):
            qux = model.StringProperty()

        class ThisKind(model.Model):
            foo = model.StructuredProperty(model_class=Expando1, repeated=True)
            baz = model.StructuredProperty(model_class=Expando2, repeated=True)

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.items = mock.Mock(
            return_value=(
                # Order matters here
                ("foo.bar", ["foo_bar_1"]),
                ("baz.qux", ["baz_qux_1", "baz_qux_2"]),
                ("foo.custom_1", ["foo_c1_1", "foo_c1_2"]),  # longer than foo.bar
            )
        )
        entity = model._entity_from_ds_entity(datastore_entity)
        assert isinstance(entity, ThisKind)
        assert len(entity.foo) == 2
        assert len(entity.baz) == 2
        assert entity.foo[0].bar == "foo_bar_1"
        assert entity.foo[0].custom_1 == "foo_c1_1"
        assert entity.foo[1].bar is None
        assert entity.foo[1].custom_1 == "foo_c1_2"
        assert entity.baz[0].qux == "baz_qux_1"
        assert entity.baz[1].qux == "baz_qux_2"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_legacy_repeated_structured_property_with_name():
        class OtherKind(model.Model):
            foo = model.IntegerProperty()
            bar = model.StringProperty()

        class ThisKind(model.Model):
            baz = model.StructuredProperty(OtherKind, "b", repeated=True)
            copacetic = model.BooleanProperty()

        key = datastore.Key("ThisKind", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.items = mock.Mock(
            return_value=(
                # Order counts for coverage
                ("b.foo", [42, 144]),
                ("b.bar", ["himom", "hellodad", "iminjail"]),
                ("copacetic", True),
            )
        )

        entity = model._entity_from_ds_entity(datastore_entity)
        assert isinstance(entity, ThisKind)
        assert entity.baz[0].foo == 42
        assert entity.baz[0].bar == "himom"
        assert entity.baz[1].foo == 144
        assert entity.baz[1].bar == "hellodad"
        assert entity.baz[2].foo is None
        assert entity.baz[2].bar == "iminjail"
        assert entity.copacetic is True

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_polymodel():
        class Animal(polymodel.PolyModel):
            foo = model.IntegerProperty()

        class Cat(Animal):
            bar = model.StringProperty()

        key = datastore.Key("Animal", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update(
            {"foo": 42, "bar": "himom!", "class": ["Animal", "Cat"]}
        )

        entity = model._entity_from_ds_entity(datastore_entity)
        assert isinstance(entity, Cat)
        assert entity.foo == 42
        assert entity.bar == "himom!"
        assert entity.class_ == ["Animal", "Cat"]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_polymodel_projection():
        class Animal(polymodel.PolyModel):
            foo = model.IntegerProperty()

        class Cat(Animal):
            bar = model.StringProperty()

        key = datastore.Key("Animal", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity.update({"foo": 42, "bar": "himom!", "class": "Cat"})

        entity = model._entity_from_ds_entity(datastore_entity)
        assert isinstance(entity, Cat)
        assert entity.foo == 42
        assert entity.bar == "himom!"
        assert entity.class_ == ["Cat"]


class Test_entity_to_protobuf:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_standard_case():
        class ThisKind(model.Model):
            a = model.IntegerProperty()
            b = model.BooleanProperty()
            c = model.PickleProperty()
            d = model.StringProperty(repeated=True)
            e = model.PickleProperty(repeated=True)
            notaproperty = True

        dill = {"sandwiches": ["turkey", "reuben"], "not_sandwiches": "tacos"}
        gherkin = [{"a": {"b": "c"}, "d": 0}, [1, 2, 3], "himom"]
        key = key_module.Key("ThisKind", 123, app="testing")

        entity = ThisKind(
            key=key,
            a=42,
            c=gherkin,
            d=["foo", "bar", "baz"],
            e=[gherkin, dill],
        )

        entity_pb = model._entity_to_protobuf(entity)
        assert isinstance(entity_pb, ds_types.Entity)
        assert entity_pb.properties["a"].integer_value == 42
        assert entity_pb.properties["b"].null_value == 0
        assert pickle.loads(entity_pb.properties["c"].blob_value) == gherkin
        d_values = entity_pb.properties["d"].array_value.values
        assert d_values[0].string_value == "foo"
        assert d_values[1].string_value == "bar"
        assert d_values[2].string_value == "baz"
        e_values = entity_pb.properties["e"].array_value.values
        assert pickle.loads(e_values[0].blob_value) == gherkin
        assert pickle.loads(e_values[1].blob_value) == dill
        assert "__key__" not in entity_pb.properties

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_property_named_key():
        class ThisKind(model.Model):
            key = model.StringProperty()

        key = key_module.Key("ThisKind", 123, app="testing")
        entity = ThisKind(key="not the key", _key=key)

        entity_pb = model._entity_to_protobuf(entity)
        assert entity_pb.properties["key"].string_value == "not the key"
        assert entity_pb.key.path[0].kind == "ThisKind"
        assert entity_pb.key.path[0].id == 123

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_override_property():
        class ThatKind(model.Model):
            a = model.StringProperty()

        class ThisKind(ThatKind):
            a = model.IntegerProperty()
            b = model.BooleanProperty()
            c = model.PickleProperty()
            d = model.StringProperty(repeated=True)
            e = model.PickleProperty(repeated=True)
            notaproperty = True

        dill = {"sandwiches": ["turkey", "reuben"], "not_sandwiches": "tacos"}
        gherkin = [{"a": {"b": "c"}, "d": 0}, [1, 2, 3], "himom"]
        key = key_module.Key("ThisKind", 123, app="testing")

        entity = ThisKind(
            key=key,
            a=42,
            c=gherkin,
            d=["foo", "bar", "baz"],
            e=[gherkin, dill],
        )

        entity_pb = model._entity_to_protobuf(entity)
        assert isinstance(entity_pb, ds_types.Entity)
        assert entity_pb.properties["a"].integer_value == 42
        assert entity_pb.properties["b"].null_value == 0
        assert pickle.loads(entity_pb.properties["c"].blob_value) == gherkin
        d_values = entity_pb.properties["d"].array_value.values
        assert d_values[0].string_value == "foo"
        assert d_values[1].string_value == "bar"
        assert d_values[2].string_value == "baz"
        e_values = entity_pb.properties["e"].array_value.values
        assert pickle.loads(e_values[0].blob_value) == gherkin
        assert pickle.loads(e_values[1].blob_value) == dill
        assert "__key__" not in entity_pb.properties

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_uninitialized_property():
        class ThisKind(model.Model):
            foo = model.StringProperty(required=True)

        entity = ThisKind()

        with pytest.raises(exceptions.BadValueError):
            model._entity_to_protobuf(entity)


class TestExpando:
    @staticmethod
    def test_constructor():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x", bar="y", baz="z")
        assert expansive._properties == {"foo": "x", "bar": "y", "baz": "z"}
        # Make sure we didn't change properties for the class
        assert Expansive._properties == {"foo": "foo"}

    @staticmethod
    def test___getattr__():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x", bar="y", baz="z")
        assert expansive.bar == "y"

    @staticmethod
    def test___getattr__from_model():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x", bar="y", baz="z")
        assert expansive._default_filters() == ()

    @staticmethod
    def test___getattr__from_model_error():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x", bar="y", baz="z")
        with pytest.raises(AttributeError):
            expansive.notaproperty

    @staticmethod
    def test___setattr__with_model():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x", bar=model.Model())
        assert isinstance(expansive.bar, model.Model)

    @staticmethod
    def test___setattr__with_dict():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x", bar={"bar": "y", "baz": "z"})
        assert expansive.bar.baz == "z"

    @staticmethod
    def test___setattr__with_dotted_name():
        """Regression test for issue #673

        https://github.com/googleapis/python-ndb/issues/673
        """

        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x")
        setattr(expansive, "a.b", "one")
        assert expansive.a.b == "one"

        setattr(expansive, "a.c", "two")
        assert expansive.a.b == "one"
        assert expansive.a.c == "two"

    @staticmethod
    def test___delattr__():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x")
        expansive.baz = "y"
        assert expansive._properties == {"foo": "x", "baz": "y"}
        del expansive.baz
        assert expansive._properties == {"foo": "x"}

    @staticmethod
    def test___delattr__from_model():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x")
        with pytest.raises(AttributeError):
            del expansive._nnexistent

    @staticmethod
    def test___delattr__non_property():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x")
        expansive.baz = "y"
        expansive._properties["baz"] = "Not a Property"
        with pytest.raises(TypeError):
            del expansive.baz

    @staticmethod
    def test___delattr__runtime_error():
        class Expansive(model.Expando):
            foo = model.StringProperty()

        expansive = Expansive(foo="x")
        expansive.baz = "y"
        model.Model._properties["baz"] = "baz"
        with pytest.raises(RuntimeError):
            del expansive.baz


class Test__legacy_db_get_value:
    @staticmethod
    def test_str_blobkey():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.BLOBKEY)
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"foo")
        assert prop._legacy_db_get_value(v, p) == model.BlobKey(b"foo")

    @staticmethod
    def test_str_blob():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.BLOB)
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"foo")
        assert prop._legacy_db_get_value(v, p) == b"foo"

    @staticmethod
    def test_str_blob_compressed():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.BLOB)
        p.set_meaning_uri("ZLIB")
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"foo")
        assert prop._legacy_db_get_value(v, p) == b"foo"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_str_entity_proto():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.ENTITY_PROTO)
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"\x6a\x03\x6a\x01\x42")
        assert isinstance(prop._legacy_db_get_value(v, p), model.Expando)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_str_entity_proto_no_key():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.ENTITY_PROTO)
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"\x72\x0a\x0b\x12\x01\x44\x18\x01\x22\x01\x45\x0c")
        assert isinstance(prop._legacy_db_get_value(v, p), model.Expando)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_str_entity_proto_bad():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.ENTITY_PROTO)
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"\x6a\x0c\x72\x0a\x0b\x12\x01\x44\x18\x01\x22\x01\x45\x0c")
        with pytest.raises(ValueError):
            prop._legacy_db_get_value(v, p)

    @staticmethod
    def test_str_bytestr_meaning():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.BYTESTRING)
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"foo")
        assert prop._legacy_db_get_value(v, p) == b"foo"

    @staticmethod
    def test_str_utf8():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        v.has_stringvalue_ = 1
        v.stringvalue_ = bytes("fo\xc3", encoding="utf-8")
        assert prop._legacy_db_get_value(v, p) == "fo\xc3"

    @staticmethod
    def test_str_decode_error():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        v.set_stringvalue(b"\xe9")
        assert prop._legacy_db_get_value(v, p) == b"\xe9"

    @staticmethod
    def test_int_gd_when():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.GD_WHEN)
        v = _legacy_entity_pb.PropertyValue()
        v.set_int64value(42)
        d = datetime.datetime(1970, 1, 1, 0, 0, 0, 42)
        assert prop._legacy_db_get_value(v, p) == d

    @staticmethod
    def test_boolean():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        v.set_booleanvalue(True)
        assert prop._legacy_db_get_value(v, p) is True

    @staticmethod
    def test_double():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        v.set_doublevalue(3.1415)
        assert prop._legacy_db_get_value(v, p) == 3.1415

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_reference():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        r = _legacy_entity_pb.PropertyValue_ReferenceValue()
        e = _legacy_entity_pb.PropertyValue_ReferenceValuePathElement()
        e.set_type("a")
        e.set_id("b")
        r.pathelement_ = [e]
        r.set_app("c")
        v.mutable_referencevalue()
        v.referencevalue_ = r
        key = key_module.Key("a", "b", app="c", namespace="")
        assert prop._legacy_db_get_value(v, p) == key

    @staticmethod
    def test_point():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        r = _legacy_entity_pb.PropertyValue_PointValue()
        r.set_x(10)
        r.set_y(20)
        v.mutable_pointvalue()
        v.pointvalue_ = r
        assert prop._legacy_db_get_value(v, p) == model.GeoPt(10, 20)

    @staticmethod
    def test_user():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        u = _legacy_entity_pb.PropertyValue_UserValue()
        user = model.User(email="aol@aol.com", _auth_domain="aol.com", _user_id="loa")
        u.set_email(b"aol@aol.com")
        u.set_auth_domain(b"aol.com")
        u.set_obfuscated_gaiaid(b"loa")
        v.mutable_uservalue()
        v.uservalue_ = u
        assert prop._legacy_db_get_value(v, p) == user

    @staticmethod
    def test_missing():
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        assert prop._legacy_db_get_value(v, p) is None


class Test__legacy_deserialize:
    @staticmethod
    def test_empty_list():
        m = model.Model()
        prop = model.Property()
        p = _legacy_entity_pb.Property()
        p.set_meaning(_legacy_entity_pb.Property.EMPTY_LIST)
        assert prop._legacy_deserialize(m, p) is None

    @staticmethod
    def test_repeated():
        m = model.Model()
        prop = model.Property(repeated=True)
        p = _legacy_entity_pb.Property()
        assert prop._legacy_deserialize(m, p) is None

    @staticmethod
    def test_repeated_with_value():
        m = model.Model()
        prop = model.Property(repeated=True)
        prop._store_value(m, [41])
        p = _legacy_entity_pb.Property()
        v = _legacy_entity_pb.PropertyValue()
        v.set_int64value(42)
        assert prop._legacy_deserialize(m, p) is None


class Test__get_property_for:
    @staticmethod
    def test_depth_bigger_than_parts():
        m = model.Model()
        p = _legacy_entity_pb.Property()
        p.set_name(b"foo")
        assert m._get_property_for(p, depth=5) is None

    @staticmethod
    def test_none():
        m = model.Model()
        p = _legacy_entity_pb.Property()
        p.set_name(b"foo")
        assert m._get_property_for(p)._name == "foo"


class Test__from_pb:
    @staticmethod
    def test_not_entity_proto_raises_error():
        m = model.Model()
        with pytest.raises(TypeError):
            m._from_pb("not a pb")

    @staticmethod
    def test_with_key():
        m = model.Model()
        pb = _legacy_entity_pb.EntityProto()
        key = key_module.Key("a", "b", app="c", database="", namespace="")
        ent = m._from_pb(pb, key=key)
        assert ent.key == key

    @staticmethod
    def test_with_index_meaning():
        m = model.Model()
        pb = _legacy_entity_pb.EntityProto()
        p = _legacy_entity_pb.Property()
        p.set_name(b"foo")
        p.set_meaning(_legacy_entity_pb.Property.INDEX_VALUE)
        pb.property_ = [p]
        ent = m._from_pb(pb)
        assert "foo" in ent._projection


class Test__fake_property:
    @staticmethod
    def test_with_clone_properties():
        def clone():
            pass

        m = model.Model()
        m._clone_properties = clone
        p = _legacy_entity_pb.Property()
        p.set_name(b"foo")
        fake = m._fake_property(p, "next")
        assert fake._name == "next"

    @staticmethod
    def test_with_same_name():
        m = model.Model()
        p = _legacy_entity_pb.Property()
        p.set_name(b"next")
        fake = m._fake_property(p, "next")
        assert fake._name == "next"


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.key.Key")
@mock.patch("google.cloud.ndb.tasklets.Future")
def test_get_multi(Key, Future):
    model1 = model.Model()
    future1 = tasklets.Future()
    future1.result.return_value = model1

    key1 = key_module.Key("a", "b", app="c")
    key1.get_async.return_value = future1

    keys = [key1]
    assert model.get_multi(keys) == [model1]


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.key.Key")
def test_get_multi_async(Key):
    future1 = tasklets.Future()

    key1 = key_module.Key("a", "b", app="c")
    key1.get_async.return_value = future1

    keys = [key1]
    assert model.get_multi_async(keys) == [future1]


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.model.Model")
def test_put_multi_async(Model):
    future1 = tasklets.Future()

    model1 = model.Model()
    model1.put_async.return_value = future1

    models = [model1]
    assert model.put_multi_async(models) == [future1]


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.model.Model")
@mock.patch("google.cloud.ndb.tasklets.Future")
def test_put_multi(Model, Future):
    key1 = key_module.Key("a", "b", app="c")
    future1 = tasklets.Future()
    future1.result.return_value = key1

    model1 = model.Model()
    model1.put_async.return_value = future1

    models = [model1]
    assert model.put_multi(models) == [key1]


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.key.Key")
def test_delete_multi_async(Key):
    future1 = tasklets.Future()

    key1 = key_module.Key("a", "b", app="c")
    key1.delete_async.return_value = future1

    keys = [key1]
    assert model.delete_multi_async(keys) == [future1]


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb.key.Key")
@mock.patch("google.cloud.ndb.tasklets.Future")
def test_delete_multi(Key, Future):
    future1 = tasklets.Future()
    future1.result.return_value = None

    key1 = key_module.Key("a", "b", app="c")
    key1.delete_async.return_value = future1

    keys = [key1]
    assert model.delete_multi(keys) == [None]


def test_get_indexes_async():
    with pytest.raises(NotImplementedError):
        model.get_indexes_async()


def test_get_indexes():
    with pytest.raises(NotImplementedError):
        model.get_indexes()


@pytest.mark.usefixtures("in_context")
def test_serialization():
    # This is needed because pickle can't serialize local objects
    global SomeKind, OtherKind

    class OtherKind(model.Model):
        foo = model.IntegerProperty()

        @classmethod
        def _get_kind(cls):
            return "OtherKind"

    class SomeKind(model.Model):
        other = model.StructuredProperty(OtherKind)

        @classmethod
        def _get_kind(cls):
            return "SomeKind"

    entity = SomeKind(other=OtherKind(foo=1, namespace="Test"), namespace="Test")
    assert entity.other.key is None or entity.other.key.id() is None
    entity = pickle.loads(pickle.dumps(entity))
    assert entity.other.foo == 1


class Test_Keyword_Name:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_property_named_project():
        class HasProjectProp(model.Model):
            project = model.StringProperty()

        has_project_prop = HasProjectProp(
            project="the-property", _project="the-ds-project"
        )
        assert has_project_prop.project == "the-property"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_property_named_app():
        class HasAppProp(model.Model):
            app = model.StringProperty()

        has_app_prop = HasAppProp(app="the-property", _app="the-gae-app")
        assert has_app_prop.app == "the-property"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_property_named_database():
        class HasDbProp(model.Model):
            database = model.StringProperty()

        has_db_prop = HasDbProp(database="the-property", _database="the-ds-database")
        assert has_db_prop.database == "the-property"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_property_named_namespace():
        class HasNamespaceProp(model.Model):
            namespace = model.StringProperty()

        has_namespace_prop = HasNamespaceProp(
            namespace="the-property", _namespace="the-ds-namespace"
        )
        assert has_namespace_prop.namespace == "the-property"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_property_named_key():
        k = key_module.Key("HasKeyProp", "k")

        class HasKeyProp(model.Model):
            key = model.StringProperty()

        has_key_prop = HasKeyProp(key="the-property", _key=k)
        assert has_key_prop.key == "the-property"
        assert has_key_prop._key == k


def ManyFieldsFactory():
    """Model type class factory.

    This indirection makes sure ``Model._kind_map`` isn't mutated at module
    scope, since any mutations would be reset by the ``reset_state`` fixture
    run for each test.
    """

    class ManyFields(model.Model):
        self = model.IntegerProperty()
        id = model.StringProperty()
        key = model.FloatProperty(repeated=True)
        value = model.StringProperty()
        unused = model.FloatProperty()

    return ManyFields


def test_model_set_projection_branches():
    class Child(model.Model):
        val = model.StringProperty()

    class Parent(model.Model):
        child = model.StructuredProperty(Child)
        children = model.StructuredProperty(Child, repeated=True)

    parent = Parent(child=Child(val="a"), children=[Child(val="b")])
    parent._set_projection(["child.val", "children.val", "nonexistent.subprop"])
    parent._properties = None
    parent._set_projection(["child.val"])
