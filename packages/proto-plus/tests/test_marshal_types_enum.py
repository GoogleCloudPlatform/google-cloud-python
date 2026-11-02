# Copyright 2019 Google LLC
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

import warnings
from unittest import mock

import proto
from proto.marshal.rules.enums import EnumRule

__protobuf__ = proto.module(package="test.marshal.enum")


def test_to_proto():
    class Foo(proto.Enum):
        FOO_UNSPECIFIED = 0
        BAR = 1
        BAZ = 2

    enum_rule = EnumRule(Foo)
    foo_a = enum_rule.to_proto(Foo.BAR)
    foo_b = enum_rule.to_proto(1)
    foo_c = enum_rule.to_proto("BAR")
    # We want to distinguish literal `1` from `Foo.BAR` here
    # (they are equivalent but not identical).
    assert foo_a is foo_b is foo_c is 1  # noqa: F632


def test_to_python():
    class Foo(proto.Enum):
        FOO_UNSPECIFIED = 0
        BAR = 1
        BAZ = 2

    enum_rule = EnumRule(Foo)
    foo_a = enum_rule.to_python(1)
    foo_b = enum_rule.to_python(Foo.BAR)
    assert foo_a is foo_b is Foo.BAR


def test_to_python_unknown_value():
    class Foo(proto.Enum):
        FOO_UNSPECIFIED = 0
        BAR = 1
        BAZ = 2

    enum_rule = EnumRule(Foo)
    with mock.patch.object(warnings, "warn") as warn:
        assert enum_rule.to_python(4) == 4
        warn.assert_called_once_with("Unrecognized Foo enum value: 4")


def test_enum_append():
    class Bivalve(proto.Enum):
        CLAM = 0
        OYSTER = 1

    class MolluscContainer(proto.Message):
        bivalves = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum=Bivalve,
        )

    mc = MolluscContainer()
    clam = Bivalve.CLAM
    mc.bivalves.append(clam)
    mc.bivalves.append(1)

    assert mc.bivalves == [clam, Bivalve.OYSTER]


def test_enum_map_insert():
    class Bivalve(proto.Enum):
        CLAM = 0
        OYSTER = 1

    class MolluscContainer(proto.Message):
        bivalves = proto.MapField(
            proto.STRING,
            proto.ENUM,
            number=1,
            enum=Bivalve,
        )

    mc = MolluscContainer()
    clam = Bivalve.CLAM
    mc.bivalves["clam"] = clam
    mc.bivalves["oyster"] = 1
    assert dict(mc.bivalves) == {"clam": clam, "oyster": Bivalve.OYSTER}
