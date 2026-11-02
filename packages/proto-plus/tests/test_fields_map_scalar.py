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

import proto


def test_basic_map():
    class Foo(proto.Message):
        tags = proto.MapField(proto.STRING, proto.STRING, number=1)

    foo = Foo(tags={"a": "foo", "b": "bar"})
    assert foo.tags["a"] == "foo"
    assert foo.tags["b"] == "bar"
    assert "c" not in foo.tags


def test_basic_map_with_underscore_field_name():
    class Foo(proto.Message):
        tag_labels = proto.MapField(proto.STRING, proto.STRING, number=1)

    foo = Foo(tag_labels={"a": "foo", "b": "bar"})
    assert foo.tag_labels["a"] == "foo"
    assert foo.tag_labels["b"] == "bar"
    assert "c" not in foo.tag_labels


def test_basic_map_assignment():
    class Foo(proto.Message):
        tags = proto.MapField(proto.STRING, proto.STRING, number=1)

    foo = Foo(tags={"a": "foo"})
    foo.tags["b"] = "bar"
    assert len(foo.tags) == 2
    assert foo.tags["a"] == "foo"
    assert foo.tags["b"] == "bar"
    assert "c" not in foo.tags


def test_basic_map_deletion():
    class Foo(proto.Message):
        tags = proto.MapField(proto.STRING, proto.STRING, number=1)

    foo = Foo(tags={"a": "foo", "b": "bar"})
    del foo.tags["b"]
    assert len(foo.tags) == 1
    assert foo.tags["a"] == "foo"
    assert "b" not in foo.tags
