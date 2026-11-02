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

_DEFAULT_PROJECT = "PROJECT"
_DEFAULT_DATABASE = ""
PROJECT = "my-prahjekt"
DATABASE = "my-database"
# NOTE: This comes directly from a running (in the dev appserver)
#       App Engine app. Created via:
#
#           from google.appengine.ext import ndb
#           key = ndb.Key(
#               'Parent', 59, 'Child', 'Feather',
#               namespace='space', app='s~sample-app')
#           urlsafe = key.urlsafe()
_URLSAFE_EXAMPLE1 = (
    b"agxzfnNhbXBsZS1hcHByHgsSBlBhcmVudBg7DAsSBUNoaWxkIgdGZWF0aGVyDKIBBXNwYWNl"
)
_URLSAFE_APP1 = "s~sample-app"
_URLSAFE_NAMESPACE1 = "space"
_URLSAFE_FLAT_PATH1 = ("Parent", 59, "Child", "Feather")
_URLSAFE_EXAMPLE2 = b"agZzfmZpcmVyDwsSBEtpbmQiBVRoaW5nDA"
_URLSAFE_APP2 = "s~fire"
_URLSAFE_FLAT_PATH2 = ("Kind", "Thing")
_URLSAFE_EXAMPLE3 = b"ahhzfnNhbXBsZS1hcHAtbm8tbG9jYXRpb25yCgsSBFpvcnAYWAw"
_URLSAFE_APP3 = "sample-app-no-location"
_URLSAFE_FLAT_PATH3 = ("Zorp", 88)


def _make_key(*args, **kwargs):
    from google.cloud.datastore.key import Key

    return Key(*args, **kwargs)


def test_key_ctor_empty():
    with pytest.raises(ValueError):
        _make_key()


def test_key_ctor_no_project():
    with pytest.raises(ValueError):
        _make_key("KIND")


def test_key_ctor_w_explicit_project_empty_path():
    with pytest.raises(ValueError):
        _make_key(project=PROJECT)


