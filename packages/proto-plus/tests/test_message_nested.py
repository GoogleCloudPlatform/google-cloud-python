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

import proto


def test_singly_nested_message():
    class Foo(proto.Message):
        class Bar(proto.Message):
            value = proto.Field(proto.INT32, number=1)

        bar = proto.Field(proto.MESSAGE, number=1, message=Bar)

    foo = Foo(bar=Foo.Bar(value=42))
    assert foo.bar.value == 42


def test_multiply_nested_message():
    class Foo(proto.Message):
        class Bar(proto.Message):
            class Baz(proto.Message):
                value = proto.Field(proto.INT32, number=1)

            baz = proto.Field(proto.MESSAGE, number=1, message=Baz)

        bar = proto.Field(proto.MESSAGE, number=1, message=Bar)

    foo = Foo(bar=Foo.Bar(baz=Foo.Bar.Baz(value=42)))
    assert foo.bar.baz.value == 42


def test_forking_nested_messages():
    class Foo(proto.Message):
        class Bar(proto.Message):
            spam = proto.Field(proto.STRING, number=1)
            eggs = proto.Field(proto.BOOL, number=2)

        class Baz(proto.Message):
            class Bacon(proto.Message):
                value = proto.Field(proto.INT32, number=1)

            bacon = proto.Field(proto.MESSAGE, number=1, message=Bacon)

        bar = proto.Field(proto.MESSAGE, number=1, message=Bar)
        baz = proto.Field(proto.MESSAGE, number=2, message=Baz)

    foo = Foo(
        bar={"spam": "xyz", "eggs": False},
        baz=Foo.Baz(bacon=Foo.Baz.Bacon(value=42)),
    )
    assert foo.bar.spam == "xyz"
    assert not foo.bar.eggs
    assert foo.baz.bacon.value == 42
