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

import itertools

import pytest

import proto


def test_message_constructor_instance():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    foo_original = Foo(bar=42)
    foo_copy = Foo(foo_original)
    assert foo_original.bar == foo_copy.bar == 42
    assert foo_original == foo_copy
    assert foo_original is not foo_copy
    assert isinstance(foo_original, Foo)
    assert isinstance(foo_copy, Foo)
    assert isinstance(Foo.pb(foo_copy), Foo.pb())


def test_message_constructor_underlying_pb2():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    foo_pb2 = Foo.pb()(bar=42)
    foo = Foo(foo_pb2)
    assert foo.bar == Foo.pb(foo).bar == foo_pb2.bar == 42
    assert foo == foo_pb2  # Not communitive. Nothing we can do about that.
    assert foo_pb2 == Foo.pb(foo)
    assert foo_pb2 is not Foo.pb(foo)
    assert isinstance(foo, Foo)
    assert isinstance(Foo.pb(foo), Foo.pb())
    assert isinstance(foo_pb2, Foo.pb())


def test_message_constructor_underlying_pb2_and_kwargs():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    foo_pb2 = Foo.pb()(bar=42)
    foo = Foo(foo_pb2, bar=99)
    assert foo.bar == Foo.pb(foo).bar == 99
    assert foo_pb2.bar == 42
    assert isinstance(foo, Foo)
    assert isinstance(Foo.pb(foo), Foo.pb())
    assert isinstance(foo_pb2, Foo.pb())


def test_message_constructor_dict():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    foo = Foo({"bar": 42})
    assert foo.bar == Foo.pb(foo).bar == 42
    assert foo != {"bar": 42}
    assert isinstance(foo, Foo)
    assert isinstance(Foo.pb(foo), Foo.pb())


def test_message_constructor_kwargs():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    foo = Foo(bar=42)
    assert foo.bar == Foo.pb(foo).bar == 42
    assert isinstance(foo, Foo)
    assert isinstance(Foo.pb(foo), Foo.pb())


def test_message_constructor_invalid():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    with pytest.raises(TypeError):
        Foo(object())


def test_message_constructor_explicit_qualname():
    class Foo(proto.Message):
        __qualname__ = "Foo"
        bar = proto.Field(proto.INT64, number=1)

    foo_original = Foo(bar=42)
    foo_copy = Foo(foo_original)
    assert foo_original.bar == foo_copy.bar == 42
    assert foo_original == foo_copy
    assert foo_original is not foo_copy
    assert isinstance(foo_original, Foo)
    assert isinstance(foo_copy, Foo)
    assert isinstance(Foo.pb(foo_copy), Foo.pb())


def test_message_contains_primitive():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    assert "bar" in Foo(bar=42)
    assert "bar" not in Foo(bar=0)
    assert "bar" not in Foo()


def test_message_contains_composite():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    class Baz(proto.Message):
        foo = proto.Field(proto.MESSAGE, number=1, message=Foo)

    assert "foo" in Baz(foo=Foo(bar=42))
    assert "foo" in Baz(foo=Foo())
    assert "foo" not in Baz()


def test_message_contains_repeated_primitive():
    class Foo(proto.Message):
        bar = proto.RepeatedField(proto.INT64, number=1)

    assert "bar" in Foo(bar=[1, 1, 2, 3, 5])
    assert "bar" in Foo(bar=[0])
    assert "bar" not in Foo(bar=[])
    assert "bar" not in Foo()


def test_message_contains_repeated_composite():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    class Baz(proto.Message):
        foo = proto.RepeatedField(proto.MESSAGE, number=1, message=Foo)

    assert "foo" in Baz(foo=[Foo(bar=42)])
    assert "foo" in Baz(foo=[Foo()])
    assert "foo" not in Baz(foo=[])
    assert "foo" not in Baz()