def test_key_ctor_parent():
    _PARENT_KIND = "KIND1"
    _PARENT_ID = 1234
    _PARENT_PROJECT = "PROJECT-ALT"
    _PARENT_DATABASE = "DATABASE-ALT"
    _PARENT_NAMESPACE = "NAMESPACE"
    _CHILD_KIND = "KIND2"
    _CHILD_ID = 2345
    _PATH = [
        {"kind": _PARENT_KIND, "id": _PARENT_ID},
        {"kind": _CHILD_KIND, "id": _CHILD_ID},
    ]
    parent_key = _make_key(
        _PARENT_KIND,
        _PARENT_ID,
        project=_PARENT_PROJECT,
        database=_PARENT_DATABASE,
        namespace=_PARENT_NAMESPACE,
    )
    key = _make_key(_CHILD_KIND, _CHILD_ID, parent=parent_key)
    assert key.project == parent_key.project
    assert key.database == parent_key.database
    assert key.namespace == parent_key.namespace
    assert key.kind == _CHILD_KIND
    assert key.path == _PATH
    assert key.parent is parent_key


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_ctor_partial_parent(database_id):
    parent_key = _make_key("KIND", project=_DEFAULT_PROJECT, database=database_id)
    with pytest.raises(ValueError):
        _make_key("KIND2", 1234, parent=parent_key, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_ctor_parent_bad_type(database_id):
    with pytest.raises(AttributeError):
        _make_key(
            "KIND2",
            1234,
            parent=("KIND1", 1234),
            project=_DEFAULT_PROJECT,
            database=database_id,
        )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_ctor_parent_bad_namespace(database_id):
    parent_key = _make_key(
        "KIND", 1234, namespace="FOO", project=_DEFAULT_PROJECT, database=database_id
    )
    with pytest.raises(ValueError) as exc:
        _make_key(
            "KIND2",
            1234,
            namespace="BAR",
            parent=parent_key,
            PROJECT=_DEFAULT_PROJECT,
            database=database_id,
        )
    assert "Child namespace must agree with parent's." in str(exc.value)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_ctor_parent_bad_project(database_id):
    parent_key = _make_key("KIND", 1234, project="FOO", database=database_id)
    with pytest.raises(ValueError) as exc:
        _make_key("KIND2", 1234, parent=parent_key, project="BAR", database=database_id)
    assert "Child project must agree with parent's." in str(exc.value)


def test_key_ctor_parent_bad_database():
    parent_key = _make_key("KIND", 1234, project=_DEFAULT_PROJECT, database="db1")
    with pytest.raises(ValueError) as exc:
        _make_key(
            "KIND2",
            1234,
            parent=parent_key,
            PROJECT=_DEFAULT_PROJECT,
            database="db2",
        )
    assert "Child database must agree with parent's" in str(exc.value)


def test_key_ctor_parent_empty_path():
    parent_key = _make_key("KIND", 1234, project=_DEFAULT_PROJECT)
    with pytest.raises(ValueError):
        _make_key(parent=parent_key)


def test_key_ctor_explicit():
    _PROJECT = "PROJECT-ALT"
    _DATABASE = "DATABASE-ALT"
    _NAMESPACE = "NAMESPACE"
    _KIND = "KIND"
    _ID = 1234
    _PATH = [{"kind": _KIND, "id": _ID}]
    key = _make_key(
        _KIND, _ID, namespace=_NAMESPACE, database=_DATABASE, project=_PROJECT
    )
    assert key.project == _PROJECT
    assert key.database == _DATABASE
    assert key.namespace == _NAMESPACE
    assert key.kind == _KIND
    assert key.path == _PATH


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_ctor_explicit_w_unspecified_database(database_id):
    _PROJECT = "PROJECT-ALT"
    _NAMESPACE = "NAMESPACE"
    _KIND = "KIND"
    _ID = 1234
    _PATH = [{"kind": _KIND, "id": _ID}]
    key = _make_key(
        _KIND, _ID, namespace=_NAMESPACE, project=_PROJECT, database=database_id
    )
    assert key.project == _PROJECT
    assert key.database == database_id
    assert key.namespace == _NAMESPACE
    assert key.kind == _KIND
    assert key.path == _PATH


def test_key_ctor_bad_kind():
    with pytest.raises(ValueError):
        _make_key(object(), project=_DEFAULT_PROJECT)


def test_key_ctor_bad_id_or_name():
    with pytest.raises(ValueError):
        _make_key("KIND", object(), project=_DEFAULT_PROJECT)

    with pytest.raises(ValueError):
        _make_key("KIND", None, project=_DEFAULT_PROJECT)

    with pytest.raises(ValueError):
        _make_key("KIND", 10, "KIND2", None, project=_DEFAULT_PROJECT)


def test_key__clone():
    _PROJECT = "PROJECT-ALT"
    _DATABASE = "DATABASE-ALT"
    _NAMESPACE = "NAMESPACE"
    _KIND = "KIND"
    _ID = 1234
    _PATH = [{"kind": _KIND, "id": _ID}]
    key = _make_key(
        _KIND, _ID, namespace=_NAMESPACE, database=_DATABASE, project=_PROJECT
    )

    clone = key._clone()

    assert clone.project == _PROJECT
    assert clone.database == _DATABASE
    assert clone.namespace == _NAMESPACE
    assert clone.kind == _KIND
    assert clone.path == _PATH


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key__clone_with_parent(database_id):
    _PROJECT = "PROJECT-ALT"
    _NAMESPACE = "NAMESPACE"
    _KIND1 = "PARENT"
    _KIND2 = "KIND"
    _ID1 = 1234
    _ID2 = 2345
    _PATH = [{"kind": _KIND1, "id": _ID1}, {"kind": _KIND2, "id": _ID2}]

    parent = _make_key(
        _KIND1, _ID1, namespace=_NAMESPACE, database=database_id, project=_PROJECT
    )
    key = _make_key(_KIND2, _ID2, parent=parent, database=database_id)
    assert key.parent is parent

    clone = key._clone()

    assert clone.parent is key.parent
    assert clone.project == _PROJECT
    assert clone.database == database_id
    assert clone.namespace == _NAMESPACE
    assert clone.path == _PATH


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___w_non_key(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _NAME = "one"
    key = _make_key(_KIND, _NAME, project=_PROJECT, database=database_id)
    assert not key == object()
    assert key != object()


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___two_incomplete_keys_same_kind(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    key1 = _make_key(_KIND, project=_PROJECT, database=database_id)
    key2 = _make_key(_KIND, project=_PROJECT, database=database_id)
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___incomplete_key_w_complete_key_same_kind(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID = 1234
    key1 = _make_key(_KIND, project=_PROJECT, database=database_id)
    key2 = _make_key(_KIND, _ID, project=_PROJECT, database=database_id)
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___complete_key_w_incomplete_key_same_kind(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID = 1234
    key1 = _make_key(_KIND, _ID, project=_PROJECT, database=database_id)
    key2 = _make_key(_KIND, project=_PROJECT, database=database_id)
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_different_ids(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID1 = 1234
    _ID2 = 2345
    key1 = _make_key(_KIND, _ID1, project=_PROJECT, database=database_id)
    key2 = _make_key(_KIND, _ID2, project=_PROJECT, database=database_id)
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_and_id(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID = 1234
    key1 = _make_key(_KIND, _ID, project=_PROJECT, database=database_id)
    key2 = _make_key(_KIND, _ID, project=_PROJECT, database=database_id)
    assert key1 == key2
    assert not key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_and_id_different_project(database_id):
    _PROJECT1 = "PROJECT1"
    _PROJECT2 = "PROJECT2"
    _KIND = "KIND"
    _ID = 1234
    key1 = _make_key(_KIND, _ID, project=_PROJECT1, database=database_id)
    key2 = _make_key(_KIND, _ID, project=_PROJECT2, database=database_id)
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_and_id_different_database(database_id):
    _PROJECT = "PROJECT"
    _DATABASE1 = "DATABASE1"
    _DATABASE2 = "DATABASE2"
    _KIND = "KIND"
    _ID = 1234
    key1 = _make_key(_KIND, _ID, project=_PROJECT, database=_DATABASE1)
    key2 = _make_key(_KIND, _ID, project=_PROJECT, database=_DATABASE2)
    key_with_explicit_default = _make_key(
        _KIND, _ID, project=_PROJECT, database=database_id
    )
    key_with_implicit_default = _make_key(
        _KIND, _ID, project=_PROJECT, database=database_id
    )
    assert not key1 == key2
    assert key1 != key2
    assert not key1 == key_with_explicit_default
    assert key1 != key_with_explicit_default
    assert not key1 == key_with_implicit_default
    assert key1 != key_with_implicit_default
    assert key_with_explicit_default == key_with_implicit_default


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_and_id_different_namespace(database_id):
    _PROJECT = "PROJECT"
    _NAMESPACE1 = "NAMESPACE1"
    _NAMESPACE2 = "NAMESPACE2"
    _KIND = "KIND"
    _ID = 1234
    key1 = _make_key(
        _KIND, _ID, project=_PROJECT, namespace=_NAMESPACE1, database=database_id
    )
    key2 = _make_key(
        _KIND, _ID, project=_PROJECT, namespace=_NAMESPACE2, database=database_id
    )
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_different_names(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _NAME1 = "one"
    _NAME2 = "two"
    key1 = _make_key(_KIND, _NAME1, project=_PROJECT, database=database_id)
    key2 = _make_key(_KIND, _NAME2, project=_PROJECT, database=database_id)
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_and_name(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _NAME = "one"
    key1 = _make_key(_KIND, _NAME, project=_PROJECT, database=database_id)
    key2 = _make_key(_KIND, _NAME, project=_PROJECT, database=database_id)
    assert key1 == key2
    assert not key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_and_name_different_project(database_id):
    _PROJECT1 = "PROJECT1"
    _PROJECT2 = "PROJECT2"
    _KIND = "KIND"
    _NAME = "one"
    key1 = _make_key(_KIND, _NAME, project=_PROJECT1, database=database_id)
    key2 = _make_key(_KIND, _NAME, project=_PROJECT2, database=database_id)
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___eq_____ne___same_kind_and_name_different_namespace(database_id):
    _PROJECT = "PROJECT"
    _NAMESPACE1 = "NAMESPACE1"
    _NAMESPACE2 = "NAMESPACE2"
    _KIND = "KIND"
    _NAME = "one"
    key1 = _make_key(
        _KIND, _NAME, project=_PROJECT, namespace=_NAMESPACE1, database=database_id
    )
    key2 = _make_key(
        _KIND, _NAME, project=_PROJECT, namespace=_NAMESPACE2, database=database_id
    )
    assert not key1 == key2
    assert key1 != key2


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___hash___incomplete(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    key = _make_key(_KIND, project=_PROJECT, database_id=database_id)
    assert hash(key) != hash(_KIND) + hash(_PROJECT) + hash(None) + hash(None) + hash(
        database_id
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___hash___completed_w_id(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _ID = 1234
    key = _make_key(_KIND, _ID, project=_PROJECT, database=database_id)
    assert hash(key) != hash(_KIND) + hash(_ID) + hash(_PROJECT) + hash(None) + hash(
        None
    ) + hash(database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key___hash___completed_w_name(database_id):
    _PROJECT = "PROJECT"
    _KIND = "KIND"
    _NAME = "NAME"
    key = _make_key(_KIND, _NAME, project=_PROJECT, database=database_id)
    assert hash(key) != hash(_KIND) + hash(_NAME) + hash(_PROJECT) + hash(None) + hash(
        None
    ) + hash(database_id)


def test_key___hash___completed_w_database_and_namespace():
    _PROJECT = "PROJECT"
    _DATABASE = "DATABASE"
    _NAMESPACE = "NAMESPACE"
    _KIND = "KIND"
    _NAME = "NAME"
    key = _make_key(
        _KIND, _NAME, project=_PROJECT, database=_DATABASE, namespace=_NAMESPACE
    )
    assert hash(key) != hash(_KIND) + hash(_NAME) + hash(_PROJECT) + hash(None) + hash(
        None
    ) + hash(None)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_key_completed_key_on_partial_w_id(database_id):
    key = _make_key("KIND", project=_DEFAULT_PROJECT, database=database_id)
    _ID = 1234
    new_key = key.completed_key(_ID)
    assert key is not new_key
    assert new_key.id == _ID
    assert new_key.name is None
    assert new_key.database == database_id


def test_key_completed_key_on_partial_w_name():
    key = _make_key("KIND", project=_DEFAULT_PROJECT)
    _NAME = "NAME"
    new_key = key.completed_key(_NAME)
    assert key is not new_key
    assert new_key.id is None
    assert new_key.name == _NAME


def test_key_completed_key_on_partial_w_invalid():
    key = _make_key("KIND", project=_DEFAULT_PROJECT)
    with pytest.raises(ValueError):
        key.completed_key(object())


def test_key_completed_key_on_complete():
    key = _make_key("KIND", 1234, project=_DEFAULT_PROJECT)
    with pytest.raises(ValueError):
        key.completed_key(5678)


def test_key_to_protobuf_defaults():
    from google.cloud.datastore_v1.types import entity as entity_pb2

    _KIND = "KIND"
    key = _make_key(_KIND, project=_DEFAULT_PROJECT)
    pb = key.to_protobuf()
    assert isinstance(pb, entity_pb2.Key)

    # Check partition ID.
    assert pb.partition_id.project_id == _DEFAULT_PROJECT
    # Unset values are False-y.
    assert pb.partition_id.database_id == _DEFAULT_DATABASE
    assert pb.partition_id.namespace_id == ""

    # Check the element PB matches the partial key and kind.
    (elem,) = list(pb.path)
    assert elem.kind == _KIND
    # Unset values are False-y.
    assert elem.name == ""
    # Unset values are False-y.
    assert elem.id == 0


def test_key_to_protobuf_w_explicit_project():
    _PROJECT = "PROJECT-ALT"
    key = _make_key("KIND", project=_PROJECT)
    pb = key.to_protobuf()
    assert pb.partition_id.project_id == _PROJECT


def test_key_to_protobuf_w_explicit_database():
    _DATABASE = "DATABASE-ALT"
    key = _make_key("KIND", project=_DEFAULT_PROJECT, database=_DATABASE)
    pb = key.to_protobuf()
    assert pb.partition_id.database_id == _DATABASE


def test_key_to_protobuf_w_explicit_namespace():
    _NAMESPACE = "NAMESPACE"
    key = _make_key("KIND", namespace=_NAMESPACE, project=_DEFAULT_PROJECT)
    pb = key.to_protobuf()
    assert pb.partition_id.namespace_id == _NAMESPACE


def test_key_to_protobuf_w_explicit_path():
    _PARENT = "PARENT"
    _CHILD = "CHILD"
    _ID = 1234
    _NAME = "NAME"
    key = _make_key(_PARENT, _NAME, _CHILD, _ID, project=_DEFAULT_PROJECT)
    pb = key.to_protobuf()
    elems = list(pb.path)
    assert len(elems) == 2
    assert elems[0].kind == _PARENT
    assert elems[0].name == _NAME
    assert elems[1].kind == _CHILD
    assert elems[1].id == _ID


def test_key_to_protobuf_w_no_kind():
    key = _make_key("KIND", project=_DEFAULT_PROJECT)
    # Force the 'kind' to be unset. Maybe `to_protobuf` should fail
    # on this? The backend certainly will.
    key._path[-1].pop("kind")
    pb = key.to_protobuf()
    # Unset values are False-y.
    assert pb.path[0].kind == ""


def test_key_to_legacy_urlsafe():
    key = _make_key(
        *_URLSAFE_FLAT_PATH1, project=_URLSAFE_APP1, namespace=_URLSAFE_NAMESPACE1
    )
    # NOTE: ``key.project`` is somewhat "invalid" but that is OK.
    urlsafe = key.to_legacy_urlsafe()
    assert urlsafe == _URLSAFE_EXAMPLE1


def test_key_to_legacy_urlsafe_strip_padding():
    key = _make_key(*_URLSAFE_FLAT_PATH2, project=_URLSAFE_APP2)
    # NOTE: ``key.project`` is somewhat "invalid" but that is OK.
    urlsafe = key.to_legacy_urlsafe()
    assert urlsafe == _URLSAFE_EXAMPLE2
    # Make sure it started with base64 padding.
    assert len(_URLSAFE_EXAMPLE2) % 4 != 0


def test_key_to_legacy_urlsafe_with_location_prefix():
    key = _make_key(*_URLSAFE_FLAT_PATH3, project=_URLSAFE_APP3)
    urlsafe = key.to_legacy_urlsafe(location_prefix="s~")
    assert urlsafe == _URLSAFE_EXAMPLE3


def test_key_to_legacy_urlsafe_w_nondefault_database():
    _KIND = "KIND"
    _ID = 1234
    _PROJECT = "PROJECT-ALT"
    _DATABASE = "DATABASE-ALT"
    key = _make_key(_KIND, _ID, project=_PROJECT, database=_DATABASE)

    with pytest.raises(
        ValueError, match="to_legacy_urlsafe only supports the default database"
    ):
        key.to_legacy_urlsafe()


def test_key_from_legacy_urlsafe():
    from google.cloud.datastore.key import Key

    key = Key.from_legacy_urlsafe(_URLSAFE_EXAMPLE1)

    assert "s~" + key.project == _URLSAFE_APP1
    assert key.database is None
    assert key.namespace == _URLSAFE_NAMESPACE1
    assert key.flat_path == _URLSAFE_FLAT_PATH1
    # Also make sure we didn't accidentally set the parent.
    assert key._parent is None
    assert key.parent is not None
    assert key._parent is key.parent


def test_key_from_legacy_urlsafe_needs_padding():
    from google.cloud.datastore.key import Key

    # Make sure it will have base64 padding added.
    len(_URLSAFE_EXAMPLE2) % 4 != 0
    key = Key.from_legacy_urlsafe(_URLSAFE_EXAMPLE2)

    assert "s~" + key.project == _URLSAFE_APP2
    assert key.namespace is None
    assert key.flat_path == _URLSAFE_FLAT_PATH2


def test_key_from_legacy_urlsafe_with_location_prefix():
    from google.cloud.datastore.key import Key

    # Make sure it will have base64 padding added.
    key = Key.from_legacy_urlsafe(_URLSAFE_EXAMPLE3)

    assert key.project == _URLSAFE_APP3
    assert key.namespace is None
    assert key.flat_path == _URLSAFE_FLAT_PATH3


def test_key_is_partial_no_name_or_id():
    key = _make_key("KIND", project=_DEFAULT_PROJECT)
    assert key.is_partial


def test_key_is_partial_w_id():
    _ID = 1234
    key = _make_key("KIND", _ID, project=_DEFAULT_PROJECT)
    assert not key.is_partial


def test_key_is_partial_w_name():
    _NAME = "NAME"
    key = _make_key("KIND", _NAME, project=_DEFAULT_PROJECT)
    assert not key.is_partial


def test_key_id_or_name_no_name_or_id():
    key = _make_key("KIND", project=_DEFAULT_PROJECT)
    assert key.id_or_name is None


def test_key_id_or_name_no_name_or_id_child():
    key = _make_key("KIND1", 1234, "KIND2", project=_DEFAULT_PROJECT)
    assert key.id_or_name is None


def test_key_id_or_name_w_id_only():
    _ID = 1234
    key = _make_key("KIND", _ID, project=_DEFAULT_PROJECT)
    assert key.id_or_name == _ID


def test_key_id_or_name_w_name_only():
    _NAME = "NAME"
    key = _make_key("KIND", _NAME, project=_DEFAULT_PROJECT)
    assert key.id_or_name == _NAME


def test_key_id_or_name_w_id_zero():
    _ID = 0
    key = _make_key("KIND", _ID, project=_DEFAULT_PROJECT)
    assert key.id_or_name == _ID


def test_key_parent_default():
    key = _make_key("KIND", project=_DEFAULT_PROJECT)
    assert key.parent is None


def test_key_parent_explicit_top_level():
    key = _make_key("KIND", 1234, project=_DEFAULT_PROJECT)
    assert key.parent is None


def test_key_parent_explicit_nested():
    _PARENT_KIND = "KIND1"
    _PARENT_ID = 1234
    _PARENT_PATH = [{"kind": _PARENT_KIND, "id": _PARENT_ID}]
    key = _make_key(_PARENT_KIND, _PARENT_ID, "KIND2", project=_DEFAULT_PROJECT)
    assert key.parent.path == _PARENT_PATH


def test_key_parent_multiple_calls():
    _PARENT_KIND = "KIND1"
    _PARENT_ID = 1234
    _PARENT_PATH = [{"kind": _PARENT_KIND, "id": _PARENT_ID}]
    key = _make_key(_PARENT_KIND, _PARENT_ID, "KIND2", project=_DEFAULT_PROJECT)
    parent = key.parent
    assert parent.path == _PARENT_PATH
    new_parent = key.parent
    assert parent is new_parent


def test__cliean_app_w_already_clean():
    from google.cloud.datastore.key import _clean_app

    app_str = PROJECT
    assert _clean_app(app_str) == PROJECT


def test__cliean_app_w_standard():
    from google.cloud.datastore.key import _clean_app

    app_str = "s~" + PROJECT
    assert _clean_app(app_str) == PROJECT


def test__cliean_app_w_european():
    from google.cloud.datastore.key import _clean_app

    app_str = "e~" + PROJECT
    assert _clean_app(app_str) == PROJECT


def test__cliean_app_w_dev_server():
    from google.cloud.datastore.key import _clean_app

    app_str = "dev~" + PROJECT
    assert _clean_app(app_str) == PROJECT


def test__get_empty_w_unset():
    from google.cloud.datastore.key import _get_empty

    for empty_value in ("", 0, 0.0, []):
        ret_val = _get_empty(empty_value, empty_value)
        assert ret_val is None


def test__get_empty_w_actually_set():
    from google.cloud.datastore.key import _get_empty

    value_pairs = (("hello", ""), (10, 0), (3.14, 0.0), (["stuff", "here"], []))
    for value, empty_value in value_pairs:
        ret_val = _get_empty(value, empty_value)
        assert ret_val is value


def test__check_database_id_w_empty_value():
    from google.cloud.datastore.key import _check_database_id

    ret_val = _check_database_id("")
    # Really we are just happy there was no exception.
    assert ret_val is None


def test__check_database_id_w_failure():
    from google.cloud.datastore.key import _check_database_id

    with pytest.raises(ValueError):
        _check_database_id("some-database-id")


def test__add_id_or_name_add_id():
    from google.cloud.datastore.key import _add_id_or_name

    flat_path = []
    id_ = 123
    element_pb = _make_element_pb(id=id_)

    ret_val = _add_id_or_name(flat_path, element_pb, False)
    assert ret_val is None
    assert flat_path == [id_]
    ret_val = _add_id_or_name(flat_path, element_pb, True)
    assert ret_val is None
    assert flat_path == [id_, id_]


def test__add_id_or_name_add_name():
    from google.cloud.datastore.key import _add_id_or_name

    flat_path = []
    name = "moon-shadow"
    element_pb = _make_element_pb(name=name)

    ret_val = _add_id_or_name(flat_path, element_pb, False)
    assert ret_val is None
    assert flat_path == [name]
    ret_val = _add_id_or_name(flat_path, element_pb, True)
    assert ret_val is None
    assert flat_path == [name, name]


def test__add_id_or_name_both_present():
    from google.cloud.datastore.key import _add_id_or_name

    element_pb = _make_element_pb(id=17, name="seventeen")
    flat_path = []
    with pytest.raises(ValueError):
        _add_id_or_name(flat_path, element_pb, False)
    with pytest.raises(ValueError):
        _add_id_or_name(flat_path, element_pb, True)

    assert flat_path == []


def test__add_id_or_name_both_empty_failure():
    from google.cloud.datastore.key import _add_id_or_name

    element_pb = _make_element_pb()
    flat_path = []
    with pytest.raises(ValueError):
        _add_id_or_name(flat_path, element_pb, False)

    assert flat_path == []


def test__add_id_or_name_both_empty_allowed():
    from google.cloud.datastore.key import _add_id_or_name

    element_pb = _make_element_pb()
    flat_path = []
    ret_val = _add_id_or_name(flat_path, element_pb, True)
    assert ret_val is None
    assert flat_path == []


def test__get_flat_path_one_pair():
    from google.cloud.datastore.key import _get_flat_path

    kind = "Widget"
    name = "Scooter"
    element_pb = _make_element_pb(type=kind, name=name)
    path_pb = _make_path_pb(element_pb)
    flat_path = _get_flat_path(path_pb)
    assert flat_path == (kind, name)


def test__get_flat_path_two_pairs():
    from google.cloud.datastore.key import _get_flat_path

    kind1 = "parent"
    id1 = 59
    element_pb1 = _make_element_pb(type=kind1, id=id1)

    kind2 = "child"
    name2 = "naem"
    element_pb2 = _make_element_pb(type=kind2, name=name2)

    path_pb = _make_path_pb(element_pb1, element_pb2)
    flat_path = _get_flat_path(path_pb)
    assert flat_path == (kind1, id1, kind2, name2)


def test__get_flat_path_partial_key():
    from google.cloud.datastore.key import _get_flat_path

    kind1 = "grandparent"
    name1 = "cats"
    element_pb1 = _make_element_pb(type=kind1, name=name1)

    kind2 = "parent"
    id2 = 1337
    element_pb2 = _make_element_pb(type=kind2, id=id2)

    kind3 = "child"
    element_pb3 = _make_element_pb(type=kind3)

    path_pb = _make_path_pb(element_pb1, element_pb2, element_pb3)
    flat_path = _get_flat_path(path_pb)
    assert flat_path == (kind1, name1, kind2, id2, kind3)


def test__to_legacy_path_w_one_pair():
    from google.cloud.datastore.key import _to_legacy_path

    kind = "Widget"
    name = "Scooter"
    dict_path = [{"kind": kind, "name": name}]
    path_pb = _to_legacy_path(dict_path)

    element_pb = _make_element_pb(type=kind, name=name)
    expected_pb = _make_path_pb(element_pb)
    assert path_pb == expected_pb


def test__to_legacy_path_w_two_pairs():
    from google.cloud.datastore.key import _to_legacy_path

    kind1 = "parent"
    id1 = 59

    kind2 = "child"
    name2 = "naem"

    dict_path = [{"kind": kind1, "id": id1}, {"kind": kind2, "name": name2}]
    path_pb = _to_legacy_path(dict_path)

    element_pb1 = _make_element_pb(type=kind1, id=id1)
    element_pb2 = _make_element_pb(type=kind2, name=name2)
    expected_pb = _make_path_pb(element_pb1, element_pb2)
    assert path_pb == expected_pb


def test__to_legacy_path_w_partial_key():
    from google.cloud.datastore.key import _to_legacy_path

    kind1 = "grandparent"
    name1 = "cats"

    kind2 = "parent"
    id2 = 1337

    kind3 = "child"

    dict_path = [
        {"kind": kind1, "name": name1},
        {"kind": kind2, "id": id2},
        {"kind": kind3},
    ]
    path_pb = _to_legacy_path(dict_path)

    element_pb1 = _make_element_pb(type=kind1, name=name1)
    element_pb2 = _make_element_pb(type=kind2, id=id2)
    element_pb3 = _make_element_pb(type=kind3)
    expected_pb = _make_path_pb(element_pb1, element_pb2, element_pb3)
    assert path_pb == expected_pb


def _make_element_pb(**kwargs):
    from google.cloud.datastore import _app_engine_key_pb2

    return _app_engine_key_pb2.Path.Element(**kwargs)


def _make_path_pb(*element_pbs):
    from google.cloud.datastore import _app_engine_key_pb2

    return _app_engine_key_pb2.Path(element=element_pbs)
