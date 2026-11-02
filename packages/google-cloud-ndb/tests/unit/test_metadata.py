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

from google.cloud.ndb import exceptions, metadata, tasklets
from google.cloud.ndb import key as key_module

from . import utils


def test___all__():
    utils.verify___all__(metadata)


class Test_BaseMetadata:
    @staticmethod
    def test_get_kind():
        kind = metadata._BaseMetadata.KIND_NAME
        assert metadata._BaseMetadata._get_kind() == kind

    @staticmethod
    def test_cannot_instantiate():
        with pytest.raises(TypeError):
            metadata._BaseMetadata()


class TestEntityGroup:
    @staticmethod
    def test_constructor():
        with pytest.raises(exceptions.NoLongerImplementedError):
            metadata.EntityGroup()


class TestKind:
    @staticmethod
    def test_get_kind():
        kind = metadata.Kind.KIND_NAME
        assert metadata.Kind._get_kind() == kind

    @staticmethod
    def test_constructor():
        kind = metadata.Kind()
        assert kind.__dict__ == {"_values": {}}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_for_kind():
        key = key_module.Key(metadata.Kind.KIND_NAME, "test")
        assert key == metadata.Kind.key_for_kind("test")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_to_kind():
        key = key_module.Key(metadata.Kind.KIND_NAME, "test")
        assert metadata.Kind.key_to_kind(key) == "test"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_kind_name():
        key = key_module.Key(metadata.Kind.KIND_NAME, "test")
        kind = metadata.Kind(key=key)
        assert kind.kind_name == "test"


class TestNamespace:
    @staticmethod
    def test_get_kind():
        kind = metadata.Namespace.KIND_NAME
        assert metadata.Namespace._get_kind() == kind

    @staticmethod
    def test_constructor():
        namespace = metadata.Namespace()
        assert namespace.__dict__ == {"_values": {}}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_for_namespace():
        key = key_module.Key(metadata.Namespace.KIND_NAME, "test")
        assert key == metadata.Namespace.key_for_namespace("test")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_for_namespace_default():
        key = key_module.Key(metadata.Namespace.KIND_NAME, "")
        assert key == metadata.Namespace.key_for_namespace("")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_for_namespace_empty():
        key = key_module.Key(
            metadata.Namespace.KIND_NAME, metadata.Namespace.EMPTY_NAMESPACE_ID
        )
        assert key == metadata.Namespace.key_for_namespace(None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_to_namespace():
        key = key_module.Key(metadata.Namespace.KIND_NAME, "test")
        assert metadata.Namespace.key_to_namespace(key) == "test"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_namespace_name():
        key = key_module.Key(metadata.Namespace.KIND_NAME, "test")
        namespace = metadata.Namespace(key=key)
        assert namespace.namespace_name == "test"


class TestProperty:
    @staticmethod
    def test_get_kind():
        kind = metadata.Property.KIND_NAME
        assert metadata.Property._get_kind() == kind

    @staticmethod
    def test_constructor():
        property = metadata.Property()
        assert property.__dict__ == {"_values": {}}

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_for_kind():
        key = key_module.Key(metadata.Kind.KIND_NAME, "test")
        assert key == metadata.Property.key_for_kind("test")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_to_kind():
        kind = key_module.Key(metadata.Kind.KIND_NAME, "test")
        assert metadata.Property.key_to_kind(kind) == "test"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_kind_name():
        key = key_module.Key(
            metadata.Kind.KIND_NAME,
            "test",
            metadata.Property.KIND_NAME,
            "test2",
        )
        property = metadata.Property(key=key)
        assert property.kind_name == "test"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_for_property():
        key = key_module.Key(
            metadata.Kind.KIND_NAME,
            "test",
            metadata.Property.KIND_NAME,
            "test2",
        )
        assert key == metadata.Property.key_for_property("test", "test2")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_to_property():
        kind = key_module.Key(metadata.Property.KIND_NAME, "test")
        assert metadata.Property.key_to_property(kind) == "test"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_key_to_property_only_kind():
        kind = key_module.Key(metadata.Kind.KIND_NAME, "test")
        assert metadata.Property.key_to_property(kind) is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_property_name():
        key = key_module.Key(
            metadata.Kind.KIND_NAME,
            "test",
            metadata.Property.KIND_NAME,
            "test2",
        )
        property = metadata.Property(key=key)
        assert property.property_name == "test2"


@pytest.mark.usefixtures("in_context")
def test_get_entity_group_version(*args, **kwargs):
    with pytest.raises(exceptions.NoLongerImplementedError):
        metadata.get_entity_group_version()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_kinds(_datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    kinds = metadata.get_kinds()
    assert kinds == []


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_kinds_with_start(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    kinds = metadata.get_kinds(start="a")
    assert kinds == []
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_kinds_with_end(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    kinds = metadata.get_kinds(end="z")
    assert kinds == []
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_kinds_empty_end(_datastore_query):
    future = tasklets.Future("fetch")
    future.set_result(["not", "empty"])
    _datastore_query.fetch.return_value = future
    kinds = metadata.get_kinds(end="")
    assert kinds == []


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_namespaces(_datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    names = metadata.get_namespaces()
    assert names == []


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_namespaces_with_start(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    names = metadata.get_namespaces(start="a")
    assert names == []
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_namespaces_with_end(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    names = metadata.get_namespaces(end="z")
    assert names == []
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_properties_of_kind(_datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    props = metadata.get_properties_of_kind("AnyKind")
    assert props == []


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_properties_of_kind_with_start(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    props = metadata.get_properties_of_kind("AnyKind", start="a")
    assert props == []
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_properties_of_kind_with_end(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    props = metadata.get_properties_of_kind("AnyKind", end="z")
    assert props == []
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_properties_of_kind_empty_end(_datastore_query):
    future = tasklets.Future("fetch")
    future.set_result(["not", "empty"])
    _datastore_query.fetch.return_value = future
    props = metadata.get_properties_of_kind("AnyKind", end="")
    assert props == []


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_representations_of_kind(_datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    reps = metadata.get_representations_of_kind("AnyKind")
    assert reps == {}


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_representations_of_kind_with_results(_datastore_query):
    class MyProp:
        property_name = "myprop"
        property_representation = "STR"

    myprop = MyProp()
    future = tasklets.Future("fetch")
    future.set_result([myprop])
    _datastore_query.fetch.return_value = future
    reps = metadata.get_representations_of_kind("MyModel")
    assert reps == {"myprop": "STR"}


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_representations_of_kind_with_start(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    reps = metadata.get_representations_of_kind("AnyKind", start="a")
    assert reps == {}
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
@mock.patch("google.cloud.ndb.query.Query")
def test_get_representations_of_kind_with_end(Query, _datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    query = Query.return_value
    reps = metadata.get_representations_of_kind("AnyKind", end="z")
    assert reps == {}
    query.filter.assert_called_once()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_query")
def test_get_representations_of_kind_empty_end(_datastore_query):
    future = tasklets.Future("fetch")
    future.set_result([])
    _datastore_query.fetch.return_value = future
    reps = metadata.get_representations_of_kind("AnyKind", end="")
    assert reps == {}
