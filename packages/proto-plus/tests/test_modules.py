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

import inspect
import sys
from unittest import mock

from google.protobuf import wrappers_pb2

import proto


def test_module_package():
    sys.modules[__name__].__protobuf__ = proto.module(package="spam.eggs.v1")
    try:

        class Foo(proto.Message):
            bar = proto.Field(proto.INT32, number=1)

        marshal = proto.Marshal(name="spam.eggs.v1")

        assert Foo.meta.package == "spam.eggs.v1"
        assert Foo.pb() in marshal._rules
    finally:
        del sys.modules[__name__].__protobuf__


def test_module_package_cross_api():
    sys.modules[__name__].__protobuf__ = proto.module(package="spam.eggs.v1")
    try:

        class Baz(proto.Message):
            foo = proto.RepeatedField(proto.INT64, number=1)

        marshal = proto.Marshal(name="spam.eggs.v1")

        assert Baz.meta.package == "spam.eggs.v1"
        assert Baz.pb() in marshal._rules

        sys.modules[__name__].__protobuf__ = proto.module(package="ham.pancakes.v1")

        class AnotherMessage(proto.Message):
            qux = proto.Field(proto.MESSAGE, number=1, message=Baz)

        marshal = proto.Marshal(name="ham.pancakes.v1")

        assert AnotherMessage.meta.package == "ham.pancakes.v1"
        assert AnotherMessage.pb() in marshal._rules
        # Confirm that Baz.pb() is no longer present in marshal._rules
        assert Baz.pb() not in marshal._rules

        # Test using multiple packages together
        # See https://github.com/googleapis/proto-plus-python/issues/349.
        msg = AnotherMessage(qux=Baz())
        assert type(msg) is AnotherMessage
    finally:
        del sys.modules[__name__].__protobuf__


def test_module_package_explicit_marshal():
    sys.modules[__name__].__protobuf__ = proto.module(
        package="spam.eggs.v1",
        marshal="foo",
    )
    try:

        class Foo(proto.Message):
            bar = proto.Field(proto.INT32, number=1)

        marshal = proto.Marshal(name="foo")

        assert Foo.meta.package == "spam.eggs.v1"
        assert Foo.pb() in marshal._rules
    finally:
        del sys.modules[__name__].__protobuf__


def test_module_manifest():
    __protobuf__ = proto.module(  # noqa: F841
        manifest={"Foo", "Bar", "Baz"},
        package="spam.eggs.v1",
    )

    # We want to fake a module, but modules have attribute access, and
    # `frame.f_locals` is a dictionary. Since we only actually care about
    # getattr, this is reasonably easy to shim over.
    frame = inspect.currentframe()
    with mock.patch.object(inspect, "getmodule") as getmodule:
        getmodule.side_effect = lambda *a: View(frame.f_locals)

        class Foo(proto.Message):
            a = proto.Field(wrappers_pb2.Int32Value, number=1)

        class Bar(proto.Message):
            b = proto.Field(proto.MESSAGE, number=1, message=Foo)

        assert not Foo.pb()
        assert not Bar.pb()

        class Baz(proto.Message):
            c = proto.Field(wrappers_pb2.BoolValue, number=1)

        assert Foo.pb()
        assert Bar.pb()
        assert Baz.pb()

        foo = Foo(a=12)
        bar = Bar(b=Foo(a=24))
        baz = Baz(c=False)
        assert foo.a == 12
        assert bar.b.a == 24
        assert baz.c is False


class View:
    """A view around a mapping, for attribute-like access."""

    def __init__(self, mapping):
        self._mapping = mapping

    def __getattr__(self, name):
        if name not in self._mapping:
            raise AttributeError
        return self._mapping[name]
