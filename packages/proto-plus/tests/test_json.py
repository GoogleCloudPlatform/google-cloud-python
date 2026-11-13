# Copyright (C) 2020  Google LLC
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

import re

import pytest
from google.protobuf.json_format import ParseError

import proto


def test_message_to_json():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    s = Squid(mass_kg=100)
    json = Squid.to_json(s)
    json = json.replace(" ", "").replace("\n", "")
    assert json == '{"massKg":100}'


def test_message_to_json_no_indent():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)
        name = proto.Field(proto.STRING, number=2)

    s = Squid(mass_kg=100, name="no_new_lines_squid")
    json = Squid.to_json(s, indent=None)
    assert json == '{"massKg": 100, "name": "no_new_lines_squid"}'


def test_message_from_json():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    json = """{
    "massKg": 100
    }
    """

    s = Squid.from_json(json)
    assert s == Squid(mass_kg=100)


def test_message_json_round_trip():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    s = Squid(mass_kg=100)
    json = Squid.to_json(s)
    s2 = Squid.from_json(json)

    assert s == s2


def test_json_stringy_enums():
    class Squid(proto.Message):
        zone = proto.Field(proto.ENUM, number=1, enum="Zone")

    class Zone(proto.Enum):
        EPIPELAGIC = 0
        MESOPELAGIC = 1
        BATHYPELAGIC = 2
        ABYSSOPELAGIC = 3

    s1 = Squid(zone=Zone.MESOPELAGIC)
    json = (
        Squid.to_json(s1, use_integers_for_enums=False)
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json == '{"zone":"MESOPELAGIC"}'

    s2 = Squid.from_json(json)
    assert s2.zone == s1.zone


def test_json_default_enums():
    class Squid(proto.Message):
        zone = proto.Field(proto.ENUM, number=1, enum="Zone")

    class Zone(proto.Enum):
        EPIPELAGIC = 0
        MESOPELAGIC = 1
        BATHYPELAGIC = 2
        ABYSSOPELAGIC = 3

    s = Squid()
    assert s.zone == Zone.EPIPELAGIC
    json1 = Squid.to_json(s).replace(" ", "").replace("\n", "")
    assert json1 == '{"zone":0}'

    json2 = (
        Squid.to_json(s, use_integers_for_enums=False)
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json2 == '{"zone":"EPIPELAGIC"}'


def test_json_default_values():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)
        name = proto.Field(proto.STRING, number=2)

    s = Squid(name="Steve")
    json1 = (
        Squid.to_json(s, including_default_value_fields=False)
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json1 == '{"name":"Steve"}'

    json1 = (
        Squid.to_json(s, always_print_fields_with_no_presence=False)
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json1 == '{"name":"Steve"}'

    json1 = (
        Squid.to_json(
            s,
            including_default_value_fields=False,
            always_print_fields_with_no_presence=False,
        )
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json1 == '{"name":"Steve"}'

    with pytest.raises(
        ValueError,
        match="Arguments.*always_print_fields_with_no_presence.*including_default_value_fields.*must match",
    ):
        Squid.to_json(
            s,
            including_default_value_fields=True,
            always_print_fields_with_no_presence=False,
        ).replace(" ", "").replace("\n", "")

    with pytest.raises(
        ValueError,
        match="Arguments.*always_print_fields_with_no_presence.*including_default_value_fields.*must match",
    ):
        Squid.to_json(
            s,
            including_default_value_fields=False,
            always_print_fields_with_no_presence=True,
        ).replace(" ", "").replace("\n", "")

    json2 = (
        Squid.to_json(
            s,
            including_default_value_fields=True,
            always_print_fields_with_no_presence=True,
        )
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json2 == '{"name":"Steve","massKg":0}'

    json2 = (
        Squid.to_json(
            s,
            including_default_value_fields=True,
        )
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json2 == '{"name":"Steve","massKg":0}'

    json2 = (
        Squid.to_json(
            s,
            always_print_fields_with_no_presence=True,
        )
        .replace(" ", "")
        .replace("\n", "")
    )
    assert json2 == '{"name":"Steve","massKg":0}'

    json2 = Squid.to_json(s).replace(" ", "").replace("\n", "")
    assert json2 == '{"name":"Steve","massKg":0}'

    s1 = Squid.from_json(json1)
    s2 = Squid.from_json(json2)
    assert s == s1 == s2


def test_json_unknown_field():
    # Note that 'lengthCm' is unknown in the local definition.
    # This could happen if the client is using an older proto definition
    # than the server.
    json_str = '{\n  "massKg": 20,\n  "lengthCm": 100\n}'

    class Octopus(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    o = Octopus.from_json(json_str, ignore_unknown_fields=True)
    assert not hasattr(o, "length_cm")
    assert not hasattr(o, "lengthCm")

    # Don't permit unknown fields by default
    with pytest.raises(ParseError):
        o = Octopus.from_json(json_str)


def test_json_snake_case():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1)

    json_str = '{\n  "mass_kg": 20\n}'
    s = Squid.from_json(json_str)

    assert s.mass_kg == 20

    assert Squid.to_json(s, preserving_proto_field_name=True) == json_str


def test_json_name():
    class Squid(proto.Message):
        massKg = proto.Field(proto.INT32, number=1, json_name="mass_in_kilograms")

    s = Squid(massKg=20)
    j = Squid.to_json(s)

    assert "mass_in_kilograms" in j

    s_two = Squid.from_json(j)

    assert s == s_two


def test_json_sort_keys():
    class Squid(proto.Message):
        name = proto.Field(proto.STRING, number=1)
        mass_kg = proto.Field(proto.INT32, number=2)

    s = Squid(name="Steve", mass_kg=20)
    j = Squid.to_json(s, sort_keys=True, indent=None)

    assert re.search(r"massKg.*name", j)


@pytest.mark.parametrize(
    "expect_proto_7_plus", [True, False], ids=["proto >= 7", "proto <= 6"]
)
def test_json_float_precision(expect_proto_7_plus):
    if (expect_proto_7_plus and int(proto.message._PROTOBUF_MAJOR_VERSION) < 7) or (
        not expect_proto_7_plus and int(proto.message._PROTOBUF_MAJOR_VERSION) >= 7
    ):
        pytest.skip("installed proto version does not match test")

    class Squid(proto.Message):
        name = proto.Field(proto.STRING, number=1)
        mass_kg = proto.Field(proto.FLOAT, number=2)

    with pytest.warns(DeprecationWarning) as warnings:
        s = Squid(name="Steve", mass_kg=3.141592)
        j = Squid.to_json(s, float_precision=3, indent=None)

    assert len(warnings) == 1

    # for protobuf <7, expect truncated float
    if expect_proto_7_plus:
        assert j == '{"name": "Steve", "massKg": 3.141592}'
        assert "`float_precision` was removed" in warnings[0].message.args[0]
    else:
        assert j == '{"name": "Steve", "massKg": 3.14}'
        assert "`float_precision` will be removed" in warnings[0].message.args[0]
