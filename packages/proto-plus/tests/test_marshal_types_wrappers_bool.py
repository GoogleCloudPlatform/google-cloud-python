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

from google.protobuf import wrappers_pb2

import proto
from proto.marshal.marshal import BaseMarshal


def test_bool_value_init():
    class Foo(proto.Message):
        bar = proto.Field(
            proto.MESSAGE,
            message=wrappers_pb2.BoolValue,
            number=1,
        )

    assert Foo(bar=True).bar is True
    assert Foo(bar=False).bar is False
    assert Foo().bar is None


def test_bool_value_init_dict():
    class Foo(proto.Message):
        bar = proto.Field(
            proto.MESSAGE,
            message=wrappers_pb2.BoolValue,
            number=1,
        )

    assert Foo({"bar": True}).bar is True
    assert Foo({"bar": False}).bar is False
    assert Foo({"bar": None}).bar is None


def test_bool_value_distinction_from_bool():
    class Foo(proto.Message):
        bar = proto.Field(
            proto.MESSAGE,
            message=wrappers_pb2.BoolValue,
            number=1,
        )
        baz = proto.Field(proto.BOOL, number=2)

    assert Foo().bar is None
    assert Foo().baz is False


def test_bool_value_rmw():
    class Foo(proto.Message):
        bar = proto.Field(wrappers_pb2.BoolValue, number=1)
        baz = proto.Field(wrappers_pb2.BoolValue, number=2)

    foo = Foo(bar=False)
    assert foo.bar is False
    assert foo.baz is None
    foo.baz = True
    assert foo.baz is True
    assert Foo.pb(foo).baz.value is True
    foo.bar = None
    assert foo.bar is None
    assert not Foo.pb(foo).HasField("bar")


def test_bool_value_write_bool_value():
    class Foo(proto.Message):
        bar = proto.Field(
            proto.MESSAGE,
            message=wrappers_pb2.BoolValue,
            number=1,
        )

    foo = Foo(bar=True)
    foo.bar = wrappers_pb2.BoolValue()
    assert foo.bar is False


def test_bool_value_del():
    class Foo(proto.Message):
        bar = proto.Field(
            proto.MESSAGE,
            message=wrappers_pb2.BoolValue,
            number=1,
        )

    foo = Foo(bar=False)
    assert foo.bar is False
    del foo.bar
    assert foo.bar is None


def test_multiple_types():
    class Foo(proto.Message):
        bar = proto.Field(wrappers_pb2.BoolValue, number=1)
        baz = proto.Field(wrappers_pb2.Int32Value, number=2)

    foo = Foo(bar=True, baz=42)
    assert foo.bar is True
    assert foo.baz == 42


def test_bool_value_to_python():
    # This path can never run in the current configuration because proto
    # values are the only thing ever saved, and `to_python` is a read method.
    #
    # However, we test idempotency for consistency with `to_proto` and
    # general resiliency.
    marshal = BaseMarshal()
    assert marshal.to_python(wrappers_pb2.BoolValue, True) is True
    assert marshal.to_python(wrappers_pb2.BoolValue, False) is False
    assert marshal.to_python(wrappers_pb2.BoolValue, None) is None
