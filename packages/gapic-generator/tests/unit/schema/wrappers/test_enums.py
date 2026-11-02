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

from typing import Tuple

from google.protobuf import descriptor_pb2

from gapic.schema import metadata
from gapic.schema import wrappers

from test_utils.test_utils import make_enum


def test_enum_properties():
    enum_type = make_enum(name="Color")
    assert enum_type.name == "Color"


def test_enum_value_properties():
    enum_type = make_enum(
        name="Irrelevant",
        values=(
            ("RED", 1),
            ("GREEN", 2),
            ("BLUE", 3),
        ),
    )
    assert len(enum_type.values) == 3
    for ev, expected in zip(enum_type.values, ("RED", "GREEN", "BLUE")):
        assert ev.name == expected


def test_enum_ident():
    enum = make_enum("Baz", package="foo.v1", module="bar")
    assert str(enum.ident) == "bar.Baz"
    assert enum.ident.sphinx == "foo.v1.bar.Baz"


def test_enum_options_dict():
    cephalopod = make_enum(
        "Cephalopod",
        package="animalia.v1",
        module="mollusca",
        options={"allow_alias": True},
    )
    assert isinstance(cephalopod.enum_pb.options, descriptor_pb2.EnumOptions)
    assert cephalopod.options_dict == {"allow_alias": True}

    bivalve = make_enum("Bivalve", package="animalia.v1", module="mollusca")
    assert isinstance(bivalve.enum_pb.options, descriptor_pb2.EnumOptions)
    assert bivalve.options_dict == {}