def test_message_eq_primitives():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)
        baz = proto.Field(proto.STRING, number=2)
        bacon = proto.Field(proto.BOOL, number=3)

    assert Foo() == Foo()
    assert Foo(bar=42, baz="42") == Foo(bar=42, baz="42")
    assert Foo(bar=42, baz="42") != Foo(baz="42")
    assert Foo(bar=42, bacon=True) == Foo(bar=42, bacon=True)
    assert Foo(bar=42, bacon=True) != Foo(bar=42)
    assert Foo(bar=42, baz="42", bacon=True) != Foo(bar=42, bacon=True)
    assert Foo(bacon=False) == Foo()
    assert Foo(bacon=True) != Foo(bacon=False)
    assert Foo(bar=21 * 2) == Foo(bar=42)
    assert Foo() == Foo(bar=0)
    assert Foo() == Foo(bar=0, baz="", bacon=False)
    assert Foo() != Foo(bar=0, baz="0", bacon=False)


def test_message_serialize():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)
        baz = proto.Field(proto.STRING, number=2)
        bacon = proto.Field(proto.BOOL, number=3)

    foo = Foo(bar=42, bacon=True)
    assert Foo.serialize(foo) == Foo.pb(foo).SerializeToString()


def test_message_dict_serialize():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)
        baz = proto.Field(proto.STRING, number=2)
        bacon = proto.Field(proto.BOOL, number=3)

    foo = {"bar": 42, "bacon": True}
    assert Foo.serialize(foo) == Foo.pb(foo, coerce=True).SerializeToString()


def test_message_deserialize():
    class OldFoo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    class NewFoo(proto.Message):
        bar = proto.Field(proto.INT64, number=1)

    serialized = OldFoo.serialize(OldFoo(bar=42))
    new_foo = NewFoo.deserialize(serialized)
    assert isinstance(new_foo, NewFoo)
    assert new_foo.bar == 42


def test_message_pb():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    assert isinstance(Foo.pb(Foo()), Foo.pb())
    with pytest.raises(TypeError):
        Foo.pb(object())


def test_invalid_field_access():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    s = Squid()
    with pytest.raises(AttributeError):
        getattr(s, "shell")


def test_setattr():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    s1 = Squid()
    s2 = Squid(mass_kg=20)

    s1._pb = s2._pb

    assert s1.mass_kg == 20


def test_serialize_to_dict():
    class Squid(proto.Message):
        # Test primitives, enums, and repeated fields.
        class Chromatophore(proto.Message):
            class Color(proto.Enum):
                UNKNOWN = 0
                RED = 1
                BROWN = 2
                WHITE = 3
                BLUE = 4

            color = proto.Field(Color, number=1)

        mass_kg = proto.Field(proto.INT32, number=1)
        chromatophores = proto.RepeatedField(Chromatophore, number=2)

    s = Squid(mass_kg=20)
    colors = ["RED", "BROWN", "WHITE", "BLUE"]
    s.chromatophores = [
        {"color": c} for c in itertools.islice(itertools.cycle(colors), 10)
    ]

    s_dict = Squid.to_dict(s)
    assert s_dict["chromatophores"][0]["color"] == 1

    new_s = Squid(s_dict)
    assert new_s == s

    s_dict = Squid.to_dict(s, use_integers_for_enums=False)
    assert s_dict["chromatophores"][0]["color"] == "RED"

    s_new_2 = Squid(mass_kg=20)
    s_dict_2 = Squid.to_dict(s_new_2, including_default_value_fields=False)
    expected_dict = {"mass_kg": 20}
    assert s_dict_2 == expected_dict

    s_dict_2 = Squid.to_dict(s_new_2, always_print_fields_with_no_presence=False)
    expected_dict = {"mass_kg": 20}
    assert s_dict_2 == expected_dict

    s_dict_2 = Squid.to_dict(
        s_new_2,
        including_default_value_fields=False,
        always_print_fields_with_no_presence=False,
    )
    expected_dict = {"mass_kg": 20}
    assert s_dict_2 == expected_dict

    s_dict_2 = Squid.to_dict(
        s_new_2,
        including_default_value_fields=True,
    )
    expected_dict = {"mass_kg": 20, "chromatophores": []}
    assert s_dict_2 == expected_dict

    s_dict_2 = Squid.to_dict(
        s_new_2,
        always_print_fields_with_no_presence=True,
    )
    expected_dict = {"mass_kg": 20, "chromatophores": []}
    assert s_dict_2 == expected_dict

    s_dict_2 = Squid.to_dict(
        s_new_2,
        including_default_value_fields=True,
        always_print_fields_with_no_presence=True,
    )
    expected_dict = {"mass_kg": 20, "chromatophores": []}
    assert s_dict_2 == expected_dict

    s_dict_2 = Squid.to_dict(s_new_2)
    expected_dict = {"mass_kg": 20, "chromatophores": []}
    assert s_dict_2 == expected_dict

    with pytest.raises(
        ValueError,
        match="Arguments.*always_print_fields_with_no_presence.*including_default_value_fields.*must match",
    ):
        s_dict_2 = Squid.to_dict(
            s_new_2,
            including_default_value_fields=True,
            always_print_fields_with_no_presence=False,
        )

    with pytest.raises(
        ValueError,
        match="Arguments.*always_print_fields_with_no_presence.*including_default_value_fields.*must match",
    ):
        s_dict_2 = Squid.to_dict(
            s_new_2,
            including_default_value_fields=False,
            always_print_fields_with_no_presence=True,
        )


