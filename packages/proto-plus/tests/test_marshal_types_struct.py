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

import pytest
from google.protobuf import struct_pb2

import proto


def test_value_primitives_read():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    assert Foo(value=3).value == 3.0
    assert Foo(value="3").value == "3"
    assert Foo(value=None).value is None
    assert Foo(value=False).value is False
    assert Foo(value=True).value is True


def test_value_absent():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    assert Foo().value is None


def test_value_primitives_rmw():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo()
    foo.value = 3
    assert isinstance(foo.value, float)
    assert abs(Foo.pb(foo).value.number_value - 3.0) < 1e-7
    foo.value = False
    assert not foo.value
    assert foo.value is False
    assert Foo.pb(foo).value.WhichOneof("kind") == "bool_value"
    foo.value = None
    assert not foo.value
    assert foo.value is None
    assert Foo.pb(foo).value.WhichOneof("kind") == "null_value"


def test_value_write_pb():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value=struct_pb2.Value(string_value="stringy"))
    assert foo.value == "stringy"


def test_value_lists_read():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value=["3", None, "foo", True])
    assert foo.value == ["3", None, "foo", True]


def test_value_lists_null():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.ListValue, number=1)

    foo = Foo()
    assert foo.value is None


def test_value_struct_null():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Struct, number=1)

    foo = Foo()
    assert foo.value is None


def test_value_lists_rmw():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value=["3", None, "foo", True])
    foo.value.append("bar")
    foo.value.pop(1)
    assert foo.value == ["3", "foo", True, "bar"]


def test_value_lists_nested():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value=[[True, False], [True, False]])
    foo.value.append([False, True])
    assert foo.value == [[True, False], [True, False], [False, True]]


def test_value_lists_struct():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value=[{"foo": "bar", "spam": "eggs"}])
    assert foo.value == [{"foo": "bar", "spam": "eggs"}]


def test_value_lists_detachment():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value=["foo", "bar"])
    detached_list = foo.value
    detached_list.append("baz")
    assert foo.value == ["foo", "bar", "baz"]


def test_value_structs_read():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value={"foo": True, "bar": False})
    assert foo.value == {"foo": True, "bar": False}


def test_value_structs_rmw():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value={"foo": True, "bar": False})
    foo.value["baz"] = "a string"
    assert foo.value == {"foo": True, "bar": False, "baz": "a string"}


def test_value_structs_nested():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo(value={"foo": True, "bar": {"spam": "eggs"}})
    assert foo.value == {"foo": True, "bar": {"spam": "eggs"}}
    sv = Foo.pb(foo).value.struct_value
    assert sv["foo"] is True
    assert sv["bar"].fields["spam"].string_value == "eggs"


def test_value_invalid_value():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    with pytest.raises(ValueError):
        Foo(value=object())


def test_value_unset():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Value, number=1)

    foo = Foo()
    assert "value" not in foo


def test_list_value_read():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.ListValue, number=1)

    foo = Foo(value=["foo", "bar", True, {"spam": "eggs"}])
    assert foo.value == ["foo", "bar", True, {"spam": "eggs"}]


def test_list_value_pb():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.ListValue, number=1)

    foo = Foo(
        value=struct_pb2.ListValue(
            values=[
                struct_pb2.Value(string_value="foo"),
                struct_pb2.Value(string_value="bar"),
                struct_pb2.Value(bool_value=True),
            ]
        )
    )
    assert foo.value == ["foo", "bar", True]


def test_list_value_reassignment():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.ListValue, number=1)

    foo = Foo(value=["foo", "bar"])
    detached = foo.value
    detached.append(True)
    foo.value = detached
    assert foo.value == ["foo", "bar", True]


def test_list_value_invalid():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.ListValue, number=1)

    with pytest.raises(TypeError):
        Foo(value=3)


def test_struct_read():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Struct, number=1)

    foo = Foo(value={"foo": "bar", "bacon": True})
    assert foo.value == {"foo": "bar", "bacon": True}


def test_struct_pb():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Struct, number=1)

    foo = Foo(
        value=struct_pb2.Struct(
            fields={
                "foo": struct_pb2.Value(string_value="bar"),
                "bacon": struct_pb2.Value(bool_value=True),
            }
        )
    )
    assert foo.value == {"foo": "bar", "bacon": True}


def test_struct_reassignment():
    class Foo(proto.Message):
        value = proto.Field(struct_pb2.Struct, number=1)

    foo = Foo(value={"foo": "bar"})
    detached = foo.value
    detached["bacon"] = True
    foo.value = detached
    assert foo.value == {"foo": "bar", "bacon": True}


def test_struct_nested():
    class Foo(proto.Message):
        struct_field: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=1,
            message=struct_pb2.Struct,
        )

    class Bar(proto.Message):
        foo_field: Foo = proto.Field(
            proto.MESSAGE,
            number=1,
            message=Foo,
        )

    foo = Foo({"struct_field": {"foo": "bagel"}})
    assert foo.struct_field == {"foo": "bagel"}

    bar = Bar({"foo_field": {"struct_field": {"foo": "cheese"}}})
    assert bar.foo_field == Foo({"struct_field": {"foo": "cheese"}})
    assert bar.foo_field.struct_field == {"foo": "cheese"}
