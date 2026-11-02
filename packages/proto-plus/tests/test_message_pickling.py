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
import pickle

import proto


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


def test_pickling():
    s = Squid(mass_kg=20)
    colors = ["RED", "BROWN", "WHITE", "BLUE"]
    s.chromatophores = [
        {"color": c} for c in itertools.islice(itertools.cycle(colors), 10)
    ]

    pickled = pickle.dumps(s)

    unpickled = pickle.loads(pickled)

    assert unpickled == s
