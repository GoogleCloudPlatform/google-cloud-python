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


def test_string_init():
    class Foo(proto.Message):
        bar = proto.Field(proto.STRING, number=1)
        baz = proto.Field(proto.STRING, number=2)

    foo = Foo(bar="spam")
    assert foo.bar == "spam"
    assert foo.baz == ""
    assert not foo.baz
    assert Foo.pb(foo).bar == "spam"
    assert Foo.pb(foo).baz == ""


def test_string_rmw():
    class Foo(proto.Message):
        spam = proto.Field(proto.STRING, number=1)
        eggs = proto.Field(proto.STRING, number=2)

    foo = Foo(spam="bar")
    foo.eggs = "baz"
    assert foo.spam == "bar"
    assert foo.eggs == "baz"
    assert Foo.pb(foo).spam == "bar"
    assert Foo.pb(foo).eggs == "baz"
    foo.spam = "bacon"
    assert foo.spam == "bacon"
    assert foo.eggs == "baz"
    assert Foo.pb(foo).spam == "bacon"
    assert Foo.pb(foo).eggs == "baz"


def test_string_del():
    class Foo(proto.Message):
        bar = proto.Field(proto.STRING, number=1)

    foo = Foo(bar="spam")
    assert foo.bar == "spam"
    del foo.bar
    assert foo.bar == ""
    assert not foo.bar
