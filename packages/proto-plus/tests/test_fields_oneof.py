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


def test_oneof():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1, oneof="bacon")
        baz = proto.Field(proto.STRING, number=2, oneof="bacon")

    foo = Foo(bar=42)
    assert foo.bar == 42
    assert not foo.baz
    foo.baz = "the answer"
    assert not foo.bar
    assert foo.baz == "the answer"


def test_multiple_oneofs():
    class Foo(proto.Message):
        bar = proto.Field(proto.INT32, number=1, oneof="spam")
        baz = proto.Field(proto.STRING, number=2, oneof="spam")
        bacon = proto.Field(proto.FLOAT, number=3, oneof="eggs")
        ham = proto.Field(proto.STRING, number=4, oneof="eggs")

    foo = Foo()
    foo.bar = 42
    foo.bacon = 42.0
    assert foo.bar == 42
    assert foo.bacon == 42.0
    assert not foo.baz
    assert not foo.ham
    foo.ham = "this one gets assigned"
    assert not foo.bacon
    assert foo.ham == "this one gets assigned"
    assert foo.bar == 42
    assert not foo.baz
