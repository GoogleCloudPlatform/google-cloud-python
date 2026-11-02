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


def test_composite_forward_ref():
    class Spam(proto.Message):
        foo = proto.Field(proto.MESSAGE, number=1, message="Foo")
        eggs = proto.Field(proto.BOOL, number=2)

    class Foo(proto.Message):
        bar = proto.Field(proto.STRING, number=1)
        baz = proto.Field(proto.INT64, number=2)

    spam = Spam(foo=Foo(bar="str", baz=42))
    assert spam.foo.bar == "str"
    assert spam.foo.baz == 42
    assert spam.eggs is False


def test_composite_forward_ref_with_package():
    sys.modules[__name__].__protobuf__ = proto.module(package="abc.def")
    try:

        class Spam(proto.Message):
            foo = proto.Field("Foo", number=1)

        class Eggs(proto.Message):
            foo = proto.Field("abc.def.Foo", number=1)

        class Foo(proto.Message):
            bar = proto.Field(proto.STRING, number=1)
            baz = proto.Field(proto.INT64, number=2)

    finally:
        del sys.modules[__name__].__protobuf__

    spam = Spam(foo=Foo(bar="str", baz=42))
    eggs = Eggs(foo=Foo(bar="rts", baz=24))
    assert spam.foo.bar == "str"
    assert spam.foo.baz == 42
    assert eggs.foo.bar == "rts"
    assert eggs.foo.baz == 24


def test_composite_backward_ref():
    class Foo(proto.Message):
        bar = proto.Field(proto.STRING, number=1)
        baz = proto.Field(proto.INT64, number=2)

    class Spam(proto.Message):
        foo = proto.Field(proto.MESSAGE, number=1, message=Foo)
        eggs = proto.Field(proto.BOOL, number=2)

    spam = Spam(foo=Foo(bar="str", baz=42))
    assert spam.foo.bar == "str"
    assert spam.foo.baz == 42
    assert spam.eggs is False


def test_composite_multi_ref():
    class Spam(proto.Message):
        foo = proto.Field(proto.MESSAGE, number=1, message="Foo")
        eggs = proto.Field(proto.BOOL, number=2)

    class Foo(proto.Message):
        bar = proto.Field(proto.STRING, number=1)
        baz = proto.Field(proto.INT64, number=2)

    class Bacon(proto.Message):
        foo = proto.Field(proto.MESSAGE, number=1, message=Foo)

    spam = Spam(foo=Foo(bar="str", baz=42))
    bacon = Bacon(foo=spam.foo)
    assert spam.foo.bar == "str"
    assert spam.foo.baz == 42
    assert spam.eggs is False
    assert bacon.foo == spam.foo


def test_composite_self_ref():
    class Spam(proto.Message):
        spam = proto.Field(proto.MESSAGE, number=1, message="Spam")
        eggs = proto.Field(proto.BOOL, number=2)

    spam = Spam(spam=Spam(eggs=True))
    assert spam.eggs is False
    assert spam.spam.eggs is True
    assert type(spam) is type(spam.spam)  # noqa: E0721
    assert not spam.spam.spam
    assert spam.spam.spam.eggs is False
    assert not spam.spam.spam.spam.spam.spam.spam.spam
