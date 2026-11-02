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

import proto

__protobuf__ = proto.module(
    package="ocean.clam.v1",
    manifest={
        "Clam",
        "Species",
        "Color",
    },
)


class Species(proto.Enum):
    UNKNOWN = 0
    SQUAMOSA = 1
    DURASA = 2
    GIGAS = 3


class Color(proto.Enum):
    COLOR_UNKNOWN = 0
    BLUE = 1
    ORANGE = 2
    GREEN = 3


class Clam(proto.Message):
    species = proto.Field(proto.ENUM, number=1, enum="Species")
    mass_kg = proto.Field(proto.DOUBLE, number=2)
    color = proto.Field(proto.ENUM, number=3, enum="Color")
