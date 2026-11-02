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

from unittest import mock

import pytest
from google.cloud.datastore import helpers

from google.cloud import datastore
from google.cloud.ndb import model, polymodel, query

from . import utils


def test___all__():
    utils.verify___all__(polymodel)


class Test_ClassKeyProperty:
    @staticmethod
    def test_constructor():
        prop = polymodel._ClassKeyProperty()
        assert prop._name == polymodel._CLASS_KEY_PROPERTY

    @staticmethod
    def test__set_value():
        prop = polymodel._ClassKeyProperty()
        with pytest.raises(TypeError):
            prop._set_value(None, None)

    @staticmethod
    def test__get_value():
        prop = polymodel._ClassKeyProperty()
        value = ["test"]
        values = {prop._name: value}
        entity = mock.Mock(
            _projection=(prop._name,),
            _values=values,
            spec=("_projection", "_values"),
        )
        assert value is prop._get_value(entity)

    @staticmethod
    def test__prepare_for_put():
        prop = polymodel._ClassKeyProperty()
        value = ["test"]
        values = {prop._name: value}
        entity = mock.Mock(
            _projection=(prop._name,),
            _values=values,
            spec=("_projection", "_values"),
        )
        assert prop._prepare_for_put(entity) is None


class TestPolyModel:
    @staticmethod
    def test_constructor():
        model = polymodel.PolyModel()
        assert model.__dict__ == {"_values": {}}

    @staticmethod
    def test_class_property():
        class Animal(polymodel.PolyModel):
            pass

        class Feline(Animal):
            pass

        class Cat(Feline):
            pass

        cat = Cat()

        assert cat._get_kind() == "Animal"
        assert cat.class_ == ["Animal", "Feline", "Cat"]

    @staticmethod
    def test_default_filters():
        class Animal(polymodel.PolyModel):
            pass

        class Cat(Animal):
            pass

        assert Animal._default_filters() == ()
        assert Cat._default_filters() == (query.FilterNode("class", "=", "Cat"),)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_entity_from_protobuf():
        class Animal(polymodel.PolyModel):
            pass

        class Cat(Animal):
            pass

        key = datastore.Key("Animal", 123, project="testing")
        datastore_entity = datastore.Entity(key=key)
        datastore_entity["class"] = ["Animal", "Cat"]
        protobuf = helpers.entity_to_protobuf(datastore_entity)
        entity = model._entity_from_protobuf(protobuf)
        assert isinstance(entity, Cat)
