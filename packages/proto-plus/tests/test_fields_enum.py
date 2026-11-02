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

import sys

import proto


def test_outer_enum_init():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo(color=Color.RED)
    assert foo.color == Color.RED
    assert foo.color == 1
    assert foo.color
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 1


def test_outer_enum_init_int():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo(color=1)
    assert foo.color == Color.RED
    assert foo.color == 1
    assert foo.color
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 1


def test_outer_enum_init_str():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo(color="RED")
    assert foo.color == Color.RED
    assert foo.color == 1
    assert foo.color
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 1


def test_outer_enum_init_dict():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo({"color": 1})
    assert foo.color == Color.RED
    assert foo.color == 1
    assert foo.color
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 1


def test_outer_enum_init_dict_str():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo({"color": "BLUE"})
    assert foo.color == Color.BLUE
    assert foo.color == 3
    assert foo.color
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 3


def test_outer_enum_init_pb2():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo(Foo.pb()(color=Color.RED))
    assert foo.color == Color.RED
    assert foo.color == 1
    assert foo.color
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 1


def test_outer_enum_unset():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo()
    assert foo.color == Color.COLOR_UNSPECIFIED
    assert foo.color == 0
    assert "color" not in foo
    assert not foo.color
    assert Foo.pb(foo).color == 0
    assert Foo.serialize(foo) == b""


def test_outer_enum_write():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo()
    foo.color = Color.GREEN
    assert foo.color == Color.GREEN
    assert foo.color == 2
    assert Foo.pb(foo).color == 2
    assert foo.color


def test_outer_enum_write_int():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo()
    foo.color = 3
    assert foo.color == Color.BLUE
    assert foo.color == 3
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 3
    assert foo.color


def test_outer_enum_write_str():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo()
    foo.color = "BLUE"
    assert foo.color == Color.BLUE
    assert foo.color == 3
    assert isinstance(foo.color, Color)
    assert Foo.pb(foo).color == 3
    assert foo.color


def test_inner_enum_init():
    class Foo(proto.Message):
        class Color(proto.Enum):
            COLOR_UNSPECIFIED = 0
            RED = 1
            GREEN = 2
            BLUE = 3

        color = proto.Field(Color, number=1)

    foo = Foo(color=Foo.Color.RED)
    assert foo.color == Foo.Color.RED
    assert foo.color == 1
    assert foo.color
    assert Foo.pb(foo).color == 1


def test_inner_enum_write():
    class Foo(proto.Message):
        class Color(proto.Enum):
            COLOR_UNSPECIFIED = 0
            RED = 1
            GREEN = 2
            BLUE = 3

        color = proto.Field(Color, number=1)

    foo = Foo()
    foo.color = Foo.Color.GREEN
    assert foo.color == Foo.Color.GREEN
    assert foo.color == 2
    assert isinstance(foo.color, Foo.Color)
    assert Foo.pb(foo).color == 2
    assert foo.color


def test_enum_del():
    class Foo(proto.Message):
        color = proto.Field(proto.ENUM, number=1, enum="Color")

    class Color(proto.Enum):
        COLOR_UNSPECIFIED = 0
        RED = 1
        GREEN = 2
        BLUE = 3

    foo = Foo(color=Color.BLUE)
    del foo.color
    assert foo.color == Color.COLOR_UNSPECIFIED
    assert foo.color == 0
    assert isinstance(foo.color, Color)
    assert "color" not in foo
    assert not foo.color
    assert Foo.pb(foo).color == 0


def test_nested_enum_from_string():
    class Trawl(proto.Message):
        # Note: this indirection with the nested field
        # is necessary to trigger the exception for testing.
        # Setting the field in an existing message accepts strings AND
        # checks for valid variants.
        # Similarly, constructing a message directly with a top level
        # enum field kwarg passed as a string is also handled correctly, i.e.
        # s = Squid(zone="ABYSSOPELAGIC")
        # does NOT raise an exception.
        squids = proto.RepeatedField("Squid", number=1)

    class Squid(proto.Message):
        zone = proto.Field(proto.ENUM, number=1, enum="Zone")

    class Zone(proto.Enum):
        EPIPELAGIC = 0
        MESOPELAGIC = 1
        BATHYPELAGIC = 2
        ABYSSOPELAGIC = 3

    t = Trawl(squids=[{"zone": "MESOPELAGIC"}])
    assert t.squids[0] == Squid(zone=Zone.MESOPELAGIC)


def test_enum_field_by_string():
    class Squid(proto.Message):
        zone = proto.Field(proto.ENUM, number=1, enum="Zone")

    class Zone(proto.Enum):
        EPIPELAGIC = 0
        MESOPELAGIC = 1
        BATHYPELAGIC = 2
        ABYSSOPELAGIC = 3

    s = Squid(zone=Zone.BATHYPELAGIC)
    assert s.zone == Zone.BATHYPELAGIC


def test_enum_field_by_string_with_package():
    sys.modules[__name__].__protobuf__ = proto.module(package="mollusca.cephalopoda")
    try:

        class Octopus(proto.Message):
            zone = proto.Field(proto.ENUM, number=1, enum="mollusca.cephalopoda.Zone")

        class Zone(proto.Enum):
            EPIPELAGIC = 0
            MESOPELAGIC = 1
            BATHYPELAGIC = 2
            ABYSSOPELAGIC = 3

    finally:
        del sys.modules[__name__].__protobuf__

    o = Octopus(zone="MESOPELAGIC")
    assert o.zone == Zone.MESOPELAGIC


def test_enums_in_different_files():
    import mollusc
    import zone

    m = mollusc.Mollusc(zone="BATHYPELAGIC")

    assert m.zone == zone.Zone.BATHYPELAGIC


def test_enums_in_one_file():
    import clam

    c = clam.Clam(species=clam.Species.DURASA)
    assert c.species == clam.Species.DURASA


def test_unwrapped_enum_fields():
    # The dayofweek_pb2 module apparently does some things that are deprecated
    # in the protobuf API.
    # There's nothing we can do about that, so ignore it.
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)

    from google.type import dayofweek_pb2 as dayofweek

    class Event(proto.Message):
        weekday = proto.Field(proto.ENUM, number=1, enum=dayofweek.DayOfWeek)

    e = Event(weekday="WEDNESDAY")
    e2 = Event.deserialize(Event.serialize(e))
    assert e == e2

    class Task(proto.Message):
        weekday = proto.Field(dayofweek.DayOfWeek, number=1)

    t = Task(weekday="TUESDAY")
    t2 = Task.deserialize(Task.serialize(t))
    assert t == t2


def test_enum_alias_good():
    # Have to split good and bad enum alias into two tests so that the generated
    # file descriptor is properly created.
    # For the python runtime, aliases are allowed by default, but we want to
    # make sure that the options don't cause problems.
    # For the cpp runtime, we need to verify that we can in fact define aliases.
    class GoodMessage(proto.Message):
        class GoodEnum(proto.Enum):
            _pb_options = {"allow_alias": True}
            UNKNOWN = 0
            DEFAULT = 0

        good_dup_enum = proto.Field(proto.ENUM, number=1, enum=GoodEnum)

    assert GoodMessage.GoodEnum.UNKNOWN == GoodMessage.GoodEnum.DEFAULT == 0
