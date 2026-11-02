# Copyright 2020 Google LLC
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


def test_optional_init():
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1, optional=True)

    squid_1 = Squid(mass_kg=20)
    squid_2 = Squid()

    assert Squid.mass_kg in squid_1
    assert squid_1.mass_kg == 20
    assert Squid.mass_kg not in squid_2

    squid_2.mass_kg = 30
    assert squid_2.mass_kg == 30
    assert Squid.mass_kg in squid_2

    del squid_1.mass_kg
    assert Squid.mass_kg not in squid_1

    with pytest.raises(AttributeError):
        Squid.shell


def test_optional_and_oneof():
    # This test is a defensive check that synthetic oneofs
    # don't interfere with user defined oneofs.

    # Oneof defined before an optional
    class Squid(proto.Message):
        mass_kg = proto.Field(proto.INT32, number=1, oneof="mass")
        mass_lbs = proto.Field(proto.INT32, number=2, oneof="mass")

        iridiphore_num = proto.Field(proto.INT32, number=3, optional=True)

    s = Squid(mass_kg=20)
    assert s.mass_kg == 20
    assert not s.mass_lbs
    assert Squid.iridiphore_num not in s

    s.iridiphore_num = 600
    assert s.mass_kg == 20
    assert not s.mass_lbs
    assert Squid.iridiphore_num in s

    s = Squid(mass_lbs=40, iridiphore_num=600)
    assert not s.mass_kg
    assert s.mass_lbs == 40
    assert s.iridiphore_num == 600

    # Oneof defined after an optional
    class Clam(proto.Message):
        flute_radius = proto.Field(proto.INT32, number=1, optional=True)

        mass_kg = proto.Field(proto.INT32, number=2, oneof="mass")
        mass_lbs = proto.Field(proto.INT32, number=3, oneof="mass")

    c = Clam(mass_kg=20)

    assert c.mass_kg == 20
    assert not c.mass_lbs
    assert Clam.flute_radius not in c
    c.flute_radius = 30
    assert c.mass_kg == 20
    assert not c.mass_lbs

    c = Clam(mass_lbs=40, flute_radius=30)
    assert c.mass_lbs == 40
    assert not c.mass_kg
    assert c.flute_radius == 30