@pytest.mark.parametrize(
    "expect_proto_7_plus", [True, False], ids=["proto >= 7", "proto <= 6"]
)
def test_serialize_to_dict_float_precision(expect_proto_7_plus):
    if (expect_proto_7_plus and int(proto.message._PROTOBUF_MAJOR_VERSION) < 7) or (
        not expect_proto_7_plus and int(proto.message._PROTOBUF_MAJOR_VERSION) >= 7
    ):
        pytest.skip("installed proto version does not match test")

    class Squid(proto.Message):
        mass_kg = proto.Field(proto.FLOAT, number=1)

    s = Squid(mass_kg=3.141592)

    with pytest.warns(DeprecationWarning) as warnings:
        s_dict = Squid.to_dict(s, float_precision=3)
    assert len(warnings) == 1
    # for protobuf <7, expect truncated float
    if expect_proto_7_plus:
        assert s_dict["mass_kg"] == pytest.approx(3.141592)
        assert "`float_precision` was removed" in warnings[0].message.args[0]
    else:
        assert s_dict["mass_kg"] == pytest.approx(3.14)
        assert "`float_precision` will be removed" in warnings[0].message.args[0]


def test_unknown_field_deserialize():
    # This is a somewhat common setup: a client uses an older proto definition,
    # while the server sends the newer definition. The client still needs to be
    # able to interact with the protos it receives from the server.

    class Octopus_Old(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    class Octopus_New(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)
        length_cm = proto.Field(proto.INT32, number=2)

    o_new = Octopus_New(mass_kg=20, length_cm=100)
    o_ser = Octopus_New.serialize(o_new)

    o_old = Octopus_Old.deserialize(o_ser)
    assert not hasattr(o_old, "length_cm")


def test_unknown_field_deserialize_keep_fields():
    # This is a somewhat common setup: a client uses an older proto definition,
    # while the server sends the newer definition. The client still needs to be
    # able to interact with the protos it receives from the server.

    class Octopus_Old(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    class Octopus_New(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)
        length_cm = proto.Field(proto.INT32, number=2)

    o_new = Octopus_New(mass_kg=20, length_cm=100)
    o_ser = Octopus_New.serialize(o_new)

    o_old = Octopus_Old.deserialize(o_ser)
    assert not hasattr(o_old, "length_cm")

    o_new = Octopus_New.deserialize(Octopus_Old.serialize(o_old))
    assert o_new.length_cm == 100


def test_unknown_field_from_dict():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    # By default we don't permit unknown fields
    with pytest.raises(ValueError):
        s = Squid({"mass_kg": 20, "length_cm": 100})

    s = Squid({"mass_kg": 20, "length_cm": 100}, ignore_unknown_fields=True)
    assert not hasattr(s, "length_cm")


def test_copy_from():
    class Mollusc(proto.Message):
        class Squid(proto.Message):
            mass_kg = proto.Field(proto.INT32, number=1)

        squid = proto.Field(Squid, number=1)

    m = Mollusc()
    s = Mollusc.Squid(mass_kg=20)
    Mollusc.Squid.copy_from(m.squid, s)
    assert m.squid is not s
    assert m.squid == s

    s.mass_kg = 30
    Mollusc.Squid.copy_from(m.squid, Mollusc.Squid.pb(s))
    assert m.squid == s

    Mollusc.Squid.copy_from(m.squid, {"mass_kg": 10})
    assert m.squid.mass_kg == 10

    with pytest.raises(TypeError):
        Mollusc.Squid.copy_from(m.squid, (("mass_kg", 20)))


def test_dir():
    class Mollusc(proto.Message):
        class Class(proto.Enum):
            UNKNOWN = 0
            GASTROPOD = 1
            BIVALVE = 2
            CEPHALOPOD = 3

        class Arm(proto.Message):
            length_cm = proto.Field(proto.INT32, number=1)

        mass_kg = proto.Field(proto.INT32, number=1)
        class_ = proto.Field(Class, number=2)
        arms = proto.RepeatedField(Arm, number=3)

    expected = (
        {
            # Fields and nested message and enum types
            "arms",
            "class_",
            "mass_kg",
            "Arm",
            "Class",
        }
        | {
            # Other methods and attributes
            "__bool__",
            "__contains__",
            "__dict__",
            "__getattr__",
            "__getstate__",
            "__module__",
            "__setstate__",
            "__weakref__",
        }
        | set(dir(object))
    )  # Gets the long tail of dunder methods and attributes.

    actual = set(dir(Mollusc()))

    # Check instance names
    assert actual == expected

    # Check type names
    expected = (
        set(dir(type))
        | {
            # Class methods from the MessageMeta metaclass
            "copy_from",
            "deserialize",
            "from_json",
            "meta",
            "pb",
            "serialize",
            "to_dict",
            "to_json",
            "wrap",
        }
        | {
            # Nested message and enum types
            "Arm",
            "Class",
        }
    )

    actual = set(dir(Mollusc))
    assert actual == expected


def test_dir_message_base():
    assert set(dir(proto.Message)) == set(dir(type))


def test_invalid_initialization_type_error():
    """Verify that bad types passed to __init__ raise a descriptive TypeError."""

    class UserProfile(proto.Message):
        username = proto.Field(proto.STRING, number=1)
        age = proto.Field(proto.INT32, number=2)

    with pytest.raises(TypeError) as excinfo:
        # Passing a list where a string is expected
        UserProfile(username=["not", "a", "string"])

    error_msg = str(excinfo.value)
    assert "Failed to initialize UserProfile" in error_msg
    assert "Underlying error" in error_msg
    assert isinstance(excinfo.value.__cause__, TypeError)


def test_invalid_assignment_type_error():
    """Verify that bad types assigned via __setattr__ raise a descriptive TypeError."""

    class UserProfile(proto.Message):
        username = proto.Field(proto.STRING, number=1)
        age = proto.Field(proto.INT32, number=2)

    profile = UserProfile()

    with pytest.raises(TypeError) as excinfo:
        # Assigning a dictionary where an integer is expected
        profile.age = {"invalid": "type"}

    error_msg = str(excinfo.value)
    assert "Failed to set field 'age' on UserProfile" in error_msg
    assert "{'invalid': 'type'}" in error_msg
    assert isinstance(excinfo.value.__cause__, TypeError)
