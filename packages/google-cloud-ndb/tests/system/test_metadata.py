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

"""
System tests for metadata.
"""

from importlib import reload

import pytest
from test_utils import retry

from google.cloud import ndb

_retry_assertion_errors = retry.RetryErrors(AssertionError)


@pytest.mark.usefixtures("client_context")
def test_kind_metadata(dispose_of, database_id):
    # ndb.Model._kind_map gets reset in-between parameterized test runs, which results in failed kind lookups for the
    # Kind metadata when we query later. Importing the metadata module has the effect of priming the kind map,
    # so force a reload here to retrigger it.
    from google.cloud.ndb import metadata

    reload(metadata)

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()

    class MyKind(ndb.Model):
        bar = ndb.StringProperty()

    entity1 = AnyKind(foo=1, id="x", database=database_id, namespace="_test_namespace_")
    entity1.put()
    dispose_of(entity1.key._key)

    entity2 = MyKind(
        bar="x", id="x", database=database_id, namespace="_test_namespace_"
    )
    entity2.put()
    dispose_of(entity2.key._key)

    @_retry_assertion_errors
    def query_metadata():
        query = ndb.Query(
            kind=ndb.metadata.Kind.KIND_NAME, namespace="_test_namespace_"
        )  # database is implicit
        results = query.fetch()
        kinds = [result.kind_name for result in results]
        assert all(kind in kinds for kind in ["AnyKind", "MyKind"])

    query_metadata()


@pytest.mark.usefixtures("client_context")
def test_get_kinds(dispose_of):
    from google.cloud.ndb.metadata import get_kinds

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()

    class MyKind(ndb.Model):
        bar = ndb.StringProperty()

    class OtherKind(ndb.Model):
        baz = ndb.IntegerProperty()

    class SomeKind(ndb.Model):
        qux = ndb.StringProperty()

    entity1 = AnyKind(foo=1)
    entity1.put()
    dispose_of(entity1.key._key)

    entity2 = MyKind(bar="a")
    entity2.put()
    dispose_of(entity2.key._key)

    entity3 = OtherKind(baz=2)
    entity3.put()
    dispose_of(entity3.key._key)

    entity4 = SomeKind(qux="a")
    entity4.put()
    dispose_of(entity4.key._key)

    @_retry_assertion_errors
    def query_metadata():
        kinds = get_kinds()
        assert all(
            kind in kinds for kind in ["AnyKind", "MyKind", "OtherKind", "SomeKind"]
        )

        kinds = get_kinds(start="N")
        assert all(kind in kinds for kind in ["OtherKind", "SomeKind"]) != []
        assert not any(kind in kinds for kind in ["AnyKind", "MyKind"])

        kinds = get_kinds(end="N")
        assert all(kind in kinds for kind in ["AnyKind", "MyKind"]) != []
        assert not any(kind in kinds for kind in ["OtherKind", "SomeKind"])

        kinds = get_kinds(start="L", end="P")
        assert all(kind in kinds for kind in ["MyKind", "OtherKind"]) != []
        assert not any(kind in kinds for kind in ["AnyKind", "SomeKind"])

    query_metadata()


@pytest.mark.usefixtures("client_context")
def test_namespace_metadata(dispose_of):
    from google.cloud.ndb.metadata import Namespace

    # Why is this not necessary for Kind?
    Namespace._fix_up_properties()

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()

    entity1 = AnyKind(foo=1, namespace="_test_namespace_")
    entity1.put()
    dispose_of(entity1.key._key)

    entity2 = AnyKind(foo=2, namespace="_test_namespace_2_")
    entity2.put()
    dispose_of(entity2.key._key)

    @_retry_assertion_errors
    def query_metadata():
        query = ndb.Query(kind=Namespace.KIND_NAME)
        results = query.fetch()

        names = [result.namespace_name for result in results]
        assert all(name in names for name in ["_test_namespace_", "_test_namespace_2_"])

    query_metadata()


