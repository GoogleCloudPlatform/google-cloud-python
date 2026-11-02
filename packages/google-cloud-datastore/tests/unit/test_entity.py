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

_PROJECT = "PROJECT"
_KIND = "KIND"
_ID = 1234


def _make_entity(key=None, exclude_from_indexes=()):
    from google.cloud.datastore.entity import Entity

    return Entity(key=key, exclude_from_indexes=exclude_from_indexes)


def test_entity_ctor_defaults():
    from google.cloud.datastore.entity import Entity

    entity = Entity()
    assert entity.key is None
    assert entity.kind is None
    assert sorted(entity.exclude_from_indexes) == []


def test_entity_ctor_explicit():
    _EXCLUDE_FROM_INDEXES = ["foo", "bar"]
    key = _Key()
    entity = _make_entity(key=key, exclude_from_indexes=_EXCLUDE_FROM_INDEXES)
    assert sorted(entity.exclude_from_indexes) == sorted(_EXCLUDE_FROM_INDEXES)


def test_entity_ctor_bad_exclude_from_indexes():
    BAD_EXCLUDE_FROM_INDEXES = object()
    key = _Key()
    with pytest.raises(TypeError):
        _make_entity(key=key, exclude_from_indexes=BAD_EXCLUDE_FROM_INDEXES)


def test_entity___eq_____ne___w_non_entity():
    from google.cloud.datastore.key import Key

    key = Key(_KIND, _ID, project=_PROJECT)
    entity = _make_entity(key=key)
    assert not entity == object()
    assert entity != object()


def test_entity___eq_____ne___w_different_keys():
    from google.cloud.datastore.key import Key

    _ID1 = 1234
    _ID2 = 2345
    key1 = Key(_KIND, _ID1, project=_PROJECT)
    entity1 = _make_entity(key=key1)
    key2 = Key(_KIND, _ID2, project=_PROJECT)
    entity2 = _make_entity(key=key2)
    assert not entity1 == entity2
    assert entity1 != entity2


def test_entity___eq_____ne___w_same_keys():
    from google.cloud.datastore.key import Key

    name = "foo"
    value = 42
    meaning = 9

    key1 = Key(_KIND, _ID, project=_PROJECT)
    entity1 = _make_entity(key=key1, exclude_from_indexes=(name,))
    entity1[name] = value
    entity1._meanings[name] = (meaning, value)

    key2 = Key(_KIND, _ID, project=_PROJECT)
    entity2 = _make_entity(key=key2, exclude_from_indexes=(name,))
    entity2[name] = value
    entity2._meanings[name] = (meaning, value)

    assert entity1 == entity2
    assert not entity1 != entity2


def test_entity___eq_____ne___w_same_keys_different_props():
    from google.cloud.datastore.key import Key

    key1 = Key(_KIND, _ID, project=_PROJECT)
    entity1 = _make_entity(key=key1)
    entity1["foo"] = "Foo"
    key2 = Key(_KIND, _ID, project=_PROJECT)
    entity2 = _make_entity(key=key2)
    entity1["bar"] = "Bar"
    assert not entity1 == entity2
    assert entity1 != entity2


def test_entity___eq_____ne___w_same_keys_props_w_equiv_keys_as_value():
    from google.cloud.datastore.key import Key

    key1 = Key(_KIND, _ID, project=_PROJECT)
    key2 = Key(_KIND, _ID, project=_PROJECT)
    entity1 = _make_entity(key=key1)
    entity1["some_key"] = key1
    entity2 = _make_entity(key=key1)
    entity2["some_key"] = key2
    assert entity1 == entity2
    assert not entity1 != entity2


def test_entity___eq_____ne___w_same_keys_props_w_diff_keys_as_value():
    from google.cloud.datastore.key import Key

    _ID1 = 1234
    _ID2 = 2345
    key1 = Key(_KIND, _ID1, project=_PROJECT)
    key2 = Key(_KIND, _ID2, project=_PROJECT)
    entity1 = _make_entity(key=key1)
    entity1["some_key"] = key1
    entity2 = _make_entity(key=key1)
    entity2["some_key"] = key2
    assert not entity1 == entity2
    assert entity1 != entity2


def test_entity___eq_____ne___w_same_keys_props_w_equiv_entities_as_value():
    from google.cloud.datastore.key import Key

    key = Key(_KIND, _ID, project=_PROJECT)
    entity1 = _make_entity(key=key)
    sub1 = _make_entity()
    sub1.update({"foo": "Foo"})
    entity1["some_entity"] = sub1
    entity2 = _make_entity(key=key)
    sub2 = _make_entity()
    sub2.update({"foo": "Foo"})
    entity2["some_entity"] = sub2
    assert entity1 == entity2
    assert not entity1 != entity2


def test_entity___eq_____ne___w_same_keys_props_w_diff_entities_as_value():
    from google.cloud.datastore.key import Key

    key = Key(_KIND, _ID, project=_PROJECT)
    entity1 = _make_entity(key=key)
    sub1 = _make_entity()
    sub1.update({"foo": "Foo"})
    entity1["some_entity"] = sub1
    entity2 = _make_entity(key=key)
    sub2 = _make_entity()
    sub2.update({"foo": "Bar"})
    entity2["some_entity"] = sub2
    assert not entity1 == entity2
    assert entity1 != entity2


def test__eq__same_value_different_exclude():
    from google.cloud.datastore.key import Key

    name = "foo"
    value = 42
    key = Key(_KIND, _ID, project=_PROJECT)

    entity1 = _make_entity(key=key, exclude_from_indexes=(name,))
    entity1[name] = value

    entity2 = _make_entity(key=key, exclude_from_indexes=())
    entity2[name] = value

    assert not entity1 == entity2
    assert entity1 != entity2


def test_entity___eq__same_value_different_meanings():
    from google.cloud.datastore.key import Key

    name = "foo"
    value = 42
    meaning = 9
    key = Key(_KIND, _ID, project=_PROJECT)

    entity1 = _make_entity(key=key, exclude_from_indexes=(name,))
    entity1[name] = value

    entity2 = _make_entity(key=key, exclude_from_indexes=(name,))
    entity2[name] = value
    entity2._meanings[name] = (meaning, value)

    assert not entity1 == entity2
    assert entity1 != entity2


def test_id():
    from google.cloud.datastore.key import Key

    key = Key(_KIND, _ID, project=_PROJECT)
    entity = _make_entity(key=key)
    assert entity.id == _ID


def test_id_none():
    entity = _make_entity(key=None)
    assert entity.id is None


def test___repr___no_key_empty():
    entity = _make_entity()
    assert repr(entity) == "<Entity {}>"


def test___repr___w_key_non_empty():
    key = _Key()
    flat_path = ("bar", 12, "baz", "himom")
    key._flat_path = flat_path
    entity = _make_entity(key=key)
    entity_vals = {"foo": "Foo"}
    entity.update(entity_vals)
    expected = "<Entity%s %s>" % (flat_path, entity_vals)
    assert repr(entity) == expected


class _Key(object):
    _MARKER = object()
    _key = "KEY"
    _partial = False
    _path = None
    _id = None
    _stored = None

    def __init__(self, project=_PROJECT):
        self.project = project
