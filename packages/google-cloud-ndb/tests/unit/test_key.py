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
import pickle
from unittest import mock

import google.cloud.datastore
import pytest
from google.cloud.datastore import _app_engine_key_pb2

from google.cloud.ndb import _options, exceptions, model, tasklets
from google.cloud.ndb import key as key_module

from . import utils


def test___all__():
    utils.verify___all__(key_module)


class TestKey:
    URLSAFE = b"agZzfmZpcmVyDwsSBEtpbmQiBVRoaW5nDA"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_default():
        key = key_module.Key("Kind", 42)

        assert key._key == google.cloud.datastore.Key("Kind", 42, project="testing")
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_unicode():
        """Regression test for #322.

        https://github.com/googleapis/python-ndb/issues/322
        """
        key = key_module.Key("Kind", 42)

        assert key._key == google.cloud.datastore.Key("Kind", 42, project="testing")
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_different_database(context):
        context.client.database = "DiffDatabase"
        key = key_module.Key("Kind", 42)

        assert key._key == google.cloud.datastore.Key(
            "Kind", 42, project="testing", database="DiffDatabase"
        )
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_different_namespace(context):
        context.client.namespace = "DiffNamespace"
        key = key_module.Key("Kind", 42)

        assert key._key == google.cloud.datastore.Key(
            "Kind", 42, project="testing", namespace="DiffNamespace"
        )
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_empty_path():
        with pytest.raises(TypeError):
            key_module.Key(pairs=())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_partial():
        with pytest.raises(ValueError):
            key_module.Key("Kind")

        key = key_module.Key("Kind", None)

        assert key._key.is_partial
        assert key._key.flat_path == ("Kind",)
        assert key._key.project == "testing"
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_invalid_id_type():
        with pytest.raises(TypeError):
            key_module.Key("Kind", object())
        with pytest.raises(exceptions.BadArgumentError):
            key_module.Key("Kind", None, "Also", 10)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_invalid_kind_type():
        with pytest.raises(TypeError):
            key_module.Key(object(), 47)
        with pytest.raises(AttributeError):
            key_module.Key(object, 47)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_kind_as_model():
        class Simple(model.Model):
            pass

        key = key_module.Key(Simple, 47)
        assert key._key == google.cloud.datastore.Key("Simple", 47, project="testing")
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_reference():
        reference = make_reference()
        key = key_module.Key(reference=reference)

        assert key._key == google.cloud.datastore.Key(
            "Parent",
            59,
            "Child",
            "Feather",
            project="sample-app",
            database="base",
            namespace="space",
        )
        assert key._reference is reference

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_serialized():
        serialized = b"j\x18s~sample-app-no-locationr\n\x0b\x12\x04Zorp\x18X\x0c"
        key = key_module.Key(serialized=serialized)

        assert key._key == google.cloud.datastore.Key(
            "Zorp", 88, project="sample-app-no-location"
        )
        assert key._reference == make_reference(
            path=({"type": "Zorp", "id": 88},),
            app="s~sample-app-no-location",
            database=None,
            namespace=None,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_serialized_with_database():
        serialized = b"j\x18s~sample-app-no-locationr\n\x0b\x12\x04Zorp\x18X\x0c\xba\x01\tsample-db"
        key = key_module.Key(serialized=serialized)

        assert key._key == google.cloud.datastore.Key(
            "Zorp", 88, project="sample-app-no-location", database="sample-db"
        )
        assert key._reference == make_reference(
            path=({"type": "Zorp", "id": 88},),
            app="s~sample-app-no-location",
            database="sample-db",
            namespace=None,
        )

    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_urlsafe(self):
        key = key_module.Key(urlsafe=self.URLSAFE)

        assert key._key == google.cloud.datastore.Key("Kind", "Thing", project="fire")
        assert key._reference == make_reference(
            path=({"type": "Kind", "name": "Thing"},),
            app="s~fire",
            database=None,
            namespace=None,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_pairs():
        key = key_module.Key(pairs=[("Kind", 1)])

        assert key._key == google.cloud.datastore.Key("Kind", 1, project="testing")
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_flat():
        key = key_module.Key(flat=["Kind", 1])

        assert key._key == google.cloud.datastore.Key("Kind", 1, project="testing")
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_flat_and_pairs():
        with pytest.raises(TypeError):
            key_module.Key(pairs=[("Kind", 1)], flat=["Kind", 1])

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_app():
        key = key_module.Key("Kind", 10, app="s~foo")

        assert key._key == google.cloud.datastore.Key("Kind", 10, project="foo")
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_project():
        key = key_module.Key("Kind", 10, project="foo")

        assert key._key == google.cloud.datastore.Key("Kind", 10, project="foo")
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_project_and_app():
        with pytest.raises(TypeError):
            key_module.Key("Kind", 10, project="foo", app="bar")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_default_database_as_empty_string():
        key = key_module.Key("Kind", 1337, database="")

        assert key._key == google.cloud.datastore.Key("Kind", 1337, project="testing")
        assert key.database() is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_database():
        key = key_module.Key("Kind", 1337, database="foo")

        assert key._key == google.cloud.datastore.Key(
            "Kind", 1337, project="testing", database="foo"
        )
        assert key.database() == "foo"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_namespace():
        key = key_module.Key("Kind", 1337, namespace="foo")

        assert key._key == google.cloud.datastore.Key(
            "Kind", 1337, project="testing", namespace="foo"
        )
        assert key.namespace() == "foo"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_default_namespace_as_empty_string(context):
        context.client.namespace = "DiffNamespace"
        key = key_module.Key("Kind", 1337, namespace="")

        assert key._key == google.cloud.datastore.Key("Kind", 1337, project="testing")
        assert key.namespace() is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_default_namespace_as_None(context):
        context.client.namespace = "DiffNamespace"
        key = key_module.Key("Kind", 1337, namespace=None)

        assert key._key == google.cloud.datastore.Key("Kind", 1337, project="testing")
        assert key.namespace() is None

    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_parent(self):
        parent = key_module.Key(urlsafe=self.URLSAFE)
        key = key_module.Key("Zip", 10, parent=parent)

        assert key._key == google.cloud.datastore.Key(
            "Kind", "Thing", "Zip", 10, project="fire"
        )
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_parent_and_database():
        parent = key_module.Key("Kind", "Thing", project="fire", database="foo")
        key = key_module.Key("Zip", 10, parent=parent, database="foo")

        assert key._key == google.cloud.datastore.Key(
            "Kind", "Thing", "Zip", 10, project="fire", database="foo"
        )
        assert key._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_parent_and_database_undefined():
        parent = key_module.Key("Kind", "Thing", project="fire", database="foo")
        key = key_module.Key("Zip", 10, parent=parent)

        assert key._key == google.cloud.datastore.Key(
            "Kind", "Thing", "Zip", 10, project="fire", database="foo"
        )
        assert key._reference is None

    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_parent_and_namespace(self):
        parent = key_module.Key(urlsafe=self.URLSAFE)
        key = key_module.Key("Zip", 10, parent=parent, namespace=None)

        assert key._key == google.cloud.datastore.Key(
            "Kind", "Thing", "Zip", 10, project="fire"
        )
        assert key._reference is None

    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_parent_and_mismatched_namespace(self):
        parent = key_module.Key(urlsafe=self.URLSAFE)
        with pytest.raises(ValueError):
            key_module.Key("Zip", 10, parent=parent, namespace="foo")

    @pytest.mark.usefixtures("in_context")
    def test_constructor_with_parent_bad_type(self):
        parent = mock.sentinel.parent
        with pytest.raises(exceptions.BadValueError):
            key_module.Key("Zip", 10, parent=parent)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_constructor_insufficient_args():
        with pytest.raises(TypeError):
            key_module.Key(app="foo")

    @pytest.mark.usefixtures("in_context")
    def test_no_subclass_for_reference(self):
        class KeySubclass(key_module.Key):
            pass

        with pytest.raises(TypeError):
            KeySubclass(urlsafe=self.URLSAFE)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_invalid_argument_combination():
        with pytest.raises(TypeError):
            key_module.Key(flat=["a", "b"], urlsafe=b"foo")

    @pytest.mark.usefixtures("in_context")
    def test_colliding_reference_arguments(self):
        urlsafe = self.URLSAFE
        padding = b"=" * (-len(urlsafe) % 4)
        serialized = base64.urlsafe_b64decode(urlsafe + padding)

        with pytest.raises(TypeError):
            key_module.Key(urlsafe=urlsafe, serialized=serialized)

    @staticmethod
    @mock.patch("google.cloud.ndb.key.Key.__init__")
    def test__from_ds_key(key_init):
        ds_key = google.cloud.datastore.Key("a", "b", project="c")
        key = key_module.Key._from_ds_key(ds_key)
        assert key._key is ds_key
        assert key._reference is None

        key_init.assert_not_called()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___repr__defaults():
        key = key_module.Key("a", "b")
        assert repr(key) == "Key('a', 'b')"
        assert str(key) == "Key('a', 'b')"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___repr__non_defaults():
        key = key_module.Key("X", 11, app="foo", namespace="bar", database="baz")
        assert (
            repr(key) == "Key('X', 11, project='foo', database='baz', namespace='bar')"
        )
        assert (
            str(key) == "Key('X', 11, project='foo', database='baz', namespace='bar')"
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___hash__():
        key1 = key_module.Key("a", 1)
        assert hash(key1) == hash(key1)
        assert hash(key1) == hash(key1.pairs())
        key2 = key_module.Key("a", 2)
        assert hash(key1) != hash(key2)

    @staticmethod
    def test__tuple():
        key = key_module.Key("X", 11, app="foo", database="d", namespace="n")
        assert key._tuple() == ("foo", "n", "d", (("X", 11),))

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___eq__():
        key1 = key_module.Key("X", 11, app="foo", namespace="n")
        key2 = key_module.Key("Y", 12, app="foo", namespace="n")
        key3 = key_module.Key("X", 11, app="bar", namespace="n")
        key4 = key_module.Key("X", 11, app="foo", namespace="m")
        key5 = mock.sentinel.key
        assert key1 == key1
        assert not key1 == key2
        assert not key1 == key3
        assert not key1 == key4
        assert not key1 == key5

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___ne__():
        key1 = key_module.Key("X", 11, app="foo", namespace="n")
        key2 = key_module.Key("Y", 12, app="foo", namespace="n")
        key3 = key_module.Key("X", 11, app="bar", namespace="n")
        key4 = key_module.Key("X", 11, app="foo", namespace="m")
        key5 = mock.sentinel.key
        key6 = key_module.Key("X", 11, app="foo", namespace="n")
        assert not key1 != key1
        assert key1 != key2
        assert key1 != key3
        assert key1 != key4
        assert key1 != key5
        assert not key1 != key6

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___lt__():
        key1 = key_module.Key("X", 11, app="foo", namespace="n")
        key2 = key_module.Key("Y", 12, app="foo", namespace="n")
        key3 = key_module.Key("X", 11, app="goo", namespace="n")
        key4 = key_module.Key("X", 11, app="foo", namespace="o")
        key5 = mock.sentinel.key
        key6 = key_module.Key("X", 11, app="foo", database="db", namespace="n")
        key7 = key_module.Key("X", 11, app="foo", database="db2", namespace="n")
        assert not key1 < key1
        assert key1 < key2
        assert key1 < key3
        assert key1 < key4
        with pytest.raises(TypeError):
            key1 < key5
        assert key1 < key6
        assert key6 < key7

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___le__():
        key1 = key_module.Key("X", 11, app="foo", namespace="n")
        key2 = key_module.Key("Y", 12, app="foo", namespace="n")
        key3 = key_module.Key("X", 11, app="goo", namespace="n")
        key4 = key_module.Key("X", 11, app="foo", namespace="o")
        key5 = mock.sentinel.key
        key6 = key_module.Key("X", 11, app="foo", database="db", namespace="n")
        key7 = key_module.Key("X", 11, app="foo", database="db2", namespace="n")
        assert key1 <= key1
        assert key1 <= key2
        assert key1 <= key3
        assert key1 <= key4
        with pytest.raises(TypeError):
            key1 <= key5
        assert key1 <= key6
        assert key6 <= key7

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___gt__():
        key1 = key_module.Key("X", 11, app="foo", namespace="n")
        key2 = key_module.Key("M", 10, app="foo", namespace="n")
        key3 = key_module.Key("X", 11, app="boo", namespace="n")
        key4 = key_module.Key("X", 11, app="foo", namespace="a")
        key5 = mock.sentinel.key
        key6 = key_module.Key("X", 11, app="foo", database="db", namespace="n")
        key7 = key_module.Key("X", 11, app="foo", database="db2", namespace="n")
        assert not key1 > key1
        assert key1 > key2
        assert key1 > key3
        assert key1 > key4
        with pytest.raises(TypeError):
            key1 > key5
        assert key6 > key1
        assert key7 > key6

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___ge__():
        key1 = key_module.Key("X", 11, app="foo", namespace="n")
        key2 = key_module.Key("M", 10, app="foo", namespace="n")
        key3 = key_module.Key("X", 11, app="boo", namespace="n")
        key4 = key_module.Key("X", 11, app="foo", namespace="a")
        key5 = mock.sentinel.key
        key6 = key_module.Key("X", 11, app="foo", database="db", namespace="n")
        key7 = key_module.Key("X", 11, app="foo", database="db2", namespace="n")
        assert key1 >= key1
        assert key1 >= key2
        assert key1 >= key3
        assert key1 >= key4
        with pytest.raises(TypeError):
            key1 >= key5
        assert key6 >= key1
        assert key7 >= key6

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_pickling():
        key = key_module.Key("a", "b", app="c", namespace="d")
        pickled = pickle.dumps(key)
        unpickled = pickle.loads(pickled)
        assert key == unpickled

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_pickling_with_default_database():
        key = key_module.Key("a", "b", app="c", namespace="d", database="")
        pickled = pickle.dumps(key)
        unpickled = pickle.loads(pickled)
        assert key == unpickled

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_pickling_with_database():
        key = key_module.Key("a", "b", app="c", namespace="d", database="e")
        pickled = pickle.dumps(key)
        unpickled = pickle.loads(pickled)
        assert key == unpickled

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test___setstate__bad_state():
        key = key_module.Key("a", "b")

        state = ("not", "length", "one")
        with pytest.raises(TypeError):
            key.__setstate__(state)

        state = ("not-a-dict",)
        with pytest.raises(TypeError):
            key.__setstate__(state)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_parent():
        key = key_module.Key("a", "b", "c", "d")
        parent = key.parent()
        assert parent._key == key._key.parent
        assert parent._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_parent_top_level():
        key = key_module.Key("This", "key")
        assert key.parent() is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_root():
        key = key_module.Key("a", "b", "c", "d")
        root = key.root()
        assert root._key == key._key.parent
        assert root._reference is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_root_top_level():
        key = key_module.Key("This", "key")
        assert key.root() is key

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_namespace():
        namespace = "my-space"
        key = key_module.Key("abc", 1, namespace=namespace)
        assert key.namespace() == namespace

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_app():
        app = "s~example"
        key = key_module.Key("X", 100, app=app)
        assert key.app() != app
        assert key.app() == app[2:]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_id():
        for id_or_name in ("x", 11, None):
            key = key_module.Key("Kind", id_or_name)
            assert key.id() == id_or_name

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_string_id():
        pairs = (("x", "x"), (11, None), (None, None))
        for id_or_name, expected in pairs:
            key = key_module.Key("Kind", id_or_name)
            assert key.string_id() == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_integer_id():
        pairs = (("x", None), (11, 11), (None, None))
        for id_or_name, expected in pairs:
            key = key_module.Key("Kind", id_or_name)
            assert key.integer_id() == expected

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_pairs():
        key = key_module.Key("a", "b")
        assert key.pairs() == (("a", "b"),)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_pairs_partial_key():
        key = key_module.Key("This", "key", "that", None)
        assert key.pairs() == (("This", "key"), ("that", None))

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_flat():
        key = key_module.Key("This", "key")
        assert key.flat() == ("This", "key")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_flat_partial_key():
        key = key_module.Key("Kind", None)
        assert key.flat() == ("Kind", None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_kind():
        key = key_module.Key("This", "key")
        assert key.kind() == "This"
        key = key_module.Key("a", "b", "c", "d")
        assert key.kind() == "c"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_reference():
        key = key_module.Key(
            "This", "key", app="fire", database="db", namespace="namespace"
        )
        assert key.reference() == make_reference(
            path=({"type": "This", "name": "key"},),
            app="fire",
            database="db",
            namespace="namespace",
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_reference_cached():
        key = key_module.Key("This", "key")
        key._reference = mock.sentinel.reference
        assert key.reference() is mock.sentinel.reference

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_reference_bad_kind():
        too_long = "a" * (key_module._MAX_KEYPART_BYTES + 1)
        for kind in ("", too_long):
            key = key_module.Key(kind, "key", app="app")
            with pytest.raises(ValueError):
                key.reference()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_reference_bad_string_id():
        too_long = "a" * (key_module._MAX_KEYPART_BYTES + 1)
        for id_ in ("", too_long):
            key = key_module.Key("kind", id_, app="app")
            with pytest.raises(ValueError):
                key.reference()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_reference_bad_integer_id():
        for id_ in (-10, 0, 2**64):
            key = key_module.Key("kind", id_, app="app")
            with pytest.raises(ValueError):
                key.reference()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_serialized():
        key = key_module.Key("a", 108, app="c")
        assert key.serialized() == b"j\x01cr\x07\x0b\x12\x01a\x18l\x0c"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_urlsafe():
        key = key_module.Key("d", None, app="f")
        assert key.urlsafe() == b"agFmcgULEgFkDA"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_to_legacy_urlsafe():
        key = key_module.Key("d", 123, app="f")
        assert key.to_legacy_urlsafe(location_prefix="s~") == b"agNzfmZyBwsSAWQYeww"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_to_legacy_urlsafe_name():
        key = key_module.Key("d", "x", app="f")
        assert key.to_legacy_urlsafe(location_prefix="s~") == b"agNzfmZyCAsSAWQiAXgM"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_to_legacy_urlsafe_w_ancestor():
        """Regression test for #478.

        https://github.com/googleapis/python-ndb/issues/478
        """
        key = key_module.Key("d", 123, "e", 234, app="f")
        urlsafe = key.to_legacy_urlsafe(location_prefix="s~")
        key2 = key_module.Key(urlsafe=urlsafe)
        assert key == key2

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_to_legacy_urlsafe_named_database_unsupported():
        key = key_module.Key("d", 123, database="anydb")
        with pytest.raises(
            ValueError, match="to_legacy_urlsafe only supports the default database"
        ):
            key.to_legacy_urlsafe(location_prefix="s~")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    @mock.patch("google.cloud.ndb.model._entity_from_protobuf")
    def test_get_with_cache_miss(_entity_from_protobuf, _datastore_api):
        class Simple(model.Model):
            pass

        ds_future = tasklets.Future()
        ds_future.set_result("ds_entity")
        _datastore_api.lookup.return_value = ds_future
        _entity_from_protobuf.return_value = "the entity"

        key = key_module.Key("Simple", "b", app="c")
        assert key.get(use_cache=True) == "the entity"

        _datastore_api.lookup.assert_called_once_with(
            key._key, _options.ReadOptions(use_cache=True)
        )
        _entity_from_protobuf.assert_called_once_with("ds_entity")

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api")
    @mock.patch("google.cloud.ndb.model._entity_from_protobuf")
    def test_get_with_cache_hit(_entity_from_protobuf, _datastore_api, in_context):
        class Simple(model.Model):
            pass

        ds_future = tasklets.Future()
        ds_future.set_result("ds_entity")
        _datastore_api.lookup.return_value = ds_future
        _entity_from_protobuf.return_value = "the entity"

        key = key_module.Key("Simple", "b", app="c")
        mock_cached_entity = mock.Mock(_key=key)
        in_context.cache[key] = mock_cached_entity
        assert key.get(use_cache=True) == mock_cached_entity

        _datastore_api.lookup.assert_not_called()
        _entity_from_protobuf.assert_not_called()

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api")
    @mock.patch("google.cloud.ndb.model._entity_from_protobuf")
    def test_get_no_cache(_entity_from_protobuf, _datastore_api, in_context):
        class Simple(model.Model):
            pass

        ds_future = tasklets.Future()
        ds_future.set_result("ds_entity")
        _datastore_api.lookup.return_value = ds_future
        _entity_from_protobuf.return_value = "the entity"

        key = key_module.Key("Simple", "b", app="c")
        mock_cached_entity = mock.Mock(_key=key)
        in_context.cache[key] = mock_cached_entity
        assert key.get(use_cache=False) == "the entity"

        _datastore_api.lookup.assert_called_once_with(
            key._key, _options.ReadOptions(use_cache=False)
        )
        _entity_from_protobuf.assert_called_once_with("ds_entity")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    @mock.patch("google.cloud.ndb.model._entity_from_protobuf")
    def test_get_w_hooks(_entity_from_protobuf, _datastore_api):
        class Simple(model.Model):
            pre_get_calls = []
            post_get_calls = []

            @classmethod
            def _pre_get_hook(cls, *args, **kwargs):
                cls.pre_get_calls.append((args, kwargs))

            @classmethod
            def _post_get_hook(cls, key, future, *args, **kwargs):
                assert isinstance(future, tasklets.Future)
                cls.post_get_calls.append(((key,) + args, kwargs))

        ds_future = tasklets.Future()
        ds_future.set_result("ds_entity")
        _datastore_api.lookup.return_value = ds_future
        _entity_from_protobuf.return_value = "the entity"

        key = key_module.Key("Simple", 42)
        assert key.get() == "the entity"

        _datastore_api.lookup.assert_called_once_with(key._key, _options.ReadOptions())
        _entity_from_protobuf.assert_called_once_with("ds_entity")

        assert Simple.pre_get_calls == [((key,), {})]
        assert Simple.post_get_calls == [((key,), {})]

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    @mock.patch("google.cloud.ndb.model._entity_from_protobuf")
    def test_get_async(_entity_from_protobuf, _datastore_api):
        ds_future = tasklets.Future()
        _datastore_api.lookup.return_value = ds_future
        _entity_from_protobuf.return_value = "the entity"

        key = key_module.Key("a", "b", app="c")
        future = key.get_async()
        ds_future.set_result("ds_entity")
        assert future.result() == "the entity"

        _datastore_api.lookup.assert_called_once_with(key._key, _options.ReadOptions())
        _entity_from_protobuf.assert_called_once_with("ds_entity")

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_get_async_not_found(_datastore_api):
        ds_future = tasklets.Future()
        _datastore_api.lookup.return_value = ds_future

        key = key_module.Key("a", "b", app="c")
        future = key.get_async()
        ds_future.set_result(_datastore_api._NOT_FOUND)
        assert future.result() is None

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_delete(_datastore_api):
        class Simple(model.Model):
            pass

        future = tasklets.Future()
        _datastore_api.delete.return_value = future
        future.set_result("result")

        key = key_module.Key("Simple", "b", app="c")
        assert key.delete() == "result"
        _datastore_api.delete.assert_called_once_with(key._key, _options.Options())

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_delete_with_cache(_datastore_api, in_context):
        class Simple(model.Model):
            pass

        future = tasklets.Future()
        _datastore_api.delete.return_value = future
        future.set_result("result")

        key = key_module.Key("Simple", "b", app="c")
        mock_cached_entity = mock.Mock(_key=key)
        in_context.cache[key] = mock_cached_entity

        assert key.delete(use_cache=True) == "result"
        assert in_context.cache[key] is None
        _datastore_api.delete.assert_called_once_with(
            key._key, _options.Options(use_cache=True)
        )

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_delete_no_cache(_datastore_api, in_context):
        class Simple(model.Model):
            pass

        future = tasklets.Future()
        _datastore_api.delete.return_value = future
        future.set_result("result")

        key = key_module.Key("Simple", "b", app="c")
        mock_cached_entity = mock.Mock(_key=key)
        in_context.cache[key] = mock_cached_entity

        assert key.delete(use_cache=False) == "result"
        assert in_context.cache[key] == mock_cached_entity
        _datastore_api.delete.assert_called_once_with(
            key._key, _options.Options(use_cache=False)
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_delete_w_hooks(_datastore_api):
        class Simple(model.Model):
            pre_delete_calls = []
            post_delete_calls = []

            @classmethod
            def _pre_delete_hook(cls, *args, **kwargs):
                cls.pre_delete_calls.append((args, kwargs))

            @classmethod
            def _post_delete_hook(cls, key, future, *args, **kwargs):
                assert isinstance(future, tasklets.Future)
                cls.post_delete_calls.append(((key,) + args, kwargs))

        future = tasklets.Future()
        _datastore_api.delete.return_value = future
        future.set_result("result")

        key = key_module.Key("Simple", 42)
        assert key.delete() == "result"
        _datastore_api.delete.assert_called_once_with(key._key, _options.Options())

        assert Simple.pre_delete_calls == [((key,), {})]
        assert Simple.post_delete_calls == [((key,), {})]

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_delete_in_transaction(_datastore_api, in_context):
        future = tasklets.Future()
        _datastore_api.delete.return_value = future

        with in_context.new(transaction=b"tx123").use():
            key = key_module.Key("a", "b", app="c")
            assert key.delete() is None
            _datastore_api.delete.assert_called_once_with(key._key, _options.Options())

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_delete_async(_datastore_api):
        key = key_module.Key("a", "b", app="c")

        future = tasklets.Future()
        _datastore_api.delete.return_value = future
        future.set_result("result")

        result = key.delete_async().get_result()

        _datastore_api.delete.assert_called_once_with(key._key, _options.Options())
        assert result == "result"

    @staticmethod
    def test_from_old_key():
        with pytest.raises(NotImplementedError):
            key_module.Key.from_old_key(None)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_to_old_key():
        key = key_module.Key("a", "b")
        with pytest.raises(NotImplementedError):
            key.to_old_key()


class Test__project_from_app:
    @staticmethod
    def test_already_clean():
        app = "my-prahjekt"
        assert key_module._project_from_app(app) == app

    @staticmethod
    def test_prefixed():
        project = "my-prahjekt"
        for prefix in ("s", "e", "dev"):
            app = "{}~{}".format(prefix, project)
            assert key_module._project_from_app(app) == project

    @staticmethod
    def test_app_fallback(context):
        context.client.project = "s~jectpro"
        with context.use():
            assert key_module._project_from_app(None) == "jectpro"


class Test__from_reference:
    def test_basic(self):
        reference = make_reference()
        ds_key = key_module._from_reference(reference, None, None, None)
        assert ds_key == google.cloud.datastore.Key(
            "Parent",
            59,
            "Child",
            "Feather",
            project="sample-app",
            database="base",
            namespace="space",
        )

    def test_matching_app(self):
        reference = make_reference()
        ds_key = key_module._from_reference(reference, "s~sample-app", None, None)
        assert ds_key == google.cloud.datastore.Key(
            "Parent",
            59,
            "Child",
            "Feather",
            project="sample-app",
            database="base",
            namespace="space",
        )

    def test_differing_app(self):
        reference = make_reference()
        with pytest.raises(RuntimeError):
            key_module._from_reference(reference, "pickles", None, None)

    def test_matching_namespace(self):
        reference = make_reference()
        ds_key = key_module._from_reference(reference, None, "space", None)
        assert ds_key == google.cloud.datastore.Key(
            "Parent",
            59,
            "Child",
            "Feather",
            project="sample-app",
            database="base",
            namespace="space",
        )

    def test_differing_namespace(self):
        reference = make_reference()
        with pytest.raises(RuntimeError):
            key_module._from_reference(reference, None, "pickles", None)

    def test_matching_database(self):
        reference = make_reference()
        ds_key = key_module._from_reference(reference, None, None, "base")
        assert ds_key == google.cloud.datastore.Key(
            "Parent",
            59,
            "Child",
            "Feather",
            project="sample-app",
            database="base",
            namespace="space",
        )

    def test_differing_database(self):
        reference = make_reference()
        with pytest.raises(RuntimeError):
            key_module._from_reference(reference, None, None, "turtles")


class Test__from_serialized:
    @staticmethod
    def test_basic():
        serialized = b'j\x0cs~sample-appr\x1e\x0b\x12\x06Parent\x18;\x0c\x0b\x12\x05Child"\x07Feather\x0c\xa2\x01\x05space\xba\x01\x04base'
        ds_key, reference = key_module._from_serialized(serialized, None, None, None)
        assert ds_key == google.cloud.datastore.Key(
            "Parent",
            59,
            "Child",
            "Feather",
            project="sample-app",
            database="base",
            namespace="space",
        )
        assert reference == make_reference()

    @staticmethod
    def test_no_app_prefix():
        serialized = b"j\x18s~sample-app-no-locationr\n\x0b\x12\x04Zorp\x18X\x0c"
        ds_key, reference = key_module._from_serialized(serialized, None, None, None)
        assert ds_key == google.cloud.datastore.Key(
            "Zorp", 88, project="sample-app-no-location"
        )
        assert reference == make_reference(
            path=({"type": "Zorp", "id": 88},),
            app="s~sample-app-no-location",
            database=None,
            namespace=None,
        )


class Test__from_urlsafe:
    @staticmethod
    def test_basic():
        urlsafe = (
            "agxzfnNhbXBsZS1hcHByHgsSBlBhcmVudBg7DAsSBUNoaWxkIgdGZWF0aGVyDKIBBXNwYWNl"
        )
        urlsafe_bytes = urlsafe.encode("ascii")
        for value in (urlsafe, urlsafe_bytes):
            ds_key, reference = key_module._from_urlsafe(value, None, None, None)
            assert ds_key == google.cloud.datastore.Key(
                "Parent",
                59,
                "Child",
                "Feather",
                project="sample-app",
                database=None,
                namespace="space",
            )
            assert reference == make_reference(database=None)

    @staticmethod
    def test_needs_padding():
        urlsafe = b"agZzfmZpcmVyDwsSBEtpbmQiBVRoaW5nDA"

        ds_key, reference = key_module._from_urlsafe(urlsafe, None, None, None)
        assert ds_key == google.cloud.datastore.Key("Kind", "Thing", project="fire")
        assert reference == make_reference(
            path=({"type": "Kind", "name": "Thing"},),
            app="s~fire",
            database=None,
            namespace=None,
        )


class Test__constructor_handle_positional:
    @staticmethod
    def test_with_path():
        args = ("Kind", 1)
        kwargs = {}
        key_module._constructor_handle_positional(args, kwargs)
        assert kwargs == {"flat": args}

    @staticmethod
    def test_path_collide_flat():
        args = ("Kind", 1)
        kwargs = {"flat": ("OtherKind", "Cheese")}
        with pytest.raises(TypeError):
            key_module._constructor_handle_positional(args, kwargs)

    @staticmethod
    def test_dict_positional():
        args = ({"flat": ("OtherKind", "Cheese"), "app": "ehp"},)
        kwargs = {}
        key_module._constructor_handle_positional(args, kwargs)
        assert kwargs == args[0]

    @staticmethod
    def test_dict_positional_with_other_kwargs():
        args = ({"flat": ("OtherKind", "Cheese"), "app": "ehp"},)
        kwargs = {"namespace": "over-here", "database": "over-there"}
        with pytest.raises(TypeError):
            key_module._constructor_handle_positional(args, kwargs)


def make_reference(
    path=({"type": "Parent", "id": 59}, {"type": "Child", "name": "Feather"}),
    app="s~sample-app",
    database="base",
    namespace="space",
):
    elements = [_app_engine_key_pb2.Path.Element(**element) for element in path]
    return _app_engine_key_pb2.Reference(
        app=app,
        path=_app_engine_key_pb2.Path(element=elements),
        database_id=database,
        name_space=namespace,
    )