@pytest.mark.usefixtures("client_context")
def test_get_namespaces(dispose_of):
    from google.cloud.ndb.metadata import get_namespaces

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()

    entity1 = AnyKind(foo=1, namespace="CoolNamespace")
    entity1.put()
    dispose_of(entity1.key._key)

    entity2 = AnyKind(foo=2, namespace="MyNamespace")
    entity2.put()
    dispose_of(entity2.key._key)

    entity3 = AnyKind(foo=3, namespace="OtherNamespace")
    entity3.put()
    dispose_of(entity3.key._key)

    @_retry_assertion_errors
    def query_metadata():
        names = get_namespaces()
        assert all(
            name in names for name in ["CoolNamespace", "MyNamespace", "OtherNamespace"]
        )

        names = get_namespaces(start="L")
        assert all(name in names for name in ["MyNamespace", "OtherNamspace"]) != []

        names = get_namespaces(end="N")
        assert all(name in names for name in ["CoolNamespace", "MyNamespace"]) != []

        names = get_namespaces(start="D", end="N")
        assert all(name in names for name in ["MyNamespace"]) != []

    query_metadata()


@pytest.mark.usefixtures("client_context")
def test_property_metadata(dispose_of):
    from google.cloud.ndb.metadata import Property

    # Why is this not necessary for Kind?
    Property._fix_up_properties()

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()
        bar = ndb.StringProperty()

    entity1 = AnyKind(foo=1, bar="x")
    entity1.put()
    dispose_of(entity1.key._key)

    @_retry_assertion_errors
    def query_metadata():
        query = ndb.Query(kind=Property.KIND_NAME)
        results = query.fetch()

        properties = [
            result.property_name for result in results if result.kind_name == "AnyKind"
        ]
        assert properties == ["bar", "foo"]

    query_metadata()


@pytest.mark.usefixtures("client_context")
def test_get_properties_of_kind(dispose_of):
    from google.cloud.ndb.metadata import get_properties_of_kind

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()
        bar = ndb.StringProperty()
        baz = ndb.IntegerProperty()
        qux = ndb.StringProperty()

    entity1 = AnyKind(foo=1, bar="x", baz=3, qux="y")
    entity1.put()
    dispose_of(entity1.key._key)

    @_retry_assertion_errors
    def query_metadata():
        properties = get_properties_of_kind("AnyKind")
        assert properties == ["bar", "baz", "foo", "qux"]

        properties = get_properties_of_kind("AnyKind", start="c")
        assert properties == ["foo", "qux"]

        properties = get_properties_of_kind("AnyKind", end="e")
        assert properties == ["bar", "baz"]

        properties = get_properties_of_kind("AnyKind", start="c", end="p")
        assert properties == ["foo"]

    query_metadata()


@pytest.mark.usefixtures("client_context")
@pytest.mark.parametrize("namespace", ["DiffNamespace"])
def test_get_properties_of_kind_different_namespace(dispose_of, namespace):
    from google.cloud.ndb.metadata import get_properties_of_kind

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()
        bar = ndb.StringProperty()
        baz = ndb.IntegerProperty()
        qux = ndb.StringProperty()

    entity1 = AnyKind(foo=1, bar="x", baz=3, qux="y", namespace="DiffNamespace")
    entity1.put()
    dispose_of(entity1.key._key)

    @_retry_assertion_errors
    def query_metadata():
        properties = get_properties_of_kind("AnyKind")
        assert properties == ["bar", "baz", "foo", "qux"]

        properties = get_properties_of_kind("AnyKind", start="c")
        assert properties == ["foo", "qux"]

        properties = get_properties_of_kind("AnyKind", end="e")
        assert properties == ["bar", "baz"]

        properties = get_properties_of_kind("AnyKind", start="c", end="p")
        assert properties == ["foo"]

    query_metadata()


@pytest.mark.usefixtures("client_context")
def test_get_representations_of_kind(dispose_of):
    from google.cloud.ndb.metadata import get_representations_of_kind

    class AnyKind(ndb.Model):
        foo = ndb.IntegerProperty()
        bar = ndb.StringProperty()
        baz = ndb.IntegerProperty()
        qux = ndb.StringProperty()

    entity1 = AnyKind(foo=1, bar="x", baz=3, qux="y")
    entity1.put()
    dispose_of(entity1.key._key)

    @_retry_assertion_errors
    def query_metadata():
        representations = get_representations_of_kind("AnyKind")
        assert representations == {
            "bar": ["STRING"],
            "baz": ["INT64"],
            "foo": ["INT64"],
            "qux": ["STRING"],
        }

        representations = get_representations_of_kind("AnyKind", start="c")
        assert representations == {"foo": ["INT64"], "qux": ["STRING"]}

        representations = get_representations_of_kind("AnyKind", end="e")
        assert representations == {"bar": ["STRING"], "baz": ["INT64"]}

        representations = get_representations_of_kind("AnyKind", start="c", end="p")
        assert representations == {"foo": ["INT64"]}

    query_metadata()
