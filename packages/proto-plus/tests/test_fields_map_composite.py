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


def test_composite_map():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    class Baz(proto.Message):
        foos = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message=Foo,
        )

    baz = Baz(foos={"i": Foo(bar=42), "j": Foo(bar=24)})
    assert len(baz.foos) == 2
    assert baz.foos["i"].bar == 42
    assert baz.foos["j"].bar == 24
    assert "k" not in baz.foos


def test_composite_map_dict():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    class Baz(proto.Message):
        foos = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message=Foo,
        )

    baz = Baz(foos={"i": {"bar": 42}, "j": {"bar": 24}})
    assert len(baz.foos) == 2
    assert baz.foos["i"].bar == 42
    assert baz.foos["j"].bar == 24
    assert "k" not in baz.foos
    with pytest.raises(KeyError):
        baz.foos["k"]


def test_composite_map_set():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    class Baz(proto.Message):
        foos = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message=Foo,
        )

    baz = Baz()
    baz.foos["i"] = Foo(bar=42)
    baz.foos["j"] = Foo(bar=24)
    assert len(baz.foos) == 2
    assert baz.foos["i"].bar == 42
    assert baz.foos["j"].bar == 24
    assert "k" not in baz.foos


def test_composite_map_deep_set():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    class Baz(proto.Message):
        foos = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message=Foo,
        )

    baz = Baz()
    baz.foos["i"] = Foo()
    baz.foos["i"].bar = 42
    assert len(baz.foos) == 1
    assert baz.foos["i"].bar == 42


def test_composite_map_del():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1)

    class Baz(proto.Message):
        foos = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message=Foo,
        )

    baz = Baz()
    baz.foos["i"] = Foo(bar=42)
    assert len(baz.foos) == 1
    del baz.foos["i"]
    assert len(baz.foos) == 0
    assert "i" not in baz.foos
