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

import proto


def test_int_init():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)
        baz = proto.Field(proto.INT32, number=2)

    foo = Foo(bar=42)
    assert foo.bar == 42
    assert foo.baz == 0
    assert not foo.baz
    assert Foo.pb(foo).bar == 42
    assert Foo.pb(foo).baz == 0


def test_int_rmw():
    class Foo(proto.Message):
        spam = proto.Field(proto.INT32, number=1)
        eggs = proto.Field(proto.INT32, number=2)

    foo = Foo(spam=42)
    foo.eggs = 76  # trombones led the big parade...
    assert foo.spam == 42
    assert foo.eggs == 76
    assert Foo.pb(foo).spam == 42
    assert Foo.pb(foo).eggs == 76
    foo.spam = 144
    assert foo.spam == 144
    assert foo.eggs == 76
    assert Foo.pb(foo).spam == 144
    assert Foo.pb(foo).eggs == 76


def test_int_del():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    foo = Foo(bar=42)
    assert foo.bar == 42
    del foo.bar
    assert foo.bar == 0
    assert not foo.bar


def test_int_size():
    class Foo(proto.Message):
        small = proto.Field(proto.INT32, number=1)
        big = proto.Field(proto.INT64, number=2)

    foo = Foo()
    foo.big = 2**40
    assert foo.big == 2**40
    with pytest.raises(ValueError):
        foo.small = 2**40
    with pytest.raises(ValueError):
        Foo(small=2**40)


def test_int_unsigned():
    class Foo(proto.Message):
        signed = proto.Field(proto.INT32, number=1)
        unsigned = proto.Field(proto.UINT32, number=2)

    foo = Foo()
    foo.signed = -10
    assert foo.signed == -10
    with pytest.raises(ValueError):
        foo.unsigned = -10
    with pytest.raises(ValueError):
        Foo(unsigned=-10)


def test_field_descriptor_idempotent():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    bar_field = Foo.meta.fields["bar"]
    assert bar_field.descriptor is bar_field.descriptor


def test_int64_dict_round_trip():
    # When converting a message to other types, protobuf turns int64 fields
    # into decimal coded strings.
    # This is not a problem for round trip JSON, but it is a problem
    # when doing a round trip conversion from a message to a dict to a message.
    # See https://github.com/protocolbuffers/protobuf/issues/2679
    # and
    # https://developers.google.com/protocol-buffers/docs/proto3#json
    # for more details.
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT64, number=1)
        length_cm = proto.Field(proto.UINT64, number=2)
        age_s = proto.Field(proto.FIXED64, number=3)
        depth_m = proto.Field(proto.SFIXED64, number=4)
        serial_num = proto.Field(proto.SINT64, number=5)

    s = Squid(mass_kg=10, length_cm=20, age_s=30, depth_m=40, serial_num=50)

    s_dict = Squid.to_dict(s)

    s2 = Squid(s_dict)

    assert s == s2

    # Double check that the conversion works with deeply nested messages.
    class Clam(proto.Message):
        class Shell(proto.Message):
            class Pearl(proto.Message):
                mass_kg = proto.Field(proto.INT64, number=1)

            pearl = proto.Field(Pearl, number=1)

        shell = proto.Field(Shell, number=1)

    c = Clam(shell=Clam.Shell(pearl=Clam.Shell.Pearl(mass_kg=10)))

    c_dict = Clam.to_dict(c)

    c2 = Clam(c_dict)

    assert c == c2
